"""Build request-v7.json from request-v6.json and request-hd-v2.json from request-hd-v1.json.
Targeted edits only: the effort Score keeps its five levels (low to max) and their texts;
the ultracode level leaves the Score and becomes its own Noul question; the model Choice is
kept, with its ladder wording corrected. Every edit is asserted so a silent miss fails."""
import json, re, sys, copy
from pathlib import Path

V6, HD1, OUT = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])

def sub_once(text, old, new):
    assert text.count(old) == 1, (old[:80], text.count(old))
    return text.replace(old, new)

def rung_to_level(s):
    s = re.sub(r"\brungs\b", "levels", s)
    return re.sub(r"\brung\b", "level", s)

# ---------- v7 ----------
v6 = json.loads(V6.read_text())
v7 = copy.deepcopy(v6)
eff = v7["questions"]["effort"]
q = eff["instructions"]["question"]
q = sub_once(q, "How high on the six-rung strength ladder does the AI coding session described in `action` belong? The rungs are ordered by",
             "Which effort level does the AI coding session described in `action` need? The levels are ordered by")
q = sub_once(q, "Read four signals in the description:", "Read three signals in the description:")
q = sub_once(q, "; (4) whether one reader can hold the whole object, or the risk is that any single reader misses something, so that only many independent readers cross-checking one another would do.",
             ". Place the session by these three signals only, not by whether the work should be split across many independent agents.")
eff["instructions"]["question"] = q
t = eff["instructions"]["tradeoff"]
t = sub_once(t, " across the five single-session rungs,", " across the five levels,")
t = sub_once(t, "; the sixth rung multiplies the cost again by the number of agents.", ".")
t = sub_once(t, "a rung too high wastes a multiple of the cost while a rung too low risks the miss the ladder exists to prevent.",
             "a level too high wastes a multiple of the cost while a level too low risks the miss the levels exist to prevent.")
eff["instructions"]["tradeoff"] = rung_to_level(t)
assert len(eff["criteria"]) == 6 and eff["criteria"][5].startswith("ultracode:")
eff["criteria"] = [rung_to_level(c) for c in eff["criteria"][:5]]
eff["criteria"][4] = sub_once(eff["criteria"][4], "max: the deepest single-session reasoning,", "max: the deepest reasoning level,")
assert [c.split(":")[0] for c in eff["criteria"]] == ["low", "medium", "high", "extra high", "max"]

mod = v7["questions"]["model"]
mq = mod["instructions"]["question"]
mod["instructions"]["question"] = sub_once(mq, "at whatever rung it needs?", "at whatever effort level it needs?")
mt = mod["instructions"]["tradeoff"]
mt = sub_once(mt, "Both are frontier agentic coding models with the same five single-session rungs; the many-agent setting is documented for any model with an extra-high rung, though the one guide that lists supported models names the lower-cost model and not the most capable one.",
              "Both are frontier agentic coding models with the same five effort levels, and either can run with the many-agent workflow setting on at any of them.")
mod["instructions"]["tradeoff"] = rung_to_level(mt)
for k, crit in mod["criteria"].items():
    for f in ("what", "not_for"):
        crit[f] = rung_to_level(crit[f])

ultra_v7 = {
    "type": "noul",
    "instructions": {
        "question": "Should the AI coding session described in `action` run with the many-agent workflow setting on, so that independent agents each take or cross-check one part of the work, rather than one session working through it alone? This is separate from how much reasoning each step needs: a broad but simple sweep can call for it at a low effort level, and a deep problem that one mind must follow from start to end can call for the deepest level without it.",
        "tradeoff": "In the coding harness this setting has Claude plan dynamic workflows of agents for substantive tasks, at whatever effort level the session runs at; each workflow runs up to 16 agents at once by default and up to 1,000 per run. No measured run of this setting exists for either model; the case for it rests on independence measured on older models: reviewer agents with error correlation of 0.05 to 0.25 lifted bug detection from 32.8% for one agent to 72.4% combined and 79.3% for the best pair, at a 50% false-positive rate; a second model reviewing another's drafts raised pass rate from 71.6% to 89.7% while self-review gained nothing; aggregating ten reviews raised recall 118%. In one controlled study, parallel agents gained 80.9% on tasks that split into independent parts and lost 39 to 70% on sequential ones. Costs multiply: ten parallel agents use quota ten times faster, a 5-agent system used 41 times the tokens of one agent, and a managed many-agent review averages about 20 minutes and $15 to $25 per review. In a controlled benchmark on a 35,000-line project, orchestration neither helped nor hurt the lower-cost model; a research synthesis puts the plateau at about four agents, and at equal compute single-agent systems matched or beat multi-agent ones on reasoning tasks. So the setting is for scale or independence that a single reader cannot supply, not for a bounded diff or a listed correction."
    },
    "criteria": {
        "true": "The work splits into many separate parts of the same kind, such as every service of a codebase, hundreds of files, many independent checks, many claims or many sources, that agents can each take on or verify in parallel without needing one another's results.",
        "false": "The work is one connected object or line of reasoning that a single session must follow as a whole, even when it is large or consequential: one change, one system, one document or one problem, such as a bounded diff, a listed correction pass, the review of one change, a focused diagnosis, an implementation carried out step by step from a plan, a live run carried out step by step, a lookup, or recording and reporting."
    }
}
v7["questions"] = {"effort": eff, "ultracode": ultra_v7, "model": mod}

# ---------- hd-v2 ----------
hd1 = json.loads(HD1.read_text())
hd2 = copy.deepcopy(hd1)
e2 = hd2["questions"]["effort"]
q = e2["instructions"]["question"]
q = sub_once(q, "How high on the six-rung strength ladder does the Human Design report-production job described in `action` belong?",
             "Which effort level does the Human Design report-production job described in `action` need?")
q = sub_once(q, "The rungs are ordered by", "The levels are ordered by")
q = sub_once(q, "Read four signals in the description:", "Read three signals in the description:")
q = sub_once(q, "; (4) whether one careful pass can hold the whole object, or the risk is that any single reader misses claims spread across long reports, so that independent checkers each taking one part would do better.",
             ". Place the job by these three signals only, not by whether the work should be split across several independent agents.")
e2["instructions"]["question"] = q
t = e2["instructions"]["tradeoff"]
t = sub_once(t, "across the five single-session rungs", "across the five levels")
t = sub_once(t, " The sixth rung multiplies the cost again by the number of agents.", "")
t = sub_once(t, "a rung too low risks the miss the ladder exists to prevent.", "a rung too low risks the miss the levels exist to prevent.")
e2["instructions"]["tradeoff"] = rung_to_level(t)
assert len(e2["criteria"]) == 6 and e2["criteria"][5].startswith("ultracode:")
e2["criteria"] = [rung_to_level(c) for c in e2["criteria"][:5]]
e2["criteria"][4] = sub_once(e2["criteria"][4], "max: the deepest single-session reasoning,", "max: the deepest reasoning level,")
assert [c.split(":")[0] for c in e2["criteria"]] == ["low", "medium", "high", "extra high", "max"]
m2 = hd2["questions"]["model"]
m2["instructions"]["question"] = sub_once(m2["instructions"]["question"], "at whatever rung it needs?", "at whatever effort level it needs?")
mt = m2["instructions"]["tradeoff"]
mt = sub_once(mt, "Both are frontier models with the same five single-session rungs.",
              "Both are frontier models with the same five effort levels, and either can run as several independent agents (in Claude Code, both support the many-agent workflow setting at every effort level).")
m2["instructions"]["tradeoff"] = rung_to_level(mt)
for k, crit in m2["criteria"].items():
    for f in list(crit.keys()):
        if isinstance(crit[f], str):
            crit[f] = rung_to_level(crit[f])
ultra_hd = {
    "type": "noul",
    "instructions": {
        "question": "Should the Human Design report-production job described in `action` be done by several independent agents, each taking or checking one part of the work, rather than by one session alone? This is separate from how much reasoning each part needs.",
        "tradeoff": "Claim-by-claim checking is cheap and close to human agreement (72% agreement with human raters on about 16,000 facts, at about $0.19 per response); one fresh review by the same model plus one by a different model caught 57% of planted errors against 43% for two reviews by the same model. Gains plateau at a few independent reviewers, and multi-agent setups used 15 to 80 times the tokens of one agent, so several agents are for independence a single reader cannot supply, not for routine reports or listed repairs."
    },
    "criteria": {
        "true": "The job splits into many separate parts of the same kind that independent checkers can each take on in parallel without needing one another's results.",
        "false": "The job is one connected piece of work that one careful pass must follow as a whole: writing one report, repairing named defects in one report, checking one published document against its source, recording or filing, or a controller run whose steps depend on each other."
    }
}
hd2["questions"] = {"effort": e2, "ultracode": ultra_hd, "model": m2}

for name, body in (("request-v7.json", v7), ("request-hd-v2.json", hd2)):
    s = json.dumps(body, ensure_ascii=False, indent=1) + "\n"
    low = s.lower()
    for bad in ("six-rung", "sixth rung", "the top rung", "strength level above max", "single-session rungs", "single-session reasoning", "must hold for everything that follows", "judge only how much"):
        assert bad not in low, (name, bad)
    assert not re.search(r"\brungs?\b", s), (name, re.findall(r".{40}\brungs?\b.{40}", s)[:3])
    (OUT / name).write_text(s, encoding="utf-8")
    print(name, len(s.encode()), "bytes; questions:", list(body["questions"]),
          "; effort levels:", len(body["questions"]["effort"]["criteria"]))
