from __future__ import annotations
import json, hashlib
from typing import Dict, Any
from engine.compat import ts_v0  # provides extract_ts, compute_features, band_v0
from engine.serializer import canon
from engine.presenter.emitter import emit_compact_json

def sercanon(obj: dict) -> bytes:
    """Canonical serializer wrapper."""
    from engine.serializer import canon
    return canon.dumps(obj)

def _band_from_charts(a_chart: Dict[str, Any], b_chart: Dict[str, Any]) -> str:
    a_ts = ts_v0.extract_ts(a_chart)
    b_ts = ts_v0.extract_ts(b_chart)
    feats = ts_v0.compute_features(a_ts, b_ts)
    return ts_v0.band_v0(feats)

def emit_public_envelope(
    a_chart: Dict[str, Any],
    b_chart: Dict[str, Any],
    engine_tag: str,
    invocation_tag: str,
    release_id: str,
) -> bytes:
    """
    Build public Reader v1 envelope (A5 minimal) and return canonical bytes.
    Preimage rule:
        pre_bytes = canon.sercanon(pre)
        idempotence_hash = hashlib.sha256(pre_bytes).hexdigest()
    """
    band = _band_from_charts(a_chart, b_chart)
    pre = {
        "eligible": True,
        "categories": [{"id": "harmony" if False else "harmony", "band": band}],
        "meta": {"engine_tag": engine_tag, "invocation_tag": invocation_tag},
        "release_id": release_id,
    }
    pre_bytes = canon.sercanon(pre)
    h = hashlib.sha256(pre_bytes).hexdigest()
    final = dict(pre, idempotence_hash=h)
    return emit_compact_json(final)[0]
