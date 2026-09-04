from fastapi.testclient import TestClient

from starter_code import app


client = TestClient(app)


def test_root_returns_welcome_message():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to the Testable Book API"


# TODO: Add tests for GET /books and GET /books/{book_id}.
# TODO: Add tests for POST /books and DELETE /books/{book_id}.
# TODO: Add tests for missing books and invalid request data.
# TODO: Add a fixture or setup strategy to isolate tests that change the data.
