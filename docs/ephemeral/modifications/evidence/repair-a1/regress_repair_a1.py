"""Must-fail regressions for the round-a1 repairs, on scratch copies of the repaired tree.

Oracle cases (R1, R2) run the default and the candidate suite; each must yield exactly its expected finding set
in both, after the full re-stamp of regress_oracle.py (oracle, map, graph and contract protected identities, the
validator literals, the profile, SKILL_TREE_SHA256, and the matrix digest in `authority` when the matrix
changes), so that only the new check can catch the mutation:
  T6   one matrix `source_row_sha256:` line tampered (GCF-14)         -> FMV-ORACLE-018 row=GCF-14
  T6b  the GCF-14 and GCF-17 lines swapped (block order)              -> FMV-ORACLE-018 rows GCF-14, GCF-17
  T7   all three digest lines deleted                                 -> FMV-ORACLE-018 (one finding)
  T1   GCF-14 moved to the end of runtime_rows (SFR-A1-1 T1)          -> FMV-ORACLE-019 row=GCF-14
  T3   one prohibited_active_patterns entry dropped (SFR-A1-1 T3)     -> FMV-ORACLE-020
  T3b  one non-profile required_global_tokens entry dropped           -> FMV-ORACLE-020
  T3c  an extra authority key added                                   -> FMV-ORACLE-020
  T5   GCF-17 approval_contract changed in oracle and matrix, its row
       digest recomputed into the oracle and the matrix line, every
       pin re-stamped (SFR-A1-1 T5)                                   -> FMV-ORACLE-019 row=GCF-17
PR-skill cases (R3, R5) run validate_glow_hde_pr_development.py (fail-fast stdout) and the non-fail-fast
evaluation of regress_skills.py; each must yield exactly its expected failure set.

usage: PYTHONDONTWRITEBYTECODE=1 python3 regress_repair_a1.py <repaired-skills-root> <candidate-root-graph-json>
"""
import ast, hashlib, json, os, re, shutil, subprocess, sys
from pathlib import Path

sys.dont_write_bytecode = True
K, GRAPH = Path(sys.argv[1]), Path(sys.argv[2])
BASE = Path("/tmp/claude-0/repair/reg")
W = BASE / "a1W"
ENV = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "TMPDIR": "/tmp/claude-0/repair/tmp"}
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


# ------------------------------------------------ oracle harness (as regress_oracle.py) -------------------------
def fresh():
    shutil.rmtree(W, ignore_errors=True); shutil.copytree(K, W)
    (W / "candidate-root/graph").mkdir(parents=True)
    shutil.copyfile(GRAPH, W / "candidate-root/graph/GCFPE-20260914.1-Candidate-Graph-Contract.json")


def sub_all(path, old, new):
    s = path.read_text(encoding="utf-8")
    path.write_text(s.replace(old, new) if old != new else s, encoding="utf-8")


def tree_stamp():
    import importlib.util
    spec = importlib.util.spec_from_file_location("vstamp_a1", FVD / "scripts/validate_gcfpe_20260914.py")
    sys.path.insert(0, str(FVD / "scripts")); v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v); sys.path.pop(0)
    p = FVD / "SKILL.md"
    p.write_text(re.sub(r"(?m)^SKILL_TREE_SHA256: [0-9a-f]{64}$", "SKILL_TREE_SHA256: " + v.skill_tree_digest(FVD),
                        p.read_text(encoding="utf-8")), encoding="utf-8")


def restamp(oracle=None, matrix_changed=False):
    old_o, old_m = sha(ORACLE.read_bytes()), sha(MAP.read_bytes())
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
    return d["verdict"], sorted((f["rule_id"], f["evidence"][:200]) for f in d["findings"])


def check(tid, expected, rows=None):
    """expected: sorted list of rule ids; rows: the row= subjects, in the same order, where the case names rows."""
    ok_all, detail = True, {}
    for cand in (False, True):
        v, got = suite(cand)
        ids = sorted(g[0] for g in got)
        ok = v == "FLOWMASTER_SUITE_FAIL" and ids == sorted(expected)
        if rows is not None:
            ok = ok and sorted(re.match(r"row=([^;]+);", g[1]).group(1) if g[1].startswith("row=") else None for g in got) == sorted(rows)
        ok_all &= ok
        detail["candidate" if cand else "default"] = got
    rec(tid, ok_all, detail)


def row(o, rid):
    return next(x for x in o["runtime_rows"] if x["id"] == rid)


BASE.mkdir(parents=True, exist_ok=True)
fresh(); tree_stamp()
v0, c0 = suite(); v1, c1 = suite(True)
rec("clean", v0 == v1 == "FLOWMASTER_SUITE_PASS" and c0 == c1 == [], (v0, c0, v1, c1))
LINE_RE = re.compile(r"(?m)^source_row_sha256: ([0-9a-f]{64})$")

# T6: one tampered digest line, matrix digest written into authority, every pin re-stamped.
fresh(); m = MATRIX.read_text(encoding="utf-8"); first = LINE_RE.findall(m)[0]
assert m.count(first) == 1
MATRIX.write_text(m.replace("source_row_sha256: " + first, "source_row_sha256: " + "0" * 64), encoding="utf-8")
restamp(matrix_changed=True); check("T6", ["FMV-ORACLE-018"], rows=["GCF-14"])
# T6b: the first two lines swapped, so each is in the wrong block.
fresh(); m = MATRIX.read_text(encoding="utf-8"); a, b = LINE_RE.findall(m)[:2]
m = m.replace(a, "@A@").replace(b, a).replace("@A@", b); MATRIX.write_text(m, encoding="utf-8")
restamp(matrix_changed=True); check("T6b", ["FMV-ORACLE-018", "FMV-ORACLE-018"], rows=["GCF-14", "GCF-17"])
# T7: all three digest lines deleted, re-stamped.
fresh(); m = MATRIX.read_text(encoding="utf-8"); m2, n = LINE_RE.subn("", m); assert n == 3
MATRIX.write_text(m2, encoding="utf-8"); restamp(matrix_changed=True); check("T7", ["FMV-ORACLE-018"])
# T1: move GCF-14 to the end of runtime_rows, re-stamped.
fresh(); o = json.loads(ORACLE.read_bytes()); r = row(o, "GCF-14"); o["runtime_rows"].remove(r); o["runtime_rows"].append(r)
restamp(o); check("T1", ["FMV-ORACLE-019"], rows=["GCF-14"])
# T3: drop one prohibited_active_patterns entry, re-stamped.
fresh(); o = json.loads(ORACLE.read_bytes()); dropped = o["prohibited_active_patterns"].pop(0)
restamp(o); check("T3", ["FMV-ORACLE-020"])
# T3b: drop one required_global_tokens entry that is not the profile id, re-stamped.
fresh(); o = json.loads(ORACLE.read_bytes())
i = next(i for i, t in enumerate(o["required_global_tokens"]) if t != o["profile_id"]); o["required_global_tokens"].pop(i)
restamp(o); check("T3b", ["FMV-ORACLE-020"])
# T3c: add an authority key after the successor keys, re-stamped.
fresh(); o = json.loads(ORACLE.read_bytes()); o["authority"]["successor_note"] = "unauthorised"
restamp(o); check("T3c", ["FMV-ORACLE-020"])
# T5: an unauthorised GCF-17 field change in both the oracle and the matrix, digest recomputed in both places.
fresh(); o = json.loads(ORACLE.read_bytes()); r = row(o, "GCF-17")
old_ac, old_digest = r["approval_contract"], r["source_row_sha256"]
r["approval_contract"] = old_ac + " The PR session may merge after review."; r["source_row_sha256"] = dig(r)
m = MATRIX.read_text(encoding="utf-8")
assert m.count(json.dumps(old_ac, ensure_ascii=False)) == 1 and m.count("source_row_sha256: " + old_digest) == 1
m = m.replace(json.dumps(old_ac, ensure_ascii=False), json.dumps(r["approval_contract"], ensure_ascii=False))
m = m.replace("source_row_sha256: " + old_digest, "source_row_sha256: " + r["source_row_sha256"])
MATRIX.write_text(m, encoding="utf-8")
restamp(o, matrix_changed=True); check("T5", ["FMV-ORACLE-019"], rows=["GCF-17"])
shutil.rmtree(W, ignore_errors=True)


# ------------------------------------------------ PR skill (R3, R5) --------------------------------------------
def pr_all_failures(root):
    tree = ast.parse((root / "glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py").read_text())
    d = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name):
            n = node.targets[0].id
            if n == "required":
                d["required"] = {k.value: v.value for k, v in zip(node.value.keys, node.value.values)}
            elif n in ("forbidden", "case_headings"):
                d[n] = [e.value for e in node.value.elts]
    skill = (root / "glow-hde-pr-development/SKILL.md").read_text()
    cases = (root / "glow-hde-pr-development/references/behavior-cases.md").read_text()
    comb = skill + "\n" + cases
    f = {f"missing {k} contract" for k, t in d["required"].items() if t not in comb}
    f |= {f"forbidden or unfinished content present: {t}" for t in d["forbidden"] if t.lower() in comb.lower()}
    f |= {f"missing behavior case: {h}" for h in d["case_headings"] if h not in cases}
    return f


def replace_once(a, b):
    def fn(t):
        assert t.count(a) == 1, (t.count(a), a[:70]); return t.replace(a, b)
    return fn


def delete_all(a):
    def fn(t):
        assert t.count(a) >= 1, a[:70]; return t.replace(a, "")
    return fn


S, B = "glow-hde-pr-development/SKILL.md", "glow-hde-pr-development/references/behavior-cases.md"
FB1, FB2, ONCEL = "missing merge fallback predicate contract", "missing conditional PR-40 fallback predicate contract", "missing PR-40 once per merge contract"
pr_cases = [
    # V2's attack: every occurrence of the predicate deleted from SKILL.md.
    ("R-FB-SKILL", [(S, delete_all(" and " + PRED))], FB1, {FB1, FB2}),
    ("R-FB-ALL", [(S, delete_all(PRED)), (B, delete_all(PRED))], FB1, {FB1, FB2}),
    ("R-FB-DISPATCH", [(S, replace_once(" and only where no `MERGE_OBSERVED` result was returned for this merge; stay subscribed", "; stay subscribed"))], FB1, {FB1}),
    ("R-FB-CONDITIONAL", [(S, replace_once("identified PR and only where no `MERGE_OBSERVED` result was returned for this merge;", "identified PR;"))], FB2, {FB2}),
    ("R-ONCE", [(S, replace_once(" " + ONCE, ""))], ONCEL, {ONCEL}),
    ("R-ONCE-VOID", [(S, replace_once(" Once either has been pasted, the other is void.", ""))], ONCEL, {ONCEL}),
]
r = subprocess.run([sys.executable, str(K / "glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py")], capture_output=True, text=True, env=ENV)
rec("PR-clean", r.returncode == 0 and pr_all_failures(K) == set(), (r.stdout.strip(), sorted(pr_all_failures(K))))
for name, muts, first, expected in pr_cases:
    d = BASE / name; shutil.rmtree(d, ignore_errors=True)
    shutil.copytree(K / "glow-hde-pr-development", d / "glow-hde-pr-development")
    for rel, fn in muts:
        p = d / rel; p.write_text(fn(p.read_text(encoding="utf-8")), encoding="utf-8")
    r = subprocess.run([sys.executable, str(d / "glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py")], capture_output=True, text=True, env=ENV)
    af = pr_all_failures(d)
    rec(name, r.returncode == 1 and r.stdout.strip() == "FAIL: " + first and af == expected, (r.returncode, r.stdout.strip(), sorted(af)))
    shutil.rmtree(d)

# R5 placement: the sentence is appended to C-DISPATCH exactly once at each skill site that carries C-DISPATCH.
ANCHOR = "No agent merges, and no session is created by an agent. " + ONCE
sites = ["glow-hde-pr-development/SKILL.md", "change-flow/SKILL.md", "session-relay-flowmaster/SKILL.md", "tw-flowmaster/SKILL.md",
         "flowmaster-validate/SKILL.md", "amthor-workspace-governance-audit/SKILL.md",
         "amthor-workspace-governance-audit/references/interoperability-contracts.md"]
counts = {s: (K / s).read_text(encoding="utf-8").count(ANCHOR) for s in sites}
carriers = sorted(str(p.relative_to(K)) for p in K.rglob("*") if p.is_file() and p.suffix == ".md"
                  and "The observed merge event is the fact PR-40 is entered on" in p.read_text(encoding="utf-8", errors="replace"))
rec("R5-SITES", all(v == 1 for v in counts.values()) and carriers == sorted(sites), (counts, carriers))
print(f"A1_REPAIR_REGRESSIONS {sum(ok for _, ok in RES)} of {len(RES)} exact")
