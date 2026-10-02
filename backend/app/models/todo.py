"""Peewee persistence model for a todo item."""

from peewee import AutoField, BooleanField, CharField, Model, TextField

from app.core.database import database


class Todo(Model):
    id = AutoField()
    title = CharField()
    description = TextField(default="")
    completed = BooleanField(default=False)

    class Meta:
        database = database
