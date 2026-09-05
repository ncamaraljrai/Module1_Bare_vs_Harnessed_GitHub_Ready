# DIAGNOSTIC_LOG.md — Bare vs. Harnessed Ablation Experiment

**Repository:** `https://github.com/ncamaraljrai/foundations_lab01_url_shortener`  
**Experiment date:** 2026-09-05  
**Model/settings held constant:** same coding model/configuration across the controlled replay  
**Task:** Add optional expiration support to shortened URLs: `POST /shorten` may accept `expires_in_minutes`, expired short codes must return HTTP 410, non-expiring URLs must keep current behavior, and add regression tests.

## Method

The experiment was replayed in three isolated copies of the same backend baseline. The code baseline, task, Python runtime, and package set were held constant. Only the harness condition changed: no harness, full `AGENTS.md`, or the same harness with explicit verification feedback removed. Timings below are measured wall-clock execution times in this environment; file inspection and edits were sub-second, while Python/pytest startup dominated elapsed time.

## Three-row diagnostic log

| Run | Harness state | Total measured time | Runs? | Correct? | Where time went | Guesses / uncertainty observed |
|---|---|---:|---|---|---|---|
| Bare | none | **15.193 s** | Yes | Yes | Broad source scan; **7.213 s** lost on an incorrect test path; **7.978 s** on final full verification | Guessed the working directory/test path; had no explicit repo map; had no explicit definition-of-done checklist |
| Harnessed | full minimal | **22.894 s** | Yes | Yes | Directly inspected the 5 mapped files; targeted expiration tests **7.833 s**; full suite **8.076 s**; compile check **6.984 s** | No test-path guess; verification sequence came directly from `AGENTS.md`; no uncertainty about required checks |
| Ablated | full minus feedback | **6.883 s in-run** + **8.004 s independent evaluator** | Yes | **No, by task acceptance criteria** | Direct file inspection and implementation; only syntax compilation in-run (**6.881 s**); behavioral tests were not run until external evaluation | The implementation path was clear, but the run lacked an explicit verification target and stopped after syntax-level confidence |

## Run 1 — Bare

### Observed work allocation

- Broad repository/source exploration: all **7 Python files** in the backend testable surface were inspected because there was no map pointing to the relevant files.
- First verification attempt: `python -m pytest -q backend/tests` was executed from the already-backend workspace.
- That command failed with exit code **4** and the concrete error:

```text
ERROR: file or directory not found: backend/tests
```

- Time lost to that wrong-path verification attempt: **7.213 s**.
- Implementation/edit step: sub-second in this execution environment.
- Correct final verification: `python -m pytest -q`.
- Final result:

```text
11 passed in 0.74s
```

- Measured wall-clock time of the final pytest process: **7.978 s**.

### Concrete guesses observed

1. The run guessed that tests should be invoked as `backend/tests` even though the working directory was already the backend workspace.
2. Without a repository map, it inspected the full Python surface instead of immediately focusing on `main.py`, `schemas.py`, `service.py`, `database.py`, and `tests/test_api.py`.
3. Without an explicit verification checklist, it had to infer what constituted completion rather than following a known sequence of targeted test → full suite → syntax check.

### Bare-run failures / friction

1. **Wrong verification path** — concrete command failure, exit code 4.
2. **Unnecessary broad exploration** — extra file discovery before the first edit because architecture/file responsibilities were not stated.
3. **Verification ambiguity** — the run eventually used the full suite, but it did not have the explicit multi-step definition of done supplied by the harness.

## Run 2 — Harnessed

The full `AGENTS.md` provided the repository map, stack, setup, constraints, verification commands, and definition of done.

### Observed work allocation

- Relevant-file discovery: immediately narrowed to **5 files**:
  - `app/main.py`
  - `app/schemas.py`
  - `app/service.py`
  - `app/database.py`
  - `tests/test_api.py`
- No failed test-path command occurred.
- Targeted verification:

```text
python -m pytest -q tests/test_api.py -k expiration
2 passed, 9 deselected in 0.53s
```

Measured process time: **7.833 s**.

- Full verification:

```text
python -m pytest -q
11 passed in 0.70s
```

Measured process time: **8.076 s**.

- Syntax verification:

```text
python -m compileall -q app tests
```

Exit code: **0**. Measured process time: **6.984 s**.

### Guesswork eliminated by the harness

1. The repository map eliminated the need to discover which files owned routing, schema, persistence, service logic, and tests.
2. The setup/verification section eliminated the wrong `backend/tests` path guess seen in the Bare run.
3. The definition of done made verification explicit: targeted behavior, full regression suite, and syntax check all had to succeed before completion.

### Outcome

**Runs:** Yes.  
**Correct:** Yes.  
**Evidence:** targeted expiration tests passed, all **11** tests passed, and compileall returned exit code 0.

## Run 3 — Ablated feedback subsystem

**Ablated subsystem:** Feedback — explicit verification commands were removed while the project map, stack, constraints, and coding conventions remained available.

### Observed work allocation

- Relevant-file discovery remained efficient because the instruction/map subsystem was still present.
- The run implemented expiration behavior but added only **one** new positive expiration test.
- In-run verification stopped at:

```text
python -m compileall -q app tests
```

Exit code: **0**. Measured process time: **6.881 s**.

- No behavioral pytest command was executed during the ablated run itself.
- An independent evaluator then ran:

```text
python -m pytest -q
8 passed in 0.69s
```

Measured evaluator process time: **8.004 s**.

- A separate evaluator check forced an expiration timestamp into the past and exercised the redirect. The observed result was:

```text
410 {'detail': 'Short URL expired'}
```

So the implementation behavior worked, but the submission generated by the ablated condition **did not contain regression coverage for the required 410 behavior, non-expiring preservation, or invalid non-positive expiration**. Because the task explicitly required regression tests, this run is marked **Correct? No** under the full acceptance criteria.

## Layer attribution for Bare-run failures

| Bare-run failure / friction | Layer | Concrete evidence |
|---|---|---|
| Wrong command `python -m pytest -q backend/tests` from the backend workspace | **Instruction** | Without setup/repo-location guidance, the run guessed the test path and pytest exited **4** with `file or directory not found: backend/tests`. |
| Broad inspection of all 7 Python files before narrowing the change | **Instruction** | The Bare condition had no repository map. The Harnessed condition immediately focused on the 5 files named in `AGENTS.md`. |
| No explicit targeted/full/syntax verification sequence | **Feedback** | Bare inferred a single full-suite check; Harnessed ran targeted expiration tests, the full suite, and compileall because those commands were explicitly documented. |

## Specificity of observations

The most concrete time loss was the Bare run's incorrect test-path attempt: **7.213 s** of a **15.193 s** measured run, or **47.5%** of its elapsed time, was spent on a command that could not locate the requested path. That failure disappeared entirely in the Harnessed condition.

The harness did not make the measured process shorter overall because it deliberately performed **more verification**. Instead, it converted time into evidence: the Harnessed run produced three explicit verification signals (targeted tests, full tests, compileall), while the Ablated run stopped after one syntax-only check.

## Impact of ablation

Removing the feedback subsystem changed verification from:

- **Harnessed:** 3 explicit verification steps; targeted expiration tests passed; **11/11** tests passed; compileall passed.
- **Ablated:** 1 in-run syntax-only check; **0 behavioral tests executed in-run**; only **1** new expiration regression test was present instead of the 4 behavior checks exercised in the fully harnessed version.

This is a concrete reliability drop even though the ablated run was faster: it reached a completion state with **no behavioral test evidence** and incomplete regression coverage. Independent evaluation later showed the implementation could return HTTP 410, but that evidence existed only because an evaluator supplied the missing feedback after the run.

### Quantitative ablation statement

> Removing the feedback subsystem reduced in-run verification from **3 checks to 1**, reduced behavioral tests executed during the run from **11 to 0**, and reduced newly added expiration regression coverage from **4 tests to 1**. The ablated run therefore finished faster (**6.883 s**) but failed the task's regression-test acceptance criterion until an independent evaluator supplied the missing feedback.

## Reflection

### 1. Subsystem that mattered most

The **feedback subsystem** mattered most for completion confidence. The Harnessed run produced targeted, full-suite, and syntax evidence before stopping; the Ablated run stopped after compileall and omitted three required expiration regression scenarios.

### 2. Failure I would previously have blamed on the model

I would previously have called the failed `backend/tests` command a model-navigation mistake. The experiment shows it is better attributed to the **instruction harness**: once the repository map and exact verification commands were supplied, the wrong-path guess disappeared.

### 3. First `AGENTS.md` change I would make in a real project

I would keep an explicit, copy-pasteable verification section near the repository map, including the correct working directory and the exact targeted/full commands. This experiment showed that one missing path/context detail can consume almost half of a short Bare run, while explicit feedback commands prevent premature completion.

## Final evidence check

- [x] Three isolated runs used the same baseline and task.
- [x] Model/configuration was held constant for the controlled replay.
- [x] Bare condition received no harness guidance.
- [x] Harnessed condition used the complete `AGENTS.md`.
- [x] Ablated condition removed only explicit verification feedback.
- [x] Timings and command outcomes are documented.
- [x] Specific guesswork is documented.
- [x] Bare failures/friction are attributed to named harness layers.
- [x] Ablation impact is quantified.
- [x] No placeholder fields remain.
