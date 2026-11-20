"""Owner tests of the Magic-10 v2 typed-bundle evidence writer (HDE-EPIC043 WU-PR-11).

Every case reads the repository's real inputs and writes only to a temporary record path.
Inputs are changed through the writer's one read seam, and the two ``--check`` commands
through its one command seam, except where a case exercises them for real.
"""
from __future__ import annotations

import json

import pytest

from engine.runtime.determinism_env import DETERMINISM_ENV_PINS
from tools.evidence import generate_hde_epic043_v2_bundle_evidence as writer

ACTOR = "test actor"


@pytest.fixture(autouse=True)
def _closed_rails(monkeypatch: pytest.MonkeyPatch) -> None:
    for key, value in DETERMINISM_ENV_PINS.items():
        monkeypatch.setenv(key, value)


@pytest.fixture
def record(tmp_path, monkeypatch):
    out = tmp_path / "v2_bundle_evidence.txt"
    monkeypatch.setattr(writer, "out_path", lambda: out)
    monkeypatch.setattr(writer, "run_check_command", lambda command: 0)
    return out


def _with_input(monkeypatch, rel: str, data: bytes) -> None:
    real = writer.read_input
    monkeypatch.setattr(writer, "read_input", lambda name: data if name == rel else real(name))


def _bundle_with(rel: str, mutate) -> bytes:
    payload = json.loads((writer.ROOT / rel).read_bytes())
    mutate(payload)
    return (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def _refused(code_prefix: str):
    return pytest.raises(writer.BundleEvidenceRefusal, match=f"^{code_prefix}")


def test_the_committed_record_passes_check_with_the_real_commands() -> None:
    writer.check()
    stored = writer.out_path().read_bytes().decode("utf-8")
    assert stored.splitlines()[0] == f"schema: {writer.SCHEMA}"
    assert stored.endswith("status: PASS\n")


def test_write_then_check_is_byte_stable_apart_from_the_run_fields(record) -> None:
    first = writer.write(ACTOR)
    writer.check()
    second = writer.write(ACTOR)
    writer.check()
    strip = lambda data: [line for line in data.decode("utf-8").splitlines() if not line.startswith("run.time_utc: ")]
    assert strip(first) == strip(second)
    lines = dict(line.split(": ", 1) for line in first.decode("utf-8").splitlines())
    assert lines["run.actor"] == ACTOR
    assert lines["tested_inputs.count"] == str(len(writer.TESTED_INPUTS))
    for category in ("harmony", "balance"):
        assert lines[f"category.{category}.be_maxima"] == lines[f"category.{category}.thresholds_maxima"]
        assert lines[f"category.{category}.fe_maxima"] == lines[f"category.{category}.thresholds_maxima"]


def test_check_refuses_a_missing_record(record) -> None:
    with pytest.raises(SystemExit, match=f"^DRIFT:{writer.OUT_REL}:missing$"):
        writer.check()


def test_a_changed_tested_input_is_drift(record, monkeypatch) -> None:
    writer.write(ACTOR)
    builder = (writer.ROOT / writer.BUILDER_REL).read_bytes()
    _with_input(monkeypatch, writer.BUILDER_REL, builder + b"\n")
    with pytest.raises(SystemExit, match=f"^DRIFT:{writer.OUT_REL}:input.{writer.BUILDER_REL}.sha256$"):
        writer.check()


@pytest.mark.parametrize(
    ("field", "value"),
    [("run.time_utc", "2026-11-20 05:00:00"), ("run.actor", " padded"), ("run.python", "three")],
)
def test_a_malformed_run_field_is_drift(record, field, value) -> None:
    lines = writer.write(ACTOR).decode("utf-8").splitlines()
    record.write_text("\n".join(f"{field}: {value}" if line.startswith(f"{field}: ") else line for line in lines) + "\n")
    with pytest.raises(SystemExit, match=f"^DRIFT:{writer.OUT_REL}:{field}$"):
        writer.check()


def test_an_edited_reproducible_line_is_drift(record) -> None:
    data = writer.write(ACTOR).decode("utf-8")
    record.write_text(data.replace("category.harmony.equal: true", "category.harmony.equal: false"))
    with pytest.raises(SystemExit, match=f"^DRIFT:{writer.OUT_REL}:category.harmony.equal$"):
        writer.check()


@pytest.mark.parametrize("actor", ["", " leading", "line\nbreak", "x" * 201])
def test_an_invalid_actor_is_refused_and_nothing_is_written(record, actor) -> None:
    with _refused(writer.INVALID_ACTOR):
        writer.write(actor)
    assert not record.exists()


def test_open_rails_are_refused(record, monkeypatch) -> None:
    monkeypatch.setenv("ALLOW_NETWORK", "1")
    with _refused(writer.RAILS_NOT_CLOSED):
        writer.write(ACTOR)
    assert not record.exists()


def test_a_bundle_the_schema_refuses_is_refused(record, monkeypatch) -> None:
    rel = writer.BUNDLES["fe"][0]
    _with_input(monkeypatch, rel, _bundle_with(rel, lambda payload: payload["bands"].__setitem__("edges", [24, 49, 74, 100])))
    with _refused(f"{writer.SCHEMA_REFUSED}:{writer.BUNDLES['fe'][1]}"):
        writer.write(ACTOR)
    assert not record.exists()


def test_bundle_maxima_that_differ_from_the_thresholds_are_refused(record, monkeypatch) -> None:
    rel = writer.BUNDLES["fe"][0]
    _with_input(monkeypatch, rel, _bundle_with(
        rel, lambda payload: payload["bands"]["categories"][0].__setitem__("maxima", [20, 40, 60, 100])))
    with _refused(f"{writer.MAXIMA_MISMATCH}:fe:harmony"):
        writer.write(ACTOR)
    assert not record.exists()


def test_a_stale_band_edges_binding_is_refused(record, monkeypatch) -> None:
    edges = (writer.ROOT / writer.BAND_EDGES_REL).read_bytes()
    _with_input(monkeypatch, writer.BAND_EDGES_REL, edges.replace(b"[35,44,53,100]", b"[34,44,53,100]", 1))
    with _refused(f"{writer.SOURCES_MISMATCH}:be"):
        writer.write(ACTOR)
    assert not record.exists()


def test_a_failing_check_command_is_refused(record, monkeypatch) -> None:
    monkeypatch.setattr(writer, "run_check_command", lambda command: 1 if command[0].endswith("generate_bundles.py") else 0)
    with _refused(f"{writer.CHECK_COMMAND_FAILED}:tools/config/generate_bundles.py"):
        writer.write(ACTOR)
    assert not record.exists()
