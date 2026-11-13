#!/usr/bin/env python3
"""Real-path tuning-run identity proof (HDE-EPIC042 WU-PR-01; HDE-DISS005.3).

Each tuning run is one evaluation of one corpus pair, in one order, under the
admitted release's thresholds.  Per pair the proof covers four runs: AB in
process, BA in process, AB again in process, and AB through
``python -m engine.cli showcompat --a-file ... --b-file ...`` stdout.  Each run
hashes the LF-terminated canonical ``magic10_compat_result.v1`` body that
``hdctl showcompat`` prints: ``engine.compat.compute.evaluate_pair`` (which calls
``engine.core.core.compute_core``), then ``engine.presenter.emitter.emit_public``.
The proof passes only when all four bodies are canonical and equal.

The fixtures resolve as release-sanity stage 04 resolves them
(``_normalize_party`` and ``_resolve_party`` with ``source_policy='local'``).
The admission owner is probed first: while the active release is not admitted,
the tool prints its refusal line, exits with the distinct code and writes
nothing.  Neither ``artifacts/compat/AB.json`` nor ``BA.json`` is read, and the
HDE-EPIC030 PR-04 records stay as written.  The record carries no wall-clock,
git or host field, so ``--check`` compares it byte for byte.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Mapping

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.cli import main as cli_main  # noqa: E402
from engine.compat.compute import evaluate_pair, evaluation_party  # noqa: E402
from engine.presenter import emitter  # noqa: E402
from engine.runtime.determinism_env import ensure_determinism_env  # noqa: E402
from engine.serializer import canon  # noqa: E402
from tools.evidence.run_sanity_pipeline import (  # noqa: E402
    RELEASE_NOT_ADMITTED_EXIT_CODE,
    ReleaseNotAdmitted,
    probe_release_admission,
)

OUT_REL = "audit/qa/hde-epic042/pr-01/tuning_identity_hash.txt"
OUT = ROOT / OUT_REL
SCHEMA = "hde_epic042_tuning_identity_hash.v1"
CORPUS_ID = "hde-epic042-pr01-complete-fixture-charts"
# The two complete mapped fixture charts, the stage 04 corpus.
CORPUS: tuple[tuple[str, str], ...] = (
    ("fixtures/charts/alice.json", "fixtures/charts/bob.json"),
)
RUN_IDS = ("ab", "ba", "ab_repeat", "cli")
RUN_SOURCES = {
    "ab": "in-process evaluate_pair(a, b)",
    "ba": "in-process evaluate_pair(b, a)",
    "ab_repeat": "in-process evaluate_pair(a, b), second run",
    "cli": "python -m engine.cli showcompat --a-file a --b-file b, stdout",
}
HASH_BASIS = (
    "sha256 over the LF-terminated canonical magic10_compat_result.v1 body that "
    "hdctl showcompat prints (engine.compat.compute.evaluate_pair, which calls "
    "engine.core.core.compute_core, then engine.presenter.emitter.emit_public)"
)
CANONICAL_FORM = (
    "UTF-8, no BOM, no CRLF, exactly one trailing LF, canonical re-serialization equal"
)
EXCLUDED_SOURCES = "artifacts/compat/AB.json, artifacts/compat/BA.json"
NOT_ADMITTED_LINE = "HDE_EPIC042_TUNING_IDENTITY_CHECK:RELEASE_NOT_ADMITTED"
FAILED_EXIT = "TUNING_IDENTITY_FAILED"


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def cjson(obj: object) -> bytes:
    return json.dumps(obj, separators=(",", ":"), sort_keys=True).encode("utf-8") + b"\n"


def env() -> dict[str, str]:
    """Closed-rails environment for the CLI subprocess (stage 04's values)."""

    environ = os.environ.copy()
    environ.update(
        {
            "SAFE_MODE": "1",
            "ALLOW_NETWORK": "0",
            "LC_ALL": "C",
            "LANG": "C",
            "TZ": "UTC",
            "APP_ENV": "test",
            "PIP_NO_INDEX": "1",
        }
    )
    ensure_determinism_env(environ=environ)
    return environ


def load_party(rel: str) -> dict:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def resolved(party: Mapping[str, object], label: str):
    normalized = cli_main._normalize_party(dict(party), label)
    return cli_main._resolve_party(normalized, source_policy="local")


def compat_body(left: Mapping[str, object], right: Mapping[str, object]) -> bytes:
    """The compat body for one order, in process, on the real path."""

    result = evaluate_pair(
        evaluation_party(resolved(left, "left")),
        evaluation_party(resolved(right, "right")),
    )
    return emitter.emit_public(result)


def cli_body(a_rel: str, b_rel: str) -> bytes:
    """``python -m engine.cli showcompat`` stdout for the pair, closed rails."""

    with tempfile.TemporaryDirectory() as raw:
        tmp = Path(raw)
        a_path = tmp / "a.json"
        b_path = tmp / "b.json"
        a_path.write_bytes(cjson(load_party(a_rel)))
        b_path.write_bytes(cjson(load_party(b_rel)))
        proc = subprocess.run(
            [
                sys.executable,
                "-m",
                "engine.cli",
                "showcompat",
                "--a-file",
                str(a_path),
                "--b-file",
                str(b_path),
            ],
            cwd=ROOT,
            env=env(),
            capture_output=True,
        )
    if proc.returncode or proc.stderr:
        raise RuntimeError(f"showcompat failed rc={proc.returncode} stderr={proc.stderr!r}")
    return proc.stdout


def canonical_ok(body: bytes) -> bool:
    if body.startswith(b"\xef\xbb\xbf") or b"\r\n" in body:
        return False
    if not body.endswith(b"\n") or body.endswith(b"\n\n"):
        return False
    try:
        return canon.sercanon(json.loads(body)) == body
    except ValueError:
        return False


def _flag(value: bool) -> str:
    return "true" if value else "false"


def _body_fields(body: bytes) -> dict:
    try:
        parsed = json.loads(body)
    except ValueError:
        return {}
    return parsed if isinstance(parsed, dict) else {}


def build(*, overrides: Mapping[str, bytes] | None = None) -> tuple[bool, bytes]:
    """Probe admission, compute every run, and return (passed, record bytes).

    ``overrides`` maps a run ID to bytes that replace that run's computed body;
    only the owner test uses it, to prove the record fails.
    """

    probe_release_admission()  # raises ReleaseNotAdmitted before any body is computed
    overrides = dict(overrides or {})
    unknown = sorted(set(overrides) - set(RUN_IDS))
    if unknown:
        raise ValueError(f"unknown run ids: {unknown}")

    pair_lines: list[str] = []
    header: dict | None = None
    passed = True
    for index, (a_rel, b_rel) in enumerate(CORPUS, start=1):
        left = load_party(a_rel)
        right = load_party(b_rel)
        bodies = {
            "ab": compat_body(left, right),
            "ba": compat_body(right, left),
            "ab_repeat": compat_body(left, right),
            "cli": cli_body(a_rel, b_rel),
        }
        bodies.update(overrides)
        ab = bodies["ab"]
        fields = _body_fields(ab)
        if header is None:
            header = fields
        canonical = all(canonical_ok(bodies[run]) for run in RUN_IDS)
        ab_ba = ab == bodies["ba"]
        two_run = ab == bodies["ab_repeat"]
        cli_parity = ab == bodies["cli"]
        passed = passed and canonical and ab_ba and two_run and cli_parity
        prefix = f"pair.{index}"
        pair_lines += [
            f"{prefix}.a: {a_rel}",
            f"{prefix}.b: {b_rel}",
            f"{prefix}.pair_key: {fields.get('pair_key')}",
            f"{prefix}.body_size_bytes: {len(ab)}",
        ]
        for run in RUN_IDS:
            pair_lines += [
                f"{prefix}.run.{run}.source: {RUN_SOURCES[run]}",
                f"{prefix}.run.{run}.sha256: {sha256_hex(bodies[run])}",
            ]
        pair_lines += [
            f"{prefix}.canonical_form_ok: {_flag(canonical)}",
            f"{prefix}.ab_ba_equal: {_flag(ab_ba)}",
            f"{prefix}.two_run_equal: {_flag(two_run)}",
            f"{prefix}.cli_parity_equal: {_flag(cli_parity)}",
        ]

    header = header or {}
    lines = [
        f"schema: {SCHEMA}",
        "epic_id: HDE-EPIC042",
        "task_id: HDE-DISS005",
        "subtask_id: HDE-DISS005.3",
        "work_unit_id: WU-PR-01",
        f"hash_basis: {HASH_BASIS}",
        f"canonical_form: {CANONICAL_FORM}",
        f"excluded_sources: {EXCLUDED_SOURCES}",
        f"release_id: {header.get('release_id')}",
        f"config_id: {header.get('config_id')}",
        f"compat_schema: {header.get('schema')}",
        f"corpus: {CORPUS_ID}",
        f"pair_count: {len(CORPUS)}",
        *pair_lines,
        f"status: {'PASS' if passed else 'FAIL'}",
    ]
    return passed, ("\n".join(lines) + "\n").encode("utf-8")


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="compare the stored proof with recomputation; write nothing")
    args = parser.parse_args(argv)
    ensure_determinism_env()
    try:
        passed, record = build()
    except ReleaseNotAdmitted:
        # No body was computed and nothing is written; the distinct code is never 0.
        print(NOT_ADMITTED_LINE)
        raise SystemExit(RELEASE_NOT_ADMITTED_EXIT_CODE)
    if not passed:
        raise SystemExit(FAILED_EXIT)
    if args.check:
        if not OUT.is_file() or OUT.read_bytes() != record:
            raise SystemExit(f"DRIFT:{OUT_REL}")
        print("tuning identity hash check ok")
        return
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes(record)
    print("tuning identity hash written")


if __name__ == "__main__":
    main()
