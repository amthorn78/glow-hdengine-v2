#!/usr/bin/env python3
"""Strict runner for reusable SAFE-rails CI job definitions.

PF10 — HDE Build Notes §2.15 (HDE-EPIC040-PR04 F01 overlay): a step may declare
``accepted_release_not_admitted_exit_code: 3`` in the job definition's native
shape.  When that step exits with exactly that code, the runner accepts the
outcome only after its own independent read-only admission probe observes the
``INCOMPLETE_RELEASE_ROSTER`` refusal; every remaining step and job still runs,
the run ends with ``RAILS_JOB_DEFINITIONS:RELEASE_NOT_ADMITTED`` and exits with
the same distinct code (never 0).  Any other non-zero exit fails as before.
The acceptance is self-extinguishing: once the complete roster is admitted the
probe returns a bundle and a non-zero step exit is an ordinary failure.
"""
from __future__ import annotations

import ast
import os
import shlex
import subprocess
import sys
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
REQUIRED_IDENTITIES = {"rails_closed_refusal", "rails_open_conformance", "logs_keys_only_redaction"}
# Distinct non-admitted exit code; tests pin it equal to
# tools.evidence.run_sanity_pipeline.RELEASE_NOT_ADMITTED_EXIT_CODE.
RELEASE_NOT_ADMITTED_EXIT_CODE = 3
RELEASE_NOT_ADMITTED_REFUSAL_CODE = "INCOMPLETE_RELEASE_ROSTER"
ACCEPTED_RELEASE_NOT_ADMITTED_KEY = "accepted_release_not_admitted_exit_code"
RELEASE_NOT_ADMITTED_MARKER = "RAILS_JOB_DEFINITIONS:RELEASE_NOT_ADMITTED"
REQUIRED_TOP_LEVEL = {"name", "rails", "scope", "live_vendor_calls", "steps"}
RAIL_KEYS = {"SAFE_MODE", "ALLOW_NETWORK", "LC_ALL", "LANG", "TZ"}
DETERMINISM = {"LC_ALL": "C", "LANG": "C", "TZ": "UTC"}
EXPECTED_RAILS = {
    "rails_closed_refusal": {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", **DETERMINISM},
    "rails_open_conformance": {"SAFE_MODE": "0", "ALLOW_NETWORK": "1", **DETERMINISM},
    "logs_keys_only_redaction": {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", **DETERMINISM},
}
CREDENTIAL_KEYS = {"secrets", "secret", "credentials", "credential", "tokens", "token", "api_key", "apikey", "authorization", "password"}
CREDENTIAL_ENV_NAMES = {"HD_API_KEY", "GEO_API_KEY", "HDAPI_BASE_URL", "HD_API_BASE_URL", "AUTHORIZATION", "API_KEY", "TOKEN", "SECRET"}
NORMALIZED_CREDENTIAL_NAMES = {re.sub(r"[^A-Z0-9]", "", name.upper()) for name in CREDENTIAL_ENV_NAMES}
ALLOWED_ARGV = {
    "rails_closed_refusal": (("python", "-m", "pytest", "tests/bodygraph/test_resolver_vendor.py", "-q"),),
    "rails_open_conformance": (
        ("python", "-m", "pytest", "tests/bodygraph/test_vendor_client.py", "tests/evidence/test_open_rails_abba_proof.py", "-q"),
        ("python", "tools/evidence/generate_open_rails_abba_proof.py", "--check-current"),
    ),
    "logs_keys_only_redaction": (
        ("python", "tools/evidence/generate_rails_gate_evidence.py", "--check"),
        ("python", "-m", "pytest", "tests/bodygraph/test_vendor_client.py", "tests/bodygraph/test_resolver_vendor.py", "-q"),
    ),
}


class DefinitionError(Exception):
    pass


def _parse_scalar(raw: str) -> Any:
    value = raw.strip()
    if not value:
        return ""
    if value[0:1] in {'"', "'"}:
        try:
            return ast.literal_eval(value)
        except Exception as exc:  # pragma: no cover
            raise DefinitionError(f"invalid quoted scalar: {raw}") from exc
    if value in {"true", "True"}:
        return True
    if value in {"false", "False"}:
        return False
    return value


def load_closed_yaml(path: Path) -> dict[str, Any]:
    """Load the tiny closed YAML schema used by ci/jobs/*.yml."""
    data: dict[str, Any] = {}
    lines = path.read_text(encoding="utf-8").splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        i += 1
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith(" "):
            raise DefinitionError(f"unexpected indentation in {path}: {line!r}")
        if ":" not in line:
            raise DefinitionError(f"expected key in {path}: {line!r}")
        key, rest = line.split(":", 1)
        if rest.strip():
            data[key] = _parse_scalar(rest)
            continue
        if key == "rails":
            rails: dict[str, str] = {}
            while i < len(lines) and lines[i].startswith("  ") and not lines[i].startswith("  -"):
                sub = lines[i].strip(); i += 1
                if ":" not in sub:
                    raise DefinitionError("malformed rails entry")
                k, v = sub.split(":", 1)
                rails[k] = str(_parse_scalar(v))
            data[key] = rails
        elif key == "steps":
            steps: list[dict[str, Any]] = []
            while i < len(lines) and lines[i].startswith("  -"):
                step_line = lines[i][3:].strip(); i += 1
                if not step_line.startswith("command:"):
                    raise DefinitionError("each step must start with command")
                step: dict[str, Any] = {"command": str(_parse_scalar(step_line.split(":", 1)[1]))}
                while i < len(lines) and lines[i].startswith("    ") and not lines[i].startswith("      - "):
                    sub = lines[i].strip()
                    if sub == "proves:":
                        i += 1
                        proves: list[str] = []
                        while i < len(lines) and lines[i].startswith("      - "):
                            proves.append(lines[i].split("- ", 1)[1].strip()); i += 1
                        step["proves"] = proves
                    elif sub.startswith(ACCEPTED_RELEASE_NOT_ADMITTED_KEY + ":"):
                        if ACCEPTED_RELEASE_NOT_ADMITTED_KEY in step:
                            raise DefinitionError("duplicate accepted outcome declaration")
                        step[ACCEPTED_RELEASE_NOT_ADMITTED_KEY] = _parse_scalar(sub.split(":", 1)[1])
                        i += 1
                    else:
                        raise DefinitionError(f"unsupported step key: {sub}")
                steps.append(step)
            data[key] = steps
        elif key.lower().replace("-", "_") in CREDENTIAL_KEYS:
            raise DefinitionError(f"credential declaration is forbidden: {key}")
        else:
            raise DefinitionError(f"unsupported nested key {key}")
    return data


def _contains_secrets_ref(obj: Any) -> bool:
    if isinstance(obj, str):
        return "${{ secrets." in obj.lower()
    if isinstance(obj, dict):
        return any(_contains_secrets_ref(k) or _contains_secrets_ref(v) for k, v in obj.items())
    if isinstance(obj, list):
        return any(_contains_secrets_ref(v) for v in obj)
    return False


def _reject_structural_credentials(obj: Any, *, in_env: bool = False) -> None:
    if isinstance(obj, dict):
        for k, v in obj.items():
            lk = str(k).lower().replace("-", "_")
            if lk in CREDENTIAL_KEYS:
                raise DefinitionError(f"credential declaration is forbidden: {k}")
            if in_env and str(k).upper() in CREDENTIAL_ENV_NAMES and str(v).strip():
                raise DefinitionError(f"credential environment value is forbidden: {k}")
            _reject_structural_credentials(v, in_env=(lk == "env" or in_env))
    elif isinstance(obj, list):
        for v in obj:
            _reject_structural_credentials(v, in_env=in_env)



def _normalized_sensitive_name(raw: str) -> str:
    return re.sub(r"[^A-Z0-9]", "", raw.upper())


def _is_sensitive_name(raw: str) -> bool:
    return _normalized_sensitive_name(raw) in NORMALIZED_CREDENTIAL_NAMES


def _reject_credential_argv(argv: list[str]) -> None:
    for idx, token in enumerate(argv):
        if "=" in token:
            name, value = token.split("=", 1)
            if name.startswith("--"):
                name = name[2:]
            if _is_sensitive_name(name) and value.strip():
                raise DefinitionError(f"credential-bearing command argument is forbidden: {name}")
        if token.startswith("--"):
            name = token[2:]
            if "=" in name:
                name = name.split("=", 1)[0]
            if _is_sensitive_name(name) and idx + 1 < len(argv) and argv[idx + 1].strip():
                raise DefinitionError(f"credential-bearing command option is forbidden: {token}")
        if token == "env" or token.endswith("/env"):
            raise DefinitionError("env wrapper is forbidden in rails job commands")


def _validate_accepted_outcome(step: dict[str, Any]) -> None:
    """The only declarable accepted non-zero outcome is the distinct non-admitted code."""

    if ACCEPTED_RELEASE_NOT_ADMITTED_KEY not in step:
        return
    raw = step[ACCEPTED_RELEASE_NOT_ADMITTED_KEY]
    text = str(raw).strip()
    if isinstance(raw, bool) or not text.isdigit() or int(text) != RELEASE_NOT_ADMITTED_EXIT_CODE:
        raise DefinitionError(
            f"{ACCEPTED_RELEASE_NOT_ADMITTED_KEY} must equal {RELEASE_NOT_ADMITTED_EXIT_CODE}"
        )
    step[ACCEPTED_RELEASE_NOT_ADMITTED_KEY] = RELEASE_NOT_ADMITTED_EXIT_CODE


def release_not_admitted_observed() -> bool:
    """Independent read-only admission probe: true only for ``INCOMPLETE_RELEASE_ROSTER``."""

    from engine.config.registry_loader import SchemaValidationError, load_active_mechanics_bundle

    try:
        load_active_mechanics_bundle()
    except SchemaValidationError as exc:
        return getattr(exc, "code", None) == RELEASE_NOT_ADMITTED_REFUSAL_CODE
    except Exception:
        return False
    return False


def _validate_allowed_argv(job_name: str, argv: list[str]) -> None:
    normalized = tuple("python" if arg == sys.executable else arg for arg in argv)
    allowed = ALLOWED_ARGV.get(job_name, ())
    if normalized not in allowed:
        raise DefinitionError(f"command argv not allowlisted for {job_name}: {normalized}")


def validate(path: Path) -> dict[str, Any]:
    job = load_closed_yaml(path)
    if not isinstance(job, dict):
        raise DefinitionError("definition must be mapping")
    missing = REQUIRED_TOP_LEVEL - set(job)
    if missing:
        raise DefinitionError(f"missing required fields: {sorted(missing)}")
    extra = set(job) - REQUIRED_TOP_LEVEL
    if extra:
        raise DefinitionError(f"unknown top-level fields: {sorted(extra)}")
    _reject_structural_credentials(job)
    if _contains_secrets_ref(job):
        raise DefinitionError("GitHub secrets references are forbidden")
    name = job["name"]
    if name not in REQUIRED_IDENTITIES:
        raise DefinitionError(f"unknown job identity: {name}")
    if not isinstance(job["scope"], str) or "hde-epic031" in job["scope"].lower():
        raise DefinitionError("scope must be reusable and non-EPIC031")
    if name == "rails_open_conformance":
        scope = job["scope"].lower()
        if not (("fixture-backed" in scope or "mocked" in scope) and "non-live" in scope):
            raise DefinitionError("open scope must state fixture-backed/mocked non-live posture")
    if job["live_vendor_calls"] != "forbidden":
        raise DefinitionError("live_vendor_calls must equal forbidden")
    rails = job["rails"]
    if not isinstance(rails, dict) or set(rails) != RAIL_KEYS:
        raise DefinitionError("rails mapping must contain exactly deterministic rails keys")
    if {str(k): str(v) for k, v in rails.items()} != EXPECTED_RAILS[name]:
        raise DefinitionError(f"rails values invalid for {name}")
    steps = job["steps"]
    if not isinstance(steps, list) or not steps:
        raise DefinitionError("steps must be non-empty list")
    for step in steps:
        if not isinstance(step, dict) or "command" not in step:
            raise DefinitionError("malformed step")
        cmd = step["command"]
        if not isinstance(cmd, str) or not cmd.strip() or "\n" in cmd or "\r" in cmd:
            raise DefinitionError("step command must be non-empty single-line string")
        if "proves" in step and (not isinstance(step["proves"], list) or not all(isinstance(x, str) for x in step["proves"])):
            raise DefinitionError("proves must be list of strings")
        _validate_accepted_outcome(step)
        try:
            argv = shlex.split(cmd)
        except ValueError as exc:
            raise DefinitionError("step command could not be parsed") from exc
        _reject_credential_argv(argv)
        _validate_allowed_argv(str(name), argv)
    return job


def run_job(job: dict[str, Any], *, outcomes: list[str] | None = None) -> int:
    """Run one job; return 0 or the first failing step's exit code.

    A step that exits with its declared ``accepted_release_not_admitted_exit_code``
    while the independent probe observes the non-admitted state is accepted: the
    remaining steps still run, and ``RELEASE_NOT_ADMITTED`` is appended to
    ``outcomes`` so the caller can end with the distinct code instead of 0.
    """

    env = dict(os.environ)
    for key in CREDENTIAL_ENV_NAMES:
        env.pop(key, None)
    env.update({str(k): str(v) for k, v in job["rails"].items()})
    for step in job["steps"]:
        cmd = step["command"]
        print(f"RUN {job['name']}: {cmd}", flush=True)
        argv = shlex.split(cmd)
        _reject_credential_argv(argv)
        _validate_allowed_argv(str(job["name"]), argv)
        result = subprocess.run(argv, cwd=ROOT, env=env, text=True)
        if result.returncode == 0:
            continue
        accepted = step.get(ACCEPTED_RELEASE_NOT_ADMITTED_KEY)
        if (
            accepted is not None
            and result.returncode == accepted
            and release_not_admitted_observed()
        ):
            print(
                f"ACCEPTED {job['name']}: RELEASE_NOT_ADMITTED (exit {accepted}; "
                f"{RELEASE_NOT_ADMITTED_REFUSAL_CODE} observed): {cmd}",
                flush=True,
            )
            if outcomes is not None:
                outcomes.append("RELEASE_NOT_ADMITTED")
            continue
        return result.returncode
    return 0


def main(argv: list[str] | None = None) -> int:
    paths = [Path(arg) for arg in (argv if argv is not None else sys.argv[1:])]
    if not paths:
        print("no job definition paths supplied", file=sys.stderr); return 2
    seen: set[str] = set(); jobs = []
    try:
        for raw in paths:
            path = (ROOT / raw).resolve() if not raw.is_absolute() else raw.resolve()
            job = validate(path)
            if job["name"] in seen:
                raise DefinitionError(f"duplicate job identity: {job['name']}")
            seen.add(job["name"]); jobs.append(job)
        if seen != REQUIRED_IDENTITIES:
            raise DefinitionError(f"required identities mismatch: {sorted(REQUIRED_IDENTITIES - seen)}")
    except Exception as exc:
        print(f"RAILS_JOB_DEFINITION_INVALID: {exc}", file=sys.stderr); return 2
    outcomes: list[str] = []
    for job in jobs:
        code = run_job(job, outcomes=outcomes)
        if code:
            return code
    if outcomes:
        print(RELEASE_NOT_ADMITTED_MARKER)
        return RELEASE_NOT_ADMITTED_EXIT_CODE
    print("RAILS_JOB_DEFINITIONS_OK")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
