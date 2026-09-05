# Experiment Task

Use this exact one-sentence task in all three fresh agent sessions:

> Add optional expiration support to shortened URLs: POST /shorten may accept `expires_in_minutes`, expired short codes must return HTTP 410, non-expiring URLs must keep current behavior, and add regression tests.

## Experiment controls

- Keep the coding model fixed across all three runs.
- Use a clean branch/worktree for each run.
- Use the same repository revision for each run.
- Hard-stop the bare run at 15 minutes as required by the lab.
- Do not improve the task wording between runs.

## Run 1 — Bare
Give the agent only the one-sentence task above.

## Run 2 — Harnessed
Give the agent `AGENTS.md`, then the same one-sentence task.

## Run 3 — Ablated
Give the agent the same `AGENTS.md` but delete only the **Verification commands** section.
Then give the same one-sentence task.
