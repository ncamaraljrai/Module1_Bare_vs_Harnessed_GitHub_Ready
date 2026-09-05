# GRADER_FEEDBACK_AND_RESUBMISSION.md

## Current grader result

- **Status:** Not passed yet
- **Score:** 1 / 3 stars
- **Weighted score:** 27 / 57
- **Passing threshold:** at least 2 / 3 stars

## Grader summary

The `AGENTS.md` was judged complete and well executed. The submission lost credit because the diagnostic evidence was still a template: the log contained `RECORD` placeholders instead of actual observations from the three experiment runs.

## Per-criterion feedback and required fix

### 1. Diagnostic log completeness — currently insufficient
**Grader feedback:** `DIAGNOSTIC_LOG.md` contains placeholders for all data entries.

**Fix required before resubmission:**
- Fill Bare, Harnessed, and Ablated rows with actual:
  - total time;
  - whether the result ran;
  - whether it was correct;
  - where time was spent;
  - guesses observed.
- Include exact commands/tests and concrete outcome evidence.

### 2. Layer attribution accuracy — currently insufficient
**Grader feedback:** no specific failures or layer attributions were provided.

**Fix required:**
For each observed Bare-run failure, name one precise layer:
- instruction
- tool
- environment
- state
- feedback

Then explain the observed evidence that supports the attribution.

### 3. AGENTS.md sufficiency — PASSED
**Grader feedback:** `AGENTS.md` is detailed, comprehensive, well organized, and meets the expected length.

**Action:** do not expand it further. Preserve the current file.

### 4. Specificity of observations — currently insufficient
**Grader feedback:** the log lacks specific observations about time lost/gained, timestamps, and work allocation.

**Fix required:**
Record:
- start/stop time;
- first edit time;
- first verification time;
- minutes spent exploring;
- minutes spent implementing;
- minutes spent verifying/debugging;
- concrete guesswork eliminated by the harness.

### 5. Impact of ablation — currently insufficient
**Grader feedback:** there is no quantitative or behavioral evidence showing the effect of removing the feedback subsystem.

**Fix required:**
Compare Harnessed vs Ablated using actual differences:
- time delta;
- verification delta;
- correctness delta;
- guesswork delta.

Write one final quantitative impact sentence, for example only after collecting real data:

> Removing the feedback subsystem increased verification time from X to Y minutes and caused Z concrete behavior.

## Resubmission procedure

1. Run three fresh coding-agent sessions from the exact same starting commit.
2. Keep the model/settings constant.
3. Use the exact task from `TASK.md`.
4. Bare: no `AGENTS.md`.
5. Harnessed: use `AGENTS.md`.
6. Ablated: use `AGENTS_ABLATED.md` as `AGENTS.md`.
7. Replace **every `RECORD`** in `DIAGNOSTIC_LOG.md` with observed evidence.
8. Verify there are no remaining `RECORD` tokens:
   ```bash
   grep -R "RECORD" -n DIAGNOSTIC_LOG.md
   ```
   The command should return nothing.
9. Commit and push the completed files.
10. Submit the public repository link again.

## Final gate before Submit again

The package is ready for resubmission only when:

- [ ] Bare row contains actual data
- [ ] Harnessed row contains actual data
- [ ] Ablated row contains actual data
- [ ] at least one Bare failure has precise layer attribution
- [ ] work allocation/timestamps are specific
- [ ] harnessed-vs-ablated impact is quantitative or behaviorally concrete
- [ ] no `RECORD` placeholders remain
- [ ] `AGENTS.md` remains unchanged unless a real experiment finding requires a correction

The grader screenshots are included in `grader_feedback/`.
