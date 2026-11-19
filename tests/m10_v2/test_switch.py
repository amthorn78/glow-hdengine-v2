"""HDE-EPIC043 WU-PR-09: the switch (R-04, R-05; HDE-CONJ010.4, HDE-CONJ010.5).

The unit's own owner tests. They admit only temporary candidate roots, assembled
from the repository's bytes and the labelled non-canon fixtures of
``tests/fixtures/magic10_v2/``, through the unchanged admission path and the
test-only roster route of ``tests/config/helpers.py``. No maxima value is a canon
value; only M10-G001 (every category 0, band Cool) is fixed by canon before the cut.

1. Temporary-root admission: the admitted object and every seam reader.
2. Surfaces: ``hdctl showcompat`` and ``POST /api/compat/v1`` emit byte-equal,
   schema-valid ``magic10_compat_result.v2`` with ``q`` at 0 and 1000.
3. Reader v1 and v2: schema-valid, golden key shapes, numeric-free; the partial
   golden regression of PF10 addendum 2.5 R-3, repeated at the switch head.
4. The zero rule on M10-G001's pair.
5. Acceptance item 2's static proof, with its constructed positive.
6. The real-root refusal code, stage-adaptive.
7. The order of admission checks.
8. The F-28 refusal mapping.
9. The roster route is unreachable from production.

Stated limits: the narrative router reads its pack relative to the working
directory, so these tests run from the repository root; the static proof follows
imports, not dynamic imports through computed strings.
"""
from __future__ import annotations

import ast
import hashlib
import inspect
import json
import shutil
from pathlib import Path

import jsonschema
import pytest

from adapter import factory, http_reader
from engine.bodygraph.gates import NormalizedGates, normalize_gates
from engine.cli.main import cli
from engine.compat import compute
from engine.compat.error_tokens import BOUNDARY_REASONS, CompatBoundaryError, admission_token_for
from engine.config import registry_loader
from engine.config.magic10_v2_loader import (
    MAGIC10_V2_COMPAT_RESULT_SCHEMA,
    MAGIC10_V2_CONFIG_ID,
    MAGIC10_V2_CONFIGURATION_PATH,
    MAGIC10_V2_RESULT_SCHEMA,
    Magic10V2Bundle,
)
from engine.config.registry_loader import (
    AdmittedMechanicsBundle,
    RegistryConfigError,
    SchemaValidationError,
    _load_active_mechanics_bundle_from_root,
    load_active_mechanics_bundle,
)
from engine.magic10_v2 import compat as magic10_v2_compat
from engine.presenter.emitter import emit_public
from tests.config.helpers import (
    synthetic_complete_release_root,
    synthetic_v2_candidate_root,
    v2_candidate_roster,
    v2_candidate_roster_admission,
)
from tests.support.pr04_fixtures import FakeCurrentViewDB, build_pack, complete_chart, inject_seams

ROOT = Path(__file__).resolve().parents[2]
UUID_1 = "11111111-1111-4111-8111-111111111111"
UUID_2 = "22222222-2222-4222-8222-222222222222"
FULL = (1 << 64) - 1
# A real pair at which equilibrium_score reaches 1000 (tests/m10_v2/test_compat_result.py).
E1000 = (0xDD21D71A78F26A4E, 0x2EF2B87542BFFFDC)
# Real pairs whose harmony band is Open, Warm and Cool under the fixture maxima
# (tests/m10_v2/test_compat_reader_projection.py).
HARMONY_PAIRS = {
    "Open": (0x7BF7EF3DFFE8F3BF, 0x7C5582D3B7EA6F37),
    "Warm": (0xB71FDFB09CE03C35, 0x9DACFBED5ACE5519),
    "Cool": (0xEE2167164A871497, 0x930ED610C95D1014),
}
V1_GOLDENS = {"Open": "g03_harmony_open", "Warm": "g04_harmony_warm", "Cool": "g05_harmony_cool"}
ORDER = json.loads((ROOT / "catalog" / "magic10.json").read_bytes())["order"]
VIEWER_PREFS = {"top_category": ORDER[0], "weights": {category: 10 for category in ORDER}}
COMPAT_SCHEMA = json.loads((ROOT / "schemas" / "magic10_compat_result_v2.schema.json").read_bytes())
FORBIDDEN_PUBLIC = ("score", "signals", "pair_key", "shared_key", "personal", "config_id", '"q"', "gates")

ENTRY_POINTS = ("adapter/factory.py", "engine/cli/main.py", "engine/http/compat_handler.py")
RETIRED_MODULES = (
    "engine.compat.thresholds",
    "engine.magic10.calculators",
    "engine.magic10.composite",
    "engine.magic10.signals",
    "engine.magic10.thresholds",
    "engine.compat.ts_v0",
    "engine.compat.type_strategy_v0",
)
SCORING_PATH = (
    "engine/config/registry_loader.py",
    "engine/config/magic10_v2_loader.py",
    "engine/core/core.py",
    "engine/compat/compute.py",
    "engine/magic10_v2/__init__.py",
    "engine/magic10_v2/calculation.py",
    "engine/magic10_v2/compat.py",
    "engine/magic10_v2/kernel.py",
    "engine/magic10_v2/signals.py",
)
V1_CONFIGURATION = ("catalog/magic10_mechanics_v1.json", "m10-channel-state-v1.0.0")
# The one closure module still naming the v1 configuration, recorded with its owner:
# the config tool's v1 config-family publication is re-targeted at the cut (WU-PR-10).
V1_CONFIGURATION_OWNERS = {"tools.config.generate_config_artifacts": "WU-PR-10"}


# --- shared seams -----------------------------------------------------------------------------

@pytest.fixture(scope="module")
def candidate(tmp_path_factory):
    """One temporary v2 candidate root and the bundle admitted from it."""
    root = synthetic_v2_candidate_root(tmp_path_factory.mktemp("wu-pr-09-switch"))
    with v2_candidate_roster_admission():
        bundle = _load_active_mechanics_bundle_from_root(root)
    return root, bundle


@pytest.fixture(scope="module")
def pack(tmp_path_factory):
    return build_pack(tmp_path_factory.mktemp("wu-pr-09-switch-pack"))


@pytest.fixture
def seams(monkeypatch, candidate, pack):
    inject_seams(monkeypatch, candidate[1], pack)
    return candidate[1]


def _gates(mask: int) -> list[int]:
    return [gate for gate in range(1, 65) if mask >> (gate - 1) & 1]


def _write(path: Path, value: object) -> str:
    path.write_text(json.dumps(value), encoding="utf-8")
    return str(path)


def _post_compat(client, a, b):
    body = json.dumps({"a": a, "b": b, "viewer_prefs": VIEWER_PREFS}, sort_keys=True)
    return client.post("/api/compat/v1", data=body, headers={"Content-Type": "application/json; charset=utf-8"})


def _showcompat(tmp_path: Path, capsys, chart_a, chart_b) -> bytes:
    path_a, path_b = _write(tmp_path / "a.json", chart_a), _write(tmp_path / "b.json", chart_b)
    capsys.readouterr()
    assert cli(["showcompat", "--a-file", path_a, "--b-file", path_b]) == 0
    return capsys.readouterr().out.encode("utf-8")


def _strict_validator():
    strict = jsonschema.validators.extend(
        jsonschema.Draft202012Validator,
        type_checker=jsonschema.Draft202012Validator.TYPE_CHECKER.redefine(
            "integer", lambda checker, value: type(value) is int
        ),
    )
    return strict(COMPAT_SCHEMA)


# --- 1. temporary-root admission --------------------------------------------------------------

def test_temporary_root_admits_the_v2_bundle_through_the_v2_rules(candidate) -> None:
    root, bundle = candidate
    manifest_raw = (root / "catalog" / "manifest.json").read_bytes()
    rows = {row["path"]: row for row in json.loads(manifest_raw)["files"]}
    config_row = rows[MAGIC10_V2_CONFIGURATION_PATH]
    assert type(bundle) is AdmittedMechanicsBundle
    assert type(bundle.magic10_v2) is Magic10V2Bundle
    assert bundle.mechanics["config_id"] == MAGIC10_V2_CONFIG_ID
    assert bundle.mechanics == bundle.magic10_v2.configuration
    assert bundle.config_sha256 == bundle.magic10_v2.config_sha256 == config_row["sha256"]
    assert bundle.release_id == bundle.manifest_sha256 == hashlib.sha256(manifest_raw).hexdigest()
    assert tuple(row.path for row in bundle.manifest.files) == v2_candidate_roster()
    assert len(bundle.manifest.files) == 57
    assert "catalog/magic10_mechanics_v1.json" not in rows
    # The roster route restored the constant: production admission is unchanged.
    assert len(registry_loader.ADMITTED_RELEASE_ROSTER) == 45
    assert "catalog/magic10_mechanics_v1.json" in registry_loader.ADMITTED_RELEASE_ROSTER


def test_every_seam_reader_reads_the_admitted_object(candidate) -> None:
    _, bundle = candidate
    # The cutover guard (P1): release_id and config_sha256, the latter equal to the v2 configuration row.
    assert len(bundle.release_id) == 64 and len(bundle.config_sha256) == 64
    assert any(
        row.path == MAGIC10_V2_CONFIGURATION_PATH and row.sha256 == bundle.config_sha256
        for row in bundle.manifest.files
    )
    # The score-distribution utility.
    assert bundle.manifest.version == registry_loader.ADMITTED_RELEASE_VERSION
    assert tuple(bundle.registry.magic10_order) == tuple(ORDER)
    assert len(bundle.registry.channels) == 36
    # The compat computation.
    assert {row.path for row in bundle.source_identities} >= {"schemas/magic10_compat_result_v2.schema.json"}
    # The config tool's capture comparison.
    assert bundle.manifest_sha256 and bundle.source_identities
    # The dormant layer receives the v2 bundle and the release identity explicitly.
    assert bundle.magic10_v2.configuration["result_schema"] == MAGIC10_V2_RESULT_SCHEMA


# --- 2. surfaces ------------------------------------------------------------------------------

@pytest.mark.parametrize("pair", [(FULL, FULL), E1000], ids=["full", "e1000"])
def test_showcompat_and_compat_post_emit_byte_equal_v2(seams, tmp_path, capsys, pair) -> None:
    chart_a, chart_b = complete_chart(UUID_1, _gates(pair[0])), complete_chart(UUID_2, _gates(pair[1]))
    stdout = _showcompat(tmp_path, capsys, chart_a, chart_b)
    value = json.loads(stdout)
    assert value["schema"] == MAGIC10_V2_COMPAT_RESULT_SCHEMA
    _strict_validator().validate(value)
    assert stdout == emit_public(value)
    client = factory.create_app().test_client()
    for a, b in ((chart_a, chart_b), (chart_b, chart_a)):
        response = _post_compat(client, a, b)
        assert response.status_code == 200
        assert emit_public(response.get_json()) == stdout


def test_q_reaches_0_and_1000_on_real_pairs(seams, tmp_path, capsys) -> None:
    seen: set[int] = set()
    for index, pair in enumerate(((FULL, FULL), E1000)):
        case = tmp_path / str(index)
        case.mkdir()
        value = json.loads(_showcompat(case, capsys, complete_chart(UUID_1, _gates(pair[0])),
                                       complete_chart(UUID_2, _gates(pair[1]))))
        seen.update(row["q"] for row in value["signals"])
    assert {0, 1000} <= seen
    assert all(0 <= q <= 1000 for q in seen)


# --- 3. Reader v1 and v2 ----------------------------------------------------------------------

def _reader_client(monkeypatch, charts):
    fake = FakeCurrentViewDB(charts)
    monkeypatch.setattr(http_reader.DBAccess, "for_current_env", classmethod(lambda cls, *a, **k: fake))
    for name in ("HD_API_BASE_URL", "HDAPI_BASE_URL", "HD_API_KEY", "GEO_API_KEY", "DATABASE_URL"):
        monkeypatch.delenv(name, raising=False)
    app = http_reader.create_app()
    app.config.update(TESTING=True)
    return app.test_client()


def _reader_post(client, version: str):
    body = json.dumps({"a_id": UUID_1, "b_id": UUID_2})
    return client.post(f"/api/reader?v={version[1:]}", data=body,
                       headers={"Content-Type": "application/json; charset=utf-8"})


@pytest.mark.parametrize("band", sorted(V1_GOLDENS))
def test_reader_v1_matches_its_golden_outside_identity(seams, monkeypatch, band) -> None:
    lo, hi = HARMONY_PAIRS[band]
    client = _reader_client(monkeypatch, {UUID_1: complete_chart(UUID_1, _gates(lo)),
                                          UUID_2: complete_chart(UUID_2, _gates(hi))})
    response = _reader_post(client, "v1")
    assert response.status_code == 200
    envelope = json.loads(response.data)
    jsonschema.Draft202012Validator(json.loads((ROOT / "schemas" / "reader.v1.schema.json").read_bytes())).validate(envelope)
    golden = json.loads((ROOT / "goldens" / "reader" / "v1" / f"{V1_GOLDENS[band]}.json").read_bytes())
    assert set(envelope) == set(golden)
    for key in ("categories", "eligible", "reader_version"):
        assert envelope[key] == golden[key]
    assert envelope["release_id"] == seams.release_id
    assert not any(token in response.data.decode("utf-8") for token in FORBIDDEN_PUBLIC)


def test_reader_v2_matches_its_golden_shape(seams, monkeypatch) -> None:
    lo, hi = HARMONY_PAIRS["Open"]
    client = _reader_client(monkeypatch, {UUID_1: complete_chart(UUID_1, _gates(lo)),
                                          UUID_2: complete_chart(UUID_2, _gates(hi))})
    response = _reader_post(client, "v2")
    assert response.status_code == 200
    envelope = json.loads(response.data)
    jsonschema.Draft202012Validator(json.loads((ROOT / "schemas" / "reader.v2.schema.json").read_bytes())).validate(envelope)
    golden = json.loads((ROOT / "goldens" / "reader" / "v2" / "g03_eligible_ten_in_order.json").read_bytes())
    assert set(envelope) == set(golden)
    assert [row["id"] for row in envelope["categories"]] == [row["id"] for row in golden["categories"]]
    assert all(set(row) == {"id", "band"} for row in envelope["categories"])
    assert not any(token in response.data.decode("utf-8") for token in FORBIDDEN_PUBLIC)


# --- 4. the zero rule -------------------------------------------------------------------------

def test_m10_g001_pair_scores_zero_cool_through_showcompat(seams, tmp_path, capsys) -> None:
    value = json.loads(_showcompat(tmp_path, capsys, complete_chart(UUID_1, [1]), complete_chart(UUID_2, [2])))
    assert [(row["score"], row["band"]) for row in value["categories"]] == [(0, "Cool")] * 10


# --- 5. acceptance item 2: no retired scorer, no fallback, no selector ------------------------

def _module_name(root: Path, path: Path) -> str:
    parts = list(path.relative_to(root).with_suffix("").parts)
    if parts[-1] == "__init__":
        parts = parts[:-1]
    return ".".join(parts)


def _module_file(root: Path, name: str) -> Path | None:
    base = root.joinpath(*name.split("."))
    if base.with_suffix(".py").is_file():
        return base.with_suffix(".py")
    if (base / "__init__.py").is_file():
        return base / "__init__.py"
    return None


def _imported_names(root: Path, path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    own = _module_name(root, path)
    package = own if path.name == "__init__.py" else own.rpartition(".")[0]
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                parts = alias.name.split(".")
                names.update(".".join(parts[:index]) for index in range(1, len(parts) + 1))
        elif isinstance(node, ast.ImportFrom):
            if node.level:
                base = package.split(".") if package else []
                if node.level > 1:
                    base = base[: len(base) - (node.level - 1)]
                module = ".".join(base + ([node.module] if node.module else []))
            else:
                module = node.module or ""
            parts = module.split(".")
            names.update(".".join(parts[:index]) for index in range(1, len(parts) + 1))
            names.update(f"{module}.{alias.name}" for alias in node.names)
    return names


def static_closure(root: Path) -> dict[str, Path]:
    """The static import closure of the three production entry points under ``root``."""
    seen: dict[str, Path] = {}
    queue = [root / entry for entry in ENTRY_POINTS]
    while queue:
        path = queue.pop()
        name = _module_name(root, path)
        if name in seen:
            continue
        seen[name] = path
        for imported in _imported_names(root, path):
            target = _module_file(root, imported)
            if target is not None and _module_name(root, target) not in seen:
                queue.append(target)
    return seen


def _names_v1_configuration(tree: ast.AST) -> bool:
    set_elements = {id(element) for node in ast.walk(tree) if isinstance(node, ast.Set) for element in node.elts}
    return any(
        isinstance(node, ast.Constant) and isinstance(node.value, str) and id(node) not in set_elements
        and any(text in node.value for text in V1_CONFIGURATION)
        for node in ast.walk(tree)
    )


def _reads_environment(tree: ast.AST) -> bool:
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr in ("environ", "getenv"):
            return True
        if isinstance(node, ast.Name) and node.id in ("environ", "getenv"):
            return True
    return False


def item_2_findings(root: Path) -> list[str]:
    """Acceptance item 2 over ``root``; each finding names the check it fails."""
    findings: list[str] = []
    closure = static_closure(root)
    findings.extend(f"retired:{name}" for name in RETIRED_MODULES if name in closure)
    if "engine.magic10_v2.calculation" not in closure:
        findings.append("v2_unreached:engine.magic10_v2.calculation")
    for relative in SCORING_PATH:
        tree = ast.parse((root / relative).read_text(encoding="utf-8"))
        if _reads_environment(tree):
            findings.append(f"selector_environment:{relative}")
    for name, path in sorted(closure.items()):
        if name in V1_CONFIGURATION_OWNERS:
            continue
        if _names_v1_configuration(ast.parse(path.read_text(encoding="utf-8"))):
            findings.append(f"names_v1_configuration:{name}")
    return findings


def test_item_2_no_retired_scorer_fallback_or_selector() -> None:
    assert item_2_findings(ROOT) == []
    # No selecting parameter: the supported entries take exactly their fixed inputs.
    assert list(inspect.signature(load_active_mechanics_bundle).parameters) == []
    assert list(inspect.signature(compute.compute_core).parameters) == [
        "member_a", "member_b", "mechanics_bundle", "release_id"]
    assert [name for name, parameter in inspect.signature(compute.evaluate_pair).parameters.items()
            if parameter.kind is inspect.Parameter.KEYWORD_ONLY] == ["bundle_provider", "cache", "router"]


def test_item_2_proof_fails_on_its_named_check_for_a_retired_import(tmp_path) -> None:
    copy = tmp_path / "tree"
    for top in ("adapter", "engine", "presenter", "scripts", "tools"):
        for path in (ROOT / top).rglob("*.py"):
            target = copy / path.relative_to(ROOT)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, target)
    compute_copy = copy / "engine" / "compat" / "compute.py"
    compute_copy.write_text(compute_copy.read_text(encoding="utf-8") + "\nimport engine.compat.thresholds\n",
                            encoding="utf-8")
    # The retired thresholds module imports its v1 twin, so both are reached; nothing else fails.
    assert item_2_findings(copy) == ["retired:engine.compat.thresholds", "retired:engine.magic10.thresholds"]


# --- 6. the real-root refusal, stage-adaptive -------------------------------------------------

def test_real_root_admission_refuses_by_name_until_the_cut() -> None:
    try:
        bundle = load_active_mechanics_bundle()
    except RegistryConfigError as exc:
        assert exc.code in {"MANIFEST_MEMBER_HASH_MISMATCH", "M10V2_CONFIGURATION_ROW_MISSING", "SOURCE_READ_FAILED"}
    else:  # after the cut (WU-PR-10) the repository root admits the v2 release
        assert bundle.mechanics["config_id"] == MAGIC10_V2_CONFIG_ID


# --- 7. the order of admission checks ---------------------------------------------------------

def test_member_hashes_are_checked_before_executing_sources(tmp_path) -> None:
    unchanged = synthetic_complete_release_root(tmp_path / "unchanged")
    with pytest.raises(SchemaValidationError) as caught:
        _load_active_mechanics_bundle_from_root(unchanged)
    assert caught.value.code == "UNBOUND_SOURCE"
    changed = synthetic_complete_release_root(tmp_path / "changed")
    member = changed / "tools" / "bodygraph" / "check_magic10_gate_readiness.py"
    member.write_bytes(member.read_bytes().replace(b"Gate", b"gate", 1))
    with pytest.raises(SchemaValidationError) as caught:
        _load_active_mechanics_bundle_from_root(changed)
    assert caught.value.code == "MANIFEST_MEMBER_HASH_MISMATCH"


# --- 8. the F-28 refusal mapping --------------------------------------------------------------

def _tokens(reason: str) -> tuple[str, str, int]:
    return BOUNDARY_REASONS[reason]


@pytest.mark.parametrize("code,token", [
    ("MANIFEST_MEMBER_HASH_MISMATCH", "ERR_M10_MANIFEST_MISMATCH"),
    ("M10V2_MANIFEST_HASH_MISMATCH", "ERR_M10_MANIFEST_MISMATCH"),
    ("M10V2_INVALID_MANIFEST_ROWS", "ERR_M10_MANIFEST_MISMATCH"),
    ("RELEASE_ROSTER_MISMATCH", "ERR_M10_MANIFEST_MISMATCH"),
    ("M10V2_CONFIGURATION_ROW_MISSING", "ERR_M10_CONFIG_MISMATCH"),
    ("M10V2_MULTIPLE_CONFIGURATIONS", "ERR_M10_CONFIG_MISMATCH"),
    ("M10V2_PINNED_CONTENT_MISMATCH", "ERR_M10_CONFIG_MISMATCH"),
    ("UNBOUND_SOURCE", "ERR_M10_CONFIG_MISMATCH"),
    ("EXECUTING_SOURCE_MISMATCH", "ERR_M10_CONFIG_MISMATCH"),
])
def test_admission_refusals_map_at_the_surface(seams, monkeypatch, code, token) -> None:
    def refusing():
        raise SchemaValidationError(code, "refused")

    monkeypatch.setattr(compute, "_BUNDLE_PROVIDER", refusing)
    assert admission_token_for(code) == token
    response = _post_compat(factory.create_app().test_client(), complete_chart(UUID_1, [1, 2]),
                            complete_chart(UUID_2, [3, 4]))
    assert response.status_code == 503
    assert token in response.get_data(as_text=True)


def _parties():
    resolved_a = compute.ResolvedCompatChart(UUID_1, complete_chart(UUID_1, [10, 20]), "resolved", None, None, None, None)
    resolved_b = compute.ResolvedCompatChart(UUID_2, complete_chart(UUID_2, [34, 57]), "resolved", None, None, None, None)
    return compute.evaluation_party(resolved_a), compute.evaluation_party(resolved_b)


def _refusal(callable_) -> CompatBoundaryError:
    with pytest.raises(CompatBoundaryError) as caught:
        callable_()
    return caught.value


def test_invalid_members_map_to_gates_invalid(seams) -> None:
    a, b = _parties()
    broken = compute.EvaluationParty(a.canonical_person_id, a.projection,
                                     NormalizedGates(a.gates.gates, a.gates.mask + 1, a.gates.mask_hex),
                                     a.chart_fingerprint)
    exc = _refusal(lambda: compute.evaluate_pair(broken, b))
    assert (exc.reason, exc.token, exc.reader_token, exc.reader_status) == ("gates_invalid", *_tokens("gates_invalid"))


def test_core_value_error_with_valid_members_maps_to_admission_config(seams, monkeypatch) -> None:
    def failing(*args):
        raise ValueError("invalid pure core contract")

    monkeypatch.setattr(compute, "compute_core", failing)
    exc = _refusal(lambda: compute.evaluate_pair(*_parties()))
    assert (exc.reason, exc.token, exc.reader_token, exc.reader_status) == ("admission_config", *_tokens("admission_config"))


@pytest.mark.parametrize("code", ["M10V2_CALC_MAXIMA_INVALID", "M10V2_KERNEL_CENTERS_INCOMPLETE", "M10V2_SIGNALS_PROFILE_MISSING"])
def test_calculation_refusals_map_to_admission_config(seams, monkeypatch, code) -> None:
    def failing(*args):
        raise SchemaValidationError(code, "refused")

    monkeypatch.setattr(compute, "compute_core", failing)
    exc = _refusal(lambda: compute.evaluate_pair(*_parties()))
    assert (exc.reason, exc.detail) == ("admission_config", code)
    assert (exc.token, exc.reader_token, exc.reader_status) == _tokens("admission_config")


def test_missing_narrative_key_maps_to_narrative_key(seams) -> None:
    exc = _refusal(lambda: compute.evaluate_pair(*_parties(), router=lambda *args: {"personal_key": "p"}))
    assert exc.reason == "narrative_key"
    assert (exc.token, exc.reader_token, exc.reader_status) == ("ERR_MISSING_NARRATIVE_KEY", "ERR_M10_RESULT_SCHEMA_MISMATCH", 503)


def test_invalid_compat_value_maps_to_result_schema(seams, monkeypatch) -> None:
    def invalid(*args, **kwargs):
        raise SchemaValidationError(magic10_v2_compat.RESULT_INVALID, "invalid", {"check": "schema"})

    monkeypatch.setattr(magic10_v2_compat, "validate_compat_result_v2", invalid)
    exc = _refusal(lambda: compute.evaluate_pair(*_parties()))
    assert (exc.reason, exc.detail) == ("result_schema", "schema")
    assert (exc.token, exc.reader_token, exc.reader_status) == _tokens("result_schema")


def test_invalid_compat_input_maps_to_admission_config(seams, monkeypatch) -> None:
    def invalid(*args, **kwargs):
        raise SchemaValidationError(magic10_v2_compat.INPUT_INVALID, "invalid", {"argument": "bundle"})

    monkeypatch.setattr(magic10_v2_compat, "compat_result_v2", invalid)
    exc = _refusal(lambda: compute.evaluate_pair(*_parties()))
    assert (exc.reason, exc.detail) == ("admission_config", magic10_v2_compat.INPUT_INVALID)
    assert (exc.token, exc.reader_token, exc.reader_status) == _tokens("admission_config")


# --- 9. the roster route is unreachable from production ---------------------------------------

def test_the_test_only_roster_route_is_unreachable_from_production() -> None:
    assert not any(name == "tests" or name.startswith("tests.") for name in static_closure(ROOT))
    assigners = []
    for top in ("adapter", "engine", "presenter", "scripts", "tools"):
        for path in sorted((ROOT / top).rglob("*.py")):
            try:
                tree = ast.parse(path.read_text(encoding="utf-8"))
            except SyntaxError:  # e.g. scripts/scratch.py, a note that no import can load
                continue
            for node in ast.walk(tree):
                targets = node.targets if isinstance(node, ast.Assign) else (
                    [node.target] if isinstance(node, (ast.AnnAssign, ast.AugAssign)) else [])
                for target in targets:
                    name = target.id if isinstance(target, ast.Name) else (
                        target.attr if isinstance(target, ast.Attribute) else None)
                    if name == "ADMITTED_RELEASE_ROSTER":
                        assigners.append(path.relative_to(ROOT).as_posix())
    assert assigners == ["engine/config/registry_loader.py"]
    assert list(inspect.signature(load_active_mechanics_bundle).parameters) == []
