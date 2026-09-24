from __future__ import annotations

import hashlib
import json
import stat
from contextlib import nullcontext
from dataclasses import dataclass
import os
from pathlib import Path
from typing import Any, Callable, Mapping, Sequence

from engine.config.registry_loader import (
    RegistryConfig, SchemaValidationError, _capture_registry_config,
    _load_active_mechanics_bundle_from_root, _validate_thresholds,
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

GOLDENS_SCHEMA = "magic10_goldens.v1"
GOLDEN_COMPARISON_SCHEMA = "magic10_golden_comparison.v1"
GOLDENS_DEFAULT_PATH = ROOT / "tests/fixtures/magic10/v1/goldens.json"
# PF01 §9.5 ownership of each golden: kernel fixtures run through PR03's
# canonical kernel functions, application fixtures through ``evaluate_pair``.
GOLDEN_CASE_TABLE = (
    ("M10-G001", "kernel", "signal_vector"),
    ("M10-G002", "kernel", "signal_vector"),
    ("M10-G003", "kernel", "signal_operation"),
    ("M10-G004", "kernel", "core"),
    ("M10-G005", "application", "evaluate_pair"),
    ("M10-G006", "kernel", "reducer"),
    ("M10-G007", "application", "evaluate_pair"),
    ("M10-G008", "application", "evaluate_pair"),
)
GOLDEN_CASE_IDS = tuple(row[0] for row in GOLDEN_CASE_TABLE)
_GOLDEN_CASE_OWNERSHIP = {row[0]: (row[1], row[2]) for row in GOLDEN_CASE_TABLE}
_GOLDEN_TOP_KEYS = frozenset({"cases", "constants", "schema", "source"})
_GOLDEN_SOURCE_KEYS = frozenset({"document", "section", "sha256", "version"})
_GOLDEN_CONSTANT_KEYS = frozenset({
    "config_id", "meta", "release_id", "router_stub", "synthetic_projection_fields",
    "uuid_1", "uuid_2", "uuid_3", "uuid_4",
})
_GOLDEN_CASE_KEYS = frozenset({
    "case_id", "case_type", "expected", "input_provenance", "inputs", "kind",
    "realizable_chart_claim", "title",
})
_GOLDEN_CASE_OPTIONAL_KEYS = frozenset({"notes"})
_GOLDEN_PROVENANCE_TAGS = frozenset({
    "pf01_9_5", "synthetic_projection_fields", "fixture_selected_within_pf01_rule",
})
_GOLDEN_KERNEL_INPUT_KEYS = {
    "signal_vector": frozenset({"channel_states"}),
    "signal_operation": frozenset({"channels", "operation", "scenarios", "signal_id", "state"}),
    "reducer": frozenset({"category_id", "pairs"}),
    "core": frozenset({"member_a_gates", "member_b_gates"}),
}
_GOLDEN_APPLICATION_INPUT_KEYS = {
    "M10-G005": frozenset({"pairs"}),
    "M10-G007": frozenset({"a", "adverse", "b", "meta", "release_id"}),
    "M10-G008": frozenset({"a", "b", "meta", "release_id"}),
}
_GOLDEN_ABSENT = "<absent>"
_GOLDEN_OWNER_SWAP = {"member_lo": "member_hi", "member_hi": "member_lo", None: None}


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
    candidate_root: str
    goldens_path: str
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


def _golden_is_str(value: object) -> bool:
    return type(value) is str and bool(value)


def _golden_load_document(goldens_path: Path) -> tuple[Mapping[str, Any], str]:
    path = Path(os.path.abspath(goldens_path))
    try:
        if path.is_symlink() or not path.is_file():
            raise _golden_refuse("GOLDENS_INVALID")
        raw = path.read_bytes()
    except OSError:
        raise _golden_refuse("GOLDENS_INVALID") from None
    try:
        document = json.loads(raw.decode("utf-8"), object_pairs_hook=_golden_pairs_hook)
    except (UnicodeDecodeError, ValueError):
        raise _golden_refuse("GOLDENS_INVALID") from None
    if not isinstance(document, dict) or canon.sercanon(document, sort_keys=True) != raw:
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
    if not isinstance(constants, dict) or set(constants) != _GOLDEN_CONSTANT_KEYS:
        raise _golden_refuse("GOLDENS_INVALID")
    if not (all(_golden_is_str(constants[key]) for key in ("config_id", "release_id", "uuid_1", "uuid_2", "uuid_3", "uuid_4"))
            and isinstance(constants["meta"], dict) and set(constants["meta"]) == {"engine_tag", "invocation_tag"}
            and isinstance(constants["router_stub"], dict)
            and set(constants["router_stub"]) == {"personal_lo_to_hi", "personal_hi_to_lo", "shared"}
            and isinstance(constants["synthetic_projection_fields"], dict)):
        raise _golden_refuse("GOLDENS_INVALID")
    if not isinstance(cases, list) or not all(isinstance(case, dict) and _golden_is_str(case.get("case_id")) for case in cases):
        raise _golden_refuse("GOLDENS_INVALID")
    if tuple(case["case_id"] for case in cases) != GOLDEN_CASE_IDS:
        raise _golden_refuse("GOLDENS_MEMBERSHIP_INVALID")
    for case in cases:
        keys = set(case)
        if not (_GOLDEN_CASE_KEYS <= keys <= (_GOLDEN_CASE_KEYS | _GOLDEN_CASE_OPTIONAL_KEYS)):
            raise _golden_refuse("GOLDENS_INVALID")
        case_type, kind = _GOLDEN_CASE_OWNERSHIP[case["case_id"]]
        if case["case_type"] != case_type or case["kind"] != kind:
            raise _golden_refuse("GOLDENS_CASE_TYPE_INVALID")
        provenance = case["input_provenance"]
        if (not _golden_is_str(case["title"])
                or type(case["realizable_chart_claim"]) not in (bool, type(None))
                or not isinstance(provenance, list) or not provenance
                or len(set(provenance)) != len(provenance)
                or not all(tag in _GOLDEN_PROVENANCE_TAGS for tag in provenance)
                or not isinstance(case["inputs"], dict) or not isinstance(case["expected"], dict)
                or not case["expected"]
                or ("notes" in case and not (isinstance(case["notes"], list)
                                              and all(_golden_is_str(note) for note in case["notes"])))):
            raise _golden_refuse("GOLDENS_INVALID")
        expected_input_keys = (_GOLDEN_APPLICATION_INPUT_KEYS[case["case_id"]] if kind == "evaluate_pair"
                               else _GOLDEN_KERNEL_INPUT_KEYS[kind])
        if set(case["inputs"]) != expected_input_keys:
            raise _golden_refuse("GOLDENS_INVALID")


def _golden_admit(candidate_root: Path):
    root = Path(os.path.abspath(candidate_root))
    try:
        if root.is_symlink() or not root.is_dir():
            raise _golden_refuse("CANDIDATE_ROOT_INVALID")
    except OSError:
        raise _golden_refuse("CANDIDATE_ROOT_INVALID") from None
    try:
        bundle = _load_active_mechanics_bundle_from_root(root)
    except SchemaValidationError as exc:
        raise _golden_refuse(f"CANDIDATE_ADMISSION_REFUSED:{exc.code}") from None
    return root, bundle


def _golden_signal_order(bundle) -> tuple[str, ...]:
    registry = bundle.registry
    return tuple(signal for category in registry.magic10_order
                 for signal in registry.magic10_caps[category].inputs)


def _golden_categories(q_by_signal: Mapping[str, int], bundle) -> list[dict[str, Any]]:
    from engine.magic10.calculators import _reduce_category

    registry, mechanics = bundle.registry, bundle.mechanics
    weights = {row["category_id"]: tuple(row["weights"]) for row in mechanics["category_weights"]}
    rows = []
    for category in registry.magic10_order:
        caps = registry.magic10_caps[category]
        value = _reduce_category(category, tuple(q_by_signal[s] for s in caps.inputs), caps.bounds, weights[category])
        rows.append({"category_id": value.category_id, "score": value.score, "band": value.band})
    return rows


def _golden_rows(states: Sequence[Mapping[str, Any]]):
    from engine.magic10.composite import ChannelClassification

    return tuple(ChannelClassification(row["channel_id"], row["state"], row["owner"]) for row in states)


def _golden_run_signal_vector(case, constants, bundle) -> dict[str, Any]:
    from engine.magic10.signals import _compute_signals

    states = case["inputs"]["channel_states"]
    fixture_ids = [row["channel_id"] for row in states]
    candidate_ids = sorted(bundle.registry.channels)
    if sorted(fixture_ids) != candidate_ids or len(set(fixture_ids)) != len(fixture_ids):
        raise _GoldenCaseMismatch("inputs.channel_states.channel_ids", candidate_ids, sorted(fixture_ids))
    signals = _compute_signals(_golden_rows(states), bundle.mechanics, _golden_signal_order(bundle))
    q_by_signal = {row.signal_id: row.q for row in signals}
    return {
        "signals": [{"signal_id": row.signal_id, "q": row.q} for row in signals],
        "categories": _golden_categories(q_by_signal, bundle),
    }


def _golden_run_signal_operation(case, constants, bundle) -> dict[str, Any]:
    from engine.magic10.composite import ChannelClassification
    from engine.magic10.signals import _signal_q

    inputs = case["inputs"]
    definition = next((row for row in bundle.mechanics["signals"] if row["signal_id"] == inputs["signal_id"]), None)
    if definition is None:
        raise _GoldenCaseMismatch("inputs.signal_id", [row["signal_id"] for row in bundle.mechanics["signals"]], inputs["signal_id"])
    responses = None
    if "profile_id" in definition:
        responses = next(row["responses"] for row in bundle.mechanics["profiles"]
                         if row["profile_id"] == definition["profile_id"])
    channel_ids = [member["channel_id"] for member in definition["channels"]]
    scenarios = []
    for scenario in inputs["scenarios"]:
        owners = list(scenario["owners"])
        if len(owners) != len(channel_ids):
            raise _GoldenCaseMismatch(f"inputs.scenarios.{scenario['scenario_id']}.owners.length", len(channel_ids), len(owners))
        rows = {cid: ChannelClassification(cid, inputs["state"], owner) for cid, owner in zip(channel_ids, owners)}
        swapped = {cid: ChannelClassification(cid, inputs["state"], _GOLDEN_OWNER_SWAP[owner])
                   for cid, owner in zip(channel_ids, owners)}
        scenarios.append({
            "scenario_id": scenario["scenario_id"],
            "q": _signal_q(definition["operation"], definition["channels"], rows, responses),
            "q_owners_swapped": _signal_q(definition["operation"], definition["channels"], swapped, responses),
        })
    return {
        "definition": {
            "operation": definition["operation"],
            "channels": [{"channel_id": member["channel_id"], "weight": member["weight"]} for member in definition["channels"]],
        },
        "scenarios": scenarios,
    }


def _golden_run_reducer(case, constants, bundle) -> dict[str, Any]:
    from engine.magic10.calculators import _reduce_category

    inputs = case["inputs"]
    category = inputs["category_id"]
    caps = bundle.registry.magic10_caps.get(category)
    if caps is None:
        raise _GoldenCaseMismatch("inputs.category_id", list(bundle.registry.magic10_order), category)
    weights = next(tuple(row["weights"]) for row in bundle.mechanics["category_weights"] if row["category_id"] == category)
    results = []
    for pair in inputs["pairs"]:
        value = _reduce_category(category, tuple(pair), caps.bounds, weights)
        results.append({"q": list(pair), "score": value.score, "band": value.band})
    return {"results": results}


def _golden_hex64(value: object) -> bool:
    return type(value) is str and len(value) == 64 and all(char in "0123456789abcdef" for char in value)


def _golden_channel_states(mask_a: int, mask_b: int, bundle) -> list[dict[str, Any]]:
    from engine.magic10.composite import _classify_channels

    return [{"channel_id": row.channel_id, "state": row.state, "owner": row.owner}
            for row in _classify_channels(mask_a, mask_b, bundle.registry.channels)]


def _golden_run_core(case, constants, bundle) -> dict[str, Any]:
    from engine.bodygraph.gates import normalize_gates
    from engine.core.core import compute_core

    inputs = case["inputs"]
    member_a = normalize_gates(list(inputs["member_a_gates"]))
    member_b = normalize_gates(list(inputs["member_b_gates"]))
    first = compute_core(member_a, member_b, bundle, bundle.release_id).to_payload()
    second = compute_core(member_a, member_b, bundle, bundle.release_id).to_payload()
    reversed_order = compute_core(member_b, member_a, bundle, bundle.release_id).to_payload()
    return {
        "channel_states": _golden_channel_states(member_a.mask, member_b.mask, bundle),
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


def _golden_party(constants: Mapping[str, Any], spec: Mapping[str, Any],
                  override: Mapping[str, Any] | None = None):
    from engine.bodygraph.resolver import ResolvedCompatChart
    from engine.compat.compute import evaluation_party

    chart = _golden_chart(constants, spec["person_uid"], spec["gates"], override)
    return evaluation_party(ResolvedCompatChart(spec["person_uid"], chart, "resolved", None, None, None, None))


def _golden_router(constants: Mapping[str, Any]) -> Callable[..., Mapping[str, str]]:
    stub = constants["router_stub"]

    def router(category: str, band: str, perspective: str, **_ignored):
        personal = stub["personal_lo_to_hi"] if perspective == "a_to_b" else stub["personal_hi_to_lo"]
        return {"personal_key": personal, "shared_key": stub["shared"]}

    return router


def _golden_reader(result: Mapping[str, Any], meta: Mapping[str, str], release_id: str):
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


def _golden_intrinsic(result: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "schema": result["schema"], "config_id": result["config_id"], "release_id": result["release_id"],
        "pair_key": result["pair_key"],
        "signals": [{"signal_id": row["signal_id"], "q": row["q"]} for row in result["signals"]],
        "categories": [{"category_id": row["category_id"], "score": row["score"], "band": row["band"]}
                       for row in result["categories"]],
    }


def _golden_run_identity_independence(case, constants, bundle) -> dict[str, Any]:
    from engine.compat.compute import evaluate_pair

    router = _golden_router(constants)
    results = []
    for pair in case["inputs"]["pairs"]:
        party_a = _golden_party(constants, pair["a"])
        party_b = _golden_party(constants, pair["b"])
        results.append(evaluate_pair(party_a, party_b, bundle_provider=lambda: bundle, router=router))
    intrinsic = [_golden_intrinsic(result) for result in results]
    return {
        "pair_key_equal_across_pairs": len({row["pair_key"] for row in intrinsic}) == 1,
        "intrinsic_bytes_equal_across_pairs": len({canon.sercanon(row) for row in intrinsic}) == 1,
        "intrinsic": {"schema": intrinsic[0]["schema"], "signals": intrinsic[0]["signals"],
                      "categories": intrinsic[0]["categories"]},
    }


def _golden_run_self_pair(case, constants, bundle) -> dict[str, Any]:
    from engine.compat.compute import evaluate_pair
    from engine.compat.error_tokens import CompatBoundaryError

    inputs = case["inputs"]
    router = _golden_router(constants)
    party_a = _golden_party(constants, inputs["a"])
    party_b = _golden_party(constants, inputs["b"])
    result = evaluate_pair(party_a, party_b, bundle_provider=lambda: bundle, router=router)
    reversed_result = evaluate_pair(party_b, party_a, bundle_provider=lambda: bundle, router=router)
    body, envelope = _golden_reader(result, inputs["meta"], inputs["release_id"])
    body_two, _ = _golden_reader(result, inputs["meta"], inputs["release_id"])
    body_ba, _ = _golden_reader(reversed_result, inputs["meta"], inputs["release_id"])
    adverse = []
    for variant in inputs["adverse"]:
        override = {variant["field"]: variant["value"]}
        mutated_a = _golden_party(constants, inputs["a"], override if variant["party"] == "a" else None)
        mutated_b = _golden_party(constants, inputs["b"], override if variant["party"] == "b" else None)
        token = reason = None
        returned = False
        try:
            evaluate_pair(mutated_a, mutated_b, bundle_provider=lambda: bundle, router=router)
            returned = True
        except CompatBoundaryError as exc:
            token, reason = exc.token, exc.reason
        adverse.append({"adverse_id": variant["adverse_id"], "token": token, "reason": reason, "result_returned": returned})
    return {
        "eligible": bool(result.get("eligible")) if "eligible" in result else True,
        "evaluate_pair_result": json.loads(canon.sercanon(result).decode("utf-8")),
        "pair_key_present": "pair_key" in result,
        "reader": {"eligible": envelope["eligible"], "categories": envelope["categories"],
                   "idempotence_hash": envelope["idempotence_hash"]},
        "reader_two_run_identical": body == body_two,
        "reader_ab_ba_identical": body == body_ba,
        "adverse": adverse,
    }


def _golden_run_equal_mask_pair(case, constants, bundle) -> dict[str, Any]:
    from engine.compat.compute import evaluate_pair, intrinsic_pair_key, is_ineligible_carrier, orient

    inputs = case["inputs"]
    router = _golden_router(constants)
    party_a = _golden_party(constants, inputs["a"])
    party_b = _golden_party(constants, inputs["b"])
    result = evaluate_pair(party_a, party_b, bundle_provider=lambda: bundle, router=router)
    result_two = evaluate_pair(party_a, party_b, bundle_provider=lambda: bundle, router=router)
    result_ba = evaluate_pair(party_b, party_a, bundle_provider=lambda: bundle, router=router)
    if is_ineligible_carrier(result):
        raise _GoldenCaseMismatch("expected.eligible", True, False)
    lo, hi = orient(party_a, party_b)
    body, envelope = _golden_reader(result, inputs["meta"], inputs["release_id"])
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
        "config_id_matches_candidate": result["config_id"] == bundle.mechanics["config_id"],
        "release_id_matches_candidate": result["release_id"] == bundle.release_id,
    }


_GOLDEN_RUNNERS = {
    ("signal_vector", None): _golden_run_signal_vector,
    ("signal_operation", None): _golden_run_signal_operation,
    ("reducer", None): _golden_run_reducer,
    ("core", None): _golden_run_core,
    ("evaluate_pair", "M10-G005"): _golden_run_identity_independence,
    ("evaluate_pair", "M10-G007"): _golden_run_self_pair,
    ("evaluate_pair", "M10-G008"): _golden_run_equal_mask_pair,
}


def _golden_runner(case: Mapping[str, Any]):
    kind = case["kind"]
    return _GOLDEN_RUNNERS[(kind, case["case_id"] if kind == "evaluate_pair" else None)]


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
    """Compare the PF01 §9.5 golden collection against one explicit candidate root.

    Read-only by construction: it validates both inputs, admits the candidate
    through the admission owner, runs each case through the canonical
    entrypoint for its kind, and reports every mismatch.  It never writes,
    activates, generates or repairs anything, and a refusal is never equality.
    """
    require_closed_rails()
    document, goldens_sha256 = _golden_load_document(goldens_path)
    root, bundle = _golden_admit(candidate_root)
    constants = document["constants"]
    outcomes: list[CaseOutcome] = []
    mismatches: list[Mismatch] = []
    for case in document["cases"]:
        case_id, expected = case["case_id"], case["expected"]
        observed: dict[str, Any] = {}
        case_mismatches: list[Mismatch]
        try:
            observed = _golden_runner(case)(case, constants, bundle)
        except _GoldenCaseMismatch as exc:
            case_mismatches = [Mismatch(case_id, exc.path, exc.expected, exc.actual)]
        except Exception as exc:
            # A case that cannot run as the fixture states it (for example a
            # CompatBoundaryError from a non-canonical identity) is that case's
            # mismatch; it never aborts the comparison of the other cases.
            case_mismatches = [Mismatch(case_id, "execution", "completed", f"{type(exc).__name__}: {exc}")]
        else:
            case_mismatches = _golden_diff(case_id, expected, observed)
        mismatches.extend(case_mismatches)
        outcomes.append(CaseOutcome(case_id, case["case_type"], case["kind"],
                                    "match" if not case_mismatches else "mismatch", expected, observed))
    ordered = tuple(sorted(mismatches, key=lambda row: (row.case_id, row.path)))
    return GoldenComparison(
        candidate_root=str(root), goldens_path=str(Path(os.path.abspath(goldens_path))),
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
