"""§9 item 9 for §5.7: regressions G1-G15 on scratch copies of the edited tree.
Each "re-stamped" regression re-serialises the successor oracle, re-derives the successor map, and moves every
pin that reads them (validate_flowmaster.py constants, validate_gcfpe_current.py installed-map constant,
authority.successor_source_matrix_sha256 when the matrix changes, validate_gcfpe_20260914.py R1 literals, the
profile's :35/:37, SKILL_TREE_SHA256), so that only the new check can catch the mutation.
Pass = findings(mutated) - findings(clean) == the expected set (rule ids, with subjects where the spec names a row).
usage: PYTHONDONTWRITEBYTECODE=1 python3 regress_oracle.py <edited-skills-root> <candidate-root-graph-json>"""
import copy, hashlib, json, os, re, shutil, subprocess, sys
from pathlib import Path
sys.dont_write_bytecode = True
K, GRAPH = Path(sys.argv[1]), Path(sys.argv[2])
W = Path("/tmp/claude-0/e2/reg/oracleW"); CR = Path("/tmp/claude-0/e2/reg/oracleCR")
ENV = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "TMPDIR": "/tmp/claude-0/e2/tmp"}
FVD, CFD = W / "flowmaster-validate", W / "change-flow"
ORACLE = FVD / "references/glow-hde-canonical-change-flow-r1-20260923.json"
MAP = CFD / "references/glow-hde-canonical-change-flow-r1-runtime-map-20260923.json"
MATRIX = FVD / "references/r1-successor-source-20260923.md"
HIST = FVD / "references/glow-hde-canonical-change-flow-r1.json"
HMAP = CFD / "references/glow-hde-canonical-change-flow-r1-runtime-map.json"
sha = lambda b: hashlib.sha256(b).hexdigest()
ser = lambda o: (json.dumps(o, indent=2, sort_keys=False, ensure_ascii=False) + "\n").encode("utf-8")
CF = ("id", "partition", "name", "change_class", "actor", "session", "consumes", "produces", "next", "approval_contract", "failure_stop_condition")
dig = lambda r: sha(json.dumps({k: r[k] for k in CF}, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())
CR.mkdir(parents=True, exist_ok=True); (CR / "graph").mkdir(exist_ok=True)
shutil.copyfile(GRAPH, CR / "graph/GCFPE-20260914.1-Candidate-Graph-Contract.json")


def fresh():
    shutil.rmtree(W, ignore_errors=True); shutil.copytree(K, W)
    (W / "candidate-root/graph").mkdir(parents=True)
    shutil.copyfile(GRAPH, W / "candidate-root/graph/GCFPE-20260914.1-Candidate-Graph-Contract.json")


def sub_all(path, old, new):
    s = path.read_text(encoding="utf-8")
    if old != new:
        s = s.replace(old, new)
    path.write_text(s, encoding="utf-8")


def restamp(oracle=None, matrix_changed=False):
    """Write the oracle and map, then move every pin downstream of them, in §5.11 order: graph
    protected_identities (both copies and the candidate root), contract (both copies), profile, literals,
    SKILL_TREE_SHA256. Under §12 S-5 the default suite runs the v4 validator, so the graph and contract
    pins must move too, or a re-stamped mutation would also fire PROTECTED_IDENTITIES."""
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
    (W / "candidate-root/graph").mkdir(parents=True, exist_ok=True)
    (W / "candidate-root/graph/GCFPE-20260914.1-Candidate-Graph-Contract.json").write_bytes(ngb)
    pairs = [(old_o, new_o), (old_m, new_m), (sha(gb), sha(ngb)), (sha(cb), sha(ncb))]
    for p in (FVD / "scripts/validate_flowmaster.py", FVD / "scripts/validate_gcfpe_current.py",
              FVD / "scripts/validate_gcfpe_20260914.py", CFD / "scripts/validate_gcfpe_20260914.py",
              FVD / "references/gcfpe-20260914.1-091426.1-validation-profile.json"):
        for a, b in pairs:
            sub_all(p, a, b)
    assert len(gb) == len(ngb) and len(cb) == len(ncb)
    tree_stamp()


def tree_stamp():
    import importlib.util
    spec = importlib.util.spec_from_file_location("vstamp", FVD / "scripts/validate_gcfpe_20260914.py")
    sys.path.insert(0, str(FVD / "scripts")); v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v); sys.path.pop(0)
    p = FVD / "SKILL.md"
    p.write_text(re.sub(r"(?m)^SKILL_TREE_SHA256: [0-9a-f]{64}$", "SKILL_TREE_SHA256: " + v.skill_tree_digest(FVD), p.read_text(encoding="utf-8")), encoding="utf-8")


def suite(candidate=False):
    cmd = [sys.executable, str(FVD / "scripts/validate_flowmaster.py"), "--skills-root", str(W)]
    if candidate:
        cmd += ["--strict-warnings", "--gcfpe-contract", str(CFD / "references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json"), "--gcfpe-candidate-root", str(W / "candidate-root")]
    r = subprocess.run(cmd, capture_output=True, text=True, env=ENV)
    d = json.loads(r.stdout)
    return d["verdict"], sorted((f["rule_id"], f["evidence"][:150]) for f in d["findings"])


RES = []
fresh(); tree_stamp(); v0, clean = suite(); vc0, cleanc = suite(True)
print("clean default:", v0, clean, "| clean candidate:", vc0, cleanc)
assert clean == [] and cleanc == []


def check(gid, got, expected_ids, row=None, exact_evidence=None):
    ids = sorted(g[0] for g in got)
    ok = ids == sorted(expected_ids) and (row is None or all(f"row={row};" in g[1] for g in got)) \
        and (exact_evidence is None or [g[1] for g in got] == [exact_evidence])
    RES.append((gid, ok)); print(("OK   " if ok else "BAD  ") + gid, got)


def edit_row(o, rid, fn):
    r = next(x for x in o["runtime_rows"] if x["id"] == rid); fn(r); return r


# G1: edit GCF-16 session, digest by formula, re-stamp -> N9 on GCF-16 only.
fresh(); o = json.loads(ORACLE.read_bytes()); r = edit_row(o, "GCF-16", lambda r: r.__setitem__("session", r["session"] + " (edited)")); r["source_row_sha256"] = dig(r)
restamp(o); check("G1", suite()[1], ["FMV-ORACLE-015"], row="GCF-16")
# G2: edit GCF-17 session in the oracle only -> N6 on GCF-17 only.
fresh(); o = json.loads(ORACLE.read_bytes()); r = edit_row(o, "GCF-17", lambda r: r.__setitem__("session", r["session"] + " (edited)")); r["source_row_sha256"] = dig(r)
restamp(o); check("G2", suite()[1], ["FMV-ORACLE-012"], row="GCF-17")
# G3: GCF-14 source_row_sha256 -> another 64-hex -> N7 on GCF-14 only.
fresh(); o = json.loads(ORACLE.read_bytes()); edit_row(o, "GCF-14", lambda r: r.__setitem__("source_row_sha256", "0" * 64))
restamp(o); check("G3", suite()[1], ["FMV-ORACLE-013"], row="GCF-14")
# G4: flip one byte in the matrix prose (outside blocks and digest lines) -> N3 only. (Not re-stamped.)
fresh(); b = bytearray(MATRIX.read_bytes()); i = b.index(b"One block per changed row"); b[i] ^= 0x01; MATRIX.write_bytes(bytes(b)); tree_stamp()
check("G4", suite()[1], ["FMV-ORACLE-009"])
# G5: flip one byte of the historical oracle inside generated_for_run -> N1 only.
fresh(); b = bytearray(HIST.read_bytes()); j = b.index(b'"generated_for_run"'); k = b.index(b'"', b.index(b":", j) + 2) + 1; b[k] ^= 0x01; HIST.write_bytes(bytes(b)); tree_stamp()
check("G5", suite()[1], ["FMV-ORACLE-008"])
# G6: flip one byte of the historical runtime map -> N2 only.
fresh(); b = bytearray(HMAP.read_bytes()); i = b.index(b"TRUTH_LOCK"); b[i] ^= 0x01; HMAP.write_bytes(bytes(b))
check("G6", suite()[1], ["FMV-GCF-MAP-007"])
# G7: add GCF-16 to authority.successor_rows, re-stamp -> N4 only.
fresh(); o = json.loads(ORACLE.read_bytes()); o["authority"]["successor_rows"].insert(1, "GCF-16")
restamp(o); check("G7", suite()[1], ["FMV-ORACLE-010"])
# G8: alter one block's supersedes digest, write the matrix digest into authority, re-stamp -> N8 only.
fresh(); m = MATRIX.read_text(encoding="utf-8"); tgt = '"supersedes_source_row_sha256": "4f033c4b'
assert m.count(tgt) == 1; MATRIX.write_text(m.replace(tgt, '"supersedes_source_row_sha256": "4f033c4c'), encoding="utf-8")
restamp(matrix_changed=True); check("G8", suite()[1], ["FMV-ORACLE-014"], row="GCF-14")
# G9: the §5.10 fixture against the historical oracle -> FMV-GCF-EDGE-003 only; against the successor -> [].
sys.path.insert(0, str(K / "flowmaster-validate/scripts"))
import validate_flowmaster as VF  # noqa: E402
fx = next(s for s in json.loads((K / "flowmaster-validate/fixtures/change-flow/scenarios.json").read_bytes())["scenarios"] if s["id"] == "GCF-LINEAGE-REPLAN-01")
hist_ids = [x["rule_id"] for x in VF.validate_fixture_payload(fx, json.loads((K / "flowmaster-validate/references/glow-hde-canonical-change-flow-r1.json").read_bytes()))]
succ_ids = [x["rule_id"] for x in VF.validate_fixture_payload(fx, json.loads((K / "flowmaster-validate/references/glow-hde-canonical-change-flow-r1-20260923.json").read_bytes()))]
ok = hist_ids == ["FMV-GCF-EDGE-003"] and succ_ids == []
RES.append(("G9", ok)); print(("OK   " if ok else "BAD  ") + "G9", "historical:", hist_ids, "successor:", succ_ids)
sys.path.pop(0)
# G10: a scratch contract with r1_oracle_changed false, every other pin re-stamped -> PROTECTED_IDENTITIES.
fresh()
c = json.loads((CFD / "references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json").read_bytes())
c["protected_identities"]["r1_oracle_changed"] = False
cb = (json.dumps(c, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")
old_c = sha((CFD / "references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json").read_bytes()); old_n = len((CFD / "references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json").read_bytes())
for p in (CFD, FVD):
    (p / "references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json").write_bytes(cb)
fvp = FVD / "scripts/validate_gcfpe_20260914.py"; sub_all(fvp, old_c, sha(cb)); sub_all(fvp, f"EXPECTED_CANDIDATE_CONTRACT_BYTES = {old_n}", f"EXPECTED_CANDIDATE_CONTRACT_BYTES = {len(cb)}")
prof = FVD / "references/gcfpe-20260914.1-091426.1-validation-profile.json"; sub_all(prof, old_c, sha(cb)); sub_all(prof, f'"byte_count": {old_n}', f'"byte_count": {len(cb)}')
tree_stamp()
r = subprocess.run([sys.executable, str(fvp), str(CFD), "--contract", str(CFD / "references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json")], capture_output=True, text=True, env=ENV)
errs = json.loads(r.stdout)["errors"]
ok = errs == ["PROTECTED_IDENTITIES"]; RES.append(("G10", ok)); print(("OK   " if ok else "BAD  ") + "G10", errs)
# G11: leave the profile's r1_oracle_sha256 at 52807e58 -> the two candidate wrapper findings.
fresh(); prof = FVD / "references/gcfpe-20260914.1-091426.1-validation-profile.json"
sub_all(prof, sha(ORACLE.read_bytes()), "52807e58c4a4659e6c1fc822749f6e50253ad7b01846c833f727ee266ca71d5e"); tree_stamp()
v, got = suite(True); check("G11", got, ["FMV-GCF-CANDIDATE-CONTRACT-001", "FMV-GCF-CANDIDATE-FIXTURE-PROFILE-001"])
print("      G11 evidence:", [g[1][:120] for g in got])
# G12: link the historical map in change-flow/SKILL.md -> the unapproved reference-file dependency.
fresh(); p = CFD / "SKILL.md"; s = p.read_text(encoding="utf-8")
s = s.replace("<!-- FLOWMASTER_SPECIALIZATION_END -->", "See the [historical map](references/glow-hde-canonical-change-flow-r1-runtime-map.json).\n\n<!-- FLOWMASTER_SPECIALIZATION_END -->", 1)
p.write_text(s, encoding="utf-8")
check("G12", suite()[1], ["FMV-SKILL-STRUCTURE-001"], exact_evidence="unapproved reference-file dependency: references/glow-hde-canonical-change-flow-r1-runtime-map.json")
# G13: delete the matrix -> only the structure finding (N3 and N5 skip).
fresh(); MATRIX.unlink(); tree_stamp()
check("G13", suite()[1], ["FMV-SKILL-STRUCTURE-001"], exact_evidence="missing bundled script: references/r1-successor-source-20260923.md")
# G14: change authority.r1_verdict in the successor oracle, re-stamp -> N10 only.
fresh(); o = json.loads(ORACLE.read_bytes()); o["authority"]["r1_verdict"] = "R1_CANONICAL_TRUTH_LOCK_FAIL"
restamp(o); check("G14", suite()[1], ["FMV-ORACLE-016"])
# G15: candidate suite; leave validate_gcfpe_20260914.py:1964 at 52807e58, every other pin re-stamped. Measured set.
fresh()
fvp = FVD / "scripts/validate_gcfpe_20260914.py"; lines = fvp.read_text(encoding="utf-8").split("\n")
succ = sha(ORACLE.read_bytes())
idx = [i for i, l in enumerate(lines) if f'"r1_oracle_sha256": "{succ}",' in l]
line1964 = max(idx)  # PROTECTED_IDENTITIES is the last of the three literals
lines[line1964] = lines[line1964].replace(succ, "52807e58c4a4659e6c1fc822749f6e50253ad7b01846c833f727ee266ca71d5e")
fvp.write_text("\n".join(lines), encoding="utf-8"); tree_stamp()
vd, gd = suite(); vc, gc = suite(True)
ids = sorted(set(g[0] for g in gd) | set(g[0] for g in gc))
ok = "FMV-ORACLE-017" in [g[0] for g in gd] and "FMV-ORACLE-017" in [g[0] for g in gc]
RES.append(("G15", ok)); print(("OK   " if ok else "BAD  ") + "G15", f"(line {line1964 + 1}) default ids:", sorted(set(g[0] for g in gd)), "| candidate ids:", ids)
print("      G15 default:", gd)
print("      G15 candidate:", gc)
shutil.rmtree(W, ignore_errors=True)
print(f"ORACLE_REGRESSIONS {sum(ok for _, ok in RES)} of {len(RES)} exact")
