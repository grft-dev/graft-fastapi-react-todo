# Agent guide

## Project intent

This is a Graftcode reference starter built with FastAPI, React, Peewee, and
SQLite. It is deliberately small and explicit so an agent can change the domain
without guessing which layer owns HTTP, business operations, or persistence.

There is no Graftcode SDK or runtime integration in this repository. Treat the
documented FastAPI contract as the stable application boundary.

## Data flow

```text
React component
  -> useTodos hook
  -> TodosApiClient
  -> FastAPI router
  -> TodoService
  -> TodoRepository
  -> Todo model / SQLite
```

Do not bypass `TodoService` from an API router or put HTTP exceptions in the
service/repository layers.

## Important paths

- `backend/app/main.py`: app factory, lifespan, middleware, router registration
- `backend/app/api/routers/todos.py`: public todo routes and HTTP error mapping
- `backend/app/services/todo_service.py`: todo application operations
- `backend/app/repositories/todo_repository.py`: database access
- `backend/app/schemas/todo.py`: public request/response models
- `backend/app/core/settings.py`: environment configuration
- `backend/tests/test_todos_api.py`: API contract tests
- `frontend/src/api/TodosApiClient.js`: browser client for `/api/todos`
- `frontend/src/hooks/useTodos.js`: React Query integration
- `frontend/src/components/`: focused presentation and interaction components
- `e2e/test_todo_e2e.py`: canonical browser tests

## Public API contract

Keep these routes stable unless the task explicitly requests an API migration:

- `GET /`
- `GET|POST /api/todos`
- `GET|PUT|DELETE /api/todos/{todo_id}`
- `POST /api/todos/{todo_id}/toggle`

Todo JSON fields are `id`, `title`, `description`, and `completed`. Creation
currently returns HTTP 200. Preserve existing `data-testid` attributes when
refactoring the UI.

## Commands

Backend setup and development:

```bash
cd backend
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
python -m pytest tests
```

Frontend:

```bash
cd frontend
npm install
npm run dev
npm run build
```

End-to-end:

```bash
cd e2e
python -m pip install -r requirements.txt
python -m playwright install chromium
python -m pytest test_todo_e2e.py
```

All tests:

```bash
python run_all_tests.py
```

The E2E suite starts the backend on `8001`, the frontend on `5175`, and stores
its SQLite database at the operating system's temporary
`todos_test.sqlite` path.

## Change workflow

When adding an operation:

1. Update request/response models in `backend/app/schemas/`.
2. Add persistence behavior in `backend/app/repositories/`.
3. Add application behavior in `backend/app/services/`.
4. Expose it in `backend/app/api/routers/`.
5. Update `frontend/src/api/` and `frontend/src/hooks/`.
6. Add backend contract tests and, for user-visible behavior, E2E coverage.

Run backend tests and the frontend build after focused changes. Run the complete
E2E suite before handing off a cross-layer change.
