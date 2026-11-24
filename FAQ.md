# FAQ and Anti-Patterns

Questions that come up in almost every scenario exercise, with the toolkit's answers. Short version of the method: `CHEATSHEET.md`. Full sequence: `guides/runbook.md`.

---

## Method

### Why four scenarios? Can we do three, or five?

Four is what two independent axes produce, and two axes is the most a group can hold in its head while still generating genuinely different worlds. Three scenarios almost always collapse into "good, bad, middle", which is a forecast with error bars, not foresight. Five or more usually means a third axis is hiding in the set; find it and ask whether it should replace one of the two you chose.

Legitimate exceptions: drop a quadrant if it is genuinely implausible (not merely uncomfortable), and say so explicitly in the scenario document. Add a fifth "wild card" only as a named discontinuity (pandemic, major conflict) that could land inside any of the four, not as a peer scenario.

### Our two uncertainties are correlated. Now what?

Then you have one axis. Keep the more impactful one and go back to the driver list for a second axis that passes the independence test: *if A goes one way, could B still go either way?* A lower-scoring but independent driver makes a better axis than a high-scoring correlated one. `framework/uncertainties.md` shows an axis that was rejected for exactly this reason.

### Is the most likely scenario just our forecast?

No, and treating it that way is the most expensive mistake in the field. The highest-probability scenario in the toolkit's example is 45%, which means a majority of the probability mass is somewhere else. Strategy should be built on the **robust moves** that score well across all four worlds (`framework/decisions.md`), with scenario-specific actions held behind **triggers**. If leadership insists on one answer, give them the stress-test table instead of a number.

### What is "wind-tunnelling"?

Another name for the stress-test in `framework/decisions.md`: run each current strategic commitment through each scenario and mark whether it wins, struggles or fails. The cells marked "fails" are your exposure; the commitments that win everywhere are your robust core. `examples/strategic_options.md` does this for eight options.

### How often should we refresh, and when is a set stale?

Weekly scans, monthly probability updates, quarterly review of the scenarios themselves, annual rebuild of the drivers (`framework/probability_updates.md` has the cadence table). A set is stale when any of these is true: a narrative's pivotal dates have passed without comment; an indicator has been Elevated for months with nobody deciding whether it fired; the evidence keeps favouring a world none of the four describes. The toolkit's own AI governance example is a Q4 2024 baseline that has deliberately *not* been refreshed, so you can see what a dated set looks like and practise the refresh on it.

### A scenario came true. Are we done?

A scenario never comes true; the world lands somewhere in the matrix and keeps moving. When one scenario is clearly dominant (say above 60% for two consecutive quarters), do three things: execute its playbook if you have not already; ask what the *next* two critical uncertainties are from that new vantage point; and rebuild the set around them. The old set becomes a record of what you prepared for and how well.

### Can we use this outside AI governance?

Yes; the method is domain-agnostic and the AI example is just the worked case. `guides/adaptation.md` walks the adaptation step by step and includes a complete second example for an energy company. The templates in `templates/` are blank. The scripts accept any axes and scenario names.

### Do we need the Python scripts?

No. They render Markdown and CSV from JSON so the matrix and register are consistent and diffable. Everything can be done by hand in the Markdown templates. Use the scripts if you want the probability check, the CSV for a spreadsheet, or a register you can regenerate after edits.

---

## Probabilities

### People argue about 32% versus 35%.

Stop the argument: that difference is below the resolution of the method. Use the step sizes in `framework/probability_updates.md` (2 points for Elevated, 5 for Fired, 10 for a cluster), communicate ranges with trend arrows, and spend the time on *what would change our mind* instead.

### Our probabilities do not sum to 100.

They must. The matrix generator refuses to render otherwise. Take the excess from, or give the shortfall to, the scenario the latest evidence most disfavours or favours; if there is no such scenario, adjust proportionally.

### Should we use Bayesian updating?

You can, and the last section of `framework/probability_updates.md` shows how. Most teams find that stating likelihoods for every signal under every scenario consumes the meeting. The step-size worksheet is a deliberate approximation that keeps the discipline (evidence in, logged change out) without the arithmetic.

---

## Indicators

### How many indicators, and how do we write thresholds that work?

Eight to twelve. More than that and the weekly scan stops happening. Each needs a threshold two analysts would agree has been crossed: a count ("two or more senior departures in a quarter"), a comparison to a baseline (">50% year-over-year"), or a named event class ("binding agreement, not a voluntary declaration"). Bare adjectives like "significant" or "major" guarantee a six-month argument about whether anything has happened. Give every indicator a **status** (Watching, Elevated, Fired, Retired) so the question has an answer.

### An indicator fired. Do we change strategy?

Not automatically. A fired indicator does two things: it feeds the monthly probability worksheet, and it is checked against the **trigger conditions** of each playbook in `framework/contingency.md`. If it matches a trigger, the pre-agreed response runs, which is usually a review or a bounded first action, not a wholesale pivot. Verify with a second source first; single-source signals go to Elevated, not Fired.

---

## Running the Work

### How do we present scenarios to a board in ten minutes?

1. The focal question (one sentence).
2. The 2x2: axes, four names, current probabilities with trend arrows. One slide.
3. The stress-test table: our commitments against the four worlds, with the "fails" cells highlighted.
4. The two or three robust moves we recommend regardless of outcome.
5. The triggers: what we will do, by when, if specific indicators fire.
6. What we are watching next quarter.

Do not present narratives to a board; they belong in the appendix. Do present losers in every scenario, or the board will hear a sales pitch.

### Leadership is not taking it seriously.

Attach the exercise to a decision they are about to make. Run the stress-test on that decision alone. The moment a scenario shows a live commitment failing, the conversation changes. More tactics in `guides/facilitation.md`, Common Challenges.

### Who owns this?

One named analyst for the weekly scan (30 minutes), a strategy owner for the monthly update, and whoever owns the decisions for the quarterly review. The decision authority matrix in `framework/contingency.md` sets who can activate what. Without a named weekly owner, the rhythm stops within two months.

---

## Anti-Patterns

| Anti-pattern | What it looks like | The fix |
|--------------|--------------------|---------|
| **Good/bad futures** | One utopia, one dystopia, two blends | Every scenario needs real winners and real losers |
| **Prediction mode** | "Which one is going to happen?" | Lead with robust moves and triggers, not a number |
| **Correlated axes** | Four scenarios that read as two | Independence test; pick a different second axis |
| **Binary axes** | "Regulated: yes or no" | Spectrum with named poles |
| **Vague thresholds** | "Significant progress" | Counts, comparisons, named event classes |
| **Probability theatre** | Thirty minutes on 32 versus 35 | Fixed step sizes, ranges, trend arrows |
| **Indicator hoarding** | 30 indicators, no scan since March | 8-12, with a named weekly owner |
| **Slide-deck death** | Beautiful set, no calendar entries | Weekly, monthly, quarterly, annual: schedule them before closing the workshop |
| **Scenario paralysis** | "We can't decide because anything could happen" | Robust moves exist in every set; find them |
| **Frozen baseline** | Narratives pivoting on dates that have passed, unremarked | Quarterly review; re-baseline; say "as of" on every document |
| **Strategy-free foresight** | Scenarios never touch a decision | Stage 5: stress-test, robust moves, triggers, playbooks |
