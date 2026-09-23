#!/usr/bin/env python3
"""E1 registry edit (execution spec v2, §7 with §12 and its v2 addendum applied).

Adapted from v2-work/v2work67__apply_v2.py (with its guards_v2, semdiff_v2 and drift_v2 checks).
Line-anchored: every op names its row and an exact anchor line, which must occur exactly once in
the row's range (or first after a named sub-anchor), or the script stops. No YAML is re-dumped.

Differences from the prototype, each required by the spec:
  * G25B (addendum, §6 and §7): required 'PR-40 is entered on the observed merge event', CTR-002,
    on PR-40 only. G25 stays on PR-35 and RS-40.
  * PR-40 :3705 (addendum): the PR-30-result input is kept, and only its PR-35 clause is replaced
    by W-4's PR-35-result input, as its own line alongside it.
  * N1 (§7.8; S-2; addendum U-4): new key body_identity_disposition under body_extraction_convention.

Usage: PYTHONDONTWRITEBYTECODE=1 python3 e1_registry_apply.py <scratch-dir> [--write]
Without --write it applies to a scratch copy only. The input must be the HEAD registry bytes."""
import copy, hashlib, json, os, shutil, subprocess, sys
from collections import Counter

sys.dont_write_bytecode = True
REPO = "/home/user/glow-hdengine-v2"
REG = REPO + "/docs/prompt_ecosystem_management/project-prompt-contract-registry.md"
REL = "docs/prompt_ecosystem_management/project-prompt-contract-registry.md"
PARTS = REPO + "/docs/graph/parts"
SK = "/root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502"
W = os.path.abspath(sys.argv[1])
WRITE = "--write" in sys.argv[2:]
shutil.rmtree(W, ignore_errors=True)
os.makedirs(W)
shutil.copytree(SK + "/amthor-workspace-governance-audit/scripts", W + "/wga/scripts")
sys.path.insert(0, W + "/wga/scripts")
from audit_workspace_governance import load_data  # noqa: E402
import yaml  # noqa: E402

BASE_SHA = "c5ae188834d5154826b1bc723a89712cebe4631bee296c56ec856b3947e1d1f7"

# ---- guards (§7.3, §12 applied; G25B from the addendum) -------------------------------------
PID = (r"(?:(?:PR|QA|RS|IA|OPS|DOC|CL|CL-C|CL-E|CF-C|CF-E|CF-PO|ESC|MGR|UTIL)-\d+|this prompt|"
       r"the next prompt|the destination prompt|a main-ecosystem prompt)")
HDR = r"\A(?:[ \t]*\n)*(?:[^\n]*\n(?:[ \t]*\n)*){0,7}[ \t>*_|`#-]*(?:\d+\.[ \t]+)?(?:\*\*|__)?"
HDR_END = r"(?:\*\*|__|`)?[ \t]*:"
STEP5 = ["CF-C-10", "CF-C-20", "CF-C-30", "CF-C-40", "CF-E-10", "CF-E-20", "CF-E-30", "CF-E-40", "CF-PO-10", "MGR-10"]
LAT10 = ["PR-10", "PR-20", "PR-30", "PR-35", "PR-40", "RS-10", "RS-20", "DOC-10", "DOC-20", "IA-30"]
ASK4 = ["QA-60", "QA-80", "RS-10", "RS-30"]
GUARDS = [
 ("G01", "forbidden_regex", "CONTROL_NOTION", "CTR-001", "ALL55"),
 ("G02", "forbidden_regex", r"(?i)operational state[^.\n]{0,80}\b(?:remains?|lives?|stays?)\b[^.\n]{0,40}\bNotion\b", "CTR-001", "ALL55"),
 ("G03", "forbidden_regex", "Notion and repository persistence", "CTR-001", ["QA-10"]),
 ("G04", "forbidden_regex", "Notion-resident artifact", "CTR-001", STEP5),
 ("G05", "required_regex", r"never\s+carries\s+the\s+only\s+copy", "CTR-002", "NPH53"),
 ("G06", "forbidden_regex", r"NEXT_PROMPT_HANDOFF(?:[^\n]|\n(?![ \t]*\n)){0,1500}?(?<!\bno )(?:(?<![/\w-])worktree\b|\bworking branch\b|\bbranch name\b|\bgit branch\b|\bhead (?:commit|SHA)\b|\bcommit (?:SHA|hash|identity|id)\b|\bremote head\b)", "TOP-001", "NPH53"),
 ("G07", "required_regex", r"The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\.", "TOP-001", "NPH53"),
 ("G08", "forbidden_regex", r"\bends? `ASK OK\?`", "CTR-002", ASK4),
 ("G08A", "required_regex", r"`ASK OK\?` is the line immediately before the block\.", "TOP-001", ASK4),
 ("G09", "required_regex", r"An\s+\*?In-flight decisions\*?\s+section", "CTR-002", ["PR-30", "PR-35", "RS-40"]),
 ("G10", "required_regex", "Decide it during work", "CTR-002", LAT10),
 ("G11", "required_regex", r"\*{0,2}Material\*{0,2} means a change to the Epic-level commitment", "CTR-002", LAT10),
 ("G12", "forbidden_regex", HDR + r"Prompt [Vv]ersion" + HDR_END, "SRC-001", "ALL55"),
 ("G13", "forbidden_regex", HDR + r"Ecosystem release" + HDR_END, "INV-003", "ALL55"),
 ("G14", "forbidden_regex", HDR + r"Set" + HDR_END, "SRC-001", "ALL55"),
 ("G15", "forbidden_regex", r"Proceed[;,]\s+(?:the\s+)?(?:same\s+)?dedicated PR-development session", "CTR-001", "MAIN54"),
 ("G16", "required_regex", "they do not share a session", "CTR-002", ["PR-30", "PR-35", "RS-40"]),
 ("G17", "required_regex", r"never\s+as\s+a\s+subagent,\s+forked\s+agent\s+or\s+workflow\s+agent\s+of\s+PR-30", "CTR-002", ["PR-30", "PR-35", "RS-40"]),
 ("G18", "required_regex", r"never\s+as\s+a\s+subagent\s+of\s+another\s+session", "CTR-002", "MAIN54"),
 ("G19", "forbidden_regex", r"(?i)(?<!never )(?<!not )(?<!n't )\b(?:run|execute|invoke|dispatch|start|launch|spawn|hand)(?:s|es|ed|ing)?\s+(?:the\s+)?" + PID + r"(?!['’]s\b)\b[^.\n]{0,40}?\b(?:as|in|to|via)\s+an?\s+(?:sub-?agent|forked agent|workflow agent)\b", "CTR-001", "MAIN54"),
 ("G20", "forbidden_regex", r"(?i)(?<!never )(?<!not )(?<!no )(?<!n't )(?<!Nathan )\b(?:launch|spawn|auto-?start|open|create|start|schedule)(?:s|es|ed|ing)?\s+(?:a\s+|the\s+)?(?:new\s+)?(?:[\w-]+\s+)?session\s+(?:for|to\s+run|running)\s+(?:the\s+)?" + PID, "CTR-001", "MAIN54"),
 ("G21", "forbidden_regex", r"(?:create_session|create_trigger|fire_trigger|spawn[-_]session)\b", "CTR-001", "MAIN54"),
 ("G22", "forbidden_regex", "launched as a new session", "CTR-001", ["PR-35", "RS-40"]),
 ("G23", "required_regex", r"[Ss]ubscribe to the pull request", "CTR-002", ["PR-35", "RS-40"]),
 ("G24", "required_regex", "stay subscribed and do not poll", "CTR-002", ["PR-35", "RS-40"]),
 ("G25", "required_regex", "The observed merge event is the fact PR-40 is entered on", "CTR-002", ["PR-35", "RS-40"]),
 ("G25B", "required_regex", "PR-40 is entered on the observed merge event", "CTR-002", ["PR-40"]),
 ("G26", "forbidden_regex", "original Proceed and a suitable actual authorized implementation vehicle", "CTR-001", ["PR-40"]),
 ("G27", "required_regex", r"accepts\s+a\s+`?PR_WORK_UNIT_LINEAGE_REVIEW`?\s+whose\s+result\s+is\s+`?REJECT", "CTR-002", ["PR-20"]),
]
# ---- texts (§3.4, §12 W-1, W-2, W-4, PR-20 input; addendum U-4) ------------------------------
PR35_ROLE = ("You are the dedicated PR-35 session for one work unit, entered from PR-30's handoff; you continue its "
             "existing pull request. PR-35 runs as its own top-level session, entered from PR-30's handoff that Nathan "
             "pastes, and never as a subagent, forked agent or workflow agent of PR-30 or of any other session.")
RS40_ROLE = ("You resume the recorded phase in its own dedicated session: PR-30's session for a PR-30 phase, "
             "the PR-35 session for PR_RETURN_PHASE PR-35.")
RS40_CREATOR = "the recorded phase's own dedicated session for the exact suspended work unit."
PR40_ENTRY = ("PR-40 is entered on the observed merge event for the identified PR, delivered to the subscribed PR-35 "
              "session as MERGE_OBSERVED, or, only where no MERGE_OBSERVED result was returned for this merge, on "
              "Nathan's assertion that he manually merged it.")
PR35_RESULT_INPUT = ("The complete PR-35 result: MERGE_OBSERVED with the observed merge event, or, only where no "
                     "MERGE_OBSERVED result was returned for this merge, the earlier MERGE_PENDING, which is historical "
                     "pre-merge evidence.")
PR20_INPUT = ("PR_WORK_UNIT_LINEAGE_REVIEW with REJECT (reject_replan) and its in-scope finding, for a re-plan of the "
              "same WORK_UNIT_ID in a new dedicated session Nathan seeds")
N1_TEXT = ("The `evidence_contract` and `source_snapshot` identities on every row describe the bodies before `D23` "
           "(2026-09-23) and no longer identify them. They are not regenerated, because hashing bodies is prohibited "
           "(`prompt-corpus-policy.md`).")
N1_LINES = ["  body_identity_disposition: 'The `evidence_contract` and `source_snapshot` identities on every row",
            "    describe the bodies before `D23` (2026-09-23) and no longer identify them. They are not",
            "    regenerated, because hashing bodies is prohibited (`prompt-corpus-policy.md`).'"]


def q(s):
    return "'" + s.replace("'", "''") + "'"


def qn(s):
    try:
        if yaml.safe_load("k: " + s) == {"k": s}:
            return s
    except Exception:
        pass
    return q(s)


def entry(value, rid, indent="    "):
    return [f"{indent}- value: {q(value)}", f"{indent}  rule_id: {rid}"]


class Reg:
    def __init__(self, text):
        self.lines = text.split("\n")

    def row_range(self, key):
        s = [i for i, l in enumerate(self.lines) if l == f"- prompt_key: {key}"]
        assert len(s) == 1, (key, s)
        s = s[0]
        e = next(i for i in range(s + 1, len(self.lines)) if self.lines[i].startswith("- prompt_key: ") or
                 self.lines[i] == "global_literals:")
        return s, e

    def find(self, key, anchor, after=None):
        s, e = self.row_range(key)
        if after is not None:
            s = self.find(key, after)
        hits = [i for i in range(s, e) if self.lines[i] == anchor]
        assert len(hits) >= 1, (key, anchor)
        if after is None:
            assert len(hits) == 1, (key, anchor, hits)
        return hits[0]

    def replace(self, key, anchor, new, after=None):
        i = self.find(key, anchor, after)
        self.lines[i:i + 1] = new if isinstance(new, list) else [new]

    def insert_after(self, key, anchor, new, after=None):
        i = self.find(key, anchor, after)
        self.lines[i + 1:i + 1] = new

    def delete_pair(self, key, l1, l2):
        i = self.find(key, l1)
        assert self.lines[i + 1] == l2, (key, self.lines[i + 1])
        del self.lines[i:i + 2]

    def list_end(self, key, header):
        i = self.find(key, header)
        ind = len(header) - len(header.lstrip())
        j = i + 1
        while j < len(self.lines):
            l = self.lines[j]
            lead = len(l) - len(l.lstrip())
            if l.strip() == "" or lead < ind or (lead == ind and not l.lstrip().startswith("- ")):
                break
            j += 1
        return j

    def append_list(self, key, header, new):
        j = self.list_end(key, header)
        self.lines[j:j] = new

    def text(self):
        return "\n".join(self.lines)


def select(rows, sel):
    keys = [r["prompt_key"] for r in rows]
    if sel == "ALL55":
        return keys
    if sel == "MAIN54":
        return [k for k in keys if k != "GCFPE-MGMT-10"]
    if sel == "NPH53":
        return [r["prompt_key"] for r in rows if any(
            (x.get("value") if isinstance(x, dict) else x) == "NEXT_PROMPT_HANDOFF"
            for x in r["audit_assertions"].get("required_literals") or [])]
    return list(sel)


def apply(src_text, old):
    R = Reg(src_text)
    # 7.2: step 43, first half
    for r in old["prompts"]:
        k = r["prompt_key"]
        R.delete_pair(k, "    - value: 'Prompt [Vv]ersion: `?091426\\.1`?'", "      rule_id: SRC-001")
        R.delete_pair(k, "    - value: 'Ecosystem release: `?GCFPE-20260914\\.1`?'", "      rule_id: INV-003")
    # 7.3: guards, appended to the end of each row's list, in guard order
    for gid, kind, value, rid, sel in GUARDS:
        for k in select(old["prompts"], sel):
            R.append_list(k, f"    {kind}:", entry(value, rid))
    # 7.5: D13-derived fields
    R.replace("PR-35", "    - RS-20", ["    - PR-40", "    - RS-20"], after="    consumers:")
    R.replace("PR-35", "  - RS-20", ["  - PR-40", "  - RS-20"], after="  required_interfaces:")
    R.replace("PR-40", "    - PR-30", "    - PR-20", after="    consumers:")
    R.replace("PR-40", "  - PR-30", "  - PR-20", after="  required_interfaces:")
    R.replace("RS-40", "    - PR-35", ["    - PR-35", "    - PR-40"], after="    consumers:")
    R.replace("RS-40", "  - PR-35", ["  - PR-35", "  - PR-40"], after="  required_interfaces:")
    R.insert_after("PR-35", "    states:", ["    - MERGE_OBSERVED"])  # ASCII order (V-12)
    R.replace("RS-40", "    - MERGE_PENDING", ["    - MERGE_OBSERVED", "    - MERGE_PENDING"], after="    states:")
    # 7.6: authored edits
    R.replace("PR-30", "    - Implement, test, commit, publish, and review-correct the exact proceeded PR work unit",
              "    - Implement, test, commit and publish the exact proceeded PR work unit; review findings and CI fixes on the published PR belong to PR-35")
    R.replace("PR-35", "  session_class: SAME_SESSION_CONTINUATION", "  session_class: DEDICATED_PR_REVIEW_SESSION")
    R.replace("PR-35", "  session_role: You are the same dedicated PR-development session that produced or recovered the exact PR_CANDIDATE_PUBLISHED result for one proceeded work unit.",
              "  session_role: " + qn(PR35_ROLE))
    R.replace("PR-35", "  creator_role: The same dedicated PR-development session; PR-30 and PR-35 are two phases of one native PR execution work unit.",
              "  creator_role: The dedicated PR-35 session; PR-30 and PR-35 are two phases of one work unit, run in two dedicated sessions.")
    R.replace("PR-35", "  - same dedicated PR session reference with session_disposition RETAIN_EXISTING",
              "  - " + q("session_disposition: NEW_DEDICATED — the dedicated PR-35 session for this WORK_UNIT_ID"))
    R.replace("PR-35", "    - Add an R1 row, actor, approval, Proceed, work unit or session",
              "    - Add an R1 row, actor, approval, Proceed or work unit, or any session beyond its own dedicated PR-35 session")
    R.insert_after("PR-20", "  - PR_INSTRUCTION_ID", ["  - " + qn(PR20_INPUT)])
    R.replace("PR-40", "  - The complete PR-30 result with PR_CANDIDATE_PUBLISHED and the complete PR-35 result whose earlier MERGE_PENDING is historical pre-merge evidence",
              ["  - The complete PR-30 result with PR_CANDIDATE_PUBLISHED", "  - " + qn(PR35_RESULT_INPUT)])
    R.replace("PR-40", "  - Existing PR reviewer/session lineage for a rereview, the dedicated PR session identity, the whole-change IA context and exact return owner",
              "  - Existing PR reviewer/session lineage for a rereview, the PR-30 and PR-35 session identities, the whole-change IA context and exact return owner")
    R.replace("PR-40", "  - Nathan's later invocation asserting the identified PR was manually merged after PR-35 produced MERGE_PENDING",
              "  - " + qn(PR40_ENTRY))
    R.replace("RS-40", "  session_role: You are the same dedicated PR engineering session for the exact suspended work unit.",
              "  session_role: " + qn(RS40_ROLE))
    R.replace("RS-40", "  creator_role: the same dedicated PR engineering session for the exact suspended work unit.",
              "  creator_role: " + qn(RS40_CREATOR))
    # 7.8 N1: new key, last under body_extraction_convention (inserted before the next top-level key)
    obs = [i for i, l in enumerate(R.lines) if l == "observation:"]
    bec = [i for i, l in enumerate(R.lines) if l == "body_extraction_convention:"]
    assert len(obs) == 1 and len(bec) == 1 and bec[0] < obs[0]
    assert all(not l or l.startswith("  ") for l in R.lines[bec[0] + 1:obs[0]])
    assert "  body_identity_disposition:" not in "\n".join(R.lines)
    R.lines[obs[0]:obs[0]] = N1_LINES
    return R.text()


# ---- checks (§7.9) ----------------------------------------------------------------------------
LISTS = ("required_literals", "forbidden_literals", "required_regex", "forbidden_regex")
ids = lambda l: [((x["value"], x.get("rule_id")) if isinstance(x, dict) else (x, None)) for x in l or []]
RM = sorted([("required_regex", ("Prompt [Vv]ersion: `?091426\\.1`?", "SRC-001")),
             ("required_regex", ("Ecosystem release: `?GCFPE-20260914\\.1`?", "INV-003"))])
EXPECTED_FIELDS = {"PR-20": ["inputs"], "PR-30": ["mutations"],
                   "PR-35": ["creator_role", "inputs", "mutations", "outputs", "required_interfaces", "session_class", "session_role"],
                   "PR-40": ["inputs", "outputs", "required_interfaces"],
                   "RS-40": ["creator_role", "outputs", "required_interfaces", "session_role"]}


def semdiff(old, new):
    rep = {}
    top = sorted(k for k in set(old) | set(new) if k != "prompts" and old.get(k) != new.get(k))
    rep["top_level_keys_changed"] = top
    ob, nb = old["body_extraction_convention"], new["body_extraction_convention"]
    rep["N1_only"] = (top == ["body_extraction_convention"] and {k: v for k, v in nb.items() if k != "body_identity_disposition"} == ob
                      and list(nb)[:-1] == list(ob) and list(nb)[-1] == "body_identity_disposition"
                      and nb["body_identity_disposition"] == N1_TEXT)
    O = {r["prompt_key"]: r for r in old["prompts"]}
    N = {r["prompt_key"]: r for r in new["prompts"]}
    rep["rows_kept_in_set_and_order"] = list(O) == list(N) and len(O) == 55
    exp = {k: [] for k in O}
    for gid, kind, value, rid, sel in GUARDS:
        for k in select(old["prompts"], sel):
            exp[k].append((kind, (value, rid)))
    bad, fields, order_bad = [], {}, []
    for k in O:
        a, b = O[k], N[k]
        f = sorted(x for x in set(a) | set(b) if x != "audit_assertions" and a.get(x) != b.get(x))
        if f:
            fields[k] = f
        if set(a["audit_assertions"]) != set(b["audit_assertions"]):
            bad.append((k, "assertion keys"))
        add, rm = [], []
        for l in LISTS:
            x, y = ids(a["audit_assertions"].get(l)), ids(b["audit_assertions"].get(l))
            cx, cy = Counter(x), Counter(y)
            add += [(l, e) for e in (cy - cx).elements()]
            rm += [(l, e) for e in (cx - cy).elements()]
            if [e for e in y if e in x] != [e for e in x if e in y]:
                order_bad.append((k, l))
        if sorted(add) != sorted(exp[k]) or sorted(rm) != RM:
            bad.append(k)
    rep["rows_with_unexpected_assertion_diff"] = bad
    rep["kept_order_violations"] = order_bad
    rep["non_assertion_fields_changed"] = fields
    rep["non_assertion_fields_as_expected"] = fields == EXPECTED_FIELDS
    tot = lambda Rg: sum(len(r["audit_assertions"].get(l) or []) for r in Rg["prompts"] for l in LISTS)
    rep["assertions"] = [tot(old), tot(new)]
    rep["rows_per_guard"] = {g[0]: sum(1 for r in new["prompts"] if (g[2], g[3]) in ids(r["audit_assertions"].get(g[1]))) for g in GUARDS}
    rep["inputs_all_str"] = all(isinstance(x, str) for r in new["prompts"] for x in r.get("inputs") or [])
    rep["states"] = {k: [o.get("states") for o in N[k]["outputs"]] for k in ("PR-35", "RS-40")}
    rep["values"] = {"PR-35.session_role == W-1": N["PR-35"]["session_role"] == PR35_ROLE,
                     "RS-40.session_role == W-2": N["RS-40"]["session_role"] == RS40_ROLE,
                     "RS-40.creator_role == W-2": N["RS-40"]["creator_role"] == RS40_CREATOR,
                     "PR-40 inputs contain PR-30 result, W-4 PR-35 result, W-4 entry": all(
                         s in N["PR-40"]["inputs"] for s in ("The complete PR-30 result with PR_CANDIDATE_PUBLISHED", PR35_RESULT_INPUT, PR40_ENTRY)),
                     "PR-20 input present": PR20_INPUT in N["PR-20"]["inputs"]}
    # diff of the changed non-assertion fields, for the record
    rep["field_diffs"] = {k: {f: {"old": O[k].get(f), "new": N[k].get(f)} for f in fs} for k, fs in fields.items()}
    return rep


def parts(d):
    return {f[:-5]: json.load(open(d + "/prompts/" + f, encoding="utf-8")) for f in os.listdir(d + "/prompts")}


def drift(reg, P):
    out = []
    for r in reg["prompts"]:
        part = P[r["prompt_key"]]
        want = sorted({e["to"] for e in part["edges"] if e["to_kind"] == "prompt" and e["to"] != part["id"]})
        cons = {c for o in r["outputs"] for c in (o.get("consumers") or [])}
        st = {s for o in r["outputs"] for s in (o.get("states") or [])}
        if r["required_interfaces"] != want or cons != set(want) or st != set(part["node"]["result_states"]):
            out.append(r["prompt_key"])
    return out


def main():
    head = subprocess.run(["git", "-C", REPO, "show", "HEAD:" + REL], capture_output=True, check=True).stdout
    assert hashlib.sha256(head).hexdigest() == BASE_SHA, "HEAD registry is not the spec baseline"
    cur = open(REG, "rb").read()
    open(W + "/registry.head.md", "wb").write(head)
    old = load_data(W + "/registry.head.md")
    new_text = apply(head.decode("utf-8"), old)
    open(W + "/registry.new.md", "w", encoding="utf-8").write(new_text)
    new = load_data(W + "/registry.new.md")
    rep = semdiff(old, new)
    ok = (rep["N1_only"] and rep["rows_kept_in_set_and_order"] and not rep["rows_with_unexpected_assertion_diff"]
          and not rep["kept_order_violations"] and rep["non_assertion_fields_as_expected"] and rep["inputs_all_str"]
          and all(rep["values"].values()))
    r = subprocess.run([sys.executable, W + "/wga/scripts/validate_project_prompt_registry.py", W + "/registry.new.md"],
                       capture_output=True, text=True, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    rep["structure_check"] = {"exit": r.returncode, "stdout": r.stdout.strip(), "stderr": r.stderr.strip()}
    P0 = {}
    base_parts = W + "/parts_head"
    os.makedirs(base_parts + "/prompts")
    for f in os.listdir(PARTS + "/prompts"):
        blob = subprocess.run(["git", "-C", REPO, "show", "HEAD:docs/graph/parts/prompts/" + f], capture_output=True, check=True).stdout
        open(base_parts + "/prompts/" + f, "wb").write(blob)
    P0, P1 = parts(base_parts), parts(PARTS)
    d = {"head registry vs head parts": drift(old, P0), "edited registry vs E1 parts": drift(new, P1),
         "unedited registry vs E1 parts (must fail)": drift(old, P1)}
    n = copy.deepcopy(new)
    {x["prompt_key"]: x for x in n["prompts"]}["PR-40"]["outputs"][0]["consumers"] = ["PR-10", "PR-30", "RS-10"]
    d["PR-30 re-injected into PR-40 consumers (must fail)"] = drift(n, P1)
    n = copy.deepcopy(new)
    {x["prompt_key"]: x for x in n["prompts"]}["RS-40"]["outputs"][0]["states"].remove("MERGE_OBSERVED")
    d["MERGE_OBSERVED removed from RS-40 states (must fail)"] = drift(n, P1)
    rep["drift"] = d
    ok = ok and r.returncode == 0 and json.loads(r.stdout) == {"valid": True, "problems": []} and d == {
        "head registry vs head parts": [], "edited registry vs E1 parts": [],
        "unedited registry vs E1 parts (must fail)": ["PR-35", "PR-40", "RS-40"],
        "PR-30 re-injected into PR-40 consumers (must fail)": ["PR-40"],
        "MERGE_OBSERVED removed from RS-40 states (must fail)": ["RS-40"]}
    rep["new_lines"] = new_text.count("\n")
    rep["new_sha256"] = hashlib.sha256(new_text.encode("utf-8")).hexdigest()
    rep["ALL_CHECKS_OK"] = ok
    print(json.dumps({k: v for k, v in rep.items() if k != "field_diffs"}, indent=1, ensure_ascii=False))
    open(W + "/report.json", "w", encoding="utf-8").write(json.dumps(rep, indent=1, ensure_ascii=False))
    assert ok, "checks failed; nothing written"
    if WRITE:
        assert cur == head or cur.decode("utf-8") == new_text, "working-tree registry is neither HEAD nor the target"
        open(REG, "w", encoding="utf-8").write(new_text)
        print("wrote", REG)


if __name__ == "__main__":
    main()
