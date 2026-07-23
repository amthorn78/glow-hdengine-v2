#!/usr/bin/env python3
"""Build release-bound evidence in an isolated copy and publish one bundle.

The source checkout is an input only. All legacy producer writes occur in a
temporary tracked-file copy, and only the resulting attestation bundle is
written to the explicitly external output directory.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.serializer import canon
from tools.evidence.regenerate_identity_closure import ATTESTATION_GENERATED_OUTPUTS
from tools.evidence.retained_evidence_safety import validate_retained_text_safety

SCHEMA = "hde.release_attestation.v1"
SCHEMA_PATH = ROOT / "schemas/hde_release_attestation.v1.json"
FAILURE_SCHEMA_PATH = ROOT / "schemas/hde_release_attestation_failure.v1.json"
CLOSED_RAILS = {
    "ALLOW_NETWORK": "0",
    "LANG": "C",
    "LC_ALL": "C",
    "PIP_NO_INDEX": "1",
    "SAFE_MODE": "1",
    "TZ": "UTC",
}
REQUIRED_EVIDENCE = (
    "catalog/manifest.json",
    "schemas/hde_release_attestation.v1.json",
    "schemas/hde_release_attestation_failure.v1.json",
    "artifacts/math/freeze_pack_manifest.json",
    "artifacts/math/freeze_pack_manifest.json.sha256",
    "artifacts/math/release_id.txt",
    "artifacts/math/release_id.txt.sha256",
    "artifacts/math/release_id_recompute.log",
    "artifacts/math/release_id_recompute.log.sha256",
    "artifacts/math/checksums_audit.log",
    "artifacts/math/manifest_snapshot.json",
    "artifacts/proofs/env_pins.txt",
    "audit/gates/json_gate/canonical/json_gate_check_log.ndjson",
    "audit/gates/json_gate/canonical/json_gate_check_log.ndjson.path_proof.txt",
    "audit/gates/json_gate/canonical/json_gate_compare_log.ndjson",
    "audit/gates/json_gate/canonical/json_gate_compare_log.ndjson.path_proof.txt",
    "audit/gates/json_gate/canonical/json_gate_structured_record.json",
    "audit/gates/json_gate/canonical/json_gate_structured_record.json.path_proof.txt",
    "audit/gates/sanity_pipeline/sanity_pipeline.log",
)
_DEREFERENCED_EVIDENCE_SYMLINKS = frozenset(
    {"docs/ENDPOINTS_CATALOG.json"}
)
_IGNORED_PARTS = frozenset(
    {
        ".git",
        ".mypy_cache",
        ".pytest_cache",
        ".ruff_cache",
        "__pycache__",
    }
)
_FORBIDDEN_TRACKED_ROOTS = frozenset(
    {
        ".tox",
        ".venv",
        "node_modules",
        "venv",
    }
)


class AttestationBuildError(RuntimeError):
    """One names-only isolated build failure."""

    def __init__(self, code: str, *, stage: str = "", returncode: int | None = None):
        super().__init__(code)
        self.code = code
        self.stage = stage
        self.returncode = returncode


def _canonical_bytes(value: object) -> bytes:
    return canon.sercanon(value, sort_keys=True)


def _safe_relative_name(name: object) -> bool:
    if not isinstance(name, str) or not name or "\x00" in name or "\\" in name:
        return False
    rel = Path(name)
    return (
        not rel.is_absolute()
        and ".." not in rel.parts
        and rel.as_posix() == name
    )


def _validate_payload(payload: Mapping[str, object]) -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    errors = tuple(Draft202012Validator(schema).iter_errors(payload))
    files = payload.get("files")
    paths = (
        [row.get("path") for row in files if isinstance(row, Mapping)]
        if isinstance(files, list)
        else []
    )
    omitted = payload.get("omitted_files")
    omitted_paths = (
        [row.get("path") for row in omitted if isinstance(row, Mapping)]
        if isinstance(omitted, list)
        else []
    )
    omitted_reason_rows = (
        [row.get("reason_codes") for row in omitted if isinstance(row, Mapping)]
        if isinstance(omitted, list)
        else []
    )
    expected_paths = set(REQUIRED_EVIDENCE) | set(ATTESTATION_GENERATED_OUTPUTS)
    if (
        errors
        or payload.get("release_id") != payload.get("manifest_sha256")
        or paths != sorted(paths)
        or len(paths) != len(set(paths))
        or omitted_paths != sorted(omitted_paths)
        or len(omitted_paths) != len(set(omitted_paths))
        or set(paths) & set(omitted_paths)
        or set(paths) | set(omitted_paths) != expected_paths
        or any(not _safe_relative_name(name) for name in paths)
        or any(not _safe_relative_name(name) for name in omitted_paths)
        or any(
            name not in REQUIRED_EVIDENCE and not _generated_path_allowed(name)
            for name in (*paths, *omitted_paths)
        )
        or any(
            not isinstance(codes, list)
            or codes != sorted(codes)
            or len(codes) != len(set(codes))
            for codes in omitted_reason_rows
        )
        or not isinstance(payload.get("transcript"), Mapping)
        or payload["transcript"].get("path") != "build.log"
    ):
        raise AttestationBuildError("attestation_contract_invalid")


def _validate_failure_payload(payload: Mapping[str, object]) -> None:
    schema = json.loads(FAILURE_SCHEMA_PATH.read_text(encoding="utf-8"))
    if tuple(Draft202012Validator(schema).iter_errors(payload)):
        raise AttestationBuildError("failure_receipt_contract_invalid")


def _is_within(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
    except ValueError:
        return False
    return True


def _validate_output_root(output: Path, source: Path) -> Path:
    if output.is_symlink():
        raise AttestationBuildError("output_root_symlink_refused")
    resolved = output.resolve()
    if resolved == source or _is_within(resolved, source):
        raise AttestationBuildError("output_root_must_be_outside_source")
    if resolved.exists():
        if not resolved.is_dir():
            raise AttestationBuildError("output_root_not_directory")
        if any(resolved.iterdir()):
            raise AttestationBuildError("output_root_not_empty")
    else:
        resolved.mkdir(parents=True)
    return resolved


def _run_git(source: Path, *args: str) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        ["git", "-C", str(source), *args],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def _tracked_paths(source: Path) -> tuple[Path, ...]:
    proc = _run_git(source, "ls-files", "-z")
    if proc.returncode != 0:
        raise AttestationBuildError("tracked_source_inventory_unavailable")
    paths = []
    for raw in proc.stdout.split(b"\0"):
        if not raw:
            continue
        try:
            rel = Path(raw.decode("utf-8"))
        except UnicodeDecodeError as exc:
            raise AttestationBuildError("tracked_source_path_not_utf8") from exc
        if rel.is_absolute() or ".." in rel.parts:
            raise AttestationBuildError("tracked_source_path_unsafe")
        if rel.parts and rel.parts[0] in _FORBIDDEN_TRACKED_ROOTS:
            raise AttestationBuildError("tracked_source_ephemeral_path")
        paths.append(rel)
    return tuple(sorted(paths, key=lambda item: item.as_posix()))


def _path_bytes(path: Path) -> bytes:
    if path.is_symlink():
        return os.readlink(path).encode("utf-8")
    return path.read_bytes()


def _file_record(root: Path, rel: Path) -> dict[str, object]:
    body = _path_bytes(root / rel)
    return {
        "path": rel.as_posix(),
        "sha256": hashlib.sha256(body).hexdigest(),
        "size": len(body),
    }


def _snapshot(root: Path, paths: Iterable[Path]) -> dict[str, dict[str, object]]:
    return {
        rel.as_posix(): _file_record(root, rel)
        for rel in paths
        if (root / rel).is_file() or (root / rel).is_symlink()
    }


def _source_tree_digest(records: Mapping[str, Mapping[str, object]]) -> str:
    rows = [dict(records[name]) for name in sorted(records)]
    return hashlib.sha256(_canonical_bytes(rows)).hexdigest()


def _copy_tracked_source(source: Path, destination: Path, paths: Sequence[Path]) -> None:
    for rel in paths:
        src = source / rel
        dst = destination / rel
        if not src.is_file() and not src.is_symlink():
            raise AttestationBuildError("tracked_source_file_missing")
        dst.parent.mkdir(parents=True, exist_ok=True)
        if src.is_symlink():
            target = os.readlink(src)
            target_path = Path(target)
            try:
                resolved_target = (src.parent / target_path).resolve()
            except (OSError, RuntimeError) as exc:
                raise AttestationBuildError("tracked_source_symlink_unsafe") from exc
            if (
                target_path.is_absolute()
                or not _is_within(resolved_target, source)
            ):
                raise AttestationBuildError("tracked_source_symlink_unsafe")
            dst.symlink_to(target)
        else:
            shutil.copy2(src, dst)


def _initialize_scratch_git(scratch: Path) -> None:
    env = _clean_child_env(scratch)
    env.update(
        {
            "GIT_AUTHOR_DATE": "2025-12-26T00:00:00Z",
            "GIT_COMMITTER_DATE": "2025-12-26T00:00:00Z",
        }
    )
    commands = (
        ("init", "-q"),
        ("config", "user.name", "HDE Release Attestation"),
        ("config", "user.email", "release-attestation@invalid"),
        ("add", "-A"),
        ("commit", "-q", "-m", "isolated source snapshot"),
    )
    for args in commands:
        proc = subprocess.run(
            ["git", *args],
            cwd=scratch,
            env=env,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if proc.returncode != 0:
            raise AttestationBuildError("scratch_git_initialization_failed")


def _walk_files(root: Path) -> tuple[Path, ...]:
    rows = []
    for path in root.rglob("*"):
        rel = path.relative_to(root)
        if any(part in _IGNORED_PARTS for part in rel.parts):
            continue
        if path.is_file() or path.is_symlink():
            rows.append(rel)
    return tuple(sorted(rows, key=lambda item: item.as_posix()))


def _generated_path_allowed(name: str) -> bool:
    return name in ATTESTATION_GENERATED_OUTPUTS


def _clean_child_env(source_root: Path | None = None) -> dict[str, str]:
    env = {
        key: value
        for key, value in os.environ.items()
        if key in {"PATH", "TMPDIR", "VIRTUAL_ENV"}
    }
    env.update(CLOSED_RAILS)
    env["HDE_ISOLATED_RELEASE_BUILD"] = "1"
    if source_root is not None:
        # This is a controlled path, not a forwarded PYTHON* value. It keeps
        # installed console entrypoints bound to the isolated source copy.
        env["PYTHONPATH"] = str(source_root)
    return env


def _run_stage(
    scratch: Path,
    stage: str,
    argv: Sequence[str],
    log: list[str],
) -> None:
    proc = subprocess.run(
        list(argv),
        cwd=scratch,
        env=_clean_child_env(scratch),
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    log.extend(
        [
            f"stage={stage}",
            "argv="
            + " ".join(
                Path(arg).name if index == 0 else arg
                for index, arg in enumerate(argv)
            ),
            f"exit_code={proc.returncode}",
            "stdout_begin",
            proc.stdout.rstrip("\n"),
            "stdout_end",
            "stderr_begin",
            proc.stderr.rstrip("\n"),
            "stderr_end",
        ]
    )
    if proc.returncode != 0:
        raise AttestationBuildError(
            "isolated_stage_failed",
            stage=stage,
            returncode=proc.returncode,
        )


def _git_identity(source: Path) -> tuple[str, bool]:
    head = _run_git(source, "rev-parse", "HEAD")
    status = _run_git(source, "status", "--porcelain=v1", "--untracked-files=all")
    if head.returncode != 0 or status.returncode != 0:
        raise AttestationBuildError("source_git_identity_unavailable")
    value = head.stdout.decode("ascii").strip()
    if len(value) != 40 or any(ch not in "0123456789abcdef" for ch in value):
        raise AttestationBuildError("source_commit_invalid")
    return value, not bool(status.stdout)


def _write_failure(output: Path, exc: AttestationBuildError) -> None:
    receipt = {
        "schema": "hde.release_attestation.failure.v1",
        "code": exc.code,
        "stage": exc.stage or None,
        "returncode": exc.returncode,
        "secret_values_recorded": False,
    }
    _validate_failure_payload(receipt)
    (output / "failure.json").write_bytes(_canonical_bytes(receipt))


def _reset_failed_output(output: Path) -> None:
    evidence = output / "evidence"
    if evidence.is_symlink() or evidence.is_file():
        evidence.unlink()
    elif evidence.is_dir():
        shutil.rmtree(evidence)
    for name in (
        "attestation.json",
        "attestation.json.sha256",
        "build.log",
        "failure.json",
    ):
        path = output / name
        if path.is_file() or path.is_symlink():
            path.unlink()


def verify_attestation(
    root: Path,
    *,
    require_exact: bool = False,
    source: Path = ROOT,
) -> None:
    """Fail closed on a mutated, incomplete, or noncanonical output bundle."""

    root = root.resolve()
    try:
        actual_root = {path.name for path in root.iterdir()}
        evidence_root = root / "evidence"
        if actual_root != {
            "attestation.json",
            "attestation.json.sha256",
            "build.log",
            "evidence",
        } or evidence_root.is_symlink() or not evidence_root.is_dir():
            raise AttestationBuildError("attestation_root_inventory_invalid")
        raw = (root / "attestation.json").read_bytes()
        payload = json.loads(raw.decode("utf-8"))
        if not isinstance(payload, Mapping) or raw != _canonical_bytes(payload):
            raise AttestationBuildError("attestation_bytes_invalid")
        if validate_retained_text_safety(root / "attestation.json", raw):
            raise AttestationBuildError("attestation_not_secret_safe")
        _validate_payload(payload)
        if require_exact:
            source = source.resolve()
            source_commit, source_clean = _git_identity(source)
            tracked = _tracked_paths(source)
            source_tree_sha256 = _source_tree_digest(_snapshot(source, tracked))
            if (
                not source_clean
                or payload.get("source_commit_exact") is not True
                or payload.get("source_commit") != source_commit
                or payload.get("source_tree_sha256") != source_tree_sha256
            ):
                raise AttestationBuildError("attestation_source_not_exact")
        expected_sidecar = (
            f"{hashlib.sha256(raw).hexdigest()}  attestation.json\n"
        ).encode("utf-8")
        if (root / "attestation.json.sha256").read_bytes() != expected_sidecar:
            raise AttestationBuildError("attestation_checksum_invalid")

        rows = payload["files"]
        listed: set[str] = set()
        for row in rows:
            name = row["path"]
            rel = Path(name)
            if not _safe_relative_name(name):
                raise AttestationBuildError("attestation_file_path_unsafe")
            listed.add(name)
            evidence_path = root / "evidence" / rel
            if evidence_path.is_symlink():
                raise AttestationBuildError("attestation_evidence_symlink_refused")
            if _file_record(root / "evidence", rel) != row:
                raise AttestationBuildError("attestation_file_binding_invalid")
            if validate_retained_text_safety(evidence_path, evidence_path.read_bytes()):
                raise AttestationBuildError("attestation_evidence_not_secret_safe")
        actual = {
            path.relative_to(root / "evidence").as_posix()
            for path in (root / "evidence").rglob("*")
            if path.is_file() or path.is_symlink()
        }
        if actual != listed or not set(REQUIRED_EVIDENCE).issubset(listed):
            raise AttestationBuildError("attestation_file_inventory_invalid")
        omitted_paths = [row["path"] for row in payload["omitted_files"]]
        if set(omitted_paths) & listed:
            raise AttestationBuildError("attestation_omitted_file_collision")
        transcript_path = root / "build.log"
        if _file_record(root, Path("build.log")) != payload["transcript"]:
            raise AttestationBuildError("attestation_transcript_binding_invalid")
        if validate_retained_text_safety(
            transcript_path,
            transcript_path.read_bytes(),
        ):
            raise AttestationBuildError("attestation_transcript_not_secret_safe")
        if (root / "failure.json").exists():
            raise AttestationBuildError("attestation_failure_receipt_present")
    except AttestationBuildError:
        raise
    except (OSError, UnicodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
        raise AttestationBuildError("attestation_unreadable") from exc


def build_attestation(
    output: Path,
    *,
    source: Path = ROOT,
    require_clean: bool = False,
) -> Path:
    source = source.resolve()
    output = _validate_output_root(output, source)
    transcript: list[str] = []
    try:
        source_commit, source_clean = _git_identity(source)
        if require_clean and not source_clean:
            raise AttestationBuildError("source_tree_not_clean")
        tracked = _tracked_paths(source)
        source_snapshot = _snapshot(source, tracked)
        source_tree_sha256 = _source_tree_digest(source_snapshot)
        with tempfile.TemporaryDirectory(prefix="hde-release-attestation-") as raw:
            scratch = Path(raw) / "source"
            scratch.mkdir()
            _copy_tracked_source(source, scratch, tracked)
            _initialize_scratch_git(scratch)
            baseline = _snapshot(scratch, tracked)

            closure = (
                sys.executable,
                "tools/evidence/regenerate_identity_closure.py",
                "--in-place-isolated",
            )
            _run_stage(scratch, "closure_write_and_check", closure, transcript)
            _run_stage(
                scratch,
                "closure_fixed_point_check",
                (*closure, "--check"),
                transcript,
            )
            _run_stage(
                scratch,
                "pr_a_sanity_stop",
                (sys.executable, "tools/evidence/run_sanity_pipeline_gate.py"),
                transcript,
            )

            after_paths = _walk_files(scratch)
            after = _snapshot(scratch, after_paths)
            removed = sorted(set(baseline) - set(after))
            if removed:
                raise AttestationBuildError("isolated_producer_deleted_tracked_file")
            changed = {
                name
                for name, record in after.items()
                if name not in baseline or baseline[name] != record
            }
            if any(not _generated_path_allowed(name) for name in changed):
                raise AttestationBuildError("isolated_write_outside_evidence_roots")
            selected = set(ATTESTATION_GENERATED_OUTPUTS) | set(REQUIRED_EVIDENCE)
            missing = sorted(name for name in selected if name not in after)
            if missing:
                raise AttestationBuildError("required_attestation_evidence_missing")

            evidence_root = output / "evidence"
            evidence_root.mkdir()
            if evidence_root.is_symlink() or not _is_within(
                evidence_root.resolve(), output.resolve()
            ):
                raise AttestationBuildError("attestation_evidence_root_invalid")
            file_rows = []
            omitted_rows = []
            omitted_primaries: set[str] = set()
            for name in sorted(selected):
                rel = Path(name)
                source_path = scratch / rel
                if source_path.is_symlink():
                    target = source_path.resolve()
                    if (
                        name not in _DEREFERENCED_EVIDENCE_SYMLINKS
                        or not _is_within(target, scratch)
                        or not target.is_file()
                    ):
                        raise AttestationBuildError(
                            "attestation_evidence_symlink_refused"
                        )
                if any(name.startswith(primary + ".") for primary in omitted_primaries):
                    omitted_rows.append(
                        {
                            "path": name,
                            "reason_codes": [
                                "PRIMARY_OMITTED_SECRET_SAFETY"
                            ],
                        }
                    )
                    continue
                safety_errors = validate_retained_text_safety(
                    source_path,
                    source_path.read_bytes(),
                )
                if safety_errors:
                    if name in REQUIRED_EVIDENCE:
                        raise AttestationBuildError(
                            "attestation_evidence_not_secret_safe"
                        )
                    omitted_rows.append(
                        {
                            "path": name,
                            "reason_codes": sorted(set(safety_errors)),
                        }
                    )
                    omitted_primaries.add(name)
                    continue
                destination = evidence_root / rel
                destination.parent.mkdir(parents=True, exist_ok=True)
                if not _is_within(destination.resolve(), evidence_root.resolve()):
                    raise AttestationBuildError("attestation_destination_escape")
                shutil.copy2(source_path, destination)
                file_rows.append(_file_record(evidence_root, rel))

            release_id = (
                scratch / "artifacts/math/release_id.txt"
            ).read_text(encoding="utf-8").strip()
            manifest_bytes = (scratch / "catalog/manifest.json").read_bytes()
            if release_id != hashlib.sha256(manifest_bytes).hexdigest():
                raise AttestationBuildError("release_identity_mismatch")
            sanity = (
                scratch / "audit/gates/sanity_pipeline/sanity_pipeline.log"
            ).read_text(encoding="utf-8")
            if "pr_a_nonfinal_ops03_pr_b_binding_required" not in sanity:
                raise AttestationBuildError("pr_a_sanity_boundary_missing")

            transcript_path = output / "build.log"
            transcript_path.write_text("\n".join(transcript) + "\n", encoding="utf-8")
            if validate_retained_text_safety(
                transcript_path,
                transcript_path.read_bytes(),
            ):
                raise AttestationBuildError("attestation_transcript_not_secret_safe")
            transcript_row = _file_record(output, Path("build.log"))
            payload = {
                "schema": SCHEMA,
                "source_commit": source_commit,
                "source_commit_exact": source_clean,
                "source_tree_sha256": source_tree_sha256,
                "release_id": release_id,
                "manifest_sha256": hashlib.sha256(manifest_bytes).hexdigest(),
                "validation_result": "PASS",
                "release_admission": "NOT_ATTEMPTED",
                "pipeline_stop": {
                    "stage": 14,
                    "reason": "pr_a_nonfinal_ops03_pr_b_binding_required",
                },
                "rails": dict(sorted(CLOSED_RAILS.items())),
                "files": file_rows,
                "omitted_files": omitted_rows,
                "transcript": transcript_row,
                "nonclaims": [
                    "no_ops03_execution",
                    "no_live_packet",
                    "no_database_write",
                    "no_pr06r_b_admission",
                    "no_release_pipeline_pass_claim",
                ],
            }
            _validate_payload(payload)
            attestation_bytes = _canonical_bytes(payload)
            attestation_path = output / "attestation.json"
            attestation_path.write_bytes(attestation_bytes)
            (output / "attestation.json.sha256").write_text(
                f"{hashlib.sha256(attestation_bytes).hexdigest()}  attestation.json\n",
                encoding="utf-8",
            )
            verify_attestation(
                output,
                require_exact=require_clean,
                source=source,
            )
    except AttestationBuildError as exc:
        _reset_failed_output(output)
        _write_failure(output, exc)
        raise
    except (OSError, UnicodeError, json.JSONDecodeError, TypeError, ValueError) as exc:
        wrapped = AttestationBuildError("attestation_build_io_or_contract_failure")
        _reset_failed_output(output)
        _write_failure(output, wrapped)
        raise wrapped from exc
    return output / "attestation.json"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--output", type=Path)
    mode.add_argument("--verify", type=Path)
    parser.add_argument("--source", type=Path, default=ROOT)
    parser.add_argument("--require-clean", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.verify is not None:
            verify_attestation(
                args.verify,
                require_exact=args.require_clean,
                source=args.source,
            )
            print(args.verify / "attestation.json")
            return 0
        path = build_attestation(
            args.output,
            source=args.source,
            require_clean=args.require_clean,
        )
    except AttestationBuildError as exc:
        print(f"RELEASE_ATTESTATION_FAILED:{exc.code}", file=sys.stderr)
        return 1
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
