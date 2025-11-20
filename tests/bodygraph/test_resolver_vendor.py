from engine.bodygraph import resolver
from engine.bodygraph.ingest import IngestOutcome, VendorInputs


def _make_outcome():
    return IngestOutcome(
        vendor="hdapi",
        vendor_version=1,
        input_fingerprint="fingerprint",
        idempotency_key="idem",
        rows_written=1,
        duration_ms=1.0,
        payload_sha256="payload",
        db_emitted_sha256="payload",
        parity_match=True,
        db_rows_after=1,
        payload={"ok": True},
    )


def test_vendor_resolver_maps_synthetic_user(monkeypatch):
    snapshot = {"safe_mode": False, "allow_network": True}
    vendor_inputs = VendorInputs(
        user_id="epic011-s10-invariance-1",
        birthdate="1990-01-01",
        birthtime="12:00",
        location="Amsterdam, Netherlands",
    )
    monkeypatch.setattr(resolver, "_resolve_inputs", lambda *args, **kwargs: vendor_inputs)

    captured = {}

    def fake_ingest(inputs, env=None):
        captured["inputs"] = inputs
        return _make_outcome()

    monkeypatch.setattr(resolver, "ingest_vendor_bodygraph", fake_ingest)

    result = resolver._resolve_vendor(
        "epic011-s10-invariance-1",
        snapshot,
        upsert=False,
        dry_run=False,
        env={},
        birthdate=None,
        birthtime=None,
        location=None,
    )

    assert captured["inputs"].user_id == "3fa85f64-5717-4562-b3fc-2c963f66afab"
    assert result.status == "ok"


def test_vendor_resolver_wraps_unexpected_normalization_errors(monkeypatch):
    snapshot = {"safe_mode": False, "allow_network": True}
    vendor_inputs = VendorInputs(
        user_id="epic011-s10-invariance-1",
        birthdate="1990-01-01",
        birthtime="12:00",
        location="Amsterdam, Netherlands",
    )
    monkeypatch.setattr(resolver, "_resolve_inputs", lambda *_, **__: vendor_inputs)

    def boom(*_, **__):
        raise RuntimeError("boom")

    monkeypatch.setattr(resolver, "resolve_db_user_id", boom)

    result = resolver._resolve_vendor(
        "epic011-s10-invariance-1",
        snapshot,
        upsert=False,
        dry_run=False,
        env={},
        birthdate=None,
        birthtime=None,
        location=None,
    )

    assert result.status == "error"
    assert result.payload["error"]["code"] == "PROVIDER_INPUT_INVALID"
