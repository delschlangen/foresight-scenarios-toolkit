# foresight-scenarios-toolkit

**Structured strategic foresight methodology for emerging technology risk.**

A complete framework for building scenarios, tracking indicators, and operationalizing horizon scanning—adapted for AI governance and emerging tech.

## Why This Exists

Foresight that lives in slide decks doesn't inform decisions. This toolkit provides a repeatable methodology that connects driver analysis → scenario building → indicator tracking → weekly operations. Built from experience running a foresight program at a Fortune 50 company, producing 50+ strategic reports on emerging technology risk.

## Quick Start

```bash
# Clone
git clone https://github.com/delschlangen/foresight-scenarios-toolkit.git
cd foresight-scenarios-toolkit

# Generate a scenario matrix
python scripts/generate_matrix.py

# Generate an indicator register  
python scripts/generate_indicators.py

# See example outputs
cat examples/scenario_matrix.md
cat examples/weekly_scan.md
```

## What's Included

### Framework Documentation (`framework/`)

| Document | Purpose |
|----------|---------|
| `method.md` | Four-stage foresight methodology |
| `drivers.md` | Example driver analysis (AI governance) |
| `uncertainties.md` | Critical uncertainty selection |
| `scenarios.md` | Four complete scenario narratives |
| `indicators.md` | Indicator register with 10 signals |

### Methodology Overview

```
DRIVERS → UNCERTAINTIES → SCENARIOS → INDICATORS
   ↓            ↓             ↓            ↓
 12 forces   2 axes       4 worlds    10 signals
 analyzed    selected     developed   monitored
```

### Scripts (`scripts/`)

| Script | Purpose |
|--------|---------|
| `generate_matrix.py` | Creates 2x2 scenario matrix from JSON config |
| `generate_indicators.py` | Creates indicator register from JSON config |

Both scripts include default configurations and output Markdown.

### Examples (`examples/`)

| File | Description |
|------|-------------|
| `scenario_matrix.md` | Generated 2x2 matrix with probabilities |
| `indicator_register.md` | Generated monitoring register |
| `weekly_scan.md` | Sample horizon scan output with 6 signals |

## Sample Output: Weekly Scan

```markdown
| # | Signal | Scenario Impact | Confidence |
|---|--------|-----------------|------------|
| 1 | Anthropic releases expanded agentic capabilities | Incremental+ | High |
| 2 | EU AI Office announces enforcement priorities | Patchwork Progress | High |
| 3 | Bipartisan AI bill stalls in Senate | Patchwork Progress | High |
| 4 | China announces AI chip progress | Fragmented Scramble | Medium |
```

## Project Structure

```
foresight-scenarios-toolkit/
├── framework/
│   ├── method.md           # Core methodology
│   ├── drivers.md          # Driver analysis (AI governance example)
│   ├── uncertainties.md    # Critical uncertainty selection
│   ├── scenarios.md        # Four scenario narratives
│   └── indicators.md       # Indicator register
├── scripts/
│   ├── generate_matrix.py  # Matrix generator
│   ├── generate_indicators.py
│   ├── scenarios_config.json
│   └── indicators_config.json
├── examples/
│   ├── scenario_matrix.md  # Generated matrix
│   ├── indicator_register.md
│   └── weekly_scan.md      # Sample horizon scan
├── README.md
└── LICENSE
```

## Adapting for Your Domain

The included example focuses on AI governance, but the methodology applies to any strategic foresight need:

1. **Replace drivers** in `drivers.md` with your domain's key forces
2. **Select new uncertainties** that matter for your focal question
3. **Build scenarios** using the 2x2 framework
4. **Define indicators** specific to your scenarios
5. **Customize configs** in `scripts/` for your content

**Other domains this works for:**
- Geopolitical risk
- Technology adoption curves  
- Market/competitive dynamics
- Regulatory landscapes
- Climate/sustainability futures

## Operational Rhythm

| Frequency | Activity | Output |
|-----------|----------|--------|
| Weekly | Horizon scan | `weekly_scan.md` |
| Monthly | Indicator review | Updated probabilities |
| Quarterly | Scenario refresh | Revised narratives if needed |
| Annually | Full reassessment | New driver analysis |

## Next Steps

- [ ] Add web scraping for automated signal collection
- [ ] Build dashboard for indicator tracking
- [ ] Add scenario stress-testing templates
- [ ] Create facilitation guide for workshops

## References

- Schwartz, P. (1991). *The Art of the Long View*
- Shell Scenarios Team. *Scenarios: An Explorer's Guide*
- IFTF. *Foresight Toolkit*

## License

MIT License — See [LICENSE](LICENSE)

---

*Built by Del Schlangen | [LinkedIn](https://linkedin.com/in/del-s-759557175/)*
