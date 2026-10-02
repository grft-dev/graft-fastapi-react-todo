from app.models import Todo


def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Todo API", "version": "1.0.0"}


def test_get_all_todos_empty(client):
    response = client.get("/api/todos")
    assert response.status_code == 200
    assert response.json() == []


def test_create_todo(client):
    response = client.post(
        "/api/todos",
        json={"title": "Learn FastAPI", "description": "Build a todo app"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "Learn FastAPI",
        "description": "Build a todo app",
        "completed": False,
    }


def test_get_all_todos(client, sample_todos):
    response = client.get("/api/todos")
    assert response.status_code == 200
    assert {todo["title"] for todo in response.json()} == {"Buy groceries", "Write tests"}


def test_get_todo(client):
    todo = Todo.create(title="Test todo", description="For testing")
    response = client.get(f"/api/todos/{todo.id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Test todo"


def test_update_todo(client):
    todo = Todo.create(title="Original", description="Original description")
    response = client.put(
        f"/api/todos/{todo.id}",
        json={"title": "Updated", "description": "Updated description", "completed": True},
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Updated"
    assert response.json()["completed"] is True


def test_partial_update_todo(client):
    todo = Todo.create(title="Original", description="Keep this")
    response = client.put(f"/api/todos/{todo.id}", json={"completed": True})
    assert response.json()["title"] == "Original"
    assert response.json()["description"] == "Keep this"
    assert response.json()["completed"] is True


def test_toggle_todo_completion(client):
    todo = Todo.create(title="Toggle test")
    assert client.post(f"/api/todos/{todo.id}/toggle").json()["completed"] is True
    assert client.post(f"/api/todos/{todo.id}/toggle").json()["completed"] is False


def test_delete_todo(client):
    todo = Todo.create(title="Delete me")
    response = client.delete(f"/api/todos/{todo.id}")
    assert response.status_code == 200
    assert "deleted" in response.json()["message"]
    assert client.get(f"/api/todos/{todo.id}").status_code == 404


def test_todo_not_found(client):
    assert client.get("/api/todos/999").status_code == 404
    assert client.put("/api/todos/999", json={"title": "Updated"}).status_code == 404
    assert client.post("/api/todos/999/toggle").status_code == 404
    assert client.delete("/api/todos/999").status_code == 404


def test_create_todo_minimal(client):
    response = client.post("/api/todos", json={"title": "Minimal todo"})
    assert response.status_code == 200
    assert response.json()["description"] == ""
    assert response.json()["completed"] is False


def test_complex_workflow(client):
    created = client.post(
        "/api/todos",
        json={"title": "Workflow todo", "description": "Testing workflow"},
    ).json()
    todo_id = created["id"]
    assert client.put(
        f"/api/todos/{todo_id}",
        json={"description": "Updated description"},
    ).json()["title"] == "Workflow todo"
    assert client.post(f"/api/todos/{todo_id}/toggle").json()["completed"] is True
    updated = client.put(f"/api/todos/{todo_id}", json={"title": "Final title"}).json()
    assert updated["title"] == "Final title"
    assert updated["completed"] is True
    assert client.delete(f"/api/todos/{todo_id}").status_code == 200
