# DIAGNOSTIC_LOG.md — Bare vs. Harnessed Ablation Experiment

**Repository:** `https://github.com/ncamaraljrai/foundations_lab01_url_shortener`  
**Starting commit:** `RECORD`  
**Model/settings held constant:** `RECORD`  
**Task:** Add optional expiration support to shortened URLs: `POST /shorten` may accept `expires_in_minutes`, expired short codes must return HTTP 410, non-expiring URLs must keep current behavior, and add regression tests.

> Replace every `RECORD` with actual evidence from the three fresh-session runs.

## Three-row diagnostic log

| Run | Harness state | Total time | Runs? | Correct? | Where time went | Guesses observed |
|---|---:|---:|---|---|---|---|
| Bare | none | `RECORD` | `Y/N` | `Y/N` | `RECORD: exploration / implementation / verification` | `RECORD` |
| Harnessed | full minimal | `RECORD` | `Y/N` | `Y/N` | `RECORD: exploration / implementation / verification` | `RECORD` |
| Ablated | full minus feedback | `RECORD` | `Y/N` | `Y/N` | `RECORD: exploration / implementation / verification` | `RECORD` |

## Run 1 — Bare

**Start / stop:** `RECORD`  
**First edit at:** `RECORD`  
**First verification at:** `RECORD / none`

**Observed work allocation**
- Repo exploration: `RECORD`
- Implementation: `RECORD`
- Verification/debugging: `RECORD`

**Commands discovered/run**
```text
RECORD
```

**Concrete guesses made by the agent**
1. `RECORD`
2. `RECORD`
3. `RECORD`

**Failures or defects observed**
1. `RECORD`
2. `RECORD`
3. `RECORD`

**Outcome evidence**
```text
RECORD exact test result / error / acceptance-check result
```

## Run 2 — Harnessed

**Start / stop:** `RECORD`  
**First edit at:** `RECORD`  
**First verification at:** `RECORD`

**Observed work allocation**
- Repo exploration: `RECORD`
- Implementation: `RECORD`
- Verification/debugging: `RECORD`

**Harness instructions used**
1. `RECORD`
2. `RECORD`
3. `RECORD`

**Guesswork eliminated relative to Bare**
1. `RECORD`
2. `RECORD`
3. `RECORD`

**Verification commands actually run**
```text
RECORD
```

**Outcome evidence**
```text
RECORD exact test result / acceptance-check result
```

## Run 3 — Ablated feedback subsystem

**Ablated subsystem:** Feedback / explicit verification commands  
**Start / stop:** `RECORD`  
**First edit at:** `RECORD`  
**First verification at:** `RECORD / none`

**Observed work allocation**
- Repo exploration: `RECORD`
- Implementation: `RECORD`
- Verification/debugging: `RECORD`

**Did the agent independently discover the correct verification commands?** `RECORD`

**What degraded compared with the harnessed run?**
- Time delta: `RECORD`
- Verification delta: `RECORD`
- Correctness delta: `RECORD`
- Guesswork delta: `RECORD`

**Outcome evidence**
```text
RECORD exact test result / acceptance-check result
```

## Layer attribution for Bare-run failures

Allowed layers: **instruction / tool / environment / state / feedback**

| Bare-run failure | Layer | Concrete evidence for attribution |
|---|---|---|
| `RECORD` | `RECORD` | `RECORD` |
| `RECORD` | `RECORD` | `RECORD` |
| `RECORD` | `RECORD` | `RECORD` |

## Reflection

### 1. Subsystem that mattered most
`RECORD. Name one subsystem and cite the measured difference between runs.`

### 2. Failure I would previously have blamed on the model
`RECORD. State the observed failure, the correct harness layer, and the evidence.`

### 3. First AGENTS.md change I would make in a real project
`RECORD. Tie the change directly to this experiment rather than giving a generic recommendation.`

## Ablation impact statement

Use a quantitative sentence wherever the evidence permits:

> Removing the `RECORD` subsystem changed `RECORD metric` from `RECORD` to `RECORD`, and caused `RECORD concrete behavioral difference`.

## Final evidence check

- [ ] All three runs started from the same commit.
- [ ] All three used the same model/settings.
- [ ] All three used the identical task sentence.
- [ ] Bare run received no `AGENTS.md`.
- [ ] Harnessed run received the complete `AGENTS.md`.
- [ ] Ablated run removed only the feedback subsystem.
- [ ] The table contains actual timings/outcomes.
- [ ] At least one specific guess is documented.
- [ ] At least one failure has precise layer attribution.
- [ ] The ablation section shows a measurable drop or behavioral difference.
- [ ] Claims of correctness are backed by test/acceptance evidence.
