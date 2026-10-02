"""Persistence operations for todo items."""

from app.domain import TodoNotFoundError
from app.models import Todo


class TodoRepository:
    def find_all(self) -> list[Todo]:
        return list(Todo.select())

    def find_by_id(self, todo_id: int) -> Todo:
        try:
            return Todo.get(Todo.id == todo_id)
        except Todo.DoesNotExist as error:
            raise TodoNotFoundError(f"Todo with id '{todo_id}' not found") from error

    def create(self, title: str, description: str = "") -> Todo:
        return Todo.create(title=title, description=description)

    def save(self, todo: Todo) -> Todo:
        todo.save()
        return todo

    def delete_by_id(self, todo_id: int) -> None:
        todo = self.find_by_id(todo_id)
        todo.delete_instance()
