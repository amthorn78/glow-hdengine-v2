import datetime as dt
import json
import os
import stat

import pytest

from tools.evidence import update_evidence_index as uei


def _configure_sanity_rebind_fixture(tmp_path, monkeypatch):
    human_index = tmp_path / "docs/evidence/INDEX.json"
    hash_sentinel = tmp_path / "docs/evidence/INDEX.sha256"
    mirror_path = tmp_path / "artifacts/evidence_index.jsonl"
    mirror_sha_path = tmp_path / "artifacts/evidence_index.jsonl.sha256"
    sanity_path = tmp_path / uei.SANITY_LOG_REL
    for path in (human_index, hash_sentinel, mirror_path, sanity_path):
        path.parent.mkdir(parents=True, exist_ok=True)

    human_entries = [
        {
            "artifact_key": "index.machine_mirror",
            "discovered_physical_path": "artifacts/evidence_index.jsonl",
        },
        {
            "artifact_key": "sanity.pipeline.log",
            "discovered_physical_path": uei.SANITY_LOG_REL,
        },
    ]
    human_bytes = (json.dumps(human_entries, indent=2) + "\n").encode("utf-8")
    human_index.write_bytes(human_bytes)
    hash_sentinel.write_bytes(
        f"{uei._sha256_bytes(human_bytes)}  docs/evidence/INDEX.json\n".encode(
            "utf-8"
        )
    )

    sanity_bytes = b"stage: test\nsummary:FAIL\n"
    sanity_path.write_bytes(sanity_bytes)
    produced = "2026-08-17T00:00:00Z"
    records = [
        {
            "artifact_key": "index.machine_mirror",
            "discovered_physical_path": "artifacts/evidence_index.jsonl",
            "produced_at_utc": produced,
            "proof_anchor": "artifacts/evidence_index.jsonl.path_proof.txt",
            "role": "self_record",
            "sha256": "0" * 64,
            "size_bytes": 0,
        },
        {
            "artifact_key": "sanity.pipeline.log",
            "discovered_physical_path": uei.SANITY_LOG_REL,
            "produced_at_utc": produced,
            "proof_anchor": f"{uei.SANITY_LOG_REL}.path_proof.txt",
            "role": "snapshot",
            "sha256": uei._sha256_bytes(sanity_bytes),
            "size_bytes": len(sanity_bytes),
        },
    ]
    mirror_path.write_text(
        "".join(
            f"{json.dumps(record, separators=(',', ':'), sort_keys=True)}\n"
            for record in records
        ),
        encoding="utf-8",
    )

    monkeypatch.setattr(uei, "ROOT", tmp_path)
    monkeypatch.setattr(uei, "HUMAN_INDEX", human_index)
    monkeypatch.setattr(uei, "HASH_SENTINEL", hash_sentinel)
    monkeypatch.setattr(uei, "MIRROR_PATH", mirror_path)
    monkeypatch.setattr(uei, "MIRROR_REL", "artifacts/evidence_index.jsonl")
    monkeypatch.setattr(uei, "MIRROR_SHA_PATH", mirror_sha_path)
    monkeypatch.setattr(uei, "_STAGED_VIEW", None)
    monkeypatch.setattr(uei, "_ACTIVE_WRITE_TRANSACTION", None)
    return {
        "human": human_index,
        "sentinel": hash_sentinel,
        "mirror": mirror_path,
        "sanity": sanity_path,
    }


def test_machine_mirror_self_proof_matches_canonical_digest():
    proof_path = uei.MIRROR_PATH.with_suffix(".jsonl.path_proof.txt")
    proof = uei._load_existing_proof(proof_path)
    assert proof, "mirror path proof must exist for invariance checks"

    produced_default = proof.get("produced_at_utc")
    if produced_default is None:
        produced_default = uei._isoformat(dt.datetime.now(tz=dt.timezone.utc))

    entries = uei._load_human_index()
    mirror_bytes, rendered_rec = uei._render_mirror(
        entries, produced_default=produced_default, check=True
    )

    mirror_text = uei.MIRROR_PATH.read_text(encoding="utf-8")
    live_records = [
        json.loads(line)
        for line in mirror_text.splitlines()
        if line.strip()
    ]
    mirror_rel = uei.MIRROR_PATH.relative_to(uei.ROOT).as_posix()
    live_rec = next(
        rec
        for rec in live_records
        if rec["artifact_key"] == "index.machine_mirror"
        and rec["discovered_physical_path"] == mirror_rel
    )

    mirror_file_sha = uei._sha256_path(uei.MIRROR_PATH)
    mirror_body_sha = rendered_rec["sha256"]
    mirror_size = uei.MIRROR_PATH.stat().st_size

    assert mirror_bytes.decode("utf-8") == mirror_text
    assert rendered_rec["sha256"] == live_rec["sha256"] == mirror_body_sha
    assert proof["sha256"] == mirror_file_sha
    assert proof["mirror_body_sha256"] == mirror_body_sha
    assert int(rendered_rec["size_bytes"]) == int(live_rec["size_bytes"]) == int(mirror_size)
    assert int(proof["size_bytes"]) == int(mirror_size)
    assert proof.get("path") == mirror_rel
    assert proof.get("produced_at_utc") == rendered_rec["produced_at_utc"]


def test_staged_publication_add_replace_remove_is_transactional(tmp_path):
    existing = tmp_path / "existing.txt"
    added = tmp_path / "added.txt"
    removed = tmp_path / "removed.txt"
    existing.write_bytes(b"before\n")
    removed.write_bytes(b"remove-me\n")

    with uei._WriteTransaction(tmp_path):
        uei._publish_staged(
            {
                existing: b"after\n",
                added: b"added\n",
                removed: uei._STAGED_DELETION,
            }
        )

    assert existing.read_bytes() == b"after\n"
    assert added.read_bytes() == b"added\n"
    assert not removed.exists()


def test_staged_publication_rolls_back_every_preimage(tmp_path, monkeypatch):
    first = tmp_path / "a.txt"
    second = tmp_path / "b.txt"
    added = tmp_path / "new-directory" / "c.txt"
    first.write_bytes(b"first-before\n")
    second.write_bytes(b"second-before\n")
    os.chmod(first, 0o640)
    os.chmod(second, 0o600)
    original_root_mode = tmp_path.stat().st_mode
    real_replace = os.replace
    calls = 0

    def fail_second(source, destination):
        nonlocal calls
        calls += 1
        if calls == 2:
            raise OSError("fault injection")
        real_replace(source, destination)

    monkeypatch.setattr(uei.os, "replace", fail_second)
    with pytest.raises(OSError, match="fault injection"):
        with uei._WriteTransaction(tmp_path):
            uei._publish_staged(
                {
                    first: b"first-after\n",
                    second: uei._STAGED_DELETION,
                    added: b"added\n",
                }
            )

    assert first.read_bytes() == b"first-before\n"
    assert second.read_bytes() == b"second-before\n"
    assert stat.S_IMODE(first.stat().st_mode) == 0o640
    assert stat.S_IMODE(second.stat().st_mode) == 0o600
    assert not added.exists()
    assert not added.parent.exists()
    assert tmp_path.stat().st_mode == original_root_mode


def test_sanity_rebind_rejects_aliased_inputs(tmp_path, monkeypatch):
    for name in ("human", "sentinel", "mirror", "sanity"):
        root = tmp_path / name
        paths = _configure_sanity_rebind_fixture(root, monkeypatch)
        alias = paths[name]
        target = root / f"real-{name}.txt"
        target.write_bytes(alias.read_bytes())
        alias.unlink()
        alias.symlink_to(target)

        with pytest.raises(SystemExit, match="ALIASED_TRANSACTION_FILE"):
            uei._run_sanity_log_rebind_transaction()

        assert alias.is_symlink()
        assert target.is_file()
        assert uei._STAGED_VIEW is None
        assert uei._ACTIVE_WRITE_TRANSACTION is None


def test_sanity_rebind_publishes_coherent_model(tmp_path, monkeypatch):
    paths = _configure_sanity_rebind_fixture(tmp_path, monkeypatch)
    human_before = paths["human"].read_bytes()
    sentinel_before = paths["sentinel"].read_bytes()

    uei._run_sanity_log_rebind_transaction()

    assert paths["human"].read_bytes() == human_before
    assert paths["sentinel"].read_bytes() == sentinel_before
    mirror_sha = uei._sha256_path(paths["mirror"])
    assert uei.MIRROR_SHA_PATH.read_bytes() == (
        f"{mirror_sha}  {uei.MIRROR_REL}\n".encode("utf-8")
    )
    for rel in (uei.SANITY_LOG_REL, uei.MIRROR_REL, f"{uei.MIRROR_REL}.sha256"):
        assert (tmp_path / f"{rel}.path_proof.txt").is_file()
    assert uei._STAGED_VIEW is None
    assert uei._ACTIVE_WRITE_TRANSACTION is None


def test_sanity_rebind_rolls_back_partial_publication(tmp_path, monkeypatch):
    _configure_sanity_rebind_fixture(tmp_path, monkeypatch)
    before = {
        path.relative_to(tmp_path): path.read_bytes()
        for path in tmp_path.rglob("*")
        if path.is_file()
    }
    real_replace = os.replace
    calls = 0

    def fail_second(source, destination):
        nonlocal calls
        calls += 1
        if calls == 2:
            raise OSError("sanity rebind fault injection")
        real_replace(source, destination)

    monkeypatch.setattr(uei.os, "replace", fail_second)
    with pytest.raises(OSError, match="sanity rebind fault injection"):
        uei._run_sanity_log_rebind_transaction()

    after = {
        path.relative_to(tmp_path): path.read_bytes()
        for path in tmp_path.rglob("*")
        if path.is_file()
    }
    assert after == before
    assert uei._STAGED_VIEW is None
    assert uei._ACTIVE_WRITE_TRANSACTION is None


def test_unchanged_fast_path_rejects_file_and_parent_aliases(
    tmp_path, monkeypatch
):
    expected = b"already-current\n"
    real_file = tmp_path / "real-file.txt"
    real_file.write_bytes(expected)
    file_alias = tmp_path / "owned-file.txt"
    file_alias.symlink_to(real_file)

    real_directory = tmp_path / "real-directory"
    real_directory.mkdir()
    (real_directory / "owned-file.txt").write_bytes(expected)
    directory_alias = tmp_path / "owned-directory"
    directory_alias.symlink_to(real_directory, target_is_directory=True)

    artifact = tmp_path / "artifact.log"
    artifact.write_bytes(expected)
    proof_target = tmp_path / "real-proof.txt"
    proof_target.write_text(
        "\n".join(
            (
                "path: artifact.log",
                f"size_bytes: {len(expected)}",
                f"sha256: {uei._sha256_bytes(expected)}",
                "mtime_utc: 2026-08-17T00:00:00Z",
                "produced_at_utc: 2026-08-17T00:00:00Z",
                "",
            )
        ),
        encoding="utf-8",
    )
    proof_alias = tmp_path / "artifact.log.path_proof.txt"
    proof_alias.symlink_to(proof_target)

    monkeypatch.chdir(tmp_path)
    with pytest.raises(SystemExit, match="ALIASED_TRANSACTION_DIRECTORY"):
        uei._write_if_changed(
            directory_alias.relative_to(tmp_path) / "owned-file.txt",
            expected,
            check=False,
        )
    with pytest.raises(SystemExit, match="ALIASED_TRANSACTION_FILE"):
        uei._load_existing_proof(proof_alias.relative_to(tmp_path))

    standalone_missing = tmp_path / "standalone-missing.txt"
    with pytest.raises(SystemExit) as exc_info:
        uei._write_if_changed(standalone_missing, expected, check=True)
    assert str(exc_info.value) == f"STALE:{standalone_missing}"

    monkeypatch.setattr(uei, "ROOT", tmp_path)
    monkeypatch.setattr(uei, "_STAGED_VIEW", None)
    monkeypatch.setattr(uei, "_ACTIVE_WRITE_TRANSACTION", None)
    cases = (
        (file_alias, "ALIASED_TRANSACTION_FILE"),
        (directory_alias / "owned-file.txt", "ALIASED_TRANSACTION_DIRECTORY"),
    )
    for path, error in cases:
        for check in (False, True):
            with pytest.raises(SystemExit, match=error):
                uei._write_if_changed(path, expected, check=check)
    for check in (False, True):
        with pytest.raises(SystemExit, match="ALIASED_TRANSACTION_FILE"):
            uei._write_path_proof(
                "artifact.log",
                sha256=uei._sha256_bytes(expected),
                size_bytes=len(expected),
                mtime_utc="2026-08-17T00:00:00Z",
                produced_at="2026-08-17T00:00:00Z",
                default_produced_at="2026-08-17T00:00:00Z",
                check=check,
                stat_mtime=artifact.stat().st_mtime,
            )

    assert file_alias.is_symlink()
    assert directory_alias.is_symlink()
    assert proof_alias.is_symlink()
    assert real_file.read_bytes() == expected
    assert (real_directory / "owned-file.txt").read_bytes() == expected
    assert proof_target.is_file()
