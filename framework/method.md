# Foresight Methodology

A structured approach to strategic foresight for emerging technology risk, adapted from Shell's scenario planning methodology and tailored for AI/technology horizon scanning.

---

## Overview

This toolkit implements a four-stage foresight process:

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   DRIVERS   │ →  │UNCERTAINTIES│ →  │  SCENARIOS  │ →  │ INDICATORS  │
│             │    │             │    │             │    │             │
│ What forces │    │ Which are   │    │ What worlds │    │ What signals│
│ shape the   │    │ critical &  │    │ could       │    │ tell us     │
│ future?     │    │ uncertain?  │    │ emerge?     │    │ which way?  │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

---

## Stage 1: Identify Drivers

**Goal:** Map the forces that will shape the future landscape.

### Driver Categories (STEEP+T)

| Category | Description | Example Drivers |
|----------|-------------|-----------------|
| **Social** | Demographics, culture, behavior | Workforce AI adoption attitudes, public trust in AI |
| **Technological** | Capabilities, diffusion, infrastructure | Model capability curves, compute availability |
| **Economic** | Markets, resources, business models | AI investment levels, automation economics |
| **Environmental** | Climate, resources, sustainability | Energy costs for training, data center constraints |
| **Political** | Governance, regulation, geopolitics | AI regulation fragmentation, US-China competition |
| **Threat** | Adversarial, misuse, unintended harms | Weaponization, misalignment, job displacement |

### Driver Analysis Template

For each driver, document:

1. **Driver name:** Clear, specific label
2. **Description:** What is this force?
3. **Direction:** Which way is it trending?
4. **Impact:** How significantly could it affect the focal question?
5. **Uncertainty:** How confident are we in its trajectory?
6. **Time horizon:** When will impact be felt?

See `drivers.md` for a populated example.

---

## Stage 2: Identify Critical Uncertainties

**Goal:** Select the 2 most critical uncertainties to form scenario axes.

### Selection Criteria

A good scenario axis is:

| Criterion | Description |
|-----------|-------------|
| **High impact** | Significantly affects the focal question |
| **High uncertainty** | Outcome is genuinely unknown |
| **Independent** | Not strongly correlated with other axis |
| **Differentiating** | Creates meaningfully different worlds |

### 2x2 Matrix Method

1. List top 8-10 drivers by impact
2. Score each for uncertainty (1-5)
3. Plot on impact vs. uncertainty grid
4. Select 2 from high-impact, high-uncertainty quadrant
5. Verify they're relatively independent
6. Frame as spectrum (not binary)

**Good axis framing:**
- "AI capability advancement: Incremental ↔ Discontinuous"
- "Regulatory environment: Fragmented ↔ Harmonized"

**Poor axis framing:**
- "AI is regulated: Yes ↔ No" *(too binary)*
- "Things go well ↔ Things go badly" *(not specific)*

See `uncertainties.md` for examples.

---

## Stage 3: Build Scenarios

**Goal:** Develop 4 internally consistent narratives exploring each quadrant.

### Scenario Components

Each scenario should include:

| Component | Description |
|-----------|-------------|
| **Name** | Memorable, evocative title |
| **Tagline** | One-sentence summary |
| **Narrative** | 1-2 page story of how this world emerged |
| **Key features** | Bullet list of defining characteristics |
| **Winners/losers** | Who thrives, who struggles |
| **Focal question answer** | How does this world answer our central question? |

### Quality Checks

Good scenarios are:

- ✅ **Plausible** — Could actually happen
- ✅ **Internally consistent** — Logic holds together
- ✅ **Differentiated** — Meaningfully different from each other
- ✅ **Challenging** — Force new thinking
- ✅ **Relevant** — Address the focal question

Bad scenarios:

- ❌ "Good future" vs. "Bad future" (not insightful)
- ❌ Predictions (scenarios are possibilities, not forecasts)
- ❌ Science fiction (plausibility matters)

See `scenarios.md` for a complete example set.

---

## Stage 4: Develop Indicators

**Goal:** Create an early warning system to detect which scenario is emerging.

### Indicator Types

| Type | Description | Example |
|------|-------------|---------|
| **Leading** | Early signals before change manifests | Research paper trends, VC investment shifts |
| **Confirming** | Validates a shift is occurring | Policy announcements, market share changes |
| **Lagging** | Confirms change after the fact | Unemployment data, adoption statistics |

### Indicator Template

For each indicator:

1. **Signal:** What are we watching for?
2. **Source:** Where do we monitor this?
3. **Threshold:** What level triggers attention?
4. **Scenario linkage:** Which scenario(s) does this support?
5. **Confidence:** How reliable is this signal?
6. **Update frequency:** How often do we check?

See `indicators.md` for a populated register.

---

## Operationalizing Foresight

### Weekly Horizon Scan

Regular scanning keeps scenarios alive:

1. Review indicator sources (30 min)
2. Log new signals
3. Assess scenario implications
4. Flag items for escalation
5. Update indicator register

See `examples/weekly_scan.md` for a template.

### Quarterly Scenario Review

Periodic deep review:

1. Are scenarios still plausible?
2. Have new drivers emerged?
3. Which scenario seems most likely now?
4. What strategic implications follow?
5. Update scenarios if needed

### Integration with Decision-Making

Foresight outputs should feed:

- Strategic planning cycles
- Risk register updates
- Investment prioritization
- Policy/advocacy positions
- Contingency planning

---

## References

- Schwartz, P. (1991). *The Art of the Long View*
- Shell Scenarios Team. *Scenarios: An Explorer's Guide*
- Wilkinson, A. & Kupers, R. (2014). *The Essence of Scenarios*
- IFTF. *Foresight Toolkit*

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2024-12 | Initial release |
