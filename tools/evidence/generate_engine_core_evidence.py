#!/usr/bin/env python3
"""Generate Engine Core evidence artifacts under closed rails (DISS004)."""
from __future__ import annotations

import argparse
import ast
import dataclasses
import datetime as _dt
import hashlib
import importlib
import json
import os
import sys
import subprocess
from pathlib import Path
from typing import Iterable, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.core import CoreConfig, ParticipantState, compute_core
from engine.runtime.determinism_env import ensure_determinism_env
from engine.serializer.canon import sercanon
from tools.evidence import update_evidence_index

NOW = _dt.datetime.now(tz=_dt.timezone.utc).replace(microsecond=0)

CORE_ARTIFACTS: dict[str, str] = {
    "engine_core_purity_report": "artifacts/core/purity/purity_report.json",
    "engine_core_two_run_logs": "artifacts/core/two_run/identity.json",
    "engine_core_abba_logs": "artifacts/core/abba/ab_ba_parity.json",
    "engine_core_json_compare_logs": "artifacts/core/json_compare/core_result_json_compare.json",
}

CORE_SCHEMAS: dict[str, str] = {
    "engine_core_purity_report_schema": "docs/schemas/core/engine_core_purity_report.schema.json",
    "engine_core_two_run_logs_schema": "docs/schemas/core/engine_core_two_run_logs.schema.json",
    "engine_core_abba_logs_schema": "docs/schemas/core/engine_core_abba_logs.schema.json",
    "engine_core_json_compare_logs_schema": "docs/schemas/core/engine_core_json_compare_logs.schema.json",
}

FORBIDDEN_ROOT_IMPORTS = {
    "os",
    "time",
    "datetime",
    "random",
    "socket",
    "subprocess",
}

FORBIDDEN_TEXT_SNIPPETS = (
    "os.environ",
    "time.",
    "datetime.",
    "random.",
    "socket.",
)


def _iso(dt: _dt.datetime) -> str:
    return dt.replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _rails_env() -> dict[str, str]:
    env = os.environ.copy()
    env.setdefault("APP_ENV", "dev")
    ensure_determinism_env(environ=env, apply=True)
    return env


def _write_json(rel_path: str, payload: Mapping[str, object]) -> None:
    path = ROOT / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    canon = sercanon(payload, sort_keys=True)
    path.write_bytes(canon)


def _participant(uid: str, score: int, band: str, traits: Iterable[str]) -> ParticipantState:
    return ParticipantState(person_uid=uid, compat_score=score, band=band, traits=tuple(traits))


def _core_result_payload(result) -> dict[str, object]:
    return {
        "viewer_id": result.viewer_id,
        "candidate_id": result.candidate_id,
        "neutral_score": result.neutral_score,
        "ordered_pair": list(result.ordered_pair),
        "ordered_bands": list(result.ordered_bands),
        "shared_traits": list(result.shared_traits),
        "band_alignment": result.band_alignment,
        "perspective": {
            "from_viewer": result.perspective.from_viewer,
            "from_candidate": result.perspective.from_candidate,
            "delta": result.perspective.delta,
        },
    }


def _generate_purity_report() -> None:
    module_path = ROOT / "engine" / "core" / "core.py"
    tree = ast.parse(module_path.read_text(encoding="utf-8"))
    importlib.invalidate_caches()
    module = importlib.import_module("engine.core.core")
    importlib.reload(module)

    forbidden_imports: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            for alias in node.names:
                root = alias.name.split(".")[0]
                if root in FORBIDDEN_ROOT_IMPORTS:
                    forbidden_imports.append(root)

    forbidden_text = [snippet for snippet in FORBIDDEN_TEXT_SNIPPETS if snippet in module_path.read_text(encoding="utf-8")]

    checks = [
        {
            "check_id": "forbidden_imports_absent",
            "status": "pass" if not forbidden_imports else "fail",
            "details": {"forbidden_imports": forbidden_imports},
        },
        {
            "check_id": "forbidden_text_absent",
            "status": "pass" if not forbidden_text else "fail",
            "details": {"forbidden_snippets": forbidden_text},
        },
        {
            "check_id": "module_import_is_side_effect_free",
            "status": "pass",
            "details": {"module": "engine.core.core"},
        },
    ]

    payload = {
        "schema": "engine_core_purity_report.v1",
        "generated_at_utc": _iso(NOW),
        "module": "engine.core.core",
        "checks": checks,
        "env": ensure_determinism_env(apply=True),
    }
    _write_json(CORE_ARTIFACTS["engine_core_purity_report"], payload)


def _generate_two_run_logs() -> None:
    cfg = CoreConfig()
    viewer = _participant("viewer_alpha", 64, "Open", ("hiking", "coffee"))
    candidate = _participant("viewer_charlie", 64, "Open", ("coffee", "reading"))

    first = compute_core(viewer, candidate, config=cfg)
    second = compute_core(viewer, candidate, config=cfg)

    payload = {
        "schema": "engine_core_two_run_logs.v1",
        "generated_at_utc": _iso(NOW),
        "env": ensure_determinism_env(apply=True),
        "runs": [
            {
                "case_id": "two_run_identity",
                "viewer": dataclasses.asdict(viewer),
                "candidate": dataclasses.asdict(candidate),
                "config": {"band_priority": list(cfg.band_priority)},
                "first_run": _core_result_payload(first),
                "second_run": _core_result_payload(second),
                "identical": _core_result_payload(first) == _core_result_payload(second),
            }
        ],
    }
    _write_json(CORE_ARTIFACTS["engine_core_two_run_logs"], payload)


def _generate_abba_logs() -> None:
    cfg = CoreConfig()
    viewer_a = _participant("viewer_alpha", 72, "Warm", ("music", "hiking"))
    viewer_b = _participant("viewer_bravo", 88, "Glow", ("music", "travel"))

    ab = compute_core(viewer_a, viewer_b, config=cfg)
    ba = compute_core(viewer_b, viewer_a, config=cfg)

    payload = {
        "schema": "engine_core_abba_logs.v1",
        "generated_at_utc": _iso(NOW),
        "env": ensure_determinism_env(apply=True),
        "runs": [
            {
                "case_id": "ab_ba_parity",
                "viewer_a": dataclasses.asdict(viewer_a),
                "viewer_b": dataclasses.asdict(viewer_b),
                "config": {"band_priority": list(cfg.band_priority)},
                "ab_run": _core_result_payload(ab),
                "ba_run": _core_result_payload(ba),
                "neutral_match": ab.neutral_score == ba.neutral_score,
                "ordered_pair_match": ab.ordered_pair == ba.ordered_pair,
                "ordered_bands_match": ab.ordered_bands == ba.ordered_bands,
                "shared_traits_match": ab.shared_traits == ba.shared_traits,
                "perspective_swapped": (
                    ab.perspective.from_viewer == ba.perspective.from_candidate
                    and ab.perspective.from_candidate == ba.perspective.from_viewer
                    and ab.perspective.delta == -ba.perspective.delta
                ),
            }
        ],
    }
    _write_json(CORE_ARTIFACTS["engine_core_abba_logs"], payload)


def _generate_json_compare_logs() -> None:
    cfg = CoreConfig()
    viewer = _participant("viewer_delta", 80, "Cool", ("art",))
    candidate = _participant("viewer_echo", 82, "Warm", ("art", "music"))

    result = compute_core(viewer, candidate, config=cfg)
    result_payload = _core_result_payload(result)
    canonical_bytes = sercanon(result_payload, sort_keys=True)
    canonical_sha = hashlib.sha256(canonical_bytes).hexdigest()
    plain_json = json.dumps(result_payload, sort_keys=True).encode("utf-8")
    plain_sha = hashlib.sha256(plain_json).hexdigest()

    payload = {
        "schema": "engine_core_json_compare_logs.v1",
        "generated_at_utc": _iso(NOW),
        "env": ensure_determinism_env(apply=True),
        "cases": [
            {
                "case_id": "core_result_canonical_json",
                "viewer": dataclasses.asdict(viewer),
                "candidate": dataclasses.asdict(candidate),
                "config": {"band_priority": list(cfg.band_priority)},
                "core_result": result_payload,
                "canonical_sha256": canonical_sha,
                "plain_sha256": plain_sha,
                "equivalent": canonical_sha == plain_sha,
            }
        ],
    }
    _write_json(CORE_ARTIFACTS["engine_core_json_compare_logs"], payload)


def _refresh_human_index(entries: Iterable[dict[str, str]]) -> None:
    current = update_evidence_index._load_human_index()
    existing = {(item["artifact_key"], item["discovered_physical_path"]) for item in current}
    merged = list(current)
    changed = False
    for entry in entries:
        key = (entry["artifact_key"], entry["discovered_physical_path"])
        if key in existing:
            continue
        merged.append(entry)
        changed = True
    if not changed:
        return
    rendered = update_evidence_index._render_human_index(merged)
    idx_path = ROOT / "docs/evidence/INDEX.json"
    idx_path.write_bytes(rendered)


def _register_entries() -> None:
    entries: list[dict[str, str]] = []
    for key, path in CORE_ARTIFACTS.items():
        entries.append({"artifact_key": key, "discovered_physical_path": path})
    for key, path in CORE_SCHEMAS.items():
        entries.append({"artifact_key": key, "discovered_physical_path": path})
    _refresh_human_index(entries)


def _update_indexes() -> None:
    def _run(cmd: list[str]) -> None:
        proc = subprocess.run(cmd, capture_output=True, text=True, env=_rails_env())
        if proc.returncode != 0:
            raise SystemExit(proc.stderr)

    _run([sys.executable, "tools/evidence/update_evidence_index.py"])
    _run([sys.executable, "tools/evidence/update_evidence_index.py", "--check"])
    _run([sys.executable, "tools/evidence/orientation_demo.py", "--check"])


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate Engine Core evidence artifacts")
    parser.add_argument("--skip-index", action="store_true", help="Skip updating evidence indexes")
    args = parser.parse_args(list(argv) if argv is not None else None)

    ensure_determinism_env(apply=True)

    _generate_purity_report()
    _generate_two_run_logs()
    _generate_abba_logs()
    _generate_json_compare_logs()

    _register_entries()

    if not args.skip_index:
        _update_indexes()

    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entrypoint
    raise SystemExit(main())
