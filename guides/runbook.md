# The Runbook: Focal Question to Decisions in One Sitting

Everything in this toolkit, in order, with time boxes. Follow it top to bottom and in about two hours you will have a focal question, a scored driver list, two axes, four named scenarios with probabilities, an indicator register with a scanning rhythm, and a first stress-test of your strategy.

Two hours produces a **first draft** good enough to show colleagues and argue about. It does not replace the one-day workshop in `guides/facilitation.md`, which is how you get a team to own the result. Use this runbook to prepare for that workshop, to refresh an existing set, or when you are the only person doing the work.

---

## What You Will Have at the End

| Output | Template | Worked example |
|--------|----------|----------------|
| Focal question (one sentence) | this page, Step 0 | `framework/drivers.md` (top) |
| 10-15 scored drivers | `templates/drivers_template.md` | `framework/drivers.md` |
| Two axes with named poles | `templates/drivers_template.md` (end) | `framework/uncertainties.md` |
| Four scenarios: name, tagline, 5 features, probability | `templates/scenario_template.md` | `framework/scenarios.md` |
| Rendered 2x2 matrix | `scripts/generate_matrix.py` | `examples/scenario_matrix.md` |
| 8-12 indicators with thresholds | `templates/indicator_template.md` | `framework/indicators.md` |
| Rendered register + CSV | `scripts/generate_indicators.py` | `examples/indicator_register.md`, `.csv` |
| Strategy stress-test and 2-3 decision triggers | `framework/decisions.md` | `examples/strategic_options.md` |
| A calendar: weekly scan, monthly update, quarterly review | this page, Step 6 | `examples/weekly_scan.md` |

You need a text editor and, optionally, Python 3.8+ for the two rendering scripts. Nothing to install.

---

## Step 0: Write the Focal Question (10 minutes)

Fill in the blanks and do not move on until every blank is filled:

> **For [organization or role], what strategy should we pursue regarding [decision area] over [time horizon], given uncertainty about [two or three key factors]?**

Test it:

- **Specific** — names a decision area, not a topic. "Our AI roadmap", not "AI".
- **Strategic** — a choice someone will actually make.
- **Actionable** — the answer changes a budget, a hire, a product, a policy position.
- **Time-bounded** — 3 to 10 years. Shorter is forecasting; longer is fiction.

Write the final sentence at the top of every document you produce. Every later step is judged against it.

*Stuck?* `guides/adaptation.md`, Step 1, has good and bad examples side by side.

---

## Step 1: List and Score Drivers (25 minutes)

Open `templates/drivers_template.md`. Work through the six STEEP+T categories (Social, Technological, Economic, Environmental, Political, Threat) and list forces that bear on the focal question. Aim for 10-15. Three or four per category is plenty; some categories will be thin, and that is fine.

For each driver write one line of description and score two things from 1 to 5:

- **Impact** — if this driver swings, how much does the answer to the focal question change?
- **Uncertainty** — how genuinely unknown is its direction over your time horizon?

Rules of thumb:

- A driver everyone agrees on is low uncertainty however important it is. It belongs in every scenario, not on an axis.
- If you can only think of "technology" as a driver, you are too abstract. Which technology, doing what to whom?
- Score fast. Rough placement on a 2x2 of impact against uncertainty is all Step 2 needs.

Fill in the prioritization matrix at the bottom of the template. Drivers scoring 4-5 on both dimensions are your axis candidates.

---

## Step 2: Choose Two Axes (15 minutes)

From the Critical drivers, pick two that pass all four tests in `framework/method.md`, Stage 2:

| Test | Ask |
|------|-----|
| High impact | Would the answer to the focal question differ between its poles? |
| High uncertainty | Could informed people disagree about which pole we are heading to? |
| Independent | If axis A goes one way, could axis B still go either way? |
| Differentiating | Do the four combinations describe worlds that feel different to live in? |

The independence test kills most bad axis pairs. If one pole of A makes one pole of B nearly certain, you have one axis dressed as two, and your four scenarios will collapse into two. Pick a different second axis even if it scored lower.

Frame each axis as a spectrum with named poles: "Regulatory coherence: Fragmented ↔ Harmonized", never "Regulated: yes ↔ no". Name the axes so a board member understands them without the driver list.

Record the two axes at the bottom of the drivers template.

---

## Step 3: Name and Sketch Four Scenarios (30 minutes)

Open `templates/scenario_template.md`. Draw the 2x2 with your axes. For each quadrant, in this order and in this much time:

1. **Name** (2 min each) — two or three words, evocative, not a label. "Patchwork Progress", not "Low Coherence / Incremental".
2. **Tagline** (1 min each) — one sentence a journalist would quote.
3. **Five features** (3 min each) — what is true in this world that is not true in the others.
4. **Winners and losers** (1 min each) — two of each. If you cannot name a loser, the scenario is a wish, not a world.

Skip the full narrative for now. Narratives take an hour each and are the first thing to add after the two-hour pass.

Then set **initial probabilities** that sum to 100. Do it quickly, argue about it later. The point of the numbers is to create something to update, not to be right. If one scenario is below 10%, ask whether it is really a distinct world or a wild card inside another.

**Render the matrix.** Copy `scripts/scenarios_config.json`, replace the values, and run:

```bash
python3 scripts/generate_matrix.py --config my_scenarios.json --output my_matrix.md
```

The script refuses probabilities that do not sum to 100, which is the most common mistake at this point.

---

## Step 4: Define Indicators (20 minutes)

Open `templates/indicator_template.md`. For each axis, ask: *what would we observe in the next 6-18 months that tells us which pole we are moving toward?* You want 8-12 indicators in total, mixing:

- **Leading** (about half) — signals before the change: funding flows, draft legislation, hiring patterns, research trends.
- **Confirming** (about a third) — the change happening: enacted policy, product launches, enforcement actions.
- **Lagging** (a few) — the change having happened: employment data, market share, adoption statistics.

For each, write a **threshold that two analysts would agree has been crossed**. A count, a comparison to a baseline, or a named class of event. "Significant increase" is not a threshold; ">50% year-over-year" is. `scripts/README.md` has more on this.

Give every indicator a **status** (start them all at Watching), a source you will actually check, and a frequency.

**Render the register and a CSV** for whoever tracks this in a spreadsheet:

```bash
python3 scripts/generate_indicators.py --config my_indicators.json --output my_register.md --csv my_register.csv
```

---

## Step 5: Connect to Decisions (20 minutes)

This is the step most scenario work skips, and the reason most scenario work changes nothing. Open `framework/decisions.md` and do the first two moves:

**Stress-test (10 min).** Write down your three to five current strategic commitments. For each, mark how it fares in each scenario: wins, struggles, or fails. One table, twenty cells. The cells marked *fails* are your exposure.

| Commitment | Scenario 1 | Scenario 2 | Scenario 3 | Scenario 4 |
|------------|------------|------------|------------|------------|
| ... | ✅ / ⚠️ / ❌ | | | |

**Robust moves (5 min).** List five actions you could take. Score each 1-5 per scenario. The actions with the highest *minimum* score are your no-regret moves. Do those first regardless of which world arrives. `examples/strategic_options.md` shows this at full scale.

**Two triggers (5 min).** Write two sentences of the form *"If [indicator] crosses [threshold] or [scenario] exceeds [probability], we will [review or action] within [days]."* Pre-committing now is what prevents rationalised inaction later. Full playbooks come later, using `framework/contingency.md`.

---

## Step 6: Set the Rhythm (5 minutes)

Put four recurring entries in a calendar before you close the laptop:

| Cadence | What | Time | Template |
|---------|------|------|----------|
| Weekly | Scan indicator sources, log signals, do **not** move probabilities | 30 min | `templates/weekly_scan_template.md` |
| Monthly | Run the probability worksheet, log changes, check triggers | 1-2 hrs | `framework/probability_updates.md`, `templates/probability_log_template.md` |
| Quarterly | Are the scenarios still the right four? Any indicator fired? Playbooks current? | half day | `framework/contingency.md`, Playbook Maintenance |
| Annually | Redo the driver list from scratch | 1-2 days | this runbook |

A scenario set with no calendar entries is a slide deck. Schedule the first weekly scan for next week.

---

## Checklist

- [ ] Focal question written in one sentence and at the top of every document
- [ ] 10-15 drivers scored for impact and uncertainty
- [ ] Two axes, independent, framed as spectra with named poles
- [ ] Four scenarios, each with name, tagline, five features, winners and losers
- [ ] Probabilities sum to 100; matrix rendered
- [ ] 8-12 indicators, each with a measurable threshold, a source, a frequency and a status
- [ ] Register and CSV rendered
- [ ] Current strategy stress-tested against all four scenarios
- [ ] At least two robust moves and two decision triggers written down
- [ ] Weekly, monthly, quarterly and annual entries in the calendar

---

## The Two Weeks After

1. Write the full narratives (1-2 pages each) using the scenario template. Write them as history from the end of the time horizon.
2. Show the set to three people who will disagree with you. Adjust the axes if two of them say the scenarios feel the same.
3. Build one contingency playbook, for the scenario your strategy fails worst in, using `framework/contingency.md`.
4. Brief whoever owns the decisions in ten minutes: focal question, the 2x2, the stress-test table, the two triggers. `FAQ.md` has a structure for that briefing.
5. Run the first weekly scan.

---

## Where This Goes Wrong

- **Axes that are secretly one axis.** The four scenarios read as two. Redo Step 2 with the independence test.
- **Scenarios as good/bad.** One utopia, one dystopia, two blends. Every scenario needs real winners and real losers.
- **Thresholds nobody can call.** Six months in, nobody agrees whether anything has fired. Rewrite with counts and comparisons.
- **Probabilities as forecasts.** Leadership asks "so which one will happen?" Answer with the robust moves, not a number. `FAQ.md` covers this.
- **No calendar.** The most common failure. Step 6 takes five minutes; skip it and the rest was decoration.
