from __future__ import annotations

import hashlib
import json
import stat
import sys
from contextlib import nullcontext
from dataclasses import dataclass
import os
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence

from engine.config.magic10_v2_loader import _validate_v2_instance
from engine.config.registry_loader import (
    RegistryConfig, RegistryConfigError, SchemaValidationError,
    _capture_registry_config, _load_active_mechanics_bundle_from_root, _validate_thresholds,
)
from engine.serializer import canon

ROOT = Path(__file__).resolve().parents[2]
BAND_SOURCE = ROOT / "math" / "thresholds.json"
ARTIFACTS_ROOT = ROOT / "artifacts"
THRESHOLDS_ROOT = ARTIFACTS_ROOT / "thresholds"
MAGIC10_CONFIG_PATH = THRESHOLDS_ROOT / "magic10_config.json"
BAND_EDGES_PATH = THRESHOLDS_ROOT / "band_edges.json"

_REQUIRED_RAILS = {
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
    "SAFE_MODE": "1",
    "ALLOW_NETWORK": "0",
}


def require_closed_rails(env: Mapping[str, str] | None = None) -> None:
    env_map = dict(os.environ if env is None else env)
    missing = {key: value for key, value in _REQUIRED_RAILS.items() if env_map.get(key) != value}
    if missing:
        raise SystemExit(f"RAILS_CLOSED_REQUIRED:{sorted(missing.items())}")


def build_magic10_config(config: RegistryConfig) -> Mapping[str, object]:
    caps = {
        key: {
            "inputs": list(value.inputs),
            "bounds": {"min": value.bounds["min"], "max": value.bounds["max"]},
        }
        for key, value in sorted(config.magic10_caps.items())
    }
    seeds = {
        key: {
            "template_id": value.template_id,
            "seed_version": value.seed_version,
            "updated_at_utc": value.updated_at_utc,
            "checksum_sha256": value.checksum_sha256,
        }
        for key, value in sorted(config.magic10_seeds.items())
    }
    return {
        "schema": "magic10_config.v1",
        "order": list(config.magic10_order),
        "caps": caps,
        "seeds": seeds,
    }


def build_band_edges(root: Path | None = None, *, _capture=None) -> Mapping[str, object]:
    """Build the lower-level projection from exact selected-root thresholds."""
    capture = _capture or _capture_registry_config(root or ROOT)
    raw = capture.read("math/thresholds.json").data
    if isinstance(raw, dict) and raw.get("version") == "2":
        payload = _band_edges_v2(capture, raw)
        if _capture is None:
            capture.verify_unchanged()
        return payload
    _validate_thresholds(raw)
    payload = {
        "schema": "band_edges.v1",
        "source": "math/thresholds.json",
        "bands": ["Cool", "Open", "Warm", "Glow"],
        "edges": list(raw["edges"]),
        "clamp": list(raw["clamp"]),
        "rounding": raw["rounding"],
        "version": raw["version"],
    }
    if _capture is None:
        capture.verify_unchanged()
    return payload


# HDE-EPIC043 WU-PR-04 (HDE-DIST008.1; HDE Schemas and Artifacts §8.14.2): the
# version-2 band-edges shape. Version-2 thresholds carry one set of inclusive
# maxima per category; they are validated against their owning schema by the
# v2 loader's validator through the same capture, and each set must be strictly
# ascending. Any document that is not version 2 keeps the v1 path above, whose
# bytes are unchanged. Refusals never echo a maxima value.
BAND_EDGES_V2_SCHEMA = "band_edges.v2"


def _band_edges_v2(capture, raw: Mapping[str, object]) -> Mapping[str, object]:
    """Per-category inclusive maxima from version-2 thresholds, in catalog order."""
    _validate_v2_instance(capture, "math/thresholds.json", raw)
    by_category = {}
    for entry in raw["categories"]:
        maxima = entry["maxima"]
        if any(earlier >= later for earlier, later in zip(maxima, maxima[1:])):
            raise SchemaValidationError(
                "M10V2_MAXIMA_NOT_ASCENDING", "category maxima must be strictly ascending",
                {"category": entry["category_id"]},
            )
        by_category[entry["category_id"]] = list(maxima)
    return {
        "bands": ["Cool", "Open", "Warm", "Glow"],
        "categories": [
            {"category_id": category, "maxima": by_category[category]}
            for category in capture.config.magic10_order
        ],
        "schema": BAND_EDGES_V2_SCHEMA,
        "source": "math/thresholds.json",
        "version": "2",
    }


def _destination_state(root: Path, paths) -> dict[Path, object]:
    """Check lexical containment and capture exact destination preimages, read-only."""
    root = Path(os.path.abspath(root))
    states = {}
    for path in paths:
        path = Path(os.path.abspath(path))
        if not path.is_relative_to(root) or path == root:
            raise RuntimeError(f"CONFIG_OUTPUT_ESCAPES_ROOT:{path}")
        for parent in (path, *path.parents):
            if parent.is_symlink():
                raise RuntimeError(f"CONFIG_OUTPUT_SYMLINK:{parent}")
            if parent != path and parent.exists() and not parent.is_dir():
                raise RuntimeError(f"CONFIG_OUTPUT_PARENT_NOT_DIRECTORY:{parent}")
        if not path.exists():
            states[path] = None
        else:
            meta = path.lstat()
            if not stat.S_ISREG(meta.st_mode):
                raise RuntimeError(f"CONFIG_OUTPUT_NOT_REGULAR:{path}")
            def identity(info):
                return (info.st_dev, info.st_ino, info.st_mode, info.st_size,
                        info.st_mtime_ns, info.st_ctime_ns)
            descriptor = os.open(path, os.O_RDONLY | os.O_NOFOLLOW)
            with os.fdopen(descriptor, "rb") as handle:
                opened = os.fstat(handle.fileno())
                raw = handle.read()
                finished = os.fstat(handle.fileno())
            if not (identity(meta) == identity(opened) == identity(finished) == identity(path.lstat())):
                raise RuntimeError(f"CONFIG_DESTINATION_CHANGED_DURING_CAPTURE:{path}")
            states[path] = (raw, *identity(meta))
    return states


def _publish_prepared(root: Path, payloads: Mapping[Path, bytes], *,
                      before: Mapping[Path, object], verify: Callable[[], None]) -> None:
    """Replace a prepared family with caught-failure restoration through its owner.

    This provides no crash-atomic or multi-file visibility guarantee. The outer
    configuration/evidence coordinator may supply the same active transaction.
    """
    from tools.evidence import update_evidence_index as updater

    root = Path(os.path.abspath(root))
    if set(before) != set(payloads):
        raise RuntimeError("CONFIG_DESTINATION_ROSTER_CHANGED")
    verify()
    if _destination_state(root, payloads) != dict(before):
        raise RuntimeError("CONFIG_DESTINATION_CHANGED_DURING_PREPARATION")
    active = updater._ACTIVE_WRITE_TRANSACTION
    if active is not None and active.root != root:
        raise RuntimeError("CONFIG_TRANSACTION_ROOT_MISMATCH")
    if active is not None:
        if not isinstance(active, updater._ConfigWriteTransaction):
            raise RuntimeError("CONFIG_TRANSACTION_OWNER_MISMATCH")
        active.assert_unchanged(payloads)
    context = nullcontext(active) if active is not None else updater._ConfigWriteTransaction(
        root, allowed_paths=set(payloads)
    )
    with context as transaction:
        transaction.prepare(payloads)
        verify()
        if _destination_state(root, payloads) != dict(before):
            raise RuntimeError("CONFIG_DESTINATION_CHANGED_BEFORE_PUBLICATION")
        for path, content in payloads.items():
            verify()
            if _destination_state(root, [path])[path] != before[path]:
                raise RuntimeError(f"CONFIG_DESTINATION_CHANGED_BEFORE_REPLACEMENT:{path}")
            updater._publish_staged({path: content})
        verify()
        for path, expected in payloads.items():
            _destination_state(root, [path])
            if path.read_bytes() != expected:
                raise RuntimeError(f"CONFIG_OUTPUT_CHANGED:{path}")


def write_magic10_config(config: RegistryConfig, root: Path | None = None) -> Path:
    require_closed_rails()
    base = Path(os.path.abspath(root or ROOT))
    target = base / "artifacts/thresholds/magic10_config.json"
    before = _destination_state(base, [target])
    capture = _capture_registry_config(base, allow_aliases=bool(config.alias_map),
                                        alias_ledger=config.alias_map or None)
    if capture.config != config:
        raise RuntimeError("CONFIG_WRITER_SOURCE_MISMATCH")
    payload = canon.sercanon(build_magic10_config(capture.config), sort_keys=True)
    _publish_prepared(base, {target: payload}, before=before, verify=capture.verify_unchanged)
    return target


def write_band_edges(root: Path | None = None) -> Path:
    require_closed_rails()
    base = Path(os.path.abspath(root or ROOT))
    target = base / "artifacts/thresholds/band_edges.json"
    before = _destination_state(base, [target])
    capture = _capture_registry_config(base)
    payload = canon.sercanon(build_band_edges(base, _capture=capture), sort_keys=True)
    _publish_prepared(base, {target: payload}, before=before, verify=capture.verify_unchanged)
    return target


# ---------------------------------------------------------------------------
# HDE-EPIC040-PR05: read-only Magic-10 golden comparison (PF01 §9.5; PF12
# §8.14.1; Plan §5.9/§6.5).  The comparator orchestrates the canonical kernel
# and application entrypoints and implements no formula.  It is structurally
# unable to reach the write, activation or generation helpers above: nothing
# below references ``write_magic10_config``, ``write_band_edges``,
# ``_publish_prepared`` or the evidence updater, and the owning tests pin that
# with an AST guard and runtime spies.  A fixture candidate's admission is
# test-only evidence and never release admission.
# ---------------------------------------------------------------------------

# HDE-EPIC043 WU-PR-09: the golden comparison reads the Magic10 v2 golden
# collection (PF01 §9.5 v2).  HDE-EPIC043 WU-PR-10 (HDE-DIST008.1; D-5, D-6): the
# collection holds M10-G001 to M10-G008, computed at the cut, and each case kind
# has its runner below.
GOLDENS_SCHEMA = "magic10_goldens.v2"
GOLDEN_COMPARISON_SCHEMA = "magic10_golden_comparison.v1"
GOLDENS_DEFAULT_PATH = ROOT / "tests/fixtures/magic10/v2/goldens.json"
# A document must be canonical and closed, so 1 MiB leaves ample room while an
# oversized input is refused after reading at most one byte past the bound.
GOLDENS_MAX_BYTES = 1_048_576
# PF01 §9.5 v2: the canon set is "M10-G001 to M10-G008".  The collection must carry
# exactly these cases in this order, each with its case type and kind: an extra,
# missing, reordered or renamed case refuses GOLDENS_MEMBERSHIP_INVALID, and a listed
# case with another type or kind refuses GOLDENS_CASE_TYPE_INVALID.
GOLDEN_CASE_TABLE = (
    ("M10-G001", "calculation", "category_vector"),
    ("M10-G002", "calculation", "core"),
    ("M10-G003", "calculation", "signal_operation"),
    ("M10-G004", "calculation", "core"),
    ("M10-G005", "application", "identity_independence"),
    ("M10-G006", "calculation", "band_boundary"),
    ("M10-G007", "application", "self_pair"),
    ("M10-G008", "application", "equal_mask_pair"),
)
GOLDEN_CASE_IDS = tuple(row[0] for row in GOLDEN_CASE_TABLE)
_GOLDEN_CASE_OWNERSHIP = {row[0]: (row[1], row[2]) for row in GOLDEN_CASE_TABLE}
_GOLDEN_TOP_KEYS = frozenset({"cases", "constants", "schema", "source"})
_GOLDEN_SOURCE_KEYS = frozenset({"document", "section", "sha256", "version"})
# The constants grow only by the two values the application runners consume: the
# PF01 §9.5 router stub and the synthetic projection fields every party carries.
_GOLDEN_CONSTANT_KEYS = frozenset({"config_id", "release_id", "router_stub", "synthetic_projection_fields"})
_GOLDEN_ROUTER_STUB_KEYS = frozenset({"personal_hi_to_lo", "personal_lo_to_hi", "shared"})
_GOLDEN_CASE_KEYS = frozenset({
    "case_id", "case_type", "expected", "input_provenance", "inputs", "kind",
    "realizable_chart_claim", "title",
})
_GOLDEN_CASE_OPTIONAL_KEYS = frozenset({"notes"})
# The closed set of case kinds, each with its case type and input keys; any other
# kind is refused (GOLDENS_INVALID) before a candidate is admitted.
_GOLDEN_KINDS = {
    "category_vector": ("calculation", frozenset({"gates_a", "gates_b"})),
    "core": ("calculation", frozenset({"gates_a", "gates_b"})),
    "signal_operation": ("calculation", frozenset({"channels", "operation", "scenarios", "signal_id", "state"})),
    "band_boundary": ("calculation", frozenset({"categories"})),
    "identity_independence": ("application", frozenset({"pairs"})),
    "self_pair": ("application", frozenset({"a", "adverse", "b", "meta", "release_id"})),
    "equal_mask_pair": ("application", frozenset({"a", "b", "meta", "release_id"})),
}
_GOLDEN_ABSENT = "<absent>"
_GOLDEN_OWNER_SWAP = {"member_lo": "member_hi", "member_hi": "member_lo"}
# The two owned Channel states (HDE Math Spec §5.2.11, bilateral_owner_mass_v2).
_GOLDEN_OWNED_STATES = ("compromise", "dominance")
# A signal_operation scenario replaces only a real kernel result's Channel states;
# compute_signals reads nothing else, so this fixed pair only supplies that result.
_GOLDEN_SIGNAL_BASE_GATES = ((1,), (2,))
# Nested input objects are closed like the rest of the collection: an unknown or
# missing key is that case's mismatch, never silently ignored.
_GOLDEN_WEIGHTED_CHANNEL_KEYS = frozenset({"channel_id", "weight"})
_GOLDEN_SCENARIO_KEYS = frozenset({"owned", "scenario_id"})
_GOLDEN_OWNED_ROW_KEYS = frozenset({"channel_id", "owner"})
_GOLDEN_BOUNDARY_ROW_KEYS = frozenset({"category_id", "scores"})
_GOLDEN_PARTY_KEYS = frozenset({"gates", "person_uid"})
_GOLDEN_PAIR_KEYS = frozenset({"a", "b", "pair_id"})
_GOLDEN_ADVERSE_KEYS = frozenset({"adverse_id", "field", "party", "value"})
_GOLDEN_META_KEYS = frozenset({"engine_tag", "invocation_tag"})


class GoldenComparisonRefusal(RuntimeError):
    """A value-free refusal: the comparison did not run to a verdict."""

    def __init__(self, code: str) -> None:
        super().__init__(code)
        self.code = code


class _GoldenCaseMismatch(Exception):
    """One case cannot be executed against this candidate as the fixture states it."""

    def __init__(self, path: str, expected: object, actual: object) -> None:
        super().__init__(path)
        self.path, self.expected, self.actual = path, expected, actual


@dataclass(frozen=True)
class Mismatch:
    case_id: str
    path: str
    expected: object
    actual: object


@dataclass(frozen=True)
class CaseOutcome:
    case_id: str
    case_type: str
    kind: str
    outcome: str
    expected: Mapping[str, Any]
    observed: Mapping[str, Any]


@dataclass(frozen=True)
class GoldenComparison:
    candidate_root: str  # display only: ".", repository-relative or "<external>"
    goldens_path: str  # display only, as candidate_root
    goldens_sha256: str
    candidate_release_id: str
    config_id: str
    cases: tuple[CaseOutcome, ...]
    mismatches: tuple[Mismatch, ...]
    ok: bool
    schema: str = GOLDEN_COMPARISON_SCHEMA


def _golden_refuse(code: str) -> GoldenComparisonRefusal:
    return GoldenComparisonRefusal(code)


def _golden_pairs_hook(pairs):
    keys = [key for key, _ in pairs]
    if len(keys) != len(set(keys)):
        raise ValueError("duplicate object key")
    return dict(pairs)


def _golden_refuse_non_integer(token: str) -> object:
    # Canonical JSON (PF12 §4.1) carries integers only: NaN, ±Infinity and every
    # fraction or exponent are refused before they could reach a report.
    raise ValueError(f"non-integer JSON number: {token}")


def _golden_is_str(value: object) -> bool:
    return type(value) is str and bool(value)


def _golden_display(path: Path) -> str:
    """A report never carries a host path: the repository root is ".", a path
    inside it is repository-relative, and any other path is "<external>"."""
    resolved, root = Path(os.path.realpath(path)), Path(os.path.realpath(ROOT))
    if resolved == root:
        return "."
    return resolved.relative_to(root).as_posix() if resolved.is_relative_to(root) else "<external>"


def _golden_read_bounded(path: Path) -> bytes:
    """Return the bytes of a regular, non-symlinked goldens file within the bound.

    The file is opened without following a final symlink and without blocking,
    and its type is checked on the opened descriptor, so a FIFO, device, directory
    or symlink is refused before anything is read, and at most one byte past
    ``GOLDENS_MAX_BYTES`` is ever read. The descriptor is closed on every path.
    """
    try:
        descriptor = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    except OSError:
        raise _golden_refuse("GOLDENS_INVALID") from None
    try:
        if not stat.S_ISREG(os.fstat(descriptor).st_mode):
            raise _golden_refuse("GOLDENS_INVALID")
        with os.fdopen(descriptor, "rb", closefd=False) as handle:
            raw = handle.read(GOLDENS_MAX_BYTES + 1)
    except OSError:
        raise _golden_refuse("GOLDENS_INVALID") from None
    finally:
        os.close(descriptor)
    if len(raw) > GOLDENS_MAX_BYTES:
        raise _golden_refuse("GOLDENS_INVALID")
    return raw


def _golden_load_document(goldens_path: Path) -> tuple[Mapping[str, Any], str]:
    raw = _golden_read_bounded(Path(os.path.abspath(goldens_path)))
    try:
        document = json.loads(raw.decode("utf-8"), object_pairs_hook=_golden_pairs_hook,
                              parse_constant=_golden_refuse_non_integer, parse_float=_golden_refuse_non_integer)
        canonical = isinstance(document, dict) and canon.sercanon(document, sort_keys=True) == raw
    except (UnicodeDecodeError, ValueError, RecursionError):
        raise _golden_refuse("GOLDENS_INVALID") from None
    if not canonical:
        raise _golden_refuse("GOLDENS_INVALID")
    _golden_validate_document(document)
    return document, hashlib.sha256(raw).hexdigest()


def _golden_constants_valid(constants: object) -> bool:
    """The closed ``constants``: two identities, the router stub and the projection fields."""
    if not isinstance(constants, dict) or set(constants) != _GOLDEN_CONSTANT_KEYS:
        return False
    stub, fields = constants["router_stub"], constants["synthetic_projection_fields"]
    return (_golden_is_str(constants["config_id"]) and _golden_is_str(constants["release_id"])
            and isinstance(stub, dict) and set(stub) == _GOLDEN_ROUTER_STUB_KEYS
            and all(_golden_is_str(value) for value in stub.values())
            # A party's Gates come from its case input, so the fields may not carry any.
            and isinstance(fields, dict) and bool(fields) and "gates" not in fields)


def _golden_validate_document(document: Mapping[str, Any]) -> None:
    if set(document) != _GOLDEN_TOP_KEYS or document["schema"] != GOLDENS_SCHEMA:
        raise _golden_refuse("GOLDENS_INVALID")
    source, constants, cases = document["source"], document["constants"], document["cases"]
    if (not isinstance(source, dict) or set(source) != _GOLDEN_SOURCE_KEYS
            or not all(_golden_is_str(value) for value in source.values())):
        raise _golden_refuse("GOLDENS_INVALID")
    if not _golden_constants_valid(constants):
        raise _golden_refuse("GOLDENS_INVALID")
    if (not isinstance(cases, list)
            or not all(isinstance(case, dict) and _golden_is_str(case.get("case_id")) for case in cases)):
        raise _golden_refuse("GOLDENS_INVALID")
    if tuple(case["case_id"] for case in cases) != GOLDEN_CASE_IDS:
        raise _golden_refuse("GOLDENS_MEMBERSHIP_INVALID")
    for case in cases:
        keys = set(case)
        if not (_GOLDEN_CASE_KEYS <= keys <= (_GOLDEN_CASE_KEYS | _GOLDEN_CASE_OPTIONAL_KEYS)):
            raise _golden_refuse("GOLDENS_INVALID")
        if not _golden_is_str(case["kind"]) or case["kind"] not in _GOLDEN_KINDS:
            raise _golden_refuse("GOLDENS_INVALID")
        input_keys = _GOLDEN_KINDS[case["kind"]][1]
        if (case["case_type"], case["kind"]) != _GOLDEN_CASE_OWNERSHIP[case["case_id"]]:
            raise _golden_refuse("GOLDENS_CASE_TYPE_INVALID")
        provenance = case["input_provenance"]
        if (not _golden_is_str(case["title"])
                or type(case["realizable_chart_claim"]) not in (bool, type(None))
                or not isinstance(provenance, list) or not provenance
                or not all(_golden_is_str(tag) for tag in provenance)
                or len(set(provenance)) != len(provenance)
                or not isinstance(case["inputs"], dict) or not isinstance(case["expected"], dict)
                or not case["expected"]
                or ("notes" in case and not (isinstance(case["notes"], list)
                                              and all(_golden_is_str(note) for note in case["notes"])))):
            raise _golden_refuse("GOLDENS_INVALID")
        if set(case["inputs"]) != input_keys:
            raise _golden_refuse("GOLDENS_INVALID")


def _golden_closed(value: object, keys: frozenset[str], path: str) -> Mapping[str, Any]:
    if not isinstance(value, dict) or set(value) != keys:
        actual = sorted(value) if isinstance(value, dict) else type(value).__name__
        raise _GoldenCaseMismatch(path, sorted(keys), actual)
    return value


def _golden_admit(candidate_root: Path):
    root = Path(os.path.abspath(candidate_root))
    try:
        if root.is_symlink() or not root.is_dir():
            raise _golden_refuse("CANDIDATE_ROOT_INVALID")
    except OSError:
        raise _golden_refuse("CANDIDATE_ROOT_INVALID") from None
    try:
        bundle = _load_active_mechanics_bundle_from_root(root)
    except RegistryConfigError as exc:
        raise _golden_refuse(f"CANDIDATE_ADMISSION_REFUSED:{exc.code}") from None
    return root, bundle


def golden_executed_member_modules(bundle) -> Mapping[str, str]:
    """Every executable member of the admitted candidate, keyed by its module name.

    HDE-EPIC040-PR06 (O-17 / CR-06); since HDE-EPIC043 WU-PR-09 derived from the
    candidate manifest's ``.py`` rows at comparison time, not from the
    import-time roster constant, so it follows the admitted candidate.
    """
    return {
        row.path: row.path[: -len(".py")].replace("/", ".")
        for row in bundle.manifest.files
        if row.path.endswith(".py")
    }


def _golden_bind_executed_members(bundle) -> None:
    """Refuse when an executing roster module's source differs from the candidate.

    Admission binds executing code to the candidate's bytes only for its
    covered mechanics modules; the golden runners also execute other roster
    members from the executing installation.  For every such member that is
    already imported, the installation's source file must be a readable
    regular ``.py`` file and its bytes must equal the candidate's
    manifest-bound identity for that path.  Read-only by construction:
    nothing is imported, reloaded, compiled or compared as code objects, and
    a module that is not loaded is not executed by the goldens and is not
    bound.  Executable equivalence for these members remains unproven.
    """
    identities = {identity.path: identity for identity in bundle.source_identities}
    for path, module_name in golden_executed_member_modules(bundle).items():
        module = sys.modules.get(module_name)
        if module is None:
            continue
        origin = getattr(module, "__file__", None)
        try:
            if (not isinstance(origin, str) or not origin.endswith(".py") or not os.path.isabs(origin)
                    or os.path.islink(origin) or not os.path.isfile(origin)):
                raise _golden_refuse(f"CANDIDATE_EXECUTING_SOURCE_UNAVAILABLE:{path}")
            with open(origin, "rb") as handle:
                executing = handle.read()
        except OSError:
            raise _golden_refuse(f"CANDIDATE_EXECUTING_SOURCE_UNAVAILABLE:{path}") from None
        identity = identities.get(path)
        if (identity is None or len(executing) != identity.size
                or hashlib.sha256(executing).hexdigest() != identity.sha256):
            raise _golden_refuse(f"CANDIDATE_EXECUTING_SOURCE_MISMATCH:{path}")


def _golden_gates(value: object, path: str):
    """Normalize one fixture Gate list as the core's members require, or report the case."""
    from engine.bodygraph.gates import GateNormalizationError, normalize_gates

    if not isinstance(value, list):
        raise _GoldenCaseMismatch(path, "list", type(value).__name__)
    try:
        return normalize_gates(list(value))
    except GateNormalizationError as exc:
        raise _GoldenCaseMismatch(path, "normalized Gate list", exc.code) from None


def _golden_pair_order(first: object, reversed_order: object) -> None:
    """PF01 §9.5 v2: every case is checked in both pair orders.

    A result that depends on member order is the case's ``pair_order`` mismatch,
    reported before any of its values is compared.
    """
    if canon.sercanon(first) != canon.sercanon(reversed_order):
        raise _GoldenCaseMismatch("pair_order", first, reversed_order)


def _golden_run_category_vector(case, constants, bundle) -> dict[str, Any]:
    """PF01 §9.5 v2: the category vector of ``compute_core`` over the admitted candidate, in both orders."""
    from engine.core.core import compute_core

    inputs = case["inputs"]
    member_a = _golden_gates(inputs["gates_a"], "inputs.gates_a")
    member_b = _golden_gates(inputs["gates_b"], "inputs.gates_b")
    first = compute_core(member_a, member_b, bundle, bundle.release_id).as_payload()
    _golden_pair_order(first, compute_core(member_b, member_a, bundle, bundle.release_id).as_payload())
    return {"categories": [
        {"category_id": row["category_id"], "score": row["score"], "band": row["band"]} for row in first["categories"]
    ]}


def _golden_hex64(value: object) -> bool:
    return type(value) is str and len(value) == 64 and all(char in "0123456789abcdef" for char in value)


def _golden_channel_states(mask_a: int, mask_b: int, bundle) -> list[dict[str, Any]]:
    """The v2 kernel's 36 Channel states with owners (HDE Math Spec §5.2.11 step 2)."""
    from engine.magic10_v2.kernel import compute_kernel

    return [{"channel_id": row.channel_id, "state": row.state, "owner": row.owner}
            for row in compute_kernel(mask_a, mask_b, bundle.magic10_v2).channels]


def _golden_run_core(case, constants, bundle) -> dict[str, Any]:
    """PF01 §9.5 v2: the complete ``compute_core`` result and Channel states, AB, AB again and BA."""
    from engine.core.core import compute_core

    inputs = case["inputs"]
    member_a = _golden_gates(inputs["gates_a"], "inputs.gates_a")
    member_b = _golden_gates(inputs["gates_b"], "inputs.gates_b")
    first = compute_core(member_a, member_b, bundle, bundle.release_id).as_payload()
    second = compute_core(member_a, member_b, bundle, bundle.release_id).as_payload()
    reversed_order = compute_core(member_b, member_a, bundle, bundle.release_id).as_payload()
    states = _golden_channel_states(member_a.mask, member_b.mask, bundle)
    _golden_pair_order({"channel_states": states, "result": first},
                       {"channel_states": _golden_channel_states(member_b.mask, member_a.mask, bundle),
                        "result": reversed_order})
    return {
        "channel_states": states,
        "signals": first["signals"],
        "categories": first["categories"],
        "ab_ba_identity": canon.sercanon(first) == canon.sercanon(reversed_order),
        "two_run_identity": canon.sercanon(first) == canon.sercanon(second),
        "identities": {
            "schema": first["schema"],
            "config_id_matches_candidate": first["config_id"] == bundle.mechanics["config_id"],
            "release_id_matches_candidate": first["release_id"] == bundle.release_id,
            "pair_key_hex64": _golden_hex64(first["pair_key"]),
        },
    }


def _golden_owner_mass_q(base, owners: Mapping[str, str], state: str, signal_id: str, bundle) -> int:
    """One signal of a real kernel result whose Channel states are exactly the stated ones."""
    import dataclasses

    from engine.magic10_v2.kernel import ChannelState
    from engine.magic10_v2.signals import compute_signals

    rows = tuple(ChannelState(row.channel_id, state, owners[row.channel_id]) if row.channel_id in owners
                 else ChannelState(row.channel_id, "none", None) for row in base.channels)
    values = compute_signals(dataclasses.replace(base, channels=rows), bundle.magic10_v2)
    return next(value.q for value in values if value.signal_id == signal_id)


def _golden_run_signal_operation(case, constants, bundle) -> dict[str, Any]:
    """PF01 §9.5 v2 (M10-G003): one signal over stated owned Channels, and with the owners swapped.

    The stated roster and operation must be the candidate's.  Each scenario's owned
    Channels carry the stated owned state and owner; every other Channel is ``none``.
    """
    from engine.bodygraph.gates import normalize_gates
    from engine.magic10_v2.kernel import compute_kernel

    inputs = case["inputs"]
    rows = bundle.magic10_v2.configuration["signals"]
    definition = next((row for row in rows if row["signal_id"] == inputs["signal_id"]), None)
    if definition is None:
        raise _GoldenCaseMismatch("inputs.signal_id", [row["signal_id"] for row in rows], inputs["signal_id"])
    candidate = {
        "operation": definition["operation"],
        "channels": [{"channel_id": member["channel_id"], "weight": member["weight"]} for member in definition["channels"]],
    }
    if not isinstance(inputs["channels"], list):
        raise _GoldenCaseMismatch("inputs.channels", "list", type(inputs["channels"]).__name__)
    for index, member in enumerate(inputs["channels"]):
        _golden_closed(member, _GOLDEN_WEIGHTED_CHANNEL_KEYS, f"inputs.channels[{index}]")
    stated = {"operation": inputs["operation"], "channels": inputs["channels"]}
    if canon.sercanon(stated) != canon.sercanon(candidate):
        raise _GoldenCaseMismatch("inputs.definition", stated, candidate)
    if inputs["state"] not in _GOLDEN_OWNED_STATES:
        raise _GoldenCaseMismatch("inputs.state", list(_GOLDEN_OWNED_STATES), inputs["state"])
    roster = [member["channel_id"] for member in candidate["channels"]]
    scenarios_in = inputs["scenarios"]
    if not isinstance(scenarios_in, list) or not scenarios_in:
        raise _GoldenCaseMismatch("inputs.scenarios", "non-empty list", scenarios_in)
    base = compute_kernel(*(normalize_gates(list(gates)).mask for gates in _GOLDEN_SIGNAL_BASE_GATES), bundle.magic10_v2)
    scenarios = []
    for index, scenario in enumerate(scenarios_in):
        path = f"inputs.scenarios[{index}]"
        _golden_closed(scenario, _GOLDEN_SCENARIO_KEYS, path)
        owned = scenario["owned"]
        if not isinstance(owned, list) or not owned:
            raise _GoldenCaseMismatch(f"{path}.owned", "non-empty list", owned)
        owners: dict[str, str] = {}
        for row_index, row in enumerate(owned):
            row_path = f"{path}.owned[{row_index}]"
            _golden_closed(row, _GOLDEN_OWNED_ROW_KEYS, row_path)
            if type(row["channel_id"]) is not str or row["channel_id"] not in roster or row["channel_id"] in owners:
                raise _GoldenCaseMismatch(f"{row_path}.channel_id", "a distinct roster Channel", row["channel_id"])
            if type(row["owner"]) is not str or row["owner"] not in _GOLDEN_OWNER_SWAP:
                raise _GoldenCaseMismatch(f"{row_path}.owner", sorted(_GOLDEN_OWNER_SWAP), row["owner"])
            owners[row["channel_id"]] = row["owner"]
        swapped = {channel: _GOLDEN_OWNER_SWAP[owner] for channel, owner in owners.items()}
        scenarios.append({
            "scenario_id": scenario["scenario_id"],
            "q": _golden_owner_mass_q(base, owners, inputs["state"], inputs["signal_id"], bundle),
            "q_owners_swapped": _golden_owner_mass_q(base, swapped, inputs["state"], inputs["signal_id"], bundle),
        })
    return {"definition": candidate, "scenarios": scenarios}


def _golden_run_band_boundary(case, constants, bundle) -> dict[str, Any]:
    """PF01 §§5.3.7, 9.5 v2 (M10-G006): stated scores banded by each category's own maxima.

    Scores are injected at ``assign_band``; no member order exists at this layer.
    """
    from engine.magic10_v2.calculation import assign_band

    rows = case["inputs"]["categories"]
    if not isinstance(rows, list):
        raise _GoldenCaseMismatch("inputs.categories", "list", type(rows).__name__)
    for index, row in enumerate(rows):
        _golden_closed(row, _GOLDEN_BOUNDARY_ROW_KEYS, f"inputs.categories[{index}]")
    order = list(bundle.registry.magic10_order)
    stated = [row["category_id"] for row in rows]
    if stated != order:
        raise _GoldenCaseMismatch("inputs.categories.category_ids", order, stated)
    maxima = bundle.magic10_v2.maxima
    categories = []
    for index, row in enumerate(rows):
        scores = row["scores"]
        if (not isinstance(scores, list) or not scores
                or not all(type(score) is int and 0 <= score <= 100 for score in scores)):
            raise _GoldenCaseMismatch(f"inputs.categories[{index}].scores", "non-empty list of integer scores 0..100", scores)
        category = row["category_id"]
        categories.append({
            "category_id": category,
            "maxima": list(maxima[category]),
            "results": [{"score": score, "band": assign_band(score, maxima[category])} for score in scores],
        })
    return {"categories": categories}


def _golden_chart(constants: Mapping[str, Any], person_uid: str, gates: Sequence[object],
                  override: Mapping[str, Any] | None = None) -> dict[str, Any]:
    fields = json.loads(json.dumps(constants["synthetic_projection_fields"]))
    if override:
        fields.update(override)
    return {
        "bodygraph": {**fields, "gates": list(gates)},
        "person": {"person_uid": person_uid},
        "person_uid": person_uid,
    }


def _golden_party(constants: Mapping[str, Any], spec: Mapping[str, Any], path: str,
                  override: Mapping[str, Any] | None = None):
    from engine.bodygraph.resolver import ResolvedCompatChart
    from engine.compat.compute import evaluation_party

    _golden_closed(spec, _GOLDEN_PARTY_KEYS, path)
    if not isinstance(spec["gates"], list):
        raise _GoldenCaseMismatch(f"{path}.gates", "list", type(spec["gates"]).__name__)
    chart = _golden_chart(constants, spec["person_uid"], spec["gates"], override)
    return evaluation_party(ResolvedCompatChart(spec["person_uid"], chart, "resolved", None, None, None, None))


def _golden_router(constants: Mapping[str, Any], bundle,
                   calls: list[tuple[object, object, object]]) -> Callable[..., Mapping[str, str]]:
    """The PF01 §9.5 router stub, held to the canonical router's contract.

    It has ``route_keys``'s signature and answers the missing key wherever that
    router does: a category outside the candidate's, a band outside the narrative
    bands, a perspective outside the narrative perspectives, and the personal key
    of the ``shared`` perspective.  Every call is recorded for the routing check.
    """
    from engine.narratives.constants import BANDS, MISSING_NARRATIVE_KEY, PERSPECTIVES

    stub = constants["router_stub"]
    categories = frozenset(bundle.registry.magic10_order)
    personal = {"a_to_b": stub["personal_lo_to_hi"], "b_to_a": stub["personal_hi_to_lo"]}

    def router(category: str, band: str, perspective: str, *, viewer_top: str | None = None,
               flags: Sequence[str] | None = None) -> dict[str, str]:
        calls.append((category, band, perspective))
        if category not in categories or band not in BANDS or perspective not in PERSPECTIVES:
            return {"personal_key": MISSING_NARRATIVE_KEY, "shared_key": MISSING_NARRATIVE_KEY}
        return {"personal_key": personal.get(perspective, MISSING_NARRATIVE_KEY), "shared_key": stub["shared"]}

    return router


def _golden_check_routing(calls: list[tuple[object, object, object]], result: Mapping[str, Any]) -> None:
    """Hold one evaluation's routing to the tuples its own result requires.

    ``evaluate_pair`` routes each category row once lo→hi (``a_to_b``) and once
    hi→lo (``b_to_a``).  The stub's constant keys cannot show a call that named
    another category, band or perspective, so the recorded calls must equal, as a
    set, the row tuples in both directions.
    """
    required = {(row["category_id"], row["band"], perspective)
                for row in result["categories"] for perspective in ("a_to_b", "b_to_a")}
    observed = set(calls)
    calls.clear()
    if observed != required:
        raise _GoldenCaseMismatch("router_calls", sorted(map(list, required), key=repr),
                                  sorted(map(list, observed), key=repr))


def _golden_meta(meta: object, path: str) -> Mapping[str, str]:
    _golden_closed(meta, _GOLDEN_META_KEYS, path)
    return meta


def _golden_reader(result: Mapping[str, Any], meta: Mapping[str, str], release_id: str):
    """The Reader v1 projection of one result: the ``harmony`` band, or ``[]`` when ineligible."""
    from engine.compat.compute import harmony_band, is_ineligible_carrier
    from presenter.reader_v1.emitter import emit_reader_v1

    if is_ineligible_carrier(result):
        categories: list[dict[str, str]] = []
    else:
        categories = [{"id": "harmony", "band": harmony_band(result)}]
    enriched = {"eligible": not is_ineligible_carrier(result), "categories": categories,
                "meta": {"engine_tag": meta["engine_tag"], "invocation_tag": meta["invocation_tag"]},
                "release_id": release_id}
    return emit_reader_v1(enriched)


def _golden_reader_v2(result: Mapping[str, Any], meta: Mapping[str, str], release_id: str):
    """The Reader v2 projection of one eligible result: the ten bands in the governed order."""
    from presenter.reader_v1.emitter import emit_reader_v2

    enriched = {"eligible": True,
                "categories": [{"id": row["category_id"], "band": row["band"]} for row in result["categories"]],
                "meta": {"engine_tag": meta["engine_tag"], "invocation_tag": meta["invocation_tag"]},
                "release_id": release_id}
    return emit_reader_v2(enriched)


def _golden_intrinsic(result: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "schema": result["schema"], "config_id": result["config_id"], "release_id": result["release_id"],
        "pair_key": result["pair_key"],
        "signals": [{"signal_id": row["signal_id"], "q": row["q"]} for row in result["signals"]],
        "categories": [{"category_id": row["category_id"], "score": row["score"], "band": row["band"]}
                       for row in result["categories"]],
    }


def _golden_run_identity_independence(case, constants, bundle) -> dict[str, Any]:
    """PF01 §9.5 (M10-G005): equal masks under other identities give the same intrinsic bytes."""
    from engine.compat.compute import evaluate_pair

    routed: list[tuple[object, object, object]] = []
    router = _golden_router(constants, bundle, routed)
    pairs = case["inputs"]["pairs"]
    if not isinstance(pairs, list) or not pairs:
        raise _GoldenCaseMismatch("inputs.pairs", "non-empty list", pairs)
    for index, pair in enumerate(pairs):
        _golden_closed(pair, _GOLDEN_PAIR_KEYS, f"inputs.pairs[{index}]")
    # Pair identifiers are positional labels; nothing else consumes them.
    labels = [f"pair_{index}" for index in range(1, len(pairs) + 1)]
    stated_labels = [pair["pair_id"] for pair in pairs]
    if stated_labels != labels:
        raise _GoldenCaseMismatch("inputs.pairs.pair_id", labels, stated_labels)
    results = []
    for index, pair in enumerate(pairs):
        party_a = _golden_party(constants, pair["a"], f"inputs.pairs[{index}].a")
        party_b = _golden_party(constants, pair["b"], f"inputs.pairs[{index}].b")
        result = evaluate_pair(party_a, party_b, bundle_provider=lambda: bundle, router=router)
        _golden_check_routing(routed, result)
        reversed_result = evaluate_pair(party_b, party_a, bundle_provider=lambda: bundle, router=router)
        _golden_check_routing(routed, reversed_result)
        _golden_pair_order(result, reversed_result)
        results.append(result)
    intrinsic = [_golden_intrinsic(result) for result in results]
    return {
        "pair_key_equal_across_pairs": len({row["pair_key"] for row in intrinsic}) == 1,
        "intrinsic_bytes_equal_across_pairs": len({canon.sercanon(row) for row in intrinsic}) == 1,
        "intrinsic": {"schema": intrinsic[0]["schema"], "signals": intrinsic[0]["signals"],
                      "categories": intrinsic[0]["categories"]},
    }


class _GoldenCacheSpy:
    """An intrinsic cache that holds nothing and records every access."""

    def __init__(self, calls: list[str]) -> None:
        self._calls = calls

    def get(self, key: str) -> None:
        self._calls.append("cache")
        return None

    def put(self, key: str, value: object) -> None:
        self._calls.append("cache")


def _golden_recording_seams(bundle, router, calls: list[str]) -> dict[str, Any]:
    """evaluate_pair's three seams, each recording every call in ``calls``."""

    def provider():
        calls.append("bundle_provider")
        return bundle

    def tracked_router(*args, **kwargs):
        calls.append("router")
        return router(*args, **kwargs)

    return {"bundle_provider": provider, "cache": _GoldenCacheSpy(calls), "router": tracked_router}


def _golden_run_self_pair(case, constants, bundle) -> dict[str, Any]:
    """PF01 §9.5 (M10-G007): a valid self-pair calls no core, cache or router and has no pair_key."""
    from engine.compat.compute import evaluate_pair
    from engine.compat.error_tokens import CompatBoundaryError

    inputs = case["inputs"]
    meta = _golden_meta(inputs["meta"], "inputs.meta")
    router = _golden_router(constants, bundle, [])
    party_a = _golden_party(constants, inputs["a"], "inputs.a")
    party_b = _golden_party(constants, inputs["b"], "inputs.b")
    # PF01 §9.5: a valid self-pair calls neither Engine Core, the intrinsic cache nor
    # the narrative router.  evaluate_pair reaches Engine Core only with the admitted
    # bundle, so the bundle provider stands for it; all three seams record any call.
    calls: list[str] = []
    seams = _golden_recording_seams(bundle, router, calls)
    result = evaluate_pair(party_a, party_b, **seams)
    reversed_result = evaluate_pair(party_b, party_a, **seams)
    _golden_pair_order(result, reversed_result)
    body, envelope = _golden_reader(result, meta, inputs["release_id"])
    body_two, _ = _golden_reader(result, meta, inputs["release_id"])
    body_ba, _ = _golden_reader(reversed_result, meta, inputs["release_id"])
    if not isinstance(inputs["adverse"], list):
        raise _GoldenCaseMismatch("inputs.adverse", "list", type(inputs["adverse"]).__name__)
    adverse = []
    for index, variant in enumerate(inputs["adverse"]):
        _golden_closed(variant, _GOLDEN_ADVERSE_KEYS, f"inputs.adverse[{index}]")
        if variant["party"] not in ("a", "b"):
            raise _GoldenCaseMismatch(f"inputs.adverse[{index}].party", ["a", "b"], variant["party"])
        override = {variant["field"]: variant["value"]}
        mutated_a = _golden_party(constants, inputs["a"], "inputs.a", override if variant["party"] == "a" else None)
        mutated_b = _golden_party(constants, inputs["b"], "inputs.b", override if variant["party"] == "b" else None)
        token = reason = None
        returned = False
        adverse_result: object = None
        adverse_calls: list[str] = []
        try:
            adverse_result = evaluate_pair(mutated_a, mutated_b, **_golden_recording_seams(bundle, router, adverse_calls))
            returned = True
        except CompatBoundaryError as exc:
            token, reason = exc.token, exc.reason
        # PF01 §9.5: the inconsistent self-pair creates no pair_key.  A pair key needs the
        # admitted bundle and keys the intrinsic cache, so reaching either seam, or
        # returning a result that carries one, is a created pair key.
        pair_key_created = ("bundle_provider" in adverse_calls or "cache" in adverse_calls
                            or (isinstance(adverse_result, Mapping) and "pair_key" in adverse_result))
        adverse.append({"adverse_id": variant["adverse_id"], "token": token, "reason": reason,
                        "pair_key_created": pair_key_created, "result_returned": returned})
    return {
        "eligible": bool(result.get("eligible")) if "eligible" in result else True,
        "evaluate_pair_result": json.loads(canon.sercanon(result).decode("utf-8")),
        "core_cache_router_called": bool(calls),
        "pair_key_present": "pair_key" in result,
        "reader": {"eligible": envelope["eligible"], "categories": envelope["categories"],
                   "idempotence_hash": envelope["idempotence_hash"]},
        "reader_two_run_identical": body == body_two,
        "reader_ab_ba_identical": body == body_ba,
        "adverse": adverse,
    }


def _golden_run_equal_mask_pair(case, constants, bundle) -> dict[str, Any]:
    """PF01 §9.5 (M10-G008): distinct people with equal Gate masks, both Reader projections."""
    from engine.compat.compute import evaluate_pair, intrinsic_pair_key, is_ineligible_carrier, orient

    inputs = case["inputs"]
    meta = _golden_meta(inputs["meta"], "inputs.meta")
    routed: list[tuple[object, object, object]] = []
    router = _golden_router(constants, bundle, routed)
    party_a = _golden_party(constants, inputs["a"], "inputs.a")
    party_b = _golden_party(constants, inputs["b"], "inputs.b")
    result = evaluate_pair(party_a, party_b, bundle_provider=lambda: bundle, router=router)
    _golden_check_routing(routed, result)
    result_two = evaluate_pair(party_a, party_b, bundle_provider=lambda: bundle, router=router)
    _golden_check_routing(routed, result_two)
    result_ba = evaluate_pair(party_b, party_a, bundle_provider=lambda: bundle, router=router)
    _golden_check_routing(routed, result_ba)
    _golden_pair_order(result, result_ba)
    if is_ineligible_carrier(result):
        raise _GoldenCaseMismatch("expected.eligible", True, False)
    lo, hi = orient(party_a, party_b)
    body, envelope = _golden_reader(result, meta, inputs["release_id"])
    _, envelope_v2 = _golden_reader_v2(result, meta, inputs["release_id"])
    preimage = {key: value for key, value in envelope.items() if key != "idempotence_hash"}
    fixture_pair_key = intrinsic_pair_key(lo, hi, config_id=bundle.mechanics["config_id"],
                                          release_id=inputs["release_id"])
    candidate_pair_key = intrinsic_pair_key(lo, hi, config_id=result["config_id"], release_id=result["release_id"])
    return {
        "eligible": True,
        "members": [{"person_uid": party.canonical_person_id, "gate_mask_hex": party.gates.mask_hex,
                     "chart_fingerprint": party.chart_fingerprint} for party in (party_a, party_b)],
        "pair_key_under_release": {"config_id": bundle.mechanics["config_id"], "release_id": inputs["release_id"],
                                   "pair_key": fixture_pair_key},
        "pair_key_matches_candidate_derivation": result["pair_key"] == candidate_pair_key,
        "channel_states": _golden_channel_states(party_a.gates.mask, party_b.gates.mask, bundle),
        "signals": [{"signal_id": row["signal_id"], "q": row["q"]} for row in result["signals"]],
        "categories": [{"category_id": row["category_id"], "score": row["score"], "band": row["band"],
                        "shared_key": row["shared_key"], "personal_lo_to_hi_key": row["personal_lo_to_hi_key"],
                        "personal_hi_to_lo_key": row["personal_hi_to_lo_key"]} for row in result["categories"]],
        "orientation": {"lo": lo.canonical_person_id, "hi": hi.canonical_person_id},
        "reversed_order_bytes_identical": canon.sercanon(result) == canon.sercanon(result_ba),
        "two_run_bytes_identical": canon.sercanon(result) == canon.sercanon(result_two),
        "reader": {"eligible": envelope["eligible"], "categories": envelope["categories"],
                   "idempotence_hash": envelope["idempotence_hash"],
                   "hash_independent_of_pair_key": envelope["idempotence_hash"] != result["pair_key"],
                   "hash_equals_sha256_of_preimage_bytes":
                       hashlib.sha256(canon.sercanon(preimage)).hexdigest() == envelope["idempotence_hash"]},
        "reader_v2": {"eligible": envelope_v2["eligible"], "categories": envelope_v2["categories"],
                      "idempotence_hash": envelope_v2["idempotence_hash"]},
        "config_id_matches_candidate": result["config_id"] == bundle.mechanics["config_id"],
        "release_id_matches_candidate": result["release_id"] == bundle.release_id,
    }


_GOLDEN_RUNNERS = {
    "category_vector": _golden_run_category_vector,
    "core": _golden_run_core,
    "signal_operation": _golden_run_signal_operation,
    "band_boundary": _golden_run_band_boundary,
    "identity_independence": _golden_run_identity_independence,
    "self_pair": _golden_run_self_pair,
    "equal_mask_pair": _golden_run_equal_mask_pair,
}


def _golden_runner(case: Mapping[str, Any]):
    return _GOLDEN_RUNNERS[case["kind"]]


def _golden_reportable(value: object) -> object:
    """A mismatch value as the canonical report can carry it.

    Canonical JSON (PF12 §4.1) carries integers, strings, booleans, null, and arrays and
    string-keyed objects of them.  Anything else an entrypoint returns (a float, a
    non-finite number, bytes, an arbitrary object) is reported as a deterministic
    description instead, so the report stays canonical and rendering it never fails.
    """
    if value is None or type(value) in (bool, int, str):
        return value
    if type(value) is list:
        return [_golden_reportable(item) for item in value]
    if type(value) is dict and all(type(key) is str for key in value):
        return {key: _golden_reportable(item) for key, item in value.items()}
    if type(value) is float:
        return f"<float {value!r}>"
    return f"<{type(value).__name__}>"


def _golden_diff(case_id: str, expected: object, observed: object) -> list[Mismatch]:
    found: list[Mismatch] = []

    def walk(exp: object, act: object, path: str) -> None:
        if isinstance(exp, dict) and isinstance(act, dict):
            for key in sorted(set(exp) | set(act)):
                child = f"{path}.{key}"
                if key not in exp:
                    found.append(Mismatch(case_id, child, _GOLDEN_ABSENT, act[key]))
                elif key not in act:
                    found.append(Mismatch(case_id, child, exp[key], _GOLDEN_ABSENT))
                else:
                    walk(exp[key], act[key], child)
        elif isinstance(exp, list) and isinstance(act, list):
            if len(exp) != len(act):
                found.append(Mismatch(case_id, f"{path}.length", len(exp), len(act)))
            for index, (item_exp, item_act) in enumerate(zip(exp, act)):
                walk(item_exp, item_act, f"{path}[{index}]")
        elif type(exp) is not type(act) or exp != act:
            found.append(Mismatch(case_id, path, exp, act))

    walk(expected, observed, "expected")
    if not found and canon.sercanon(expected) != canon.sercanon(observed):
        found.append(Mismatch(case_id, "expected", "<canonical bytes>", "<canonical bytes differ>"))
    return found


def compare_goldens(candidate_root: Path, goldens_path: Path = GOLDENS_DEFAULT_PATH) -> GoldenComparison:
    """Compare the PF01 §9.5 v2 golden collection against one explicit candidate root.

    Read-only by construction: it validates both inputs, admits the candidate
    through the admission owner, runs each case through the canonical
    entrypoint for its kind, and reports every mismatch.  It never writes,
    activates, generates or repairs anything, and a refusal is never equality.

    The entrypoints are those of the executing installation.  Admission proves
    executable equivalence with the candidate's bytes only for the admission
    owner's covered mechanics modules, so a candidate root other than the
    executing installation is a fixture candidate whose success is test-only,
    never release admission.
    """
    require_closed_rails()
    document, goldens_sha256 = _golden_load_document(goldens_path)
    root, bundle = _golden_admit(candidate_root)
    _golden_bind_executed_members(bundle)
    constants = document["constants"]
    outcomes: list[CaseOutcome] = []
    mismatches: list[Mismatch] = []
    for case in document["cases"]:
        case_id, expected = case["case_id"], case["expected"]
        observed: dict[str, Any] = {}
        case_mismatches: list[Mismatch]
        try:
            observed = _golden_runner(case)(case, constants, bundle)
            case_mismatches = _golden_diff(case_id, expected, observed)
        except _GoldenCaseMismatch as exc:
            case_mismatches = [Mismatch(case_id, exc.path, exc.expected, exc.actual)]
        except Exception as exc:
            # A case that cannot run or be compared as the fixture states it (for
            # example a CompatBoundaryError from a non-canonical identity) is that
            # case's mismatch; it never aborts the comparison of the other cases.
            case_mismatches = [Mismatch(case_id, "execution", "completed", f"{type(exc).__name__}: {exc}")]
        case_mismatches = [Mismatch(row.case_id, row.path, _golden_reportable(row.expected), _golden_reportable(row.actual))
                           for row in case_mismatches]
        mismatches.extend(case_mismatches)
        outcomes.append(CaseOutcome(case_id, case["case_type"], case["kind"],
                                    "match" if not case_mismatches else "mismatch", expected, observed))
    # The runners import lazily: bind every member they loaded before a verdict.
    _golden_bind_executed_members(bundle)
    # A collection transcribed for another configuration never matches this candidate.
    if constants["config_id"] != bundle.mechanics["config_id"]:
        mismatches.append(Mismatch("constants", "constants.config_id", constants["config_id"], bundle.mechanics["config_id"]))
    ordered = tuple(sorted(mismatches, key=lambda row: (row.case_id, row.path)))
    return GoldenComparison(
        candidate_root=_golden_display(root), goldens_path=_golden_display(Path(goldens_path)),
        goldens_sha256=goldens_sha256, candidate_release_id=bundle.release_id,
        config_id=bundle.mechanics["config_id"], cases=tuple(outcomes), mismatches=ordered, ok=not ordered,
    )


def render_golden_report(result: GoldenComparison) -> bytes:
    """Canonical JSON report bytes (UTF-8, sorted keys, compact, one LF)."""
    return canon.sercanon({
        "schema": result.schema,
        "candidate_root": result.candidate_root,
        "goldens_path": result.goldens_path,
        "goldens_sha256": result.goldens_sha256,
        "candidate_release_id": result.candidate_release_id,
        "config_id": result.config_id,
        "ok": result.ok,
        "cases": [{"case_id": row.case_id, "case_type": row.case_type, "kind": row.kind, "outcome": row.outcome}
                  for row in result.cases],
        "mismatches": [{"case_id": row.case_id, "path": row.path, "expected": row.expected, "actual": row.actual}
                       for row in result.mismatches],
    }, sort_keys=True)
