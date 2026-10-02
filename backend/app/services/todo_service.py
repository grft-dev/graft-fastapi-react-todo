"""Application logic for todo operations."""

from app.repositories import TodoRepository
from app.schemas import TodoCreate, TodoResponse, TodoUpdate


class TodoService:
    def __init__(self, repository: TodoRepository | None = None):
        self.repository = repository or TodoRepository()

    @staticmethod
    def _to_response(todo) -> TodoResponse:
        return TodoResponse.model_validate(todo, from_attributes=True)

    def list_todos(self) -> list[TodoResponse]:
        return [self._to_response(todo) for todo in self.repository.find_all()]

    def get_todo(self, todo_id: int) -> TodoResponse:
        return self._to_response(self.repository.find_by_id(todo_id))

    def create_todo(self, todo_data: TodoCreate) -> TodoResponse:
        todo = self.repository.create(
            title=todo_data.title,
            description=todo_data.description,
        )
        return self._to_response(todo)

    def update_todo(self, todo_id: int, update_data: TodoUpdate) -> TodoResponse:
        todo = self.repository.find_by_id(todo_id)

        if update_data.title is not None:
            todo.title = update_data.title
        if update_data.description is not None:
            todo.description = update_data.description
        if update_data.completed is not None:
            todo.completed = update_data.completed

        return self._to_response(self.repository.save(todo))

    def toggle_todo(self, todo_id: int) -> TodoResponse:
        todo = self.repository.find_by_id(todo_id)
        todo.completed = not todo.completed
        return self._to_response(self.repository.save(todo))

    def delete_todo(self, todo_id: int) -> dict[str, str]:
        self.repository.delete_by_id(todo_id)
        return {"message": f"Todo with id '{todo_id}' deleted"}
