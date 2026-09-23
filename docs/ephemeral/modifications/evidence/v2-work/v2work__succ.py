import json, hashlib, copy, sys
SK = "/root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502"
ser = lambda o: (json.dumps(o, indent=2, sort_keys=False, ensure_ascii=False) + "\n").encode("utf-8")
hb = open(SK + "/flowmaster-validate/references/glow-hde-canonical-change-flow-r1.json", "rb").read()
assert hashlib.sha256(hb).hexdigest().startswith("52807e58")
H = json.loads(hb); assert ser(H) == hb
mb = open(SK + "/change-flow/references/glow-hde-canonical-change-flow-r1-runtime-map.json", "rb").read()
assert ser({k: H[k] for k in ("profile_id", "authority", "coverage", "runtime_rows")}) == mb
CF = ("id","partition","name","change_class","actor","session","consumes","produces","next","approval_contract","failure_stop_condition")
dig = lambda r: hashlib.sha256(json.dumps({k: r[k] for k in CF}, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()).hexdigest()
S = copy.deepcopy(H)
S["profile_id"] = "GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260923_1"
t = S["required_global_tokens"]; t[t.index("GLOW_HDE_CANONICAL_CHANGE_FLOW_R1_20260831_1")] = S["profile_id"]
R = {r["id"]: r for r in S["runtime_rows"]}
hist = {r["id"]: r for r in H["runtime_rows"]}
r = R["GCF-17"]
r["name"] = "Dedicated PR session implements and creates PR lineage; PR-35 continues it in its own session"
r["actor"] = "Dedicated PR session (PR-30 phase) and dedicated PR-35 session (PR-35 phase)"
r["session"] = "PR-30: exactly the GCF-14 planning session, continuing for implementation of its one authorized work unit. PR-35: its own dedicated top-level session for the same work unit and pull request, entered from PR-30's handoff; never a subagent of another session."
old = r["failure_stop_condition"]; print("GCF-17 old fsc:", old)
r["failure_stop_condition"] = "STOP_SESSION_MISMATCH, STOP_SCOPE_CHANGE, STOP_REMOTE_INTEGRITY_DRIFT, or STOP_VALIDATION_FAILURE; recovery owner: the phase's own PR session/IA rescope."
r = R["GCF-17.LINEAGE"]; print("LIN old next/fsc:", r["next"], r["failure_stop_condition"])
r["next"] = ["GCF-14", "GCF-19", "GCF-20"]
r["failure_stop_condition"] = "STOP_LINEAGE_INCOMPLETE, STOP_UNATTRIBUTABLE_CHANGE, or STOP_WORK_UNIT_NOT_TO_SPEC; recovery owner: a new top-level PR session Nathan creates for a re-plan (GCF-14), the reviewer, or IA."
r = R["GCF-14"]; print("14 old consumes:", r["consumes"]); r["consumes"] = r["consumes"] + ["pr_work_unit_lineage_review"]
order = [x["id"] for x in S["runtime_rows"] if x["id"] in ("GCF-14", "GCF-17", "GCF-17.LINEAGE")]
print("oracle order", order)
blocks = []
for i in order:
    R[i]["source_row_sha256"] = dig(R[i]); print(i, R[i]["source_row_sha256"])
    b = {k: R[i][k] for k in CF}; b["supersedes_source_row_sha256"] = hist[i]["source_row_sha256"]
    assert list(R[i].keys())[:11] == list(CF)
    blocks.append((b, R[i]["source_row_sha256"]))
open("blocks.txt", "w").write("".join("```json\n" + json.dumps(b, indent=2, ensure_ascii=False) + "\n```\nsource_row_sha256: " + d + "\n\n" for b, d in blocks))
S["authority"]["successor_source_matrix_sha256"] = "0" * 64
S["authority"]["successor_rows"] = order
S["authority"]["successor_authority"] = "D23-D, D23-F; Product Owner 2026-09-23"
ob = ser(S); mp = ser({k: S[k] for k in ("profile_id", "authority", "coverage", "runtime_rows")})
print("oracle bytes", len(ob), "map bytes", len(mp), "rows", len(S["runtime_rows"]))
print(json.dumps(S["authority"], indent=2))
