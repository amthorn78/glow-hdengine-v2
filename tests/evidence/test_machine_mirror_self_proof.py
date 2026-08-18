import datetime as dt
import json
import os
import stat

import pytest

from tools.evidence import update_evidence_index as uei


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

    assert file_alias.is_symlink()
    assert directory_alias.is_symlink()
    assert real_file.read_bytes() == expected
    assert (real_directory / "owned-file.txt").read_bytes() == expected
