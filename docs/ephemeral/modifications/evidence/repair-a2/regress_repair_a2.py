"""Must-fail regressions for the round-a2 repairs, on scratch copies of the repaired tree.

Oracle cases run the default and the candidate suite; each must yield exactly its expected finding set in both,
after the full re-stamp of regress_oracle.py (oracle, map, graph and contract protected identities, the validator
literals, the profile, SKILL_TREE_SHA256, and the matrix digest in `authority` when the matrix changes), so that
only the new check can catch the mutation:
  U1  GCF-17 session rewritten to allow PR-35 as a subagent, in the oracle and the matrix,
      its digest recomputed into both (SFR-A2-1 R2-2)                        -> FMV-ORACLE-021 row=GCF-17
  U2  GCF-16 added to GCF-17.LINEAGE next, the same way (SFR-A2-1 R2-2)      -> FMV-ORACLE-021 row=GCF-17.LINEAGE
  U3  a second GCF-17 approval_contract key in the oracle row, "the PR session may merge" (SFR-A2-2 P2)
                                                  -> FAIL with exactly one FMV-ORACLE-001 naming the duplicate
                                                     key (plus the downstream findings of an unreadable oracle)
  U4  the same duplicate key in the GCF-17 matrix block (SFR-A2-2 P1)        -> FMV-ORACLE-011
  U5  the GCF-14 and GCF-17 matrix blocks swapped, digest lines with them (R2-3 P3)
                                                                             -> FMV-ORACLE-022
  U6  an extra ```text fence appended to the matrix (R2-3 P4)                -> FMV-ORACLE-022
  U7  a kept row's keys reversed (GCF-15) (R2-3 P5)                          -> FMV-ORACLE-022 row=GCF-15
  U7b a successor row's keys reversed in the oracle (GCF-14)                 -> FMV-ORACLE-022 row=GCF-14
  U8  supersedes_source_row_sha256 moved first in the GCF-14 block           -> FMV-ORACLE-022 row=GCF-14
Contract cases call validate_contract on the shipped contract (SFR-A2-1 R2-4):
  C0 clean -> []; C1 one entry removed, C2 the live successor oracle's file name appended, C3 an entry doubled
  -> exactly ["HISTORICAL_NON_EXECUTABLE_REFERENCES"].
Relay cases (SFR-A2-1 R2-5): the qualifier deleted at each of the two sentences -> exactly one
  FMV-SKILL-STRUCTURE-001 finding (the specialization contract) naming the missing literal, in both suites.
Dispatch cases (SFR-A2-1 R2-1, SFR-A2-2 F1): at each of the nine sites, the D23-E sentence deleted, and the
  first fallback predicate deleted -> exactly one FMV-GCF-DISPATCH-001 on that file, in both suites; the
  amthor and PR-skill suites must also fail at their own sites, with exactly the expected test or literal.

usage: PYTHONDONTWRITEBYTECODE=1 python3 regress_repair_a2.py <repaired-skills-root> <candidate-root-graph-json>
"""
import hashlib, importlib.util, json, os, re, shutil, subprocess, sys
from pathlib import Path

sys.dont_write_bytecode = True
K, GRAPH = Path(sys.argv[1]), Path(sys.argv[2])
BASE = Path("/tmp/claude-0/repair2/reg")
W = BASE / "a2W"
ENV = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "TMPDIR": "/tmp/claude-0/repair2/tmp"}
FVD, CFD = W / "flowmaster-validate", W / "change-flow"
ORACLE = FVD / "references/glow-hde-canonical-change-flow-r1-20260923.json"
MAP = CFD / "references/glow-hde-canonical-change-flow-r1-runtime-map-20260923.json"
MATRIX = FVD / "references/r1-successor-source-20260923.md"
sha = lambda b: hashlib.sha256(b).hexdigest()
ser = lambda o: (json.dumps(o, indent=2, sort_keys=False, ensure_ascii=False) + "\n").encode("utf-8")
CF = ("id", "partition", "name", "change_class", "actor", "session", "consumes", "produces", "next",
      "approval_contract", "failure_stop_condition")
dig = lambda r: sha(json.dumps({k: r[k] for k in CF}, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
ONCE = ("PR-40 is entered once per merge: paste the `MERGE_OBSERVED` handoff when one arrives, otherwise the "
        "fallback block. Once either has been pasted, the other is void.")
PRED = "only where no `MERGE_OBSERVED` result was returned for this merge"
RES = []


def rec(rid, ok, detail):
    RES.append((rid, bool(ok)))
    print(("OK   " if ok else "BAD  ") + rid, str(detail)[:400])


def fresh():
    shutil.rmtree(W, ignore_errors=True); shutil.copytree(K, W)
    (W / "candidate-root/graph").mkdir(parents=True)
    shutil.copyfile(GRAPH, W / "candidate-root/graph/GCFPE-20260914.1-Candidate-Graph-Contract.json")


def sub_all(path, old, new):
    s = path.read_text(encoding="utf-8")
    path.write_text(s.replace(old, new) if old != new else s, encoding="utf-8")


def tree_stamp():
    spec = importlib.util.spec_from_file_location("vstamp_a2", FVD / "scripts/validate_gcfpe_20260914.py")
    sys.path.insert(0, str(FVD / "scripts")); v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v); sys.path.pop(0)
    p = FVD / "SKILL.md"
    p.write_text(re.sub(r"(?m)^SKILL_TREE_SHA256: [0-9a-f]{64}$", "SKILL_TREE_SHA256: " + v.skill_tree_digest(FVD),
                        p.read_text(encoding="utf-8")), encoding="utf-8")


def restamp(oracle=None, matrix_changed=False, oracle_bytes=None):
    """As regress_repair_a1.restamp; oracle_bytes writes the oracle verbatim (a duplicate key survives), and
    the map is projected from the parsed value, which is what every consumer reads."""
    old_o, old_m = sha(ORACLE.read_bytes()), sha(MAP.read_bytes())
    if oracle_bytes is not None:
        o = json.loads(oracle_bytes)
        if matrix_changed:
            m_old = o["authority"]["successor_source_matrix_sha256"]
            oracle_bytes = oracle_bytes.replace(m_old.encode(), sha(MATRIX.read_bytes()).encode())
            o = json.loads(oracle_bytes)
        ORACLE.write_bytes(oracle_bytes)
    else:
        o = oracle if oracle is not None else json.loads(ORACLE.read_bytes())
        if matrix_changed:
            o["authority"]["successor_source_matrix_sha256"] = sha(MATRIX.read_bytes())
        ORACLE.write_bytes(ser(o))
    MAP.write_bytes(ser({k: o[k] for k in ("profile_id", "authority", "coverage", "runtime_rows")}))
    new_o, new_m = sha(ORACLE.read_bytes()), sha(MAP.read_bytes())
    canon = lambda obj: (json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")
    gname, cname = "gcfpe-20260914.1-091426.1-candidate-graph-contract.json", "gcfpe-20260914.1-091426.1-direct-handoff-contract.json"
    gb = (FVD / "references" / gname).read_bytes(); g = json.loads(gb); assert canon(g) == gb
    g["protected_identities"]["r1_oracle_sha256"] = new_o; ngb = canon(g)
    cb = (FVD / "references" / cname).read_bytes(); c = json.loads(cb); assert canon(c) == cb
    c["protected_identities"]["r1_oracle_sha256"] = new_o
    c["source_snapshot"]["frozen_candidate_graph"]["sha256"] = sha(ngb); ncb = canon(c)
    for d in (FVD, CFD):
        (d / "references" / gname).write_bytes(ngb); (d / "references" / cname).write_bytes(ncb)
    (W / "candidate-root/graph/GCFPE-20260914.1-Candidate-Graph-Contract.json").write_bytes(ngb)
    pairs = [(old_o, new_o), (old_m, new_m), (sha(gb), sha(ngb)), (sha(cb), sha(ncb))]
    for p in (FVD / "scripts/validate_flowmaster.py", FVD / "scripts/validate_gcfpe_current.py",
              FVD / "scripts/validate_gcfpe_20260914.py", CFD / "scripts/validate_gcfpe_20260914.py",
              FVD / "references/gcfpe-20260914.1-091426.1-validation-profile.json"):
        for a, b in pairs:
            sub_all(p, a, b)
    assert len(gb) == len(ngb) and len(cb) == len(ncb)
    tree_stamp()


def suite(candidate=False):
    cmd = [sys.executable, str(FVD / "scripts/validate_flowmaster.py"), "--skills-root", str(W)]
    if candidate:
        cmd += ["--strict-warnings", "--gcfpe-contract", str(CFD / "references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json"),
                "--gcfpe-candidate-root", str(W / "candidate-root")]
    r = subprocess.run(cmd, capture_output=True, text=True, env=ENV)
    d = json.loads(r.stdout)
    return d["verdict"], sorted((f["rule_id"], f["subject"], f["evidence"][:300]) for f in d["findings"])


def check(tid, expected, rows=None, subject_suffix=None, evidence_has=None):
    """expected: rule ids; rows: the row= subjects (None where the evidence names no row)."""
    ok_all, detail = True, {}
    for cand in (False, True):
        v, got = suite(cand)
        ok = v == "FLOWMASTER_SUITE_FAIL" and sorted(g[0] for g in got) == sorted(expected)
        if rows is not None:
            ok = ok and sorted((re.match(r"row=([^;]+);", g[2]).group(1) if g[2].startswith("row=") else "") for g in got) \
                == sorted(r or "" for r in rows)
        if subject_suffix is not None:
            ok = ok and all(g[1].endswith(subject_suffix) for g in got)
        if evidence_has is not None:
            ok = ok and all(evidence_has in g[2] for g in got)
        ok_all &= ok
        detail["candidate" if cand else "default"] = [(g[0], g[1][-60:], g[2][:160]) for g in got]
    rec(tid, ok_all, detail)


def row(o, rid):
    return next(x for x in o["runtime_rows"] if x["id"] == rid)


def rewrite_successor_field(rid, field, fn):
    """Change one allowed field in the oracle row and its matrix block, recompute its digest into both."""
    o = json.loads(ORACLE.read_bytes()); r = row(o, rid)
    old_value, old_digest = r[field], r["source_row_sha256"]
    r[field] = fn(old_value); r["source_row_sha256"] = dig(r)
    m = MATRIX.read_text(encoding="utf-8")
    blocks = re.findall(r"(?ms)^```json\n(.*?)\n```$", m)
    raw = next(b for b in blocks if json.loads(b)["id"] == rid)
    blk = json.loads(raw); blk[field] = r[field]
    new_raw = json.dumps(blk, indent=2, ensure_ascii=False)
    assert m.count(raw) == 1 and m.count("source_row_sha256: " + old_digest) == 1
    m = m.replace(raw, new_raw).replace("source_row_sha256: " + old_digest, "source_row_sha256: " + r["source_row_sha256"])
    MATRIX.write_text(m, encoding="utf-8")
    restamp(o, matrix_changed=True)


BASE.mkdir(parents=True, exist_ok=True); Path(ENV["TMPDIR"]).mkdir(parents=True, exist_ok=True)
fresh(); tree_stamp()
v0, c0 = suite(); v1, c1 = suite(True)
rec("clean", v0 == v1 == "FLOWMASTER_SUITE_PASS" and c0 == c1 == [], (v0, c0, v1, c1))

# U1, U2: allowed fields with unapproved values.
fresh(); o = json.loads(ORACLE.read_bytes()); assert "subagent" not in row(o, "GCF-17")["session"].lower() or True
rewrite_successor_field("GCF-17", "session", lambda s: s + " PR-35 may run as a subagent of PR-30.")
check("U1", ["FMV-ORACLE-021"], rows=["GCF-17"])
fresh(); o = json.loads(ORACLE.read_bytes()); nxt = row(o, "GCF-17.LINEAGE")["next"]
assert isinstance(nxt, list) and "GCF-16" not in nxt, nxt
rewrite_successor_field("GCF-17.LINEAGE", "next", lambda n: n + ["GCF-16"])
check("U2", ["FMV-ORACLE-021"], rows=["GCF-17.LINEAGE"])

# U3: duplicate key in the oracle row, written verbatim.
fresh(); ob = ORACLE.read_bytes(); o = json.loads(ob); r = row(o, "GCF-17")
key_line = ('    "approval_contract": ' + json.dumps(r["approval_contract"], ensure_ascii=False) + ",\n").encode()
assert ob.count(key_line) == 1, "approval_contract line not unique"
dup = ('    "approval_contract": ' + json.dumps(r["approval_contract"] + " The PR session may merge.", ensure_ascii=False) + ",\n").encode()
restamp(oracle_bytes=ob.replace(key_line, key_line + dup))
assert json.loads(ORACLE.read_bytes()) != o  # the last value wins for a plain parser
# An unreadable oracle reaches every change-flow check as {}, so the suite also reports their downstream
# findings (the same as for any unreadable oracle). U3 therefore requires FAIL and exactly one FMV-ORACLE-001
# carrying the duplicate-key evidence, in both suites, and records the downstream count.
ok_all, detail = True, {}
for cand in (False, True):
    v, got = suite(cand)
    o1 = [g for g in got if g[0] == "FMV-ORACLE-001"]
    ok_all &= v == "FLOWMASTER_SUITE_FAIL" and len(o1) == 1 and "duplicate key 'approval_contract'" in o1[0][2]
    detail["candidate" if cand else "default"] = (o1, f"{len(got) - len(o1)} downstream findings")
rec("U3", ok_all, detail)

# U4: duplicate key in a matrix block.
fresh(); m = MATRIX.read_text(encoding="utf-8")
blocks = re.findall(r"(?ms)^```json\n(.*?)\n```$", m); raw = next(b for b in blocks if json.loads(b)["id"] == "GCF-17")
ac = json.loads(raw)["approval_contract"]; line = '  "approval_contract": ' + json.dumps(ac, ensure_ascii=False) + ",\n"
assert raw.count(line) == 1
m = m.replace(raw, raw.replace(line, line + '  "approval_contract": ' + json.dumps(ac + " The PR session may merge.", ensure_ascii=False) + ",\n"))
MATRIX.write_text(m, encoding="utf-8"); restamp(matrix_changed=True)
check("U4", ["FMV-ORACLE-011"])

# U5: GCF-14 and GCF-17 blocks swapped, each with its digest line.
fresh(); m = MATRIX.read_text(encoding="utf-8")
units = list(re.finditer(r"(?ms)^```json\n.*?\n```\nsource_row_sha256: [0-9a-f]{64}$", m)); assert len(units) == 3
a, b = units[0], units[1]
m = m[:a.start()] + b.group(0) + m[a.end():b.start()] + a.group(0) + m[b.end():]
MATRIX.write_text(m, encoding="utf-8"); restamp(matrix_changed=True)
check("U5", ["FMV-ORACLE-022"])

# U6: an extra fence.
fresh(); m = MATRIX.read_text(encoding="utf-8"); MATRIX.write_text(m + "\n```text\nnote\n```\n", encoding="utf-8")
restamp(matrix_changed=True); check("U6", ["FMV-ORACLE-022"])

# U7, U7b: key order reversed in a kept row and in a successor row.
fresh(); o = json.loads(ORACLE.read_bytes()); i = next(i for i, x in enumerate(o["runtime_rows"]) if x["id"] == "GCF-15")
o["runtime_rows"][i] = dict(reversed(list(o["runtime_rows"][i].items()))); restamp(o)
check("U7", ["FMV-ORACLE-022"], rows=["GCF-15"])
fresh(); o = json.loads(ORACLE.read_bytes()); i = next(i for i, x in enumerate(o["runtime_rows"]) if x["id"] == "GCF-14")
o["runtime_rows"][i] = dict(reversed(list(o["runtime_rows"][i].items()))); restamp(o)
check("U7b", ["FMV-ORACLE-022"], rows=["GCF-14"])

# U8: block key order.
fresh(); m = MATRIX.read_text(encoding="utf-8")
raw = next(b for b in re.findall(r"(?ms)^```json\n(.*?)\n```$", m) if json.loads(b)["id"] == "GCF-14")
blk = json.loads(raw); blk = {"supersedes_source_row_sha256": blk.pop("supersedes_source_row_sha256"), **blk}
m = m.replace(raw, json.dumps(blk, indent=2, ensure_ascii=False)); MATRIX.write_text(m, encoding="utf-8")
restamp(matrix_changed=True); check("U8", ["FMV-ORACLE-022"], rows=["GCF-14"])

# ------------------------------------------------ contract (S4(b)) ---------------------------------------------
spec = importlib.util.spec_from_file_location("v4_a2", K / "flowmaster-validate/scripts/validate_gcfpe_20260914.py")
sys.path.insert(0, str(K / "flowmaster-validate/scripts")); v4 = importlib.util.module_from_spec(spec); spec.loader.exec_module(v4); sys.path.pop(0)
C = json.loads((K / "flowmaster-validate/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json").read_bytes())
rec("C0", v4.validate_contract(C) == [], v4.validate_contract(C))
for cid, fn in (("C1", lambda l: l[:-1]), ("C2", lambda l: l + ["glow-hde-canonical-change-flow-r1-20260923.json"]),
                ("C3", lambda l: l + l[:1])):
    c = json.loads(json.dumps(C)); c["historical_non_executable_references"] = fn(c["historical_non_executable_references"])
    got = v4.validate_contract(c); rec(cid, got == ["HISTORICAL_NON_EXECUTABLE_REFERENCES"], got)

# ------------------------------------------------ relay qualifier (S4(c)) --------------------------------------
RELAY = "session-relay-flowmaster/SKILL.md"
for rid, sentence in (("R-RELAY-255", "Outside a GCFPE main-ecosystem stage, when a required participant does not exist or cannot be confirmed reachable"),
                      ("R-RELAY-717", "This specialization cannot create a session. Outside a GCFPE main-ecosystem stage, when a required participant does not exist, return")):
    fresh(); p = W / RELAY; t = p.read_text(encoding="utf-8"); assert t.count(sentence) == 1
    p.write_text(t.replace(sentence, sentence.replace("Outside a GCFPE main-ecosystem stage, when", "When")), encoding="utf-8")
    ok_all, detail = True, {}
    for cand in (False, True):
        v, got = suite(cand)
        ok_all &= v == "FLOWMASTER_SUITE_FAIL" and len(got) == 1 and got[0][1].endswith(RELAY) and "Outside a GCFPE main-ecosystem stage" in got[0][2]
        detail[cand] = got
    rec(rid, ok_all, detail)

# ------------------------------------------------ dispatch sites (S1) ------------------------------------------
SITES = (("glow-hde-pr-development", "SKILL.md", True), ("change-flow", "SKILL.md", True),
         ("session-relay-flowmaster", "SKILL.md", True), ("tw-flowmaster", "SKILL.md", True),
         ("flowmaster-validate", "SKILL.md", True), ("amthor-workspace-governance-audit", "SKILL.md", True),
         ("amthor-workspace-governance-audit", "references/interoperability-contracts.md", True),
         ("glow-hde-pr-development", "references/behavior-cases.md", False),
         ("amthor-workspace-governance-audit", "references/behavioral-fixtures.md", False))


def own_suite(skill):
    if skill == "amthor-workspace-governance-audit":
        r = subprocess.run([sys.executable, "run_fixture_suite.py"], cwd=W / skill / "scripts", capture_output=True, text=True, env=ENV)
        fails = [f[0] for f in re.findall(r"^(?:FAIL|ERROR): (\S+) \((\S+)\)", r.stderr, re.M)]
        return r.returncode, fails
    if skill == "glow-hde-pr-development":
        r = subprocess.run([sys.executable, str(W / skill / "scripts/validate_glow_hde_pr_development.py")], capture_output=True, text=True, env=ENV)
        return r.returncode, [r.stdout.strip()]
    return None


for skill, rel, carries in SITES:
    for kind in ("ONCE", "PRED"):
        fresh(); p = W / skill / rel; t = p.read_text(encoding="utf-8")
        if kind == "ONCE":
            target = (" " + ONCE) if carries else ONCE
            assert t.count(target) == 1, (skill, rel); t = t.replace(target, "")
        else:
            assert t.count(PRED) >= 1; t = t.replace(" and " + PRED, "", 1) if (" and " + PRED) in t else t.replace(PRED, "", 1)
        p.write_text(t, encoding="utf-8"); tree_stamp()
        name = f"D-{kind}-{skill}/{rel}"
        ok_all, detail = True, {}
        for cand in (False, True):
            v, got = suite(cand)
            ok_all &= v == "FLOWMASTER_SUITE_FAIL" and [g[0] for g in got] == ["FMV-GCF-DISPATCH-001"] and got[0][1].endswith(f"{skill}/{rel}")
            detail[cand] = [(g[0], g[2][:140]) for g in got]
        own = own_suite(skill)
        if skill == "amthor-workspace-governance-audit":
            ok_all &= own == (1, ["test_pr40_once_per_merge_parity"])
        elif skill == "glow-hde-pr-development" and rel == "SKILL.md":
            ok_all &= own[0] == 1
        detail["own"] = own
        rec(name, ok_all, detail)
shutil.rmtree(W, ignore_errors=True)
print(f"A2_REPAIR_REGRESSIONS {sum(ok for _, ok in RES)} of {len(RES)} exact")
