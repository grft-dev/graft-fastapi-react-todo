import pytest
from fastapi.testclient import TestClient

from app.core.database import database
from app.main import app
from app.models import Todo


@pytest.fixture(autouse=True)
def clean_database():
    if database.is_closed():
        database.connect()
    database.drop_tables([Todo], safe=True)
    database.create_tables([Todo])
    yield
    database.drop_tables([Todo], safe=True)


@pytest.fixture
def client(clean_database):
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def sample_todos():
    Todo.create(title="Buy groceries", description="Milk, bread, eggs")
    Todo.create(title="Write tests", description="Unit tests for todo API", completed=True)
