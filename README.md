# Graftcode FastAPI + React Todo

A small full-stack reference application designed to be easy for people and coding
agents to understand, run, and adapt.

## What “Graftcode” means here

This repository demonstrates a clearly layered existing application that can be
used as a Graftcode starter or reference project. Its business operations are
kept behind a stable HTTP contract so tools and agents can build on trusted
application logic.

This repository does **not** contain a Graftcode runtime, SDK, or production
agent integration. Those integrations should call or expose the documented
application boundary instead of depending on UI implementation details.

## Stable application boundary

The public todo contract is:

- `GET /` — API metadata
- `GET /api/todos` — list todos
- `POST /api/todos` — create a todo
- `GET /api/todos/{todo_id}` — get one todo
- `PUT /api/todos/{todo_id}` — update a todo
- `POST /api/todos/{todo_id}/toggle` — toggle completion
- `DELETE /api/todos/{todo_id}` — delete a todo

Todo responses contain `id`, `title`, `description`, and `completed`. See the
generated OpenAPI document at `http://localhost:8000/docs`.

## Architecture

```text
React components
  -> useTodos
  -> TodosApiClient
  -> FastAPI todo router
  -> TodoService
  -> TodoRepository
  -> Peewee / SQLite
```

Backend responsibilities:

- `backend/app/api/routers/` translates HTTP requests and errors.
- `backend/app/services/` contains application operations.
- `backend/app/repositories/` owns persistence queries.
- `backend/app/models/` contains Peewee database models.
- `backend/app/schemas/` defines the public API contracts.
- `backend/app/core/` contains settings and database infrastructure.
- `backend/app/domain/` contains framework-independent domain errors.

Frontend responsibilities:

- `frontend/src/api/` contains transport and resource clients.
- `frontend/src/hooks/` manages server state with TanStack Query.
- `frontend/src/components/` contains focused UI components.
- `frontend/src/App.jsx` composes the application screen.

## Local development

Prerequisites: Python 3.11+, Node.js 18+, and npm.

```bash
cd backend
python -m venv .venv
# Activate .venv using the command for your shell
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload --port 8000
```

In another terminal:

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173`. The API runs at `http://localhost:8000`.

## Tests

Backend contract tests:

```bash
cd backend
python -m pytest tests
```

The canonical browser suite is the Python Playwright suite under `e2e/`:

```bash
cd e2e
python -m pip install -r requirements.txt
python -m playwright install chromium
python -m pytest test_todo_e2e.py
```

It starts isolated services on ports `8001` and `5175` and uses
`todos_test.sqlite` in the operating-system temporary directory.

To run both complete suites:

```bash
python run_all_tests.py
```

Cross-platform Invoke aliases are also available in `tasks.py`, for example
`inv backend`, `inv frontend`, and `inv test-all`.

## Configuration

- `APP_ENV`: `development` (default), `test`, or `production`
- `DATABASE_PATH`: optional SQLite path override
- `SERVER_HOST`: optional backend host override
- `SERVER_PORT`: optional backend port override
- `VITE_API_URL`: frontend API origin; defaults to `http://localhost:8000`

## Docker

```bash
docker compose up --build
```

Production data is persisted as `/app/data/todos_production.sqlite` in the
`sqlite_data` volume.
