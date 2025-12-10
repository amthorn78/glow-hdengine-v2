"""Generic QA harness utilities shared across epic-specific scripts."""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, MutableMapping, Sequence, Tuple

from engine.runtime.determinism_env import (
    DETERMINISM_ENV_PINS,
    DeterminismEnvError,
    ensure_determinism_env,
)


@dataclass
class HarnessConfig:
    epic_id: str
    qa_root: Path
    acceptance_map_path: Path
    token_matrix_path: Path
    step_names: Sequence[str]


class CheckResult:
    def __init__(self, name: str, status: str, notes: str | None = None):
        self.name = name
        self.status = status
        self.notes = notes

    def render_line(self) -> str:
        if self.notes:
            return f"check {self.name}:{self.status} {self.notes}"
        return f"check {self.name}:{self.status}"


def validate_env_pins(environ: MutableMapping[str, str] | None = None) -> Dict[str, str]:
    """Enforce closed-rails env pins using the shared determinism helper."""

    return ensure_determinism_env(environ=environ)


def collect_env_for_logging(
    environ: Mapping[str, str] | None = None,
) -> Dict[str, str]:
    """Collect env pins for logging, defaulting to expected values when missing."""

    source = environ if environ is not None else {}
    env_pins: Dict[str, str] = {}
    for key, expected in DETERMINISM_ENV_PINS.items():
        env_pins[key] = source.get(key, expected)
    return env_pins


def summarize_checks(checks: Iterable[CheckResult]) -> str:
    for check in checks:
        if check.status.startswith("FAIL"):
            return "summary:FAIL"
    return "summary:PASS"


def write_bootstrap_log(
    config: HarnessConfig, run_id: str, checks: List[CheckResult], env_pins: Mapping[str, str]
) -> Path:
    config.qa_root.mkdir(parents=True, exist_ok=True)
    run_dir = config.qa_root / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    log_path = run_dir / "D0_bootstrap.log"
    lines = [f"run:{run_id}", f"env:{dict(env_pins)}"]
    lines.extend(check.render_line() for check in checks)
    lines.append(summarize_checks(checks))
    log_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return log_path


def write_canonical_bootstrap(
    config: HarnessConfig, checks: List[CheckResult], run_id: str, env_pins: Mapping[str, str]
) -> Path:
    lines = [
        f"run:{run_id}",
        f"env:{dict(env_pins)}",
        *(check.render_line() for check in checks),
        summarize_checks(checks),
    ]
    canonical_path = config.qa_root / "test_tooling_bootstrap.log"
    canonical_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return canonical_path


def write_step_log(
    config: HarnessConfig,
    run_id: str,
    step_name: str,
    checks: List[CheckResult],
    env_pins: Mapping[str, str],
) -> Path:
    run_dir = config.qa_root / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    log_path = run_dir / f"step_{step_name}.log"
    lines = [f"env:{dict(env_pins)}"]
    lines.extend(check.render_line() for check in checks)
    lines.append(summarize_checks(checks))
    log_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return log_path


def update_manifest(
    config: HarnessConfig, run_id: str, steps: List[Tuple[str, Path, str]]
) -> Path:
    config.qa_root.mkdir(parents=True, exist_ok=True)
    manifest_path = config.qa_root / "qa_step_logs_manifest.json"
    produced_at = datetime.now(timezone.utc).isoformat()
    manifest = {
        "epic_id": config.epic_id,
        "runs": [],
    }
    if manifest_path.exists():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            manifest = {"epic_id": config.epic_id, "runs": []}

    run_entry = {
        "run_id": run_id,
        "produced_at_utc": produced_at,
        "steps": [
            {
                "name": name,
                "status": status,
                "log_path": str(path),
            }
            for name, path, status in steps
        ],
    }

    manifest.setdefault("runs", [])
    manifest["runs"] = [run for run in manifest["runs"] if run.get("run_id") != run_id]
    manifest["epic_id"] = config.epic_id
    manifest["runs"].append(run_entry)

    tmp_path = manifest_path.with_suffix(".json.tmp")
    tmp_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    tmp_path.replace(manifest_path)
    return manifest_path


def _load_matrix_tokens(matrix_path: Path) -> Dict[str, Dict[str, str]]:
    tokens: Dict[str, Dict[str, str]] = {}
    for line in matrix_path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        parts = [part.strip() for part in line.strip().split("|") if part.strip()]
        if len(parts) < 5:
            continue
        token_name = parts[0]
        tokens[token_name] = {
            "evidence": parts[2],
            "status": parts[5] if len(parts) > 5 else "",
        }
    return tokens


def generate_acceptance_map_viability(
    config: HarnessConfig, run_id: str
) -> Tuple[Path, Dict[str, str]]:
    acceptance_map = config.acceptance_map_path
    matrix_path = config.token_matrix_path
    log_path = config.qa_root / "acceptance_map_viability.log"

    map_data = json.loads(acceptance_map.read_text(encoding="utf-8"))
    matrix_tokens = _load_matrix_tokens(matrix_path)

    covered = planned = missing = 0
    per_token_status: Dict[str, str] = {}
    lines: List[str] = [f"run:{run_id} utc:{datetime.now(timezone.utc).isoformat()}"]

    for token in map_data.get("tokens", []):
        name = token.get("name")
        if not name:
            continue
        if name not in matrix_tokens:
            status = "MISSING"
            missing += 1
            per_token_status[name] = status
            lines.append(f"token {name}: {status} missing from matrix")
            continue
        evidence_entry = matrix_tokens[name]["evidence"]
        matrix_status = matrix_tokens[name]["status"].lower()
        if matrix_status.startswith("implemented") and evidence_entry:
            status = "COVERED"
            covered += 1
        else:
            status = "PLANNED"
            planned += 1
        per_token_status[name] = status
        lines.append(f"token {name}: {status}")

    lines.append(f"summary: COVERED={covered} PLANNED={planned} MISSING={missing}")
    log_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return log_path, per_token_status

