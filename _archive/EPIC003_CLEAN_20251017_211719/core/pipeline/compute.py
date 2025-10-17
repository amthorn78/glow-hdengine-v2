from __future__ import annotations
from typing import Any, Dict, Iterable, Tuple
from core.pipeline.presenter import present_public
from core.config.toggles_resolver import resolve_toggles
from core.stable.identity_constants import ENGINE_TAG, RELEASE_ID

def _bands_from_math(_: Any) -> Iterable[str]:
    # placeholder labels; real math lands later in 008
    return ("4B-60","4B-40","4B-20")

def compute_pair(a: Dict[str,Any], b: Dict[str,Any], *, toggles: Dict[str,Any]|None=None, debug: bool=False) -> Dict[str,Any]:
    resolved, frozen_sha, _ = resolve_toggles() if toggles is None else (toggles, "manual", False)
    bands = list(_bands_from_math((a,b,resolved)))
    eligible = True
    uncertainty = "low"
    prompt = "Be kind; agree pace."
    flags: list[str] = []
    versions = {"engine_tag": ENGINE_TAG, "release_id": RELEASE_ID, "toggles_sha": frozen_sha}
    admin_debug = {"input":{"a":a,"b":b}, "toggles_sha": frozen_sha} if debug else None
    return present_public(bands, eligible, prompt, uncertainty, flags, versions, admin_debug=admin_debug)
