"""Must-fail regressions for the round-a3 hardening (H1-H5), on scratch copies of the hardened tree.

Harness: regress_repair_a2.py's, re-pathed (full re-stamp of every pin; each oracle-side case runs the default and
the candidate suite and must give exactly its expected finding set in both).
  Q1  a fourth JSON block inside a block quote in the matrix (SFR-A3-2 Q1, SFR-A3-1 F1)  -> FMV-ORACLE-022
  Q2  the same inside a list item (SFR-A3-2 Q2)                                           -> FMV-ORACLE-022
  Q3  an HTML <pre> block in the matrix (SFR-A3-2 Q3)                                      -> FMV-ORACLE-022
  Q8  change-flow: one fallback predicate removed from its sentence and re-added at the end
      of the file, so the count is unchanged (SFR-A3-2 Q8)                                -> FMV-GCF-DISPATCH-001
  Q9  PR skill: the anchored pair ("No agent merges, ..." + the D23-E sentence) moved out of C-DISPATCH
      to the end of the file (SFR-A3-2 Q9)                                                -> FMV-GCF-DISPATCH-001
  Q10 behavior-cases: the D23-E sentence put inside an HTML comment in place (SFR-A3-1 limit)
                                                                                          -> FMV-GCF-DISPATCH-001
Control: every case except K0, K2 and Q2 must fail on the round-a3 reviewed tree (outputs/regress_repair_a3_on_pre.out);
Q2 was already caught there, as SFR-A3-1 found.
  Q11 behavioral-fixtures: the D23-E sentence moved to the end of the file                  -> FMV-GCF-DISPATCH-001
  V1  amthor removed from the skills root (SFR-A3-1 V1)   -> exactly three FMV-GCF-DISPATCH-001, one per amthor site
  V2  an extra top-level key in the successor map, map pin re-stamped (SFR-A3-1 V2)       -> FMV-GCF-MAP-005
  K0  validate_contract on the shipped contract -> []
  K1  route_graph_semantics.pr40_entry reverted to the pre-a3 text (without the D23-E sentence)
                                                                -> exactly ["ROUTE_GRAPH_SEMANTICS"]
  K2  the graph and routing surface are the ones Nathan read: graph ae2bd159..., routing fecc319b.../284,
      and the contract's source_snapshot still names that graph.

usage: PYTHONDONTWRITEBYTECODE=1 python3 regress_repair_a3.py <hardened-skills-root> <candidate-root-graph-json>
"""
import hashlib, importlib.util, json, os, re, shutil, subprocess, sys
from pathlib import Path

sys.dont_write_bytecode = True
K, GRAPH = Path(sys.argv[1]), Path(sys.argv[2])
BASE = Path("/tmp/claude-0/repair3/reg")
W = BASE / "a3W"
ENV = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "TMPDIR": "/tmp/claude-0/repair3/tmp"}
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
    spec = importlib.util.spec_from_file_location("vstamp_a3", FVD / "scripts/validate_gcfpe_20260914.py")
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



def restamp_map_only():
    """Re-stamp after a map-only change: the map pin in both validators and the profile, then the tree digest."""
    old_m = MAP_OLD
    new_m = sha(MAP.read_bytes())
    for p in (FVD / "scripts/validate_flowmaster.py", FVD / "scripts/validate_gcfpe_current.py",
              FVD / "scripts/validate_gcfpe_20260914.py", CFD / "scripts/validate_gcfpe_20260914.py",
              FVD / "references/gcfpe-20260914.1-091426.1-validation-profile.json", CFD / "SKILL.md"):
        sub_all(p, old_m, new_m)
    tree_stamp()


def move(rel, text_fn):
    p = W / rel
    p.write_text(text_fn(p.read_text(encoding="utf-8")), encoding="utf-8")
    tree_stamp()


def dispatch_check(tid, subject_suffixes):
    ok_all, detail = True, {}
    for cand in (False, True):
        v, got = suite(cand)
        ok_all &= v == "FLOWMASTER_SUITE_FAIL" and [g[0] for g in got] == ["FMV-GCF-DISPATCH-001"] * len(subject_suffixes) \
            and sorted(g[1].rsplit("/", 2)[-2] + "/" + g[1].rsplit("/", 2)[-1] if "/" in g[1] else g[1] for g in got) == sorted(subject_suffixes)
        detail["candidate" if cand else "default"] = [(g[0], g[1][-60:], g[2][:200]) for g in got]
    rec(tid, ok_all, detail)


BASE.mkdir(parents=True, exist_ok=True); Path(ENV["TMPDIR"]).mkdir(parents=True, exist_ok=True)
fresh(); tree_stamp()
v0, c0 = suite(); v1, c1 = suite(True)
rec("clean", v0 == v1 == "FLOWMASTER_SUITE_PASS" and c0 == c1 == [], (v0, c0, v1, c1))

FAKE = json.dumps({"id": "GCF-17", "session": "PR-35 may run as a subagent of PR-30"}, indent=2)
# Q1-Q3: a rendered fourth block the old count missed.
for qid, extra in (("Q1", "\n> ```json\n" + "\n".join("> " + l for l in FAKE.split("\n")) + "\n> ```\n"),
                   ("Q2", "\n- note:\n  ```json\n" + "\n".join("  " + l for l in FAKE.split("\n")) + "\n  ```\n"),
                   ("Q3", "\n<pre>\n" + FAKE + "\n</pre>\n")):
    fresh(); m = MATRIX.read_text(encoding="utf-8"); MATRIX.write_text(m + extra, encoding="utf-8")
    restamp(matrix_changed=True); check(qid, ["FMV-ORACLE-022"])

# Q8: a change-flow predicate moved, count unchanged.
CF_CTX = "invocation. Only after Nathan has manually merged the identified PR, and only where no `MERGE_OBSERVED` result was returned for this merge,"
fresh()
move("change-flow/SKILL.md", lambda t: (lambda u: u + "\nNote: " + PRED + ".\n")(t.replace(CF_CTX, CF_CTX.replace(" and " + PRED, ""), 1)))
assert (W / "change-flow/SKILL.md").read_text(encoding="utf-8").count(PRED) == 4
dispatch_check("Q8", ["change-flow/SKILL.md"])
# Q9: the anchored pair (C-DISPATCH's last two sentences) moved to the end of the PR skill; every count holds.
fresh()
PAIR = "No agent merges, and no session is created by an agent. " + ONCE
move("glow-hde-pr-development/SKILL.md", lambda t: t.replace(" " + PAIR, "", 1) + "\n" + PAIR + "\n")
dispatch_check("Q9", ["glow-hde-pr-development/SKILL.md"])
# Q10: the fixture-text D23-E sentence put inside an HTML comment in place.
fresh()
move("glow-hde-pr-development/references/behavior-cases.md", lambda t: t.replace(ONCE, "<!-- " + ONCE + " -->", 1))
dispatch_check("Q10", ["references/behavior-cases.md"])
# Q11: the fixture sentence moved to the end of behavioral-fixtures.md.
fresh()
move("amthor-workspace-governance-audit/references/behavioral-fixtures.md", lambda t: t.replace(" " + ONCE, "", 1) + "\n" + ONCE + "\n")
dispatch_check("Q11", ["references/behavioral-fixtures.md"])

# V1: amthor removed.
fresh(); shutil.rmtree(W / "amthor-workspace-governance-audit")
ok_all, detail = True, {}
for cand in (False, True):
    v, got = suite(cand)
    ok_all &= v == "FLOWMASTER_SUITE_FAIL" and [g[0] for g in got] == ["FMV-GCF-DISPATCH-001"] * 3 \
        and all(g[1] == "amthor-workspace-governance-audit" for g in got)
    detail["candidate" if cand else "default"] = [(g[0], g[1], g[2][:120]) for g in got]
rec("V1", ok_all, detail)

# V2: an extra top-level key in the successor map, its pin re-stamped everywhere.
fresh(); MAP_OLD = sha(MAP.read_bytes()); mp = json.loads(MAP.read_bytes()); mp["note"] = "unauthorised"
MAP.write_bytes(ser(mp)); restamp_map_only()
check("V2", ["FMV-GCF-MAP-005"])

# K0-K2: the contract-only value, and the unchanged graph and routing surface.
spec = importlib.util.spec_from_file_location("v4_a3", K / "flowmaster-validate/scripts/validate_gcfpe_20260914.py")
sys.path.insert(0, str(K / "flowmaster-validate/scripts")); v4 = importlib.util.module_from_spec(spec); spec.loader.exec_module(v4); sys.path.pop(0)
C = json.loads((K / "flowmaster-validate/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json").read_bytes())
rec("K0", v4.validate_contract(C) == [], v4.validate_contract(C))
c = json.loads(json.dumps(C)); c["route_graph_semantics"]["pr40_entry"] = c["route_graph_semantics"]["pr40_entry"].replace(" " + ONCE, "")
got = v4.validate_contract(c); rec("K1", got == ["ROUTE_GRAPH_SEMANTICS"], got)
gb = (K / "flowmaster-validate/references/gcfpe-20260914.1-091426.1-candidate-graph-contract.json").read_bytes(); g = json.loads(gb)
surface = v4.routing_surface({"route_edges": g["edges"], "state_routes": g["state_routes"]})
rec("K2", sha(gb).startswith("ae2bd159") and surface == ("fecc319bdd4ce7ee6201cb77d7231861", 284)
    and C["source_snapshot"]["frozen_candidate_graph"]["sha256"] == sha(gb), (sha(gb)[:16], surface))
shutil.rmtree(W, ignore_errors=True)
print(f"A3_REPAIR_REGRESSIONS {sum(ok for _, ok in RES)} of {len(RES)} exact")
