# ai-inference-gateway

A secure FastAPI-based AI inference gateway connecting a Next.js frontend to
an LLM provider.

## Project status

The project is being built incrementally. Each milestone is tested and committed
separately so the Git history documents the architecture as it develops.

Completed milestones:

1. **FastAPI foundation** - created the application, `GET /health`, pinned
   runtime dependencies, and protected local secrets with `.gitignore`.
2. **Secure configuration** - added typed settings loaded from `.env`, safe
   defaults, application naming, and startup validation.
3. **Health endpoint coverage** - added the first automated API test.
4. **Configuration coverage** - added tests for defaults, environment variables,
   and invalid configuration values.
5. **Backend package structure** - moved application code into the `app/`
   package without changing existing behavior.
6. **Model registry** - added a backend-controlled `GET /models` endpoint for
   populating the frontend model selector.
7. **Chat contract** - added validated request and response schemas for the
   future `POST /chat` endpoint.

Planned milestones:

8. Add model selection logic and the `POST /chat` route.
9. Add the Groq provider adapter.
10. Build the Next.js model selector and chat interface.
11. Add production hardening such as CORS restrictions, rate limiting, and
    structured logging.

## Backend setup

Create and activate the virtual environment, then install runtime dependencies:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

For development and testing, install the test dependencies as well:

```powershell
python -m pip install -r requirements-dev.txt
```

Copy the example environment file before starting the backend:

```powershell
Copy-Item .env.example .env
```

The `.env` file is ignored by Git and must never contain values committed to the
repository. Invalid `APP_ENV` values cause the application to fail during
startup.

Start the development server:

```powershell
.\scripts\start.ps1
```

The startup script uses the project's virtual environment directly, so manual
activation is not required.

The health check is available at <http://127.0.0.1:8000/health>.

## Running tests

Run the complete test suite from the repository root:

```powershell
python -m pytest -q
```

The current suite covers the health endpoint, application configuration, the
available model registry, and chat contract validation.

The model list is available at <http://127.0.0.1:8000/models>.

## Current structure

```text
ai-inference-gateway/
|-- app/
|   |-- __init__.py
|   |-- config.py
|   |-- main.py
|   |-- schemas/
|   |   |-- __init__.py
|   |   |-- chat.py
|   |   `-- models.py
|   `-- services/
|       |-- __init__.py
|       `-- model_registry.py
+-- tests/
|   +-- __init__.py
|   +-- test_config.py
|   +-- test_chat.py
|   +-- test_health.py
|   +-- test_models.py
+-- .env.example
+-- .gitignore
+-- requirements-dev.txt
+-- requirements.txt
+-- README.md
```

## Configuration

The example configuration is:

```env
APP_ENV=development
APP_NAME=ai-inference-gateway
```

Supported `APP_ENV` values are:

```text
development
testing
production
```

Provider API keys will be added later. They will remain in the backend
environment and will never be sent to the frontend.

## Available models

The backend registry currently exposes these safe model IDs to the frontend:

| ID | Provider | Backend model |
| --- | --- | --- |
| `groq-llama-70b` | Groq | `llama-3.3-70b-versatile` |
| `groq-gpt-oss` | Groq | `openai/gpt-oss-120b` |

The frontend receives only the public ID, label, and provider. Provider model
names and API-key environment variable names remain internal to the backend.
