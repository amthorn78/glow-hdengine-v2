"""Derive the round-a2 copies of the earlier regression harnesses, with every changed expectation asserted.

The originals (e2/*.py, repair-a1/regress_repair_a1.py) stay unchanged as the record of their rounds. The copies
are written to <out>, re-pathed to /tmp/claude-0/repair2/{tmp,reg}. Each substitution asserts its anchor once.
The only expectation changes, all consequences of the round-a2 repairs, not relaxations:
  regress_oracle.py G2, G3   gain FMV-ORACLE-021: the mutated row digest is no longer the approved digest (S2).
  regress_skills.py          the amthor suite runs 35 tests, not 34: S1 adds test_pr40_once_per_merge_parity.
                             R-DISP (C-DISPATCH's last sentence deleted) fails two PR-skill literals, not one: S1
                             anchors the once-per-merge literal to that sentence; the first failure is unchanged.
  regress_repair_a1.py T1    gains FMV-ORACLE-022: GCF-14 moved to the end puts the matrix blocks out of oracle
                             row order (S4(a)). Its row check maps a finding without a row to "" rather than None,
                             so the sort can compare it.
  regress_repair_a1.py T5    gains FMV-ORACLE-021 on GCF-17, as G2 (S2).
usage: python3 derive_regressions_a2.py <out-dir>
"""
import sys
from pathlib import Path

EV = Path(__file__).resolve().parents[1]
OUT = Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True)
PATHS = [("/tmp/claude-0/e2/tmp", "/tmp/claude-0/repair2/tmp"), ("/tmp/claude-0/e2/reg", "/tmp/claude-0/repair2/reg"),
         ("/tmp/claude-0/repair/tmp", "/tmp/claude-0/repair2/tmp"), ("/tmp/claude-0/repair/reg", "/tmp/claude-0/repair2/reg")]
CHANGES = {
    "e2/regress_oracle.py": [
        ('restamp(o); check("G2", suite()[1], ["FMV-ORACLE-012", "FMV-ORACLE-018"], row="GCF-17")',
         '# (round-a2 repair S2) and FMV-ORACLE-021: the recomputed digest is not the approved GCF-17 digest.\n'
         'restamp(o); check("G2", suite()[1], ["FMV-ORACLE-012", "FMV-ORACLE-018", "FMV-ORACLE-021"], row="GCF-17")'),
        ('restamp(o); check("G3", suite()[1], ["FMV-ORACLE-013", "FMV-ORACLE-018"], row="GCF-14")',
         '# (round-a2 repair S2) and FMV-ORACLE-021: 0*64 is not the approved GCF-14 digest.\n'
         'restamp(o); check("G3", suite()[1], ["FMV-ORACLE-013", "FMV-ORACLE-018", "FMV-ORACLE-021"], row="GCF-14")'),
    ],
    "e2/regress_skills.py": [
        ('ran and ran.group(1) == "34"', 'ran and ran.group(1) == "35"  # round-a2 S1 adds one amthor test'),
        ('"FAIL: missing no agent-created session contract", 1),',
         '"FAIL: missing no agent-created session contract", 2),  # a2 S1: the once-per-merge literal is anchored here'),
    ],
    "repair-a1/regress_repair_a1.py": [
        ('if g[1].startswith("row=") else None for g in got) == sorted(rows)',
         'if g[1].startswith("row=") else "" for g in got) == sorted(r or "" for r in rows)'),
        ('restamp(o); check("T1", ["FMV-ORACLE-019"], rows=["GCF-14"])',
         'restamp(o); check("T1", ["FMV-ORACLE-019", "FMV-ORACLE-022"], rows=["GCF-14", None])  # a2 S4(a): block order'),
        ('restamp(o, matrix_changed=True); check("T5", ["FMV-ORACLE-019"], rows=["GCF-17"])',
         'restamp(o, matrix_changed=True); check("T5", ["FMV-ORACLE-019", "FMV-ORACLE-021"], rows=["GCF-17", "GCF-17"])  # a2 S2'),
    ],
}
for rel in ("e2/run_suites.py", "e2/regress_oracle.py", "e2/regress_skills.py", "e2/regress_contract.py",
            "e2/regress_fixtures.py", "e2/texts.py", "repair-a1/regress_repair_a1.py"):
    s = (EV / rel).read_text(encoding="utf-8")
    for old, new in CHANGES.get(rel, []):
        assert s.count(old) == 1, (rel, old[:80], s.count(old))
        s = s.replace(old, new)
    for old, new in PATHS:
        s = s.replace(old, new)
    (OUT / Path(rel).name).write_text(s, encoding="utf-8")
print("derived", sorted(p.name for p in OUT.iterdir()))
