import hashlib, json, subprocess
from pathlib import Path
from engine.serializer import canon
from engine.runtime.identity import identity_admin
from tools.evidence import generate_identity_provenance as identity_provenance

def test_identity_provenance_check_and_outputs_nonwriting():
    before = {p: p.read_bytes() for p in [Path('artifacts/identity/service_identity.json'), Path('artifacts/identity/release_id.json'), Path('artifacts/parity/two_run_identity.log')] if p.exists()}
    subprocess.run(['python','tools/evidence/generate_identity_provenance.py','--check'], check=True)
    after = {p: p.read_bytes() for p in before}
    assert before == after
    service = json.loads(Path('artifacts/identity/service_identity.json').read_text())
    assert list(service) == sorted(identity_admin())
    assert service == identity_admin()
    manifest = json.loads(Path('catalog/manifest.json').read_text())
    assert hashlib.sha256(canon.sercanon(manifest, sort_keys=True)).hexdigest() == service['release_id']
    inv = json.loads(Path('artifacts/invocation.json').read_text())['invocation']
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
