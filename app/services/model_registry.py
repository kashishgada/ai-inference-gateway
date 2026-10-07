from app.schemas.models import ModelDefinition


AVAILABLE_MODELS: tuple[ModelDefinition, ...] = (
    ModelDefinition(
        id="groq-llama-70b",
        label="Llama 3.3 70B via Groq",
        provider="groq",
        model_name="llama-3.3-70b-versatile",
        api_key_env="GROQ_API_KEY",
    ),
    ModelDefinition(
        id="groq-gpt-oss",
        label="GPT OSS 120B via Groq",
        provider="groq",
        model_name="openai/gpt-oss-120b",
        api_key_env="GROQ_API_KEY",
    ),
)
