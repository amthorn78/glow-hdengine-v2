"""Owner tests of the Magic-10 v2 integration evidence writer (HDE-EPIC043 WU-PR-12; HDE-CONJ010.6).

One case runs the committed record's real ``--check`` in a second process (W-1).  Every other
case runs the writer in process over a reduced set, writing only to a temporary record path:
the first 30 corpus pairs (which carry every band of every category, so the surface set is the
full run's), their own band counts in place of the frozen baseline, the real CLI code run in
process instead of as a subprocess, the declared outcomes of the six disclosed tools, and the
admitted root bundle for the default provider.  Negative controls break one v2 rule each and
assert the writer's named refusal (addendum 2.6 R-3).
"""
from __future__ import annotations

import contextlib
import dataclasses
import io
import json
import os
import subprocess
import sys
from types import SimpleNamespace

import pytest

from engine.compat import compute
from engine.config.registry_loader import RegistryConfigError, _load_active_mechanics_bundle_from_root
from engine.runtime.determinism_env import DETERMINISM_ENV_PINS
from tools.evidence import generate_hde_epic043_v2_integration_evidence as writer

ACTOR = "test actor"
REDUCED_PAIRS = 30
REAL_CHECK_TIMEOUT_SECONDS = 2400


@pytest.fixture(autouse=True)
def _closed_rails(monkeypatch: pytest.MonkeyPatch) -> None:
    for key, value in DETERMINISM_ENV_PINS.items():
        monkeypatch.setenv(key, value)
    monkeypatch.setenv("APP_ENV", "dev")
    monkeypatch.chdir(writer.ROOT)


@pytest.fixture(scope="module")
def admitted():
    return _load_active_mechanics_bundle_from_root(writer.ROOT)


@pytest.fixture(scope="module")
def golden_comparison():
    saved = {key: os.environ.get(key) for key in DETERMINISM_ENV_PINS}
    os.environ.update(DETERMINISM_ENV_PINS)
    try:
        return writer.compare_goldens_at_root()
    finally:
        for key, value in saved.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value


@pytest.fixture(scope="module")
def reduced_corpus():
    digest, people, pairs = writer.corpus()
    return digest, people, pairs[:REDUCED_PAIRS]


@pytest.fixture(scope="module")
def reduced_counts(admitted, reduced_corpus):
    from tools.score_distribution.score_distribution import reference_party

    _digest, people, pairs = reduced_corpus
    parties = [reference_party(person) for person in people]
    overall = {band: 0 for band in writer.BANDS}
    per_category = {category: {band: 0 for band in writer.BANDS} for category in admitted.registry.magic10_order}
    for a, b in pairs:
        for row in writer.evaluate(parties[a], parties[b], admitted)["categories"]:
            overall[row["band"]] += 1
            per_category[row["category_id"]][row["band"]] += 1
    return overall, per_category


def cli_in_process(arguments):
    """The real ``engine.cli.main.cli`` run in this process, with its streams captured."""

    from engine.cli import main as cli_main

    out = io.BytesIO()
    err = io.StringIO()
    stdout = io.TextIOWrapper(out, encoding="utf-8")
    with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(err):
        code = cli_main.cli(list(arguments))
        stdout.flush()
    return subprocess.CompletedProcess(list(arguments), code, out.getvalue(), err.getvalue().encode("utf-8"))


def declared_tool(path, arguments):
    for tool, _args, exit_code, refusal, _cause, _run_here in writer.BASELINE_FAILURES:
        if tool == path:
            return subprocess.CompletedProcess([path, *arguments], exit_code, b"", refusal.encode("utf-8"))
    raise AssertionError(path)


@pytest.fixture
def reduced(tmp_path, monkeypatch, admitted, golden_comparison, reduced_corpus, reduced_counts):
    out = tmp_path / "v2_integration_evidence.txt"
    monkeypatch.setattr(writer, "out_path", lambda: out)
    monkeypatch.setattr(writer, "corpus", lambda: reduced_corpus)
    monkeypatch.setattr(writer, "baseline_counts", lambda bundle, digest: reduced_counts)
    monkeypatch.setattr(writer, "load_root_bundle", lambda: admitted)
    monkeypatch.setattr(writer, "compare_goldens_at_root", lambda: golden_comparison)
    monkeypatch.setattr(writer, "run_cli", cli_in_process)
    monkeypatch.setattr(writer, "run_tool", declared_tool)
    monkeypatch.setattr(compute, "_BUNDLE_PROVIDER", lambda: admitted)
    return out


def _refused(code_prefix: str):
    return pytest.raises(writer.IntegrationEvidenceRefusal, match=f"^{code_prefix}")


def _record(out) -> dict[str, str]:
    return dict(writer.parse_record(out.read_bytes()))


def _wrap_evaluate(monkeypatch, change):
    real = writer.evaluate

    def wrapped(left, right, bundle):
        value = real(left, right, bundle)
        change(left, right, value)
        return value

    monkeypatch.setattr(writer, "evaluate", wrapped)


def _bump(value, index=0):
    signal = value["signals"][index]
    signal["q"] = signal["q"] + 1 if signal["q"] < 1000 else signal["q"] - 1


# --- W-1: the committed record, by the real --check in a second process ---------------------------

def test_the_committed_record_passes_the_real_check_in_a_second_process() -> None:
    env = {**os.environ, **DETERMINISM_ENV_PINS, "APP_ENV": "dev"}
    result = subprocess.run([sys.executable, writer.GENERATOR_REL, "--check"], cwd=writer.ROOT, env=env,
                            capture_output=True, timeout=REAL_CHECK_TIMEOUT_SECONDS)
    assert result.returncode == 0, result.stderr.decode("utf-8", "replace")[-2000:]
    assert result.stdout == b"v2 integration evidence check ok\n"


# --- W-2 to W-5: the PASS, disclosure and deferred paths, byte-stable --------------------------------

def test_write_then_check_twice_is_byte_stable_apart_from_the_run_fields(reduced) -> None:
    first = writer.write(ACTOR)
    writer.check()
    writer.check()
    second = writer.write(ACTOR)
    strip = lambda data: [line for line in data.splitlines() if not line.startswith(b"run.time_utc: ")]
    assert strip(first) == strip(second)
    assert reduced.read_bytes() == second


def test_every_passing_class_renders_pass_with_its_counts(reduced) -> None:
    writer.write(ACTOR)
    record = _record(reduced)
    for class_id in ("full_matrix", "ab_ba_two_run", "pair_cache_identity", "uid_independence", "result_schema",
                     "reader_projection", "internal_parity"):
        assert record[f"class.{class_id}.result"] == "PASS", class_id
    assert record["class.full_matrix.pairs"] == str(REDUCED_PAIRS)
    assert record["class.full_matrix.baseline.equal"] == "true"
    assert record["set.surface.corpus_indices"] == "[0,1,2,3,4,5,6,8,13,15,18,27]"
    assert record["set.surface.pairs"] == "16"
    assert record["class.internal_parity.runs"] == "32"
    assert record["class.internal_parity.cli_stdout_equal"] == "32"
    assert record["class.internal_parity.http_body_equal"] == "32"
    assert record["class.reader_projection.eligible_runs"] == "30"
    assert record["class.uid_independence.surface.identical"] == "30"
    assert record["class.result_schema.adverse_refused"].count(":") == 10
    assert record["release.release_id"] == record["class.full_matrix.baseline.release_id"]
    assert record["classes.pass"] == "7" and record["classes.baseline_failure_disclosed"] == "1"
    assert record["status"] == "COMPLETE"


def test_the_failure_token_class_and_the_tools_render_their_disclosures(reduced) -> None:
    writer.write(ACTOR)
    record = _record(reduced)
    assert record["class.failure_tokens.result"] == "BASELINE_FAILURE_DISCLOSED"
    assert record["class.failure_tokens.cause"] == writer.GATE_DATA_CAUSE
    for row in ("FT-1", "FT-2", "FT-8"):
        assert record[f"class.failure_tokens.{row}.result"] == "PASS"
        assert f"class.failure_tokens.{row}.cause" not in record
    for row, governed in (("FT-3", "ERR_M10_GATES_MISSING"), ("FT-4", "ERR_M10_GATES_MISSING"),
                          ("FT-5", "ERR_M10_GATES_INVALID"), ("FT-6", "ERR_M10_GATES_INVALID"),
                          ("FT-7", "ERR_M10_GATES_INVALID")):
        assert record[f"class.failure_tokens.{row}.result"] == "BASELINE_FAILURE_DISCLOSED"
        assert record[f"class.failure_tokens.{row}.governed"] == f"{governed} 422"
        assert record[f"class.failure_tokens.{row}.cause"] == writer.GATE_DATA_CAUSE
    assert record["baseline_failure.count"] == "6"
    assert record["baseline_failure.1.command"] == "python tools/presenter/generate_presenter_artifacts.py --check"
    assert record["baseline_failure.3.observed"] == writer.NOT_RUN_OBSERVATION
    assert record["baseline_failure.4.observed"] == writer.NOT_RUN_OBSERVATION


def test_a_disclosed_tool_whose_outcome_changes_is_refused(reduced, monkeypatch) -> None:
    def tool(path, arguments):
        if path == "scripts/validate/sidecar_check.py":
            return subprocess.CompletedProcess([path], 0, b"", b"")
        return declared_tool(path, arguments)

    monkeypatch.setattr(writer, "run_tool", tool)
    with _refused(f"{writer.BASELINE_FAILURE_CHANGED}:scripts/validate/sidecar_check.py"):
        writer.write(ACTOR)
    assert not reduced.exists()


def test_the_deferred_lines_name_the_live_parts_and_nothing_else_is_deferred(reduced) -> None:
    writer.write(ACTOR)
    record = _record(reduced)
    assert record["deferred.HDE-COAG003.8"] == "live current-row Gate readiness: DEFERRED; not represented as achieved (C-09)"
    assert record["deferred.HDE-COAG003.9"] == "live DB Reader success: DEFERRED; not represented as achieved (C-09)"
    deferred = sorted(key for key, value in record.items() if "DEFERRED" in value)
    assert deferred == ["deferred.HDE-COAG003.8", "deferred.HDE-COAG003.9", "limitation.1"]
    assert all(value in ("PASS", "BASELINE_FAILURE_DISCLOSED")
               for key, value in record.items() if key.startswith("class.") and key.endswith(".result"))


# --- W-6: stale, edited and missing records ----------------------------------------------------------

def test_check_refuses_a_missing_record(reduced) -> None:
    with pytest.raises(SystemExit, match=f"^DRIFT:{writer.OUT_REL}:missing$"):
        writer.check()


def test_an_edited_record_line_is_drift_at_its_key(reduced) -> None:
    writer.write(ACTOR)
    data = reduced.read_bytes().replace(b"class.internal_parity.runs: 32\n", b"class.internal_parity.runs: 33\n")
    reduced.write_bytes(data)
    with pytest.raises(SystemExit, match=f"^DRIFT:{writer.OUT_REL}:class.internal_parity.runs$"):
        writer.check()


def test_a_changed_tested_input_is_drift_before_any_class_runs(reduced, monkeypatch) -> None:
    writer.write(ACTOR)
    real = writer.read_input
    rel = "tools/config/artifacts.py"
    monkeypatch.setattr(writer, "read_input", lambda name: real(name) + b"# edited\n" if name == rel else real(name))
    monkeypatch.setattr(writer, "corpus", lambda: (_ for _ in ()).throw(AssertionError("a class ran")))
    with pytest.raises(SystemExit, match=f"^DRIFT:{writer.OUT_REL}:input.{rel}.sha256$"):
        writer.check()


def test_a_malformed_run_field_is_drift(reduced) -> None:
    writer.write(ACTOR)
    lines = reduced.read_bytes().split(b"\n")
    lines = [b"run.time_utc: yesterday" if line.startswith(b"run.time_utc: ") else line for line in lines]
    reduced.write_bytes(b"\n".join(lines))
    with pytest.raises(SystemExit, match=f"^DRIFT:{writer.OUT_REL}:run.time_utc$"):
        writer.check()


# --- W-7 and W-8: preconditions and the v2-only guard ---------------------------------------------------

def test_open_rails_are_refused_and_nothing_is_written(reduced, monkeypatch) -> None:
    monkeypatch.setenv("SAFE_MODE", "0")
    with _refused(writer.RAILS_NOT_CLOSED):
        writer.write(ACTOR)
    assert not reduced.exists()


def test_an_app_env_outside_the_compat_gate_is_refused(reduced, monkeypatch) -> None:
    monkeypatch.setenv("APP_ENV", "prod")
    with _refused(writer.APP_ENV_NOT_DEV):
        writer.write(ACTOR)
    assert not reduced.exists()


def test_another_working_directory_is_refused(reduced, monkeypatch, tmp_path) -> None:
    monkeypatch.chdir(tmp_path)
    with _refused(writer.WORKING_DIRECTORY_INVALID):
        writer.write(ACTOR)
    assert not reduced.exists()


@pytest.mark.parametrize("actor", ["", " padded", "line\nbreak", "x" * 201])
def test_an_invalid_actor_is_refused(reduced, actor) -> None:
    with _refused(writer.INVALID_ACTOR):
        writer.write(actor)
    assert not reduced.exists()


def test_a_non_admitted_candidate_is_refused(reduced, monkeypatch, tmp_path) -> None:
    from tests.config.helpers import admit_synthetic_v2_candidate

    synthetic = admit_synthetic_v2_candidate(tmp_path)
    monkeypatch.setattr(writer, "load_root_bundle", lambda: synthetic)
    with _refused(f"{writer.NOT_ADMITTED_V2_PATH}:release$"):
        writer.write(ACTOR)
    assert not reduced.exists()


def test_a_class_value_on_the_v1_configuration_is_refused(reduced, monkeypatch) -> None:
    _wrap_evaluate(monkeypatch, lambda left, right, value: value.__setitem__("config_id", writer.V1_CONFIG_ID))
    with _refused(f"{writer.NOT_ADMITTED_V2_PATH}:full_matrix$"):
        writer.write(ACTOR)


def test_a_root_that_does_not_admit_is_refused(reduced, monkeypatch) -> None:
    def refuse():
        raise RegistryConfigError("MANIFEST_MEMBER_HASH_MISMATCH", "member bytes differ")

    monkeypatch.setattr(writer, "load_root_bundle", refuse)
    with _refused(f"{writer.RELEASE_REFUSED}:MANIFEST_MEMBER_HASH_MISMATCH$"):
        writer.write(ACTOR)


# --- negative controls, one or more per class (addendum 2.6 R-3) -------------------------------------

def test_n1_band_counts_that_differ_from_the_baseline_are_refused(reduced, monkeypatch, reduced_counts) -> None:
    overall, per_category = reduced_counts
    changed = {category: dict(counts) for category, counts in per_category.items()}
    changed["harmony"]["Cool"] += 1
    monkeypatch.setattr(writer, "baseline_counts", lambda bundle, digest: (overall, changed))
    with _refused(f"{writer.MATRIX_BASELINE_MISMATCH}:harmony$"):
        writer.write(ACTOR)


def test_n1_an_incomplete_result_is_refused(reduced, monkeypatch) -> None:
    _wrap_evaluate(monkeypatch, lambda left, right, value: value["categories"].pop())
    with _refused(f"{writer.MATRIX_INCOMPLETE}$"):
        writer.write(ACTOR)


def test_n2_a_result_that_differs_between_ab_and_ba_is_refused(reduced, monkeypatch) -> None:
    seen = set()

    def change(left, right, value):
        if (id(right), id(left)) in seen:
            _bump(value)
        seen.add((id(left), id(right)))

    _wrap_evaluate(monkeypatch, change)
    with _refused(f"{writer.ABBA_MISMATCH}:corpus\\[0\\]$"):
        writer.write(ACTOR)


def test_n2_a_second_run_that_differs_is_refused(reduced, monkeypatch) -> None:
    seen = set()

    def change(left, right, value):
        if (id(left), id(right)) in seen:
            _bump(value)
        seen.add((id(left), id(right)))

    _wrap_evaluate(monkeypatch, change)
    with _refused(f"{writer.TWO_RUN_MISMATCH}:in_process:corpus\\[0\\].ab$"):
        writer.write(ACTOR)


def test_n3_a_pair_key_under_another_configuration_is_refused(reduced, monkeypatch) -> None:
    def change(left, right, value):
        value["pair_key"] = writer.pair_key_for(left, right, config_id=writer.V1_CONFIG_ID,
                                                release_id=value["release_id"],
                                                result_schema=writer.V2_RESULT_SCHEMA)

    _wrap_evaluate(monkeypatch, change)
    with _refused(f"{writer.PAIR_KEY_MISMATCH}$"):
        writer.write(ACTOR)


def test_n3_a_cache_key_with_the_v1_prefix_is_refused(reduced, monkeypatch) -> None:
    monkeypatch.setattr(writer, "magic10_v2_intrinsic_cache_key", lambda pair_key: writer.V1_CACHE_PREFIX + pair_key)
    with _refused(f"{writer.CACHE_KEY_MISMATCH}$"):
        writer.write(ACTOR)


def test_n4_a_user_id_entering_the_intrinsic_content_is_refused(reduced, monkeypatch) -> None:
    labels = [f"corpus[{index}]" for index in range(REDUCED_PAIRS)] + list(writer.SURFACE_GOLDEN_PARTIES)
    variants = {writer.variant_uid(label, variant, side) for label in labels
                for variant in writer.UID_VARIANTS for side in ("left", "right")}

    def change(left, right, value):
        if left.canonical_person_id in variants:
            _bump(value)

    _wrap_evaluate(monkeypatch, change)
    with _refused(f"{writer.UID_DEPENDENT}:corpus\\[0\\]$"):
        writer.write(ACTOR)


def test_n5_a_malformed_result_reaching_the_writer_is_refused(reduced, monkeypatch) -> None:
    _wrap_evaluate(monkeypatch, lambda left, right, value: value["categories"][0].__setitem__("score", 101))
    with _refused(f"{writer.RESULT_SCHEMA_REFUSED}:{writer.RESULT_SCHEMA_REL}$"):
        writer.write(ACTOR)


def test_n5_a_validator_that_accepts_an_adverse_variant_is_refused(reduced, monkeypatch) -> None:
    permissive = SimpleNamespace(validate=lambda document: None, is_valid=lambda document: True)
    monkeypatch.setattr(writer, "strict_validator", lambda rel: permissive)
    with _refused(f"{writer.SCHEMA_ADVERSE_ACCEPTED}:{writer.RESULT_SCHEMA_REL}:score_101$"):
        writer.write(ACTOR)


def test_n6_a_reader_body_carrying_a_number_is_refused(reduced, monkeypatch) -> None:
    from engine.magic10_v2 import compat as v2_compat

    real = v2_compat.reader_projection_v2

    def projection(result, version):
        body, envelope = real(result, version)
        if version == "v2":
            parsed = json.loads(body)
            parsed["categories"][0]["score"] = 1
            body = json.dumps(parsed, sort_keys=True, separators=(",", ":")).encode("utf-8")
        return body, envelope

    monkeypatch.setattr(v2_compat, "reader_projection_v2", projection)
    with _refused(f"{writer.READER_MISMATCH}:v2_"):
        writer.write(ACTOR)


def test_n6_a_reader_v1_band_other_than_the_result_band_is_refused(reduced, monkeypatch) -> None:
    from engine.magic10_v2 import compat as v2_compat

    real = v2_compat.reader_projection_v2

    def projection(result, version):
        categories = tuple(
            dataclasses.replace(row, band="Glow" if row.band != "Glow" else "Cool") if row.category_id == "harmony" else row
            for row in result.categories
        )
        return real(dataclasses.replace(result, categories=categories), version)

    monkeypatch.setattr(v2_compat, "reader_projection_v2", projection)
    with _refused(f"{writer.READER_MISMATCH}:v1_band:corpus\\[0\\].ab$"):
        writer.write(ACTOR)


def test_n6_a_reader_golden_one_byte_off_is_refused(reduced, monkeypatch) -> None:
    rel = "goldens/reader/v1/g05_harmony_cool.json"
    real = writer.read_input
    monkeypatch.setattr(writer, "read_input", lambda name: real(name).replace(b"Cool", b"Cool ") if name == rel else real(name))
    with _refused(f"{writer.READER_GOLDEN_MISMATCH}:{rel}$"):
        writer.write(ACTOR)


def test_n7_a_cli_token_other_than_the_declared_one_is_refused(reduced, monkeypatch) -> None:
    def cli(arguments):
        result = cli_in_process(arguments)
        if result.stderr == b"ERR_M10_LEGACY_INPUT_UNSUPPORTED\n":
            return subprocess.CompletedProcess(result.args, 1, b"", b"ERR_READER_INVALID_CHART\n")
        return result

    monkeypatch.setattr(writer, "run_cli", cli)
    with _refused(f"{writer.FAILURE_TOKEN_MISMATCH}:FT-1:cli$"):
        writer.write(ACTOR)


def test_n7_an_http_error_without_no_store_is_refused(reduced, monkeypatch) -> None:
    real = writer.http_client

    class Client:
        def __init__(self) -> None:
            self.inner = real()

        def post(self, *args, **kwargs):
            response = self.inner.post(*args, **kwargs)
            if response.status_code < 400:
                return response
            headers = {key: value for key, value in response.headers.items() if key != "Cache-Control"}
            return SimpleNamespace(status_code=response.status_code, data=response.data, headers=headers)

    monkeypatch.setattr(writer, "http_client", Client)
    with _refused(f"{writer.FAILURE_TOKEN_MISMATCH}:FT-1:http$"):
        writer.write(ACTOR)


def test_n8_cli_stdout_one_byte_off_is_refused(reduced, monkeypatch) -> None:
    def cli(arguments):
        result = cli_in_process(arguments)
        if result.returncode == 0:
            return subprocess.CompletedProcess(result.args, 0, result.stdout.replace(b'"', b"'", 1), result.stderr)
        return result

    monkeypatch.setattr(writer, "run_cli", cli)
    with _refused(f"{writer.PARITY_MISMATCH}:cli:corpus\\[0\\].ab$"):
        writer.write(ACTOR)


def test_n8_an_http_body_one_byte_off_is_refused(reduced, monkeypatch) -> None:
    real = writer.http_client

    class Client:
        def __init__(self) -> None:
            self.inner = real()

        def post(self, *args, **kwargs):
            response = self.inner.post(*args, **kwargs)
            return SimpleNamespace(status_code=response.status_code, data=response.data + b" ",
                                   headers=dict(response.headers.items()))

    monkeypatch.setattr(writer, "http_client", Client)
    with _refused(f"{writer.PARITY_MISMATCH}:http:corpus\\[0\\].ab$"):
        writer.write(ACTOR)


def test_n8_a_reader_dump_one_byte_off_is_refused(reduced, monkeypatch) -> None:
    def cli(arguments):
        result = cli_in_process(arguments)
        if "--dump-reader" in arguments:
            dump = arguments[arguments.index("--dump-reader") + 1]
            with open(dump, "ab") as handle:
                handle.write(b" ")
        return result

    monkeypatch.setattr(writer, "run_cli", cli)
    with _refused(f"{writer.PARITY_MISMATCH}:reader:corpus\\[0\\].ab$"):
        writer.write(ACTOR)
