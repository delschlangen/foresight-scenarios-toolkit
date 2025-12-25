# Decision Framework: Using Scenarios to Inform Strategy

Scenarios are only valuable if they change decisions. This framework bridges foresight outputs to strategic action.

---

## The Core Problem

Most scenario work dies on the vine because:
- Scenarios feel abstract and disconnected from real choices
- There's no clear trigger for "what do we do now?"
- Strategic options aren't pre-developed, so response is slow
- Probability updates don't translate to action

This framework solves these problems by creating explicit links between scenarios and decisions.

---

## Three Uses of Scenarios

### 1. Test Current Strategy (Stress Testing)

**Question:** "How does our current strategy perform across all four scenarios?"

| Step | Action |
|------|--------|
| 1 | Document current strategy (3-5 key commitments) |
| 2 | For each scenario, assess: Does this strategy succeed, struggle, or fail? |
| 3 | Identify vulnerabilities: Which scenarios break your strategy? |
| 4 | Calculate exposure: Probability × Impact for vulnerable scenarios |
| 5 | Decide: Accept the risk, hedge, or pivot |

**Example Output:**

| Strategic Commitment | Coordinated Caution | Emergency Coordination | Patchwork Progress | Fragmented Scramble |
|---------------------|--------------------|-----------------------|-------------------|-------------------|
| Heavy investment in EU compliance | ✅ Wins | ✅ Wins | ⚠️ Overinvested | ❌ Wasted spend |
| US-first market strategy | ⚠️ Works | ⚠️ Works | ✅ Optimal | ❌ High risk |
| Minimal safety investment | ❌ Fails | ❌ Fails | ⚠️ Risky | ⚠️ Risky |

---

### 2. Find Robust Moves (No-Regret Actions)

**Question:** "What actions make sense regardless of which scenario unfolds?"

**Robust moves** are valuable across multiple scenarios. Prioritize these when uncertainty is high.

**How to Identify:**

1. List 10-15 potential strategic actions
2. Score each action's value (1-5) under each scenario
3. Calculate robustness: minimum score across scenarios
4. Prioritize actions with high minimum scores

**Example Analysis:**

| Strategic Action | CC | EC | PP | FS | Min | Robustness |
|-----------------|-----|-----|-----|-----|-----|------------|
| Build internal AI safety expertise | 5 | 5 | 3 | 4 | 3 | High |
| Develop compliance modularity | 4 | 4 | 5 | 2 | 2 | Medium |
| Invest in regulatory relationships | 5 | 4 | 4 | 2 | 2 | Medium |
| Go all-in on speed-to-market | 2 | 1 | 3 | 4 | 1 | Low |
| Delay AI adoption entirely | 3 | 4 | 2 | 1 | 1 | Low |

**Robust moves** (high minimum scores): Build internal AI safety expertise, develop compliance flexibility, maintain optionality.

**Risky bets** (low minimum scores): Go all-in on speed OR delay entirely.

---

### 3. Develop Contingent Strategies (If-Then Planning)

**Question:** "What should we do IF a specific scenario becomes likely?"

Pre-develop strategic responses so you can move fast when indicators shift.

**Framework:**

```
IF [indicator threshold reached]
AND [scenario probability exceeds X%]
THEN [trigger pre-planned response]
```

See `contingency.md` for detailed templates.

---

## Decision Triggers

### Probability Thresholds

Define organizational thresholds that trigger review or action:

| Probability Range | Response Level |
|------------------|----------------|
| < 15% | Monitor only |
| 15-30% | Quarterly strategic review |
| 30-50% | Active contingency planning |
| > 50% | Execute scenario-specific strategy |

### Indicator Triggers

Beyond probability, specific indicators can trigger immediate action:

| Indicator | Threshold | Trigger Action |
|-----------|-----------|----------------|
| Major AI incident reported | Any serious incident | Emergency leadership briefing |
| International AI agreement announced | Signed by US+EU+2 others | Activate "Coordinated Caution" playbook |
| Capability discontinuity claimed | Credible source | Immediate scenario reassessment |
| Key market closes to your product | Any major market | Accelerate compliance adaptation |

---

## The Strategy Development Process

### Step 1: Current State Assessment

Answer these questions:
- What is our focal question? (What are we trying to decide?)
- What is our current strategic posture?
- What are our key commitments/constraints?
- What decisions are we facing in the next 6-12 months?

### Step 2: Scenario Testing

For each upcoming decision:
1. What would we decide under Scenario 1?
2. What would we decide under Scenario 2?
3. ... (repeat for all scenarios)
4. Where do answers converge? (Robust decisions)
5. Where do answers diverge? (Contingent decisions)

### Step 3: Options Development

For divergent decisions, develop options:
- **Option A:** Best for Scenarios 1 and 2
- **Option B:** Best for Scenarios 3 and 4
- **Option C:** Hedged approach (works reasonably for all)

### Step 4: Decision Rule

Choose your decision-making approach:

| Approach | When to Use | How It Works |
|----------|-------------|--------------|
| **Expected value** | Moderate stakes, good probability estimates | Weight options by scenario probability |
| **Maximin** | High stakes, severe downside risk | Optimize for worst-case scenario |
| **Minimax regret** | Fear of being wrong | Minimize potential regret across scenarios |
| **Real options** | High uncertainty, can delay | Preserve optionality; decide when clearer |

---

## Worked Example: AI Adoption Decision

**Focal Question:** Should we deploy AI agents for customer service in 2025?

### Current State
- 500-person customer service team
- Competitors testing AI agents
- Board pressure to cut costs
- Brand dependent on service quality

### Decision Under Each Scenario

| Scenario | Optimal Decision | Rationale |
|----------|-----------------|-----------|
| Coordinated Caution | Cautious pilot | Compliance frameworks emerging; wait for clarity |
| Emergency Coordination | Delay | High regulatory risk; focus on safety |
| Patchwork Progress | Moderate deployment | Move forward but design for compliance modularity |
| Fragmented Scramble | Aggressive deployment | Speed advantage; worry about compliance later |

### Convergence Analysis
- **Converges on:** Some level of AI experimentation is warranted
- **Diverges on:** Speed and scale of deployment

### Robust Action
- **Pilot program** with clear success metrics
- **Modular architecture** allowing scale-up or scale-back
- **Human oversight** maintained initially

### Contingent Actions
- **IF** Patchwork Progress probability > 50%: Accelerate deployment
- **IF** Emergency Coordination probability > 30%: Pause expansion, increase safety investment
- **IF** major AI incident occurs: Immediate deployment freeze, safety review

---

## Integration with Indicator Tracking

Weekly scans should feed decision-making:

```
WEEKLY SCAN → PROBABILITY UPDATE → THRESHOLD CHECK → ACTION TRIGGER
     ↓              ↓                    ↓                ↓
  6 signals    45% → 52%           "Exceeds 50%"    "Execute PP strategy"
```

See `indicators.md` for the signal tracking system.

---

## Common Pitfalls

### Pitfall 1: Scenario Paralysis
**Symptom:** "We can't decide because any scenario could happen"
**Fix:** Use robust moves. There are always actions that make sense across scenarios.

### Pitfall 2: Probability Anchoring
**Symptom:** Over-committing to the "most likely" scenario
**Fix:** Stress-test strategy against all scenarios, especially high-impact low-probability ones.

### Pitfall 3: False Precision
**Symptom:** Debating whether probability is 32% or 35%
**Fix:** Use ranges and thresholds, not point estimates. The goal is direction, not precision.

### Pitfall 4: Delayed Response
**Symptom:** Indicators shift but strategy doesn't
**Fix:** Pre-commit to decision triggers. Define in advance what will cause action.

---

## Quick Reference: Decision Checklist

Before any major strategic decision:

- [ ] Have we tested this decision against all four scenarios?
- [ ] Do we understand which scenarios make this decision successful?
- [ ] Do we understand which scenarios make this decision fail?
- [ ] Have we identified robust alternatives?
- [ ] Have we defined trigger conditions for changing course?
- [ ] Is our current scenario probability assessment up to date?
- [ ] Are we over-weighting the "most likely" scenario?

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2024-12 | Initial framework |
