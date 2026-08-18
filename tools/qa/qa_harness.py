"""Deterministic, current-state QA harness primitives."""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path, PurePosixPath
from typing import Iterable, Mapping, MutableMapping, Sequence

from engine.runtime.determinism_env import DETERMINISM_ENV_PINS, ensure_determinism_env

EPIC_RE = re.compile(r"HDE-EPIC([0-9]{3})\Z")
CHECK_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*\Z")
TOKEN_RE = re.compile(r"\b[A-Z][A-Z0-9]*(?:[_-][A-Z0-9]+)+\b")
PATH_RE = re.compile(r"(?<![A-Za-z0-9_./-])([A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)+)(?![A-Za-z0-9_./-])")
TOKEN_DECLARATION_RE = re.compile(
    r"^\s*(?:[*+-]\s+)?\*\*`?"
    r"(?P<name>[A-Z][A-Z0-9]*(?:(?:\\_|_|-)[A-Z0-9]+)+)"
    r"`?(?:(?:\*\*\s*[—–-])|(?:\s+[—–-].*\*\*))",
    re.VERBOSE,
)


class Status(str, Enum):
    PASS = "PASS"
    FAIL_BEHAVIOR = "FAIL_BEHAVIOR"
    FAIL_TOOLING = "FAIL_TOOLING"
    TOOLING_BLOCKED = "TOOLING_BLOCKED"
    PARKED = "PARKED"


@dataclass(frozen=True)
class HarnessConfig:
    epic_id: str
    repo_root: Path | None = None
    step_names: Sequence[str] = ()

    def __post_init__(self) -> None:
        match = EPIC_RE.fullmatch(self.epic_id)
        if not match:
            raise ValueError("epic_id must match HDE-EPIC<NNN>")
        root = (self.repo_root or Path(__file__).resolve().parents[2]).resolve()
        if not root.is_dir():
            raise ValueError("repository root is unavailable")
        object.__setattr__(self, "repo_root", root)
        object.__setattr__(self, "epic_number", match.group(1))
        object.__setattr__(self, "qa_root", root / "audit" / "qa" / f"hde-epic{match.group(1)}")
        object.__setattr__(self, "acceptance_map_path", root / "docs" / f"acceptance_map_epic{match.group(1)}.json")
        object.__setattr__(self, "token_matrix_path", self.qa_root / "token_evidence_matrix.md")
        object.__setattr__(self, "viability_ledger_path", self.qa_root / "acceptance_map_viability.log")


@dataclass(frozen=True)
class CheckResult:
    check_id: str
    status: Status
    status_reason: str = ""
    check_name: str = ""
    command: tuple[str, ...] = ()
    command_provenance: str = "Not executed"
    exit_code: int | None = None
    output: str = ""
    evidence_artifacts: tuple[str, ...] = ()
    intended_tokens: tuple[str, ...] = ()
    pf_refs: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        validate_check_id(self.check_id)
        if not isinstance(self.status, Status):
            raise ValueError("status must be a Status")


@dataclass(frozen=True)
class ViabilityResult:
    status: Status
    status_reason: str
    primary_log: Path | None
    manifest: Path | None
    governed_ledger: Path | None
    token_status: Mapping[str, str]


def validate_check_id(check_id: str) -> str:
    if not isinstance(check_id, str) or not CHECK_RE.fullmatch(check_id) or check_id in {".", ".."}:
        raise ValueError("check_id must be a safe single path segment")
    return check_id


def validate_env_pins(environ: MutableMapping[str, str] | None = None) -> dict[str, str]:
    return ensure_determinism_env(environ=environ)


def collect_env_for_logging(environ: Mapping[str, str] | None = None) -> dict[str, str]:
    source = os.environ if environ is None else environ
    keys = (*DETERMINISM_ENV_PINS.keys(), "APP_ENV")
    return {key: source[key] for key in keys if key in source}


def summarize_checks(checks: Iterable[CheckResult]) -> Status:
    statuses = [check.status for check in checks]
    if not statuses:
        return Status.TOOLING_BLOCKED
    for status in (Status.FAIL_TOOLING, Status.TOOLING_BLOCKED, Status.FAIL_BEHAVIOR, Status.PARKED):
        if status in statuses:
            return status
    return Status.PASS


def _atomic_write(path: Path, content: str) -> None:
    if not content:
        raise ValueError("refusing to write empty QA evidence")
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        Path(temporary).replace(path)
    except BaseException:
        Path(temporary).unlink(missing_ok=True)
        raise


def _repo_relative(config: HarnessConfig, path: Path) -> str:
    return path.resolve().relative_to(config.repo_root).as_posix()


def _primary_log_content(config: HarnessConfig, result: CheckResult) -> tuple[Path, str]:
    path = config.qa_root / "checks" / result.check_id / "primary.log"
    rel = _repo_relative(config, path)
    evidence = list(result.evidence_artifacts)
    if rel not in evidence:
        evidence.insert(0, rel)
    name = result.check_name or result.check_id
    reason = result.status_reason
    if result.status is Status.PASS and (result.exit_code != 0 or reason or not evidence):
        raise ValueError("PASS requires exit_code 0, no reason, and non-empty evidence")
    if result.status is not Status.PASS and not reason:
        raise ValueError("non-PASS status requires a causal reason")
    if bool(result.command) == (result.command_provenance == "Not executed"):
        raise ValueError("command provenance is inconsistent")
    header = {
        "captured_env": collect_env_for_logging(),
        "check_id": result.check_id,
        "check_name": name,
        "claimed_tokens": [],
        "command": list(result.command),
        "command_provenance": result.command_provenance,
        "evidence_artifacts": evidence,
        "exit_code": result.exit_code,
        "intended_tokens": list(result.intended_tokens),
        "pf_refs": list(result.pf_refs),
        "schema_version": "pf27.step_log_header.v2",
        "status": result.status.value,
        "status_reason": reason,
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
    }
    body = result.output.rstrip("\n")
    content = json.dumps(header, sort_keys=True, separators=(",", ":")) + "\n"
    if body:
        content += body + "\n"
    return path, content


def write_primary_log(config: HarnessConfig, result: CheckResult) -> Path:
    """Write one primary log; prefer ``record_check`` for coherent publication."""
    path, content = _primary_log_content(config, result)
    _atomic_write(path, content)
    parsed = read_primary_header(path)
    if parsed["check_id"] != result.check_id or parsed["status"] != result.status.value:
        raise RuntimeError("primary log verification failed")
    return path


def read_primary_header(path: Path) -> dict[str, object]:
    if not path.is_file() or path.stat().st_size == 0:
        raise ValueError("primary log is missing or empty")
    first = path.read_text(encoding="utf-8").splitlines()[0]
    data = json.loads(first)
    required = {"schema_version", "timestamp_utc", "check_id", "check_name", "status", "status_reason", "command", "command_provenance", "exit_code", "evidence_artifacts", "captured_env", "pf_refs", "intended_tokens", "claimed_tokens"}
    if set(data) != required or data["schema_version"] != "pf27.step_log_header.v2":
        raise ValueError("malformed PF27 v2 header")
    Status(data["status"])
    if data["claimed_tokens"] != []:
        raise ValueError("PR-03 logs cannot claim tokens")
    return data


def _preflight_manifest(config: HarnessConfig) -> dict[str, dict[str, str]]:
    path = config.qa_root / "qa_step_logs_manifest.json"
    if not path.exists():
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or payload.get("epic_id") != config.epic_id:
        raise ValueError("manifest epic identity is malformed")
    if isinstance(payload.get("checks"), dict) and set(payload) == {"checks", "epic_id"}:
        return dict(payload["checks"])
    if isinstance(payload.get("runs"), list) and set(payload) == {"epic_id", "runs"}:
        # Recognized transition envelope. Historical run data is deliberately
        # neither interpreted nor imported into current-state correctness.
        return {}
    raise ValueError("unknown QA manifest shape")


def _manifest_content(config: HarnessConfig, checks: Mapping[str, Mapping[str, str]]) -> str:
    payload = {"checks": {key: checks[key] for key in sorted(checks)}, "epic_id": config.epic_id}
    return json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n"


def update_manifest(config: HarnessConfig, log_path: Path) -> Path:
    header = read_primary_header(log_path)
    check_id = validate_check_id(str(header["check_id"]))
    expected = config.qa_root / "checks" / check_id / "primary.log"
    if log_path.resolve() != expected.resolve():
        raise ValueError("non-canonical primary log path")
    path = config.qa_root / "qa_step_logs_manifest.json"
    checks = _preflight_manifest(config)
    checks[check_id] = {"check_id": check_id, "log_path": _repo_relative(config, expected), "status": str(header["status"])}
    _atomic_write(path, _manifest_content(config, checks))
    verify_manifest_entry(config, check_id)
    return path


def verify_manifest_entry(config: HarnessConfig, check_id: str) -> dict[str, str]:
    path = config.qa_root / "qa_step_logs_manifest.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    entry = payload["checks"][check_id]
    log = config.repo_root / entry["log_path"]
    header = read_primary_header(log)
    if entry != {"check_id": check_id, "log_path": _repo_relative(config, log), "status": header["status"]}:
        raise ValueError("manifest and primary log disagree")
    return entry


def run_pytest_check(config: HarnessConfig, check_id: str, pytest_args: Sequence[str], *, check_name: str = "", intended_tokens: Sequence[str] = ()) -> CheckResult:
    command = (sys.executable, "-m", "pytest", *pytest_args)
    entrypoints = [arg for arg in pytest_args if not arg.startswith("-")]
    missing = [arg for arg in entrypoints if not (config.repo_root / arg.split("::", 1)[0]).exists()]
    if missing:
        return CheckResult(check_id, Status.TOOLING_BLOCKED, f"required pytest entrypoint unavailable: {missing[0]}", check_name, command, "epic wrapper check definition", None, intended_tokens=tuple(intended_tokens))
    readiness = subprocess.run((sys.executable, "-m", "pytest", "--version"), cwd=config.repo_root, capture_output=True, text=True, check=False)
    if readiness.returncode:
        return CheckResult(check_id, Status.TOOLING_BLOCKED, "pytest readiness check failed", check_name, command, "epic wrapper check definition", None, readiness.stdout + readiness.stderr, intended_tokens=tuple(intended_tokens))
    try:
        completed = subprocess.run(command, cwd=config.repo_root, capture_output=True, text=True, check=False)
    except (OSError, subprocess.SubprocessError) as exc:
        return CheckResult(check_id, Status.FAIL_TOOLING, f"pytest process malfunction: {exc}", check_name, command, "epic wrapper check definition", None, intended_tokens=tuple(intended_tokens))
    status = Status.PASS if completed.returncode == 0 else (Status.FAIL_TOOLING if completed.returncode in {2, 3, 4} else Status.FAIL_BEHAVIOR)
    reason = "" if status is Status.PASS else ("pytest collection/tooling failed" if status is Status.FAIL_TOOLING else "pytest assertions contradicted required behavior")
    return CheckResult(check_id, status, reason, check_name, command, "epic wrapper check definition", completed.returncode, completed.stdout + completed.stderr, intended_tokens=tuple(intended_tokens), pf_refs=("PF14 — HDE Mechanics Guide §1.6.1", "PF19 — Glow QA Guide §2.2.5", "PF27 — Plan Templates §Step-log header schema expectations (required; v2)"))


def _publish_atomically(files: Sequence[tuple[Path, str]]) -> None:
    """Publish a small related file set and restore prior bytes on failure."""
    originals = {path: path.read_bytes() if path.exists() else None for path, _ in files}
    written: list[Path] = []
    try:
        for path, content in files:
            _atomic_write(path, content)
            written.append(path)
    except BaseException:
        for path in reversed(written):
            original = originals[path]
            if original is None:
                path.unlink(missing_ok=True)
            else:
                _atomic_write(path, original.decode("utf-8"))
        raise


def record_check(
    config: HarnessConfig,
    result: CheckResult,
    *,
    additional_files: Sequence[tuple[Path, str]] = (),
) -> tuple[Path, Path]:
    """Preflight and coherently publish a primary log and manifest."""
    checks = _preflight_manifest(config)
    log, log_content = _primary_log_content(config, result)
    rel = _repo_relative(config, log)
    checks[result.check_id] = {
        "check_id": result.check_id,
        "log_path": rel,
        "status": result.status.value,
    }
    manifest = config.qa_root / "qa_step_logs_manifest.json"
    _publish_atomically(((log, log_content), (manifest, _manifest_content(config, checks)), *additional_files))
    header = read_primary_header(log)
    if header["status"] != result.status.value:
        raise RuntimeError("primary log verification failed")
    verify_manifest_entry(config, result.check_id)
    return log, manifest


def _governance_tokens(config: HarnessConfig) -> tuple[set[str] | None, str]:
    matches = sorted((config.repo_root / "docs" / "pfcanon").glob("PF04-Canon-HDE-Governance-v*.md"))
    if len(matches) != 1:
        return None, "exactly one current PF04 Governance source is required"
    try:
        text = matches[0].read_text(encoding="utf-8")
    except OSError as exc:
        return None, f"PF04 Governance source unreadable: {exc}"
    start = text.find("## **2.0 Acceptance Tokens")
    end = text.find("## **2.1 ", start)
    if start < 0 or end < 0:
        return None, "PF04 §2.0 token roster is incomplete"
    tokens: set[str] = set()
    for line in text[start:end].splitlines():
        declaration = TOKEN_DECLARATION_RE.match(line)
        if declaration:
            name = declaration.group("name").replace("\\_", "_")
            if TOKEN_RE.fullmatch(name):
                tokens.add(name)
    if not tokens:
        return None, "PF04 §2.0 token roster is empty"
    return tokens, ""


def _matrix_rows(path: Path) -> tuple[dict[str, tuple[str, ...]], str]:
    rows: dict[str, tuple[str, ...]] = {}
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        return {}, str(exc)
    for line in lines:
        if not line.lstrip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 3 or cells[0].lower().replace(" ", "_") == "token_name" or set(cells[0]) <= {"-", ":"}:
            continue
        name = cells[0]
        if not TOKEN_RE.fullmatch(name) or name in rows:
            return {}, f"malformed or duplicate matrix token row: {name}"
        references = tuple(item.strip() for item in cells[2].split(";"))
        if not references or any(not item for item in references):
            return {}, f"empty evidence reference in matrix token row: {name}"
        rows[name] = references
    return rows, "" if rows else "matrix contains no token rows"


def _resolve_reference(config: HarnessConfig, value: object) -> tuple[Path | None, str]:
    if not isinstance(value, str) or not value.strip() or value.startswith(("/", "~")):
        return None, "malformed evidence reference"
    raw = value.strip().strip("`")
    candidates = [raw] if " " not in raw and "`" not in value else PATH_RE.findall(value)
    candidates = list(dict.fromkeys(candidate.strip("`.,;:()[]") for candidate in candidates))
    if len(candidates) != 1:
        return None, "evidence reference must contain exactly one repository-relative path"
    pure = PurePosixPath(candidates[0])
    if pure.is_absolute() or ".." in pure.parts or not pure.parts:
        return None, "evidence reference traverses or is absolute"
    target = (config.repo_root / pure).resolve()
    try:
        target.relative_to(config.repo_root)
    except ValueError:
        return None, "evidence reference escapes repository"
    if not target.is_file() or target.stat().st_size == 0:
        return None, "evidence target is missing or empty"
    if target.suffix == ".json":
        try:
            parsed = json.loads(target.read_text(encoding="utf-8"))
            if parsed in ({}, [], None):
                raise ValueError("partial JSON")
        except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
            return None, "required JSON evidence is malformed or partial"
    return target, ""


def generate_acceptance_map_viability(
    config: HarnessConfig,
    check_id: str = "acceptance-map-viability",
    *,
    publish_governed_ledger: bool = False,
) -> ViabilityResult:
    """Evaluate derived acceptance inputs and record a current-state viability check."""
    validate_check_id(check_id)
    missing = [path for path in (config.acceptance_map_path, config.token_matrix_path) if not path.is_file() or path.stat().st_size == 0]
    registry, registry_error = _governance_tokens(config)
    if missing or registry is None:
        reason = registry_error or f"required input unavailable: {_repo_relative(config, missing[0])}"
        status, token_status = Status.TOOLING_BLOCKED, {}
    else:
        try:
            data = json.loads(config.acceptance_map_path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as exc:
            data, status, reason, token_status = None, Status.FAIL_TOOLING, f"acceptance-map parser failed: {exc}", {}
        if data is not None:
            tokens = data.get("tokens") if isinstance(data, dict) else None
            if data.get("epic_id") != config.epic_id or not isinstance(tokens, list):
                status, reason, token_status = Status.FAIL_BEHAVIOR, "acceptance map epic or tokens contract mismatch", {}
            else:
                names = [item.get("name") if isinstance(item, dict) else None for item in tokens]
                if any(not isinstance(name, str) or not name for name in names) or len(names) != len(set(names)):
                    status, reason, token_status = Status.FAIL_BEHAVIOR, "acceptance map has malformed or duplicate token names", {}
                elif any(name not in registry for name in names):
                    status, reason, token_status = Status.FAIL_BEHAVIOR, "acceptance map contains an unregistered token", {name: "UNREGISTERED" for name in names if name not in registry}
                else:
                    matrix, matrix_error = _matrix_rows(config.token_matrix_path)
                    if matrix_error:
                        status, reason, token_status = Status.FAIL_TOOLING, matrix_error, {}
                    elif set(matrix) != set(names):
                        status, reason, token_status = Status.FAIL_BEHAVIOR, "acceptance map and matrix token coverage differ", {name: "MISSING_MATRIX" for name in set(names) - set(matrix)} | {name: "ORPHAN_MATRIX" for name in set(matrix) - set(names)}
                    else:
                        errors: dict[str, str] = {}
                        for name, references in matrix.items():
                            reference_errors = [
                                f"reference {index}: {error}"
                                for index, reference in enumerate(references, start=1)
                                if (error := _resolve_reference(config, reference)[1])
                            ]
                            if reference_errors:
                                errors[name] = "; ".join(reference_errors)
                        status = Status.PASS if not errors else Status.FAIL_BEHAVIOR
                        reason = "" if not errors else "; ".join(f"{name}: {errors[name]}" for name in sorted(errors))
                        token_status = {name: ("VALID" if name not in errors else "INVALID_REFERENCE") for name in names}
    evaluation = {
        "epic_id": config.epic_id,
        "status": status.value,
        "status_reason": reason,
        "token_status": token_status,
    }
    evaluation_content = json.dumps(evaluation, sort_keys=True, separators=(",", ":")) + "\n"
    result = CheckResult(check_id, status, reason, "Acceptance-map viability", (), "Not executed", 0 if status is Status.PASS else None, evaluation_content, intended_tokens=(), pf_refs=("PF04 — HDE Governance §2.0", "PF14 — HDE Mechanics Guide §1.6.3", "PF19 — Glow QA Guide §4.4.5", "PF27 — Plan Templates §Step-log header schema expectations (required; v2)"))
    try:
        additional = ((config.viability_ledger_path, evaluation_content),) if publish_governed_ledger else ()
        log, manifest = record_check(config, result, additional_files=additional)
        verify_manifest_entry(config, check_id)
        governed_ledger = config.viability_ledger_path if publish_governed_ledger else None
        if governed_ledger is not None and governed_ledger.read_text(encoding="utf-8") != evaluation_content:
            raise RuntimeError("governed viability ledger verification failed")
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as exc:
        return ViabilityResult(Status.FAIL_TOOLING, f"viability evidence writer failed: {exc}", None, None, None, token_status)
    return ViabilityResult(status, reason, log, manifest, governed_ledger, token_status)


def require_governed_viability(result: ViabilityResult, expected_path: Path) -> Path:
    """Fail closed unless a generator received its verified PASS ledger."""
    ledger = result.governed_ledger
    if result.status is not Status.PASS:
        raise SystemExit(f"ACCEPTANCE_MAP_VIABILITY_{result.status.value}:{result.status_reason}")
    if ledger is None or ledger.resolve() != expected_path.resolve():
        raise SystemExit("ACCEPTANCE_MAP_VIABILITY_LEDGER_MISMATCH")
    if not ledger.is_file() or ledger.stat().st_size == 0:
        raise SystemExit("ACCEPTANCE_MAP_VIABILITY_LEDGER_MISSING")
    try:
        payload = json.loads(ledger.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise SystemExit(f"ACCEPTANCE_MAP_VIABILITY_LEDGER_MALFORMED:{exc}") from exc
    match = re.fullmatch(r"hde-epic([0-9]{3})", expected_path.parent.name)
    expected_epic = f"HDE-EPIC{match.group(1)}" if match else None
    if payload.get("epic_id") != expected_epic or payload.get("status") != Status.PASS.value:
        raise SystemExit("ACCEPTANCE_MAP_VIABILITY_LEDGER_STALE_OR_MISMATCHED")
    if expected_epic is None:
        raise SystemExit("ACCEPTANCE_MAP_VIABILITY_LEDGER_MISMATCH")
    config = HarnessConfig(expected_epic, repo_root=expected_path.parents[3])
    if result.primary_log is None or result.manifest is None:
        raise SystemExit("ACCEPTANCE_MAP_VIABILITY_CURRENT_STATE_MISSING")
    if result.primary_log.resolve() != (config.qa_root / "checks/acceptance-map-viability/primary.log").resolve():
        raise SystemExit("ACCEPTANCE_MAP_VIABILITY_PRIMARY_MISMATCH")
    if result.manifest.resolve() != (config.qa_root / "qa_step_logs_manifest.json").resolve():
        raise SystemExit("ACCEPTANCE_MAP_VIABILITY_MANIFEST_MISMATCH")
    try:
        verify_manifest_entry(config, "acceptance-map-viability")
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        raise SystemExit(f"ACCEPTANCE_MAP_VIABILITY_CURRENT_STATE_INVALID:{exc}") from exc
    return ledger
