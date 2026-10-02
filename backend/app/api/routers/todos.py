"""HTTP routes for todo operations."""

from fastapi import APIRouter, HTTPException

from app.domain import TodoNotFoundError
from app.schemas import TodoCreate, TodoResponse, TodoUpdate
from app.services import TodoService


router = APIRouter(prefix="/api/todos", tags=["todos"])
service = TodoService()


def _not_found(error: TodoNotFoundError) -> HTTPException:
    return HTTPException(status_code=404, detail=str(error))


@router.get("", response_model=list[TodoResponse])
def list_todos():
    return service.list_todos()


@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: int):
    try:
        return service.get_todo(todo_id)
    except TodoNotFoundError as error:
        raise _not_found(error) from error


@router.post("", response_model=TodoResponse)
def create_todo(todo: TodoCreate):
    return service.create_todo(todo)


@router.put("/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, update: TodoUpdate):
    try:
        return service.update_todo(todo_id, update)
    except TodoNotFoundError as error:
        raise _not_found(error) from error


@router.post("/{todo_id}/toggle", response_model=TodoResponse)
def toggle_todo(todo_id: int):
    try:
        return service.toggle_todo(todo_id)
    except TodoNotFoundError as error:
        raise _not_found(error) from error


@router.delete("/{todo_id}")
def delete_todo(todo_id: int):
    try:
        return service.delete_todo(todo_id)
    except TodoNotFoundError as error:
        raise _not_found(error) from error
