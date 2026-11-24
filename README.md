# Foresight Scenarios Toolkit

**Strategic foresight methodology for scenario planning, uncertainty analysis, and decision-making under ambiguity.**

[![Try It Live](https://img.shields.io/badge/Try%20It%20Live-Visit%20Site-blue?style=for-the-badge)](https://delschlangen.github.io/foresight-scenarios-toolkit)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![Cite This](https://img.shields.io/badge/Cite-CITATION.cff-orange?style=for-the-badge)](CITATION.cff)
[![CI](https://github.com/delschlangen/foresight-scenarios-toolkit/actions/workflows/ci.yml/badge.svg)](https://github.com/delschlangen/foresight-scenarios-toolkit/actions/workflows/ci.yml)

> **🚀 [Use this tool live →](https://delschlangen.github.io/foresight-scenarios-toolkit)** — No installation required. Try it in your browser.

A complete **scenario planning toolkit** for strategists, risk managers, and foresight practitioners. Build 2x2 scenario matrices, track leading indicators, stress-test strategies against multiple futures, and translate uncertainty into actionable decisions. Based on Shell's proven foresight methodology, with blank templates, a decision framework, a probability-update worksheet, and two dependency-free scripts.

**New here?** Read the [one-page cheat sheet](CHEATSHEET.md), then follow the [two-hour runbook](guides/runbook.md) from focal question to decisions.

---

## Contents

- [Who This Is For](#who-this-is-for)
- [What Makes This Different](#what-makes-this-different)
- [Quick Start](#quick-start)
- [What's Included](#whats-included)
- [The Methodology](#the-methodology)
- [Use Cases](#use-cases)
- [The AI Governance Example](#the-ai-governance-example)
- [Adapting for Your Domain](#adapting-for-your-domain)
- [Operational Rhythm](#operational-rhythm)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Contributing and Showcase](#contributing-and-showcase)
- [Live Demo](#live-demo)
- [Citation](#citation) · [License](#license)

---

## Who This Is For

| You Are | Your Problem | How This Helps |
|---------|--------------|----------------|
| **Strategy leader** | Board wants to see we've thought about uncertainty | Structured scenarios with probability tracking and a stress-test table |
| **Risk manager** | Current risk register assumes one future | Stress-test controls against four plausible worlds |
| **Policy advocate** | Need to argue for different regulatory approaches | Scenario-based framing with indicator evidence |
| **Startup founder** | Betting the company on assumptions about the future | Identify which assumptions matter most, and the robust moves |
| **Foresight practitioner** | Scenarios die in slide decks | An operational system: weekly scans, monthly updates, triggers, playbooks |

---

## What Makes This Different

Most scenario planning produces documents that gather dust. This toolkit is built around the step most methods skip, **connecting scenarios to decisions**, and around the rhythm that keeps them alive:

1. **Decision Framework** — Stress-test strategy, find robust moves, pre-commit to triggers ([`framework/decisions.md`](framework/decisions.md))
2. **Contingency Playbooks** — Pre-built responses with trigger conditions ([`framework/contingency.md`](framework/contingency.md))
3. **Indicator Tracking with Status** — Measurable thresholds and a Watching → Elevated → Fired status so "did it fire?" has an answer ([`framework/indicators.md`](framework/indicators.md))
4. **Probability Updates You Can Audit** — A worksheet with fixed step sizes and a log, instead of arguing over 32% vs 35% ([`framework/probability_updates.md`](framework/probability_updates.md))
5. **Workshop and Runbook** — A one-day facilitation guide for teams and a two-hour runbook for one person ([`guides/`](guides/))
6. **Templates and Scripts** — Blank forms for every stage, and scripts that render your matrix and register from JSON ([`templates/`](templates/), [`scripts/`](scripts/))

---

## Quick Start

Requires only a text editor. The two optional scripts need Python 3.8+ and nothing else; they never write files except the ones you name.

```bash
git clone https://github.com/delschlangen/foresight-scenarios-toolkit.git
cd foresight-scenarios-toolkit

# Render the AI governance example to the terminal
python3 scripts/generate_matrix.py
python3 scripts/generate_indicators.py

# Render your own configs (copy and edit the JSON files in scripts/ first)
python3 scripts/generate_matrix.py     --config my_scenarios.json  --output my_matrix.md
python3 scripts/generate_indicators.py --config my_indicators.json --output my_register.md --csv my_register.csv
```

Then open [`guides/runbook.md`](guides/runbook.md) and work through the six steps. Schema and vocabulary for the JSON configs: [`scripts/README.md`](scripts/README.md).

---

## What's Included

### Framework (`framework/`)

The method, and the AI governance worked example carried through every stage.

| Document | Purpose |
|----------|---------|
| [`method.md`](framework/method.md) | Five-stage methodology, from focal question to decisions |
| [`drivers.md`](framework/drivers.md) | Example: 14 drivers across all six STEEP+T categories, scored and prioritized |
| [`uncertainties.md`](framework/uncertainties.md) | How the two axes were chosen, and which were rejected |
| [`scenarios.md`](framework/scenarios.md) | Four complete scenario narratives |
| [`indicators.md`](framework/indicators.md) | Ten indicators with measurable thresholds, a status log, and a monitoring schedule |
| [`decisions.md`](framework/decisions.md) | Stress-testing, robust moves, decision triggers, decision rules |
| [`contingency.md`](framework/contingency.md) | Playbook structure, worked playbook, activation checklist |
| [`probability_updates.md`](framework/probability_updates.md) | Cadence rules and a worksheet for moving probabilities when indicators fire |

### Guides (`guides/`)

| Guide | Purpose |
|-------|---------|
| [`runbook.md`](guides/runbook.md) | The whole method in one sitting: time boxes, templates, commands, checklist |
| [`facilitation.md`](guides/facilitation.md) | One-day workshop agenda, facilitator scripts, remote adaptations |
| [`adaptation.md`](guides/adaptation.md) | Applying the method to any domain, with a complete energy-transition example |

### Templates (`templates/`)

Blank forms with `[FILL IN]` placeholders and hints in comments.

| Template | Purpose |
|----------|---------|
| [`drivers_template.md`](templates/drivers_template.md) | Driver analysis across STEEP+T; prioritization matrix; axis selection |
| [`scenario_template.md`](templates/scenario_template.md) | Scenario narratives, comparison matrix, probabilities, quality checklist |
| [`indicator_template.md`](templates/indicator_template.md) | Indicator register with thresholds, status fields, source library |
| [`weekly_scan_template.md`](templates/weekly_scan_template.md) | 30-minute horizon scan with source types and action tracking |
| [`probability_log_template.md`](templates/probability_log_template.md) | Auditable record of probability changes and the indicators behind them |

### Scripts (`scripts/`)

Standard-library Python. Tested; CI runs the tests on every push.

| File | Purpose |
|------|---------|
| [`generate_matrix.py`](scripts/generate_matrix.py) | Renders a 2x2 matrix from JSON; validates that probabilities sum to 100; wraps long names |
| [`generate_indicators.py`](scripts/generate_indicators.py) | Renders an indicator register and optional CSV; groups by frequency, type, status |
| [`scenarios_config.json`](scripts/scenarios_config.json), [`indicators_config.json`](scripts/indicators_config.json) | The example configs; copy these to start your own |
| [`README.md`](scripts/README.md) | JSON schema, accepted vocabulary, writing measurable thresholds, templates-to-config mapping |

### Examples (`examples/`)

| File | Description |
|------|-------------|
| [`scenario_matrix.md`](examples/scenario_matrix.md) | Generated 2x2 with probabilities |
| [`indicator_register.md`](examples/indicator_register.md), [`indicator_register.csv`](examples/indicator_register.csv) | Generated register (Markdown and spreadsheet-ready CSV) |
| [`weekly_scan.md`](examples/weekly_scan.md) | A completed horizon scan with six signals |
| [`strategic_options.md`](examples/strategic_options.md) | Eight strategic options scored across four scenarios: robustness, expected value, triggers |

### Reference

| File | Purpose |
|------|---------|
| [`CHEATSHEET.md`](CHEATSHEET.md) | The whole method on one page |
| [`FAQ.md`](FAQ.md) | Why four scenarios, how to brief a board, what stale looks like, anti-patterns |
| [`CHANGELOG.md`](CHANGELOG.md) | What changed in each version |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | How to share a scenario set, report an inconsistency, or improve the content |
| [`docs/`](docs/) | The GitHub Pages site: interactive matrix, drivers, indicators, methodology, and a "Use the Toolkit" tab |

---

## The Methodology

```
FOCAL QUESTION → DRIVERS → UNCERTAINTIES → SCENARIOS → INDICATORS → DECISIONS
                    ↓            ↓             ↓            ↓            ↓
                10-15 forces   2 axes       4 worlds    8-12 signals  Stress-test,
                scored         selected     developed   with status   robust moves,
                                                                      triggers
```

**Before you start:** write the focal question. *For [organization], what strategy should we pursue regarding [decision area] over [horizon], given uncertainty about [factors]?*

**Stage 1: Identify Drivers** — Map 10-15 forces shaping your focal question using the STEEP+T framework; score each for impact and uncertainty.

**Stage 2: Select Uncertainties** — Choose two high-impact, high-uncertainty, *independent* drivers as scenario axes. Frame them as spectra.

**Stage 3: Build Scenarios** — Develop four narrative futures, one per quadrant. Each has winners and losers. Probabilities sum to 100.

**Stage 4: Define Indicators** — Create 8-12 early-warning signals with thresholds two analysts would agree have been crossed.

**Stage 5: Connect to Decisions** — Stress-test strategy, find robust moves, pre-commit to triggers, build contingency playbooks.

Then run the rhythm: weekly scan, monthly probability update, quarterly scenario review, annual rebuild. Full detail in [`framework/method.md`](framework/method.md); one-page version in [`CHEATSHEET.md`](CHEATSHEET.md).

---

## Use Cases

### Use Case 1: Strategic Planning

**Situation:** Annual strategy refresh; the board wants assurance that multiple futures were considered.

**How to Use:** Run a workshop with [`guides/facilitation.md`](guides/facilitation.md). Test current strategy against all four scenarios using the stress-test table in [`framework/decisions.md`](framework/decisions.md). Identify robust moves; set contingency triggers.

**Deliverable:** Strategy document with a scenario stress-test section. See [`examples/strategic_options.md`](examples/strategic_options.md) for the shape of it.

### Use Case 2: Investment Decision

**Situation:** Major capital allocation with a 5+ year horizon.

**How to Use:** Define the focal question around the decision. Build scenarios around the key uncertainties. Score the options under each scenario and compute probability-weighted and minimum (robustness) values, as in [`examples/strategic_options.md`](examples/strategic_options.md). Set decision triggers: "If scenario X exceeds 40%, we [action]."

**Deliverable:** Investment memo with scenario-weighted analysis.

### Use Case 3: Policy Advocacy

**Situation:** Advocating for a regulatory approach to an emerging technology.

**How to Use:** Build scenarios showing different regulatory futures. Identify which aligns with your preferred policy. Develop indicator-based arguments: "Early signs (I-03, I-05) suggest [scenario], which supports [policy]." Prepare positions for the alternatives.

**Deliverable:** Policy brief with scenario-based framing.

### Use Case 4: Risk Management

**Situation:** The enterprise risk register assumes a single future.

**How to Use:** Map current risks to scenario likelihoods. Identify scenario-specific risks not currently tracked. Stress-test controls against each scenario. Add scenario probability to risk weighting.

**Deliverable:** Enhanced risk register with scenario overlays.

### Use Case 5: Ongoing Horizon Scanning

**Situation:** Leadership wants regular updates on the strategic environment.

**How to Use:** Set up the register from [`templates/indicator_template.md`](templates/indicator_template.md). Run weekly 30-minute scans ([`templates/weekly_scan_template.md`](templates/weekly_scan_template.md)). Move probabilities monthly with the worksheet in [`framework/probability_updates.md`](framework/probability_updates.md). Trigger a strategic review when a threshold is crossed.

**Deliverable:** Weekly scan memo, monthly probability log, quarterly dashboard.

---

## The AI Governance Example

The worked example runs the full method on AI governance, 2024-2030.

> **As of Q4 2024.** The example was authored in late 2024 and is deliberately kept as a dated baseline, so you can see what a complete set looks like and practise the refresh process on it. Every example document carries an explicit status note.

**Focal Question:** How will AI governance evolve, and what does that mean for strategy?

**Axes:** AI Capability (Incremental ↔ Discontinuous) and Global Regulation (Fragmented ↔ Harmonized)

| Scenario | Quadrant | Baseline probability |
|----------|----------|----------------------|
| **Coordinated Caution** | Incremental + Harmonized | 20% |
| **Emergency Coordination** | Discontinuous + Harmonized | 15% |
| **Patchwork Progress** | Incremental + Fragmented | 45% |
| **Fragmented Scramble** | Discontinuous + Fragmented | 20% |

Fourteen drivers, ten indicators with status, a completed weekly scan, a worked contingency playbook, and a full strategic-options analysis. Explore it interactively on the [live site](https://delschlangen.github.io/foresight-scenarios-toolkit).

---

## Adapting for Your Domain

The methodology applies to any strategic foresight need. [`guides/adaptation.md`](guides/adaptation.md) gives step-by-step instructions with a second complete worked example (energy transition for an oil and gas company).

**Domains this works for:** geopolitical risk · technology adoption and disruption · market and competitive dynamics · regulatory landscapes · climate and sustainability futures · supply chain resilience · workforce evolution

Built a set in a new domain? Add it to the [showcase](CONTRIBUTING.md#showcase).

---

## Operational Rhythm

| Frequency | Activity | Time | Output | Probabilities |
|-----------|----------|------|--------|---------------|
| Weekly | Indicator scan; update indicator status | 30 min | Signal log | Do not move |
| Monthly | Probability worksheet; check triggers | 1-2 hrs | Probability log entry | Move, with step sizes |
| Quarterly | Deep scenario review; playbook maintenance | Half day | Narrative updates if needed | Re-baseline if the set changes |
| Annually | Full reassessment of drivers and axes | 1-2 days | Refreshed scenario set | New baseline |

Why the weekly scan does not move probabilities, and how the monthly review does: [`framework/probability_updates.md`](framework/probability_updates.md).

---

## Project Structure

```
foresight-scenarios-toolkit/
├── README.md                   # This file
├── CHEATSHEET.md               # One-page quick reference
├── FAQ.md                      # Questions and anti-patterns
├── CHANGELOG.md
├── CONTRIBUTING.md             # Including the showcase of adapted scenario sets
├── CITATION.cff
├── LICENSE
├── framework/
│   ├── method.md               # Five-stage methodology
│   ├── drivers.md              # Example: 14 drivers
│   ├── uncertainties.md        # Example: axis selection
│   ├── scenarios.md            # Example: four narratives
│   ├── indicators.md           # Example: register with status log
│   ├── decisions.md            # Decision framework
│   ├── contingency.md          # Contingency playbooks
│   └── probability_updates.md  # Probability update worksheet
├── guides/
│   ├── runbook.md              # End-to-end in one sitting
│   ├── facilitation.md         # Workshop guide
│   └── adaptation.md           # Domain adaptation + energy example
├── templates/
│   ├── drivers_template.md
│   ├── scenario_template.md
│   ├── indicator_template.md
│   ├── weekly_scan_template.md
│   └── probability_log_template.md
├── scripts/
│   ├── README.md               # Config schema and vocabulary
│   ├── generate_matrix.py
│   ├── generate_indicators.py
│   ├── scenarios_config.json
│   ├── indicators_config.json
│   └── test_generators.py      # Generator and consistency tests
├── examples/
│   ├── scenario_matrix.md      # Generated
│   ├── indicator_register.md   # Generated
│   ├── indicator_register.csv  # Generated
│   ├── weekly_scan.md
│   └── strategic_options.md
├── docs/                       # GitHub Pages site
│   ├── index.html
│   ├── styles.css
│   └── app.js
└── .github/
    ├── workflows/ci.yml
    └── ISSUE_TEMPLATE/
```

---

## Getting Started

**Fastest path: the runbook.** [`guides/runbook.md`](guides/runbook.md) takes you from focal question to a first stress-test in about two hours, pointing at the right template and command at each step.

**Option A: Learn the methodology.** Read [`framework/method.md`](framework/method.md), then follow the AI governance example across `framework/*.md`, finishing with [`framework/decisions.md`](framework/decisions.md) and [`examples/strategic_options.md`](examples/strategic_options.md).

**Option B: Run a workshop.** Start with [`guides/facilitation.md`](guides/facilitation.md); use [`guides/adaptation.md`](guides/adaptation.md) for non-AI domains.

**Option C: Set up ongoing scanning.** Define your indicators in a copy of [`scripts/indicators_config.json`](scripts/indicators_config.json), render the register with `generate_indicators.py --config`, and start the weekly rhythm with [`templates/weekly_scan_template.md`](templates/weekly_scan_template.md).

**Option D: Build from templates.** Copy the files in [`templates/`](templates/) to your working directory and fill in the placeholders; each template ends with a "Next Step" pointing to the following one.

---

## Contributing and Showcase

The most useful contribution is evidence the method works somewhere new. If you built a scenario set with this toolkit, open an issue with the **Share a scenario set** template and it will be listed in the [showcase](CONTRIBUTING.md#showcase). Inconsistencies, fixes, and new worked examples are welcome too; see [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

## Live Demo

Use this tool directly in your browser: **https://delschlangen.github.io/foresight-scenarios-toolkit**

No installation or dependencies required.

---

## References

- Schwartz, P. (1991). *The Art of the Long View*
- Shell Scenarios Team. *Scenarios: An Explorer's Guide*
- Wilkinson, A. & Kupers, R. (2014). *The Essence of Scenarios*
- IFTF. *Foresight Toolkit*

---

## Citation

If you use this toolkit in your research or work, please cite it:

```bibtex
@software{schlangen2025foresight,
  author  = {Schlangen, Del},
  title   = {Foresight Scenarios Toolkit},
  year    = {2025},
  version = {1.2.0},
  url     = {https://github.com/delschlangen/foresight-scenarios-toolkit}
}
```

See [CITATION.cff](CITATION.cff) for full citation metadata.

---

## License

This project is licensed under the **MIT License** — you are free to use, modify, and distribute this toolkit for any purpose. See [LICENSE](LICENSE) for details.

---

*Built by [Del Schlangen](https://linkedin.com/in/del-s-759557175/) · [ORCID](https://orcid.org/0009-0005-5116-9564)*
