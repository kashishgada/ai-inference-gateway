from fastapi import FastAPI

from app.config import get_settings
from app.schemas.models import ModelInfo, ModelsResponse
from app.services.model_registry import AVAILABLE_MODELS

settings = get_settings()
app = FastAPI(title=settings.app_name)


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "environment": settings.app_env,
    }


@app.get("/models", response_model=ModelsResponse)
async def list_models() -> ModelsResponse:
    return ModelsResponse(
        models=[
            ModelInfo(
                id=model.id,
                label=model.label,
                provider=model.provider,
            )
            for model in AVAILABLE_MODELS
        ]
    )
