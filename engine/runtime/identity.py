from __future__ import annotations

import datetime as dt
from dataclasses import dataclass
from hashlib import sha256
from importlib.resources import files
import json
from pathlib import Path
import re
from typing import Mapping

from engine.serializer import canon

_HEX64_RE = re.compile(r"^[0-9a-f]{64}$")
_MANIFEST_FIELDS = {"root", "version", "built_at_utc", "files"}
_MANIFEST_FILE_FIELDS = {"path", "sha256", "size"}
_VERSION_RE = re.compile(
    r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)"
    r"(?:-(?:0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*)"
    r"(?:\.(?:0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*))*)?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$"
)
_BUILT_AT_RE = re.compile(
    r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"
)
_FIELDS = (
    "engine_tag",
    "build_commit",
    "invocation_tag",
    "invocation_sha256",
    "emitter_sha256",
    "release_id",
)

# Static build identity fields. The release ID is derived once at import from
# the packaged canonical manifest, so a release cut never rewrites Python
# source and request paths never read evidence artifacts or environment values.
_STATIC_IDENTITY = {
    "engine_tag": "hdengine@prod",
    "build_commit": "9479d28",
    "invocation_tag": "INV-f2ac55d77ce9aacc",
    "invocation_sha256": "3f119e727a2a1f8a5332fe8f159321ea5274988e6a05633103fe0a5ae42c6e69",
    "emitter_sha256": "c828effe645deae150593adbc90589f67141ab20fab1e719171cd8effad9bc19",
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


def _manifest_release_id_from_bytes(raw: bytes) -> str:
    try:
        payload = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError("release_manifest_invalid_json") from exc
    canonical = canon.sercanon(payload, sort_keys=True)
    if raw != canonical:
        raise ValueError("release_manifest_not_canonical")
    if (
        not isinstance(payload, dict)
        or set(payload) != _MANIFEST_FIELDS
        or payload.get("root") != "catalog/"
        or not isinstance(payload.get("version"), str)
        or _VERSION_RE.fullmatch(payload["version"]) is None
        or not isinstance(payload.get("built_at_utc"), str)
        or _BUILT_AT_RE.fullmatch(payload["built_at_utc"]) is None
        or not isinstance(payload.get("files"), list)
        or not payload["files"]
    ):
        raise ValueError("release_manifest_contract_invalid")
    try:
        dt.datetime.fromisoformat(
            payload["built_at_utc"].replace("Z", "+00:00")
        )
    except ValueError as exc:
        raise ValueError("release_manifest_contract_invalid") from exc
    paths: list[str] = []
    for entry in payload["files"]:
        if (
            not isinstance(entry, dict)
            or set(entry) != _MANIFEST_FILE_FIELDS
            or not isinstance(entry.get("path"), str)
            or not entry["path"]
            or entry["path"].startswith("/")
            or "\x00" in entry["path"]
            or "\\" in entry["path"]
            or ".." in entry["path"].split("/")
            or Path(entry["path"]).as_posix() != entry["path"]
            or entry["path"] == "catalog/manifest.json"
            or not isinstance(entry.get("sha256"), str)
            or _HEX64_RE.fullmatch(entry["sha256"]) is None
            or not isinstance(entry.get("size"), int)
            or isinstance(entry["size"], bool)
            or entry["size"] < 0
        ):
            raise ValueError("release_manifest_contract_invalid")
        paths.append(entry["path"])
    if paths != sorted(paths) or len(paths) != len(set(paths)):
        raise ValueError("release_manifest_contract_invalid")
    return sha256(canonical).hexdigest()


def _manifest_release_id() -> str:
    """Return the canonical packaged-manifest digest or fail closed."""

    raw = files("catalog").joinpath("manifest.json").read_bytes()
    return _manifest_release_id_from_bytes(raw)


_IDENTITY = _validate_identity(
    {**_STATIC_IDENTITY, "release_id": _manifest_release_id()}
)


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
