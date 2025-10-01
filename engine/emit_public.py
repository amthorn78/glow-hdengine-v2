from __future__ import annotations
import json, hashlib
from typing import Dict, Any
from engine.compat import ts_v0  # provides extract_ts, compute_features, band_v0

def sercanon(obj: Dict[str, Any]) -> bytes:
    """
    Canonical serializer:
      - UTF-8
      - sort_keys=True
      - separators=(',',':')
      - ensure_ascii=False
      - exactly one trailing LF
    """
    s = json.dumps(obj, sort_keys=True, separators=(',',':'), ensure_ascii=False)
    if s.endswith("\n"):
        s = s.rstrip("\n")
    return (s + "\n").encode("utf-8")

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
      idempotence_hash = sha256(sercanon(preimage)).hexdigest()
    """
    band = _band_from_charts(a_chart, b_chart)
    pre = {
        "eligible": True,
        "categories": [{"id": "harmony", "band": band}],
        "meta": {"engine_tag": engine_tag, "invocation_tag": invocation_tag},
        "release_id": release_id,
    }
    h = hashlib.sha256(sercanon(pre)).hexdigest()
    final = dict(pre, idempotence_hash=h)
    return sercanon(final)
