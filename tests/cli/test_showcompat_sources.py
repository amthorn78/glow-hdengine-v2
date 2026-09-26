"""Source-selection and prohibited-side-effect matrix for ``hdctl showcompat`` (PR04 proof class 5)."""
from __future__ import annotations

import json

import pytest

from engine.cli import main as cli_main
from engine.cli.main import cli
from engine.compat import compute
from engine.bodygraph import ingest as ingest_module
from engine.bodygraph.ingest import resolve_db_user_id
from engine.bodygraph.vendor_client import VendorRequest, VendorResult
from engine.db.errors import AdapterError
from engine.serializer.canon import sercanon
from tests.support.pr04_fixtures import (
    GATES_A,
    GATES_B,
    UUID_A,
    UUID_B,
    FakeCurrentViewDB,
    build_bundle,
    build_pack,
    complete_chart,
    inject_seams,
)

VENDOR_CHART = json.loads(open("tests/fixtures/bodygraph/source_invariance/vendor_chart_result.v1.json", encoding="utf-8").read())["payload"]
BIRTH_ARGS = [
    "--birthdate-a", "1990-01-01", "--birthtime-a", "12:00", "--location-a", "Amsterdam",
    "--birthdate-b", "1991-02-02", "--birthtime-b", "13:00", "--location-b", "Berlin",
]


@pytest.fixture(scope="module")
def bundle(tmp_path_factory):
    return build_bundle(tmp_path_factory.mktemp("pr04-sources-bundle"))


@pytest.fixture(scope="module")
def pack(tmp_path_factory):
    return build_pack(tmp_path_factory.mktemp("pr04-sources-pack"))


@pytest.fixture(autouse=True)
def _seams(monkeypatch, bundle, pack):
    inject_seams(monkeypatch, bundle, pack)
    for name in ("HD_API_BASE_URL", "HDAPI_BASE_URL", "HD_API_KEY", "GEO_API_KEY", "DATABASE_URL", "HDE_FORCE_DB_UNAVAILABLE"):
        monkeypatch.delenv(name, raising=False)


@pytest.fixture
def spies(monkeypatch):
    calls = {"vendor": 0, "ingest": 0, "persist": 0}
    monkeypatch.setattr("engine.bodygraph.resolver.HdApiClient.from_env", lambda **kwargs: calls.__setitem__("vendor", calls["vendor"] + 1) or pytest.fail("vendor client constructed"))
    monkeypatch.setattr("engine.bodygraph.resolver.ingest_vendor_bodygraph", lambda *a, **k: calls.__setitem__("ingest", calls["ingest"] + 1) or pytest.fail("ingest attempted"))
    monkeypatch.setattr("engine.bodygraph.resolver.persist_mapped_bodygraph", lambda *a, **k: calls.__setitem__("persist", calls["persist"] + 1) or pytest.fail("mapped-cache write attempted"))
    monkeypatch.setattr(ingest_module, "_append_jsonl", lambda path, record: pytest.fail("value log written"))
    return calls


def _install_db(monkeypatch, charts=None, *, fail=None):
    db = FakeCurrentViewDB(charts, fail=fail)
    monkeypatch.setattr("engine.cli.main.DBAccess.for_current_env", lambda *a, **k: db)
    return db


def _user_charts():
    key_1 = resolve_db_user_id("user-1")
    key_2 = resolve_db_user_id("user-2")
    return {key_1: complete_chart(f"person-{key_1}", GATES_A), key_2: complete_chart(f"person-{key_2}", GATES_B)}


def _result(captured):
    payload = json.loads(captured.out)
    assert sercanon(payload).decode("utf-8") == captured.out
    return payload


def test_showcompat_db_source_reads_current_rows_only(monkeypatch, capsys, spies):
    db = _install_db(monkeypatch, _user_charts())
    exit_code = cli(["showcompat", "--source", "db", "--user-a", "user-1", "--user-b", "user-2"])
    captured = capsys.readouterr()
    assert exit_code == 0, captured.err
    assert captured.err == ""
    payload = _result(captured)
    assert payload["schema"] == "magic10_compat_result.v1"
    assert set(payload) == {"schema", "config_id", "release_id", "pair_key", "signals", "categories"}
    assert len(payload["categories"]) == 10
    assert {params[0] for _sql, params in db.queries} == set(_user_charts())
    for sql, _params in db.queries:
        assert "public.hde_body_graphs_current" in sql and "vendor = 'hdapi'" in sql
        assert not any(verb in sql.upper() for verb in ("INSERT", "UPDATE", "DELETE", "CALL"))
    assert db.writes == [] and spies == {"vendor": 0, "ingest": 0, "persist": 0}


def test_showcompat_db_source_ab_ba_and_two_run_identity(monkeypatch, capsys, spies):
    _install_db(monkeypatch, _user_charts())
    outputs = []
    for args in (["user-1", "user-2"], ["user-2", "user-1"], ["user-1", "user-2"]):
        assert cli(["showcompat", "--source", "db", "--user-a", args[0], "--user-b", args[1]]) == 0
        outputs.append(capsys.readouterr().out)
    assert outputs[0] == outputs[1] == outputs[2]


def test_showcompat_db_source_miss_is_missing_chart_without_vendor(monkeypatch, capsys, spies):
    _install_db(monkeypatch, {})
    exit_code = cli(["showcompat", "--source", "db", "--user-a", "user-1", "--user-b", "user-2"])
    captured = capsys.readouterr()
    assert exit_code == 64
    assert captured.out == ""
    assert captured.err == "BODYGRAPH_NOT_FOUND\n"


def test_showcompat_db_source_invalid_row_gates_refuse_before_evaluation(monkeypatch, capsys, spies):
    charts = _user_charts()
    key_1 = resolve_db_user_id("user-1")
    charts[key_1]["bodygraph"]["gates"] = ["10", "10"]
    db = _install_db(monkeypatch, charts)
    monkeypatch.setattr(compute, "compute_core", lambda *a, **k: pytest.fail("core reached"))
    exit_code = cli(["showcompat", "--source", "db", "--user-a", "user-1", "--user-b", "user-2"])
    captured = capsys.readouterr()
    assert exit_code == 1
    assert captured.out == ""
    assert captured.err == "ERR_READER_INVALID_CHART\n"
    db.charts[key_1]["bodygraph"]["gates"] = []
    exit_code = cli(["showcompat", "--source", "db", "--user-a", "user-1", "--user-b", "user-2"])
    captured = capsys.readouterr()
    assert exit_code == 1 and captured.err == "ERR_READER_MISSING_PARAM\n"


def test_showcompat_db_source_type_only_row_is_incomplete(monkeypatch, capsys, spies):
    key_1 = resolve_db_user_id("user-1")
    key_2 = resolve_db_user_id("user-2")
    db = FakeCurrentViewDB({key_2: complete_chart(f"person-{key_2}", GATES_B)})
    db.charts[key_1] = {"type": "Generator", "birth": {"date": "1990-01-01", "time": "12:00"}}
    monkeypatch.setattr("engine.cli.main.DBAccess.for_current_env", lambda *a, **k: db)
    exit_code = cli(["showcompat", "--source", "db", "--user-a", "user-1", "--user-b", "user-2"])
    captured = capsys.readouterr()
    assert exit_code == 1
    assert captured.out == ""
    assert captured.err == "ERR_READER_MISSING_PARAM\n"


def test_showcompat_auto_is_db_only_and_never_falls_back_to_vendor(monkeypatch, capsys, spies):
    _install_db(monkeypatch, _user_charts())
    assert cli(["showcompat", "--source", "auto", "--user-a", "user-1", "--user-b", "user-2"]) == 0
    assert _result(capsys.readouterr())["schema"] == "magic10_compat_result.v1"
    monkeypatch.setenv("SAFE_MODE", "0")
    monkeypatch.setenv("ALLOW_NETWORK", "1")
    exit_code = cli(["showcompat", "--source", "auto", *BIRTH_ARGS])
    captured = capsys.readouterr()
    assert exit_code == 64
    assert captured.out == ""
    assert captured.err == "AUTO_SOURCE_UNRESOLVED\n"
    assert spies["vendor"] == 0


def test_showcompat_vendor_closed_rails_refuses_before_any_io(monkeypatch, capsys, spies):
    monkeypatch.setattr("engine.cli.main.DBAccess.for_current_env", lambda *a, **k: pytest.fail("DB constructed"))
    exit_code = cli(["showcompat", "--source", "vendor", *BIRTH_ARGS])
    captured = capsys.readouterr()
    assert exit_code == 1
    assert captured.out == ""
    assert captured.err == "PROVIDER_REFUSED\n"
    assert spies["vendor"] == 0


def test_showcompat_vendor_dry_run_uses_the_v2_adapter_path_without_persistence(monkeypatch, capsys):
    monkeypatch.setenv("SAFE_MODE", "0")
    monkeypatch.setenv("ALLOW_NETWORK", "1")
    monkeypatch.setenv("APP_ENV", "test")
    monkeypatch.setenv("HD_API_BASE_URL", "https://vendor.test/v2")
    monkeypatch.setenv("HD_API_KEY", "set")
    monkeypatch.setenv("GEO_API_KEY", "set")
    fetches = []

    class FakeTransport:
        def build_contract_route_request(self, **kwargs):
            return VendorRequest(url="https://vendor.test/v2/charts", headers={}, body_bytes=json.dumps(kwargs, sort_keys=True).encode(), input_fingerprint="c" * 64, route="vendor.hdapi.post:/charts")

        def fetch(self, request):
            fetches.append(request)
            data = dict(VENDOR_CHART)
            data["gates"] = GATES_A if len(fetches) == 1 else GATES_B
            return VendorResult(payload={"timestamp": "2026-07-16T00:00:00Z", "success": True, "message": "Chart generated", "errorCode": "", "type": "ChartResult", "data": data}, duration_ms=1, attempts=1)

    monkeypatch.setattr("engine.bodygraph.resolver.HdApiClient.from_env", lambda **kwargs: FakeTransport())
    monkeypatch.setattr("engine.bodygraph.resolver.DBAccess.for_current_env", lambda **kwargs: pytest.fail("DB constructed"))
    monkeypatch.setattr("engine.cli.main.DBAccess.for_current_env", lambda **kwargs: pytest.fail("DB constructed"))
    monkeypatch.setattr("engine.bodygraph.resolver.persist_mapped_bodygraph", lambda *a, **k: pytest.fail("mapped-cache write attempted"))
    monkeypatch.setattr("engine.bodygraph.resolver.ingest_vendor_bodygraph", lambda *a, **k: pytest.fail("legacy ingest attempted"))
    monkeypatch.setattr(ingest_module, "_append_jsonl", lambda path, record: pytest.fail("value log written"))

    exit_code = cli(["showcompat", "--source", "vendor", *BIRTH_ARGS])
    captured = capsys.readouterr()
    assert exit_code == 0, captured.err
    payload = _result(captured)
    assert payload["schema"] == "magic10_compat_result.v1"
    assert len(fetches) == 2
    assert captured.err == ""
    assert "1990-01-01" not in captured.out and "Amsterdam" not in captured.out


def test_showcompat_file_input_with_label_and_no_trusted_context_refuses(monkeypatch, capsys, tmp_path, spies):
    monkeypatch.setattr("engine.cli.main.DBAccess.for_current_env", lambda *a, **k: pytest.fail("DB constructed"))
    left = complete_chart("person-alice", GATES_A)
    right = complete_chart(UUID_B, GATES_B)
    pair = tmp_path / "pair.json"
    pair.write_text(json.dumps({"left": left, "right": right}), encoding="utf-8")
    exit_code = cli(["showcompat", "--pair-file", str(pair)])
    captured = capsys.readouterr()
    assert exit_code == 1
    assert captured.out == ""
    assert captured.err == "ERR_READER_MISSING_PARAM\n"


def test_showcompat_file_input_complete_charts_use_no_db_or_vendor(monkeypatch, capsys, tmp_path, spies):
    monkeypatch.setattr("engine.cli.main.DBAccess.for_current_env", lambda *a, **k: pytest.fail("DB constructed"))
    pair = tmp_path / "pair.json"
    pair.write_text(json.dumps({"left": complete_chart(UUID_A, GATES_A), "right": complete_chart(UUID_B, GATES_B)}), encoding="utf-8")
    assert cli(["showcompat", "--pair-file", str(pair)]) == 0
    payload = _result(capsys.readouterr())
    assert payload["schema"] == "magic10_compat_result.v1"


def test_showcompat_self_pair_carrier_exit_zero(monkeypatch, capsys, tmp_path, spies):
    pair = tmp_path / "pair.json"
    pair.write_text(json.dumps({"left": complete_chart(UUID_A, GATES_A), "right": complete_chart(UUID_A, GATES_A)}), encoding="utf-8")
    monkeypatch.setattr(compute, "compute_core", lambda *a, **k: pytest.fail("core reached for a self-pair"))
    exit_code = cli(["showcompat", "--pair-file", str(pair)])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out == '{"categories":[],"eligible":false}\n'
    assert captured.err == ""


def test_showcompat_conjunction_surfaces_db_query_failed(monkeypatch, capsys, spies):
    _install_db(monkeypatch, {}, fail=AdapterError("db down"))
    exit_code = cli(["showcompat", "--conjunction", "--user-a", "user-1", "--user-b", "user-2"])
    captured = capsys.readouterr()
    assert exit_code == 64
    assert captured.out == ""
    assert captured.err == "DB_QUERY_FAILED\n"


def test_showcompat_conjunction_surfaces_invalid_bodygraph_payload(monkeypatch, capsys, spies):
    class _DB:
        def query(self, sql: str, params):
            return [(params[0], "hdapi", 2, "a" * 64, "{bad")]

    monkeypatch.setattr("engine.cli.main.DBAccess.for_current_env", lambda *a, **k: _DB())
    exit_code = cli(["showcompat", "--conjunction", "--user-a", "user-1", "--user-b", "user-2"])
    captured = capsys.readouterr()
    assert exit_code == 64
    assert captured.out == ""
    assert captured.err == "INVALID_BODYGRAPH_PAYLOAD\n"


def test_showcompat_conjunction_local_first_hit_needs_no_vendor(monkeypatch, capsys, spies):
    _install_db(monkeypatch, _user_charts())
    exit_code = cli(["showcompat", "--conjunction", "--user-a", "user-1", "--user-b", "user-2"])
    captured = capsys.readouterr()
    assert exit_code == 0, captured.err
    payload = _result(captured)
    assert set(payload["conjunction"]) == {"left", "right", "compat"}
    assert {payload["conjunction"]["left"]["person_uid"], payload["conjunction"]["right"]["person_uid"]} == set(_user_charts())
    assert payload["conjunction"]["compat"]["schema"] == "magic10_compat_result.v1"


def test_showcompat_conjunction_db_source_miss_is_missing_chart_not_refusal(monkeypatch, capsys, spies):
    _install_db(monkeypatch, {})
    exit_code = cli(["showcompat", "--conjunction", "--source", "db", "--user-a", "user-1", "--user-b", "user-2"])
    captured = capsys.readouterr()
    assert exit_code == 1
    assert captured.out == ""
    assert captured.err == "ERR_NOT_FOUND\n"


def test_showcompat_refuses_without_an_admitted_release(monkeypatch, capsys, tmp_path, spies):
    from engine.config.registry_loader import SchemaValidationError
    from engine.runtime.identity import identity_meta

    def refuse():
        raise SchemaValidationError("INCOMPLETE_RELEASE_ROSTER", "patched provider")

    monkeypatch.setattr(compute, "_BUNDLE_PROVIDER", refuse)
    pair = tmp_path / "pair.json"
    pair.write_text(json.dumps({"left": complete_chart(UUID_A, GATES_A), "right": complete_chart(UUID_B, GATES_B)}), encoding="utf-8")
    exit_code = cli(["showcompat", "--pair-file", str(pair)])
    captured = capsys.readouterr()
    assert exit_code == 1
    assert captured.out == ""
    assert captured.err == "INCOMPLETE_RELEASE_ROSTER\n"
    # The real admission owner admits the repository root: the same pair evaluates.
    monkeypatch.setattr(compute, "_BUNDLE_PROVIDER", compute.load_active_mechanics_bundle)
    assert cli(["showcompat", "--pair-file", str(pair)]) == 0
    captured = capsys.readouterr()
    assert captured.err == ""
    assert captured.out.endswith("\n")
    assert json.loads(captured.out)["release_id"] == identity_meta()["release_id"]


def test_legacy_helpers_are_gone_from_the_cli():
    for name in ("_derive_uid", "_chart_for", "_canonical_pair", "compat_public", "ts_v0"):
        assert not hasattr(cli_main, name), name
