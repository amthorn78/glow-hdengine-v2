import json, os, shutil, subprocess, sys, hashlib
sys.dont_write_bytecode = True
SK = "/root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502"
GP = SK + "/glow-graph-contract/scripts/graph_parts.py"
W = "/tmp/claude-0/v2work"
sys.path.insert(0, W + "/routesim/fvscripts")
import validate_gcfpe_20260914 as V
src = W + "/routesim/parts_new"; dst = W + "/parts_final"
shutil.rmtree(dst, ignore_errors=True); shutil.copytree(src, dst)
def ld(f): return json.load(open(dst + "/" + f, encoding="utf-8"))
def sv(f, o): open(dst + "/" + f, "w", encoding="utf-8").write(json.dumps(o, indent=2, sort_keys=True, ensure_ascii=False) + "\n")
g = ld("global.json")
hc = g["handoff_contract"]
hc["required"] = ["exact selected prompt full name/version/direct Notion URL", "receiving role and exact session",
  "input artifact repository paths with one-line labels", "pull request reference when the receiver continues an existing PR",
  "minimum exceptional context only for a condition the artifacts do not record"]
hc["prohibited"] += ["branch", "commit", "restated artifact content"]
pc = g["pr_continuity_contract"]
pc["shared_exactly_one"].remove("dedicated PR-development session")
pc["adds"]["session"] = 1; pc["adds"]["cross_session_route"] = 1
pm = g["post_merge_three_event_contract"]
pm["event_2"] = {"actor": "Nathan / Product Owner", "fact": "product_owner_manual_merge_observed_or_asserted",
  "time": "observed by the subscribed PR-35 session; asserted at the later PR-40 invocation only where no MERGE_OBSERVED result was returned for this merge", "value": True}
pm["observed_merge_edges"] = [{"from": f, "to": "PR-40", "branch_id": "merge_observed", "state": "MERGE_OBSERVED", "automatic": False, "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"} for f in ("PR-35", "RS-40")]
sv("global.json", g)
p = ld("prompts/PR-35.json"); n = p["node"]
n["session_class"] = "DEDICATED_PR_REVIEW_SESSION"
n["receiving_role"] = "You are the dedicated PR-35 session for one work unit, entered from PR-30's handoff; you continue its existing pull request. PR-35 runs as its own top-level session, entered from PR-30's handoff that Nathan pastes, and never as a subagent, forked agent or workflow agent of PR-30 or of any other session."
n["adds_session"] = True; n["cross_session_route"] = True
nf = n["native_function"]; assert nf.endswith("without merging.")
n["native_function"] = nf[:-1] + "; return MERGE_OBSERVED when an active subscription observes Nathan's merge."
sv("prompts/PR-35.json", p)
r = ld("prompts/RS-40.json")
r["node"]["receiving_role"] = "You resume the recorded phase in its own dedicated session: PR-30's session for a PR-30 phase, the PR-35 session for PR_RETURN_PHASE PR-35."
sv("prompts/RS-40.json", r)
out = W + "/graph_final.md"
res = subprocess.run([sys.executable, GP, "build", dst, out], capture_output=True, text=True, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
print(res.returncode, res.stdout.strip().replace("\n", " | "), res.stderr.strip())
raw = open(out, encoding="utf-8").read().split("\n")
s = next(i for i, l in enumerate(raw) if l.strip() == "```json"); e = len(raw) - 1
while raw[e].strip() != "```": e -= 1
block = ("\n".join(raw[s + 1:e]) + "\n").encode()
G = json.loads(block)
print("edges", len(G["edges"]), "bytes", len(block), hashlib.sha256(block).hexdigest())
print(V.routing_surface({"route_edges": G["edges"], "state_routes": G["state_routes"]}))
for f in ["global.json"] + ["prompts/%s.json" % k for k in ("DOC-10","PR-10","PR-20","PR-30","PR-35","PR-40","RS-40")]:
    b = open(dst + "/" + f, "rb").read(); print(f, hashlib.sha256(b).hexdigest(), len(b))
print(json.dumps(pm["observed_merge_edges"], indent=2, sort_keys=True))
print(n["native_function"])
