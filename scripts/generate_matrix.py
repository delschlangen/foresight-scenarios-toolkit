#!/usr/bin/env python3
"""
generate_matrix.py — render a 2x2 scenario matrix as Markdown from a JSON config.

Usage:
    python3 scripts/generate_matrix.py
        Renders scripts/scenarios_config.json (the AI governance example) to stdout.

    python3 scripts/generate_matrix.py --config my_scenarios.json
        Renders your own config to stdout.

    python3 scripts/generate_matrix.py --config my_scenarios.json --output my_matrix.md
        Writes the Markdown to a file instead of stdout.

Requires Python 3.8+ and nothing outside the standard library.
The script never writes anything except the file named by --output.

Config schema: see scripts/README.md.
"""

import argparse
import json
import sys
import textwrap
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_CONFIG = HERE / "scenarios_config.json"

QUADRANTS = ("top_left", "top_right", "bottom_left", "bottom_right")
REQUIRED_TOP_LEVEL = ("title", "axis_x", "axis_y", "scenarios")
REQUIRED_AXIS_X = ("name", "left", "right")
REQUIRED_AXIS_Y = ("name", "top", "bottom")
REQUIRED_SCENARIO = ("name", "tagline", "probability")

MIN_CELL_WIDTH = 17  # interior width of each quadrant cell in the ASCII matrix


class ConfigError(ValueError):
    """Raised when the config file is missing, malformed, or inconsistent."""


# ---------------------------------------------------------------------------
# Loading and validation
# ---------------------------------------------------------------------------

def load_config(path):
    """Load and validate a scenario config. Raises ConfigError on any problem."""
    path = Path(path)
    if not path.exists():
        raise ConfigError(
            f"Config file not found: {path}\n"
            f"Pass --config <file> or create {DEFAULT_CONFIG.name} next to this script."
        )
    try:
        config = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ConfigError(f"{path} is not valid JSON: {exc}") from exc
    validate_config(config)
    return config


def validate_config(config):
    """Check structure and that probabilities sum to 100. Raises ConfigError."""
    problems = []

    if not isinstance(config, dict):
        raise ConfigError("Config must be a JSON object at the top level.")

    for key in REQUIRED_TOP_LEVEL:
        if key not in config:
            problems.append(f"missing top-level key '{key}'")
    if problems:
        raise ConfigError("Invalid config:\n  - " + "\n  - ".join(problems))

    for key in REQUIRED_AXIS_X:
        if key not in config["axis_x"]:
            problems.append(f"axis_x is missing '{key}'")
    for key in REQUIRED_AXIS_Y:
        if key not in config["axis_y"]:
            problems.append(f"axis_y is missing '{key}'")

    scenarios = config["scenarios"]
    for quadrant in QUADRANTS:
        if quadrant not in scenarios:
            problems.append(f"scenarios is missing quadrant '{quadrant}'")
            continue
        for key in REQUIRED_SCENARIO:
            if key not in scenarios[quadrant]:
                problems.append(f"scenarios.{quadrant} is missing '{key}'")
        prob = scenarios[quadrant].get("probability")
        if prob is not None and (not isinstance(prob, (int, float)) or prob < 0 or prob > 100):
            problems.append(f"scenarios.{quadrant}.probability must be a number between 0 and 100 (got {prob!r})")

    if problems:
        raise ConfigError("Invalid config:\n  - " + "\n  - ".join(problems))

    total = sum(scenarios[q]["probability"] for q in QUADRANTS)
    if abs(total - 100) > 1e-9:
        breakdown = ", ".join(f"{scenarios[q]['name']} {scenarios[q]['probability']}%" for q in QUADRANTS)
        raise ConfigError(
            f"Scenario probabilities must sum to 100 (got {total:g}): {breakdown}.\n"
            f"Adjust the numbers so they total exactly 100."
        )


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

def wrap_label(text, width, max_lines=2):
    """Wrap a label into at most max_lines lines of at most width characters.

    Words are never broken. If the text still does not fit, the last line is
    truncated with an ellipsis so nothing is silently chopped mid-word.
    """
    lines = textwrap.wrap(text, width, break_long_words=False) or [""]
    if len(lines) > max_lines:
        lines = lines[: max_lines - 1] + [" ".join(lines[max_lines - 1 :])]
        if len(lines[-1]) > width:
            lines[-1] = lines[-1][: width - 1] + "…"
    return lines


def render_matrix_ascii(config):
    """Render the 2x2 matrix as box-drawing ASCII art.

    Cell width grows to fit the longest word in any scenario name, scenario
    names wrap onto two lines, and the axis row is padded so its centre cross
    lines up with the box for any pole-label length.
    """
    ax, ay, sc = config["axis_x"], config["axis_y"], config["scenarios"]

    names = [sc[q]["name"] for q in QUADRANTS]
    longest_word = max(len(word) for name in names for word in name.split()) if any(names) else 0
    inner = max(MIN_CELL_WIDTH, longest_word + 2)

    cells = {q: [line.center(inner) for line in wrap_label(sc[q]["name"], inner - 2)] for q in QUADRANTS}
    rows = max(len(lines) for lines in cells.values())
    for lines in cells.values():
        while len(lines) < rows:
            lines.append(" " * inner)

    left, right = ax["left"].upper(), ax["right"].upper()
    top, bottom = ay["top"].upper(), ay["bottom"].upper()

    margin = len(left) + 1          # space reserved for the left pole label
    pad = " " * margin
    cross = margin + 1 + inner      # column index of the vertical axis line

    blank_row = pad + "│" + " " * inner + "│" + " " * inner + "│"
    horizontal = "─" * inner

    out = []
    out.append(" " * max(0, cross - len(top) // 2) + top)
    out.append(" " * cross + "▲")
    out.append(" " * cross + "│")
    out.append(pad + "┌" + horizontal + "┼" + horizontal + "┐")
    out.append(blank_row)
    for i in range(rows):
        out.append(pad + "│" + cells["top_left"][i] + "│" + cells["top_right"][i] + "│")
    out.append(blank_row)
    out.append(left + " ◄" + horizontal + "┼" + horizontal + "► " + right)
    out.append(blank_row)
    for i in range(rows):
        out.append(pad + "│" + cells["bottom_left"][i] + "│" + cells["bottom_right"][i] + "│")
    out.append(blank_row)
    out.append(pad + "└" + horizontal + "┼" + horizontal + "┘")
    out.append(" " * cross + "│")
    out.append(" " * cross + "▼")
    out.append(" " * max(0, cross - len(bottom) // 2) + bottom)
    return "\n".join(out)


def render_markdown(config, config_name="config"):
    """Render the full Markdown document."""
    ax, ay, sc = config["axis_x"], config["axis_y"], config["scenarios"]
    lines = []

    lines.append(f"# Scenario Matrix: {config['title']}\n")
    if config.get("focal_question"):
        lines.append(f"**Focal Question:** {config['focal_question']}\n")
    if config.get("as_of"):
        lines.append(f"**Probabilities as of:** {config['as_of']}\n")
    if config.get("note"):
        lines.append(f"> {config['note']}\n")

    lines.append("## Axes\n")
    lines.append(f"**X-Axis:** {ax['name']}")
    lines.append(f"- Left: {ax['left']}")
    lines.append(f"- Right: {ax['right']}\n")
    lines.append(f"**Y-Axis:** {ay['name']}")
    lines.append(f"- Top: {ay['top']}")
    lines.append(f"- Bottom: {ay['bottom']}\n")

    lines.append("## Matrix\n")
    lines.append("```")
    lines.append(render_matrix_ascii(config))
    lines.append("```\n")

    lines.append("## Scenarios\n")
    lines.append("| Quadrant | Scenario | Tagline | Probability |")
    lines.append("|----------|----------|---------|-------------|")
    labels = {
        "top_left": f"{ax['left']} + {ay['top']}",
        "top_right": f"{ax['right']} + {ay['top']}",
        "bottom_left": f"{ax['left']} + {ay['bottom']}",
        "bottom_right": f"{ax['right']} + {ay['bottom']}",
    }
    for quadrant, label in labels.items():
        s = sc[quadrant]
        lines.append(f"| {label} | **{s['name']}** | {s['tagline']} | {s['probability']:g}% |")

    total = sum(sc[q]["probability"] for q in QUADRANTS)
    lines.append(f"\n*Total probability: {total:g}%*\n")
    lines.append("---")
    lines.append(f"*Generated by scripts/generate_matrix.py from {config_name}*")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser():
    parser = argparse.ArgumentParser(
        description="Render a 2x2 scenario matrix as Markdown from a JSON config.",
        epilog="Config schema and examples: scripts/README.md",
    )
    parser.add_argument(
        "--config", "-c", default=str(DEFAULT_CONFIG),
        help=f"path to a scenario config JSON (default: {DEFAULT_CONFIG.name} next to this script)",
    )
    parser.add_argument(
        "--output", "-o", default=None,
        help="write Markdown to this file instead of stdout",
    )
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        config = load_config(args.config)
    except ConfigError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    markdown = render_markdown(config, Path(args.config).name)

    if args.output:
        Path(args.output).write_text(markdown, encoding="utf-8")
        print(f"Matrix written to {args.output}", file=sys.stderr)
    else:
        sys.stdout.write(markdown)
    return 0


if __name__ == "__main__":
    sys.exit(main())
