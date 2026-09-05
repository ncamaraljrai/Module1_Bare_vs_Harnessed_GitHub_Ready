# SUBMISSION.md

## Required public repository
https://github.com/ncamaraljrai/foundations_lab01_url_shortener

## Files the grader must be able to find
1. `AGENTS.md`
2. `DIAGNOSTIC_LOG.md`
3. `TASK.md` (recommended for reproducibility)

## Grading alignment

### #1 Diagnostic log completeness — weight ×5
`DIAGNOSTIC_LOG.md` contains one row for Bare, Harnessed, and Ablated plus detailed evidence sections for each.

### #2 Layer attribution accuracy — weight ×4
The attribution table forces every Bare-run failure into one named harness layer and requires concrete evidence.

### #3 AGENTS.md sufficiency — weight ×4
`AGENTS.md` includes project overview, stack, setup, repository map, constraints, verification, definition of done, and working method while staying near the requested 80–100-line target.

### #4 Specificity of observations — weight ×3
The log records timestamps, work allocation, exact commands, concrete guesses, and exact outcome evidence.

### #5 Impact of ablation — weight ×3
The ablation section requires time, verification, correctness, and guesswork deltas plus a quantitative impact statement.

## Before publishing
Do not publish `AGENTS.md` into the Bare-run worktree before running the experiment.
After all three runs are complete:
- replace every `RECORD`;
- copy the final `AGENTS.md`, `DIAGNOSTIC_LOG.md`, and `TASK.md` into the public repo;
- commit and push;
- confirm the repository is public;
- submit the repository URL above.
