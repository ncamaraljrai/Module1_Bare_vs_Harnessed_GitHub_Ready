# AGENTS.md
## Project overview
This repository is a full-stack URL shortener.
The backend is FastAPI + SQLite; the frontend is Next.js + TypeScript.
Backend responsibilities: validation, short-code generation, persistence, redirects.
Frontend responsibilities: API calls, loading/error states, result display, copy action.
## Stack
- Python 3.10+
- FastAPI >=0.115,<1
- Uvicorn >=0.30,<1
- Pydantic >=2.8,<3
- Pytest >=8,<9
- HTTPX >=0.27,<1
- SQLite
- Next.js + TypeScript
- Node.js / npm
## Repository map
- `backend/app/main.py` — FastAPI routes and HTTP behavior
- `backend/app/schemas.py` — request/response models
- `backend/app/service.py` — code generation and URL lookup/create logic
- `backend/app/database.py` — SQLite connection and schema initialization
- `backend/tests/test_api.py` — API regression tests
- `backend/requirements.txt` — Python dependencies
- `frontend/` — Next.js application
## Existing backend behavior
- `POST /shorten` accepts a URL and returns a 6-character alphanumeric code.
- Re-submitting the same URL returns the existing code.
- `GET /{short_code}` redirects with HTTP 307.
- Unknown or malformed codes return HTTP 404.
- URL validation is handled by Pydantic.
- `/health` returns `{"status": "ok"}`.
## Backend setup
From repository root:
```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```
macOS/Linux activation: `source .venv/bin/activate`
## Backend run
```powershell
cd backend
uvicorn app.main:app --reload --port 8000
```
API docs: `http://localhost:8000/docs`
## Non-negotiable constraints
1. Preserve the existing `/shorten` contract except where the task explicitly extends it.
2. Preserve 6-character alphanumeric short codes.
3. Preserve duplicate-URL idempotency.
4. Keep request validation in Pydantic schemas.
5. Keep persistence concerns in `database.py` / `service.py`, not route handlers.
6. Use parameterized SQL.
7. Preserve HTTP 307 for valid, non-expired redirects.
8. Preserve HTTP 404 for unknown or malformed codes.
9. Add regression tests for every requested behavior change.
10. Avoid new dependencies unless the existing stack or standard library cannot solve it.
11. Keep environment-specific configuration in environment variables.
12. Do not rewrite unrelated files.
13. Keep error behavior deterministic and testable.
14. Do not declare completion before verification.
## Coding conventions
- Use explicit type hints where practical.
- Follow the existing route -> service -> database separation.
- Keep Pydantic models API-focused.
- Prefer small, focused helper functions.
- Preserve current naming style.
- Make the smallest coherent change.
- State assumptions instead of silently guessing.
## Verification commands — intentionally ablated for Run 3
_This feedback subsystem has been removed for the ablation experiment._
## Definition of done
- Requested behavior is implemented.
- New regression tests cover the feature.
- Existing backend tests still pass.
- Syntax compilation passes.
- Existing duplicate and redirect behavior remains intact.
- Schema, service, database, and tests agree on any new field.
- Verification evidence is reported accurately.
## Working method
Inspect the smallest relevant file set first.
Implement the narrowest correct change.
Run targeted verification, then the full backend checks.
If a check cannot run, report the blocker instead of claiming success.
