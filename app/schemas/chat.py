from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    model: str = Field(min_length=1)
    message: str = Field(min_length=1)


class ChatResponse(BaseModel):
    model: str
    response: str
