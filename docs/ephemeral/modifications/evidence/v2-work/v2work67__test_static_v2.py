import re, sys, yaml
sys.path.insert(0, "/tmp/claude-0/v2work67")
import texts_v2 as T
from guards_v2 import GUARDS, G25_PR40_CANDIDATE
J, W = T.J, T.W
BODY = [k for k in J if k not in T.NON_BODY]
C = lambda *ks: " ".join(J[k] for k in ks)
HR = "Emit exactly one `NEXT_PROMPT_HANDOFF` block."
COMBOS = {
 "PLACE+HANDOFF+SESSION+TOP": C("C-PLACE", "C-HANDOFF", "C-SESSION", "C-TOP"),
 "rule+HANDOFF+PLACE+TOP": HR + " " + C("C-HANDOFF", "C-PLACE", "C-TOP"),
 "PLACE+SESSION": C("C-PLACE", "C-SESSION"),
 "DISPATCH+SUB+TOP": C("C-DISPATCH", "C-SUB", "C-TOP"),
 "rule+HANDOFF+ASKvariant+TOP": HR + " " + C("C-HANDOFF", "C-PLACE ASK OK? variant", "C-TOP"),
 "REPLAN+PROCEED+PR30+TOP": C("C-REPLAN", "C-PROCEED", "C-PR30-ENTRY", "C-TOP"),
 "long single paragraph": HR + " " + C("C-HANDOFF", "C-SESSION", "C-DISPATCH", "C-SUB", "C-PLACE", "C-TOP", "C-PROCEED", "C-REPLAN", "W-4 PR-40 entry"),
}
WORKER = ["use subagents as workers within this task", "spawn worker subagents for parallel reads within this session",
          "Run PR-35's tests in a subagent.", "Nathan creates a new session for PR-40 and pastes the handoff.",
          "Hand PR-35's result to a workflow agent for summarising.", "Nathan opens a new session for PR-40.",
          "It may use subagents as workers within its own task.", "subagents may be used as workers within task",
          "Dispatch worker subagents to read the files in parallel.", "Spawn a worker subagent to run the tests.",
          "Workers within a task are allowed.", "Never run PR-35 as a subagent.", "Do not run PR-35 as a subagent.",
          "Don't run PR-35 as a subagent.", "Do not launch a new session for PR-40.", "Never launch a new session for PR-40.",
          "It never creates, starts or schedules another session.", "Nathan creates the PR-40 session and pastes it.",
          "Subscribing is not polling, and it creates no session.", "schedule a reminder with mcp__Claude_Code_Remote__send_later"]
INJECT = {
 "G19": ["Run PR-35 as a subagent.", "run PR-35 as a subagent", "Invoke the next prompt as a subagent.",
         "dispatch PR-40 to a workflow agent", "Hand PR-40 to a forked agent.", "start this prompt in a sub-agent",
         "spawns PR-20 as a subagent", "launched PR-35 via a workflow agent"],
 "G20": ["Launch a new session for PR-40.", "launch a new session for PR-40", "spawn a session to run PR-40",
         "open a new session for PR-20", "Starts a new session running PR-35", "create a new session for this prompt",
         "schedule a session for the next prompt"],
 "G21": ["mcp__Claude_Code_Remote__create_session", "call create_trigger", "fire_trigger", "spawn-session", "spawn_session"],
}
LIMITS = {
 "G19": ["running PR-35 as a subagent", "executed PR-35 as a subagent", "invoked PR-35 as a subagent",
         "executing PR-35 in a subagent", "PR-35 is run as a subagent", "run it as a subagent",
         "It is forbidden to run PR-35 as a subagent.", "Do not ever run PR-35 as a subagent.",
         "PR-35 must never be used to run PR-40 as a subagent.", "subagents run PR-35's tests in a subagent",
         "Run PR-35s tests in a subagent."],
 "G20": ["launch a new session.", "created a session for PR-40", "No agent may launch a new session for PR-40.",
         "No agent may start a session for PR-40.", "without launching a new session for PR-40",
         "Nathan, not the agent, may open a new session for PR-40.", "Nathan will create a new session for PR-40."],
 "G21": ["mcp__Claude_Code_Remote__send_later"],
}
fail = 0
out = []
for g in GUARDS + [G25_PR40_CANDIDATE]:
    gid, kind, value, rid, rows, home = g
    rx = re.compile(value, re.M)
    y = "- value: '" + value.replace("'", "''") + "'\n  rule_id: " + rid + "\n"
    rt = yaml.safe_load(y) == [{"value": value, "rule_id": rid}]
    plain_ok = True
    try:
        plain_ok = yaml.safe_load("- value: " + value + "\n  rule_id: " + rid + "\n") == [{"value": value, "rule_id": rid}]
    except Exception:
        plain_ok = False
    line = f"{gid} {kind[:3]} rt={rt} plain_rt={plain_ok}"
    fail += not rt
    if kind == "required_regex":
        hj = {h: bool(rx.search(J[h])) for h in home}
        hw = {h: bool(rx.search(W[h])) for h in home if h in W}
        others = [k for k in BODY if k not in home and rx.search(J[k])]
        line += f" home_joined={hj} home_wrapped={hw} other_body_hits={others}"
        fail += (not all(hj.values())) + bool(others)
        if gid in ("G07", "G24", "G25", "G08A", "G25P"):
            cnt = {k: len(rx.findall(t)) for k, t in list(J.items()) + list(COMBOS.items()) if rx.search(t)}
            line += f" occurrences={cnt}"
    else:
        hits = [(k, f) for k in J for f, D in (("J", J), ("W", W)) if k in D and rx.search(D[k])]
        ch = [k for k, t in COMBOS.items() if rx.search(t)]
        wh = [p for p in WORKER if rx.search(p)]
        sup = [k for k, t in T.SUPERSEDED.items() if rx.search(t)]
        line += f" canonical_hits={hits} combo_hits={ch} worker_hits={wh} superseded_hits={sup}"
        fail += bool(hits) + bool(ch) + bool(wh)
        if gid in INJECT:
            miss = [p for p in INJECT[gid] if not rx.search(p)]
            line += f" injections={len(INJECT[gid]) - len(miss)}/{len(INJECT[gid])} missed={miss}"
            fail += bool(miss)
        if gid in LIMITS:
            line += f" limit_probes_matched={[p for p in LIMITS[gid] if rx.search(p)]}"
    out.append(line)
print("\n".join(out))
print("four named worker phrasings:", {p: [g[0] for g in GUARDS if g[1] == 'forbidden_regex' and re.search(g[2], p, re.M)] for p in WORKER[:4]})
print("long paragraph chars:", len(COMBOS["long single paragraph"]))
print("STATIC FAILURES:", fail)
