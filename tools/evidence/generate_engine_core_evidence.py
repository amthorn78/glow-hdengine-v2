#!/usr/bin/env python3
"""Produce the existing four core proofs using a synthetic admitted release."""
from __future__ import annotations

import argparse
import ast
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import jsonschema
from referencing import Registry, Resource

from engine.bodygraph.gates import normalize_gates
from engine.config.registry_loader import _load_active_mechanics_bundle_from_root
from engine.core import compute_core
from engine.magic10_v2.kernel import compute_kernel
from engine.runtime.determinism_env import ensure_determinism_env
from engine.serializer.canon import sercanon
from tests.config.helpers import synthetic_v2_candidate_root, v2_candidate_roster_admission

CORE_ARTIFACTS = {
    "engine_core_purity_report": "artifacts/core/purity/purity_report.json",
    "engine_core_two_run_logs": "artifacts/core/two_run/identity.json",
    "engine_core_abba_logs": "artifacts/core/abba/ab_ba_parity.json",
    "engine_core_json_compare_logs": "artifacts/core/json_compare/core_result_json_compare.json",
}
CORE_SCHEMAS = {
    key + "_schema": "docs/schemas/core/" + key + ".schema.json" for key in CORE_ARTIFACTS
}
# HDE-EPIC043 WU-PR-09: the switched core and the Magic10 v2 modules it executes.
PURE_PATHS = (
    "engine/core/core.py", "engine/magic10_v2/kernel.py",
    "engine/magic10_v2/signals.py", "engine/magic10_v2/calculation.py",
)
# The governed v2 configuration does not exist before the cut; the labelled
# fixture stands in for it, and its ``sources`` bind the other inputs by digest.
SOURCE_PATHS = PURE_PATHS + (
    "engine/core/__init__.py", "engine/magic10_v2/__init__.py",
    "engine/bodygraph/gates.py", "engine/config/registry_loader.py",
    "engine/config/magic10_v2_loader.py",
    "engine/serializer/canon.py", "engine/stable/sercanon.py",
    "tests/fixtures/magic10_v2/magic10_mechanics_v2.fixture.json", "schemas/magic10_result_v2.schema.json",
)
FORBIDDEN_ROOTS = frozenset((
    "os", "time", "datetime", "random", "secrets", "uuid", "socket", "subprocess",
    "pathlib", "io", "json", "decimal", "requests", "urllib", "http", "locale",
    "sqlite3", "psycopg", "redis", "importlib",
))
FORBIDDEN_CALLS = frozenset((
    "open", "eval", "exec", "compile", "__import__", "getenv",
    "read_text", "read_bytes", "write_text", "write_bytes",
))
# HDE Math Spec §9.5 (v2): M10-G001 (no Channel, two Reflectors) is the one v2
# golden canon fixes before the cut: every category scores 0, band Cool.
G001_GATES = ((1,), (2,))
G001_SCORES = (0,) * 10
# Refusal while the governed proof schemas still bind another input list (they
# move to v2 with the proofs' regeneration at the cut, WU-PR-10).
SCHEMA_SOURCE_LIST_MISMATCH = "CORE_PROOF_SCHEMA_SOURCE_LIST_MISMATCH"


def _sha(raw):
    return hashlib.sha256(raw).hexdigest()


def _purity_rows():
    rows = []
    for path in PURE_PATHS:
        tree = ast.parse((ROOT / path).read_text(encoding="utf-8"))
        imports, calls = [], []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imports.extend(a.name for a in node.names if a.name.split(".")[0] in FORBIDDEN_ROOTS)
            elif isinstance(node, ast.ImportFrom):
                if (node.module or "").split(".")[0] in FORBIDDEN_ROOTS:
                    imports.append(node.module)
            elif isinstance(node, ast.Call):
                name = node.func.id if isinstance(node.func, ast.Name) else (
                    node.func.attr if isinstance(node.func, ast.Attribute) else ""
                )
                # ``re.compile`` builds a regular expression, not code; builtin ``compile`` stays forbidden.
                regex = (name == "compile" and isinstance(node.func, ast.Attribute)
                         and isinstance(node.func.value, ast.Name) and node.func.value.id == "re")
                if name in FORBIDDEN_CALLS and not regex:
                    calls.append(name)
        rows.append({"module": path, "forbidden_imports": sorted(imports),
                     "forbidden_calls": sorted(calls), "passed": not (imports or calls)})
    return rows


def _schema_registry():
    """Resolve every result schema a governed proof schema may reference."""
    registry = Registry()
    for path in ("schemas/magic10_result_v1.schema.json", "schemas/magic10_result_v2.schema.json"):
        registry = registry.with_resource(path, Resource.from_contents(json.loads((ROOT / path).read_bytes())))
    return registry


def _validate_payloads(payloads):
    registry = _schema_registry()
    for key, payload in payloads.items():
        schema = json.loads((ROOT / CORE_SCHEMAS[key + "_schema"]).read_bytes())
        if schema["properties"]["source_sha256"]["required"] != list(SOURCE_PATHS):
            # The governed schema binds another input list: no proof is valid
            # against it until it moves with the proofs at the cut.
            raise ValueError(SCHEMA_SOURCE_LIST_MISMATCH)
        jsonschema.Draft202012Validator(schema, registry=registry).validate(payload)


def _build_payloads():
    env = ensure_determinism_env(apply=True)
    command = [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "tests/core/test_engine_core_purity.py"]
    run_env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", PYTHONPATH=str(ROOT))
    guarded = subprocess.run(command, cwd=ROOT, env=run_env, capture_output=True, text=True)
    if guarded.returncode:
        raise ValueError("core behavioral purity guard failed")
    purity = _purity_rows()
    if not all(row["passed"] for row in purity):
        raise ValueError("core static purity guard failed")
    captured = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    common = {
        "generated_at_utc": captured, "fixture_kind": "synthetic_complete_release_only",
        "source_sha256": {path: _sha((ROOT / path).read_bytes()) for path in SOURCE_PATHS},
        "env": env,
    }
    with TemporaryDirectory(prefix="hde-pr03-core-evidence-") as tmp:
        candidate = synthetic_v2_candidate_root(Path(tmp), source_root=ROOT)
        with v2_candidate_roster_admission():
            bundle = _load_active_mechanics_bundle_from_root(candidate)
        a, b = normalize_gates([5, 19, 20, 34, 43, 49]), normalize_gates([9, 12, 15, 22, 23, 52])
        first = compute_core(a, b, bundle, bundle.release_id)
        second = compute_core(a, b, bundle, bundle.release_id)
        reverse = compute_core(b, a, bundle, bundle.release_id)
        equal = compute_core(a, a, bundle, bundle.release_id)
        oracle = compute_core(normalize_gates(list(G001_GATES[0])), normalize_gates(list(G001_GATES[1])),
                              bundle, bundle.release_id)
        first_payload, second_payload = first.as_payload(), second.as_payload()
        reverse_payload, equal_payload = reverse.as_payload(), equal.as_payload()
        schema = json.loads((ROOT / "schemas/magic10_result_v2.schema.json").read_bytes())
        for result in (first_payload, second_payload, reverse_payload, equal_payload, oracle.as_payload()):
            jsonschema.Draft202012Validator(schema).validate(result)
        if (tuple(r.score for r in oracle.categories) != G001_SCORES
                or any(r.band != "Cool" for r in oracle.categories)):
            raise ValueError("fixed G001 oracle mismatch")
        canonical = sercanon(first_payload, sort_keys=True)
        repeated = sercanon(second_payload, sort_keys=True)
        reversed_bytes = sercanon(reverse_payload, sort_keys=True)
        reparsed = sercanon(json.loads(canonical), sort_keys=True)
        ab_states = compute_kernel(a.mask, b.mask, bundle.magic10_v2).channels
        ba_states = compute_kernel(b.mask, a.mask, bundle.magic10_v2).channels
        owners = {r.channel_id: r.owner for r in ab_states if r.owner is not None}
        owner_ok = owners == {"09-52": "member_hi", "12-22": "member_hi",
                              "19-49": "member_lo", "20-34": "member_lo"}
        inputs = {"member_a_mask_hex": a.mask_hex, "member_b_mask_hex": b.mask_hex,
                  "config_id": bundle.mechanics["config_id"], "release_id": bundle.release_id}
        payloads = {
            "engine_core_purity_report": dict(common, schema="engine_core_purity_report.v1",
                modules=purity, behavioral_guard_passed=True, behavioral_guard_exit_code=guarded.returncode),
            "engine_core_two_run_logs": dict(common, schema="engine_core_two_run_logs.v1",
                inputs=inputs, first_run=first_payload, second_run=second_payload,
                identical=first_payload == second_payload, canonical_bytes_equal=canonical == repeated,
                fixed_g001_oracle_passed=True),
            "engine_core_abba_logs": dict(common, schema="engine_core_abba_logs.v1",
                inputs=inputs, ab_run=first_payload, ba_run=reverse_payload,
                equal_mask_run=equal_payload, complete_result_equal=first_payload == reverse_payload,
                canonical_bytes_equal=canonical == reversed_bytes,
                classification_equal=ab_states == ba_states, normalized_owners_verified=owner_ok,
                equal_masks_complete=len(equal.signals) == 20 and len(equal.categories) == 10),
            "engine_core_json_compare_logs": dict(common, schema="engine_core_json_compare_logs.v1",
                inputs=inputs, core_result=first_payload, canonical_sha256=_sha(canonical),
                roundtrip_sha256=_sha(reparsed), size_bytes=len(canonical),
                canonical_bytes_equal=canonical == reparsed, result_schema_valid=True),
        }
    _validate_payloads(payloads)
    return payloads


def _write_payloads(payloads):
    for key, payload in payloads.items():
        path = ROOT / CORE_ARTIFACTS[key]
        if path.exists():
            existing = json.loads(path.read_bytes())
            # An identical proof retains its original observed capture time.
            if {k: v for k, v in existing.items() if k != "generated_at_utc"} == {
                k: v for k, v in payload.items() if k != "generated_at_utc"
            }:
                continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(sercanon(payload, sort_keys=True))


def main(argv=None):
    parser = argparse.ArgumentParser(description="Generate existing core proofs from a synthetic admitted release")
    parser.add_argument("--skip-index", action="store_true")
    args = parser.parse_args(argv)
    payloads = _build_payloads()
    _write_payloads(payloads)
    if not args.skip_index:
        for command in (
            ["tools/evidence/update_evidence_index.py"],
            ["tools/evidence/update_evidence_index.py", "--check"],
            ["tools/evidence/orientation_demo.py", "--check"],
        ):
            subprocess.run([sys.executable, *command], cwd=ROOT, check=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
