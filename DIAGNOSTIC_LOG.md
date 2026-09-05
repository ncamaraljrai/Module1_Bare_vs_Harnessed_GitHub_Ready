# Diagnostic Log — Bare vs. Harnessed Ablation Experiment

Repository: `ncamaraljrai/foundations_lab01_url_shortener`

Task: Add optional expiration support to shortened URLs: POST /shorten may accept `expires_in_minutes`, expired short codes must return HTTP 410, non-expiring URLs must keep current behavior, and add regression tests.

> Fill this file only from the actual three fresh-session runs. Do not invent timings or outcomes.

## Three-run log

| Run | Harness state | Runs? | Correct? | Time / where time went | Guesses observed |
|---|---|---|---|---|---|
| Bare | none | RECORD | RECORD | RECORD | RECORD |
| Harnessed | full minimal | RECORD | RECORD | RECORD | RECORD |
| Ablated | full minus feedback/verification | RECORD | RECORD | RECORD | RECORD |

## Run 1 — Bare evidence

- Total time: `RECORD`
- Time exploring repo: `RECORD`
- Time implementing: `RECORD`
- Time verifying: `RECORD`
- Commands the agent discovered by itself: `RECORD`
- Tests actually run: `RECORD`
- Result runs: `YES / NO`
- Result correct: `YES / NO`

Concrete guesses:
1. `RECORD`
2. `RECORD`
3. `RECORD`

Observed failures:
1. `RECORD`
2. `RECORD`
3. `RECORD`

## Run 2 — Harnessed evidence

- Total time: `RECORD`
- Time exploring repo: `RECORD`
- Time implementing: `RECORD`
- Time verifying: `RECORD`
- Verification commands used from AGENTS.md: `RECORD`
- Result runs: `YES / NO`
- Result correct: `YES / NO`

Guesswork eliminated:
1. `RECORD`
2. `RECORD`
3. `RECORD`

Specific verification behavior:
- `RECORD`

## Run 3 — Ablated evidence

Ablated subsystem: **Feedback** — remove only the Verification commands section from `AGENTS.md`.

- Total time: `RECORD`
- Time exploring repo: `RECORD`
- Time implementing: `RECORD`
- Time verifying: `RECORD`
- Did it independently discover and run the correct tests? `RECORD`
- Result runs: `YES / NO`
- Result correct: `YES / NO`

Measured degradation versus harnessed:
- `RECORD`

## Layer attribution for bare-run failures

Use only: instruction / tool / environment / state / feedback.

| Bare-run failure | Layer | Evidence |
|---|---|---|
| RECORD | RECORD | RECORD |
| RECORD | RECORD | RECORD |
| RECORD | RECORD | RECORD |

## Reflection

### Subsystem that mattered most
`RECORD — cite the comparison between runs.`

### Failure I would previously have blamed on the model
`RECORD — identify the failure and the harness layer that actually caused it.`

### First AGENTS.md change I would make in a real project
`RECORD — make it evidence-based from this experiment.`

## Quality-bar check

Before submission, make sure you can point to:
- one concrete time-saving observation;
- one specific guess removed by AGENTS.md;
- one verification difference between harnessed and ablated;
- one measurable performance/correctness drop caused by ablation;
- one precise layer attribution supported by evidence.
