from __future__ import annotations

def test_env_guard_import_and_stub_callable():
    # Import must succeed without side effects
    import adapter.env_guard as eg  # noqa: F401
    assert hasattr(eg, "validate_or_fail")
    assert callable(eg.validate_or_fail)
    # Stub does nothing and returns None
    assert eg.validate_or_fail({}) is None
