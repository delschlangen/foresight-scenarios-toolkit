# Scripts

Two small, dependency-free Python scripts turn JSON configs into the Markdown (and CSV) artifacts in `examples/`. Use them to regenerate the toolkit's example, or point them at your own configs once you have adapted the toolkit to your domain.

**Requirements:** Python 3.8 or newer. Standard library only, nothing to install.

```bash
# Render the AI governance example to the terminal
python3 scripts/generate_matrix.py
python3 scripts/generate_indicators.py

# Render your own configs to files (plus a CSV for spreadsheets)
python3 scripts/generate_matrix.py     --config my_scenarios.json  --output my_matrix.md
python3 scripts/generate_indicators.py --config my_indicators.json --output my_register.md --csv my_register.csv

# Help
python3 scripts/generate_matrix.py --help
```

The scripts only ever write the files you name with `--output` and `--csv`. Running them with no arguments prints to the terminal and changes nothing on disk.

---

## From templates to generated outputs

The Markdown templates in `templates/` are where you think. The JSON configs are where you record the decisions so they can be rendered, versioned and diffed. The mapping is direct:

| You filled in | Copy into | Then run |
|---------------|-----------|----------|
| `templates/scenario_template.md` (axes, names, taglines, probabilities) | a copy of `scripts/scenarios_config.json` | `generate_matrix.py` |
| `templates/indicator_template.md` (ID, signal, source, threshold, type, frequency) | a copy of `scripts/indicators_config.json` | `generate_indicators.py` |

Start by copying the example configs and replacing the values. Keep the copies next to your own scenario documents, not inside this repo's `scripts/` folder.

---

## Scenario config schema (`scenarios_config.json`)

```json
{
  "title": "AI Governance Futures (2024-2030)",
  "focal_question": "optional: the question the scenarios answer",
  "as_of": "optional: when the probabilities were last set, e.g. Q4 2024",
  "note": "optional: one-line caveat rendered under the title",
  "axis_x": { "name": "AI Capability Trajectory", "left": "Incremental", "right": "Discontinuous" },
  "axis_y": { "name": "Global Regulatory Coherence", "top": "Harmonized", "bottom": "Fragmented" },
  "scenarios": {
    "top_left":     { "name": "Coordinated Caution",    "tagline": "...", "probability": 20 },
    "top_right":    { "name": "Emergency Coordination", "tagline": "...", "probability": 15 },
    "bottom_left":  { "name": "Patchwork Progress",     "tagline": "...", "probability": 45 },
    "bottom_right": { "name": "Fragmented Scramble",    "tagline": "...", "probability": 20 }
  }
}
```

Rules the script enforces:

- All four quadrants are required, each with `name`, `tagline` and `probability`.
- Probabilities must be numbers between 0 and 100 **and sum to exactly 100**. The script refuses to render otherwise, because a matrix whose probabilities do not sum to 100 misleads everyone who reads it.
- Scenario names of any length are fine. Cells widen to fit the longest word and names wrap onto two lines.

Quadrant positions: `top` is the high pole of the Y axis, `right` is the high pole of the X axis. `top_left` is therefore X-left + Y-top.

---

## Indicator config schema (`indicators_config.json`)

```json
{
  "title": "AI Governance Indicator Register",
  "focal_question": "optional",
  "updated": "2024-12",
  "note": "optional: one-line caveat rendered under the title",
  "indicators": [
    {
      "id": "I-01",
      "signal": "Frontier model capability announcements",
      "source": "Lab blogs, arXiv, press releases, product launches",
      "scenarios": ["All"],
      "type": "Leading",
      "frequency": "Weekly",
      "confidence": "High",
      "threshold": "Release whose capability gains clearly exceed the prior 12-month trend",
      "status": "Watching",
      "last_reviewed": "2024-12",
      "last_fired": null,
      "notes": "optional free text"
    }
  ]
}
```

Required per indicator: `id`, `signal`, `source`, `scenarios` (a list), `type`, `frequency`, `confidence`, `threshold`. IDs must be unique.

Optional per indicator: `status`, `last_reviewed`, `last_fired`, `notes`. If any indicator carries a status field, the register gains Status and Last Reviewed columns plus a Status Summary table, so you can see at a glance what is elevated or has fired.

Vocabulary the toolkit uses (case-insensitive):

| Field | Values | Meaning |
|-------|--------|---------|
| `type` | Leading, Confirming, Lagging | See `framework/method.md`, Stage 4 |
| `frequency` | Continuous, Daily, Weekly, Monthly, Quarterly, Annually | Drives the Monitoring Schedule table |
| `status` | Watching, Elevated, Fired, Retired | Watching = baseline; Elevated = partial evidence; Fired = threshold crossed; Retired = no longer tracked |

Values outside these lists are **still rendered** in their own row, with a warning on stderr, so a typo never silently drops an indicator from a table.

### Writing a threshold that can actually fire

A threshold is useful only if two analysts would agree whether it has been crossed. Prefer:

- a count: "two or more senior departures within a quarter"
- a comparison to a baseline: ">50% year-over-year increase"
- a named event class: "binding multilateral agreement (not a voluntary declaration)"

Avoid "significant", "major" or "rapid" on their own. If you cannot quantify, name the kind of evidence that would settle the question.

---

## Tests

```bash
python3 -m unittest discover -s scripts -p "test_*.py" -v
```

The tests check the generators and also guard against drift: the committed examples must match what the scripts produce, the GitHub Pages site must show the same probabilities, thresholds and schedule as the config, and every user-facing file must be mentioned in the README. CI runs them on every push.
