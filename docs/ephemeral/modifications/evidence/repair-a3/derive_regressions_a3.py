"""Derive the round-a3 copies of every earlier regression harness: the round-a2 derivation (derive_regressions_a2.py,
with its listed expectation changes) plus regress_repair_a2.py, all re-pathed from /tmp/claude-0/repair2 to
/tmp/claude-0/repair3. The hardening changes no earlier expectation: all 191 earlier regressions are exact on the
hardened tree as they stand.
usage: python3 derive_regressions_a3.py <out-dir>
"""
import subprocess
import sys
from pathlib import Path

EV = Path(__file__).resolve().parents[1]
OUT = Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True)
subprocess.run([sys.executable, str(EV / "repair-a2/derive_regressions_a2.py"), str(OUT)], check=True)
(OUT / "regress_repair_a2.py").write_text((EV / "repair-a2/regress_repair_a2.py").read_text(encoding="utf-8"), encoding="utf-8")
for p in OUT.glob("*.py"):
    s = p.read_text(encoding="utf-8")
    p.write_text(s.replace("/tmp/claude-0/repair2/", "/tmp/claude-0/repair3/"), encoding="utf-8")
print("derived", sorted(p.name for p in OUT.iterdir()))
