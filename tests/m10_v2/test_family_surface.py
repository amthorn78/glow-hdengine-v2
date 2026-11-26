"""HDE-EPIC043 WU-PR-04: the v2 proof family, version-neutral surface cases (HDE-DIST008.1).

Items v2 does not change, whose mechanism lives in release members that reach a
v2 result only from the switch (WU-PR-09): F-21b (release-binding rejection),
F-22 (valid identical self-pair short-circuit), F-23 (same identity, unequal
projection), F-24 (distinct-person equal-mask intrinsic identity, fingerprint
part), F-25 (equal-mask orientation by ASCII UUID tie-break), F-26 (independent
public Reader idempotence), F-27 (CLI, internal HTTP, compat and Reader parity)
and F-28 (PF05 token and HTTP mapping of the existing fail-closed conditions).

Each case calls the existing surface through its existing seams over the bundle
the provider admits, with no bundle injected: at Stage A that is the active
release, and after WU-PR-09 re-targets the members the same case runs over v2
without an edit (WU-PR-13 runs it on the frozen candidate). Version-neutral: no
case asserts a schema name, a ``q`` range, a score or band value, a
``release_id`` literal, a cache-key prefix or a ``config_id``; a ``release_id``
is read from the admitted bundle at run time. The refused mutations patch one
rule in-process; no release member file is edited. Identities are synthetic.

Stated limits: the mapping of the v2 refusal codes to PF05 tokens (F-28) and
"no fallback and no selector" (F-18) are delivered by WU-PR-09's own tests,
``tests/m10_v2/test_switch.py``; at WU-PR-09's head the cases that admit the
repository root fail with the named refusal until WU-PR-10's admission.
"""
from __future__ import annotations

import functools
import json
import shutil
from pathlib import Path

import pytest

from adapter.factory import create_app
from engine.bodygraph.resolver import ResolvedCompatChart
from engine.cli.main import cli
from engine.compat import compute
from engine.compat import error_tokens
from engine.compat.error_tokens import BOUNDARY_REASONS, MAGIC10_HTTP_STATUS, CompatBoundaryError, admission_token_for
from engine.config import registry_loader
from engine.config.registry_loader import (
    ADMITTED_RELEASE_ROSTER,
    RegistryConfigError,
    SourceIdentity,
    _load_active_mechanics_bundle_from_root,
    load_active_mechanics_bundle,
)
from engine.runtime import public
from engine.serializer.canon import sercanon

ROOT = Path(__file__).resolve().parents[2]
UUID_1 = "00000000-0000-0000-0000-000000000001"
UUID_2 = "00000000-0000-0000-0000-000000000002"
UUID_3 = "00000000-0000-0000-0000-000000000003"
UUID_4 = "00000000-0000-0000-0000-000000000004"
GATES_A = [1, 8, 20, 57, 32, 54, 10, 34]
GATES_B = [3, 60, 21, 45, 47, 64, 2, 14]
META = {"engine_tag": "m10-family", "invocation_tag": "m10-family-surface"}
ORDER = json.loads((ROOT / "catalog" / "magic10.json").read_bytes())["order"]
# The internal HTTP route requires viewer preferences; they are an input-side handoff and never enter scoring.
VIEWER_PREFS = {"top_category": ORDER[0], "weights": {category: 10 for category in ORDER}}


def _post(client, body: dict):
    data = json.dumps({**body, "viewer_prefs": VIEWER_PREFS}, sort_keys=True)
    return client.post("/api/compat/v1", data=data, headers={"Content-Type": "application/json; charset=utf-8"})


def _chart(uid: str, gates, **overrides) -> dict:
    """A complete mapped chart projection with one identity (synthetic)."""
    bodygraph = {
        "authority": "Emotional", "birthDateUtc": "2000-01-01T00:00:00Z", "centers": ["Ajna", "Solar Plexus"],
        "channelsLong": ["10-20"], "channelsShort": ["34-20"], "definition": "Single", "gates": list(gates),
        "profile": "1/3", "strategy": "Wait to Respond", "type": "Manifesting Generator",
    }
    bodygraph.update(overrides)
    return {"bodygraph": bodygraph, "person": {"person_uid": uid}, "person_uid": uid}


def _party(uid: str, gates, **overrides) -> compute.EvaluationParty:
    resolved = ResolvedCompatChart(uid, _chart(uid, gates, **overrides), "resolved", None, None, None, None)
    return compute.evaluation_party(resolved)


def _stub_router(category, band, perspective):
    return {"personal_key": f"m10.family.personal.{perspective}", "shared_key": "m10.family.shared"}


def _check(function):
    """A check reports a failed assertion, or the product's own typed refusal, as ``AssertionError``.

    Any other exception propagates, so a mutation case cannot pass on an unrelated crash
    (HDE-EPIC043 WU-PR-13; PF10 addendum 2.6 R-3).
    """
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except CompatBoundaryError as exc:
            raise AssertionError(f"{function.__name__}: {exc}") from exc
    return wrapper


@pytest.fixture(autouse=True)
def _closed_rails(monkeypatch):
    for name, value in (("SAFE_MODE", "1"), ("ALLOW_NETWORK", "0"), ("APP_ENV", "test")):
        monkeypatch.setenv(name, value)


class _Spy:
    def __init__(self):
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        raise AssertionError("seam reached")


class _Cache:
    def __init__(self):
        self.gets = []

    def get(self, key):
        self.gets.append(key)

    def put(self, key, value):
        raise AssertionError("cache written")


# --- F-21b ------------------------------------------------------------------------------------

def _release_root(base: Path) -> Path:
    root = base / "release"
    for path in (*ADMITTED_RELEASE_ROSTER, "catalog/manifest.json"):
        (root / path).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / path, root / path)
    return root


@_check
def _check_f21b(base: Path) -> None:
    root = _release_root(base)
    admitted = _load_active_mechanics_bundle_from_root(root)
    assert admitted.release_id == load_active_mechanics_bundle().release_id
    member = sorted(path for path in ADMITTED_RELEASE_ROSTER if path.endswith(".py"))[0]
    (root / member).write_bytes((root / member).read_bytes() + b"\n# a byte the manifest does not bind\n")
    try:
        _load_active_mechanics_bundle_from_root(root)
    except RegistryConfigError as exc:
        assert exc.code == "MANIFEST_MEMBER_HASH_MISMATCH"
        assert admission_token_for(exc.code) == "ERR_M10_MANIFEST_MISMATCH"
    else:
        raise AssertionError("a member that the manifest does not bind was admitted")


def test_f21b_release_binding_rejection(tmp_path) -> None:
    _check_f21b(tmp_path)


def test_f21b_mutation_unbound_member_admitted_is_refused(tmp_path, monkeypatch) -> None:
    def lenient(capture, manifest):
        for entry in manifest.files:
            capture.capture_release_member(entry.path)
        return tuple(SourceIdentity(entry.path, entry.sha256, entry.size) for entry in manifest.files)

    monkeypatch.setattr(registry_loader, "_capture_admitted_members", lenient)
    with pytest.raises(AssertionError):
        _check_f21b(tmp_path)


# --- F-22 -------------------------------------------------------------------------------------

@_check
def _check_f22() -> None:
    a, b = _party(UUID_1, GATES_A), _party(UUID_1, [str(gate) for gate in GATES_A])
    assert compute.validate_pair_eligibility(a, b) == "ineligible_self"
    cache, router = _Cache(), _Spy()
    for first, second in ((a, b), (b, a)):
        result = compute.evaluate_pair(first, second, cache=cache, router=router)
        assert result == {"categories": [], "eligible": False}
        assert compute.is_ineligible_carrier(result) and "pair_key" not in result
    assert cache.gets == [] and router.calls == 0


def test_f22_self_pair_short_circuit(monkeypatch) -> None:
    for name in ("compute_core", "intrinsic_pair_key", "route_keys"):
        monkeypatch.setattr(compute, name, _Spy())
    monkeypatch.setattr(compute, "_BUNDLE_PROVIDER", _Spy())
    _check_f22()


def test_f22_mutation_self_pair_evaluated_is_refused(monkeypatch) -> None:
    monkeypatch.setattr(compute, "validate_pair_eligibility", lambda a, b: "eligible")
    with pytest.raises(AssertionError):
        _check_f22()


# --- F-23 -------------------------------------------------------------------------------------

@_check
def _check_f23() -> None:
    a, b = _party(UUID_1, GATES_A), _party(UUID_1, GATES_B)
    try:
        compute.evaluate_pair(a, b, router=_stub_router)
    except CompatBoundaryError as exc:
        assert exc.reason == "inconsistent_self"
        assert exc.reader_token == "ERR_READER_INVALID_CHART"
    else:
        raise AssertionError("same identity with unequal projections was evaluated")


def test_f23_same_identity_unequal_projection_is_refused() -> None:
    _check_f23()


def test_f23_mutation_inconsistent_self_treated_as_self_is_refused(monkeypatch) -> None:
    monkeypatch.setattr(compute, "validate_pair_eligibility", lambda a, b: "ineligible_self")
    with pytest.raises(AssertionError):
        _check_f23()


# --- F-24, fingerprint part --------------------------------------------------------------------

@_check
def _check_f24() -> None:
    a, b = _party(UUID_1, GATES_A), _party(UUID_2, GATES_A)
    c, d = _party(UUID_3, GATES_A), _party(UUID_4, GATES_A)
    assert a.chart_fingerprint == b.chart_fingerprint == c.chart_fingerprint == d.chart_fingerprint
    first = compute.evaluate_pair(a, b, router=_stub_router)
    second = compute.evaluate_pair(c, d, router=_stub_router)
    assert first["pair_key"] == second["pair_key"]
    assert sercanon(first) == sercanon(second)


def test_f24_equal_masks_of_distinct_people_share_one_identity_free_pair_key() -> None:
    _check_f24()


def test_f24_mutation_identity_in_the_pair_preimage_is_refused(monkeypatch) -> None:
    original = compute.intrinsic_pair_key

    def with_identity(lo, hi, *, config_id, release_id):
        return original(lo, hi, config_id=f"{config_id}:{lo.canonical_person_id}", release_id=release_id)

    monkeypatch.setattr(compute, "intrinsic_pair_key", with_identity)
    with pytest.raises(AssertionError) as refused:
        _check_f24()
    # The product refuses the mutated rule: evaluate_pair's fail-closed pair_key guard.
    cause = refused.value.__cause__
    assert isinstance(cause, CompatBoundaryError) and (cause.reason, cause.detail) == ("result_schema", "pair_key")


# --- F-25 -------------------------------------------------------------------------------------

@_check
def _check_f25() -> None:
    a, b = _party(UUID_2, GATES_A), _party(UUID_1, GATES_A)
    for first, second in ((a, b), (b, a)):
        lo, hi = compute.orient(first, second)
        assert (lo.canonical_person_id, hi.canonical_person_id) == (UUID_1, UUID_2)
        carrier = compute.conjunction_public(first, second, router=_stub_router)["conjunction"]
        assert (carrier["left"], carrier["right"]) == ({"person_uid": UUID_1}, {"person_uid": UUID_2})
    forward = compute.conjunction_public(a, b, router=_stub_router)
    backward = compute.conjunction_public(b, a, router=_stub_router)
    assert sercanon(forward) == sercanon(backward)


def test_f25_equal_mask_orientation_by_uuid_tie_break() -> None:
    _check_f25()


def test_f25_mutation_request_order_kept_on_a_tie_is_refused(monkeypatch) -> None:
    original = compute.orient

    def request_order(a, b):
        return (a, b) if a.gates.mask == b.gates.mask else original(a, b)

    monkeypatch.setattr(compute, "orient", request_order)
    with pytest.raises(AssertionError):
        _check_f25()


# --- F-26 -------------------------------------------------------------------------------------

def _reader(eligible: bool, release_id: str, harmony_band: str | None = None):
    return public.emit_reader_public_envelope(eligible=eligible, harmony_band=harmony_band, release_id=release_id, **META)


@_check
def _check_f26() -> None:
    release_id = load_active_mechanics_bundle().release_id
    self_pair = compute.evaluate_pair(_party(UUID_1, GATES_A), _party(UUID_1, GATES_A))
    assert compute.is_ineligible_carrier(self_pair)
    eligible = compute.evaluate_pair(_party(UUID_1, GATES_A), _party(UUID_2, GATES_A))
    band = compute.harmony_band(eligible)
    raw_self, envelope_self = _reader(False, release_id)
    raw_pair, envelope_pair = _reader(True, release_id, band)
    assert raw_self != raw_pair
    assert envelope_self["idempotence_hash"] != envelope_pair["idempotence_hash"]
    assert _reader(False, release_id) == (raw_self, envelope_self)
    assert _reader(True, release_id, band) == (raw_pair, envelope_pair)
    assert envelope_self["meta"] == envelope_pair["meta"] and envelope_self["release_id"] == envelope_pair["release_id"]


def test_f26_self_pair_and_equal_mask_pair_never_share_public_bytes() -> None:
    _check_f26()


def test_f26_mutation_eligibility_outside_the_preimage_is_refused(monkeypatch) -> None:
    original = public._build_enriched_envelope
    monkeypatch.setattr(
        public, "_build_enriched_envelope", lambda **kwargs: original(**{**kwargs, "eligible": False, "categories": []})
    )
    with pytest.raises(AssertionError):
        _check_f26()


# --- F-27 -------------------------------------------------------------------------------------

def _write(path: Path, value: object) -> str:
    path.write_text(json.dumps(value), encoding="utf-8")
    return str(path)


@_check
def _check_f27(tmp_path: Path, capsys) -> None:
    chart_a, chart_b = _chart(UUID_1, GATES_A), _chart(UUID_2, GATES_B)
    direct = compute.evaluate_pair(_party(UUID_1, GATES_A), _party(UUID_2, GATES_B))
    expected = json.loads(sercanon(direct, sort_keys=True))
    path_a, path_b = _write(tmp_path / "a.json", chart_a), _write(tmp_path / "b.json", chart_b)
    outputs = []
    for args in (["--a-file", path_a, "--b-file", path_b], ["--a-file", path_b, "--b-file", path_a]):
        capsys.readouterr()
        assert cli(["showcompat", *args]) == 0
        outputs.append(capsys.readouterr().out)
    assert outputs[0] == outputs[1]
    assert json.loads(outputs[0]) == expected
    client = create_app().test_client()
    for body in ({"a": chart_a, "b": chart_b}, {"a": chart_b, "b": chart_a}):
        response = _post(client, body)
        assert response.status_code == 200
        assert response.get_json() == expected
    reader_path = tmp_path / "reader.bin"
    capsys.readouterr()
    assert cli(["showcompat", "--a-file", path_a, "--b-file", path_b, "--dump-reader", str(reader_path)]) == 0
    capsys.readouterr()
    dumped = reader_path.read_bytes()
    decoded = json.loads(dumped)
    emitted = public.emit_reader_public_bytes(
        eligible=True, harmony_band=compute.harmony_band(direct), release_id=decoded["release_id"], **decoded["meta"]
    )
    assert dumped == emitted
    assert decoded["release_id"] == load_active_mechanics_bundle().release_id


def test_f27_cli_internal_http_compat_and_reader_parity(tmp_path, capsys) -> None:
    _check_f27(tmp_path, capsys)


def test_f27_mutation_one_surface_diverges_is_refused(tmp_path, capsys, monkeypatch) -> None:
    from engine.http import compat_handler

    original = compat_handler.evaluate_pair

    def diverging(*args, **kwargs):
        result = dict(original(*args, **kwargs))
        result["signals"] = list(result["signals"])[1:]
        return result

    monkeypatch.setattr(compat_handler, "evaluate_pair", diverging)
    with pytest.raises(AssertionError):
        _check_f27(tmp_path, capsys)


# --- F-28 -------------------------------------------------------------------------------------

TOKEN_MAP = ROOT / "errors" / "token_map" / "token_map.json"


@_check
def _check_f28_mapping() -> None:
    governed = {row["code"] for row in json.loads(TOKEN_MAP.read_bytes())}
    for reason, (token, reader_token, reader_status) in BOUNDARY_REASONS.items():
        assert token in governed and token in error_tokens.ERROR_TOKEN_MAP, reason
        assert reader_token in governed and reader_token in error_tokens.ERROR_TOKEN_MAP, reason
        assert reader_status == MAGIC10_HTTP_STATUS[reader_token], reason


SURFACE_REFUSALS = {
    # reason: (party A chart, party B chart)
    "inconsistent_self": (_chart(UUID_1, GATES_A), _chart(UUID_1, GATES_B)),
    "gates_invalid": (_chart(UUID_1, [0, 8]), _chart(UUID_2, GATES_B)),
    "gates_missing": (_chart(UUID_1, []), _chart(UUID_2, GATES_B)),
}


@_check
def _check_f28_surfaces(tmp_path: Path, capsys) -> None:
    client = create_app().test_client()
    for reason, (chart_a, chart_b) in SURFACE_REFUSALS.items():
        token = BOUNDARY_REASONS[reason][0]
        path_a = _write(tmp_path / f"{reason}-a.json", chart_a)
        path_b = _write(tmp_path / f"{reason}-b.json", chart_b)
        capsys.readouterr()
        assert cli(["showcompat", "--a-file", path_a, "--b-file", path_b]) == 1, reason
        captured = capsys.readouterr()
        assert (captured.out, captured.err) == ("", f"{token}\n"), reason
        body = {"a": chart_a, "b": chart_b}
        response = _post(client, body)
        assert response.status_code == MAGIC10_HTTP_STATUS.get(token, 422), reason
        assert token in response.get_data(as_text=True), reason


def test_f28_token_and_status_mapping_agree() -> None:
    _check_f28_mapping()


def test_f28_surfaces_emit_the_mapped_token_and_status(tmp_path, capsys) -> None:
    _check_f28_surfaces(tmp_path, capsys)


def test_f28_mutation_reader_status_out_of_mapping_is_refused(monkeypatch) -> None:
    token, reader_token, _status = BOUNDARY_REASONS["inconsistent_self"]
    monkeypatch.setitem(BOUNDARY_REASONS, "inconsistent_self", (token, reader_token, 503))
    with pytest.raises(AssertionError):
        _check_f28_mapping()


def test_f28_mutation_http_status_out_of_mapping_is_refused(tmp_path, capsys, monkeypatch) -> None:
    from engine.http import compat_handler

    monkeypatch.setattr(compat_handler, "_boundary_status", lambda exc: 500)
    with pytest.raises(AssertionError):
        _check_f28_surfaces(tmp_path, capsys)
