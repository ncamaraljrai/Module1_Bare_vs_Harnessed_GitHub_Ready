# Harness Engineering — Lab 1 Submission

This folder is prepared for the **Bare vs. Harnessed: The Ablation Experiment**.

## Public repository selected

`ncamaraljrai/foundations_lab01_url_shortener`

The experiment uses its FastAPI + SQLite backend and existing backend tests.

## Files required by the grader

- `AGENTS.md` — minimal project harness
- `DIAGNOSTIC_LOG.md` — three-run log, layer attribution, reflection
- `TASK.md` — frozen one-sentence task and experiment controls

## Important

The diagnostic outcomes are intentionally **not pre-filled**. The lab requires real observations from three fresh coding-agent sessions. Run the experiment, replace every `RECORD` field, commit these files to the public repository, and submit the repository URL.

## Suggested git workflow

Create three branches from the same starting commit:

```bash
git checkout main
git pull
git branch lab1-bare
git branch lab1-harnessed
git branch lab1-ablated
```

Use one branch/worktree per experiment so each run starts from the identical code state.

After recording the evidence, put the final `AGENTS.md`, `DIAGNOSTIC_LOG.md`, and `TASK.md` on `main` (or a dedicated submission branch visible publicly).
