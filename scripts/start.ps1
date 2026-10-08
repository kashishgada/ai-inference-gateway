$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent $PSScriptRoot
$python = Join-Path $projectRoot "venv\Scripts\python.exe"

if (-not (Test-Path $python)) {
    throw "Virtual environment not found. Run 'python -m venv venv' first."
}

& $python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
