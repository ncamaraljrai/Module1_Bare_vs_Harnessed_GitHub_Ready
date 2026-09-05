# TASK.md — Frozen experiment task

Use this exact one-sentence task in **all three fresh agent sessions**:

> Add optional expiration support to shortened URLs: `POST /shorten` may accept `expires_in_minutes`, expired short codes must return HTTP 410, non-expiring URLs must keep current behavior, and add regression tests.

## Controls
- Keep the coding model and model settings fixed.
- Start every run from the same Git commit.
- Use a clean branch/worktree for every run.
- Do not improve or clarify the task between runs.
- Bare run: provide only the one sentence above.
- Harnessed run: provide `AGENTS.md`, then the same sentence.
- Ablated run: provide `AGENTS_ABLATED.md`, then the same sentence.
- Stop the bare run at 15 minutes, as required by the lab.
- Record only observed evidence; do not reconstruct timings from memory later.
