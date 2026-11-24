# Changelog

All notable changes to this toolkit. Format follows [Keep a Changelog](https://keepachangelog.com/); versions follow [Semantic Versioning](https://semver.org/) loosely (major = method changes, minor = new content or features, patch = fixes).

## [1.2.0] - 2026-11-24

### Added
- `guides/runbook.md`: the whole method in one sitting with time boxes, templates and commands.
- `framework/probability_updates.md`: a worksheet for moving probabilities when indicators fire, with step sizes, cadence rules and a worked example from the December 2024 scan.
- `templates/probability_log_template.md`: auditable log of probability changes.
- `CHEATSHEET.md`: one-page quick reference.
- `FAQ.md`: common questions and an anti-pattern table.
- `scripts/README.md`: JSON schema, vocabulary, and the path from the Markdown templates to generated outputs.
- `scripts/test_generators.py` and a GitHub Actions workflow: generators are tested, and the committed examples, framework docs, README and site are checked for drift on every push.
- `examples/indicator_register.csv`: spreadsheet-ready export of the example register.
- Indicator **status** fields (Watching, Elevated, Fired, Retired) with last-reviewed and last-fired dates, in the config, the generated register, the framework register and the template.
- Environmental and Threat drivers in the worked example, so all six STEEP+T categories are populated (14 drivers).
- `CONTRIBUTING.md` and issue templates, including one for sharing adapted scenario sets.
- GitHub Pages site: a "Use the Toolkit" tab linking templates, guides and the decision framework; social-sharing metadata; deep-linkable tabs; accessible modal dialog.

### Changed
- `scripts/generate_matrix.py` and `scripts/generate_indicators.py` rewritten: `--config/--output/--csv/--help` flags, validation with clear errors (probabilities must sum to 100, missing keys reported together), no silent fallback to defaults, and **no write-back** into the repo. Scenario names wrap instead of truncating; the matrix aligns for any pole-label length. Unknown frequency or type values are listed with a warning instead of dropped.
- `framework/method.md` now describes five stages (adding Stage 5: Connect to Decisions) and a focal-question preamble, matching the README and the site.
- Indicator thresholds made measurable and aligned across `scripts/indicators_config.json`, `framework/indicators.md`, `examples/indicator_register.md` and `docs/index.html`.
- I-06 (major incidents) scheduled as Continuous everywhere; previously listed as Quarterly in two places.
- `examples/strategic_options.md` uses the scenario set's probabilities (20/15/45/20); expected values recomputed.
- `framework/contingency.md` worked example cites I-04 (not I-03) for US legislation; `examples/weekly_scan.md` Signal 1 no longer cites I-02.
- Every example document carries an explicit "example status / as of Q4 2024" note.
- `CITATION.cff` release date corrected to the first public commit (2025-12-24); version 1.2.0.
- README restructured: table of contents, accurate project tree and file inventory, corrected Quick Start, links to all new documents.
- Site fixes: indicator table scrolls horizontally on mobile instead of clipping; Y-axis pole labels visible and correctly ordered; tabs wrap on narrow screens; "tap for details" hint on touch devices.

### Removed
- `scripts/scenario_config.json` and `scripts/indicator_config.json`: orphaned configs with an incompatible schema that nothing loaded.
- Hard-coded default dictionaries inside the scripts (the JSON configs are now the single source of truth).

## [1.1.0] - 2025-12-25

### Added
- `framework/decisions.md` (decision framework), `framework/contingency.md` (playbooks).
- `guides/adaptation.md` (domain adaptation with an energy-transition example), `guides/facilitation.md` (workshop guide).
- `examples/strategic_options.md`.
- Blank templates: drivers, scenarios, indicators, weekly scan.
- GitHub Pages site with interactive 2x2 matrix (`docs/`).
- `CITATION.cff`, README badges and live-demo links.

### Changed
- Repository flattened so content lives at the root.
- `examples/weekly_scan.md` gained `source_type` and `action_required` fields.

## [1.0.0] - 2025-12-24

First public release. Core methodology, the AI governance worked example (drivers, uncertainties, four scenarios, ten indicators), generator scripts and example outputs. Content authored Q4 2024.
