"""FastAPI application entrypoint."""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers import root_router, todos_router
from app.core.database import database
from app.core.settings import settings
from app.models import Todo


@asynccontextmanager
async def lifespan(_: FastAPI):
    if database.is_closed():
        database.connect()
    database.create_tables([Todo], safe=True)

    yield

    if not database.is_closed():
        database.close()


def create_app() -> FastAPI:
    application = FastAPI(title=settings.app_title, lifespan=lifespan)
    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.include_router(root_router)
    application.include_router(todos_router)
    return application


app = create_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host=settings.server_host,
        port=settings.server_port,
        reload=settings.reload,
    )
