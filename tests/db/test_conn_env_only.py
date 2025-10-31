import importlib
import sys

import pytest

pytestmark = pytest.mark.epic006


def _import_http_reader():
    importlib.invalidate_caches()
    sys.modules.pop("adapter.http_reader", None)
    sys.modules.pop("adapter", None)
    return importlib.import_module("adapter.http_reader")


def test_http_reader_import_without_dsn(monkeypatch):
    monkeypatch.delenv("DATABASE_URL", raising=False)
    module = _import_http_reader()
    assert module is not None


def test_http_reader_import_with_dsn(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgresql://example")
    module = _import_http_reader()
    assert module is not None
