import pytest
from pydantic import ValidationError

from app.schemas.chat import ChatRequest, ChatResponse


def test_chat_request_accepts_model_and_message() -> None:
    request = ChatRequest(
        model="groq-gpt-oss",
        message="Explain recursion simply",
    )

    assert request.model == "groq-gpt-oss"
    assert request.message == "Explain recursion simply"


@pytest.mark.parametrize("field", ["model", "message"])
def test_chat_request_rejects_empty_required_fields(field: str) -> None:
    values = {
        "model": "groq-gpt-oss",
        "message": "Explain recursion simply",
    }
    values[field] = ""

    with pytest.raises(ValidationError):
        ChatRequest(**values)


def test_chat_response_has_model_and_response() -> None:
    response = ChatResponse(
        model="groq-gpt-oss",
        response="Recursion is when a function calls itself.",
    )

    assert response.model == "groq-gpt-oss"
    assert response.response == "Recursion is when a function calls itself."
