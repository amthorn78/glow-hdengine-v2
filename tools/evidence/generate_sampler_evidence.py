#!/usr/bin/env python3
"""Generate sampler evidence artifacts under closed rails (DISS003)."""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Iterable, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from adapter.factory import create_app
from engine.runtime.determinism_env import ensure_determinism_env
from engine.sampler.core import (
    CandidateFeatures,
    SamplerConfig,
    ViewerProfile,
    _is_eligible,
    _is_zero_weight,
    _resolve_band,
    build_candidate_pool,
    sample_and_rank,
)
from engine.serializer.canon import sercanon
from tools.evidence import update_evidence_index

NOW = _dt.datetime.now(tz=_dt.timezone.utc).replace(microsecond=0)

SAMPLER_ARTIFACTS: dict[str, str] = {
    "sampler_pool_snapshots": "artifacts/sampler/pool_snapshots/baseline.json",
    "sampler_two_run_logs": "artifacts/sampler/two_run/identity.json",
    "sampler_abba_logs": "artifacts/sampler/abba/ab_ba_parity.json",
    "sampler_diversity_artifacts": "artifacts/sampler/diversity/diversity_requirements.json",
    "sampler_seed_replay_logs": "artifacts/sampler/seed_replay/cli_http_seed_replay.json",
}

SAMPLER_SCHEMAS: dict[str, str] = {
    "sampler_pool_snapshots_schema": "docs/schemas/sampler/pool_snapshots.schema.json",
    "sampler_two_run_logs_schema": "docs/schemas/sampler/two_run_logs.schema.json",
    "sampler_abba_logs_schema": "docs/schemas/sampler/abba_logs.schema.json",
    "sampler_diversity_artifacts_schema": "docs/schemas/sampler/diversity_artifacts.schema.json",
    "sampler_seed_replay_logs_schema": "docs/schemas/sampler/seed_replay_logs.schema.json",
}


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


def _candidate_payload(candidate: CandidateFeatures, cfg: SamplerConfig) -> dict[str, object]:
    band = _resolve_band(candidate)
    eligible = not _is_zero_weight(candidate) and _is_eligible(candidate, band, cfg)
    reason = None
    if _is_zero_weight(candidate):
        reason = "zero_weight"
    elif not _is_eligible(candidate, band, cfg):
        if candidate.compat_score < cfg.min_compat_score:
            reason = "below_min_compat"
        elif cfg.allowed_bands is not None and band not in cfg.allowed_bands:
            reason = "disallowed_band"
        elif band in cfg.excluded_bands:
            reason = "excluded_band"
        elif cfg.require_diversity_key and not candidate.diversity_key:
            reason = "missing_diversity_key"
        else:  # pragma: no cover - defensive
            reason = "ineligible"
    return {
        "person_uid": candidate.person_uid,
        "weight": candidate.weight,
        "compat_score": candidate.compat_score,
        "band_input": candidate.band,
        "resolved_band": band,
        "diversity_key": candidate.diversity_key,
        "is_recent": candidate.is_recent,
        "eligible": eligible,
        "exclusion_reason": reason,
    }


def _ranked_payload(ranked) -> list[dict[str, object]]:
    return [
        {
            "person_uid": cand.person_uid,
            "score": cand.score,
            "weight": cand.weight,
            "band": cand.band,
            "rank": cand.rank,
            "diversity_key": cand.diversity_key,
            "is_recent": cand.is_recent,
        }
        for cand in ranked.candidates
    ]


def _generate_pool_snapshots() -> None:
    config = SamplerConfig(min_compat_score=60, excluded_bands=("Cool",))
    viewer = ViewerProfile(person_uid="viewer-pool-1")
    candidates = [
        CandidateFeatures("cool-zero", 0.0, 99, band="Glow"),
        CandidateFeatures("cool-low", 1.0, 40, band="Cool"),
        CandidateFeatures("eligible-glow", 2.0, 90, band=None, diversity_key="band-a"),
        CandidateFeatures("eligible-warm", 1.5, 70, band="Warm", diversity_key=None),
    ]
    pool = build_candidate_pool(viewer, candidates, config)

    payload = {
        "schema": "sampler_pool_snapshots.v1",
        "generated_at_utc": _iso(NOW),
        "cases": [
            {
                "case_id": "baseline_pool_filtering",
                "viewer_id": viewer.person_uid,
                "config": {
                    "min_compat_score": config.min_compat_score,
                    "excluded_bands": list(config.excluded_bands),
                    "allowed_bands": None,
                    "require_diversity_key": config.require_diversity_key,
                    "band_priority": list(config.band_priority),
                },
                "candidates": [_candidate_payload(c, config) for c in candidates],
                "pool": {
                    "viewer_id": pool.viewer_id,
                    "candidates": [
                        {
                            "person_uid": c.person_uid,
                            "weight": c.weight,
                            "compat_score": c.compat_score,
                            "band": c.band,
                            "diversity_key": c.diversity_key,
                            "is_recent": c.is_recent,
                        }
                        for c in pool.candidates
                    ],
                },
            }
        ],
    }
    _write_json(SAMPLER_ARTIFACTS["sampler_pool_snapshots"], payload)


def _generate_two_run_logs() -> None:
    viewer = ViewerProfile(person_uid="viewer-two-run")
    candidates = [
        CandidateFeatures("alpha", 2.0, 60, band="Warm"),
        CandidateFeatures("bravo", 2.0, 65, band="Warm"),
        CandidateFeatures("charlie", 1.0, 90, band="Glow"),
    ]
    first = sample_and_rank(viewer, candidates)
    second = sample_and_rank(viewer, list(candidates))
    payload = {
        "schema": "sampler_two_run_logs.v1",
        "generated_at_utc": _iso(NOW),
        "runs": [
            {
                "case_id": "two_run_identity",
                "viewer_id": viewer.person_uid,
                "seed": None,
                "input_candidate_ids": [c.person_uid for c in candidates],
                "first_run": _ranked_payload(first),
                "second_run": _ranked_payload(second),
                "identical": _ranked_payload(first) == _ranked_payload(second),
            }
        ],
    }
    _write_json(SAMPLER_ARTIFACTS["sampler_two_run_logs"], payload)


def _generate_abba_logs() -> None:
    viewer_a = ViewerProfile(person_uid="viewer-a")
    viewer_b = ViewerProfile(person_uid="viewer-b")
    raw_ab = [
        CandidateFeatures("viewer-b", 1.0, 75),
        CandidateFeatures("viewer-a", 1.0, 65),
    ]
    raw_ba = [
        CandidateFeatures("viewer-a", 1.0, 75),
        CandidateFeatures("viewer-b", 1.0, 65),
    ]
    ranked_ab = sample_and_rank(viewer_a, raw_ab)
    ranked_ba = sample_and_rank(viewer_b, raw_ba)
    payload = {
        "schema": "sampler_abba_logs.v1",
        "generated_at_utc": _iso(NOW),
        "runs": [
            {
                "case_id": "ab_ba_identity",
                "viewer_a": viewer_a.person_uid,
                "viewer_b": viewer_b.person_uid,
                "ab_run": {
                    "viewer_id": viewer_a.person_uid,
                    "ordered_ids": [c.person_uid for c in ranked_ab.candidates],
                    "ranked": _ranked_payload(ranked_ab),
                },
                "ba_run": {
                    "viewer_id": viewer_b.person_uid,
                    "ordered_ids": [c.person_uid for c in ranked_ba.candidates],
                    "ranked": _ranked_payload(ranked_ba),
                },
                "swap_consistent": (
                    ranked_ab.candidates[0].person_uid == viewer_b.person_uid
                    and ranked_ba.candidates[0].person_uid == viewer_a.person_uid
                ),
            }
        ],
    }
    _write_json(SAMPLER_ARTIFACTS["sampler_abba_logs"], payload)


def _generate_diversity_artifacts() -> None:
    config = SamplerConfig(
        min_compat_score=50,
        allowed_bands=("Glow", "Warm"),
        require_diversity_key=True,
        band_priority=("Glow", "Warm", "Open", "Cool"),
    )
    viewer = ViewerProfile(person_uid="viewer-diversity")
    candidates = [
        CandidateFeatures("diverse-a1", 1.0, 90, diversity_key="div-a", is_recent=True),
        CandidateFeatures("diverse-a2", 1.0, 80, diversity_key="div-a", is_recent=False),
        CandidateFeatures("diverse-b1", 1.0, 70, diversity_key="div-b", is_recent=False),
        CandidateFeatures("missing-div", 1.0, 85, diversity_key=None, is_recent=False),
    ]
    ranked = sample_and_rank(viewer, candidates, config=config)
    payload = {
        "schema": "sampler_diversity_artifacts.v1",
        "generated_at_utc": _iso(NOW),
        "cases": [
            {
                "case_id": "require_diversity_key_and_band_window",
                "viewer_id": viewer.person_uid,
                "config": {
                    "min_compat_score": config.min_compat_score,
                    "allowed_bands": list(config.allowed_bands) if config.allowed_bands else None,
                    "require_diversity_key": config.require_diversity_key,
                    "band_priority": list(config.band_priority),
                },
                "candidates": [_candidate_payload(c, config) for c in candidates],
                "ranked": _ranked_payload(ranked),
            }
        ],
    }
    _write_json(SAMPLER_ARTIFACTS["sampler_diversity_artifacts"], payload)


def _write_candidates_tmp(tmpdir: Path, payload: Mapping[str, object]) -> Path:
    path = tmpdir / "candidates.json"
    path.write_bytes(sercanon(payload, sort_keys=True))
    return path


def _run_dev_sampler_cli(tmpdir: Path, *, seed: str | None) -> dict[str, object]:
    candidates_payload = {
        "candidates": [
            {"person_uid": "alpha", "weight": 2, "compat_score": 70, "band": "Warm"},
            {"person_uid": "bravo", "weight": 2, "compat_score": 80, "band": "Glow"},
            {"person_uid": "charlie", "weight": 1, "compat_score": 90, "band": "Glow"},
        ]
    }
    payload_path = _write_candidates_tmp(tmpdir, candidates_payload)
    cmd = [
        sys.executable,
        "-m",
        "engine.cli",
        "dev:sampler",
        "--viewer",
        "evidence-viewer-cli",
        "--candidates-file",
        str(payload_path),
    ]
    if seed is not None:
        cmd.extend(["--seed", seed])
    proc = subprocess.run(cmd, capture_output=True, text=True, env=_rails_env())
    if proc.returncode != 0:
        raise SystemExit(proc.stderr)
    return json.loads(proc.stdout)


def _run_dev_sampler_http(seed: str | None) -> dict[str, object]:
    os.environ.setdefault("APP_ENV", "dev")
    app = create_app()
    payload = {
        "viewer_id": "evidence-viewer-http",
        "candidate_ids": ["delta", "echo", "foxtrot"],
    }
    if seed is not None:
        payload["seed"] = seed
    with app.test_client() as client:
        resp = client.post(
            "/internal/dev/sampler",
            data=json.dumps(payload),
            headers={"Content-Type": "application/json; charset=utf-8"},
        )
    if resp.status_code != 200:
        raise SystemExit(f"dev sampler HTTP failed: {resp.status_code}")
    return json.loads(resp.data)


def _generate_seed_replay_logs() -> None:
    runs: list[dict[str, object]] = []
    with tempfile.TemporaryDirectory() as tmp:
        tmpdir = Path(tmp)
        cli_first = _run_dev_sampler_cli(tmpdir, seed="seed-1")
        cli_second = _run_dev_sampler_cli(tmpdir, seed="seed-2")
        runs.append(
            {
                "harness": "cli",
                "viewer_id": cli_first.get("viewer_id"),
                "seed": cli_first.get("seed"),
                "candidate_ids": [c["person_uid"] for c in cli_first.get("candidates", [])],
                "response": cli_first,
                "ordering_equal_to_seed2": cli_first.get("candidates") == cli_second.get("candidates"),
            }
        )
        runs.append(
            {
                "harness": "cli",
                "viewer_id": cli_second.get("viewer_id"),
                "seed": cli_second.get("seed"),
                "candidate_ids": [c["person_uid"] for c in cli_second.get("candidates", [])],
                "response": cli_second,
                "ordering_equal_to_seed1": cli_second.get("candidates") == cli_first.get("candidates"),
            }
        )

    http_first = _run_dev_sampler_http(seed="http-seed-1")
    http_second = _run_dev_sampler_http(seed="http-seed-2")
    runs.append(
        {
            "harness": "http",
            "viewer_id": http_first.get("viewer_id"),
            "seed": http_first.get("meta", {}).get("seed"),
            "candidate_ids": http_first.get("candidate_ids", []),
            "response": http_first,
            "ordering_equal_to_second": http_first.get("candidate_ids") == http_second.get("candidate_ids"),
        }
    )
    runs.append(
        {
            "harness": "http",
            "viewer_id": http_second.get("viewer_id"),
            "seed": http_second.get("meta", {}).get("seed"),
            "candidate_ids": http_second.get("candidate_ids", []),
            "response": http_second,
            "ordering_equal_to_first": http_second.get("candidate_ids") == http_first.get("candidate_ids"),
        }
    )

    payload = {
        "schema": "sampler_seed_replay_logs.v1",
        "generated_at_utc": _iso(NOW),
        "runs": runs,
    }
    _write_json(SAMPLER_ARTIFACTS["sampler_seed_replay_logs"], payload)


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
    for key, path in SAMPLER_ARTIFACTS.items():
        entries.append({"artifact_key": key, "discovered_physical_path": path})
    for key, path in SAMPLER_SCHEMAS.items():
        entries.append({"artifact_key": key, "discovered_physical_path": path})
    _refresh_human_index(entries)


def _update_indexes() -> None:
    def _run(cmd: list[str]) -> None:
        proc = subprocess.run(cmd, capture_output=True, text=True, env=_rails_env())
        if proc.returncode != 0:
            raise SystemExit(proc.stderr)

    _run([sys.executable, "tools/evidence/update_evidence_index.py"])
    _run([sys.executable, "tools/evidence/orientation_demo.py"])
    _run([sys.executable, "tools/evidence/update_evidence_index.py"])
    _run([sys.executable, "tools/evidence/update_evidence_index.py", "--check"])
    _run([sys.executable, "tools/evidence/orientation_demo.py", "--check"])


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate sampler evidence artifacts")
    parser.add_argument("--skip-index", action="store_true", help="Skip updating evidence indexes")
    args = parser.parse_args(list(argv) if argv is not None else None)

    ensure_determinism_env(apply=True)

    _generate_pool_snapshots()
    _generate_two_run_logs()
    _generate_abba_logs()
    _generate_diversity_artifacts()
    _generate_seed_replay_logs()

    _register_entries()

    if not args.skip_index:
        _update_indexes()

    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entrypoint
    raise SystemExit(main())
