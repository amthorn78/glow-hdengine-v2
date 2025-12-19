import datetime as dt
import json

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
    mirror_file_sha = uei._sha256_bytes(uei.MIRROR_PATH.read_bytes())
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

    assert mirror_bytes.decode("utf-8") == mirror_text
    assert proof["sha256"] == mirror_file_sha
    assert proof["mirror_body_sha256"] == rendered_rec["sha256"]
    assert rendered_rec["sha256"] == live_rec["sha256"]
    assert int(rendered_rec["size_bytes"]) == int(live_rec["size_bytes"]) == int(
        proof["size_bytes"]
    )
    assert proof.get("path") == mirror_rel
    assert proof.get("produced_at_utc") == rendered_rec["produced_at_utc"]
