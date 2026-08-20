import pytest

from ci.checks.import_http_reader_for_tests import import_http_reader_for_test


HTTP_READER_DYNAMIC_OWNER = "adapter.http_reader"


@pytest.mark.epic006
def test_import_service_without_db_env(monkeypatch):
    monkeypatch.delenv("DATABASE_URL", raising=False)
    module = import_http_reader_for_test()
    assert module.__name__ == HTTP_READER_DYNAMIC_OWNER
