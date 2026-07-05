from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check_returns_healthy_status() -> None:
    response = client.get("/health")

    assert response.status_code == 200

    response_data = response.json()

    assert response_data["status"] == "healthy"
    assert response_data["service"] == "leadpilot-api"