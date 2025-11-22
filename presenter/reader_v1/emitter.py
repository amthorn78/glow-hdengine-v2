from __future__ import annotations
import hashlib
from typing import Dict, List, Any, Tuple

from engine.presenter import emitter  # emits UTF-8 with exactly one trailing LF

_CATEGORY_BANDS = {"Cool","Open","Warm","Glow"}

def _dedupe_and_sort_categories(categories: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Enforce 'categories is a set' and sort by id.
    - Reject duplicate ids (explicitly fail-closed rather than arbitrary pick).
    - Preserve only allowed keys ('id','band','prompt') if present; do not inject anything new.
    """
    seen = set()
    cleaned: List[Dict[str, Any]] = []
    for c in categories or []:
        cid = c.get("id")
        if cid in seen:
            raise ValueError(f"Duplicate category id: {cid}")
        seen.add(cid)
        band = c.get("band")
        # Basic band sanity (schema will also enforce; keep this light)
        if band not in _CATEGORY_BANDS:
            raise ValueError(f"Invalid band for {cid}: {band}")
        item = {"id": cid, "band": band}
        if "prompt" in c:
            item["prompt"] = c["prompt"]
        cleaned.append(item)
    cleaned.sort(key=lambda x: x["id"])
    return cleaned

def _build_preimage(enriched: Dict[str, Any]) -> Dict[str, Any]:
    """
    Build success envelope WITHOUT idempotence_hash (preimage).
    Required in enriched:
      eligible: bool
      categories: list[{id,band[,prompt]}]
      meta: {engine_tag, invocation_tag}
      release_id: hex64
    """
    pre = {
        "reader_version": "v1",
        "eligible": bool(enriched.get("eligible", False)),
        "categories": _dedupe_and_sort_categories(enriched.get("categories", [])),
        "meta": {
            "engine_tag": enriched["meta"]["engine_tag"],
            "invocation_tag": enriched["meta"]["invocation_tag"],
        },
        "release_id": enriched["release_id"],
    }
    return pre

def emit_reader_v1(enriched: Dict[str, Any]) -> Tuple[bytes, Dict[str, Any]]:
    """
    Returns (public_bytes, final_envelope_dict).
    public_bytes are LF-terminated, produced by sercanon.serialize.
    """
    preimage = _build_preimage(enriched)
    pre_bytes, _ = emitter.emit_compact_json(preimage)
    digest = hashlib.sha256(pre_bytes).hexdigest()
    final = dict(preimage)
    final["idempotence_hash"] = digest
    public_bytes, _ = emitter.emit_compact_json(final)
    return public_bytes, final
