from __future__ import annotations

from dataclasses import dataclass, asdict
import re
from typing import Mapping

_HEX64_RE = re.compile(r"^[0-9a-f]{64}$")
_FIELDS = ("engine_tag", "build_commit", "invocation_tag", "invocation_sha256", "emitter_sha256", "release_id")

# Cut-time identity snapshot. Runtime code must not read evidence artifacts or
# identity environment variables on request paths; governed evidence generators
# verify and regenerate the corresponding artifact bytes.
_CUT_TIME_IDENTITY = {
    "engine_tag": "hdengine@prod",
    "build_commit": "9479d28",
    "invocation_tag": "INV-f2ac55d77ce9aacc",
    "invocation_sha256": "3f119e727a2a1f8a5332fe8f159321ea5274988e6a05633103fe0a5ae42c6e69",
    "emitter_sha256": "c828effe645deae150593adbc90589f67141ab20fab1e719171cd8effad9bc19",
    "release_id": "12523fec11d4f0ff375bbc7e0d88352a6f3beb07f3a74cecfae901307bbb6e5c",
}


@dataclass(frozen=True)
class IdentitySnapshot:
    engine_tag: str
    build_commit: str
    invocation_tag: str
    invocation_sha256: str
    emitter_sha256: str
    release_id: str


def _validate_identity(values: Mapping[str, object]) -> IdentitySnapshot:
    keys = set(values)
    expected = set(_FIELDS)
    missing = sorted(expected - keys)
    unknown = sorted(keys - expected)
    if missing:
        raise ValueError(f"identity_missing_fields:{','.join(missing)}")
    if unknown:
        raise ValueError(f"identity_unknown_fields:{','.join(unknown)}")
    normalized: dict[str, str] = {}
    for field in _FIELDS:
        value = values[field]
        if not isinstance(value, str) or not value:
            raise ValueError(f"identity_invalid_field:{field}")
        normalized[field] = value
    for field in ("invocation_sha256", "emitter_sha256", "release_id"):
        if not _HEX64_RE.fullmatch(normalized[field]):
            raise ValueError(f"identity_invalid_sha256:{field}")
    return IdentitySnapshot(**normalized)


_IDENTITY = _validate_identity(_CUT_TIME_IDENTITY)


def _initialize_identity_for_tests(values: Mapping[str, object]) -> IdentitySnapshot:
    """Private validation seam for tests; production identity is immutable."""
    candidate = _validate_identity(values)
    if candidate != _IDENTITY:
        raise RuntimeError("identity_conflicting_reinitialization")
    return _IDENTITY


def identity_admin() -> dict[str, str]:
    return {field: getattr(_IDENTITY, field) for field in _FIELDS}


def identity_meta() -> dict[str, str]:
    return {
        "engine_tag": _IDENTITY.engine_tag,
        "invocation_tag": _IDENTITY.invocation_tag,
        "release_id": _IDENTITY.release_id,
    }
