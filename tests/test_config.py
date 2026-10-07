import pytest
from pydantic import ValidationError

from config import Settings


def test_settings_use_safe_defaults() -> None:
    settings = Settings(_env_file=None)

    assert settings.app_env == "development"
    assert settings.app_name == "ai-inference-gateway"


def test_settings_load_environment_variables(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("APP_ENV", "testing")
    monkeypatch.setenv("APP_NAME", "Test gateway")

    settings = Settings(_env_file=None)

    assert settings.app_env == "testing"
    assert settings.app_name == "Test gateway"


def test_settings_reject_invalid_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("APP_ENV", "invalid")

    with pytest.raises(ValidationError):
        Settings(_env_file=None)
