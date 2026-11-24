# Updating Scenario Probabilities

How to move scenario probabilities when indicators fire, without false precision and with a record anyone can audit.

---

## What the Numbers Are For

Scenario probabilities are not forecasts. Nobody can put a calibrated number on "Fragmented Scramble by 2030". The numbers do three jobs:

1. **Direction.** Is the world drifting toward or away from each scenario since last quarter?
2. **Triggers.** Decision thresholds (`decisions.md`: review at 15-30%, plan at 30-50%, act above 50%) need a number to cross.
3. **Discipline.** Writing down *why* a number moved forces the team to say what evidence it is reacting to.

That is why the method below favours small, rule-bound, logged movements over debate about whether a scenario is at 32% or 35%.

---

## Cadence: Who Moves What, When

The toolkit mentions weekly, monthly and quarterly reviews. They do different things.

| Cadence | Probabilities | What actually happens |
|---------|---------------|-----------------------|
| **Weekly scan** | **Do not move** | Log signals, update indicator status (Watching → Elevated → Fired), flag items. Exception: a verified **Fired** indicator may trigger an immediate update and a playbook check. |
| **Monthly update** | **Move, using the worksheet** | Translate the month's status changes into point shifts. Log every change. Check decision thresholds. |
| **Quarterly review** | **Reset if needed** | Ask whether the four scenarios are still the right four. Re-baseline if the scenario set changes. |
| **Annual refresh** | **Re-baseline** | Redo drivers and axes. Start a new probability log. |

If your weekly scan template shows a "Scenario Probability Update" table (the example in `examples/weekly_scan.md` does), treat those as *proposed* shifts for the monthly review, not as changes to the official numbers.

---

## The Monthly Worksheet

Work through the five steps with the indicator register and last month's probabilities in front of you.

### 1. List what changed

Every indicator whose **status** changed since the last update, and any that fired more than once.

| Indicator | Previous status | New status | Evidence (one line, with source) | Confidence |
|-----------|-----------------|------------|----------------------------------|------------|
| I-05 | Watching | Fired | First AI Act fine issued (Commission press release, date) | High |
| I-02 | Watching | Elevated | Two senior safety departures reported, one unconfirmed | Medium |

Nothing changed? Record "no status changes" in the log and stop. Probabilities do not drift on their own.

### 2. Record direction

For each change, which scenarios does it favour and which does it disfavour? Take this from the **scenario linkage** row of the indicator register, not from the mood of the meeting.

| Indicator | Favours | Disfavours |
|-----------|---------|------------|
| I-05 Fired | Patchwork Progress | Coordinated Caution (if no US equivalent follows) |
| I-02 Elevated | Emergency Coordination | Patchwork Progress |

### 3. Assign magnitude

Use fixed step sizes. They are deliberately coarse.

| Status change | Points moved **to** the favoured scenario(s) |
|---------------|-----------------------------------------------|
| Watching → Elevated | 2 |
| Elevated → Fired, or Watching → Fired | 5 |
| Cluster: 3+ indicators fire toward the same scenario in one quarter | 10 (instead of 5 each) |
| Status reverts (Elevated → Watching, false alarm) | reverse the earlier move |

Adjust for confidence: **Medium** confidence halves the step (round down); **Low** confidence contributes 0 points and is logged as watch-only.

Hard limits:

- No scenario moves more than **10 points in one month** without a cluster or sign-off from the decision authority in `contingency.md`.
- No scenario goes below **5%**. If you believe a scenario is dead, retire it at the quarterly review rather than starving it.

### 4. Apply and renormalise

Add the points to the favoured scenarios. Take the same total from the disfavoured scenarios named in step 2; if the evidence does not single out a loser, take it proportionally from all others. Round to whole numbers and confirm the total is 100.

Worked arithmetic for the two rows above, starting from 20 / 15 / 45 / 20 (CC / EC / PP / FS):

- I-05 Fired, High confidence: +5 to PP, −5 from CC → 15 / 15 / 50 / 20
- I-02 Elevated, Medium confidence: 2 points halved to 1: +1 to EC, −1 from PP → 15 / 16 / 49 / 20
- Total 100. Patchwork Progress is now within a point of the 50% action threshold.

### 5. Log and check triggers

Write one entry per update in the probability log (`templates/probability_log_template.md`): date, old → new, the indicators cited, the rationale in two sentences, who approved. Then:

- Compare the new numbers to the **probability thresholds** in `decisions.md`. Crossing one schedules a review; it does not by itself change strategy.
- Check every **playbook trigger** in `contingency.md`. A single fired indicator may activate a playbook regardless of the probabilities.
- Update the "Current" and "Trend" columns of the Scenario Probability Tracker in your indicator register.

---

## Worked Example: The December 2024 Scan

`examples/weekly_scan.md` logs six signals and proposes moving 20 / 15 / 45 / 20 to 18 / 17 / 47 / 18. Running the worksheet on it:

| Signal | Indicator | Status | Confidence | Direction | Points |
|--------|-----------|--------|------------|-----------|--------|
| EU enforcement priorities published | I-05 | Watching → Elevated | High | +PP, −CC | 2 |
| US bill stalls | I-04 | stays Watching (inaction is the baseline) | High | +PP, −CC | 0, note only |
| Red team disbanded (single source) | I-02 | Watching → Elevated | Medium | +EC, −PP | 2 halved → 1 |
| China chip progress | I-09 | Watching → Elevated | Medium | +FS, −CC | 2 halved → 1 |
| OECD draft framework | I-03 | stays Watching (draft, non-binding) | Medium | +CC | 0, note only |
| Agentic release | I-01 | stays Watching (incremental) | High | — | 0 |

Applied: CC 20 − 2 − 1 = 17; PP 45 + 2 − 1 = 46; EC 15 + 1 = 16; FS 20 + 1 = 21. Total 100.

The worksheet lands at 17 / 16 / 46 / 21 against the scan's intuitive 18 / 17 / 47 / 18. Same direction on three of four scenarios; the one disagreement (Fragmented Scramble up rather than down) is because the worksheet credits the chip signal and does not let a non-binding OECD draft offset it. That is the kind of difference worth five minutes of discussion at the monthly review, and exactly the discussion the worksheet exists to provoke.

---

## Guardrails

- **Single-source signals move nothing to Fired.** Elevate, note, wait for confirmation.
- **Recency.** If three of this month's changes are the same story reported three times, count it once.
- **Anchoring.** Before reading last month's numbers, have each reviewer write down what they think the direction of travel is. Then compare.
- **Decay.** An Elevated indicator with no new evidence for two consecutive months reverts to Watching, and its points come back.
- **Narrative drift.** If the evidence consistently favours a world none of the four scenarios describes, the answer is a new scenario at the quarterly review, not a probability of 60% on the nearest fit.
- **Point estimates in public.** Communicate ranges and arrows (Patchwork Progress 45-50%, rising), never a single number without its trend.

---

## Communicating an Update

For a leadership audience, one slide, four lines:

1. *Where we are:* the four scenarios with current probability and a trend arrow each.
2. *What moved and why:* the two or three indicator events behind the arrows.
3. *What it means:* any decision threshold or trigger crossed, and the pre-agreed response.
4. *What would change our mind:* the next indicators to watch and their thresholds.

Line 4 is what distinguishes foresight from a forecast. It tells the audience what to look for themselves.

---

## If You Want Formal Bayesian Updating

The worksheet is a disciplined approximation. If your team is comfortable with it, the formal version is: for each scenario *S* and observed signal *E*, multiply the prior P(S) by the likelihood P(E | S), then renormalise. The likelihoods are the hard part: you must state, for each scenario, how probable this signal would be *if that world were unfolding*. In practice teams spend the meeting arguing about likelihoods instead of strategy, which is why the step-size method above is the default. Use the formal method when a signal is unusually diagnostic, meaning it would be very likely in one scenario and very unlikely in the others, and record the likelihoods you used in the log.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.2 | 2026-11 | Initial worksheet, cadence rules, worked example |
