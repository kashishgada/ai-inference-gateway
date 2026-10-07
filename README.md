# ai-inference-gateway

A secure FastAPI-based AI inference gateway connecting a Next.js frontend to
multiple LLM providers.

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

Planned milestones:

5. Organize the backend into a maintainable `app/` package.
6. Add a controlled model registry and `GET /models`.
7. Define and test the `POST /chat` request and response contract.
8. Add provider adapters for Groq and Google Gemini.
9. Build the Next.js model selector and chat interface.
10. Add production hardening such as CORS restrictions, rate limiting, and
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
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

The health check is available at <http://127.0.0.1:8000/health>.

## Running tests

Run the complete test suite from the repository root:

```powershell
python -m pytest -q
```

The current suite covers the health endpoint and application configuration.

## Current structure

```text
ai-inference-gateway/
+-- tests/
|   +-- __init__.py
|   +-- test_config.py
|   +-- test_health.py
+-- .env.example
+-- .gitignore
+-- config.py
+-- main.py
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
