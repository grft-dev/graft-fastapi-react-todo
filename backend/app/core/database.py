"""Database connection shared by the application."""

from peewee import SqliteDatabase

from app.core.settings import settings


database = SqliteDatabase(settings.database_path)
