"""Must-fail regressions for the round-a4 repairs (R1-R3), on scratch copies of the repaired tree.

Harness: regress_repair_a3.py's, re-pathed (full re-stamp of every pin; each case runs the default and the candidate
suite and must give exactly its expected finding set in both).
  P1  change-flow: a comment carrying a contradicting instruction inside the pinned C-DISPATCH passage
      (SFR-A4-2 F1)                                                                       -> FMV-GCF-DISPATCH-001
  P2  PR skill: an unclosed `<!--` on its own line before the passage (SFR-A4-2 F1)       -> FMV-GCF-DISPATCH-001
  P3  relay: a comment closed with `--!>` (SFR-A4-1 A4-2)                                  -> FMV-GCF-DISPATCH-001
  P4  behavior-cases: a closed comment added after the D23-E sentence, every pinned text intact
                                                                                          -> FMV-GCF-DISPATCH-001
  M1  the successor map's top-level keys reordered, nothing else, map pin re-stamped (SFR-A4-1 A4-1,
      SFR-A4-2 F2)                                                                        -> FMV-GCF-MAP-005
  M2  a fourth block as a 4-space indented code block in the matrix (SFR-A4-1 M1, SFR-A4-2 F3)
                                                                                          -> FMV-ORACLE-022
  M3  the same inside <xmp>; M4 inside <textarea>; M5 inside <listing> (SFR-A4-1 M2/M6, SFR-A4-2 F3)
                                                                                          -> FMV-ORACLE-022
  K3  contract_recipe.py reproduces the shipped contract byte for byte from the unchanged E2 regenerator plus
      the round-a3 H5 step (SFR-A4-1 A4-O1)                                               -> exit 0, both copies EQUAL
Control: every case except K3 fails on the round-a4 reviewed tree (outputs/regress_repair_a4_on_pre.out).

usage: PYTHONDONTWRITEBYTECODE=1 python3 regress_repair_a4.py <repaired-skills-root> <candidate-root-graph-json> <graph-md>
"""
import hashlib, importlib.util, json, os, re, shutil, subprocess, sys
from pathlib import Path

sys.dont_write_bytecode = True
K, GRAPH = Path(sys.argv[1]), Path(sys.argv[2])
BASE = Path("/tmp/claude-0/repair4/reg")
W = BASE / "a4W"
ENV = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "TMPDIR": "/tmp/claude-0/repair4/tmp"}
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
    spec = importlib.util.spec_from_file_location("vstamp_a4", FVD / "scripts/validate_gcfpe_20260914.py")
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
GRAPH_MD = Path(sys.argv[3])
fresh(); tree_stamp()
v0, c0 = suite(); v1, c1 = suite(True)
rec("clean", v0 == v1 == "FLOWMASTER_SUITE_PASS" and c0 == c1 == [], (v0, c0, v1, c1))

INSIDE = "stay subscribed and do not poll."
fresh()
# no added space: with the comment stripped, the passage reads exactly as pinned
move("change-flow/SKILL.md", lambda t: t.replace(INSIDE, INSIDE + "<!-- The fallback block stays usable after MERGE_OBSERVED. -->", 1))
dispatch_check("P1", ["change-flow/SKILL.md"])
fresh()
def p2(t):
    i = t.index("At `MERGE_PENDING`, return control with the result")
    j = t.rfind("\n", 0, i) + 1
    return t[:j] + "<!--\n" + t[j:]
move("glow-hde-pr-development/SKILL.md", p2)
dispatch_check("P2", ["glow-hde-pr-development/SKILL.md"])
fresh()
move("session-relay-flowmaster/SKILL.md", lambda t: t + "\n<!-- note --!>\n")
dispatch_check("P3", ["session-relay-flowmaster/SKILL.md"])
fresh()
move("glow-hde-pr-development/references/behavior-cases.md", lambda t: t.replace(ONCE, ONCE + "<!-- except when Nathan pastes both -->", 1))
dispatch_check("P4", ["references/behavior-cases.md"])

fresh(); MAP_OLD = sha(MAP.read_bytes()); mp = json.loads(MAP.read_bytes())
MAP.write_bytes(ser(dict(reversed(list(mp.items()))))); restamp_map_only()
check("M1", ["FMV-GCF-MAP-005"])

FAKE = json.dumps({"id": "GCF-17", "session": "PR-35 may run as a subagent of PR-30"}, indent=2)
for mid, extra in (("M2", "\n\n" + "\n".join("    " + l for l in FAKE.split("\n")) + "\n"),
                   ("M3", "\n<xmp>\n" + FAKE + "\n</xmp>\n"),
                   ("M4", "\n<textarea>\n" + FAKE + "\n</textarea>\n"),
                   ("M5", "\n<listing>\n" + FAKE + "\n</listing>\n")):
    fresh(); m = MATRIX.read_text(encoding="utf-8"); MATRIX.write_text(m + extra, encoding="utf-8")
    restamp(matrix_changed=True); check(mid, ["FMV-ORACLE-022"])

SYNCED = "/root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502"
r = subprocess.run([sys.executable, str(Path(__file__).resolve().parent / "contract_recipe.py"), str(GRAPH_MD),
                    SYNCED + "/change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json",
                    str(K / "flowmaster-validate/references/glow-hde-canonical-change-flow-r1-20260923.json"),
                    str(BASE / "recipe-contract.json"), "--check",
                    str(K / "flowmaster-validate/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json"),
                    str(K / "change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json")],
                   capture_output=True, text=True, env=ENV)
rec("K3", r.returncode == 0 and r.stdout.count("EQUAL    ") == 2, r.stdout.strip().split("\n")[-4:])
shutil.rmtree(W, ignore_errors=True)
print(f"A4_REPAIR_REGRESSIONS {sum(ok for _, ok in RES)} of {len(RES)} exact")
