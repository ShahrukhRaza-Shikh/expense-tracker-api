from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_add_expense():
    response = client.post(
        "/expenses",
        json={
            "title": "Lunch",
            "amount": 250,
            "category": "Food",
            "date": "2026-08-01"
        }
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Lunch"


def test_get_expenses():
    response = client.get("/expenses")
    assert response.status_code == 200


def test_total():
    response = client.get("/expenses/total")
    assert response.status_code == 200