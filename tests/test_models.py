from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_list_models_returns_available_models() -> None:
    response = client.get("/models")

    assert response.status_code == 200
    assert response.json() == {
        "models": [
            {
                "id": "groq-llama-70b",
                "label": "Llama 3.3 70B via Groq",
                "provider": "groq",
            },
            {
                "id": "groq-gpt-oss",
                "label": "GPT OSS 120B via Groq",
                "provider": "groq",
            },
        ]
    }
