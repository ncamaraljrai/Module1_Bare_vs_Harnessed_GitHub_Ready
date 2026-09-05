# AGENTS.md

## Project overview
This repository is a URL shortener built as a small full-stack application.
The backend is FastAPI + SQLite; the frontend is Next.js + TypeScript.
The backend owns URL validation, code generation, persistence, and redirects.
The frontend calls the backend API and presents loading, success, copy, and error states.

## Stack and versions
- Python 3.10+
- FastAPI >=0.115,<1
- Uvicorn >=0.30,<1
- Pydantic >=2.8,<3
- Pytest >=8,<9
- HTTPX >=0.27,<1
- SQLite
- Next.js + TypeScript
- Node.js / npm

## Key backend files
- backend/app/main.py — FastAPI routes and HTTP behavior
- backend/app/schemas.py — Pydantic request/response models
- backend/app/service.py — short-code generation and persistence logic
- backend/app/database.py — SQLite connection and schema setup
- backend/tests/ — backend regression tests
- backend/requirements.txt — Python dependencies

## Existing behavior
- POST /shorten accepts a URL and returns a six-character short code.
- Duplicate URLs reuse the existing short code.
- GET /{short_code} redirects with HTTP 307.
- Unknown or malformed short codes return 404.
- URL validation is performed by Pydantic.
- SQLite stores the mapping.
- /health returns a basic health response.

## Setup — backend
From the repository root:

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

macOS/Linux activation:
```bash
source .venv/bin/activate
```

## Run — backend
```powershell
cd backend
uvicorn app.main:app --reload --port 8000
```

API docs:
- http://localhost:8000/docs

## Setup — frontend
```powershell
cd frontend
npm install
Copy-Item .env.local.example .env.local
npm run dev
```

## Non-negotiable constraints
1. Preserve the existing POST /shorten contract unless the task explicitly changes it.
2. Preserve six-character alphanumeric short codes.
3. Preserve duplicate-URL idempotency.
4. Keep URL validation in the Pydantic request schema.
5. Keep database operations in the existing service/database layers.
6. Do not move SQL into route handlers unless there is no viable existing abstraction.
7. Preserve HTTP 307 for successful redirects.
8. Preserve HTTP 404 for unknown short codes.
9. Add regression tests for every behavior change.
10. Do not silently change deployment configuration.
11. Keep environment-specific URLs in environment variables.
12. Avoid introducing a new dependency when the standard library or current stack is sufficient.
13. Keep error responses deterministic and testable.
14. Do not claim completion before verification commands run.

## Coding conventions
- Prefer explicit type hints.
- Follow the existing separation: route -> service -> database.
- Keep Pydantic models small and API-focused.
- Use parameterized SQL.
- Keep helper functions focused.
- Preserve existing naming style.
- Add comments only when they explain a non-obvious design decision.
- Keep changes scoped to the requested feature.

## Verification commands
Run these before declaring the task complete.

Backend tests:
```powershell
cd backend
python -m pytest -q
```

Backend syntax:
```powershell
python -m compileall app tests
```

Manual API smoke:
```powershell
uvicorn app.main:app --port 8000
```

Then verify:
- POST /shorten with a valid HTTPS URL succeeds.
- Repeating the same URL returns the same code.
- Invalid URL is rejected.
- GET /{short_code} redirects with 307.
- Unknown code returns 404.
- Any new behavior from the task has a direct regression check.

## Definition of done
- Requested behavior is implemented.
- Existing backend tests still pass.
- New regression tests cover the feature.
- No unrelated files were rewritten.
- Existing redirect and duplicate behavior still works.
- Any schema/database change is reflected consistently across layers.
- Verification evidence is reported accurately.

## Working method
Inspect the relevant files before editing.
State assumptions explicitly instead of guessing.
Make the smallest coherent change.
Run narrow tests first, then the full backend suite.
If verification cannot run, report the blocker instead of claiming success.
