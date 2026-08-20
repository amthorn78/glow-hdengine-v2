import pytest

from ci.checks.import_http_reader_for_tests import import_http_reader_for_test
from engine.db import adapter as db_adapter

pytestmark = pytest.mark.epic006
HTTP_READER_DYNAMIC_OWNER = "adapter.http_reader"


def test_http_reader_import_without_dsn(monkeypatch):
    monkeypatch.delenv("DATABASE_URL", raising=False)
    module = import_http_reader_for_test()
    assert module.__name__ == HTTP_READER_DYNAMIC_OWNER


def test_http_reader_import_with_dsn(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgresql://example")
    provider_attempts: list[str] = []

    def forbid_provider(_dsn: str):
        provider_attempts.append("provider")
        pytest.fail("Reader import must not construct a database provider")

    monkeypatch.setattr(db_adapter, "PsycopgProvider", forbid_provider)
    module = import_http_reader_for_test()
    assert module.__name__ == HTTP_READER_DYNAMIC_OWNER
    assert not provider_attempts
