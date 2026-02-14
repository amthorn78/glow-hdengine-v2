"""
Conjunction computation contract (HDE-EPIC026 PR-01).

Produces a deterministic, JSON-serializable conjunction result for a pair
of resolved BodyGraph inputs.  Reuses the existing compatibility engine
(compat_public) and pair-ordering primitives (normalize_pair / pair_key)
so that AB↔BA identity is inherited.

The result is emittable through the single canonical JSON emitter
(engine.presenter.emit_public) with no additional serialization path.
"""
from __future__ import annotations

from typing import Any, Dict

from engine.compat.compute import compat_public
from engine.compat.ordering import normalize_pair, pair_key


def compute_conjunction(
    a: Dict[str, object],
    b: Dict[str, object],
    viewer_top: str,
    viewer_weights: Dict[str, int],
    *,
    engine_tag: str = "dev",
    release_id: str = "dev",
    invocation_tag: str = "INV-DEV",
) -> Dict[str, Any]:
    """Compute a conjunction result for a pair of resolved BodyGraph inputs.

    Returns a plain dict with stable key ordering suitable for canonical
    JSON serialization.  The result satisfies AB↔BA byte-identity when
    serialized through ``emit_public`` because pair ordering is
    canonicalized before any computation.

    Parameters
    ----------
    a, b : dict
        Resolved BodyGraph dicts.  Must contain ``person_uid``.
    viewer_top : str
        Top category from viewer preferences (one of the Magic-10).
    viewer_weights : dict[str, int]
        Category weights from viewer preferences.
    engine_tag, release_id, invocation_tag : str
        Metadata tags forwarded to the compatibility engine.

    Returns
    -------
    dict
        Conjunction result structure ready for canonical envelope wrapping.
    """
    # Canonicalize pair order *before* computation so that (a,b) and (b,a)
    # always enter the compat engine in the same normalized order.
    a_norm, b_norm = normalize_pair(a, b)
    pkey = pair_key(a_norm, b_norm)

    compat_result = compat_public(
        a_norm,
        b_norm,
        viewer_top,
        viewer_weights,
        engine_tag=engine_tag,
        release_id=release_id,
        invocation_tag=invocation_tag,
    )

    return {
        "categories": compat_result["categories"],
        "meta": compat_result["meta"],
        "pair_key": pkey,
    }


def build_conjunction_envelope(
    a: Dict[str, object],
    b: Dict[str, object],
    viewer_top: str,
    viewer_weights: Dict[str, int],
    *,
    engine_tag: str = "dev",
    release_id: str = "dev",
    invocation_tag: str = "INV-DEV",
) -> Dict[str, Any]:
    """Build a canonical envelope for a conjunction result.

    The envelope follows the existing ``emit_public`` convention
    (flat dict with sorted keys → canonical JSON bytes).

    Returns
    -------
    dict
        A dict suitable for ``emit_public(envelope)``.
    """
    result = compute_conjunction(
        a,
        b,
        viewer_top,
        viewer_weights,
        engine_tag=engine_tag,
        release_id=release_id,
        invocation_tag=invocation_tag,
    )

    return {
        "kind": "conjunction",
        "ok": True,
        "schema": "v1",
        "result": result,
    }
