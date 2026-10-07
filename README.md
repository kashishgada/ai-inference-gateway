# ai-inference-gateway
A secure FastAPI-based AI inference gateway connecting Next.js applications to multiple LLM providers.

## Backend setup

Create and activate the virtual environment, then install all backend dependencies from
the pinned requirements file:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Start the development server:

```powershell
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

The health check is available at <http://127.0.0.1:8000/health>.
