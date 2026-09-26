from __future__ import annotations
import hashlib
from typing import Dict, List, Any, Tuple

from engine.presenter import emitter  # emits UTF-8 with exactly one trailing LF
from engine.categories.registry import FROZEN_MAGIC10_ORDER

_CATEGORY_BANDS = {"Cool","Open","Warm","Glow"}
_CATEGORY_KEYS = {"id", "band"}


def _clean_category(c: Any) -> Dict[str, str]:
    """One public category item: exactly ``{id, band}`` with a governed band.

    The public covenant (PF01 §2.2, PF04 §8.1.2) never permitted ``prompt`` or
    any other key on a category item, so anything but ``id`` and ``band`` is
    refused rather than passed through.
    """
    if not isinstance(c, dict) or set(c) != _CATEGORY_KEYS:
        raise ValueError("Invalid category item: exactly {id, band} is required")
    cid = c["id"]
    band = c["band"]
    if not isinstance(cid, str) or not cid:
        raise ValueError("Invalid category id")
    if band not in _CATEGORY_BANDS:
        raise ValueError(f"Invalid band for {cid}: {band}")
    return {"id": cid, "band": band}


def _dedupe_and_sort_categories(categories: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Reader v1: enforce 'categories is a set' and sort by id.
    - Reject duplicate ids (explicitly fail-closed rather than arbitrary pick).
    - Each item is exactly {id, band}; nothing else is injected or passed through.
    """
    seen = set()
    cleaned: List[Dict[str, Any]] = []
    for c in categories or []:
        item = _clean_category(c)
        if item["id"] in seen:
            raise ValueError(f"Duplicate category id: {item['id']}")
        seen.add(item["id"])
        cleaned.append(item)
    cleaned.sort(key=lambda x: x["id"])
    return cleaned


def _ordered_categories_v2(categories: List[Dict[str, Any]], *, eligible: bool) -> List[Dict[str, Any]]:
    """
    Reader v2 (PF10 §2.23, C040-07): the ordered ten-item array in the canonical
    governed order of catalog/magic10.json — never set-sorted — or [] when
    ineligible.  Exactly one item per Magic-10 identifier; no omission,
    duplication, default fill or substitution.
    """
    items = [_clean_category(c) for c in (categories or [])]
    if not eligible:
        if items:
            raise ValueError("Reader v2 ineligible envelope must carry no categories")
        return []
    if [item["id"] for item in items] != list(FROZEN_MAGIC10_ORDER):
        raise ValueError("Reader v2 categories must be exactly the ten Magic-10 identifiers in canonical governed order")
    return items

def _build_preimage(enriched: Dict[str, Any]) -> Dict[str, Any]:
    """
    Build the Reader v1 success envelope WITHOUT idempotence_hash (preimage).
    Required in enriched:
      eligible: bool
      categories: list[{id,band}]
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


def _build_preimage_v2(enriched: Dict[str, Any]) -> Dict[str, Any]:
    """Build the Reader v2 success envelope WITHOUT idempotence_hash (preimage).

    Same five keys and the same recipe as v1; ``reader_version`` is ``"v2"`` and
    ``categories`` is the ordered ten-item array (or ``[]`` when ineligible).
    """
    eligible = bool(enriched.get("eligible", False))
    return {
        "reader_version": "v2",
        "eligible": eligible,
        "categories": _ordered_categories_v2(enriched.get("categories", []), eligible=eligible),
        "meta": {
            "engine_tag": enriched["meta"]["engine_tag"],
            "invocation_tag": enriched["meta"]["invocation_tag"],
        },
        "release_id": enriched["release_id"],
    }


def _emit(preimage: Dict[str, Any]) -> Tuple[bytes, Dict[str, Any]]:
    """PF05 §6.3: canonicalize the five-key preimage, hash it, add the sixth key, re-emit."""
    pre_bytes = emitter.emit_public(preimage)
    digest = hashlib.sha256(pre_bytes).hexdigest()
    final = dict(preimage)
    final["idempotence_hash"] = digest
    public_bytes = emitter.emit_public(final)
    return public_bytes, final


def emit_reader_v1(enriched: Dict[str, Any]) -> Tuple[bytes, Dict[str, Any]]:
    """
    Returns (public_bytes, final_envelope_dict) for Reader v1.
    public_bytes are LF-terminated, produced by sercanon.serialize.
    """
    return _emit(_build_preimage(enriched))


def emit_reader_v2(enriched: Dict[str, Any]) -> Tuple[bytes, Dict[str, Any]]:
    """
    Returns (public_bytes, final_envelope_dict) for Reader v2 (full Magic-10, ordered).
    public_bytes are LF-terminated, produced by sercanon.serialize.
    """
    return _emit(_build_preimage_v2(enriched))
