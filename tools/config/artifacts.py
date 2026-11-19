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
# collection (PF01 §9.5 v2).  Before the cut it holds M10-G001 only; WU-PR-10 adds
# M10-G002 to M10-G008 and the runners their case kinds need.
GOLDENS_SCHEMA = "magic10_goldens.v2"
GOLDEN_COMPARISON_SCHEMA = "magic10_golden_comparison.v1"
GOLDENS_DEFAULT_PATH = ROOT / "tests/fixtures/magic10/v2/goldens.json"
# A document must be canonical and closed, so 1 MiB leaves ample room while an
# oversized input is refused after reading at most one byte past the bound.
GOLDENS_MAX_BYTES = 1_048_576
_GOLDEN_TOP_KEYS = frozenset({"cases", "constants", "schema", "source"})
_GOLDEN_SOURCE_KEYS = frozenset({"document", "section", "sha256", "version"})
_GOLDEN_CONSTANT_KEYS = frozenset({"config_id", "release_id"})
_GOLDEN_CASE_KEYS = frozenset({
    "case_id", "case_type", "expected", "input_provenance", "inputs", "kind",
    "realizable_chart_claim", "title",
})
_GOLDEN_CASE_OPTIONAL_KEYS = frozenset({"notes"})
# The closed set of case kinds, each with its case type and input keys; any other
# kind is refused (GOLDENS_INVALID) before a candidate is admitted.
_GOLDEN_KINDS = {
    "category_vector": ("calculation", frozenset({"gates_a", "gates_b"})),
}
_GOLDEN_ABSENT = "<absent>"


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


def _golden_validate_document(document: Mapping[str, Any]) -> None:
    if set(document) != _GOLDEN_TOP_KEYS or document["schema"] != GOLDENS_SCHEMA:
        raise _golden_refuse("GOLDENS_INVALID")
    source, constants, cases = document["source"], document["constants"], document["cases"]
    if (not isinstance(source, dict) or set(source) != _GOLDEN_SOURCE_KEYS
            or not all(_golden_is_str(value) for value in source.values())):
        raise _golden_refuse("GOLDENS_INVALID")
    if (not isinstance(constants, dict) or set(constants) != _GOLDEN_CONSTANT_KEYS
            or not all(_golden_is_str(value) for value in constants.values())):
        raise _golden_refuse("GOLDENS_INVALID")
    if (not isinstance(cases, list) or not cases
            or not all(isinstance(case, dict) and _golden_is_str(case.get("case_id")) for case in cases)):
        raise _golden_refuse("GOLDENS_INVALID")
    case_ids = [case["case_id"] for case in cases]
    if len(set(case_ids)) != len(case_ids):
        raise _golden_refuse("GOLDENS_MEMBERSHIP_INVALID")
    for case in cases:
        keys = set(case)
        if not (_GOLDEN_CASE_KEYS <= keys <= (_GOLDEN_CASE_KEYS | _GOLDEN_CASE_OPTIONAL_KEYS)):
            raise _golden_refuse("GOLDENS_INVALID")
        if case["kind"] not in _GOLDEN_KINDS:
            raise _golden_refuse("GOLDENS_INVALID")
        case_type, input_keys = _GOLDEN_KINDS[case["kind"]]
        if case["case_type"] != case_type:
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


def _golden_run_category_vector(case, constants, bundle) -> dict[str, Any]:
    """PF01 §9.5 v2: the category vector of ``compute_core`` over the admitted candidate."""
    from engine.core.core import compute_core

    inputs = case["inputs"]
    member_a = _golden_gates(inputs["gates_a"], "inputs.gates_a")
    member_b = _golden_gates(inputs["gates_b"], "inputs.gates_b")
    result = compute_core(member_a, member_b, bundle, bundle.release_id)
    return {"categories": [
        {"category_id": row.category_id, "score": row.score, "band": row.band} for row in result.categories
    ]}


_GOLDEN_RUNNERS = {
    "category_vector": _golden_run_category_vector,
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
