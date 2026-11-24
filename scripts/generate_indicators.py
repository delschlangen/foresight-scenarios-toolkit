#!/usr/bin/env python3
"""
generate_indicators.py — render an indicator register (Markdown, optional CSV) from a JSON config.

Usage:
    python3 scripts/generate_indicators.py
        Renders scripts/indicators_config.json (the AI governance example) to stdout.

    python3 scripts/generate_indicators.py --config my_indicators.json
        Renders your own config to stdout.

    python3 scripts/generate_indicators.py --config my_indicators.json --output register.md --csv register.csv
        Writes Markdown and a flat CSV (for spreadsheets or BI tools).

Requires Python 3.8+ and nothing outside the standard library.
The script never writes anything except the files named by --output and --csv.

Config schema: see scripts/README.md.
"""

import argparse
import csv
import json
import sys
from collections import OrderedDict
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_CONFIG = HERE / "indicators_config.json"

REQUIRED_TOP_LEVEL = ("title", "indicators")
REQUIRED_INDICATOR = ("id", "signal", "source", "scenarios", "type", "frequency", "confidence", "threshold")
OPTIONAL_INDICATOR = ("status", "last_reviewed", "last_fired", "notes")

# Known vocabularies. Unknown values are still rendered (and warned about), never dropped.
KNOWN_FREQUENCIES = ("Continuous", "Daily", "Weekly", "Monthly", "Quarterly", "Annually")
KNOWN_TYPES = ("Leading", "Confirming", "Lagging")
KNOWN_STATUSES = ("Watching", "Elevated", "Fired", "Retired")

TYPE_PURPOSE = {
    "Leading": "Early warning signals",
    "Confirming": "Validates shift occurring",
    "Lagging": "Confirms after the fact",
}

CSV_COLUMNS = (
    "id", "signal", "source", "scenarios", "type", "frequency", "confidence",
    "threshold", "status", "last_reviewed", "last_fired", "notes",
)


class ConfigError(ValueError):
    """Raised when the config file is missing, malformed, or inconsistent."""


# ---------------------------------------------------------------------------
# Loading and validation
# ---------------------------------------------------------------------------

def load_config(path):
    """Load and validate an indicator config. Raises ConfigError on any problem."""
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
    """Check structure. Raises ConfigError listing every problem found."""
    problems = []

    if not isinstance(config, dict):
        raise ConfigError("Config must be a JSON object at the top level.")
    for key in REQUIRED_TOP_LEVEL:
        if key not in config:
            problems.append(f"missing top-level key '{key}'")
    if problems:
        raise ConfigError("Invalid config:\n  - " + "\n  - ".join(problems))

    indicators = config["indicators"]
    if not isinstance(indicators, list) or not indicators:
        raise ConfigError("'indicators' must be a non-empty list.")

    seen_ids = set()
    for position, ind in enumerate(indicators, 1):
        label = ind.get("id", f"#{position}") if isinstance(ind, dict) else f"#{position}"
        if not isinstance(ind, dict):
            problems.append(f"indicator {label} must be an object")
            continue
        for key in REQUIRED_INDICATOR:
            if key not in ind:
                problems.append(f"indicator {label} is missing '{key}'")
        if "scenarios" in ind and not isinstance(ind["scenarios"], list):
            problems.append(f"indicator {label}: 'scenarios' must be a list of scenario names")
        if "id" in ind:
            if ind["id"] in seen_ids:
                problems.append(f"duplicate indicator id '{ind['id']}'")
            seen_ids.add(ind["id"])

    if problems:
        raise ConfigError("Invalid config:\n  - " + "\n  - ".join(problems))


def warn_unknown_vocabulary(config, stream=sys.stderr):
    """Warn (do not fail) about frequency/type/status values outside the documented vocabulary."""
    for ind in config["indicators"]:
        for field, known in (("frequency", KNOWN_FREQUENCIES), ("type", KNOWN_TYPES), ("status", KNOWN_STATUSES)):
            value = ind.get(field)
            if value and canonical(value, known) is None:
                print(
                    f"warning: indicator {ind['id']} has {field}='{value}', which is not one of "
                    f"{', '.join(known)}. It is still listed, but check for a typo.",
                    file=stream,
                )


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def canonical(value, known):
    """Return the canonical spelling of value if it matches a known term (case-insensitive), else None."""
    needle = str(value).strip().lower()
    for term in known:
        if term.lower() == needle:
            return term
    return None


def group_by(indicators, field, known):
    """Group indicators by a field. Known values come first in canonical order; unknown values follow verbatim."""
    groups = OrderedDict((term, []) for term in known)
    extras = OrderedDict()
    for ind in indicators:
        raw = ind.get(field, "")
        term = canonical(raw, known)
        if term is not None:
            groups[term].append(ind)
        else:
            extras.setdefault(str(raw).strip() or "(unspecified)", []).append(ind)
    result = OrderedDict((k, v) for k, v in groups.items() if v)
    result.update(extras)
    return result


def ids(indicators):
    return ", ".join(ind["id"] for ind in indicators)


def dash(value):
    return value if value not in (None, "") else "—"


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

def render_markdown(config, config_name="config"):
    indicators = config["indicators"]
    has_status = any(ind.get(key) for ind in indicators for key in ("status", "last_reviewed", "last_fired"))
    lines = []

    lines.append(f"# {config['title']}\n")
    if config.get("focal_question"):
        lines.append(f"**Focal Question:** {config['focal_question']}\n")
    lines.append(f"**Last Updated:** {dash(config.get('updated'))}\n")
    if config.get("note"):
        lines.append(f"> {config['note']}\n")

    # Summary table
    lines.append("## Indicator Summary\n")
    if has_status:
        lines.append("| ID | Signal | Scenarios | Type | Frequency | Status | Last Reviewed |")
        lines.append("|----|--------|-----------|------|-----------|--------|---------------|")
    else:
        lines.append("| ID | Signal | Scenarios | Type | Frequency |")
        lines.append("|----|--------|-----------|------|-----------|")
    for ind in indicators:
        row = f"| {ind['id']} | {ind['signal']} | {', '.join(ind['scenarios'])} | {ind['type']} | {ind['frequency']} |"
        if has_status:
            row += f" {dash(ind.get('status'))} | {dash(ind.get('last_reviewed'))} |"
        lines.append(row)
    lines.append("")

    # Detailed indicators
    lines.append("## Detailed Indicators\n")
    for ind in indicators:
        lines.append(f"### {ind['id']}: {ind['signal']}\n")
        lines.append("| Attribute | Details |")
        lines.append("|-----------|---------|")
        lines.append(f"| **Source** | {ind['source']} |")
        lines.append(f"| **Linked Scenarios** | {', '.join(ind['scenarios'])} |")
        lines.append(f"| **Indicator Type** | {ind['type']} |")
        lines.append(f"| **Threshold** | {ind['threshold']} |")
        lines.append(f"| **Confidence** | {ind['confidence']} |")
        lines.append(f"| **Update Frequency** | {ind['frequency']} |")
        if has_status:
            lines.append(f"| **Status** | {dash(ind.get('status'))} |")
            lines.append(f"| **Last Reviewed** | {dash(ind.get('last_reviewed'))} |")
            lines.append(f"| **Last Fired** | {dash(ind.get('last_fired'))} |")
        if ind.get("notes"):
            lines.append(f"| **Notes** | {ind['notes']} |")
        lines.append("")

    # Monitoring schedule (grouped by whatever frequencies appear)
    lines.append("## Monitoring Schedule\n")
    lines.append("| Frequency | Indicators |")
    lines.append("|-----------|------------|")
    for freq, group in group_by(indicators, "frequency", KNOWN_FREQUENCIES).items():
        lines.append(f"| {freq} | {ids(group)} |")
    lines.append("")

    # By type
    lines.append("## Indicators by Type\n")
    lines.append("| Type | Purpose | Indicators |")
    lines.append("|------|---------|------------|")
    for type_name, group in group_by(indicators, "type", KNOWN_TYPES).items():
        lines.append(f"| {type_name} | {TYPE_PURPOSE.get(type_name, '—')} | {ids(group)} |")
    lines.append("")

    # Status summary
    if has_status:
        lines.append("## Status Summary\n")
        lines.append("| Status | Indicators |")
        lines.append("|--------|------------|")
        for status, group in group_by(indicators, "status", KNOWN_STATUSES).items():
            lines.append(f"| {status} | {ids(group)} |")
        lines.append("")

    lines.append("---")
    lines.append(f"*Generated by scripts/generate_indicators.py from {config_name}*")
    return "\n".join(lines) + "\n"


def write_csv(config, path):
    """Write one row per indicator. Lists are joined with '; '."""
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        for ind in config["indicators"]:
            row = {col: ind.get(col, "") for col in CSV_COLUMNS}
            row["scenarios"] = "; ".join(ind.get("scenarios", []))
            writer.writerow({k: ("" if v is None else v) for k, v in row.items()})


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser():
    parser = argparse.ArgumentParser(
        description="Render an indicator register as Markdown (and optionally CSV) from a JSON config.",
        epilog="Config schema and examples: scripts/README.md",
    )
    parser.add_argument(
        "--config", "-c", default=str(DEFAULT_CONFIG),
        help=f"path to an indicator config JSON (default: {DEFAULT_CONFIG.name} next to this script)",
    )
    parser.add_argument("--output", "-o", default=None, help="write Markdown to this file instead of stdout")
    parser.add_argument("--csv", default=None, help="also write a flat CSV of all indicators to this file")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        config = load_config(args.config)
    except ConfigError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    warn_unknown_vocabulary(config)
    markdown = render_markdown(config, Path(args.config).name)

    if args.output:
        Path(args.output).write_text(markdown, encoding="utf-8")
        print(f"Indicator register written to {args.output}", file=sys.stderr)
    else:
        sys.stdout.write(markdown)

    if args.csv:
        write_csv(config, args.csv)
        print(f"CSV written to {args.csv}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
