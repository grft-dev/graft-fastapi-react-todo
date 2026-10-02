"""Cross-platform Invoke tasks for local development."""

import shutil
import sys
from pathlib import Path

from invoke import task


PYTHON = f'"{sys.executable}"'
ROOT = Path(__file__).resolve().parent


@task
def backend(ctx):
    """Run the FastAPI development server."""
    with ctx.cd(str(ROOT / "backend")):
        ctx.run(f"{PYTHON} -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000")


@task
def frontend(ctx):
    """Run the React development server."""
    with ctx.cd(str(ROOT / "frontend")):
        ctx.run("npm run dev")


@task
def test_api(ctx):
    """Run all backend API tests."""
    with ctx.cd(str(ROOT / "backend")):
        ctx.run(f"{PYTHON} -m pytest tests")


@task
def test_e2e(ctx):
    """Run all browser end-to-end tests."""
    with ctx.cd(str(ROOT / "e2e")):
        ctx.run(f"{PYTHON} -m pytest test_todo_e2e.py")


@task(test_api, test_e2e)
def test_all(_):
    """Run backend and browser tests."""


@task
def install_backend(ctx):
    with ctx.cd(str(ROOT / "backend")):
        ctx.run(f"{PYTHON} -m pip install -r requirements.txt")


@task
def install_frontend(ctx):
    with ctx.cd(str(ROOT / "frontend")):
        ctx.run("npm install")


@task(install_backend, install_frontend)
def install(_):
    """Install backend and frontend dependencies."""


@task
def build_frontend(ctx):
    with ctx.cd(str(ROOT / "frontend")):
        ctx.run("npm run build")


@task
def docker_up(ctx):
    ctx.run("docker compose up --build")


@task
def docker_down(ctx):
    ctx.run("docker compose down")


@task
def clean(_):
    """Remove generated caches, builds, and local databases."""
    paths = [
        ROOT / "backend" / ".pytest_cache",
        ROOT / "backend" / "todos_development.sqlite",
        ROOT / "frontend" / "dist",
        ROOT / "e2e" / ".pytest_cache",
    ]
    for path in paths:
        if path.is_dir():
            shutil.rmtree(path)
        elif path.exists():
            path.unlink()
