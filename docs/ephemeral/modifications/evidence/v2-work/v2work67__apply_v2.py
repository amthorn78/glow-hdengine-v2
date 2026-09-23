"""Prototype of the line-anchored registry edit (spec §7), run on a scratch copy only.
Every op names its row and an exact anchor line; each anchor must occur exactly once inside the
row's line range, or the script stops. No YAML is re-serialized: new lines are inserted verbatim."""
import json, re, sys
sys.path.insert(0, "/tmp/claude-0/v2work67")
from guards_v2 import GUARDS

SRC = "/tmp/claude-0/v2work67/registry.md"
OUT = "/tmp/claude-0/v2work67/registry.new.md"


def q(s):
    """YAML single-quoted scalar."""
    return "'" + s.replace("'", "''") + "'"


def qn(s):
    """Plain when the plain form round-trips, else single-quoted."""
    import yaml
    try:
        if yaml.safe_load("k: " + s) == {"k": s}:
            return s
    except Exception:
        pass
    return q(s)


def entry(value, rid, indent="    "):
    return [f"{indent}- value: {q(value)}", f"{indent}  rule_id: {rid}"]


class Reg:
    def __init__(self, path):
        self.lines = open(path, encoding="utf-8").read().split("\n")

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
        """Index just after the last item of the list opened by `header` (e.g. '    forbidden_regex:')."""
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

    def save(self, path):
        open(path, "w", encoding="utf-8").write("\n".join(self.lines))


def select(reg_rows, sel):
    keys = [r["prompt_key"] for r in reg_rows]
    if sel == "ALL55":
        return keys
    if sel == "MAIN54":
        return [k for k in keys if k != "GCFPE-MGMT-10"]
    if sel == "NPH53":
        return [r["prompt_key"] for r in reg_rows if any(
            (x.get("value") if isinstance(x, dict) else x) == "NEXT_PROMPT_HANDOFF"
            for x in r["audit_assertions"].get("required_literals") or [])]
    if sel == "STEP32":  # open: set known only at E3; prototype uses the three named rows
        return ["PR-30", "PR-35", "RS-40"]
    return list(sel)


def main(choices):
    sys.path.insert(0, "/tmp/claude-0/v2work67/wga/scripts")
    from audit_workspace_governance import load_data
    old = load_data(SRC)
    R = Reg(SRC)
    # 1. step 43: remove the two release-identity required_regex entries from all 55 rows
    for r in old["prompts"]:
        k = r["prompt_key"]
        R.delete_pair(k, "    - value: 'Prompt [Vv]ersion: `?091426\\.1`?'", "      rule_id: SRC-001")
        R.delete_pair(k, "    - value: 'Ecosystem release: `?GCFPE-20260914\\.1`?'", "      rule_id: INV-003")
    # 2. guards, appended to the end of the row's list, in guard order
    for gid, kind, value, rid, sel, home in GUARDS:
        for k in select(old["prompts"], sel):
            R.append_list(k, f"    {kind}:", entry(value, rid))
    # 3. D13-derived fields (registry deriver), sorted consumers and interfaces
    R.replace("PR-35", "    - RS-20", ["    - PR-40", "    - RS-20"], after="    consumers:")
    R.replace("PR-35", "  - RS-20", ["  - PR-40", "  - RS-20"], after="  required_interfaces:")
    R.replace("PR-40", "    - PR-30", "    - PR-20", after="    consumers:")
    R.replace("PR-40", "  - PR-30", "  - PR-20", after="  required_interfaces:")
    R.replace("RS-40", "    - PR-35", ["    - PR-35", "    - PR-40"], after="    consumers:")
    R.replace("RS-40", "  - PR-35", ["  - PR-35", "  - PR-40"], after="  required_interfaces:")
    st = choices["states_order"]  # 'sorted' or 'vocabulary'
    if st == "sorted":
        R.insert_after("PR-35", "    states:", ["    - MERGE_OBSERVED"])
        R.replace("RS-40", "    - MERGE_PENDING", ["    - MERGE_OBSERVED", "    - MERGE_PENDING"], after="    states:")
    else:
        R.replace("PR-35", "    - MERGE_PENDING", ["    - MERGE_PENDING", "    - MERGE_OBSERVED"], after="    states:")
        R.replace("RS-40", "    - MERGE_PENDING", ["    - MERGE_PENDING", "    - MERGE_OBSERVED"], after="    states:")
    # 4. authored edits
    R.replace("PR-30", "    - Implement, test, commit, publish, and review-correct the exact proceeded PR work unit",
              "    - Implement, test, commit and publish the exact proceeded PR work unit; review findings and CI fixes on the published PR belong to PR-35")
    R.replace("PR-35", "  session_class: SAME_SESSION_CONTINUATION", "  session_class: DEDICATED_PR_REVIEW_SESSION")
    R.replace("PR-35", "  session_role: You are the same dedicated PR-development session that produced or recovered the exact PR_CANDIDATE_PUBLISHED result for one proceeded work unit.",
              "  session_role: " + qn(choices["pr35_role"]))
    R.replace("PR-35", "  creator_role: The same dedicated PR-development session; PR-30 and PR-35 are two phases of one native PR execution work unit.",
              "  creator_role: The dedicated PR-35 session; PR-30 and PR-35 are two phases of one work unit, run in two dedicated sessions.")
    R.replace("PR-35", "  - same dedicated PR session reference with session_disposition RETAIN_EXISTING",
              "  - " + q("session_disposition: NEW_DEDICATED — the dedicated PR-35 session for this WORK_UNIT_ID"))
    R.replace("PR-35", "    - Add an R1 row, actor, approval, Proceed, work unit or session",
              "    - Add an R1 row, actor, approval, Proceed or work unit, or any session beyond its own dedicated PR-35 session")
    R.insert_after("PR-20", "  - PR_INSTRUCTION_ID", ["  - " + qn(choices["pr20_input"])])
    R.replace("PR-40", "  - Existing PR reviewer/session lineage for a rereview, the dedicated PR session identity, the whole-change IA context and exact return owner",
              "  - Existing PR reviewer/session lineage for a rereview, the PR-30 and PR-35 session identities, the whole-change IA context and exact return owner")
    R.replace("PR-40", "  - Nathan's later invocation asserting the identified PR was manually merged after PR-35 produced MERGE_PENDING",
              "  - " + qn(choices["pr40_input"]))
    R.replace("RS-40", "  session_role: You are the same dedicated PR engineering session for the exact suspended work unit.",
              "  session_role: " + qn(choices["rs40_role"]))
    import texts_v2 as T
    R.replace("RS-40", "  creator_role: the same dedicated PR engineering session for the exact suspended work unit.",
              "  creator_role: " + qn(T.J["W-2 RS-40 creator"]))
    R.replace("PR-40", "  - The complete PR-30 result with PR_CANDIDATE_PUBLISHED and the complete PR-35 result whose earlier MERGE_PENDING is historical pre-merge evidence",
              "  - " + qn(T.J["W-4 PR-35 result input"]))
    R.save(OUT)
    return old, load_data(OUT)


if __name__ == "__main__":
    import texts_v2 as T
    ch = {"states_order": "sorted", "pr35_role": T.J["W-1 PR-35 role"], "pr20_input": T.J["PR-20 input"],
          "pr40_input": T.J["W-4 PR-40 entry"], "rs40_role": T.J["W-2 RS-40 role"]}
    old, new = main(ch)
    print("applied; rows", len(new["prompts"]))
