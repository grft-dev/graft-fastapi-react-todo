"""Environment-based application settings."""

import os
import tempfile
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    environment: str
    database_path: str
    server_host: str
    server_port: int
    cors_origins: list[str]
    app_title: str
    reload: bool


def load_settings() -> Settings:
    environment = os.getenv("APP_ENV", "development")

    if environment == "test":
        defaults = {
            "database_path": os.path.join(tempfile.gettempdir(), "todos_test.sqlite"),
            "server_port": 8001,
            "cors_origins": ["http://localhost:5175"],
            "app_title": "Todo API - Test",
            "reload": False,
        }
    elif environment == "production":
        defaults = {
            "database_path": "todos_production.sqlite",
            "server_port": 8000,
            "cors_origins": [],
            "app_title": "Todo API - Production",
            "reload": False,
        }
    else:
        defaults = {
            "database_path": "todos_development.sqlite",
            "server_port": 8000,
            "cors_origins": [
                "http://localhost:5173",
                "http://localhost:5174",
                "http://localhost:3000",
            ],
            "app_title": "Todo API",
            "reload": True,
        }

    return Settings(
        environment=environment,
        database_path=os.getenv("DATABASE_PATH", defaults["database_path"]),
        server_host=os.getenv("SERVER_HOST", "0.0.0.0"),
        server_port=int(os.getenv("SERVER_PORT", defaults["server_port"])),
        cors_origins=defaults["cors_origins"],
        app_title=defaults["app_title"],
        reload=defaults["reload"],
    )


settings = load_settings()
