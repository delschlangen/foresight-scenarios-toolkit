# Foresight Scenarios Toolkit

**A complete system for turning strategic uncertainty into better decisions.**

This isn't just another scenario planning guide. It's an operational toolkit that takes you from "we should think about the future" to "here's what we're doing about it."

---

## Who This Is For

| You Are | Your Problem | How This Helps |
|---------|--------------|----------------|
| **Strategy leader** | Board wants to see we've thought about uncertainty | Structured scenarios with probability tracking |
| **Risk manager** | Current risk register assumes one future | Stress-test against multiple plausible worlds |
| **Policy advocate** | Need to argue for different regulatory approaches | Scenario-based framing for stakeholder engagement |
| **Startup founder** | Betting the company on assumptions about the future | Identify which assumptions matter most |
| **Foresight practitioner** | Scenarios die in slide decks | Operational system that keeps scenarios alive |

---

## What Makes This Different

Most scenario planning produces nice documents that gather dust. This toolkit solves that with:

1. **Decision Framework** — Explicit methods to translate scenarios into strategic choices
2. **Indicator Tracking** — Early warning system to detect which scenario is emerging
3. **Contingency Playbooks** — Pre-developed responses so you can move fast
4. **Weekly Operations** — 30-minute scanning rhythm that keeps scenarios current
5. **Workshop Guides** — Step-by-step facilitation for running sessions

---

## Quick Start

```bash
# Clone the repo
git clone https://github.com/delschlangen/foresight-scenarios-toolkit.git
cd foresight-scenarios-toolkit

# Generate outputs from the AI governance example
python scripts/generate_matrix.py
python scripts/generate_indicators.py

# See example weekly scan
cat examples/weekly_scan.md
```

---

## What's Included

### Framework (`framework/`)

| Document | Purpose |
|----------|---------|
| `method.md` | Four-stage foresight methodology |
| `drivers.md` | Example: 12 AI governance drivers analyzed |
| `uncertainties.md` | How to select critical uncertainties |
| `scenarios.md` | Four complete scenario narratives |
| `indicators.md` | 10 signals with thresholds and sources |
| `decisions.md` | **NEW:** How to use scenarios in decision-making |
| `contingency.md` | **NEW:** Pre-built response playbooks |

### Guides (`guides/`)

| Guide | Purpose |
|-------|---------|
| `adaptation.md` | **NEW:** Step-by-step domain adaptation with worked example |
| `facilitation.md` | **NEW:** How to run scenario workshops |

### Scripts (`scripts/`)

| Script | Purpose |
|--------|---------|
| `generate_matrix.py` | Creates 2x2 matrix from config |
| `generate_indicators.py` | Creates indicator register from config |

### Examples (`examples/`)

| File | Description |
|------|-------------|
| `scenario_matrix.md` | Generated 2x2 with probabilities |
| `indicator_register.md` | Complete monitoring register |
| `weekly_scan.md` | Sample horizon scan with 6 signals |

---

## The Methodology

```
DRIVERS → UNCERTAINTIES → SCENARIOS → INDICATORS → DECISIONS
   ↓            ↓             ↓            ↓            ↓
 12 forces   2 axes       4 worlds    10 signals   Action
 analyzed    selected     developed   monitored    triggers
```

**Stage 1: Identify Drivers**
Map 10-15 forces shaping your focal question using STEEP+T framework.

**Stage 2: Select Uncertainties**
Choose 2 high-impact, high-uncertainty drivers as scenario axes.

**Stage 3: Build Scenarios**
Develop 4 narrative futures for each quadrant of the 2x2 matrix.

**Stage 4: Define Indicators**
Create early warning signals for each scenario.

**Stage 5: Connect to Decisions**
Stress-test strategies, find robust moves, build contingency plans.

---

## Use Cases

### Use Case 1: Strategic Planning

**Situation:** Annual strategy refresh, board wants assurance we've considered multiple futures.

**How to Use:**
1. Run workshop using `guides/facilitation.md`
2. Test current strategy against all 4 scenarios
3. Identify robust moves that work across scenarios
4. Build contingency triggers for scenario-specific responses

**Deliverable:** Strategy document with scenario stress-testing section.

---

### Use Case 2: Investment Decision

**Situation:** Major capital allocation decision with 5+ year horizon.

**How to Use:**
1. Define focal question around the investment decision
2. Build scenarios around key uncertainties
3. Calculate expected value of investment under each scenario
4. Set decision triggers: "If scenario X probability exceeds 40%, we [action]"

**Deliverable:** Investment memo with scenario-weighted analysis.

---

### Use Case 3: Policy Advocacy

**Situation:** Advocating for regulatory approach to emerging technology.

**How to Use:**
1. Build scenarios showing different regulatory futures
2. Identify which scenario aligns with your preferred policy
3. Develop indicator-based arguments: "Early signs suggest [scenario], which supports [policy]"
4. Prepare responses for alternative scenarios

**Deliverable:** Policy brief with scenario-based framing.

---

### Use Case 4: Risk Management

**Situation:** Enterprise risk register assumes a single future.

**How to Use:**
1. Map current risks to scenario likelihoods
2. Identify scenario-specific risks not currently tracked
3. Stress-test controls against each scenario
4. Add scenario probability to risk weighting

**Deliverable:** Enhanced risk register with scenario overlays.

---

### Use Case 5: Ongoing Horizon Scanning

**Situation:** Leadership wants regular updates on strategic environment.

**How to Use:**
1. Set up indicator monitoring per `indicators.md`
2. Run weekly 30-minute scans
3. Update scenario probabilities monthly
4. Trigger strategic review when thresholds crossed

**Deliverable:** Weekly scan memo, monthly probability dashboard.

---

## The AI Governance Example

The included example focuses on AI governance 2024-2030:

**Focal Question:** How will AI governance evolve, and what does that mean for strategy?

**Axes:**
- AI Capability: Incremental ↔ Discontinuous
- Regulation: Fragmented ↔ Harmonized

**Scenarios:**
1. **Coordinated Caution** — Orderly governance before capabilities leap
2. **Emergency Coordination** — Crisis forces cooperation
3. **Patchwork Progress** — Steady advancement, messy governance
4. **Fragmented Scramble** — Transformative AI with minimal guardrails

This example is fully worked through all stages, including indicators, weekly scans, and decision implications.

---

## Adapting for Your Domain

The methodology applies to any strategic foresight need. See `guides/adaptation.md` for step-by-step instructions with a worked example (energy transition).

**Domains this works for:**
- Geopolitical risk
- Technology adoption/disruption
- Market/competitive dynamics
- Regulatory landscapes
- Climate/sustainability futures
- Supply chain resilience
- Workforce evolution

---

## Operational Rhythm

| Frequency | Activity | Time | Output |
|-----------|----------|------|--------|
| Weekly | Indicator scan | 30 min | Signal log |
| Monthly | Probability review | 1-2 hrs | Updated probabilities |
| Quarterly | Deep scenario review | Half day | Narrative updates if needed |
| Annually | Full reassessment | 1-2 days | Refresh drivers and scenarios |

---

## Project Structure

```
foresight-scenarios-toolkit/
├── framework/
│   ├── method.md           # Core methodology
│   ├── drivers.md          # Driver analysis example
│   ├── uncertainties.md    # Uncertainty selection
│   ├── scenarios.md        # Four scenario narratives
│   ├── indicators.md       # Indicator register
│   ├── decisions.md        # Decision framework     ← NEW
│   └── contingency.md      # Contingency playbooks  ← NEW
├── guides/
│   ├── adaptation.md       # Domain adaptation      ← NEW
│   └── facilitation.md     # Workshop guide         ← NEW
├── scripts/
│   ├── generate_matrix.py
│   ├── generate_indicators.py
│   ├── scenarios_config.json
│   └── indicators_config.json
├── examples/
│   ├── scenario_matrix.md
│   ├── indicator_register.md
│   └── weekly_scan.md
├── README.md
└── LICENSE
```

---

## Getting Started

**Option A: Learn the methodology**
1. Read `framework/method.md` for the four-stage process
2. Study the AI governance example across `framework/*.md`
3. Review `framework/decisions.md` for the action framework

**Option B: Run a workshop**
1. Start with `guides/facilitation.md`
2. Adapt the agenda for your context
3. Use `guides/adaptation.md` for non-AI domains

**Option C: Set up ongoing scanning**
1. Define your scenarios (or use/adapt the example)
2. Configure indicators in `scripts/indicators_config.json`
3. Run `python scripts/generate_indicators.py`
4. Establish weekly scanning rhythm

---

## References

- Schwartz, P. (1991). *The Art of the Long View*
- Shell Scenarios Team. *Scenarios: An Explorer's Guide*
- Wilkinson, A. & Kupers, R. (2014). *The Essence of Scenarios*
- IFTF. *Foresight Toolkit*

---

## License

MIT License — See [LICENSE](LICENSE)

---

*Built by Del Schlangen | [LinkedIn](https://linkedin.com/in/del-s-759557175/)*
