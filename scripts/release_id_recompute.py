#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Iterable, Mapping

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.config.registry_loader import DuplicateIdError, Manifest, load_manifest  # noqa: E402
from engine.config.registry_loader import SchemaValidationError  # noqa: E402
from engine.serializer import canon  # noqa: E402
from tools.config.artifacts import require_closed_rails  # noqa: E402


def _utcnow_iso() -> str:
    return _dt.datetime.now(tz=_dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _hex64(value: str) -> bool:
    return isinstance(value, str) and bool(value) and len(value) == 64 and all(c in "0123456789abcdef" for c in value)


def _write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def _sha256_sidecar_bytes(path: Path, digest: str) -> bytes:
    return f"{digest}  {path.as_posix()}\n".encode("utf-8")


def _write_sha256_sidecar(path: Path, digest: str) -> None:
    sidecar = path.with_suffix(path.suffix + ".sha256")
    _write_bytes(sidecar, _sha256_sidecar_bytes(path, digest))


def _compute_manifest_bytes(manifest_path: Path) -> tuple[Manifest | None, bytes, bytes, list[str]]:
    problems: list[str] = []
    try:
        manifest_bytes = manifest_path.read_bytes()
    except FileNotFoundError:
        return None, b"", b"", ["manifest_missing"]

    canonical_bytes = manifest_bytes
    manifest_obj: Manifest | None = None
    try:
        loaded = json.loads(manifest_bytes.decode("utf-8"))
        canonical_bytes = canon.sercanon(loaded, sort_keys=True)
    except Exception as exc:  # pragma: no cover - logged as a problem
        problems.append(f"manifest_json_error:{exc}")
        return manifest_obj, manifest_bytes, canonical_bytes, problems

    try:
        manifest_obj = load_manifest(manifest_path.parent.parent)
    except (SchemaValidationError, DuplicateIdError) as exc:
        code = exc.code if isinstance(exc, SchemaValidationError) else exc.code
        problems.append(f"manifest_schema_error:{code}")

    if manifest_bytes != canonical_bytes:
        problems.append("manifest_not_canonical")

    return manifest_obj, manifest_bytes, canonical_bytes, problems


def _audit_files(manifest: Manifest, *, repo_root: Path = ROOT) -> list[str]:
    audit: list[str] = []
    for entry in manifest.files:
        path = repo_root / entry.path
        if not path.exists():
            audit.append(f"MISSING {entry.path}")
            continue
        disk_bytes = path.read_bytes()
        sha = hashlib.sha256(disk_bytes).hexdigest()
        size = len(disk_bytes)
        if sha == entry.sha256 and size == entry.size:
            audit.append(f"PASS {entry.path}")
        else:
            audit.append(f"BAD {entry.path} expected {entry.sha256}:{entry.size} got {sha}:{size}")
    if not audit:
        audit.append("EMPTY")
    return audit


def _refresh_manifest_entries(manifest_path: Path) -> None:
    repo_root = manifest_path.parent.parent
    payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    entries = payload.get("files") if isinstance(payload, dict) else None
    if not isinstance(entries, list):
        raise ValueError("manifest_files_invalid")

    for entry in entries:
        if not isinstance(entry, dict) or not isinstance(entry.get("path"), str):
            raise ValueError("manifest_entry_invalid")
        disk_path = repo_root / entry["path"]
        if not disk_path.is_file():
            raise FileNotFoundError(f"manifest_source_missing:{entry['path']}")
        disk_bytes = disk_path.read_bytes()
        entry["sha256"] = hashlib.sha256(disk_bytes).hexdigest()
        entry["size"] = len(disk_bytes)

    manifest_path.write_bytes(canon.sercanon(payload, sort_keys=True))


def _env_pins_bytes() -> bytes:
    pins = [
        ("ALLOW_NETWORK", "0"),
        ("LANG", "C"),
        ("LC_ALL", "C"),
        ("SAFE_MODE", "1"),
        ("TZ", "UTC"),
    ]
    lines = [f"{key}={value}" for key, value in pins]
    return ("\n".join(lines) + "\n").encode("utf-8")


class _EvalResult(tuple):
    __slots__ = ()
    _fields = (
        "manifest_obj",
        "canonical_bytes",
        "manifest_digest",
        "freeze_digest",
        "release_id_value",
        "expected_release_id",
        "problems",
    )

    def __new__(
        cls,
        manifest_obj: Manifest | None,
        canonical_bytes: bytes,
        manifest_digest: str,
        freeze_digest: str | None,
        release_id_value: str | None,
        expected_release_id: str,
        problems: list[str],
    ):
        return tuple.__new__(
            cls,
            (
                manifest_obj,
                canonical_bytes,
                manifest_digest,
                freeze_digest,
                release_id_value,
                expected_release_id,
                problems,
            ),
        )

    def __getattr__(self, name: str):
        try:
            idx = self._fields.index(name)
        except ValueError:
            raise AttributeError(name)
        return self[idx]


def _evaluate_state(
    *,
    manifest_path: Path,
    freeze_path: Path,
    release_id_path: Path,
) -> _EvalResult:
    problems: list[str] = []
    manifest_obj, manifest_bytes, canonical_bytes, parse_problems = _compute_manifest_bytes(manifest_path)
    problems.extend(parse_problems)

    expected_release_id = hashlib.sha256(canonical_bytes).hexdigest()
    freeze_bytes = freeze_path.read_bytes() if freeze_path.exists() else None
    freeze_digest = hashlib.sha256(freeze_bytes).hexdigest() if freeze_bytes is not None else None
    manifest_digest = hashlib.sha256(canonical_bytes).hexdigest()

    if freeze_bytes is None:
        problems.append("freeze_pack_manifest_missing")
    elif freeze_bytes != canonical_bytes:
        problems.append("freeze_pack_manifest_not_equal")

    release_id_value = None
    if release_id_path.exists():
        release_id_value = release_id_path.read_text(encoding="utf-8").strip()
        if not _hex64(release_id_value):
            problems.append("release_id_txt_invalid")
        elif release_id_value != expected_release_id:
            problems.append("release_id_mismatch")
    else:
        problems.append("release_id_txt_missing")

    if manifest_obj is None:
        problems.append("manifest_unvalidated")
    else:
        repo_root = manifest_path.parent.parent
        for audit_line in _audit_files(manifest_obj, repo_root=repo_root):
            if not audit_line.startswith("PASS "):
                problems.append(f"manifest_file_audit:{audit_line}")

    return _EvalResult(
        manifest_obj,
        canonical_bytes,
        manifest_digest,
        freeze_digest,
        release_id_value,
        expected_release_id,
        problems,
    )


def _release_log_bytes(eval_result: _EvalResult) -> bytes:
    produced_at_utc = (
        eval_result.manifest_obj.built_at_utc
        if eval_result.manifest_obj is not None
        else ""
    )
    log_lines = [
        "release_id_recompute",
        f"produced_at_utc={produced_at_utc}",
        f"manifest_sha256={eval_result.manifest_digest}",
        f"release_id_txt={eval_result.release_id_value or ''}",
        f"expected_release_id={eval_result.expected_release_id}",
        f"freeze_pack_sha256={eval_result.freeze_digest or ''}",
        f"match={str(not eval_result.problems).lower()}",
        f"problems_count={len(eval_result.problems)}",
    ]
    log_lines.extend(f"problem={problem}" for problem in eval_result.problems)
    return ("\n".join(log_lines) + "\n").encode("utf-8")


def _expected_evidence_outputs(
    eval_result: _EvalResult,
    *,
    manifest_path: Path,
    freeze_path: Path,
    release_id_path: Path,
    manifest_snapshot_path: Path,
    checksums_path: Path,
    env_pins_path: Path,
    log_path: Path,
    schema_report_path: Path | None,
) -> dict[Path, bytes]:
    release_bytes = (eval_result.expected_release_id + "\n").encode("utf-8")
    outputs = {
        freeze_path: eval_result.canonical_bytes,
        freeze_path.with_suffix(freeze_path.suffix + ".sha256"): _sha256_sidecar_bytes(
            freeze_path,
            eval_result.manifest_digest,
        ),
        release_id_path: release_bytes,
        release_id_path.with_suffix(release_id_path.suffix + ".sha256"): _sha256_sidecar_bytes(
            release_id_path,
            hashlib.sha256(release_bytes).hexdigest(),
        ),
        env_pins_path: _env_pins_bytes(),
    }

    if eval_result.manifest_obj is not None:
        audit = _audit_files(
            eval_result.manifest_obj,
            repo_root=manifest_path.parent.parent,
        )
        outputs[checksums_path] = ("\n".join(audit) + "\n").encode("utf-8")
        snapshot_payload = {
            "manifest": {
                "root": eval_result.manifest_obj.root,
                "version": eval_result.manifest_obj.version,
                "built_at_utc": eval_result.manifest_obj.built_at_utc,
                "files": [
                    {"path": entry.path, "sha256": entry.sha256, "size": entry.size}
                    for entry in eval_result.manifest_obj.files
                ],
            },
            "release_id": eval_result.expected_release_id,
            "produced_at_utc": eval_result.manifest_obj.built_at_utc,
        }
        outputs[manifest_snapshot_path] = canon.sercanon(
            snapshot_payload,
            sort_keys=True,
        )

    log_bytes = _release_log_bytes(eval_result)
    outputs[log_path] = log_bytes
    outputs[log_path.with_suffix(log_path.suffix + ".sha256")] = _sha256_sidecar_bytes(
        log_path,
        hashlib.sha256(log_bytes).hexdigest(),
    )
    if schema_report_path is not None:
        schema_payload = {
            "ok": not eval_result.problems,
            "issues": eval_result.problems,
        }
        outputs[schema_report_path] = (
            json.dumps(
                schema_payload,
                separators=(",", ":"),
                ensure_ascii=False,
            )
            + "\n"
        ).encode("utf-8")
    return outputs


def _stale_outputs(expected: Mapping[Path, bytes]) -> list[Path]:
    return [
        path
        for path, expected_bytes in expected.items()
        if not path.is_file() or path.read_bytes() != expected_bytes
    ]


def check_manifest_only(
    manifest_path: Path | str = Path("catalog/manifest.json"),
) -> int:
    """Validate the immutable release input without reading derived evidence."""

    require_closed_rails()
    path = Path(manifest_path)
    manifest_obj, _raw, _canonical, problems = _compute_manifest_bytes(path)
    if manifest_obj is None:
        problems.append("manifest_unvalidated")
    else:
        for audit_line in _audit_files(
            manifest_obj,
            repo_root=path.parent.parent,
        ):
            if not audit_line.startswith("PASS "):
                problems.append(f"manifest_file_audit:{audit_line}")
    for problem in sorted(set(problems)):
        print(f"MANIFEST_ERROR:{problem}", file=sys.stderr)
    return 0 if not problems else 1


def recompute(
    *,
    manifest_path: Path | str = Path("catalog/manifest.json"),
    freeze_path: Path | str = Path("artifacts/math/freeze_pack_manifest.json"),
    release_id_path: Path | str = Path("artifacts/math/release_id.txt"),
    manifest_snapshot_path: Path | str = Path("artifacts/math/manifest_snapshot.json"),
    checksums_path: Path | str = Path("artifacts/math/checksums_audit.log"),
    env_pins_path: Path | str = Path("artifacts/proofs/env_pins.txt"),
    log_path: Path | str = Path("artifacts/math/release_id_recompute.log"),
    schema_report_path: Path | str | None = None,
    check: bool = False,
    refresh_manifest: bool = False,
) -> int:
    require_closed_rails()

    manifest_path = Path(manifest_path)
    freeze_path = Path(freeze_path)
    release_id_path = Path(release_id_path)
    manifest_snapshot_path = Path(manifest_snapshot_path)
    checksums_path = Path(checksums_path)
    env_pins_path = Path(env_pins_path)
    log_path = Path(log_path)
    schema_report_path = Path(schema_report_path) if schema_report_path else None

    if refresh_manifest:
        if check:
            raise ValueError("refresh_manifest_is_write_only")
        _refresh_manifest_entries(manifest_path)

    eval_result = _evaluate_state(
        manifest_path=manifest_path,
        freeze_path=freeze_path,
        release_id_path=release_id_path,
    )
    if not check:
        _write_bytes(freeze_path, eval_result.canonical_bytes)
        _write_text(release_id_path, eval_result.expected_release_id + "\n")
        eval_result = _evaluate_state(
            manifest_path=manifest_path,
            freeze_path=freeze_path,
            release_id_path=release_id_path,
        )

    expected_outputs = _expected_evidence_outputs(
        eval_result,
        manifest_path=manifest_path,
        freeze_path=freeze_path,
        release_id_path=release_id_path,
        manifest_snapshot_path=manifest_snapshot_path,
        checksums_path=checksums_path,
        env_pins_path=env_pins_path,
        log_path=log_path,
        schema_report_path=schema_report_path,
    )

    if check:
        stale_paths = _stale_outputs(expected_outputs)
        if stale_paths:
            print(
                "STALE:" + ",".join(path.as_posix() for path in stale_paths),
                file=sys.stderr,
            )
        return 0 if not eval_result.problems and not stale_paths else 1

    for path, data in expected_outputs.items():
        _write_bytes(path, data)
    return 0 if not eval_result.problems else 1


def main(argv: Iterable[str] | None = None) -> int:  # pragma: no cover
    parser = argparse.ArgumentParser(description="Recompute and validate release_id from the canonical manifest")
    parser.add_argument("--manifest", default="catalog/manifest.json", help="Path to the source-of-truth manifest")
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail non-zero on derived-output mismatches without writing",
    )
    parser.add_argument(
        "--check-manifest-only",
        action="store_true",
        help="Read-only validation of the canonical manifest and its declared inputs",
    )
    parser.add_argument(
        "--refresh-manifest",
        action="store_true",
        help=argparse.SUPPRESS,
    )
    args = parser.parse_args(list(argv) if argv is not None else None)
    if args.check_manifest_only:
        if args.check or args.refresh_manifest:
            parser.error(
                "--check-manifest-only cannot be combined with --check or --refresh-manifest"
            )
        return check_manifest_only(Path(args.manifest))
    if args.refresh_manifest:
        parser.error(
            "--refresh-manifest is retired; use scripts/cut_release_manifest.py"
        )
    if not args.check and os.environ.get("HDE_ISOLATED_RELEASE_BUILD") != "1":
        parser.error(
            "source-tree release evidence writes are retired; "
            "use tools/evidence/build_release_attestation.py"
        )
    return recompute(
        manifest_path=Path(args.manifest),
        check=args.check,
        refresh_manifest=args.refresh_manifest,
    )


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
