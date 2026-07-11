import hashlib, json, subprocess, sys
from pathlib import Path
from engine.serializer import canon
from engine.runtime.identity import identity_admin
from tools.evidence import generate_identity_provenance as identity_provenance

def test_identity_provenance_check_and_outputs_nonwriting():
    before = {p: p.read_bytes() for p in [Path('artifacts/identity/service_identity.json'), Path('artifacts/identity/release_id.json'), Path('artifacts/parity/two_run_identity.log')] if p.exists()}
    subprocess.run([sys.executable,'tools/evidence/generate_identity_provenance.py','--check'], check=True)
    after = {p: p.read_bytes() for p in before}
    assert before == after
    service = json.loads(Path('artifacts/identity/service_identity.json').read_text())
    assert list(service) == sorted(identity_admin())
    assert service == identity_admin()
    manifest = json.loads(Path('catalog/manifest.json').read_text())
    assert hashlib.sha256(canon.sercanon(manifest, sort_keys=True)).hexdigest() == service['release_id']
    inv = json.loads(Path('artifacts/invocation.json').read_text())['invocation']
    assert hashlib.sha256(inv['tag'].encode('utf-8')).hexdigest() == inv['sha256']
    assert inv['sha256'] == service['invocation_sha256']
    assert Path('artifacts/parity/two_run_identity.log').read_bytes().endswith(b'\n')

def test_two_run_identity_uses_independent_identity_serializations(monkeypatch):
    stable = identity_admin()
    drifted = {**stable, "engine_tag": "drifted"}
    runs = iter((stable, drifted))
    monkeypatch.setattr(identity_provenance, "identity_admin", lambda: next(runs))
    monkeypatch.setattr(identity_provenance, "require_closed_rails", lambda: None)

    try:
        identity_provenance._expected()
    except SystemExit as exc:
        assert str(exc) == "TWO_RUN_IDENTITY_MISMATCH"
    else:
        raise AssertionError("independent identity drift was not detected")


def test_invocation_digest_is_recomputed_before_identity_comparison(
    tmp_path,
    monkeypatch,
):
    identity = identity_admin()
    invocation_path = tmp_path / "artifacts/invocation.json"
    invocation_path.parent.mkdir(parents=True)
    invocation_path.write_text(
        json.dumps(
            {
                "invocation": {
                    "tag": identity["invocation_tag"],
                    "sha256": "0" * 64,
                }
            }
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(identity_provenance, "ROOT", tmp_path)

    try:
        identity_provenance._load_validated_invocation(
            {
                **identity,
                "invocation_sha256": "0" * 64,
            }
        )
    except SystemExit as exc:
        assert str(exc) == "INVOCATION_SHA256_MISMATCH"
    else:
        raise AssertionError("invalid invocation digest was accepted")
