import os, glob, pathlib

def test_architecture_md_exists():
    assert pathlib.Path("ARCHITECTURE.md").exists(), "ARCHITECTURE.md missing"

def test_latest_arch_snapshot_lf_and_present():
    snaps = sorted(glob.glob("_arch/*/routes.txt"))
    assert snaps, "No _arch snapshots found — run scripts/architecture_capture.sh"
    # verify LF termination on a few key files
    base = pathlib.Path(snaps[-1]).parent
    for name in ("routes.txt","imports.adapters.txt","imports.core.txt","imports.server.txt","tree.txt","status.txt"):
        p = base / name
        assert p.exists(), f"{p} missing"
        with open(p,"rb") as f:
            data = f.read()
        assert data.endswith(b"\n"), f"{p} must be LF-terminated"
