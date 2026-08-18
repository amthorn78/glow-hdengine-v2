"""Deterministic, current-state QA harness primitives."""

from __future__ import annotations

import json
import os
import re
import shlex
import subprocess
import sys
import tempfile
from collections.abc import Callable, Iterable, Mapping, MutableMapping, Sequence
from dataclasses import dataclass, replace
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path, PurePosixPath

from engine.runtime.determinism_env import DETERMINISM_ENV_PINS, ensure_determinism_env

EPIC_RE = re.compile(r"HDE-EPIC([0-9]{3})\Z")
CHECK_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*\Z")
PF_TITLE_RE = re.compile(
    r"PF[0-9]{2}(?:\.[0-9]+)?-(?:Canon|Reference)-[A-Za-z0-9][A-Za-z0-9-]*\Z"
)
TOKEN_RE = re.compile(r"\b[A-Z][A-Z0-9]*(?:[_-][A-Z0-9]+)+\b")
PATH_RE = re.compile(
    r"(?<![A-Za-z0-9_./-])([A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)+)(?![A-Za-z0-9_./-])"
)
EXACT_RELATIVE_PATH_RE = re.compile(r"[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*\Z")
PLACEHOLDER_RE = re.compile(r"(?:<[^>]+>|\{[^}]+\}|\bTBD\b|\be\.g\.)", re.IGNORECASE)
TOKEN_DECLARATION_RE = re.compile(
    r"^\s*(?:[*+-]\s+)?\*\*`?"
    r"(?P<name>[A-Z][A-Z0-9]*(?:(?:\\_|_|-)[A-Z0-9]+)+)"
    r"`?(?:(?:\*\*\s*[—–-])|(?:\s+[—–-].*\*\*))",
    re.VERBOSE,
)
UTC_TIMESTAMP_RE = re.compile(
    r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z\Z"
)
ADMITTED_ENV_KEYS = frozenset((*DETERMINISM_ENV_PINS.keys(), "APP_ENV"))
NONCLAIM_EXPLANATION = "token_claim_posture: intended tokens are recorded but not claimed by this PR-03 receipt"


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
        object.__setattr__(
            self, "qa_root", root / "audit" / "qa" / f"hde-epic{match.group(1)}"
        )
        object.__setattr__(
            self,
            "acceptance_map_path",
            root / "docs" / f"acceptance_map_epic{match.group(1)}.json",
        )
        object.__setattr__(
            self, "token_matrix_path", self.qa_root / "token_evidence_matrix.md"
        )
        object.__setattr__(
            self, "viability_ledger_path", self.qa_root / "acceptance_map_viability.log"
        )


@dataclass(frozen=True)
class CheckResult:
    check_id: str
    status: Status
    status_reason: str = ""
    check_name: str = ""
    command: tuple[str, ...] | tuple[tuple[str, ...], ...] = ()
    command_provenance: str = "Not executed"
    exit_code: int | None = None
    output: str = ""
    evidence_artifacts: tuple[str, ...] = ()
    intended_tokens: tuple[str, ...] = ()
    pf_refs: tuple[str, ...] = ()
    captured_env: tuple[tuple[str, str], ...] = ()

    def __post_init__(self) -> None:
        validate_check_id(self.check_id)
        if not isinstance(self.status, Status):
            raise ValueError("status must be a Status")  # noqa: TRY004
        _validate_command(self.command)
        if self.exit_code is not None and (
            not isinstance(self.exit_code, int) or isinstance(self.exit_code, bool)
        ):
            raise ValueError("exit_code must be an integer or None")
        if bool(self.command) != (self.exit_code is not None):
            raise ValueError("command execution and exit_code presence disagree")
        if any(
            not isinstance(reference, str) or not PF_TITLE_RE.fullmatch(reference)
            for reference in self.pf_refs
        ):
            raise ValueError("pf_refs must contain exact in-document PF titles")
        _validate_captured_env(self.captured_env)


@dataclass(frozen=True)
class AcceptanceTokenEntry:
    name: str
    owner_pf: str
    evidence_titles: tuple[str, ...]


@dataclass(frozen=True)
class MatrixRow:
    token_name: str
    owner_pf: str
    evidence_artifacts: tuple[str, ...]
    ci_tests_jobs: tuple[str, ...]
    qa_root_logs: tuple[str, ...]
    status: str
    notes: str


@dataclass(frozen=True)
class PytestCollectionRequest:
    selectors: tuple[str, ...]
    options: tuple[str, ...]


@dataclass(frozen=True)
class ReferenceDiagnostic:
    token: str
    source_field: str
    item_index: int
    value: str
    status: Status
    reason: str = ""
    resolved_path: str | None = None

    def as_dict(self) -> dict[str, object]:
        return {
            "item_index": self.item_index,
            "reason": self.reason,
            "resolved_path": self.resolved_path,
            "source_field": self.source_field,
            "status": self.status.value,
            "token": self.token,
            "value": self.value,
        }


@dataclass(frozen=True)
class ViabilityResult:
    status: Status
    status_reason: str
    primary_log: Path | None
    manifest: Path | None
    governed_ledger: Path | None
    token_status: Mapping[str, str]


def validate_check_id(check_id: str) -> str:
    if (
        not isinstance(check_id, str)
        or not CHECK_RE.fullmatch(check_id)
        or check_id in {".", ".."}
    ):
        raise ValueError("check_id must be a safe single path segment")
    return check_id


def validate_env_pins(
    environ: MutableMapping[str, str] | None = None,
) -> dict[str, str]:
    return ensure_determinism_env(environ=environ)


def collect_env_for_logging(environ: Mapping[str, str] | None = None) -> dict[str, str]:
    source = os.environ if environ is None else environ
    keys = (*DETERMINISM_ENV_PINS.keys(), "APP_ENV")
    return {key: source[key] for key in keys if key in source}


def _validate_command(command: object) -> None:
    if command == ():
        return
    if not isinstance(command, tuple) or not command:
        raise ValueError(
            "command must be an argv tuple or an ordered tuple of argv tuples"
        )
    if all(isinstance(part, str) for part in command):
        if any(not part for part in command):
            raise ValueError("command argv cannot contain empty strings")
        return
    if all(isinstance(argv, tuple) for argv in command):
        if any(
            not argv or any(not isinstance(part, str) or not part for part in argv)
            for argv in command
        ):
            raise ValueError("every command argv must contain only non-empty strings")
        return
    raise ValueError("command cannot mix argv strings and nested argv tuples")


def _serialized_command(
    command: tuple[str, ...] | tuple[tuple[str, ...], ...],
) -> list[str] | list[list[str]]:
    _validate_command(command)
    if command and isinstance(command[0], tuple):
        return [list(argv) for argv in command]
    return list(command)


def _validate_captured_env(captured_env: object) -> None:
    if not isinstance(captured_env, tuple):
        raise TypeError("captured_env must be an immutable tuple of key/value pairs")
    seen: set[str] = set()
    for item in captured_env:
        if (
            not isinstance(item, tuple)
            or len(item) != 2
            or not all(isinstance(value, str) for value in item)
        ):
            raise ValueError("captured_env entries must be string key/value pairs")
        key, _ = item
        if key not in ADMITTED_ENV_KEYS or key in seen:
            raise ValueError("captured_env contains a duplicate or non-admitted key")
        seen.add(key)


def _captured_env(result: CheckResult) -> dict[str, str]:
    if result.captured_env:
        return dict(result.captured_env)
    return collect_env_for_logging()


def _validate_timestamp(value: str) -> str:
    if not isinstance(value, str) or not UTC_TIMESTAMP_RE.fullmatch(value):
        raise ValueError("captured_at_utc must use second-precision UTC Z form")
    try:
        parsed = datetime.fromisoformat(value.removesuffix("Z") + "+00:00")
    except ValueError as exc:
        raise ValueError("captured_at_utc is not a valid UTC timestamp") from exc
    if parsed.tzinfo != timezone.utc:
        raise ValueError("captured_at_utc must be UTC")
    return value


def _utc_now() -> str:
    return (
        datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    )


def summarize_checks(checks: Iterable[CheckResult]) -> Status:
    statuses = [check.status for check in checks]
    if not statuses:
        return Status.TOOLING_BLOCKED
    for status in (
        Status.FAIL_TOOLING,
        Status.TOOLING_BLOCKED,
        Status.FAIL_BEHAVIOR,
        Status.PARKED,
    ):
        if status in statuses:
            return status
    return Status.PASS


def _atomic_write(path: Path, content: str) -> None:
    if not content:
        raise ValueError("refusing to write empty QA evidence")
    _atomic_write_bytes(path, content.encode("utf-8"))


def _atomic_write_bytes(
    path: Path, content: bytes, *, allow_empty: bool = False
) -> None:
    if not content and not allow_empty:
        raise ValueError("refusing to write empty QA evidence")
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        Path(temporary).replace(path)
    except BaseException:
        Path(temporary).unlink(missing_ok=True)
        raise


def _repo_relative(config: HarnessConfig, path: Path) -> str:
    return path.resolve().relative_to(config.repo_root).as_posix()


def _primary_log_content(
    config: HarnessConfig,
    result: CheckResult,
    *,
    captured_at_utc: str | None = None,
) -> tuple[Path, str]:
    path = config.qa_root / "checks" / result.check_id / "primary.log"
    rel = _repo_relative(config, path)
    evidence = list(result.evidence_artifacts)
    if rel not in evidence:
        evidence.insert(0, rel)
    name = result.check_name or result.check_id
    reason = result.status_reason
    command_executed = bool(result.command)
    if command_executed != (result.exit_code is not None):
        raise ValueError("command execution and exit_code presence disagree")
    if result.status is Status.PASS and (
        result.exit_code != 0 or reason or not evidence
    ):
        raise ValueError(
            "PASS requires successful executed commands when present, no reason, and evidence"
        )
    if result.status is not Status.PASS and not reason:
        raise ValueError("non-PASS status requires a causal reason")
    if bool(result.command) == (result.command_provenance == "Not executed"):
        raise ValueError("command provenance is inconsistent")
    header = {
        "captured_env": _captured_env(result),
        "check_id": result.check_id,
        "check_name": name,
        "claimed_tokens": [],
        "command": _serialized_command(result.command),
        "command_provenance": result.command_provenance,
        "evidence_artifacts": evidence,
        "exit_code": result.exit_code,
        "intended_tokens": list(result.intended_tokens),
        "pf_refs": list(result.pf_refs),
        "schema_version": "pf27.step_log_header.v2",
        "status": result.status.value,
        "status_reason": reason,
        "timestamp_utc": _validate_timestamp(captured_at_utc or _utc_now()),
    }
    body = result.output.rstrip("\n")
    if (
        result.status is Status.PASS
        and result.intended_tokens
        and NONCLAIM_EXPLANATION not in body.splitlines()
    ):
        body = f"{body}\n{NONCLAIM_EXPLANATION}" if body else NONCLAIM_EXPLANATION
    content = json.dumps(header, sort_keys=True, separators=(",", ":")) + "\n"
    if body:
        content += body + "\n"
    return path, content


def write_primary_log(config: HarnessConfig, result: CheckResult) -> Path:
    """Write one primary log; prefer ``record_check`` for coherent publication."""
    path, content = _primary_log_content(config, result)
    _publish_with_rollback(
        ((path, content),),
        lambda: _verify_written_primary(path, result.check_id, result.status),
        repo_root=config.repo_root,
    )
    return path


def read_primary_header(path: Path) -> dict[str, object]:
    if not path.is_file() or path.stat().st_size == 0:
        raise ValueError("primary log is missing or empty")
    first = path.read_text(encoding="utf-8").splitlines()[0]
    data = _loads_json_strict(first)
    required = {
        "schema_version",
        "timestamp_utc",
        "check_id",
        "check_name",
        "status",
        "status_reason",
        "command",
        "command_provenance",
        "exit_code",
        "evidence_artifacts",
        "captured_env",
        "pf_refs",
        "intended_tokens",
        "claimed_tokens",
    }
    if (
        not isinstance(data, dict)
        or set(data) != required
        or data["schema_version"] != "pf27.step_log_header.v2"
    ):
        raise ValueError("malformed PF27 v2 header")
    check_id = validate_check_id(data["check_id"])
    if not isinstance(data["check_name"], str) or not data["check_name"]:
        raise ValueError("malformed PF27 v2 check_name")
    status = Status(data["status"])
    if not isinstance(data["status_reason"], str):
        raise ValueError("malformed PF27 v2 status_reason")  # noqa: TRY004
    command = data["command"]
    if not isinstance(command, list):
        raise ValueError("malformed PF27 v2 command")  # noqa: TRY004
    normalized_command: tuple[str, ...] | tuple[tuple[str, ...], ...]
    if command and all(isinstance(part, list) for part in command):
        normalized_command = tuple(tuple(part) for part in command)
    else:
        normalized_command = tuple(command)
    _validate_command(normalized_command)
    if (
        not isinstance(data["command_provenance"], str)
        or not data["command_provenance"]
    ):
        raise ValueError("malformed PF27 v2 command_provenance")
    if bool(command) == (data["command_provenance"] == "Not executed"):
        raise ValueError("PF27 v2 command provenance is inconsistent")
    if data["exit_code"] is not None and (
        not isinstance(data["exit_code"], int) or isinstance(data["exit_code"], bool)
    ):
        raise ValueError("malformed PF27 v2 exit_code")
    if bool(command) != (data["exit_code"] is not None):
        raise ValueError("PF27 v2 command execution and exit_code presence disagree")
    for field in ("evidence_artifacts", "pf_refs", "intended_tokens", "claimed_tokens"):
        if not isinstance(data[field], list) or any(
            not isinstance(item, str) or not item for item in data[field]
        ):
            raise ValueError(f"malformed PF27 v2 {field}")
    if any(not PF_TITLE_RE.fullmatch(reference) for reference in data["pf_refs"]):
        raise ValueError("PF27 v2 pf_refs are not exact in-document PF titles")
    if not data["evidence_artifacts"]:
        raise ValueError("PF27 v2 evidence_artifacts cannot be empty")
    if not isinstance(data["captured_env"], dict) or any(
        key not in ADMITTED_ENV_KEYS or not isinstance(value, str)
        for key, value in data["captured_env"].items()
    ):
        raise ValueError("malformed PF27 v2 captured_env")
    _validate_timestamp(data["timestamp_utc"])
    if status is Status.PASS and (
        data["exit_code"] != 0 or data["status_reason"]
    ):
        raise ValueError("PF27 v2 PASS causality is malformed")
    if status is not Status.PASS and not data["status_reason"]:
        raise ValueError("PF27 v2 non-PASS status lacks a causal reason")
    if data["claimed_tokens"] != []:
        raise ValueError("PR-03 logs cannot claim tokens")
    if status is Status.PASS and data["intended_tokens"]:
        body_lines = path.read_text(encoding="utf-8").splitlines()[1:]
        if NONCLAIM_EXPLANATION not in body_lines:
            raise ValueError(
                "PF27 v2 PASS with intended tokens lacks an explicit nonclaim"
            )
    if data["check_id"] != check_id:
        raise ValueError("malformed PF27 v2 check_id")
    return data


def _verify_written_primary(path: Path, check_id: str, status: Status) -> None:
    parsed = read_primary_header(path)
    if parsed["check_id"] != check_id or parsed["status"] != status.value:
        raise RuntimeError("primary log verification failed")


def _read_supported_primary_header(
    path: Path, *, expected_check_id: str
) -> dict[str, object]:
    if not path.is_file() or path.stat().st_size == 0:
        raise ValueError("primary log is missing or empty")
    first = path.read_text(encoding="utf-8").splitlines()[0]
    if first.startswith("["):
        raise ValueError(
            f"unsupported primary-log schema without governed status: {expected_check_id}"
        )
    try:
        data = _loads_json_strict(first)
    except (json.JSONDecodeError, ValueError) as exc:
        raise ValueError(
            f"unsupported primary-log schema: {expected_check_id}"
        ) from exc
    if not isinstance(data, dict):
        raise ValueError(  # noqa: TRY004
            f"unsupported primary-log schema: {expected_check_id}"
        )
    schema = data.get("schema_version")
    if schema == "pf27.step_log_header.v2":
        data = read_primary_header(path)
    elif schema == "pf27.step_log_header.v1":
        if data.get("check_id") != expected_check_id:
            raise ValueError(
                "manifest key, entry, and primary header check identity disagree"
            )
        try:
            Status(data.get("status"))
        except (TypeError, ValueError) as exc:
            raise ValueError("PF27 v1 primary header has an invalid status") from exc
    else:
        raise ValueError(f"unsupported primary-log JSON schema: {schema!r}")
    if data.get("check_id") != expected_check_id:
        raise ValueError(
            "manifest key, entry, and primary header check identity disagree"
        )
    return data


def _manifest_entry_log_path(
    config: HarnessConfig,
    check_id: str,
    entry: object,
    *,
    require_nonempty: bool = True,
) -> Path:
    validate_check_id(check_id)
    if not isinstance(entry, dict) or entry.get("check_id") != check_id:
        raise ValueError("manifest key and entry check identity disagree")
    raw_path = entry.get("log_path")
    if not isinstance(raw_path, str) or not raw_path or "\\" in raw_path:
        raise ValueError("manifest log path is malformed")
    pure = PurePosixPath(raw_path)
    if pure.is_absolute() or ".." in pure.parts or "." in pure.parts:
        raise ValueError("manifest log path traverses or is absolute")
    expected = config.qa_root / "checks" / check_id / "primary.log"
    allowed = {
        PurePosixPath("checks") / check_id / "primary.log",
        PurePosixPath(_repo_relative(config, expected)),
    }
    if pure not in allowed:
        raise ValueError(
            "manifest log path is foreign, noncanonical, or check-mismatched"
        )
    if require_nonempty and (not expected.is_file() or expected.stat().st_size == 0):
        raise ValueError("manifest primary log is missing or empty")
    return expected


def _manifest_payload(config: HarnessConfig) -> object:
    path = config.qa_root / "qa_step_logs_manifest.json"
    try:
        return _loads_json_strict(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        raise ValueError(f"QA manifest is unreadable or malformed: {exc}") from exc


def _manifest_shape(
    config: HarnessConfig, payload: object
) -> tuple[str, Mapping[str, object]]:
    if not isinstance(payload, dict):
        raise ValueError("unknown QA manifest shape")  # noqa: TRY004
    if set(payload) == {"epic_id", "checks"}:
        if payload.get("epic_id") != config.epic_id or not isinstance(
            payload.get("checks"), dict
        ):
            raise ValueError("manifest epic identity or checks mapping is malformed")
        return "wrapped-checks", payload["checks"]
    if set(payload) == {"epic_id", "runs"}:
        if payload.get("epic_id") != config.epic_id or not isinstance(
            payload.get("runs"), list
        ):
            raise ValueError("historical manifest envelope is malformed")
        return "historical-runs", {}
    if not payload or (
        not ({"epic_id", "checks", "runs"} & set(payload))
        and all(
            isinstance(key, str) and CHECK_RE.fullmatch(key) and isinstance(value, dict)
            for key, value in payload.items()
        )
    ):
        return "flat-checks", payload
    raise ValueError("unknown QA manifest shape: mixed or unsupported structure")


def _normalize_manifest_checks(
    config: HarnessConfig,
    checks: Mapping[str, object],
) -> dict[str, dict[str, str]]:
    normalized: dict[str, dict[str, str]] = {}
    for check_id in sorted(checks):
        entry = checks[check_id]
        log = _manifest_entry_log_path(config, check_id, entry)
        header = _read_supported_primary_header(log, expected_check_id=check_id)
        assert isinstance(entry, dict)
        allowed_fields = {
            "check_id",
            "check_name",
            "fail_status",
            "log_path",
            "status",
            "timestamp_utc",
        }
        if not {"check_id", "log_path", "status"} <= set(entry) or not set(
            entry
        ) <= allowed_fields:
            raise ValueError("manifest entry has missing or unsupported fields")
        if any(
            not isinstance(entry[field], str)
            for field in set(entry) - {"check_id", "log_path"}
        ):
            raise ValueError("manifest entry metadata must be strings")
        if (
            header.get("schema_version") == "pf27.step_log_header.v2"
            and entry.get("status") != header.get("status")
        ):
            raise ValueError("canonical manifest status disagrees with primary header")
        normalized[check_id] = {
            "check_id": check_id,
            "log_path": _repo_relative(config, log),
            "status": Status(header["status"]).value,
        }
    return normalized


def _preflight_manifest(config: HarnessConfig) -> dict[str, dict[str, str]]:
    path = config.qa_root / "qa_step_logs_manifest.json"
    if not path.exists():
        return {}
    shape, checks = _manifest_shape(config, _manifest_payload(config))
    if shape == "historical-runs":
        # Historical run records are recognized but never imported into
        # current-state correctness.
        return {}
    return _normalize_manifest_checks(config, checks)


def _preflight_legacy_family_replacement(
    config: HarnessConfig,
    expected_ids: set[str],
) -> None:
    path = config.qa_root / "qa_step_logs_manifest.json"
    if not path.is_file() or path.stat().st_size == 0:
        raise ValueError(
            "complete-family replacement requires an existing legacy manifest"
        )
    shape, checks = _manifest_shape(config, _manifest_payload(config))
    if shape != "wrapped-checks" or set(checks) != expected_ids:
        raise ValueError(
            "legacy replacement manifest is partial, extra, or not the expected wrapper"
        )
    for check_id in sorted(expected_ids):
        # This bounded transition validates identity, path safety, and bytes,
        # but deliberately does not infer or trust a bracket log status.
        _manifest_entry_log_path(config, check_id, checks[check_id])


def _manifest_content(checks: Mapping[str, Mapping[str, str]]) -> str:
    payload = {key: dict(checks[key]) for key in sorted(checks)}
    return json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n"


def update_manifest(config: HarnessConfig, log_path: Path) -> Path:
    header = _read_supported_primary_header(
        log_path,
        expected_check_id=validate_check_id(log_path.parent.name),
    )
    check_id = validate_check_id(str(header["check_id"]))
    expected = config.qa_root / "checks" / check_id / "primary.log"
    if log_path.resolve() != expected.resolve():
        raise ValueError("non-canonical primary log path")
    path = config.qa_root / "qa_step_logs_manifest.json"
    checks = _preflight_manifest(config)
    checks[check_id] = {
        "check_id": check_id,
        "log_path": _repo_relative(config, expected),
        "status": str(header["status"]),
    }
    expected_content = _manifest_content(checks)
    _publish_with_rollback(
        ((path, expected_content),),
        lambda: _verify_flat_manifest(config, checks),
        repo_root=config.repo_root,
    )
    return path


def verify_manifest_entry(config: HarnessConfig, check_id: str) -> dict[str, str]:
    path = config.qa_root / "qa_step_logs_manifest.json"
    payload = _loads_json_strict(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or check_id not in payload:
        raise ValueError("canonical flat manifest entry is missing")
    entry = payload[check_id]
    log = config.repo_root / entry["log_path"]
    header = _read_supported_primary_header(log, expected_check_id=check_id)
    if entry != {
        "check_id": check_id,
        "log_path": _repo_relative(config, log),
        "status": header["status"],
    }:
        raise ValueError("manifest and primary log disagree")
    return entry


def _verify_flat_manifest(
    config: HarnessConfig,
    expected: Mapping[str, Mapping[str, str]],
) -> None:
    path = config.qa_root / "qa_step_logs_manifest.json"
    if not path.is_file() or path.stat().st_size == 0:
        raise ValueError("canonical flat manifest is missing or empty")
    payload = _loads_json_strict(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or payload != {
        key: dict(expected[key]) for key in sorted(expected)
    }:
        raise ValueError(
            "canonical flat manifest bytes or entries disagree with the staged family"
        )
    for check_id in sorted(expected):
        verify_manifest_entry(config, check_id)


def run_pytest_check(
    config: HarnessConfig,
    check_id: str,
    pytest_args: Sequence[str],
    *,
    check_name: str = "",
    intended_tokens: Sequence[str] = (),
) -> CheckResult:
    command = (sys.executable, "-m", "pytest", *pytest_args)
    readiness_command = (sys.executable, "-m", "pytest", "--version")
    entrypoints = [arg for arg in pytest_args if not arg.startswith("-")]
    missing = [
        arg
        for arg in entrypoints
        if not (config.repo_root / arg.split("::", 1)[0]).exists()
    ]
    if missing:
        return CheckResult(
            check_id,
            Status.TOOLING_BLOCKED,
            f"required pytest entrypoint unavailable: {missing[0]}",
            check_name,
            (),
            "Not executed",
            None,
            intended_tokens=(),
        )
    try:
        readiness = subprocess.run(
            readiness_command,
            cwd=config.repo_root,
            capture_output=True,
            text=True,
            check=False,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        return CheckResult(
            check_id,
            Status.FAIL_TOOLING,
            f"pytest readiness process malfunction: {exc}",
            check_name,
            (),
            "Not executed",
            None,
            intended_tokens=tuple(intended_tokens),
        )
    if readiness.returncode:
        return CheckResult(
            check_id,
            Status.TOOLING_BLOCKED,
            "pytest readiness check failed",
            check_name,
            readiness_command,
            "epic wrapper readiness command",
            readiness.returncode,
            readiness.stdout + readiness.stderr,
            intended_tokens=(),
        )
    try:
        completed = subprocess.run(
            command, cwd=config.repo_root, capture_output=True, text=True, check=False
        )
    except (OSError, subprocess.SubprocessError) as exc:
        return CheckResult(
            check_id,
            Status.FAIL_TOOLING,
            f"pytest process malfunction: {exc}",
            check_name,
            readiness_command,
            "epic wrapper readiness completed; test command launch failed",
            readiness.returncode,
            intended_tokens=tuple(intended_tokens),
        )
    status = (
        Status.PASS
        if completed.returncode == 0
        else (
            Status.TOOLING_BLOCKED
            if completed.returncode == 5
            else (
                Status.FAIL_TOOLING
                if completed.returncode in {2, 3, 4}
                else Status.FAIL_BEHAVIOR
            )
        )
    )
    reason = (
        ""
        if status is Status.PASS
        else (
            "pytest collected no required tests"
            if status is Status.TOOLING_BLOCKED
            else (
                "pytest collection/tooling failed"
                if status is Status.FAIL_TOOLING
                else "pytest assertions contradicted required behavior"
            )
        )
    )
    return CheckResult(
        check_id,
        status,
        reason,
        check_name,
        (readiness_command, command),
        "epic wrapper readiness and test commands; exact ordered argv",
        completed.returncode,
        completed.stdout + completed.stderr,
        intended_tokens=(
            () if status is Status.TOOLING_BLOCKED else tuple(intended_tokens)
        ),
        pf_refs=(
            "PF14-Canon-HDE-Mechanics-Guide",
            "PF19-Canon-Glow-QA-Guide",
            "PF27-Canon-Plan-Templates",
        ),
    )


def _publish_with_rollback(
    files: Sequence[tuple[Path, str]],
    verifier: Callable[[], None],
    *,
    repo_root: Path,
) -> None:
    """Publish and verify a related file family inside one rollback boundary."""
    if not files:
        raise ValueError("publication family cannot be empty")
    resolved_paths = [path.resolve() for path, _ in files]
    if len(resolved_paths) != len(set(resolved_paths)):
        raise ValueError("publication family contains duplicate output paths")
    for path, content in files:
        if path.is_symlink():
            raise ValueError("publication output cannot be a symlink")
        ancestor = path.parent
        while ancestor != repo_root:
            if ancestor.is_symlink():
                raise ValueError("publication output parent cannot be a symlink")
            if ancestor == ancestor.parent:
                break
            ancestor = ancestor.parent
        try:
            path.resolve().relative_to(repo_root)
        except ValueError as exc:
            raise ValueError("publication output escapes repository") from exc
        if not content:
            raise ValueError("publication output cannot be empty")
    originals = {
        path: path.read_bytes() if path.exists() else None for path, _ in files
    }
    absent_parents: set[Path] = set()
    for path, _ in files:
        parent = path.parent
        while parent != repo_root and not parent.exists():
            absent_parents.add(parent)
            parent = parent.parent
    try:
        for path, content in files:
            _atomic_write(path, content)
        for path, content in files:
            if not path.is_file() or path.stat().st_size == 0:
                raise RuntimeError(f"published output is missing or empty: {path}")
            if path.read_bytes() != content.encode("utf-8"):
                raise RuntimeError(f"published output bytes disagree: {path}")
        verifier()
    except BaseException as publish_error:
        rollback_errors: list[BaseException] = []
        for path, _ in reversed(tuple(files)):
            try:
                original = originals[path]
                if original is None:
                    path.unlink(missing_ok=True)
                else:
                    _atomic_write_bytes(path, original, allow_empty=True)
            except BaseException as exc:  # noqa: BLE001  # pragma: no cover
                rollback_errors.append(exc)
        for parent in sorted(
            absent_parents, key=lambda item: len(item.parts), reverse=True
        ):
            try:
                parent.rmdir()
            except OSError:
                pass
        if rollback_errors:  # pragma: no cover - catastrophic filesystem failure
            raise RuntimeError(
                "publication failed and rollback was incomplete"
            ) from publish_error
        raise


def _publish_atomically(files: Sequence[tuple[Path, str]]) -> None:
    """Backward-compatible transactional writer without extra coherence checks."""
    if not files:
        raise ValueError("publication family cannot be empty")
    common = Path(os.path.commonpath([str(path.resolve()) for path, _ in files]))
    repo_root = common if common.is_dir() else common.parent
    _publish_with_rollback(files, lambda: None, repo_root=repo_root)


def record_check(
    config: HarnessConfig,
    result: CheckResult,
    *,
    additional_files: Sequence[tuple[Path, str]] = (),
) -> tuple[Path, Path]:
    """Preflight and coherently publish one primary log and the flat manifest."""
    logs, manifest = record_check_family(
        config,
        (result,),
        additional_files=additional_files,
    )
    return logs[0], manifest


def record_check_family(
    config: HarnessConfig,
    results: Sequence[CheckResult],
    *,
    additional_files: Sequence[tuple[Path, str]] = (),
    coherence_verifier: Callable[[], None] | None = None,
    replace_legacy_family_ids: Sequence[str] = (),
    admit_new_check_ids: Sequence[str] = (),
    captured_at_utc: str | None = None,
) -> tuple[tuple[Path, ...], Path]:
    """Publish a complete current-state family with all verification in-boundary."""
    staged_results = tuple(results)
    if not staged_results:
        raise ValueError("check family cannot be empty")
    result_ids = [result.check_id for result in staged_results]
    if len(result_ids) != len(set(result_ids)):
        raise ValueError("check family contains duplicate check IDs")
    replacement_ids = {
        validate_check_id(check_id) for check_id in replace_legacy_family_ids
    }
    admitted_ids = {validate_check_id(check_id) for check_id in admit_new_check_ids}
    if replacement_ids & admitted_ids:
        raise ValueError("replacement and admitted check IDs must be disjoint")
    if replacement_ids:
        if set(result_ids) != replacement_ids | admitted_ids:
            raise ValueError(
                "fresh family is partial, extra, or missing an explicitly admitted check"
            )
        _preflight_legacy_family_replacement(config, replacement_ids)
        checks: dict[str, dict[str, str]] = {}
    else:
        if admitted_ids:
            raise ValueError(
                "admitted check IDs require a bounded legacy-family replacement"
            )
        checks = _preflight_manifest(config)
    family_timestamp = _validate_timestamp(captured_at_utc or _utc_now())
    rendered: list[tuple[Path, str]] = []
    logs: list[Path] = []
    for result in staged_results:
        log, content = _primary_log_content(
            config,
            result,
            captured_at_utc=family_timestamp,
        )
        logs.append(log)
        rendered.append((log, content))
        checks[result.check_id] = {
            "check_id": result.check_id,
            "log_path": _repo_relative(config, log),
            "status": result.status.value,
        }
    manifest = config.qa_root / "qa_step_logs_manifest.json"
    staged_files = (
        *rendered,
        (manifest, _manifest_content(checks)),
        *tuple(additional_files),
    )

    def verify_family() -> None:
        for log, result in zip(logs, staged_results, strict=True):
            _verify_written_primary(log, result.check_id, result.status)
        _verify_flat_manifest(config, checks)
        if coherence_verifier is not None:
            coherence_verifier()

    _publish_with_rollback(
        staged_files,
        verify_family,
        repo_root=config.repo_root,
    )
    return tuple(logs), manifest


def _governance_tokens(config: HarnessConfig) -> tuple[set[str] | None, str]:
    matches = sorted(
        (config.repo_root / "docs" / "pfcanon").glob("PF04-Canon-HDE-Governance-v*.md")
    )
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


def _normalized_cell(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")


def _is_matrix_header(cells: Sequence[str]) -> bool:
    if len(cells) != 7:
        return False
    normalized = [_normalized_cell(cell) for cell in cells]
    return (
        normalized[0] == "token_name"
        and "owner" in normalized[1]
        and normalized[2].startswith("evidence_artifacts")
        and "ci" in normalized[3]
        and ("test" in normalized[3] or "job" in normalized[3])
        and normalized[4].startswith("qa_root_logs")
        and normalized[5] == "status"
        and normalized[6] == "notes"
    )


def _split_reference_items(
    value: str, *, field: str, token_name: str
) -> tuple[str, ...]:
    items = tuple(item.strip() for item in value.split(";"))
    if not items or any(not item for item in items):
        raise ValueError(f"empty {field} reference in matrix token row: {token_name}")
    return items


def _matrix_rows(path: Path) -> tuple[dict[str, MatrixRow], str]:
    rows: dict[str, MatrixRow] = {}
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        return {}, str(exc)
    found_header = False
    for line in lines:
        if not line.lstrip().startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if _is_matrix_header(cells):
            found_header = True
            continue
        if cells and set(cells[0]) <= {"-", ":"}:
            continue
        if not found_header:
            continue
        if len(cells) != 7:
            return {}, "token matrix row does not contain exactly seven columns"
        name = cells[0]
        if not TOKEN_RE.fullmatch(name) or name in rows:
            return {}, f"malformed or duplicate matrix token row: {name}"
        if any(not cells[index] for index in (1, 2, 3, 4, 5, 6)):
            return {}, f"matrix token row has an empty required column: {name}"
        try:
            evidence = _split_reference_items(
                cells[2], field="evidence_artifacts", token_name=name
            )
            ci = _split_reference_items(
                cells[3], field="ci_tests_jobs", token_name=name
            )
            qa = _split_reference_items(cells[4], field="qa_root_logs", token_name=name)
        except ValueError as exc:
            return {}, str(exc)
        rows[name] = MatrixRow(name, cells[1], evidence, ci, qa, cells[5], cells[6])
    if not found_header:
        return {}, "matrix is missing the complete seven-column header"
    return rows, "" if rows else "matrix contains no token rows"


def _extract_reference_path(value: object) -> tuple[PurePosixPath | None, Status, str]:
    if not isinstance(value, str) or not value.strip():
        return None, Status.TOOLING_BLOCKED, "reference is missing or non-string"
    stripped = value.strip()
    if PLACEHOLDER_RE.search(stripped) or "*" in stripped:
        return (
            None,
            Status.TOOLING_BLOCKED,
            "reference contains a wildcard or placeholder",
        )
    if stripped.startswith(("/", "~")) or "\\" in stripped:
        return (
            None,
            Status.FAIL_BEHAVIOR,
            "reference is absolute or uses a non-repository separator",
        )
    unwrapped = (
        stripped[1:-1].strip()
        if stripped.startswith("`") and stripped.endswith("`")
        else stripped
    )
    if EXACT_RELATIVE_PATH_RE.fullmatch(unwrapped):
        candidates = [unwrapped]
    else:
        candidates = [
            candidate.strip("`.,;:()[]") for candidate in PATH_RE.findall(stripped)
        ]
    candidates = list(dict.fromkeys(candidate for candidate in candidates if candidate))
    if not candidates:
        return (
            None,
            Status.TOOLING_BLOCKED,
            "reference contains no supported repository-relative path",
        )
    if len(candidates) != 1:
        return (
            None,
            Status.FAIL_BEHAVIOR,
            "reference contains multiple ambiguous repository-relative paths",
        )
    pure = PurePosixPath(candidates[0])
    if pure.is_absolute() or not pure.parts or ".." in pure.parts or "." in pure.parts:
        return None, Status.FAIL_BEHAVIOR, "reference traverses or is absolute"
    return pure, Status.PASS, ""


def _repo_target(config: HarnessConfig, pure: PurePosixPath) -> Path:
    target = (config.repo_root / pure).resolve()
    try:
        target.relative_to(config.repo_root)
    except ValueError as exc:
        raise ValueError("reference escapes repository") from exc
    return target


def _validate_json_evidence(path: Path) -> None:
    try:
        parsed = _loads_json_strict(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError("required JSON evidence is malformed or partial") from exc
    if parsed in ({}, [], None):
        raise ValueError("required JSON evidence is malformed or partial")


def _reject_duplicate_json_keys(
    pairs: Sequence[tuple[str, object]],
) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON object key: {key}")
        result[key] = value
    return result


def _loads_json_strict(text: str) -> object:
    return json.loads(text, object_pairs_hook=_reject_duplicate_json_keys)


def _file_diagnostic(
    config: HarnessConfig,
    *,
    token: str,
    source_field: str,
    item_index: int,
    value: object,
    planned_paths: set[Path],
    referenced_manifests: set[str],
) -> ReferenceDiagnostic:
    pure, status, reason = _extract_reference_path(value)
    rendered = value if isinstance(value, str) else repr(value)
    if pure is None:
        return ReferenceDiagnostic(
            token, source_field, item_index, rendered, status, reason
        )
    try:
        target = _repo_target(config, pure)
    except ValueError as exc:
        return ReferenceDiagnostic(
            token, source_field, item_index, rendered, Status.FAIL_BEHAVIOR, str(exc)
        )
    relative = _repo_relative(config, target)
    manifest_path = config.qa_root / "qa_step_logs_manifest.json"
    if target == manifest_path:
        referenced_manifests.add(relative)
        if target.exists():
            try:
                _preflight_manifest(config)
            except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as exc:
                return ReferenceDiagnostic(
                    token,
                    source_field,
                    item_index,
                    rendered,
                    Status.FAIL_TOOLING,
                    f"referenced manifest is untrustworthy: {exc}",
                    relative,
                )
        elif target not in planned_paths:
            return ReferenceDiagnostic(
                token,
                source_field,
                item_index,
                rendered,
                Status.TOOLING_BLOCKED,
                "referenced manifest is missing",
                relative,
            )
        return ReferenceDiagnostic(
            token,
            source_field,
            item_index,
            rendered,
            Status.PASS,
            resolved_path=relative,
        )
    if target in planned_paths:
        return ReferenceDiagnostic(
            token,
            source_field,
            item_index,
            rendered,
            Status.PASS,
            resolved_path=relative,
        )
    if not target.is_file() or target.stat().st_size == 0:
        return ReferenceDiagnostic(
            token,
            source_field,
            item_index,
            rendered,
            Status.TOOLING_BLOCKED,
            "referenced file is missing or empty",
            relative,
        )
    if target.suffix == ".json":
        try:
            _validate_json_evidence(target)
        except ValueError as exc:
            return ReferenceDiagnostic(
                token,
                source_field,
                item_index,
                rendered,
                Status.FAIL_TOOLING,
                str(exc),
                relative,
            )
    return ReferenceDiagnostic(
        token, source_field, item_index, rendered, Status.PASS, resolved_path=relative
    )


def _qa_diagnostic(
    config: HarnessConfig,
    *,
    token: str,
    item_index: int,
    value: object,
    planned_paths: set[Path],
    referenced_manifests: set[str],
) -> ReferenceDiagnostic:
    source_field = "matrix.qa_root_logs"
    pure, status, reason = _extract_reference_path(value)
    rendered = value if isinstance(value, str) else repr(value)
    if pure is None:
        return ReferenceDiagnostic(
            token, source_field, item_index, rendered, status, reason
        )
    qa_prefix = PurePosixPath(_repo_relative(config, config.qa_root))
    if pure.parts[:2] == ("audit", "qa"):
        if pure.parts[: len(qa_prefix.parts)] != qa_prefix.parts:
            return ReferenceDiagnostic(
                token,
                source_field,
                item_index,
                rendered,
                Status.FAIL_BEHAVIOR,
                "QA locator points to a foreign epic",
            )
        target = _repo_target(config, pure)
    else:
        target = (config.qa_root / pure).resolve()
    try:
        target.relative_to(config.qa_root)
    except ValueError:
        return ReferenceDiagnostic(
            token,
            source_field,
            item_index,
            rendered,
            Status.FAIL_BEHAVIOR,
            "QA locator escapes the epic QA root",
        )
    return _file_diagnostic(
        config,
        token=token,
        source_field=source_field,
        item_index=item_index,
        value=_repo_relative(config, target),
        planned_paths=planned_paths,
        referenced_manifests=referenced_manifests,
    )


def _resolve_reference(config: HarnessConfig, value: object) -> tuple[Path | None, str]:
    diagnostic = _file_diagnostic(
        config,
        token="",
        source_field="evidence",
        item_index=1,
        value=value,
        planned_paths=set(),
        referenced_manifests=set(),
    )
    if diagnostic.status is not Status.PASS or diagnostic.resolved_path is None:
        return None, diagnostic.reason
    return config.repo_root / diagnostic.resolved_path, ""


def _command_path(
    config: HarnessConfig,
    raw: str,
    *,
    require_executable: bool = False,
) -> tuple[Path | None, Status, str]:
    pure, status, reason = _extract_reference_path(raw)
    if pure is None:
        return None, status, reason
    try:
        target = _repo_target(config, pure)
    except ValueError as exc:
        return None, Status.FAIL_BEHAVIOR, str(exc)
    if not target.is_file() or target.stat().st_size == 0:
        return (
            None,
            Status.TOOLING_BLOCKED,
            "required script or test file is missing or empty",
        )
    if require_executable and not os.access(target, os.X_OK):
        return (
            None,
            Status.TOOLING_BLOCKED,
            "required bare script is not executable",
        )
    return target, Status.PASS, ""


def _ci_diagnostic(
    config: HarnessConfig,
    *,
    token: str,
    item_index: int,
    value: object,
) -> tuple[ReferenceDiagnostic, PytestCollectionRequest | None]:
    source_field = "matrix.ci_tests_jobs"
    rendered = value if isinstance(value, str) else repr(value)
    if not isinstance(value, str) or not value.strip():
        return (
            ReferenceDiagnostic(
                token,
                source_field,
                item_index,
                rendered,
                Status.TOOLING_BLOCKED,
                "CI/test locator is missing or non-string",
            ),
            None,
        )
    if PLACEHOLDER_RE.search(value) or "*" in value:
        return (
            ReferenceDiagnostic(
                token,
                source_field,
                item_index,
                rendered,
                Status.TOOLING_BLOCKED,
                "CI/test locator contains a wildcard or placeholder",
            ),
            None,
        )
    try:
        argv = shlex.split(value)
    except ValueError as exc:
        return (
            ReferenceDiagnostic(
                token,
                source_field,
                item_index,
                rendered,
                Status.FAIL_TOOLING,
                f"CI/test locator parser failed: {exc}",
            ),
            None,
        )
    if not argv or any(part in {"&&", "||", "|", ">", ">>"} for part in argv):
        return (
            ReferenceDiagnostic(
                token,
                source_field,
                item_index,
                rendered,
                Status.FAIL_BEHAVIOR,
                "CI/test locator contains an unsupported shell composition",
            ),
            None,
        )
    pytest_args: list[str] | None = None
    script_arg: str | None = None
    bare_script = False
    if argv[0] == "python" and len(argv) >= 3 and argv[1:3] == ["-m", "pytest"]:
        pytest_args = argv[3:]
    elif argv[0] == "pytest":
        pytest_args = argv[1:]
    elif argv[0] == "python" and len(argv) >= 2 and not argv[1].startswith("-"):
        script_arg = argv[1]
    elif "/" in argv[0] or argv[0].endswith((".py", ".sh")):
        script_arg = argv[0]
        bare_script = True
    else:
        return (
            ReferenceDiagnostic(
                token,
                source_field,
                item_index,
                rendered,
                Status.TOOLING_BLOCKED,
                "CI/test locator is prose or uses an unsupported command form",
            ),
            None,
        )
    if script_arg is not None:
        script_position = argv.index(script_arg)
        if any(
            not argument.startswith("-") for argument in argv[script_position + 1 :]
        ):
            return (
                ReferenceDiagnostic(
                    token,
                    source_field,
                    item_index,
                    rendered,
                    Status.TOOLING_BLOCKED,
                    "script locator contains unsupported prose or positional arguments",
                ),
                None,
            )
        target, status, reason = _command_path(
            config, script_arg, require_executable=bare_script
        )
        return (
            ReferenceDiagnostic(
                token,
                source_field,
                item_index,
                rendered,
                status,
                reason,
                _repo_relative(config, target) if target is not None else None,
            ),
            None,
        )
    selectors_list: list[str] = []
    options: list[str] = []
    arguments = tuple(pytest_args or ())
    argument_index = 0
    option_error = ""
    while argument_index < len(arguments):
        argument = arguments[argument_index]
        if argument in {"-q", "--quiet", "--collect-only"}:
            options.append(argument)
            argument_index += 1
            continue
        if argument == "-p":
            if (
                argument_index + 1 >= len(arguments)
                or arguments[argument_index + 1] != "no:cacheprovider"
            ):
                option_error = "pytest locator admits only -p no:cacheprovider"
                break
            options.extend((argument, arguments[argument_index + 1]))
            argument_index += 2
            continue
        if argument in {"-k", "-m"}:
            if argument_index + 1 >= len(arguments):
                option_error = f"pytest locator option {argument} lacks its expression"
                break
            options.extend((argument, arguments[argument_index + 1]))
            argument_index += 2
            continue
        if (argument.startswith("-k") or argument.startswith("-m")) and len(
            argument
        ) > 2:
            options.append(argument)
            argument_index += 1
            continue
        if argument.startswith("-"):
            option_error = f"pytest locator uses unsupported option: {argument}"
            break
        if ".py" not in argument:
            option_error = "pytest locator contains unsupported positional prose"
            break
        selectors_list.append(argument)
        argument_index += 1
    if option_error:
        return (
            ReferenceDiagnostic(
                token,
                source_field,
                item_index,
                rendered,
                Status.TOOLING_BLOCKED,
                option_error,
            ),
            None,
        )
    selectors = tuple(selectors_list)
    if not selectors:
        return (
            ReferenceDiagnostic(
                token,
                source_field,
                item_index,
                rendered,
                Status.TOOLING_BLOCKED,
                "pytest locator does not name a repository test file or node",
            ),
            None,
        )
    for selector in selectors:
        base = selector.split("::", 1)[0]
        target, status, reason = _command_path(config, base)
        if target is None:
            return (
                ReferenceDiagnostic(
                    token, source_field, item_index, rendered, status, reason
                ),
                None,
            )
    first_target = config.repo_root / selectors[0].split("::", 1)[0]
    return (
        ReferenceDiagnostic(
            token,
            source_field,
            item_index,
            rendered,
            Status.PASS,
            resolved_path=_repo_relative(config, first_target),
        ),
        PytestCollectionRequest(
            selectors=selectors,
            options=tuple(options),
        ),
    )


def _collect_pytest_file(
    config: HarnessConfig,
    test_file: str,
    pytest_options: tuple[str, ...],
    temp_root: Path,
) -> tuple[
    Status,
    str,
    frozenset[str],
    tuple[str, ...] | None,
    int | None,
]:
    command = (
        sys.executable,
        "-m",
        "pytest",
        "--collect-only",
        "-q",
        "-p",
        "no:cacheprovider",
        f"--basetemp={temp_root}",
        *pytest_options,
        test_file,
    )
    source_env = os.environ
    runtime_bin = str(Path(sys.executable).parent)
    inherited_path = source_env.get("PATH", "")
    env = {
        **DETERMINISM_ENV_PINS,
        "PATH": runtime_bin
        + (os.pathsep + inherited_path if inherited_path else ""),
        "PYTHONDONTWRITEBYTECODE": "1",
    }
    if "APP_ENV" in source_env:
        env["APP_ENV"] = source_env["APP_ENV"]
    try:
        completed = subprocess.run(
            command,
            cwd=config.repo_root,
            capture_output=True,
            text=True,
            check=False,
            env=env,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        return (
            Status.FAIL_TOOLING,
            f"pytest collection process malfunction: {exc}",
            frozenset(),
            None,
            None,
        )
    output = f"{completed.stdout}\n{completed.stderr}"
    lowered = output.lower()
    if completed.returncode != 0:
        if (
            completed.returncode == 5
            or "not found:" in lowered
            or "no tests collected" in lowered
        ):
            return (
                Status.TOOLING_BLOCKED,
                f"pytest file is unavailable: {test_file}",
                frozenset(),
                command,
                completed.returncode,
            )
        if "no module named pytest" in lowered:
            return (
                Status.TOOLING_BLOCKED,
                "pytest collection prerequisite is unavailable",
                frozenset(),
                command,
                completed.returncode,
            )
        return (
            Status.FAIL_TOOLING,
            f"pytest collection/import failed for: {test_file}",
            frozenset(),
            command,
            completed.returncode,
        )
    node_lines = frozenset(
        line.strip() for line in completed.stdout.splitlines() if "::" in line
    )
    return Status.PASS, "", node_lines, command, completed.returncode


def _apply_pytest_collection(
    config: HarnessConfig,
    diagnostics: list[ReferenceDiagnostic],
    requests: Mapping[int, PytestCollectionRequest],
) -> tuple[tuple[tuple[str, ...], int], ...]:
    if not requests:
        return ()
    cache: dict[
        tuple[str, tuple[str, ...]],
        tuple[
            Status,
            str,
            frozenset[str],
            tuple[str, ...] | None,
            int | None,
        ],
    ] = {}
    receipts: list[tuple[tuple[str, ...], int]] = []
    try:
        temporary = tempfile.TemporaryDirectory(prefix="qa-harness-pytest-")
    except OSError as exc:
        for index in requests:
            diagnostics[index] = replace(
                diagnostics[index],
                status=Status.FAIL_TOOLING,
                reason=f"temporary pytest collection root failed: {exc}",
            )
        return ()
    with temporary as root:
        for diagnostic_index, request in requests.items():
            selector_results: list[tuple[Status, str]] = []
            for selector in request.selectors:
                test_file = selector.split("::", 1)[0]
                cache_key = (test_file, request.options)
                if cache_key not in cache:
                    cache[cache_key] = _collect_pytest_file(
                        config,
                        test_file,
                        request.options,
                        Path(root) / f"collection-{len(cache)}",
                    )
                    _, _, _, executed_command, exit_code = cache[cache_key]
                    if executed_command is not None and exit_code is not None:
                        receipts.append((executed_command, exit_code))
                status, selector_reason, nodes, _, _ = cache[cache_key]
                if (
                    status is Status.PASS
                    and "::" in selector
                    and not any(
                        node == selector
                        or node.startswith((f"{selector}[", f"{selector}::"))
                        for node in nodes
                    )
                ):
                    status = Status.TOOLING_BLOCKED
                    selector_reason = (
                        f"pytest node was not collected exactly: {selector}"
                    )
                selector_results.append((status, selector_reason))
            statuses = [status for status, _ in selector_results]
            final = _status_rollup(statuses)
            if final is not Status.PASS:
                reason = next(
                    reason
                    for status, reason in selector_results
                    if status is final and reason
                )
                diagnostics[diagnostic_index] = replace(
                    diagnostics[diagnostic_index], status=final, reason=reason
                )
    return tuple(receipts)


def _status_rollup(statuses: Iterable[Status]) -> Status:
    observed = tuple(statuses)
    for status in (
        Status.FAIL_TOOLING,
        Status.TOOLING_BLOCKED,
        Status.FAIL_BEHAVIOR,
        Status.PARKED,
    ):
        if status in observed:
            return status
    return Status.PASS


def _planned_qa_paths(
    config: HarnessConfig,
    check_id: str,
    *,
    planned_governed_ledger: bool,
) -> set[Path]:
    planned = {
        (config.qa_root / "qa_step_logs_manifest.json").resolve(),
        (config.qa_root / "checks" / check_id / "primary.log").resolve(),
    }
    if planned_governed_ledger:
        planned.add(config.viability_ledger_path.resolve())
    for step_name in config.step_names:
        validate_check_id(step_name)
        planned.add((config.qa_root / f"{step_name}.log").resolve())
        planned.add((config.qa_root / "checks" / step_name / "primary.log").resolve())
        planned.add(
            (
                config.qa_root / "checks" / step_name.replace("_", "-") / "primary.log"
            ).resolve()
        )
    return planned


def evaluate_acceptance_map_viability(
    config: HarnessConfig,
    check_id: str = "acceptance-map-viability",
    *,
    planned_governed_ledger: bool = False,
    proof_command: tuple[str, ...] | tuple[tuple[str, ...], ...] | None = None,
    proof_command_provenance: str = (
        "Current process invocation containing the approved in-process "
        "acceptance-map viability proof action"
    ),
) -> tuple[CheckResult, str]:
    """Evaluate every governed map/matrix reference without publishing files."""
    validate_check_id(check_id)
    issues: list[tuple[Status, str]] = []
    diagnostics: list[ReferenceDiagnostic] = []
    collection_requests: dict[int, PytestCollectionRequest] = {}
    referenced_manifests: set[str] = set()
    planned_paths = _planned_qa_paths(
        config,
        check_id,
        planned_governed_ledger=planned_governed_ledger,
    )
    entries: list[AcceptanceTokenEntry] = []
    matrix: dict[str, MatrixRow] = {}

    registry, registry_error = _governance_tokens(config)
    if registry is None:
        issues.append((Status.TOOLING_BLOCKED, registry_error))

    if (
        not config.acceptance_map_path.is_file()
        or config.acceptance_map_path.stat().st_size == 0
    ):
        issues.append(
            (
                Status.TOOLING_BLOCKED,
                f"required input unavailable: {_repo_relative(config, config.acceptance_map_path)}",
            )
        )
        data: object = None
    else:
        try:
            data = _loads_json_strict(
                config.acceptance_map_path.read_text(encoding="utf-8")
            )
        except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
            data = None
            issues.append((Status.FAIL_TOOLING, f"acceptance-map parser failed: {exc}"))
    if data is not None:
        if not isinstance(data, dict) or data.get("epic_id") != config.epic_id:
            issues.append(
                (
                    Status.FAIL_BEHAVIOR,
                    "acceptance map epic identity is malformed or mismatched",
                )
            )
        tokens = data.get("tokens") if isinstance(data, dict) else None
        if not isinstance(tokens, list) or not tokens:
            issues.append(
                (Status.FAIL_BEHAVIOR, "acceptance map tokens must be a non-empty list")
            )
        else:
            for token_index, item in enumerate(tokens, start=1):
                if not isinstance(item, dict):
                    issues.append(
                        (
                            Status.FAIL_BEHAVIOR,
                            f"acceptance token entry {token_index} is not an object",
                        )
                    )
                    continue
                name = item.get("name")
                owner_pf = item.get("owner_pf")
                evidence_titles = item.get("evidence_titles")
                if not isinstance(name, str) or not TOKEN_RE.fullmatch(name):
                    issues.append(
                        (
                            Status.FAIL_BEHAVIOR,
                            f"acceptance token entry {token_index} has an invalid name",
                        )
                    )
                    continue
                if not isinstance(owner_pf, str) or not owner_pf.strip():
                    issues.append(
                        (
                            Status.FAIL_BEHAVIOR,
                            f"acceptance token {name} has a missing or invalid owner_pf",
                        )
                    )
                    continue
                if (
                    not isinstance(evidence_titles, list)
                    or not evidence_titles
                    or any(
                        not isinstance(value, str) or not value.strip()
                        for value in evidence_titles
                    )
                ):
                    issues.append(
                        (
                            Status.FAIL_BEHAVIOR,
                            f"acceptance token {name} has malformed or empty evidence_titles",
                        )
                    )
                    continue
                entries.append(
                    AcceptanceTokenEntry(name, owner_pf.strip(), tuple(evidence_titles))
                )
            names = [entry.name for entry in entries]
            if len(names) != len(set(names)):
                issues.append(
                    (Status.FAIL_BEHAVIOR, "acceptance map has duplicate token names")
                )

    if (
        not config.token_matrix_path.is_file()
        or config.token_matrix_path.stat().st_size == 0
    ):
        issues.append(
            (
                Status.TOOLING_BLOCKED,
                f"required input unavailable: {_repo_relative(config, config.token_matrix_path)}",
            )
        )
    else:
        matrix, matrix_error = _matrix_rows(config.token_matrix_path)
        if matrix_error:
            issues.append((Status.FAIL_TOOLING, matrix_error))

    entry_names = {entry.name for entry in entries}
    matrix_names = set(matrix)
    if entries and matrix and entry_names != matrix_names:
        issues.append(
            (Status.FAIL_BEHAVIOR, "acceptance map and matrix token coverage differ")
        )
    for entry in entries:
        matrix_row = matrix.get(entry.name)
        if matrix_row is not None and entry.owner_pf != matrix_row.owner_pf:
            issues.append(
                (
                    Status.FAIL_BEHAVIOR,
                    f"acceptance map and matrix owner_pf disagree for {entry.name}",
                )
            )
    if registry is not None:
        for name in sorted(entry_names - registry):
            issues.append(
                (
                    Status.FAIL_BEHAVIOR,
                    f"acceptance map contains unregistered token: {name}",
                )
            )

    for entry in entries:
        for item_index, value in enumerate(entry.evidence_titles, start=1):
            diagnostics.append(
                _file_diagnostic(
                    config,
                    token=entry.name,
                    source_field="acceptance_map.evidence_titles",
                    item_index=item_index,
                    value=value,
                    planned_paths=planned_paths,
                    referenced_manifests=referenced_manifests,
                )
            )
    for token_name in sorted(matrix):
        row = matrix[token_name]
        for item_index, value in enumerate(row.evidence_artifacts, start=1):
            diagnostics.append(
                _file_diagnostic(
                    config,
                    token=token_name,
                    source_field="matrix.evidence_artifacts",
                    item_index=item_index,
                    value=value,
                    planned_paths=planned_paths,
                    referenced_manifests=referenced_manifests,
                )
            )
        for item_index, value in enumerate(row.ci_tests_jobs, start=1):
            diagnostic, collection_request = _ci_diagnostic(
                config,
                token=token_name,
                item_index=item_index,
                value=value,
            )
            diagnostic_index = len(diagnostics)
            diagnostics.append(diagnostic)
            if collection_request is not None and diagnostic.status is Status.PASS:
                collection_requests[diagnostic_index] = collection_request
        for item_index, value in enumerate(row.qa_root_logs, start=1):
            diagnostics.append(
                _qa_diagnostic(
                    config,
                    token=token_name,
                    item_index=item_index,
                    value=value,
                    planned_paths=planned_paths,
                    referenced_manifests=referenced_manifests,
                )
            )
    collection_receipts = _apply_pytest_collection(
        config, diagnostics, collection_requests
    )

    broken = [
        diagnostic for diagnostic in diagnostics if diagnostic.status is not Status.PASS
    ]
    all_statuses = [status for status, _ in issues] + [
        diagnostic.status for diagnostic in broken
    ]
    final_status = _status_rollup(all_statuses)
    final_reasons = [reason for status, reason in issues if status is final_status]
    final_reasons.extend(
        f"{diagnostic.token} {diagnostic.source_field}[{diagnostic.item_index}]: {diagnostic.reason}"
        for diagnostic in broken
        if diagnostic.status is final_status
    )
    reason = "; ".join(dict.fromkeys(final_reasons))

    token_status: dict[str, str] = {}
    for name in sorted(entry_names | matrix_names):
        if registry is not None and name not in registry:
            token_status[name] = "UNREGISTERED"
        elif name not in matrix_names:
            token_status[name] = "MISSING_MATRIX"
        elif name not in entry_names:
            token_status[name] = "ORPHAN_MATRIX"
        else:
            token_diagnostics = [item.status for item in broken if item.token == name]
            token_status[name] = (
                _status_rollup(token_diagnostics).value
                if token_diagnostics
                else "VALID"
            )
    source_fields = (
        "acceptance_map.evidence_titles",
        "matrix.evidence_artifacts",
        "matrix.ci_tests_jobs",
        "matrix.qa_root_logs",
    )
    resolved_counts = {
        source_field: sum(
            diagnostic.status is Status.PASS and diagnostic.source_field == source_field
            for diagnostic in diagnostics
        )
        for source_field in source_fields
    }
    evaluation = {
        "acceptance_map_path": _repo_relative(config, config.acceptance_map_path),
        "broken_references": [diagnostic.as_dict() for diagnostic in broken],
        "epic_id": config.epic_id,
        "referenced_manifests": sorted(referenced_manifests),
        "resolved_reference_counts": resolved_counts,
        "status": final_status.value,
        "status_reason": reason,
        "token_reference_disposition": token_status,
        "token_status": token_status,
    }
    evaluation_content = (
        json.dumps(evaluation, sort_keys=True, separators=(",", ":")) + "\n"
    )
    executed_command: tuple[str, ...] | tuple[tuple[str, ...], ...]
    exit_code: int | None
    command_provenance: str
    if len(collection_receipts) == 1:
        executed_command = collection_receipts[0][0]
        exit_code = collection_receipts[0][1]
        command_provenance = "Exact pytest collection argv executed by the viability walker"
    elif collection_receipts:
        executed_command = tuple(command for command, _ in collection_receipts)
        exit_code = collection_receipts[-1][1]
        command_provenance = (
            "Exact ordered pytest collection argv executed by the viability walker"
        )
    elif final_status is Status.PASS:
        executed_command = proof_command or (sys.executable, *sys.argv)
        _validate_command(executed_command)
        if not executed_command or not proof_command_provenance:
            raise ValueError(
                "PASS viability requires an exact command or approved proof action"
            )
        exit_code = 0
        command_provenance = proof_command_provenance
    else:
        executed_command = ()
        exit_code = None
        command_provenance = "Not executed"
    result = CheckResult(
        check_id=check_id,
        status=final_status,
        status_reason=reason,
        check_name="Acceptance-map viability",
        command=executed_command,
        command_provenance=command_provenance,
        exit_code=exit_code,
        output=evaluation_content,
        intended_tokens=(),
        pf_refs=(
            "PF04-Canon-HDE-Governance",
            "PF14-Canon-HDE-Mechanics-Guide",
            "PF19-Canon-Glow-QA-Guide",
            "PF27-Canon-Plan-Templates",
        ),
    )
    return result, evaluation_content


def generate_acceptance_map_viability(
    config: HarnessConfig,
    check_id: str = "acceptance-map-viability",
    *,
    publish_governed_ledger: bool = False,
) -> ViabilityResult:
    """Evaluate and publish a current-state acceptance-map viability check."""
    result, evaluation_content = evaluate_acceptance_map_viability(
        config,
        check_id,
        planned_governed_ledger=publish_governed_ledger,
    )
    token_status = _loads_json_strict(evaluation_content)["token_status"]
    try:
        additional = (
            ((config.viability_ledger_path, evaluation_content),)
            if publish_governed_ledger
            else ()
        )
        log, manifest = record_check(config, result, additional_files=additional)
        verify_manifest_entry(config, check_id)
        governed_ledger = (
            config.viability_ledger_path if publish_governed_ledger else None
        )
        if (
            governed_ledger is not None
            and governed_ledger.read_text(encoding="utf-8") != evaluation_content
        ):
            raise RuntimeError("governed viability ledger verification failed")
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as exc:
        return ViabilityResult(
            Status.FAIL_TOOLING,
            f"viability evidence writer failed: {exc}",
            None,
            None,
            None,
            token_status,
        )
    return ViabilityResult(
        result.status,
        result.status_reason,
        log,
        manifest,
        governed_ledger,
        token_status,
    )


def require_governed_viability(result: ViabilityResult, expected_path: Path) -> Path:
    """Fail closed unless a generator received its verified PASS ledger."""
    ledger = result.governed_ledger
    if result.status is not Status.PASS:
        raise SystemExit(
            f"ACCEPTANCE_MAP_VIABILITY_{result.status.value}:{result.status_reason}"
        )
    if ledger is None or ledger.resolve() != expected_path.resolve():
        raise SystemExit("ACCEPTANCE_MAP_VIABILITY_LEDGER_MISMATCH")
    if not ledger.is_file() or ledger.stat().st_size == 0:
        raise SystemExit("ACCEPTANCE_MAP_VIABILITY_LEDGER_MISSING")
    try:
        payload = _loads_json_strict(ledger.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        raise SystemExit(f"ACCEPTANCE_MAP_VIABILITY_LEDGER_MALFORMED:{exc}") from exc
    match = re.fullmatch(r"hde-epic([0-9]{3})", expected_path.parent.name)
    expected_epic = f"HDE-EPIC{match.group(1)}" if match else None
    if (
        payload.get("epic_id") != expected_epic
        or payload.get("status") != Status.PASS.value
    ):
        raise SystemExit("ACCEPTANCE_MAP_VIABILITY_LEDGER_STALE_OR_MISMATCHED")
    if expected_epic is None:
        raise SystemExit("ACCEPTANCE_MAP_VIABILITY_LEDGER_MISMATCH")
    config = HarnessConfig(expected_epic, repo_root=expected_path.parents[3])
    if result.primary_log is None or result.manifest is None:
        raise SystemExit("ACCEPTANCE_MAP_VIABILITY_CURRENT_STATE_MISSING")
    if (
        result.primary_log.resolve()
        != (config.qa_root / "checks/acceptance-map-viability/primary.log").resolve()
    ):
        raise SystemExit("ACCEPTANCE_MAP_VIABILITY_PRIMARY_MISMATCH")
    if (
        result.manifest.resolve()
        != (config.qa_root / "qa_step_logs_manifest.json").resolve()
    ):
        raise SystemExit("ACCEPTANCE_MAP_VIABILITY_MANIFEST_MISMATCH")
    try:
        verify_manifest_entry(config, "acceptance-map-viability")
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        raise SystemExit(
            f"ACCEPTANCE_MAP_VIABILITY_CURRENT_STATE_INVALID:{exc}"
        ) from exc
    return ledger
