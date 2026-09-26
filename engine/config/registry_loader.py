from __future__ import annotations

import ast
import hashlib
import json
import math
import os
import re
import stat
import sys as _sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from types import CodeType, MappingProxyType, ModuleType
from typing import Iterable, Mapping

import jsonschema
from jsonschema import validators
from referencing import Registry, Resource
from referencing.exceptions import NoSuchResource

from engine.categories import registry as category_registry
from engine.categories.registry import FROZEN_MAGIC10_ORDER
from engine.serializer import canon


# Retain actual execution provenance without reading or executing source bytes.
# Unsupported provenance leaves candidate APIs usable; active admission refuses.
try:
    _MODULE_EXECUTION = (
        _sys._getframe().f_code, __name__, __file__, __spec__.origin,
        _sys.flags.optimize, _sys.implementation.cache_tag,
    )
except Exception:
    _MODULE_EXECUTION = None


# PF12 — HDE Schemas & Artifacts, §2.1 owns the closed Gate domain 1..64,
# while §4.2 preserves array order unless an owning contract declares set
# semantics.  The Gate catalog rows are ordered source data, not a declared
# set, so preserve the exact numeric domain order rather than normalizing it.
FROZEN_GATE_IDS = tuple(range(1, 65))


# PF08 — Human Design System, §Channels defines the complete 36-Channel
# BodyGraph roster.  This is an identity set: catalog ordering is enforced by
# the canonical JSON gate, while this loader independently refuses a
# schema-valid substitution of one Channel identity for another.
FROZEN_CHANNEL_IDS = (
    "01-08",
    "02-14",
    "03-60",
    "04-63",
    "05-15",
    "06-59",
    "07-31",
    "09-52",
    "10-20",
    "10-34",
    "10-57",
    "11-56",
    "12-22",
    "13-33",
    "16-48",
    "17-62",
    "18-58",
    "19-49",
    "20-34",
    "20-57",
    "21-45",
    "23-43",
    "24-61",
    "25-51",
    "26-44",
    "27-50",
    "28-38",
    "29-46",
    "30-41",
    "32-54",
    "34-57",
    "35-36",
    "37-40",
    "39-55",
    "42-53",
    "47-64",
)


# PF12 — HDE Schemas & Artifacts, §2.1 owns the exact Gate counts for the
# nine canonical center IDs.  Individual Gate-to-center assignments remain
# single-homed in catalog/gates_v1.json; this aggregate independently refuses
# a coherent cross-catalog reassignment that changes the governed topology.
FROZEN_GATE_CENTER_COUNTS = {
    "ajna": 6,
    "ego": 4,
    "g": 8,
    "head": 3,
    "root": 9,
    "sacral": 9,
    "solar_plexus": 7,
    "spleen": 7,
    "throat": 11,
}


# PF08 — Human Design System, §Channels lists each Channel's Gate endpoints in
# the same order as its Center heading (for example, 8-1 under Throat-to-G).
# Preserve that exact Gate-to-Center assignment independently of the Gate
# catalog so a coherent reassignment cannot redefine its own expected topology.
FROZEN_CHANNEL_ENDPOINT_CENTERS = {
    "01-08": ((8, "throat"), (1, "g")),
    "02-14": ((2, "g"), (14, "sacral")),
    "03-60": ((3, "sacral"), (60, "root")),
    "04-63": ((63, "head"), (4, "ajna")),
    "05-15": ((15, "g"), (5, "sacral")),
    "06-59": ((59, "sacral"), (6, "solar_plexus")),
    "07-31": ((31, "throat"), (7, "g")),
    "09-52": ((9, "sacral"), (52, "root")),
    "10-20": ((20, "throat"), (10, "g")),
    "10-34": ((10, "g"), (34, "sacral")),
    "10-57": ((10, "g"), (57, "spleen")),
    "11-56": ((11, "ajna"), (56, "throat")),
    "12-22": ((12, "throat"), (22, "solar_plexus")),
    "13-33": ((33, "throat"), (13, "g")),
    "16-48": ((16, "throat"), (48, "spleen")),
    "17-62": ((17, "ajna"), (62, "throat")),
    "18-58": ((18, "spleen"), (58, "root")),
    "19-49": ((49, "solar_plexus"), (19, "root")),
    "20-34": ((20, "throat"), (34, "sacral")),
    "20-57": ((20, "throat"), (57, "spleen")),
    "21-45": ((45, "throat"), (21, "ego")),
    "23-43": ((43, "ajna"), (23, "throat")),
    "24-61": ((61, "head"), (24, "ajna")),
    "25-51": ((25, "g"), (51, "ego")),
    "26-44": ((26, "ego"), (44, "spleen")),
    "27-50": ((50, "spleen"), (27, "sacral")),
    "28-38": ((28, "spleen"), (38, "root")),
    "29-46": ((46, "g"), (29, "sacral")),
    "30-41": ((30, "solar_plexus"), (41, "root")),
    "32-54": ((32, "spleen"), (54, "root")),
    "34-57": ((57, "spleen"), (34, "sacral")),
    "35-36": ((35, "throat"), (36, "solar_plexus")),
    "37-40": ((40, "ego"), (37, "solar_plexus")),
    "39-55": ((55, "solar_plexus"), (39, "root")),
    "42-53": ((42, "sacral"), (53, "root")),
    "47-64": ((64, "head"), (47, "ajna")),
}


# PF12 §2.5 makes each caps `inputs` value an array, and §4.2 preserves array
# order unless an owning contract declares set semantics.  The current Magic-10
# calculators consume these values as tuples in catalog order.  Freeze the exact
# ordered input contract here without sorting or deduplicating it.
FROZEN_MAGIC10_INPUTS = {
    "harmony": ("rapport_delta", "resonance_strength"),
    "heat": ("spark_intensity", "momentum_flux"),
    "communication": ("signal_clarity", "exchange_density"),
    "alignment": ("vector_cohesion", "axis_agreement"),
    "comfort": ("soothe_index", "buffer_resilience"),
    "consistency": ("pattern_integrity", "variance_stability"),
    "expansion": ("growth_tendency", "horizon_reach"),
    "creativity": ("novelty_factor", "expression_flow"),
    "drive": ("willpower_current", "focus_pressure"),
    "balance": ("equilibrium_score", "counterweight_ratio"),
}


# Discovery (PR3 / EPIC017): this loader owns the PF12 catalogs under catalog/ (gates_v1,
# channels_v1, magic10*.json, manifest.json). The legacy registry_report lived at
# artifacts/reports/registry_report.json with only category ranks; we normalize it to
# artifacts/registry/registry_report.json with PF14 keys and hardened validation. Legacy
# Magic-10 order/caps checks must be preserved; catalog ID handling is tightened to fail
# closed on unknown IDs and aliases.


class RegistryConfigError(Exception):
    def __init__(self, code: str, message: str, details: Mapping[str, object] | None = None):
        super().__init__(message)
        self.code = code
        self.message = message
        self.details = dict(details or {})


class UnknownIdError(RegistryConfigError):
    pass


class DuplicateIdError(RegistryConfigError):
    pass


class AliasPolicyError(RegistryConfigError):
    pass


class SchemaValidationError(RegistryConfigError):
    pass


@dataclass(frozen=True, slots=True)
class Gate:
    gate: int
    center: str


@dataclass(frozen=True, slots=True)
class Channel:
    id: str
    gates: tuple[int, int]
    centers: tuple[str, str]
    circuit_primary: str
    substream: str | None
    primary_domain: str
    domains: tuple[str, ...]
    flags: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class Magic10Caps:
    inputs: tuple[str, ...]
    bounds: Mapping[str, int]


@dataclass(frozen=True, slots=True)
class Magic10Seed:
    template_id: str
    seed_version: str
    updated_at_utc: str
    checksum_sha256: str


@dataclass(frozen=True, slots=True)
class ManifestEntry:
    path: str
    sha256: str
    size: int


@dataclass(frozen=True, slots=True)
class Manifest:
    root: str
    version: str
    built_at_utc: str
    files: tuple[ManifestEntry, ...]


@dataclass(frozen=True, slots=True)
class RegistryConfig:
    gates: Mapping[int, Gate]
    channels: Mapping[str, Channel]
    alias_map: Mapping[str, str]
    magic10_order: tuple[str, ...]
    magic10_caps: Mapping[str, Magic10Caps]
    magic10_seeds: Mapping[str, Magic10Seed]
    manifest: Manifest
    centers: tuple[str, ...]
    domains: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class SourceIdentity:
    path: str
    sha256: str
    size: int


@dataclass(frozen=True, slots=True)
class AdmittedMechanicsBundle:
    registry: RegistryConfig
    mechanics: Mapping[str, object]
    manifest: Manifest
    config_sha256: str
    source_identities: tuple[SourceIdentity, ...]
    manifest_sha256: str
    release_id: str



# PF10 Addendum 2.5 / PF12: source-fixed construction sentries, not a second catalog.
_CHANNEL_CLASSIFICATIONS = {'01-08': ('individual', 'knowing'),
 '02-14': ('individual', 'knowing'),
 '03-60': ('individual', 'knowing'),
 '04-63': ('collective', 'logic'),
 '05-15': ('collective', 'logic'),
 '06-59': ('tribal', 'defense'),
 '07-31': ('collective', 'logic'),
 '09-52': ('collective', 'logic'),
 '10-20': ('individual', 'integration'),
 '10-34': ('individual', 'centering'),
 '10-57': ('individual', 'integration'),
 '11-56': ('collective', 'sensing'),
 '12-22': ('individual', 'knowing'),
 '13-33': ('collective', 'sensing'),
 '16-48': ('collective', 'logic'),
 '17-62': ('collective', 'logic'),
 '18-58': ('collective', 'logic'),
 '19-49': ('tribal', 'ego'),
 '20-34': ('individual', 'integration'),
 '20-57': ('individual', 'knowing'),
 '21-45': ('tribal', 'ego'),
 '23-43': ('individual', 'knowing'),
 '24-61': ('individual', 'knowing'),
 '25-51': ('individual', 'centering'),
 '26-44': ('tribal', 'ego'),
 '27-50': ('tribal', 'defense'),
 '28-38': ('individual', 'knowing'),
 '29-46': ('collective', 'sensing'),
 '30-41': ('collective', 'sensing'),
 '32-54': ('tribal', 'ego'),
 '34-57': ('individual', 'integration'),
 '35-36': ('collective', 'sensing'),
 '37-40': ('tribal', 'ego'),
 '39-55': ('individual', 'knowing'),
 '42-53': ('collective', 'sensing'),
 '47-64': ('collective', 'sensing')}

_CHANNEL_PRODUCT_METADATA = {'01-08': ('narrative', ['narrative'], []),
 '02-14': ('bonding_feel', ['bonding_feel', 'rhythm'], []),
 '03-60': ('rhythm', ['rhythm'], ['format']),
 '04-63': ('narrative', ['narrative'], []),
 '05-15': ('bonding_feel', ['bonding_feel', 'rhythm'], []),
 '06-59': ('narrative', ['narrative'], []),
 '07-31': ('narrative', ['narrative'], []),
 '09-52': ('rhythm', ['rhythm'], ['format']),
 '10-20': ('talk', ['talk'], []),
 '10-34': ('bonding_feel', ['bonding_feel', 'rhythm'], []),
 '10-57': ('bonding_feel', ['bonding_feel', 'rhythm'], []),
 '11-56': ('talk', ['narrative', 'talk'], []),
 '12-22': ('action_voice', ['action_voice', 'talk'], ['direct_mt']),
 '13-33': ('narrative', ['narrative'], []),
 '16-48': ('action_voice', ['action_voice', 'talk'], []),
 '17-62': ('talk', ['narrative', 'talk'], []),
 '18-58': ('rhythm', ['rhythm'], []),
 '19-49': ('rhythm', ['rhythm'], []),
 '20-34': ('action_voice', ['action_voice', 'talk'], ['direct_mt']),
 '20-57': ('narrative', ['narrative'], []),
 '21-45': ('action_voice', ['action_voice', 'talk'], ['direct_mt']),
 '23-43': ('talk', ['narrative', 'talk'], []),
 '24-61': ('narrative', ['narrative'], []),
 '25-51': ('bonding_feel', ['bonding_feel', 'rhythm'], []),
 '26-44': ('narrative', ['narrative'], []),
 '27-50': ('narrative', ['narrative'], []),
 '28-38': ('rhythm', ['rhythm'], []),
 '29-46': ('bonding_feel', ['bonding_feel', 'rhythm'], []),
 '30-41': ('rhythm', ['rhythm'], []),
 '32-54': ('rhythm', ['rhythm'], []),
 '34-57': ('narrative', ['narrative'], []),
 '35-36': ('action_voice', ['action_voice', 'talk'], ['direct_mt']),
 '37-40': ('narrative', ['narrative'], []),
 '39-55': ('rhythm', ['rhythm'], []),
 '42-53': ('rhythm', ['rhythm'], ['format']),
 '47-64': ('narrative', ['narrative'], [])}

_SIGNAL_MEMBERSHIP = {'rapport_delta': ('coherence_bp_v1', ['19-49', '26-44', '27-50', '37-40']),
 'resonance_strength': ('coherence_bp_v1', ['05-15', '06-59', '12-22', '13-33']),
 'spark_intensity': ('activation_bp_v1', ['06-59', '25-51', '30-41', '39-55']),
 'momentum_flux': ('activation_bp_v1', ['03-60', '20-34', '29-46', '35-36']),
 'signal_clarity': ('expression_bp_v1', ['04-63', '17-62', '23-43', '24-61', '47-64']),
 'exchange_density': ('expression_bp_v1', ['11-56', '12-22', '13-33', '20-57', '26-44']),
 'vector_cohesion': ('coherence_bp_v1', ['02-14', '07-31', '10-20', '10-34']),
 'axis_agreement': ('coherence_bp_v1', ['19-49', '27-50', '28-38', '32-54']),
 'soothe_index': ('coherence_bp_v1', ['06-59', '12-22', '19-49', '37-40']),
 'buffer_resilience': ('coherence_bp_v1', ['05-15', '10-57', '27-50', '34-57']),
 'pattern_integrity': ('coherence_bp_v1', ['05-15', '09-52', '16-48', '17-62', '18-58']),
 'variance_stability': ('coherence_bp_v1', ['03-60', '29-46', '32-54', '42-53']),
 'growth_tendency': ('activation_bp_v1', ['03-60', '18-58', '32-54', '42-53']),
 'horizon_reach': ('activation_bp_v1', ['11-56', '28-38', '29-46', '35-36']),
 'novelty_factor': ('activation_bp_v1', ['01-08', '03-60', '23-43', '25-51']),
 'expression_flow': ('expression_bp_v1', ['10-20', '11-56', '12-22', '16-48', '35-36']),
 'willpower_current': ('activation_bp_v1', ['02-14', '21-45', '25-51', '26-44', '32-54']),
 'focus_pressure': ('activation_bp_v1', ['09-52', '18-58', '20-34', '28-38', '42-53']),
 'equilibrium_score': ('twice_min_owner_mass_v1',
                       ['02-14', '07-31', '21-45', '26-44', '32-54', '37-40']),
 'counterweight_ratio': ('companionship_em_mass_v1',
                         ['05-15', '06-59', '10-20', '13-33', '27-50', '39-55'])}

_PROFILE_RESPONSES = {
    "activation_bp_v1": {"none": 0, "companionship": 5000, "dominance": 7500, "compromise": 2500, "electromagnetic": 10000},
    "coherence_bp_v1": {"none": 0, "companionship": 10000, "dominance": 5000, "compromise": 2500, "electromagnetic": 7500},
    "expression_bp_v1": {"none": 0, "companionship": 7500, "dominance": 5000, "compromise": 2500, "electromagnetic": 10000},
}
_MECHANICS_SOURCE_PATHS = {
    "caps": "catalog/magic10_caps.json", "categories": "catalog/magic10.json",
    "channels": "catalog/channels_v1.json", "thresholds": "math/thresholds.json",
}
_CONSUMER_SCHEMAS = {
    "docs/schemas/config_bundle_be.json": "config_bundle.be.v1",
    "docs/schemas/config_bundle_fe.json": "config_bundle.fe.v1",
}
_LOCAL_SCHEMAS = frozenset({
    "schemas/gates_v1.schema.json", "schemas/channels_v1.schema.json",
    "schemas/magic10_mechanics_v1.schema.json", "schemas/magic10_result_v1.schema.json",
    "schemas/magic10_compat_result_v1.schema.json", *_CONSUMER_SCHEMAS,
})

# HDE-EPIC040's adopted complete mechanics release.  The active loader accepts
# this exact sorted union only; catalog/manifest.json itself is never a member.
ADMITTED_RELEASE_VERSION = "1.3.0"
ADMITTED_RELEASE_BUILT_AT_UTC = "2026-08-24T18:04:49Z"
ADMITTED_RELEASE_ROSTER = tuple(sorted({
    "adapter/http_reader.py",
    "adapter/schemas/error_v1.schema.json",
    "catalog/channels_v1.json",
    "catalog/gates_v1.json",
    "catalog/magic10.json",
    "catalog/magic10_caps.json",
    "catalog/magic10_mechanics_v1.json",
    "catalog/magic10_seeds.json",
    "catalog/narratives/keys.json",
    "catalog/narratives/manifest.json",
    "catalog/narratives/palettes.json",
    "catalog/narratives/suppression_map.json",
    "catalog/narratives/templates.json",
    "engine/bodygraph/gates.py",
    "engine/bodygraph/mapped_cache.py",
    "engine/bodygraph/projection.py",
    "engine/bodygraph/resolver.py",
    "engine/bodygraph/v2_adapter.py",
    "engine/cli/main.py",
    "engine/categories/registry.py",
    "engine/compat/compute.py",
    "engine/compat/error_tokens.py",
    "engine/config/registry_loader.py",
    "engine/core/core.py",
    "engine/http/compat_handler.py",
    "engine/magic10/calculators.py",
    "engine/magic10/composite.py",
    "engine/magic10/signals.py",
    "engine/narratives/router.py",
    "engine/presenter/emitter.py",
    "engine/runtime/public.py",
    "errors/token_map/token_map.json",
    "math/thresholds.json",
    "migrations/005_identity.sql",
    "presenter/reader_v1/emitter.py",
    "schemas/channels_v1.schema.json",
    "schemas/gates_v1.schema.json",
    "schemas/magic10_compat_result_v1.schema.json",
    "schemas/magic10_mechanics_v1.schema.json",
    "schemas/magic10_result_v1.schema.json",
    "schemas/reader.v1.schema.json",
    "schemas/reader.v2.schema.json",
    "tools/bodygraph/check_magic10_gate_readiness.py",
    "engine/serializer/canon.py",
    "engine/stable/sercanon.py",
}))

if len(ADMITTED_RELEASE_ROSTER) != 45:  # pragma: no cover - import-time invariant
    raise RuntimeError("ADMITTED_RELEASE_ROSTER_INVALID")

@dataclass(frozen=True)
class _CapturedJson:
    relative_path: str
    raw: bytes
    data: object | None
    sha256: str
    size_bytes: int
    identity: tuple[int, int, int, int, int, int]


def _file_identity(info: os.stat_result) -> tuple[int, int, int, int, int, int]:
    return (info.st_dev, info.st_ino, info.st_mode, info.st_size, info.st_mtime_ns, info.st_ctime_ns)


def _safe_source_path(root: Path, relative_path: str) -> Path:
    """Check lexical identity before resolution can hide an ancestor symlink."""
    rel = Path(relative_path)
    if (not relative_path or rel.is_absolute() or '\\' in relative_path
            or rel.as_posix() != relative_path or any(part in {'.', '..'} for part in rel.parts)):
        raise SchemaValidationError('UNSAFE_SOURCE_PATH', 'source path must be a canonical relative path')
    current = root
    for part in (None, *rel.parts):
        if part is not None:
            current /= part
        try:
            info = current.lstat()
        except OSError as exc:
            raise SchemaValidationError('MISSING_FILE', f'missing source: {relative_path}') from exc
        if stat.S_ISLNK(info.st_mode):
            raise SchemaValidationError('UNSAFE_SOURCE_PATH', f'symlink source: {relative_path}')
        if current != root / rel and not stat.S_ISDIR(info.st_mode):
            raise SchemaValidationError('UNSAFE_SOURCE_PATH', f'non-directory source ancestor: {relative_path}')
    if not stat.S_ISREG(info.st_mode):
        raise SchemaValidationError('UNSAFE_SOURCE_PATH', f'non-regular source: {relative_path}')
    try:
        current.resolve(strict=True).relative_to(root.resolve(strict=True))
    except (ValueError, OSError) as exc:
        raise SchemaValidationError('UNSAFE_SOURCE_PATH', 'source escaped selected root') from exc
    return current


def _read_captured_file(root: Path, relative_path: str) -> tuple[bytes, tuple[int, int, int, int, int, int]]:
    """Read through no-follow directory descriptors, then verify the lexical source."""
    path = _safe_source_path(root, relative_path)
    before = _file_identity(path.lstat())
    descriptors: list[int] = []
    leaf: int | None = None
    try:
        # Walk from the filesystem root so even an upper ancestor swap cannot
        # redirect the read through a symlink before a later identity refusal.
        directory_flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
        descriptor = os.open(root.anchor, directory_flags)
        descriptors.append(descriptor)
        parts = (*root.parts[1:], *Path(relative_path).parts[:-1])
        for part in parts:
            descriptor = os.open(part, directory_flags, dir_fd=descriptor)
            descriptors.append(descriptor)
        leaf = os.open(Path(relative_path).name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=descriptor)
        opened = _file_identity(os.fstat(leaf))
        if not stat.S_ISREG(opened[2]):
            raise SchemaValidationError('UNSAFE_SOURCE_PATH', 'captured source is not a regular file')
        with os.fdopen(leaf, 'rb') as handle:
            leaf = None
            raw = handle.read()
            after = _file_identity(os.fstat(handle.fileno()))
        current = _file_identity(_safe_source_path(root, relative_path).lstat())
        if before != opened or opened != after or after != current:
            raise SchemaValidationError('SOURCE_CHANGED', f'source changed during capture: {relative_path}')
        return raw, after
    except RegistryConfigError:
        raise
    except OSError as exc:
        raise SchemaValidationError('SOURCE_READ_FAILED', f'cannot safely read {relative_path}') from exc
    finally:
        if leaf is not None:
            os.close(leaf)
        for descriptor in reversed(descriptors):
            os.close(descriptor)


def _duplicate_aware_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result = {}
    for key, value in pairs:
        if key in result:
            raise SchemaValidationError('DUPLICATE_JSON_KEY', 'duplicate JSON object key')
        result[key] = value
    return result


def _refuse_nonfinite(value: str) -> object:
    raise SchemaValidationError('NONFINITE_JSON', 'non-finite JSON numbers are forbidden')


def _validate_unicode(value: object) -> None:
    if isinstance(value, float) and not math.isfinite(value):
        raise SchemaValidationError('NONFINITE_JSON', 'non-finite JSON numbers are forbidden')
    if isinstance(value, str):
        if any(0xD800 <= ord(char) <= 0xDFFF for char in value):
            raise SchemaValidationError('INVALID_UNICODE', 'unpaired Unicode surrogate in JSON')
    elif isinstance(value, dict):
        for key, item in value.items():
            _validate_unicode(key)
            _validate_unicode(item)
    elif isinstance(value, list):
        for item in value:
            _validate_unicode(item)


def _parse_source_bytes(
    raw: bytes,
    relative_path: str,
    *,
    require_canonical: bool | None = None,
) -> object:
    try:
        if raw.startswith(b'\xef\xbb\xbf'):
            raise SchemaValidationError('INVALID_UTF8', 'JSON BOM is forbidden')
        text = raw.decode('utf-8', errors='strict')
        data = json.loads(text, object_pairs_hook=_duplicate_aware_object, parse_constant=_refuse_nonfinite)
        _validate_unicode(data)
        # Existing consumer schema documents retain their independently owned formatting.
        canonical_required = relative_path not in _CONSUMER_SCHEMAS if require_canonical is None else require_canonical
        if canonical_required and canon.sercanon(data, sort_keys=True) != raw:
            raise SchemaValidationError('NONCANONICAL_JSON', f'noncanonical JSON bytes: {relative_path}')
        return data
    except RegistryConfigError:
        raise
    except (UnicodeError, ValueError, TypeError, OverflowError, RecursionError) as exc:
        raise SchemaValidationError('INVALID_JSON', f'failed to parse source: {relative_path}') from exc


def _parse_release_member_bytes(raw: bytes, relative_path: str) -> object | None:
    """Validate one exact release member without rewriting or normalizing it."""
    suffix = Path(relative_path).suffix
    if suffix == '.json':
        return _parse_source_bytes(raw, relative_path, require_canonical=True)
    if suffix not in {'.py', '.sql'}:
        raise SchemaValidationError('UNSUPPORTED_MEMBER_FORMAT', 'release member format is unsupported')
    if raw.startswith(b'\xef\xbb\xbf'):
        raise SchemaValidationError('INVALID_UTF8', 'text member BOM is forbidden')
    try:
        text = raw.decode('utf-8', errors='strict')
    except UnicodeError as exc:
        raise SchemaValidationError('INVALID_UTF8', f'invalid UTF-8 member: {relative_path}') from exc
    if b'\r' in raw or not raw.endswith(b'\n') or raw.endswith(b'\n\n'):
        raise SchemaValidationError('INVALID_MEMBER_FINAL_LF', f'member must have exactly one final LF: {relative_path}')
    if not text[:-1].strip():
        raise SchemaValidationError('EMPTY_MEMBER', f'release member is empty: {relative_path}')
    if suffix == '.py':
        try:
            ast.parse(text, filename=relative_path)
        except (SyntaxError, ValueError, TypeError, MemoryError) as exc:
            raise SchemaValidationError('INVALID_PYTHON_MEMBER', f'Python member is not syntactically valid: {relative_path}') from exc
    return None


@dataclass
class _LocalCapture:
    """Bounded local construction data; not admitted, recursively frozen or active."""
    root: Path
    sources: dict[str, _CapturedJson] = field(default_factory=dict)

    def __post_init__(self) -> None:
        self.root = Path(os.path.abspath(self.root))
        # Reject the selected root itself and its existing symlink ancestors.
        for ancestor in (self.root, *self.root.parents):
            if ancestor.is_symlink():
                raise SchemaValidationError('UNSAFE_SOURCE_PATH', 'selected root has a symlink ancestor')

    def read(self, relative_path: str) -> _CapturedJson:
        if Path(relative_path).suffix != '.json':
            raise SchemaValidationError('INVALID_JSON_SOURCE', 'JSON reader accepts only .json sources')
        if relative_path in self.sources:
            return self.sources[relative_path]
        raw, after = _read_captured_file(self.root, relative_path)
        data = _parse_source_bytes(raw, relative_path)
        source = _CapturedJson(relative_path, raw, data, hashlib.sha256(raw).hexdigest(), len(raw), after)
        self.sources[relative_path] = source
        return source

    def capture_release_member(self, relative_path: str) -> _CapturedJson:
        """Capture one roster member and enforce its exact extension contract."""
        if relative_path in self.sources:
            source = self.sources[relative_path]
            _parse_release_member_bytes(source.raw, relative_path)
            return source
        raw, after = _read_captured_file(self.root, relative_path)
        data = _parse_release_member_bytes(raw, relative_path)
        source = _CapturedJson(relative_path, raw, data, hashlib.sha256(raw).hexdigest(), len(raw), after)
        self.sources[relative_path] = source
        return source

    def verify_unchanged(
        self,
        *,
        identity_only: frozenset[str] = frozenset(),
    ) -> None:
        if not identity_only.issubset(self.sources):
            raise SchemaValidationError(
                'UNBOUND_SOURCE', 'identity-only verification requires a captured source'
            )
        for name, source in self.sources.items():
            if name in identity_only:
                continue
            raw, identity = _read_captured_file(self.root, name)
            if identity != source.identity or raw != source.raw:
                raise SchemaValidationError('SOURCE_CHANGED', f'captured source changed: {name}')
        # A previously checked file can change while a later file is read.
        # Recheck the whole identity set after all verification reads finish.
        for name, source in self.sources.items():
            try:
                identity = _file_identity(_safe_source_path(self.root, name).lstat())
            except OSError as exc:
                raise SchemaValidationError('SOURCE_CHANGED', f'captured source changed: {name}') from exc
            if identity != source.identity:
                raise SchemaValidationError('SOURCE_CHANGED', f'captured source changed: {name}')


@dataclass
class _RegistryCapture(_LocalCapture):
    config: RegistryConfig | None = None


@dataclass
class _MechanicsCapture(_LocalCapture):
    config: Mapping[str, object] | None = None
    registry: RegistryConfig | None = None


def _reject_schema_retrieval(uri: str) -> object:
    raise NoSuchResource(ref=uri)


def _schema_references(value: object) -> None:
    if isinstance(value, dict):
        for key, item in value.items():
            if key in {'$ref', '$dynamicRef', '$recursiveRef'} and (not isinstance(item, str) or not item.startswith('#')):
                raise SchemaValidationError('NONLOCAL_SCHEMA_REFERENCE', 'only same-document schema references are supported')
            _schema_references(item)
    elif isinstance(value, list):
        for item in value:
            _schema_references(item)


def _validate_local_schema(capture: _LocalCapture, relative_path: str, data: object) -> None:
    """Execute the owning captured schema with strict integers and no remote lookup."""
    if relative_path not in _LOCAL_SCHEMAS:
        raise SchemaValidationError('UNKNOWN_SCHEMA', 'schema is outside the local owning set')
    schema = capture.read(relative_path).data
    if not isinstance(schema, dict):
        raise SchemaValidationError('INVALID_SCHEMA', 'schema must be an object')
    if relative_path in _CONSUMER_SCHEMAS:
        expected_draft = 'http://json-schema.org/draft-07/schema#'
        expected_identity = _CONSUMER_SCHEMAS[relative_path]
        properties = schema.get('properties')
        identity_schema = properties.get('schema') if isinstance(properties, dict) else None
        if not isinstance(identity_schema, dict):
            raise SchemaValidationError('INVALID_SCHEMA', 'consumer schema identity must be an object')
        if identity_schema.get('const') != expected_identity:
            raise SchemaValidationError('SCHEMA_IDENTITY_MISMATCH', 'consumer schema identity mismatch')
        base_validator = jsonschema.Draft7Validator
    else:
        expected_draft = 'https://json-schema.org/draft/2020-12/schema'
        if schema.get('$id') != relative_path:
            raise SchemaValidationError('SCHEMA_IDENTITY_MISMATCH', 'owning schema identity mismatch')
        base_validator = jsonschema.Draft202012Validator
    if schema.get('$schema') != expected_draft:
        raise SchemaValidationError('SCHEMA_DRAFT_MISMATCH', 'owning schema draft mismatch')
    _schema_references(schema)
    strict = validators.extend(base_validator, type_checker=base_validator.TYPE_CHECKER.redefine('integer', lambda checker, value: type(value) is int))
    try:
        strict.check_schema(schema)
        strict(schema, registry=Registry(retrieve=_reject_schema_retrieval)).validate(data)
    except RegistryConfigError:
        raise
    except Exception as exc:
        raise SchemaValidationError('SCHEMA_VALIDATION_FAILED', f'owning schema refused: {relative_path}', {'schema': relative_path}) from exc


def _validate_release_schema_document(
    capture: _LocalCapture,
    relative_path: str,
    *,
    expected_draft: str,
    expected_identity: str | None,
) -> None:
    """Validate a captured schema dependency without manufacturing an instance."""
    schema = capture.read(relative_path).data
    if not isinstance(schema, dict):
        raise SchemaValidationError('INVALID_SCHEMA', 'schema must be an object')
    if schema.get('$schema') != expected_draft:
        raise SchemaValidationError('SCHEMA_DRAFT_MISMATCH', 'release schema draft mismatch')
    if expected_identity is None:
        if '$id' in schema:
            raise SchemaValidationError('SCHEMA_IDENTITY_MISMATCH', 'release schema identity mismatch')
    elif schema.get('$id') != expected_identity:
        raise SchemaValidationError('SCHEMA_IDENTITY_MISMATCH', 'release schema identity mismatch')
    _schema_references(schema)
    base_validator = (
        jsonschema.Draft7Validator
        if expected_draft == 'http://json-schema.org/draft-07/schema#'
        else jsonschema.Draft202012Validator
    )
    strict = validators.extend(
        base_validator,
        type_checker=base_validator.TYPE_CHECKER.redefine(
            'integer', lambda checker, value: type(value) is int
        ),
    )
    try:
        strict.check_schema(schema)
        resource = Resource.from_contents(schema)
        resolver = Registry(retrieve=_reject_schema_retrieval).resolver_with_root(resource)

        def check_references(node: object) -> None:
            if isinstance(node, dict):
                # The adopted schemas use one document identity. A nested ID
                # would change the meaning of otherwise same-document refs.
                if node is not schema and '$id' in node:
                    raise SchemaValidationError(
                        'NESTED_SCHEMA_ID_FORBIDDEN', 'nested schema identities are not admitted'
                    )
                for key, value in node.items():
                    if key in {'$ref', '$dynamicRef', '$recursiveRef'}:
                        try:
                            target = resolver.lookup(value).contents
                        except Exception as exc:
                            raise SchemaValidationError(
                                'UNRESOLVED_SCHEMA_REFERENCE', 'schema reference has no captured local target'
                            ) from exc
                        if not isinstance(target, (dict, bool)):
                            raise SchemaValidationError(
                                'INVALID_SCHEMA_REFERENCE_TARGET', 'schema reference target is not a schema'
                            )
                    check_references(value)
            elif isinstance(node, list):
                for value in node:
                    check_references(value)

        check_references(schema)
    except RegistryConfigError:
        raise
    except Exception as exc:
        raise SchemaValidationError(
            'SCHEMA_VALIDATION_FAILED',
            f'release schema refused: {relative_path}',
            {'schema': relative_path},
        ) from exc


def _load_json(path: Path) -> object:
    return _LocalCapture(path.parent).read(path.name).data


def validate_channel_gates(gates: object, channel_id: str | None = None) -> tuple[int, int]:
    """Validate authoritative numeric endpoints without sorting or coercion."""
    if not isinstance(gates, (list, tuple)) or len(gates) != 2:
        raise SchemaValidationError('INVALID_CHANNELS', 'channel must reference two gates')
    if any(type(gate) is not int or not 1 <= gate <= 64 for gate in gates):
        raise SchemaValidationError('INVALID_CHANNEL_GATE', 'Channel endpoints must be exact integers in 1..64')
    first, second = gates
    if first == second:
        raise SchemaValidationError('DUPLICATE_CHANNEL_GATE', 'Channel must reference two distinct gates')
    if first > second:
        raise SchemaValidationError('CHANNEL_GATE_ORDER_MISMATCH', 'Channel endpoints must already be ascending')
    if channel_id is not None:
        if not isinstance(channel_id, str) or re.fullmatch(r'(?:0[1-9]|[1-5][0-9]|6[0-4])-(?:0[1-9]|[1-5][0-9]|6[0-4])', channel_id) is None:
            raise SchemaValidationError('INVALID_CHANNEL_ID', 'invalid ASCII Channel ID')
        if channel_id != f'{first:02d}-{second:02d}':
            raise SchemaValidationError('CHANNEL_ID_MISMATCH', f'channel id {channel_id} does not match gates {gates}')
    return first, second


def _normalize_channel_id(channel_id: str, gates: Iterable[int]) -> str:
    pair = validate_channel_gates(gates, channel_id)
    return f'{pair[0]:02d}-{pair[1]:02d}'


def _load_gates(
    capture: _LocalCapture,
    *,
    validate_schema: bool = True,
) -> tuple[dict[int, Gate], tuple[str, ...]]:
    raw = capture.read('catalog/gates_v1.json').data
    if validate_schema:
        _validate_local_schema(capture, 'schemas/gates_v1.schema.json', raw)
    if not isinstance(raw, dict) or set(raw) != {'gates'} or not isinstance(raw.get('gates'), list):
        raise SchemaValidationError('INVALID_GATES', 'gate catalog must contain exactly a gates list')
    gates = {}
    source_ids = []
    for entry in raw['gates']:
        if (not isinstance(entry, dict) or set(entry) != {'gate', 'center'}
                or not isinstance(entry.get('center'), str) or not entry['center']):
            raise SchemaValidationError('INVALID_GATES', 'gate rows must contain exact gate and center fields')
        gate_id = entry['gate']
        if type(gate_id) is not int or not 1 <= gate_id <= 64:
            raise SchemaValidationError('INVALID_GATES', 'gate id must be an exact integer in 1..64')
        if gate_id in gates:
            raise DuplicateIdError('DUPLICATE_GATE', f'duplicate gate id {gate_id}')
        gates[gate_id] = Gate(gate_id, entry['center'])
        source_ids.append(gate_id)
    if tuple(source_ids) != FROZEN_GATE_IDS:
        raise SchemaValidationError('GATE_ID_ORDER_MISMATCH', 'gate catalog rows must preserve the exact 1..64 source order', {'actual': source_ids, 'expected': list(FROZEN_GATE_IDS)})
    counts = {center: sum(g.center == center for g in gates.values()) for center in sorted({g.center for g in gates.values()})}
    if counts != FROZEN_GATE_CENTER_COUNTS:
        raise SchemaValidationError('GATE_CENTER_COUNTS_MISMATCH', 'gate center counts must match the frozen topology', {'actual': counts, 'expected': dict(FROZEN_GATE_CENTER_COUNTS)})
    return gates, tuple(sorted(counts))


def _load_channels(capture: _LocalCapture, *, gate_map: Mapping[int, Gate], known_centers: set[str], allow_aliases: bool, alias_ledger: Mapping[str, str] | None) -> tuple[dict[str, Channel], dict[str, str], tuple[str, ...]]:
    raw = capture.read('catalog/channels_v1.json').data
    _validate_local_schema(capture, 'schemas/channels_v1.schema.json', raw)
    channels = {}
    domains = set()
    for entry in raw['channels']:
        validate_channel_gates(entry['gates'], entry['id'])
    source_ids = [entry['id'] for entry in raw['channels']]
    if len(source_ids) != len(set(source_ids)):
        raise DuplicateIdError('DUPLICATE_CHANNEL', 'duplicate channel id')
    expected_ids = set(FROZEN_CHANNEL_IDS)
    if set(FROZEN_CHANNEL_ENDPOINT_CENTERS) != expected_ids:
        raise SchemaValidationError('FROZEN_CHANNEL_CENTER_ROSTER_MISMATCH', 'frozen Channel center bindings must cover the exact Channel roster')
    if set(source_ids) != expected_ids:
        raise SchemaValidationError('CHANNEL_ID_ROSTER_MISMATCH', 'channel identities must match the frozen 36-Channel roster', {'missing': sorted(expected_ids - set(source_ids)), 'unknown': sorted(set(source_ids) - expected_ids)})
    for entry in raw['channels']:
        channel_id = entry['id']
        pair = validate_channel_gates(entry['gates'], channel_id)
        if channel_id in channels:
            raise DuplicateIdError('DUPLICATE_CHANNEL', f'duplicate channel id {channel_id}')
        for gate in pair:
            if gate not in gate_map:
                raise UnknownIdError('UNKNOWN_GATE', f'channel {channel_id} references unknown gate {gate}')
        centers = entry['centers']
        if any(center not in known_centers for center in centers):
            raise UnknownIdError('UNKNOWN_CENTER', f'channel {channel_id} references unknown center')
        actual_endpoints = {gate: gate_map[gate].center for gate in pair}
        projected = sorted(set(actual_endpoints.values()))
        if len(projected) != 2:
            raise SchemaValidationError('DUPLICATE_CHANNEL_CENTER', f'channel {channel_id} gate projection must contain two distinct centers')
        if centers != projected:
            raise SchemaValidationError('CHANNEL_CENTER_PROJECTION_MISMATCH', f'channel {channel_id} centers do not match its gate projection')
        expected_endpoints = dict(FROZEN_CHANNEL_ENDPOINT_CENTERS.get(channel_id, ()))
        if actual_endpoints != expected_endpoints:
            raise SchemaValidationError('CHANNEL_CENTER_IDENTITY_MISMATCH', f'channel {channel_id} endpoints do not match the frozen Channel topology', {'actual': [[g, actual_endpoints[g]] for g in sorted(actual_endpoints)], 'expected': [[g, expected_endpoints[g]] for g in sorted(expected_endpoints)]})
        if (entry['circuit_primary'], entry['substream']) != _CHANNEL_CLASSIFICATIONS.get(channel_id):
            raise SchemaValidationError('CHANNEL_ASSIGNMENT_MISMATCH', f'channel {channel_id} classification differs from the approved assignment')
        if (entry['primary_domain'], entry['domains'], entry['flags']) != _CHANNEL_PRODUCT_METADATA.get(channel_id):
            raise SchemaValidationError('CHANNEL_PRODUCT_METADATA_MISMATCH', f'channel {channel_id} Product metadata differs from its retained source')
        domains.update(entry['domains'])
        channels[channel_id] = Channel(channel_id, pair, tuple(centers), entry['circuit_primary'], entry['substream'], entry['primary_domain'], tuple(entry['domains']), tuple(entry['flags']))
    if tuple(channels) != FROZEN_CHANNEL_IDS:
        raise SchemaValidationError('CHANNEL_ID_ROSTER_MISMATCH', 'channel identities must preserve the frozen 36-Channel source order')
    aliases = {}
    if alias_ledger is not None and not isinstance(alias_ledger, Mapping):
        raise AliasPolicyError('INVALID_ALIAS_LEDGER', 'alias ledger must be a mapping')
    if alias_ledger and not allow_aliases:
        raise AliasPolicyError('ALIASES_FORBIDDEN', 'alias input is not allowed by default')
    for alias, target in (alias_ledger or {}).items():
        if not isinstance(alias, str) or not isinstance(target, str):
            raise AliasPolicyError('INVALID_ALIAS', 'alias and target must be strings')
        if re.fullmatch(r'(?:0[1-9]|[1-5][0-9]|6[0-4])-(?:0[1-9]|[1-5][0-9]|6[0-4])', alias) is None:
            raise AliasPolicyError('INVALID_ALIAS', 'alias must use the supported ASCII spelling')
        a, b = (int(part) for part in alias.split('-'))
        if a >= b:
            raise AliasPolicyError('INVALID_ALIAS', 'alias spelling must be min-first')
        if alias in channels or alias in aliases:
            raise DuplicateIdError('DUPLICATE_ALIAS', 'alias collides with a canonical or prior identity')
        if target not in channels:
            raise UnknownIdError('UNKNOWN_ALIAS_TARGET', 'alias target is not a canonical Channel')
        aliases[alias] = target
    return channels, aliases, tuple(sorted(domains))


def _load_magic10(capture: _LocalCapture) -> tuple[tuple[str, ...], dict[str, Magic10Caps], dict[str, Magic10Seed]]:
    order_raw = capture.read("catalog/magic10.json").data
    if not isinstance(order_raw, dict) or set(order_raw) != {"order"}:
        raise SchemaValidationError("INVALID_MAGIC10", "magic10.json must contain an order array")
    order_list = order_raw.get("order")
    if not isinstance(order_list, list):
        raise SchemaValidationError("INVALID_MAGIC10", "magic10 order must be a list")
    magic_order = tuple(order_list)
    if magic_order != FROZEN_MAGIC10_ORDER:
        raise SchemaValidationError("MAGIC10_ORDER_MISMATCH", "magic10 order must match registry")
    if set(FROZEN_MAGIC10_INPUTS) != set(magic_order):
        raise SchemaValidationError(
            "FROZEN_MAGIC10_INPUT_ROSTER_MISMATCH",
            "frozen Magic-10 input bindings must cover the exact category roster",
        )

    caps_raw = capture.read("catalog/magic10_caps.json").data
    if not isinstance(caps_raw, dict):
        raise SchemaValidationError("INVALID_MAGIC10", "magic10_caps must be an object")
    if set(caps_raw.keys()) != set(magic_order):
        raise SchemaValidationError("MAGIC10_CAPS_COVERAGE", "magic10_caps must cover full magic10 order")
    caps: dict[str, Magic10Caps] = {}
    for key, entry in caps_raw.items():
        if not isinstance(entry, dict) or set(entry) != {"inputs", "bounds"}:
            raise SchemaValidationError(
                "INVALID_MAGIC10", "magic10_caps entries must contain inputs and bounds only"
            )
        inputs = entry.get("inputs")
        bounds = entry.get("bounds")
        if not isinstance(inputs, list) or not inputs:
            raise SchemaValidationError("INVALID_MAGIC10", f"magic10_caps[{key}] inputs must be a non-empty list")
        if any(not isinstance(value, str) or not value for value in inputs):
            raise SchemaValidationError(
                "INVALID_MAGIC10", f"magic10_caps[{key}] inputs must be non-empty strings"
            )
        expected_inputs = FROZEN_MAGIC10_INPUTS[key]
        if tuple(inputs) != expected_inputs:
            raise SchemaValidationError(
                "MAGIC10_INPUTS_MISMATCH",
                f"magic10_caps[{key}] inputs must match the frozen ordered contract",
                {
                    "actual": list(inputs),
                    "expected": list(expected_inputs),
                },
            )
        if not isinstance(bounds, dict) or set(bounds) != {"min", "max"}:
            raise SchemaValidationError("INVALID_MAGIC10", f"magic10_caps[{key}] bounds invalid")
        minimum = bounds["min"]
        maximum = bounds["max"]
        if (
            type(minimum) is not int
            or type(maximum) is not int
            or minimum != 0
            or maximum != 100
        ):
            raise SchemaValidationError(
                "INVALID_MAGIC10",
                f"magic10_caps[{key}] bounds must be integers with min 0 and max 100",
            )
        caps[key] = Magic10Caps(
            inputs=tuple(inputs), bounds={"min": minimum, "max": maximum}
        )

    seeds_raw = capture.read("catalog/magic10_seeds.json").data
    if not isinstance(seeds_raw, dict):
        raise SchemaValidationError("INVALID_MAGIC10", "magic10_seeds must be an object")
    unknown_seeds = set(seeds_raw.keys()) - set(magic_order)
    if unknown_seeds:
        raise UnknownIdError("UNKNOWN_MAGIC10_SEED", f"unknown magic10 seed ids: {sorted(unknown_seeds)}")
    seeds: dict[str, Magic10Seed] = {}
    for key, entry in seeds_raw.items():
        if not isinstance(entry, dict):
            raise SchemaValidationError("INVALID_MAGIC10", "magic10_seeds entries must be objects")
        required = {"template_id", "seed_version", "updated_at_utc", "checksum_sha256"}
        if set(entry) != required:
            raise SchemaValidationError(
                "INVALID_MAGIC10", f"magic10_seeds[{key}] fields invalid"
            )
        if any(not isinstance(entry[field], str) or not entry[field] for field in required):
            raise SchemaValidationError(
                "INVALID_MAGIC10", f"magic10_seeds[{key}] values must be non-empty strings"
            )
        checksum = entry["checksum_sha256"]
        if re.fullmatch(r"[0-9a-f]{64}", checksum) is None:
            raise SchemaValidationError(
                "INVALID_MAGIC10", f"magic10_seeds[{key}] checksum invalid"
            )
        timestamp = entry["updated_at_utc"]
        if re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z", timestamp) is None:
            raise SchemaValidationError(
                "INVALID_MAGIC10", f"magic10_seeds[{key}] timestamp invalid"
            )
        try:
            datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%SZ")
        except ValueError as exc:
            raise SchemaValidationError(
                "INVALID_MAGIC10", f"magic10_seeds[{key}] timestamp invalid"
            ) from exc
        seeds[key] = Magic10Seed(
            template_id=entry["template_id"],
            seed_version=entry["seed_version"],
            updated_at_utc=timestamp,
            checksum_sha256=checksum,
        )

    return magic_order, caps, seeds


def _parse_manifest(raw: object) -> Manifest:
    if not isinstance(raw, dict):
        raise SchemaValidationError("INVALID_MANIFEST", "manifest.json must be an object")
    expected_keys = {"root", "version", "built_at_utc", "files"}
    if set(raw.keys()) != expected_keys:
        raise SchemaValidationError(
            "INVALID_MANIFEST_KEYS",
            "manifest.json must contain exactly root, version, built_at_utc, files",
        )

    root = raw.get("root")
    version = raw.get("version")
    built_at_utc = raw.get("built_at_utc")
    files_raw = raw.get("files")

    if root != "catalog/":
        raise SchemaValidationError("INVALID_MANIFEST_ROOT", "manifest root must be 'catalog/'")
    if not isinstance(version, str) or not version:
        raise SchemaValidationError("INVALID_MANIFEST_VERSION", "manifest version must be a non-empty string")
    if not isinstance(built_at_utc, str) or not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z", built_at_utc):
        raise SchemaValidationError(
            "INVALID_MANIFEST_TIMESTAMP", "built_at_utc must be an ISO-8601 UTC timestamp ending with Z"
        )
    try:
        datetime.strptime(built_at_utc, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError as exc:
        raise SchemaValidationError("INVALID_MANIFEST_TIMESTAMP", "manifest timestamp is not a valid UTC date") from exc
    if not isinstance(files_raw, list):
        raise SchemaValidationError("INVALID_MANIFEST", "manifest files must be a list")

    manifest_entries: list[ManifestEntry] = []
    seen_paths: set[str] = set()
    last_path: str | None = None
    for entry in files_raw:
        if not isinstance(entry, dict):
            raise SchemaValidationError("INVALID_MANIFEST", "manifest file entry must be an object")
        if set(entry.keys()) != {"path", "sha256", "size"}:
            raise SchemaValidationError("INVALID_MANIFEST", "manifest file entry must contain path, sha256, size only")

        path = entry.get("path")
        sha = entry.get("sha256")
        size = entry.get("size")
        if not isinstance(path, str) or not path:
            raise SchemaValidationError("INVALID_MANIFEST", "manifest file path must be a non-empty string")
        if (Path(path).is_absolute() or "\\" in path or Path(path).as_posix() != path
                or any(part in {".", ".."} for part in Path(path).parts)
                or not path.isascii()):
            raise SchemaValidationError("INVALID_MANIFEST_PATH", "manifest file path must be canonical and relative")
        if path == "catalog/manifest.json":
            raise SchemaValidationError("SELF_LISTING_MANIFEST_FORBIDDEN", "manifest.json must not list itself")
        if not isinstance(sha, str) or not re.fullmatch(r"[0-9a-f]{64}", sha):
            raise SchemaValidationError("INVALID_MANIFEST", f"manifest sha256 invalid for {path}")
        if type(size) is not int or size < 0:
            raise SchemaValidationError("INVALID_MANIFEST", f"manifest size invalid for {path}")
        if path in seen_paths:
            raise DuplicateIdError("DUPLICATE_MANIFEST_ENTRY", f"duplicate manifest path {path}")
        if last_path is not None and path <= last_path:
            raise SchemaValidationError("INVALID_MANIFEST_ORDER", "manifest files must be ASCII-sorted and deduped by path")

        seen_paths.add(path)
        last_path = path
        manifest_entries.append(ManifestEntry(path=path, sha256=sha, size=size))

    return Manifest(
        root=str(root),
        version=str(version),
        built_at_utc=str(built_at_utc),
        files=tuple(manifest_entries),
    )


def load_manifest(root: Path | str | None = None) -> Manifest:
    """Validate manifest structure and bytes; full member admission belongs to PR02."""
    capture = _LocalCapture(Path(root) if root is not None else Path.cwd())
    result = _parse_manifest(capture.read('catalog/manifest.json').data)
    capture.verify_unchanged()
    return result


def _capture_registry_config(root: Path | str | None = None, *, allow_aliases: bool = False, alias_ledger: Mapping[str, str] | None = None) -> _RegistryCapture:
    capture = _RegistryCapture(Path(root) if root is not None else Path.cwd())
    gates, centers = _load_gates(capture)
    channels, aliases, domains = _load_channels(capture, gate_map=gates, known_centers=set(centers), allow_aliases=allow_aliases, alias_ledger=alias_ledger)
    order, caps, seeds = _load_magic10(capture)
    manifest = _parse_manifest(capture.read('catalog/manifest.json').data)
    capture.config = RegistryConfig(gates, channels, aliases, order, caps, seeds, manifest, centers, domains)
    capture.verify_unchanged()
    return capture


def load_registry_config(root: Path | str | None = None, *, allow_aliases: bool = False, alias_ledger: Mapping[str, str] | None = None) -> RegistryConfig:
    """Return the existing local registry view, without mechanics release admission."""
    return _capture_registry_config(root, allow_aliases=allow_aliases, alias_ledger=alias_ledger).config


def _validate_thresholds(data: object) -> Mapping[str, object]:
    """Validate the existing lower-level domain; initial mechanics pins its defaults."""
    if not isinstance(data, dict) or set(data) != {'clamp', 'edges', 'rounding', 'version'}:
        raise SchemaValidationError('INVALID_THRESHOLDS', 'threshold fields must be closed')
    clamp, edges = data['clamp'], data['edges']
    if (not isinstance(clamp, list) or len(clamp) != 2 or any(type(x) is not int for x in clamp)
            or clamp != [0, 100] or not isinstance(edges, list) or len(edges) != 4
            or any(type(x) is not int or not 0 <= x <= 100 for x in edges)
            or any(a >= b for a, b in zip(edges, edges[1:])) or edges[-1] != 100
            or data['rounding'] != 'ROUND_HALF_UP' or data['version'] != '1'):
        raise SchemaValidationError('INVALID_THRESHOLDS', 'threshold domain/order/type contract failed')
    return data


def _validate_mechanics_domain(capture: _LocalCapture, data: object, registry: RegistryConfig) -> None:
    """Check legal v1 domains/relations only; this is not a publishing/admission path."""
    _validate_local_schema(capture, 'schemas/magic10_mechanics_v1.schema.json', data)
    profiles = data['profiles']
    if [row['profile_id'] for row in profiles] != sorted(_PROFILE_RESPONSES):
        raise SchemaValidationError('PROFILE_ROSTER_MISMATCH', 'profiles must preserve the exact ordered roster')
    inequalities = {
        'activation_bp_v1': ('electromagnetic', 'dominance', 'companionship', 'compromise', 'none'),
        'coherence_bp_v1': ('companionship', 'electromagnetic', 'dominance', 'compromise', 'none'),
        'expression_bp_v1': ('electromagnetic', 'companionship', 'dominance', 'compromise', 'none'),
    }
    for row in profiles:
        values = [row['responses'][name] for name in inequalities[row['profile_id']]]
        if any(a <= b for a, b in zip(values, values[1:])):
            raise SchemaValidationError('PROFILE_INEQUALITY_MISMATCH', 'profile response ordering failed')
    expected_signal_order = [signal for category in registry.magic10_order for signal in registry.magic10_caps[category].inputs]
    if [row['signal_id'] for row in data['signals']] != expected_signal_order:
        raise SchemaValidationError('SIGNAL_ORDER_MISMATCH', 'signal order must flatten the exact ordered caps pairs')
    used = set()
    by_id = {}
    for signal in data['signals']:
        signal_id = signal['signal_id']
        expected_profile, _ = _SIGNAL_MEMBERSHIP[signal_id]
        if expected_profile.endswith('_bp_v1'):
            if signal.get('profile_id') != expected_profile or signal['operation'] != 'weighted_state_sum_v1':
                raise SchemaValidationError('SIGNAL_OPERATION_MISMATCH', 'ordinary signal profile/operation mismatch')
        elif 'profile_id' in signal or signal['operation'] != expected_profile:
            raise SchemaValidationError('SIGNAL_OPERATION_MISMATCH', 'Balance operation/profile mismatch')
        members = [row['channel_id'] for row in signal['channels']]
        if members != sorted(set(members)) or any(member not in registry.channels for member in members):
            raise SchemaValidationError('SIGNAL_MEMBERSHIP_INVALID', 'members must be unique ordered canonical Channels')
        by_id[signal_id] = set(members)
        used.update(members)
    for category in registry.magic10_order:
        a, b = registry.magic10_caps[category].inputs
        if by_id[a] & by_id[b]:
            raise SchemaValidationError('SIGNAL_CATEGORY_OVERLAP', 'a Channel cannot occur in both category signals')
    if used != set(registry.channels):
        raise SchemaValidationError('CHANNEL_USE_INCOMPLETE', 'the signal map must use every canonical Channel')
    if [row['category_id'] for row in data['category_weights']] != list(registry.magic10_order):
        raise SchemaValidationError('CATEGORY_ORDER_MISMATCH', 'category weights must preserve exact category order')
    for name, path in _MECHANICS_SOURCE_PATHS.items():
        source = capture.read(path)
        if data['sources'][name] != {'path': path, 'sha256': source.sha256}:
            raise SchemaValidationError('MECHANICS_SOURCE_MISMATCH', f'mechanics source binding mismatch: {name}')
    _validate_thresholds(capture.read('math/thresholds.json').data)


def _validate_initial_mechanics(capture: _LocalCapture, data: object, registry: RegistryConfig) -> None:
    _validate_mechanics_domain(capture, data, registry)
    if data['config_id'] != 'm10-channel-state-v1.0.0':
        raise SchemaValidationError('INITIAL_CONFIG_ID_MISMATCH', 'initial mechanics config identity mismatch')
    if data['profiles'] != [{'profile_id': name, 'responses': responses} for name, responses in sorted(_PROFILE_RESPONSES.items())]:
        raise SchemaValidationError('INITIAL_PROFILE_MISMATCH', 'initial mechanics responses differ from the adopted defaults')
    for signal in data['signals']:
        _, ids = _SIGNAL_MEMBERSHIP[signal['signal_id']]
        expected = [{'channel_id': name, 'weight': 1} for name in ids]
        if signal['channels'] != expected:
            raise SchemaValidationError('INITIAL_SIGNAL_MAP_MISMATCH', 'initial membership/default weights differ from the adopted map')
    if sum(len(signal['channels']) for signal in data['signals']) != 90:
        raise SchemaValidationError('INITIAL_MEMBERSHIP_COUNT_MISMATCH', 'initial map must contain ninety memberships')
    if any(row['weights'] != [1, 1] for row in data['category_weights']):
        raise SchemaValidationError('INITIAL_CATEGORY_WEIGHTS_MISMATCH', 'initial category weights must be [1,1]')
    if capture.read('math/thresholds.json').data['edges'] != [24, 49, 74, 100]:
        raise SchemaValidationError('INITIAL_THRESHOLDS_MISMATCH', 'initial mechanics thresholds differ from the adopted maxima')


def _capture_mechanics_config(root: Path | str | None = None) -> _MechanicsCapture:
    """Validate the complete initial candidate; never return an active release handle."""
    base = _capture_registry_config(root)
    capture = _MechanicsCapture(base.root, base.sources, registry=base.config)
    data = capture.read('catalog/magic10_mechanics_v1.json').data
    _validate_initial_mechanics(capture, data, base.config)
    capture.config = data
    capture.verify_unchanged()
    return capture


def _validate_admitted_manifest(manifest: Manifest) -> None:
    paths = tuple(entry.path for entry in manifest.files)
    if paths != ADMITTED_RELEASE_ROSTER:
        expected = set(ADMITTED_RELEASE_ROSTER)
        actual = set(paths)
        if actual < expected:
            raise SchemaValidationError(
                'INCOMPLETE_RELEASE_ROSTER',
                'release manifest does not yet contain the complete adopted roster',
            )
        raise SchemaValidationError(
            'RELEASE_ROSTER_MISMATCH',
            'release manifest does not contain the exact adopted roster',
        )
    if manifest.version != ADMITTED_RELEASE_VERSION:
        raise SchemaValidationError(
            'RELEASE_VERSION_MISMATCH', 'release manifest version is not the adopted version'
        )
    if manifest.built_at_utc != ADMITTED_RELEASE_BUILT_AT_UTC:
        raise SchemaValidationError(
            'RELEASE_TIMESTAMP_MISMATCH',
            'release manifest timestamp is not the adopted timestamp',
        )


def _capture_admitted_members(
    capture: _MechanicsCapture,
    manifest: Manifest,
) -> tuple[SourceIdentity, ...]:
    identities: list[SourceIdentity] = []
    for entry in manifest.files:
        source = capture.capture_release_member(entry.path)
        if source.sha256 != entry.sha256:
            raise SchemaValidationError(
                'MANIFEST_MEMBER_HASH_MISMATCH',
                f'manifest digest does not match captured member: {entry.path}',
            )
        if source.size_bytes != entry.size:
            raise SchemaValidationError(
                'MANIFEST_MEMBER_SIZE_MISMATCH',
                f'manifest size does not match captured member: {entry.path}',
            )
        identities.append(SourceIdentity(entry.path, source.sha256, source.size_bytes))
    return tuple(identities)


def _admission_execution_provenance(
) -> tuple[Path, tuple[tuple[str, CodeType, int], ...]]:
    """Validate the eight actual consumers' passive import provenance.

    This proves neither historical imported bytes nor arbitrary in-process
    tamper resistance. It establishes safe common origin and compilation
    semantics for the bounded executable-equivalence comparison below.
    """
    # Resolve mechanics only at admission, after this module's types exist.
    # These are ordinary imports from the executing installation, never imports
    # of captured release bytes. Keeping them here avoids core/type import cycles.
    try:
        from engine.core import core as pure_core
        from engine.magic10 import calculators, composite, signals
    except Exception as exc:
        raise SchemaValidationError(
            'EXECUTION_PROVENANCE_UNAVAILABLE', 'covered mechanics module is unavailable',
        ) from exc
    owners = (
        ('engine/config/registry_loader.py', 'engine.config.registry_loader', globals()),
        ('engine/serializer/canon.py', 'engine.serializer.canon', canon),
        ('engine/stable/sercanon.py', 'engine.stable.sercanon', getattr(canon, 'stable_sercanon', None)),
        ('engine/categories/registry.py', 'engine.categories.registry', category_registry),
        ('engine/core/core.py', 'engine.core.core', pure_core),
        ('engine/magic10/composite.py', 'engine.magic10.composite', composite),
        ('engine/magic10/signals.py', 'engine.magic10.signals', signals),
        ('engine/magic10/calculators.py', 'engine.magic10.calculators', calculators),
    )
    root: Path | None = None
    executions: list[tuple[str, CodeType, int]] = []
    for relative_path, expected_name, owner in owners:
        if isinstance(owner, ModuleType):
            namespace = vars(owner)
        elif owner is globals():
            namespace = owner
        else:
            raise SchemaValidationError('EXECUTION_PROVENANCE_UNAVAILABLE', 'covered admission module is unavailable')
        spec = namespace.get('__spec__')
        if getattr(spec, '_initializing', False):
            raise SchemaValidationError('EXECUTION_PROVENANCE_UNAVAILABLE', 'covered module is partially initialized')
        provenance = namespace.get('_MODULE_EXECUTION')
        if type(provenance) is not tuple or len(provenance) != 6:
            raise SchemaValidationError('EXECUTION_PROVENANCE_UNAVAILABLE', 'module execution provenance is unavailable')
        code, name, filename, origin, optimization, cache_tag = provenance
        if not isinstance(code, CodeType) or code.co_name != '<module>':
            raise SchemaValidationError('EXECUTION_PROVENANCE_UNAVAILABLE', 'top-level execution code is unavailable')
        if (
            type(optimization) is not int or optimization not in (0, 1, 2)
            or optimization != _sys.flags.optimize
            or not isinstance(cache_tag, str) or not cache_tag
            or cache_tag != _sys.implementation.cache_tag
        ):
            raise SchemaValidationError('EXECUTION_SEMANTICS_MISMATCH', 'module compilation semantics are incompatible')
        if (
            name != expected_name or namespace.get('__name__') != expected_name
            or getattr(spec, 'name', None) != expected_name
            or not isinstance(filename, str) or not isinstance(origin, str)
            or filename != origin or namespace.get('__file__') != filename
            or getattr(spec, 'origin', None) != origin
            or code.co_filename != filename
        ):
            raise SchemaValidationError('UNSAFE_SOURCE_PATH', 'module origin does not match retained execution provenance')
        path = Path(filename)
        relative = Path(relative_path)
        if (
            not path.is_absolute() or str(path) != filename
            or '..' in path.parts or path.parts[-len(relative.parts):] != relative.parts
        ):
            raise SchemaValidationError('UNSAFE_SOURCE_PATH', 'module origin is not the owning absolute source path')
        module_root = path.parents[len(relative.parts) - 1]
        if root is None:
            root = module_root
        elif module_root != root:
            raise SchemaValidationError('UNSAFE_SOURCE_PATH', 'covered admission modules have different roots')
        _safe_source_path(module_root, relative_path)
        executions.append((relative_path, code, optimization))
    assert root is not None  # the fixed eight-owner set is nonempty
    return root, tuple(executions)


def _validate_executing_admission_sources(
    capture: _MechanicsCapture,
    executions: tuple[tuple[str, CodeType, int], ...],
) -> None:
    """Compare actual executed code with compilation of manifest-owned bytes.

    Compilation is passive: no captured source is executed or imported. Code
    equality is deliberately separate from exact source and release identities.
    """
    for relative_path, executed, optimization in executions:
        source = capture.sources.get(relative_path)
        if source is None or relative_path not in ADMITTED_RELEASE_ROSTER:
            raise SchemaValidationError('UNBOUND_SOURCE', 'executing module source is not captured and manifest-bound')
        try:
            compiled = compile(
                source.raw, executed.co_filename, 'exec',
                dont_inherit=True, optimize=optimization,
            )
        except Exception as exc:
            raise SchemaValidationError('EXECUTION_COMPILATION_FAILED', 'captured admission source cannot be compiled') from exc
        if compiled != executed:
            raise SchemaValidationError(
                'EXECUTING_SOURCE_MISMATCH',
                f'executing code differs from captured source: {relative_path}',
            )


def _validate_admitted_schema_documents(capture: _MechanicsCapture) -> None:
    draft_2020 = 'https://json-schema.org/draft/2020-12/schema'
    for path in (
        'schemas/channels_v1.schema.json',
        'schemas/gates_v1.schema.json',
        'schemas/magic10_mechanics_v1.schema.json',
        'schemas/magic10_result_v1.schema.json',
        'schemas/magic10_compat_result_v1.schema.json',
    ):
        _validate_release_schema_document(
            capture,
            path,
            expected_draft=draft_2020,
            expected_identity=path,
        )
    _validate_release_schema_document(
        capture,
        'schemas/reader.v1.schema.json',
        expected_draft=draft_2020,
        expected_identity='https://example.org/schemas/reader.v1.schema.json',
    )
    _validate_release_schema_document(
        capture,
        'adapter/schemas/error_v1.schema.json',
        expected_draft='http://json-schema.org/draft-07/schema#',
        expected_identity=None,
    )


def _deep_freeze(value: object) -> object:
    if isinstance(value, Mapping):
        return MappingProxyType({key: _deep_freeze(item) for key, item in value.items()})
    if isinstance(value, (list, tuple)):
        return tuple(_deep_freeze(item) for item in value)
    return value


def _freeze_manifest(manifest: Manifest) -> Manifest:
    return Manifest(
        root=manifest.root,
        version=manifest.version,
        built_at_utc=manifest.built_at_utc,
        files=tuple(ManifestEntry(row.path, row.sha256, row.size) for row in manifest.files),
    )


def _freeze_registry(registry: RegistryConfig, manifest: Manifest) -> RegistryConfig:
    gates = {key: Gate(value.gate, value.center) for key, value in registry.gates.items()}
    channels = {
        key: Channel(
            value.id, tuple(value.gates), tuple(value.centers),
            value.circuit_primary, value.substream, value.primary_domain,
            tuple(value.domains), tuple(value.flags),
        )
        for key, value in registry.channels.items()
    }
    caps = {
        key: Magic10Caps(tuple(value.inputs), MappingProxyType(dict(value.bounds)))
        for key, value in registry.magic10_caps.items()
    }
    seeds = {
        key: Magic10Seed(
            value.template_id, value.seed_version, value.updated_at_utc,
            value.checksum_sha256,
        )
        for key, value in registry.magic10_seeds.items()
    }
    return RegistryConfig(
        gates=MappingProxyType(gates),
        channels=MappingProxyType(channels),
        alias_map=MappingProxyType(dict(registry.alias_map)),
        magic10_order=tuple(registry.magic10_order),
        magic10_caps=MappingProxyType(caps),
        magic10_seeds=MappingProxyType(seeds),
        manifest=manifest,
        centers=tuple(registry.centers),
        domains=tuple(registry.domains),
    )


def _load_active_mechanics_bundle_from_root(root: Path) -> AdmittedMechanicsBundle:
    """Private fixture seam; public admission fixes the verified execution root.

    Isolated fixtures may copy the identical implementation to a different
    directory. They still undergo the complete executable-equivalence check.
    """
    _, executions = _admission_execution_provenance()
    capture = _MechanicsCapture(Path(root))
    manifest_source = capture.read('catalog/manifest.json')
    manifest = _parse_manifest(manifest_source.data)
    _validate_admitted_manifest(manifest)
    source_identities = _capture_admitted_members(capture, manifest)
    _validate_executing_admission_sources(capture, executions)

    gates, centers = _load_gates(capture)
    channels, aliases, domains = _load_channels(
        capture,
        gate_map=gates,
        known_centers=set(centers),
        allow_aliases=False,
        alias_ledger=None,
    )
    order, caps, seeds = _load_magic10(capture)
    registry = RegistryConfig(
        gates, channels, aliases, order, caps, seeds, manifest, centers, domains
    )
    capture.registry = registry

    mechanics_source = capture.read('catalog/magic10_mechanics_v1.json')
    mechanics = mechanics_source.data
    _validate_initial_mechanics(capture, mechanics, registry)
    capture.config = mechanics
    _validate_admitted_schema_documents(capture)

    frozen_manifest = _freeze_manifest(manifest)
    frozen_registry = _freeze_registry(registry, frozen_manifest)
    frozen_mechanics = _deep_freeze(mechanics)
    if not isinstance(frozen_mechanics, Mapping):  # guarded by mechanics schema
        raise SchemaValidationError('INVALID_MECHANICS', 'mechanics config must be an object')
    manifest_sha256 = manifest_source.sha256
    capture.verify_unchanged(
        identity_only=frozenset({'catalog/manifest.json'}),
    )
    return AdmittedMechanicsBundle(
        registry=frozen_registry,
        mechanics=frozen_mechanics,
        manifest=frozen_manifest,
        config_sha256=mechanics_source.sha256,
        source_identities=source_identities,
        manifest_sha256=manifest_sha256,
        release_id=manifest_sha256,
    )


def load_active_mechanics_bundle() -> AdmittedMechanicsBundle:
    """Admit the exact installed complete mechanics release, or fail closed."""
    # Derive the lexical root from retained actual execution provenance and
    # corroborate all four live origins. Patching __file__ cannot select a root.
    repository_root, _ = _admission_execution_provenance()
    return _load_active_mechanics_bundle_from_root(repository_root)


def _validate_result_fixture(capture: _MechanicsCapture, data: object) -> None:
    """Validate a complete interface fixture, without executing the PR03 kernel."""
    if (not isinstance(data, dict) or not isinstance(data.get('schema'), str)
            or data['schema'] not in {'magic10_result.v1', 'magic10_compat_result.v1'}):
        raise SchemaValidationError('RESULT_SCHEMA_IDENTITY_MISMATCH', 'unknown result identity')
    internal = data['schema'] == 'magic10_compat_result.v1'
    path = 'schemas/magic10_compat_result_v1.schema.json' if internal else 'schemas/magic10_result_v1.schema.json'
    _validate_local_schema(capture, path, data)
    if data['config_id'] != capture.config['config_id']:
        raise SchemaValidationError('RESULT_CONFIG_ID_MISMATCH', 'result config identity differs from the owning config')
    signal_order = [signal for category in capture.registry.magic10_order for signal in capture.registry.magic10_caps[category].inputs]
    if [row['signal_id'] for row in data['signals']] != signal_order:
        raise SchemaValidationError('RESULT_SIGNAL_ORDER_MISMATCH', 'result signal roster/order mismatch')
    if [row['category_id'] for row in data['categories']] != list(capture.registry.magic10_order):
        raise SchemaValidationError('RESULT_CATEGORY_ORDER_MISMATCH', 'result category roster/order mismatch')


def _validate_result_augmentation(capture: _MechanicsCapture, pure: object, internal: object) -> None:
    """Assert the PR04 augmentation promise on fixtures; does not produce a result."""
    _validate_result_fixture(capture, pure)
    _validate_result_fixture(capture, internal)
    if pure['schema'] != 'magic10_result.v1' or internal['schema'] != 'magic10_compat_result.v1':
        raise SchemaValidationError('RESULT_AUGMENTATION_SHAPE_MISMATCH', 'augmentation needs pure then internal fixtures')
    for key in ('config_id', 'release_id', 'pair_key', 'signals'):
        if pure[key] != internal[key]:
            raise SchemaValidationError('RESULT_AUGMENTATION_MISMATCH', f'augmentation changed {key}')
    stripped = [{key: row[key] for key in ('category_id', 'score', 'band')} for row in internal['categories']]
    if stripped != pure['categories']:
        raise SchemaValidationError('RESULT_AUGMENTATION_MISMATCH', 'augmentation changed category values/bands/order')
