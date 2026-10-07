from typing import Literal

from pydantic import BaseModel


class ModelDefinition(BaseModel):
    id: str
    label: str
    provider: Literal["groq"]
    model_name: str
    api_key_env: str


class ModelInfo(BaseModel):
    id: str
    label: str
    provider: Literal["groq"]


class ModelsResponse(BaseModel):
    models: list[ModelInfo]