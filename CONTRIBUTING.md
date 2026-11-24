# Contributing

Thanks for using the toolkit. The most valuable contribution is evidence that it works somewhere new.

## Share a scenario set you built with it

If you adapted the method to your own domain, open an issue using the **"Share a scenario set"** template. Include your focal question, the two axes, the four scenario names, and a link if the work is public. Sets that are shared get listed in the Showcase below so other practitioners can see the range of domains the method handles. Confidential work is welcome in anonymised form (axes and scenario names only).

## Report an inconsistency or a bug

Open an issue with the **"Bug or inconsistency"** template. The repo has one worked example that appears in several places (framework docs, generated examples, the site), and the most useful reports are "file A says X, file B says Y". The test suite catches many of these; if you found one it did not, say so and we will add a check.

## Improve the content

Pull requests are welcome for:

- Clearer wording, better examples, fixed links.
- New worked examples in `guides/adaptation.md` style (a different domain, fully worked through all five stages).
- Template improvements that make a step easier to do.
- Translations of the templates and cheat sheet.

Please keep these conventions:

- **Date your examples.** Any example that contains a probability, a threshold or a narrative gets an explicit "as of" note. Scenario work goes stale; the toolkit should model saying so.
- **One source of truth for the worked example.** Scenario names, probabilities and indicator thresholds live in `scripts/*.json`. If you change them there, regenerate `examples/` and update `framework/` and `docs/index.html` to match. The tests will tell you if you missed one.
- **No new dependencies.** The scripts are standard-library Python 3.8+ on purpose, so a strategy team can run them without a developer.
- **Plain Markdown.** Tables and fenced code blocks; nothing that needs a particular renderer.

## Running the checks

```bash
# Regenerate the example outputs after editing a config
python3 scripts/generate_matrix.py --output examples/scenario_matrix.md
python3 scripts/generate_indicators.py --output examples/indicator_register.md --csv examples/indicator_register.csv

# Run the tests (also run in CI on every push)
python3 -m unittest discover -s scripts -p "test_*.py" -v
```

The tests check the generators and guard against drift between the configs, the committed examples, the framework docs, the README and the GitHub Pages site.

## Showcase

Scenario sets built with this toolkit. Add yours via the issue template.

| Domain | Focal question (short) | Axes | By |
|--------|------------------------|------|----|
| AI governance 2024-2030 | How will global AI governance evolve? | Capability: Incremental ↔ Discontinuous; Regulation: Fragmented ↔ Harmonized | this repo (`framework/`) |
| Energy transition 2025-2035 | Portfolio strategy for a mid-size oil & gas company | Transition pace: Gradual ↔ Rapid; Policy: Supportive ↔ Volatile | this repo (`guides/adaptation.md`) |

## License

By contributing you agree that your contribution is licensed under the MIT License that covers the project.
