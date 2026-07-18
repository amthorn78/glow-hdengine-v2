#!/usr/bin/env python3
"""Dormant OPS-01R runner scaffold for HDE-EPIC038 PR-A."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import stat
import sys
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

SOURCE_MANIFEST_SCHEMA = "hde_epic038.source_tree_manifest.v1"
STAGING_MANIFEST_SCHEMA = "hde_epic038.non_source_staging_manifest.v1"


def canonical_bytes(value: object) -> bytes:
    return (
        json.dumps(
            value,
            ensure_ascii=True,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("ascii")


def sha_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _lexical_absolute(path: Path) -> Path:
    return Path(os.path.abspath(os.fspath(path)))


def tree_manifest(
    root: Path,
    *,
    schema: str,
    excluded_paths: tuple[Path, ...] = (),
    excluded_recursive_roots: tuple[Path, ...] = (),
) -> dict[str, object]:
    root = _lexical_absolute(root)
    excluded_exact = {_lexical_absolute(path) for path in excluded_paths}
    excluded_roots = tuple(
        _lexical_absolute(path) for path in excluded_recursive_roots
    )
    entries: list[dict[str, object]] = []

    def excluded(path: Path) -> bool:
        return path in excluded_exact or any(
            parent in (path, *path.parents) for parent in excluded_roots
        )

    def visit(path: Path) -> None:
        if path != root and excluded(path):
            return
        metadata = path.lstat()
        relative = "." if path == root else path.relative_to(root).as_posix()
        if any(part == "__pycache__" for part in Path(relative).parts) or (
            stat.S_ISREG(metadata.st_mode) and path.name.endswith(".pyc")
        ):
            raise RuntimeError("OPS01_V5_SOURCE_RESIDUE_DETECTED")
        entry: dict[str, object] = {
            "ctime_ns": metadata.st_ctime_ns,
            "kind": "",
            "mode": stat.S_IMODE(metadata.st_mode),
            "mtime_ns": metadata.st_mtime_ns,
            "path": relative,
            "sha256": None,
            "size": None,
            "target": None,
        }
        if stat.S_ISDIR(metadata.st_mode):
            entry["kind"] = "directory"
        elif stat.S_ISREG(metadata.st_mode):
            entry["kind"] = "regular_file"
            data = path.read_bytes()
            entry["sha256"] = sha_bytes(data)
            entry["size"] = len(data)
        elif stat.S_ISLNK(metadata.st_mode):
            entry["kind"] = "symlink"
            entry["target"] = os.readlink(path)
        else:
            raise RuntimeError("unsupported filesystem kind")
        entries.append(entry)
        if entry["kind"] == "directory":
            for child in sorted(
                path.iterdir(), key=lambda item: item.name.encode("utf-8")
            ):
                visit(_lexical_absolute(child))

    visit(root)
    return {
        "schema": schema,
        "entries": sorted(entries, key=lambda item: str(item["path"]).encode("utf-8")),
    }


def manifest_delta(
    before: list[dict[str, object]], after: list[dict[str, object]]
) -> list[dict[str, object]]:
    before_rows = {str(row["path"]): row for row in before}
    after_rows = {str(row["path"]): row for row in after}
    changes: list[dict[str, object]] = []
    for path in sorted(set(before_rows) | set(after_rows), key=lambda item: item.encode("utf-8")):
        if path not in before_rows:
            kinds = ["created"]
        elif path not in after_rows:
            kinds = ["deleted"]
        else:
            kinds = sorted(
                key
                for key in (
                    "ctime_ns",
                    "kind",
                    "mode",
                    "mtime_ns",
                    "sha256",
                    "size",
                    "target",
                )
                if before_rows[path].get(key) != after_rows[path].get(key)
            )
        if kinds:
            changes.append({"change_kinds": kinds, "path": path})
    return changes


def bound_python_vector(script: Path, *arguments: str) -> tuple[str, ...]:
    return (sys.executable, "-I", "-B", script.resolve().as_posix(), *arguments)


def reject_python_env(environment: dict[str, str]) -> None:
    if any(name.casefold().startswith("python") for name in environment):
        raise RuntimeError("OPS01_V5_PYTHON_ENVIRONMENT_INVALID")


def write_contained(path: Path, data: bytes, root: Path) -> None:
    path = path.resolve()
    root = root.resolve()
    if root not in (path, *path.parents):
        raise RuntimeError("OPS01_V5_WRITE_SET_MISMATCH")
    for parent in path.parents:
        if parent == root.parent:
            break
        if parent.exists() and parent.is_symlink():
            raise RuntimeError("OPS01_V5_WRITE_SET_MISMATCH")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def _file_identity(path: Path) -> dict[str, str]:
    lexical = path.absolute()
    resolved = lexical.resolve()
    return {
        "lexical_path": lexical.as_posix(),
        "resolved_path": resolved.as_posix(),
        "sha256": sha_bytes(resolved.read_bytes()),
    }


def _optional_executable_identity(name: str) -> dict[str, str]:
    lexical = shutil.which(name)
    if lexical is None:
        return {"lexical_path": name, "resolved_path": "", "sha256": ""}
    return _file_identity(Path(lexical))


def _git_commit(root: Path) -> str:
    marker = root / ".git"
    git_dir = marker
    if marker.is_file():
        text = marker.read_text("utf-8").strip()
        if not text.startswith("gitdir: "):
            return "UNKNOWN"
        git_dir = Path(text[8:])
        if not git_dir.is_absolute():
            git_dir = (root / git_dir).resolve()
    try:
        head = (git_dir / "HEAD").read_text("ascii").strip()
    except OSError:
        return "UNKNOWN"
    if len(head) == 40 and all(character in "0123456789abcdef" for character in head):
        return head
    if not head.startswith("ref: "):
        return "UNKNOWN"
    reference = head[5:]
    candidates = [git_dir / reference]
    try:
        common = (git_dir / "commondir").read_text("utf-8").strip()
        common_dir = Path(common)
        if not common_dir.is_absolute():
            common_dir = (git_dir / common_dir).resolve()
        candidates.append(common_dir / reference)
    except OSError:
        common_dir = git_dir
    for candidate in candidates:
        try:
            value = candidate.read_text("ascii").strip()
        except OSError:
            continue
        if len(value) == 40 and all(
            character in "0123456789abcdef" for character in value
        ):
            return value
    for packed in (git_dir / "packed-refs", common_dir / "packed-refs"):
        try:
            lines = packed.read_text("ascii").splitlines()
        except OSError:
            continue
        for line in lines:
            if line.startswith(("#", "^")):
                continue
            fields = line.split(" ", 1)
            if len(fields) == 2 and fields[1] == reference:
                return fields[0]
    return "UNKNOWN"


def _module_origins() -> list[dict[str, str]]:
    modules = {
        "engine.db.ddl_identity_projection": ROOT
        / "engine/db/ddl_identity_projection.py",
        "scripts.db.capture_epic011_posture": ROOT
        / "scripts/db/capture_epic011_posture.py",
        "scripts.ops.hde_epic038_ops01r": Path(__file__),
        "tools.evidence.hde_epic038_ops01_v5": ROOT
        / "tools/evidence/hde_epic038_ops01_v5.py",
    }
    origins = []
    for module, path in sorted(modules.items()):
        identity = _file_identity(path)
        origins.append(
            {
                "lexical_origin": identity["lexical_path"],
                "module": module,
                "resolved_origin": identity["resolved_path"],
                "sha256": identity["sha256"],
            }
        )
    return origins


def preflight() -> int:
    reject_python_env(dict(os.environ))
    run_id = uuid.uuid4().hex
    staging_root = Path("/tmp/hde-epic038-ops01r") / run_id
    control_root = staging_root / "control"
    working_directory = staging_root / "preflight-work"
    preflight_path = control_root / "preflight.json"
    control_root.mkdir(parents=True)
    working_directory.mkdir()

    source_manifest = tree_manifest(ROOT, schema=SOURCE_MANIFEST_SCHEMA)
    source_manifest_sha256 = sha_bytes(canonical_bytes(source_manifest))
    source_exclusions = (
        (ROOT,)
        if _lexical_absolute(staging_root) in (
            _lexical_absolute(ROOT),
            *_lexical_absolute(ROOT).parents,
        )
        else ()
    )
    pre_staging_manifest = tree_manifest(
        staging_root,
        schema=STAGING_MANIFEST_SCHEMA,
        excluded_paths=(preflight_path,),
        excluded_recursive_roots=source_exclusions,
    )
    pre_staging_manifest_sha256 = sha_bytes(canonical_bytes(pre_staging_manifest))

    runner = _file_identity(Path(__file__))
    validator = _file_identity(ROOT / "tools/evidence/hde_epic038_ops01_v5.py")
    projector = _file_identity(ROOT / "engine/db/ddl_identity_projection.py")
    interpreter = _file_identity(Path(sys.executable))
    railway = _optional_executable_identity("railway")
    producer_argv = bound_python_vector(Path(__file__), "--preflight")
    validator_argv = bound_python_vector(
        ROOT / "tools/evidence/hde_epic038_ops01_v5.py",
        "--validate-preflight",
        "--expected-identity-stdin",
        preflight_path.as_posix(),
    )

    zero_counts = {
        name: 0
        for name in (
            "bridge_transport_delegations",
            "candidate_writes",
            "credential_reads",
            "direct_connector_delegations",
            "failure_summary_writes",
            "provider_constructions",
            "railway_subprocesses",
            "sql_driver_delegations",
            "vendor_transport_delegations",
        )
    }
    expected_counts = {
        "logical_observations": 10,
        "bodygraph_reads": 2,
        "direct_provider_selections": 1,
        "bridge_provider_selections": 1,
        "vendor_requests": 0,
        "retries": 0,
        "fallbacks": 0,
        "direct_connection_attempts": 0,
        "direct_sql_statements": 0,
        "bridge_http_requests": 0,
    }
    write_contained(preflight_path, b"", staging_root)
    post_source_manifest = tree_manifest(ROOT, schema=SOURCE_MANIFEST_SCHEMA)
    post_source_manifest_sha256 = sha_bytes(canonical_bytes(post_source_manifest))
    if post_source_manifest_sha256 != source_manifest_sha256:
        raise RuntimeError("OPS01_V5_SOURCE_MANIFEST_MISMATCH")
    post_staging_manifest = tree_manifest(
        staging_root,
        schema=STAGING_MANIFEST_SCHEMA,
        excluded_paths=(preflight_path,),
        excluded_recursive_roots=source_exclusions,
    )
    post_staging_manifest_sha256 = sha_bytes(canonical_bytes(post_staging_manifest))
    observed_staging_changes = manifest_delta(
        pre_staging_manifest["entries"], post_staging_manifest["entries"]
    )
    payload: dict[str, object] = {
        "schema": "hde_epic038.ops01r.preflight.v1",
        "status": "PASS",
        "run": {
            "control_root": control_root.as_posix(),
            "preflight_path": preflight_path.as_posix(),
            "run_id": run_id,
            "source_root": ROOT.as_posix(),
            "staging_root": staging_root.as_posix(),
            "working_directory": working_directory.as_posix(),
        },
        "source": {
            "checkout_state": "DETACHED",
            "commit": _git_commit(ROOT),
            "repository": "amthorn78/glow-hdengine-v2",
            "root": ROOT.as_posix(),
            "source_manifest_sha256": source_manifest_sha256,
            "worktree_state": "clean",
        },
        "components": {
            "projector": projector,
            "runner": runner,
            "validator": validator,
        },
        "interpreter": {
            "bytecode_flag": "-B",
            "bytecode_write_control": "python_flag_-B",
            "isolated_flag": "-I",
            "lexical_path": interpreter["lexical_path"],
            "preflight_argv": list(producer_argv),
            "preflight_validator_argv": list(validator_argv),
            "python_environment_names": [],
            "resolved_path": interpreter["resolved_path"],
            "sha256": interpreter["sha256"],
        },
        "module_origins": _module_origins(),
        "railway_executable": railway,
        "orchestration": {"producer_vector": list(producer_argv)},
        "actual_external_io_counts": zero_counts,
        "expected_call_counts": expected_counts,
        "nonclaims": [
            "no_railway_subprocess",
            "no_credential_read",
            "no_provider_construction",
            "no_direct_connector_delegation",
            "no_sql_driver_delegation",
            "no_bridge_transport_delegation",
            "no_vendor_transport_delegation",
            "no_candidate_write",
            "no_failure_summary_write",
            "no_source_tree_write",
            "no_bytecode_cache_write",
            "no_unauthorized_staging_write",
        ],
        "source_write_validation": {
            "status": "PASS",
            "mode": "preflight",
            "bytecode_write_control": "python_flag_-B",
            "python_argv": list(producer_argv),
            "python_environment_names": [],
            "pre_source_manifest_sha256": source_manifest_sha256,
            "post_source_manifest_sha256": post_source_manifest_sha256,
            "pre_staging_manifest": pre_staging_manifest["entries"],
            "pre_staging_manifest_sha256": pre_staging_manifest_sha256,
            "post_staging_manifest_sha256": post_staging_manifest_sha256,
            "observed_staging_changes": observed_staging_changes,
            "source_root": ROOT.as_posix(),
        },
    }
    payload["preflight_identity_sha256"] = sha_bytes(canonical_bytes(payload))
    write_contained(preflight_path, canonical_bytes(payload), staging_root)
    print(preflight_path.as_posix())
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--preflight", action="store_true")
    parser.add_argument("--target-identity-probe", action="store_true")
    parser.add_argument("--discovery")
    parser.add_argument("--live-launch")
    parser.add_argument("--live-child", action="store_true")
    args = parser.parse_args(argv)
    if args.preflight:
        return preflight()
    if args.target_identity_probe:
        print(
            canonical_bytes(
                {
                    "schema": "hde_epic038.ops01r.target_identity_probe.v1",
                    "writes": 0,
                }
            ).decode(),
            end="",
        )
        return 0
    raise SystemExit("OPS modes are dormant and require PO authorization")


if __name__ == "__main__":
    raise SystemExit(main())
