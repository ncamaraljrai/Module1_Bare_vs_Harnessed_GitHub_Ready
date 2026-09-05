# EXPERIMENT_RUNBOOK.md

## 1. Freeze the starting point
Record the exact starting commit:

```bash
git rev-parse HEAD
```

Starting SHA: `RECORD`

Create three worktrees from that same SHA:

```bash
git worktree add ../url-shortener-bare -b lab1-bare HEAD
git worktree add ../url-shortener-harnessed -b lab1-harnessed HEAD
git worktree add ../url-shortener-ablated -b lab1-ablated HEAD
```

Do **not** place `AGENTS.md` in the bare worktree.

## 2. Run 1 — Bare
Open a fresh coding-agent session in `url-shortener-bare`.
Give it only the sentence from `TASK.md`.
Start a timer. Hard stop at 15 minutes.
Record exploration, implementation, verification, guesses, commands, and outcome.

## 3. Run 2 — Harnessed
Copy `AGENTS.md` into the repository root of `url-shortener-harnessed`.
Open a fresh session.
Tell the agent to read `AGENTS.md`, then give the exact same task sentence.
Record the same metrics.

## 4. Run 3 — Ablated
Copy `AGENTS_ABLATED.md` into the repository root of `url-shortener-ablated` **as `AGENTS.md`**.
Open a fresh session and give the exact same task.
The only removed subsystem is explicit verification feedback.
Record whether the agent independently discovers and runs the correct checks.

## 5. What counts as “Runs?” and “Correct?”
**Runs? = Yes** only if the changed code starts/imports and the relevant automated tests can execute.
**Correct? = Yes** only if all task acceptance criteria are met and pre-existing behavior is preserved.

For this task, verify:
1. Omitting `expires_in_minutes` preserves current behavior.
2. Providing a valid positive expiration creates an expiring short URL.
3. Before expiry, the redirect remains HTTP 307.
4. After expiry, the short code returns HTTP 410.
5. Unknown/malformed codes remain HTTP 404.
6. Duplicate/non-expiring behavior is not accidentally broken.
7. Regression tests cover expiration.

## 6. Timing discipline
Record timestamps at:
- session start;
- first code edit;
- first verification command;
- session stop.

This makes “where time went” measurable rather than impressionistic.

## 7. After all runs
Fill `DIAGNOSTIC_LOG.md`.
Use actual observations and exact commands/errors where possible.
Only after the experiment is complete should you commit the final submission files to the public repository.
