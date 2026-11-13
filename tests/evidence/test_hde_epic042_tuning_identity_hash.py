"""Owner test of the HDE-EPIC042 WU-PR-01 real-path tuning-run identity generator.

The admitted repository root is used as it is: the real admission owner, the
two complete fixture charts and the real compat path.  Differing bodies are
supplied through the generator's ``overrides`` build seam to prove the record
can fail (AC-01).  The non-admitted branch is reached through the evaluation
provider seam with the refusal code the admission owner emits, as stage 04's
owner test does.  Nothing is written under the repository tree.
"""
from __future__ import annotations

import ast
import hashlib
import io
import json
import os
import sys
from pathlib import Path

import pytest

from engine.cli.main import cli
from engine.compat import compute
from engine.compat.compute import evaluate_pair, evaluation_party
from engine.config.registry_loader import SchemaValidationError, load_active_mechanics_bundle
from engine.presenter import emitter
from engine.serializer import canon
from tools.evidence import generate_hde_epic042_tuning_identity_hash as g
from tools.evidence import run_sanity_pipeline as release_sanity

ROOT = Path(__file__).resolve().parents[2]
CLOSED_RAILS = {"LC_ALL": "C", "LANG": "C", "TZ": "UTC", "SAFE_MODE": "1", "ALLOW_NETWORK": "0"}
COMPAT_DIR = (ROOT / "artifacts" / "compat").resolve()
EXPECTED_KEYS = [
    "schema",
    "epic_id",
    "task_id",
    "subtask_id",
    "work_unit_id",
    "hash_basis",
    "canonical_form",
    "excluded_sources",
    "release_id",
    "config_id",
    "compat_schema",
    "corpus",
    "pair_count",
    "pair.1.a",
    "pair.1.b",
    "pair.1.pair_key",
    "pair.1.body_size_bytes",
    "pair.1.run.ab.source",
    "pair.1.run.ab.sha256",
    "pair.1.run.ba.source",
    "pair.1.run.ba.sha256",
    "pair.1.run.ab_repeat.source",
    "pair.1.run.ab_repeat.sha256",
    "pair.1.run.cli.source",
    "pair.1.run.cli.sha256",
    "pair.1.canonical_form_ok",
    "pair.1.ab_ba_equal",
    "pair.1.two_run_equal",
    "pair.1.cli_parity_equal",
    "status",
]

# One process-wide audit hook; it records only while a test sets the flag.
_OPENED: list[object] = []
_RECORDING = {"on": False}


def _audit(event: str, args: tuple) -> None:
    if _RECORDING["on"] and event == "open" and args:
        _OPENED.append(args[0])


sys.addaudithook(_audit)


def _parse(record: bytes) -> dict[str, str]:
    text = record.decode("utf-8")
    assert text.endswith("\n") and not text.endswith("\n\n")
    pairs = [line.split(": ", 1) for line in text.splitlines()]
    assert all(len(pair) == 2 for pair in pairs)
    keys = [key for key, _ in pairs]
    assert len(keys) == len(set(keys))
    return dict(pairs)


def _keys(record: bytes) -> list[str]:
    return [line.split(": ", 1)[0] for line in record.decode("utf-8").splitlines()]


@pytest.fixture
def rails(monkeypatch):
    for name, value in CLOSED_RAILS.items():
        monkeypatch.setenv(name, value)


@pytest.fixture
def out(monkeypatch, tmp_path):
    path = tmp_path / "audit" / "qa" / "hde-epic042" / "pr-01" / "tuning_identity_hash.txt"
    monkeypatch.setattr(g, "OUT", path)
    return path


def _left_right():
    a_rel, b_rel = g.CORPUS[0]
    return g.load_party(a_rel), g.load_party(b_rel)


def _real_body(left, right) -> bytes:
    """An independent recomputation of the compat body for one order."""

    def party(chart, label):
        from engine.cli import main as cli_main

        return evaluation_party(cli_main._resolve_party(cli_main._normalize_party(dict(chart), label), source_policy="local"))

    return emitter.emit_public(evaluate_pair(party(left, "left"), party(right, "right")))


def _differing_canonical_body() -> bytes:
    """The real AB body with one category's band changed, still canonical."""

    left, right = _left_right()
    parsed = json.loads(_real_body(left, right))
    first = parsed["categories"][0]
    first["band"] = "Glow" if first["band"] != "Glow" else "Cool"
    body = canon.sercanon(parsed)
    assert g.canonical_ok(body)
    return body


def _in_process_cli_body(a_rel: str, b_rel: str) -> bytes:
    """The CLI file path in process, so the audit hook observes it too."""

    buffer = io.BytesIO()
    wrapper = io.TextIOWrapper(buffer, encoding="utf-8")
    previous = sys.stdout
    sys.stdout = wrapper
    try:
        code = cli(["showcompat", "--a-file", str(ROOT / a_rel), "--b-file", str(ROOT / b_rel)])
        wrapper.flush()
    finally:
        sys.stdout = previous
    assert code == 0
    return buffer.getvalue()


# --- positive matrix on the admitted repository root -----------------------------------------

def test_check_passes_on_the_admitted_root_and_writes_nothing(rails, capsys):
    committed = g.OUT.read_bytes()
    g.main(["--check"])
    assert capsys.readouterr().out == "tuning identity hash check ok\n"
    assert g.OUT.read_bytes() == committed


def test_record_hashes_the_real_compat_body_of_every_run(rails):
    passed, record = g.build()
    assert passed
    fields = _parse(record)
    bundle = load_active_mechanics_bundle()
    assert fields["release_id"] == bundle.release_id
    assert fields["config_id"] == bundle.mechanics["config_id"]
    assert fields["compat_schema"] == "magic10_compat_result.v1"
    assert fields["hash_basis"] == g.HASH_BASIS
    assert fields["excluded_sources"] == "artifacts/compat/AB.json, artifacts/compat/BA.json"
    left, right = _left_right()
    ab, ba = _real_body(left, right), _real_body(right, left)
    assert fields["pair.1.run.ab.sha256"] == hashlib.sha256(ab).hexdigest()
    assert fields["pair.1.run.ba.sha256"] == hashlib.sha256(ba).hexdigest()
    assert fields["pair.1.run.ab_repeat.sha256"] == hashlib.sha256(ab).hexdigest()
    assert fields["pair.1.run.cli.sha256"] == hashlib.sha256(ab).hexdigest()
    assert fields["pair.1.body_size_bytes"] == str(len(ab))
    assert fields["pair.1.pair_key"] == json.loads(ab)["pair_key"]
    for key in ("canonical_form_ok", "ab_ba_equal", "two_run_equal", "cli_parity_equal"):
        assert fields[f"pair.1.{key}"] == "true"
    assert fields["status"] == "PASS"


def test_write_mode_is_deterministic_and_equals_the_committed_proof(rails, out):
    g.main([])
    first = out.read_bytes()
    g.main([])
    assert out.read_bytes() == first
    assert first == (ROOT / g.OUT_REL).read_bytes()


def test_record_layout_is_closed_and_carries_no_time_field(rails):
    _passed, record = g.build()
    assert _keys(record) == EXPECTED_KEYS
    assert not any("time" in key or "date" in key or key.endswith("_at") for key in _keys(record))


# --- the proof can fail (AC-01) --------------------------------------------------------------

@pytest.mark.parametrize(
    ("run_id", "predicate"),
    [("ba", "ab_ba_equal"), ("ab_repeat", "two_run_equal"), ("cli", "cli_parity_equal")],
)
def test_a_differing_body_fails_the_record(rails, run_id, predicate):
    passed, record = g.build(overrides={run_id: _differing_canonical_body()})
    fields = _parse(record)
    assert not passed
    assert fields["status"] == "FAIL"
    assert fields[f"pair.1.{predicate}"] == "false"
    assert fields["pair.1.canonical_form_ok"] == "true"


@pytest.mark.parametrize("mutation", ["crlf", "no_final_lf"])
def test_a_non_canonical_body_fails_the_record(rails, mutation):
    left, right = _left_right()
    ab = _real_body(left, right)
    body = ab[:-1] + b"\r\n" if mutation == "crlf" else ab[:-1]
    passed, record = g.build(overrides={"ab_repeat": body})
    fields = _parse(record)
    assert not passed
    assert fields["pair.1.canonical_form_ok"] == "false"
    assert fields["status"] == "FAIL"


def test_write_mode_refuses_a_failing_record_and_writes_nothing(rails, out, monkeypatch, tmp_path):
    real_build = g.build
    monkeypatch.setattr(g, "build", lambda: real_build(overrides={"ba": _differing_canonical_body()}))
    with pytest.raises(SystemExit) as excinfo:
        g.main([])
    assert excinfo.value.code == "TUNING_IDENTITY_FAILED"
    assert not out.exists()
    assert list(tmp_path.iterdir()) == []


# --- placeholder captures are never a source -------------------------------------------------

def test_the_generator_opens_nothing_under_artifacts_compat(rails, monkeypatch):
    monkeypatch.setattr(g, "cli_body", _in_process_cli_body)
    _OPENED.clear()
    _RECORDING["on"] = True
    try:
        passed, _record = g.build()
    finally:
        _RECORDING["on"] = False
    assert passed
    opened = []
    for target in _OPENED:
        if isinstance(target, int):
            continue
        raw = os.fsdecode(target)
        opened.append(Path(raw if os.path.isabs(raw) else ROOT / raw).resolve())
    assert opened, "the audit hook observed no open event"
    assert not [path for path in opened if path == COMPAT_DIR or COMPAT_DIR in path.parents]
    assert _compat_path_literals() == []


def _compat_path_literals() -> list[str]:
    """String constants naming artifacts/compat, outside the docstring and EXCLUDED_SOURCES."""

    tree = ast.parse(Path(g.__file__).read_text(encoding="utf-8"))
    allowed: set[int] = {id(tree.body[0].value)}  # the module docstring
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "EXCLUDED_SOURCES" for target in node.targets
        ):
            allowed.update(id(child) for child in ast.walk(node.value))
    return [
        node.value
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant)
        and isinstance(node.value, str)
        and "artifacts/compat" in node.value
        and id(node) not in allowed
    ]


# --- release not admitted --------------------------------------------------------------------

def _refuse_admission(monkeypatch, code="INCOMPLETE_RELEASE_ROSTER"):
    def refuse():
        raise SchemaValidationError(code, "patched provider")

    monkeypatch.setattr(compute, "_BUNDLE_PROVIDER", refuse)


def _forbid_live_capture(monkeypatch):
    monkeypatch.setattr(g, "compat_body", lambda *a, **k: pytest.fail("compat body computed"))
    monkeypatch.setattr(g, "cli_body", lambda *a, **k: pytest.fail("CLI run attempted"))
    monkeypatch.setattr(g.subprocess, "run", lambda *a, **k: pytest.fail("subprocess spawned"))


@pytest.mark.parametrize("argv", [["--check"], []])
def test_not_admitted_prints_refusal_exits_three_and_writes_nothing(rails, out, monkeypatch, tmp_path, capsys, argv):
    _refuse_admission(monkeypatch)
    _forbid_live_capture(monkeypatch)
    with pytest.raises(SystemExit) as excinfo:
        g.main(argv)
    assert excinfo.value.code == release_sanity.RELEASE_NOT_ADMITTED_EXIT_CODE == 3
    assert capsys.readouterr().out == "HDE_EPIC042_TUNING_IDENTITY_CHECK:RELEASE_NOT_ADMITTED\n"
    assert list(tmp_path.iterdir()) == []


def test_other_admission_refusals_propagate(rails, monkeypatch):
    _refuse_admission(monkeypatch, code="SCHEMA_INVALID")
    _forbid_live_capture(monkeypatch)
    with pytest.raises(SchemaValidationError, match="patched provider"):
        g.build()


# --- --check reports drift -------------------------------------------------------------------

def test_check_fails_when_the_stored_proof_differs(rails, out):
    committed = (ROOT / g.OUT_REL).read_bytes()
    marker = b"pair.1.run.ab.sha256: "
    start = committed.index(marker) + len(marker)
    flipped = b"0" if committed[start:start + 1] != b"0" else b"1"
    out.parent.mkdir(parents=True)
    out.write_bytes(committed[:start] + flipped + committed[start + 1:])
    with pytest.raises(SystemExit) as excinfo:
        g.main(["--check"])
    assert str(excinfo.value.code).startswith("DRIFT:")


def test_check_fails_when_the_stored_proof_is_missing(rails, out):
    with pytest.raises(SystemExit) as excinfo:
        g.main(["--check"])
    assert str(excinfo.value.code).startswith("DRIFT:")
    assert not out.exists()
