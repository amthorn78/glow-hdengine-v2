"""Build request-v8.1.json from request-v8.json: the one revision the pre-registration allows,
fitted to v8's run-1 Part B miss (TYPESAFE-FOUR-MODEL-RESULTS-20261016.md, section 3).

Only the strong model's criteria change. Its "what" returns to v6's accepted text, less the three
kinds of work v8 hands to the cheaper options (checking results against a list, recording
decisions, writing or updating documents), with its measurement sentence restated for four
models. Removed: v8's "where a miss would reach a merge, a live system or later work", "across a
large or security-sensitive codebase" and "the exact-head review that gates a merge", and the
exact-head review example. Everything else is v8's, and the build asserts it.

usage: python3 build_v8_1.py request-v8.json request-v8.1.json
"""
import copy, json, sys
from pathlib import Path

SRC, OUT = Path(sys.argv[1]), Path(sys.argv[2])
v8 = json.loads(SRC.read_text())
v81 = copy.deepcopy(v8)
crit = v81["questions"]["model"]["criteria"]["strong_model"]
crit["what"] = ("Well-specified agentic coding and code review that a strong model completes reliably, including long-running "
                "coding sessions on a known task list: applying named fixes each with a test, reviewing a correction pass against "
                "the findings it claims to fix, a repeat review of a component already reviewed once. Independent measurements put "
                "it first of the four on the general and work-task indexes at max, at a quarter to a sixth of the most capable "
                "model's cost per task and 2 to 3 times faster per task.")
crit["examples"] = crit["examples"][:2]
assert crit["examples"] == ["Fix five review findings that each name a file and a defect, adding a test for each",
                            "Review a correction pass against the findings it says it fixed"]
# Everything outside the strong model's "what" and "examples" is unchanged.
a, b = copy.deepcopy(v8), copy.deepcopy(v81)
for d in (a, b):
    d["questions"]["model"]["criteria"]["strong_model"].pop("what")
    d["questions"]["model"]["criteria"]["strong_model"].pop("examples")
assert a == b
for phrase in ("exact-head", "later work", "security-sensitive codebase"):
    assert phrase not in crit["what"] and not any(phrase in e for e in crit["examples"])
for name in ("Fable", "Opus", "Sonnet", "Haiku", "Claude", "Anthropic"):
    assert name not in json.dumps(v81)
OUT.write_text(json.dumps(v81, indent=1, ensure_ascii=False) + "\n")
print("built", OUT)
