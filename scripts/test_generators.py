#!/usr/bin/env python3
"""
Tests for the generator scripts and for drift between the config files, the
committed examples, the framework docs, the README and the GitHub Pages site.

Run from the repo root:
    python3 -m unittest discover -s scripts -p "test_*.py" -v

Standard library only.
"""

import io
import json
import re
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stderr
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

import generate_indicators as gi  # noqa: E402
import generate_matrix as gm  # noqa: E402

SCENARIOS_CONFIG = HERE / "scenarios_config.json"
INDICATORS_CONFIG = HERE / "indicators_config.json"
MATRIX_EXAMPLE = ROOT / "examples" / "scenario_matrix.md"
REGISTER_EXAMPLE = ROOT / "examples" / "indicator_register.md"
REGISTER_CSV_EXAMPLE = ROOT / "examples" / "indicator_register.csv"
SITE_INDEX = ROOT / "docs" / "index.html"
FRAMEWORK_INDICATORS = ROOT / "framework" / "indicators.md"
README = ROOT / "README.md"


def read(path):
    return path.read_text(encoding="utf-8")


def normalize(text):
    return "\n".join(line.rstrip() for line in text.strip().splitlines())


class MatrixGeneratorTests(unittest.TestCase):
    def setUp(self):
        self.config = gm.load_config(SCENARIOS_CONFIG)

    def test_default_config_is_valid(self):
        gm.validate_config(self.config)

    def test_committed_example_matches_generator(self):
        """examples/scenario_matrix.md must be exactly what the generator produces today."""
        generated = gm.render_markdown(self.config, SCENARIOS_CONFIG.name)
        self.assertEqual(
            normalize(read(MATRIX_EXAMPLE)), normalize(generated),
            "examples/scenario_matrix.md is stale. Regenerate with:\n"
            "  python3 scripts/generate_matrix.py --output examples/scenario_matrix.md",
        )

    def test_scenario_names_are_not_truncated(self):
        art = gm.render_matrix_ascii(self.config)
        for quadrant in gm.QUADRANTS:
            for word in self.config["scenarios"][quadrant]["name"].split():
                self.assertIn(word, art, f"'{word}' missing from ASCII matrix")

    def test_axis_row_aligns_with_box_for_long_labels(self):
        config = json.loads(json.dumps(self.config))
        config["axis_x"]["left"] = "Gradual Transition"
        config["axis_x"]["right"] = "Rapid Transition"
        config["scenarios"]["top_right"]["name"] = "Green Acceleration"
        art = gm.render_matrix_ascii(config).splitlines()
        cross_columns = {line.index("┼") for line in art if "┼" in line}
        self.assertEqual(len(cross_columns), 1, f"centre cross drifts between rows: {cross_columns}")
        box_rows = [line for line in art if line.count("│") == 3]  # left wall, divider, right wall
        self.assertGreaterEqual(len(box_rows), 6)
        self.assertEqual(len({len(line) for line in box_rows}), 1, "box rows have ragged widths")

    def test_probabilities_must_sum_to_100(self):
        config = json.loads(json.dumps(self.config))
        config["scenarios"]["top_left"]["probability"] = 50
        with self.assertRaises(gm.ConfigError) as ctx:
            gm.validate_config(config)
        self.assertIn("sum to 100", str(ctx.exception))

    def test_missing_config_file_is_an_error(self):
        with self.assertRaises(gm.ConfigError):
            gm.load_config(HERE / "does_not_exist.json")

    def test_missing_keys_are_reported_together(self):
        config = json.loads(json.dumps(self.config))
        del config["scenarios"]["top_left"]["tagline"]
        del config["axis_y"]["bottom"]
        with self.assertRaises(gm.ConfigError) as ctx:
            gm.validate_config(config)
        message = str(ctx.exception)
        self.assertIn("tagline", message)
        self.assertIn("bottom", message)

    def test_cli_does_not_write_into_the_repo(self):
        """Running with no arguments (as the README shows) must leave the checkout untouched."""
        before = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT, capture_output=True, text=True).stdout
        subprocess.run([sys.executable, str(HERE / "generate_matrix.py")], cwd=ROOT, capture_output=True, check=True)
        subprocess.run([sys.executable, str(HERE / "generate_indicators.py")], cwd=ROOT, capture_output=True, check=True)
        after = subprocess.run(["git", "status", "--porcelain"], cwd=ROOT, capture_output=True, text=True).stdout
        self.assertEqual(before, after, "a generator modified tracked files as a side effect")

    def test_cli_bad_config_exits_nonzero(self):
        result = subprocess.run(
            [sys.executable, str(HERE / "generate_matrix.py"), "--config", "/definitely/missing.json"],
            capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("not found", result.stderr)


class IndicatorGeneratorTests(unittest.TestCase):
    def setUp(self):
        self.config = gi.load_config(INDICATORS_CONFIG)

    def test_default_config_is_valid(self):
        gi.validate_config(self.config)

    def test_committed_example_matches_generator(self):
        generated = gi.render_markdown(self.config, INDICATORS_CONFIG.name)
        self.assertEqual(
            normalize(read(REGISTER_EXAMPLE)), normalize(generated),
            "examples/indicator_register.md is stale. Regenerate with:\n"
            "  python3 scripts/generate_indicators.py --output examples/indicator_register.md "
            "--csv examples/indicator_register.csv",
        )

    def test_committed_csv_matches_generator(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "reg.csv"
            gi.write_csv(self.config, out)
            self.assertEqual(normalize(read(REGISTER_CSV_EXAMPLE)), normalize(read(out)),
                             "examples/indicator_register.csv is stale; regenerate it.")

    def test_unknown_frequency_is_listed_not_dropped(self):
        config = json.loads(json.dumps(self.config))
        config["indicators"][0]["frequency"] = "Daily-ish"
        config["indicators"][0]["type"] = "Coincident"
        markdown = gi.render_markdown(config)
        self.assertRegex(markdown, r"\| Daily-ish \| I-01")
        self.assertRegex(markdown, r"\| Coincident \| — \| I-01")

    def test_unknown_vocabulary_warns_on_stderr(self):
        config = json.loads(json.dumps(self.config))
        config["indicators"][1]["frequency"] = "Fortnightly"
        buffer = io.StringIO()
        gi.warn_unknown_vocabulary(config, stream=buffer)
        self.assertIn("Fortnightly", buffer.getvalue())

    def test_case_insensitive_grouping(self):
        config = json.loads(json.dumps(self.config))
        config["indicators"][0]["frequency"] = "weekly"
        markdown = gi.render_markdown(config)
        self.assertRegex(markdown, r"\| Weekly \| I-01, I-02 \|")

    def test_duplicate_ids_rejected(self):
        config = json.loads(json.dumps(self.config))
        config["indicators"][1]["id"] = config["indicators"][0]["id"]
        with self.assertRaises(gi.ConfigError):
            gi.validate_config(config)

    def test_csv_has_one_row_per_indicator(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "reg.csv"
            gi.write_csv(self.config, out)
            lines = read(out).strip().splitlines()
            self.assertEqual(len(lines), len(self.config["indicators"]) + 1)
            self.assertTrue(lines[0].startswith("id,signal,source,scenarios,type,frequency"))


class CrossFileConsistencyTests(unittest.TestCase):
    """Guards against the example drifting between config, framework docs, README and the site."""

    @classmethod
    def setUpClass(cls):
        cls.scenarios = gm.load_config(SCENARIOS_CONFIG)
        cls.indicators = gi.load_config(INDICATORS_CONFIG)
        cls.site = read(SITE_INDEX)
        cls.framework_indicators = read(FRAMEWORK_INDICATORS)
        cls.readme = read(README)

    def test_site_shows_every_scenario_with_its_probability(self):
        for quadrant in gm.QUADRANTS:
            scenario = self.scenarios["scenarios"][quadrant]
            self.assertIn(scenario["name"], self.site)
            self.assertIn(f"{scenario['probability']:g}%", self.site)

    def test_site_lists_every_indicator_with_matching_threshold_and_frequency(self):
        for ind in self.indicators["indicators"]:
            self.assertIn(ind["id"], self.site, f"{ind['id']} missing from docs/index.html")
            self.assertIn(ind["threshold"], self.site,
                          f"docs/index.html threshold for {ind['id']} differs from scripts/indicators_config.json")

    def test_site_monitoring_schedule_matches_config(self):
        groups = gi.group_by(self.indicators["indicators"], "frequency", gi.KNOWN_FREQUENCIES)
        for frequency, group in groups.items():
            expected = gi.ids(group)
            self.assertIn(expected, self.site,
                          f"docs/index.html monitoring schedule for {frequency} should read '{expected}'")

    def test_framework_register_covers_every_indicator(self):
        for ind in self.indicators["indicators"]:
            self.assertIn(f"{ind['id']}:", self.framework_indicators, f"{ind['id']} missing from framework/indicators.md")

    def test_framework_monitoring_schedule_matches_config(self):
        groups = gi.group_by(self.indicators["indicators"], "frequency", gi.KNOWN_FREQUENCIES)
        for frequency, group in groups.items():
            self.assertIn(gi.ids(group), self.framework_indicators,
                          f"framework/indicators.md schedule for {frequency} should read '{gi.ids(group)}'")

    def test_readme_mentions_every_user_facing_file(self):
        """Every doc, template, example and script must be discoverable from the README."""
        tracked = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True).stdout.split()
        user_facing = [
            path for path in tracked
            if path.startswith(("framework/", "guides/", "templates/", "examples/", "scripts/"))
            and not path.startswith("scripts/test_")
        ]
        missing = [path for path in user_facing if Path(path).name not in self.readme]
        self.assertEqual(missing, [], f"README.md does not mention: {missing}")

    def test_readme_probabilities_match_config(self):
        """If the README states the example probabilities, they must match the config."""
        for quadrant in gm.QUADRANTS:
            scenario = self.scenarios["scenarios"][quadrant]
            pattern = re.compile(re.escape(scenario["name"]) + r"[^\n|]*?\|\s*(\d+)%")
            for match in pattern.finditer(self.readme):
                self.assertEqual(int(match.group(1)), scenario["probability"],
                                 f"README probability for {scenario['name']} disagrees with config")


if __name__ == "__main__":
    unittest.main()
