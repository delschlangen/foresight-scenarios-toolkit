# Foresight Scenarios Toolkit: One-Page Cheat Sheet

Print this. Everything else in the repo is the long version. Full sequence with time boxes: `guides/runbook.md`.

---

## The Process

| Stage | Question | Output | Template | Example |
|-------|----------|--------|----------|---------|
| **0. Focal question** | What decision, for whom, over what horizon? | One sentence | `guides/runbook.md` Step 0 | top of `framework/drivers.md` |
| **1. Drivers** | What forces shape the answer? | 10-15 drivers scored 1-5 for impact and uncertainty | `templates/drivers_template.md` | `framework/drivers.md` |
| **2. Uncertainties** | Which two matter most and are genuinely unknown? | Two independent axes with named poles | end of drivers template | `framework/uncertainties.md` |
| **3. Scenarios** | What are the four worlds? | Name, tagline, features, winners/losers, probability | `templates/scenario_template.md` | `framework/scenarios.md` |
| **4. Indicators** | How will we know which world is arriving? | 8-12 signals with measurable thresholds | `templates/indicator_template.md` | `framework/indicators.md` |
| **5. Decisions** | What do we do about it? | Stress-test, robust moves, triggers, playbooks | `framework/decisions.md`, `framework/contingency.md` | `examples/strategic_options.md` |

Render outputs: `python3 scripts/generate_matrix.py --config x.json` and `python3 scripts/generate_indicators.py --config y.json --csv out.csv`. Python 3.8+, no installs.

---

## Picking Axes

An axis must be **high impact**, **high uncertainty**, **independent** of the other axis, and **differentiating**. The independence test: *if A goes one way, could B still go either way?* If not, you have one axis, not two.

Frame as a spectrum with named poles: "Fragmented ↔ Harmonized". Never "yes ↔ no".

**Top** = Y-axis high pole. **Right** = X-axis high pole. Top-left is X-low + Y-high.

---

## Scenario Quality

Plausible · Internally consistent · Differentiated · Challenging · Relevant to the focal question.

Every scenario has winners **and** losers. No utopia, no dystopia. Not predictions. Not science fiction.

Probabilities sum to 100. They are a device for direction and triggers, not a forecast.

---

## Indicators

| Type | Share | Tells you |
|------|-------|-----------|
| Leading | ~50% | the change is coming (funding, drafts, hiring) |
| Confirming | ~30% | the change is happening (enacted policy, launches, enforcement) |
| Lagging | ~20% | the change has happened (employment data, market share) |

A **threshold** is a count, a comparison to a baseline, or a named event class. "Significant" is not a threshold. Two analysts must agree whether it has been crossed.

**Status**: Watching → Elevated → Fired (→ Retired). Record Last reviewed every time you look.

---

## The Rhythm

| When | Do | Don't |
|------|----|-------|
| **Weekly** (30 min) | Scan sources, log signals, update indicator status | Move probabilities |
| **Monthly** (1-2 hrs) | Run the worksheet, move probabilities, log, check triggers | Move anything >10 points without sign-off |
| **Quarterly** (half day) | Ask if these are still the right four scenarios; review playbooks | Keep a dead scenario alive below 5% |
| **Annually** (1-2 days) | Redo the drivers | Assume last year's axes still hold |

---

## Moving Probabilities (`framework/probability_updates.md`)

Watching → Elevated **+2** · → Fired **+5** · 3+ indicators toward one scenario **+10 total** · Medium confidence halves · Low confidence 0 · take the points from the disfavoured scenario · renormalise to 100 · **log it** with indicator IDs and rationale.

---

## Decision Thresholds (`framework/decisions.md`)

| Scenario probability | Response |
|----------------------|----------|
| < 15% | Monitor |
| 15-30% | Quarterly strategic review |
| 30-50% | Active contingency planning |
| > 50% | Execute scenario-specific strategy |

A **fired indicator** can activate a playbook regardless of probability. Write the trigger before the signal arrives: *If [indicator] crosses [threshold] or [scenario] exceeds [p%], we will [action] within [days].*

---

## Three Uses of a Scenario Set

1. **Stress-test**: does each current commitment win, struggle or fail in each world?
2. **Robust moves**: score actions 1-5 per scenario; highest *minimum* wins. Do those first.
3. **Contingencies**: one playbook per scenario your strategy fails in. Trigger, day-1 actions, 6-month adaptations, owner.

---

## Pitfalls

Correlated axes · good-vs-bad scenarios · prediction mode · vague thresholds · probability theatre (debating 32 vs 35) · no calendar · scenarios that never touch a decision.

More: `FAQ.md`.
