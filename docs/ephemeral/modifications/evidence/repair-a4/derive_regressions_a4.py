"""Derive the round-a4 copies of every earlier regression harness: the round-a3 derivation (E2, round a1 and round
a2 harnesses, with the expectation changes derive_regressions_a2.py lists) plus regress_repair_a3.py, all
re-pathed to /tmp/claude-0/repair4. The round-a4 repairs change no earlier expectation.
usage: python3 derive_regressions_a4.py <out-dir>
"""
import subprocess
import sys
from pathlib import Path

EV = Path(__file__).resolve().parents[1]
OUT = Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True)
subprocess.run([sys.executable, str(EV / "repair-a3/derive_regressions_a3.py"), str(OUT)], check=True)
(OUT / "regress_repair_a3.py").write_text((EV / "repair-a3/regress_repair_a3.py").read_text(encoding="utf-8"), encoding="utf-8")
for p in OUT.glob("*.py"):
    s = p.read_text(encoding="utf-8")
    p.write_text(s.replace("/tmp/claude-0/repair3/", "/tmp/claude-0/repair4/"), encoding="utf-8")
print("derived", sorted(p.name for p in OUT.iterdir()))
