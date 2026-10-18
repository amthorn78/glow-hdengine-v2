"""Build request-v8.2.json from request-v6.json and request-v8.json: the revision Nathan chose on
2026-10-18 (option (c), "c, go ahead") after v8 and v8.1 failed gate B_model.

v6's model question is kept word for word: its question, its two-model tradeoff and its two options
(`most_capable_model`, `strong_lower_cost_model`) with their texts and examples. The tradeoff is
prefixed with one sentence that scopes it to those two options, and a paragraph about the two new
options is appended. The two new options (`balanced_model`, `small_fast_model`) are v8's, with
"the strong model" renamed to v6's "the strong lower-cost model". The effort Score is v6's,
unchanged. Every edit is asserted.

usage: python3 build_v8_2.py request-v6.json request-v8.json request-v8.2.json
"""
import copy, json, sys
from pathlib import Path

V6, V8, OUT = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
v6, v8 = json.loads(V6.read_text()), json.loads(V8.read_text())
v82 = copy.deepcopy(v6)
m6 = v6["questions"]["model"]
m = v82["questions"]["model"]
assert list(m6["criteria"]) == ["most_capable_model", "strong_lower_cost_model"]

PREFIX = "The first two options, the most capable model and the strong lower-cost model, compare as follows. "
NEW = (" The two further options are smaller and cheaper. List prices per million input and output tokens: the balanced model $2 "
       "and $10; the small fast model $0.10 and $0.50 for prompts up to 100,000 tokens ($0.50 and $2.50 above). Independent index by "
       "rung, low to max, with cost per task: balanced 36, 41, 47, 52, 56 at $0.35, $0.48, $0.88, $2.01, $5.46; small fast 29, 34, 38, "
       "41, 43 at $0.02, $0.05, $0.08, $0.12, $0.21. An editor's agentic-coding benchmark by rung, low to max: balanced 35.8% to 55.5% "
       "at $0.37 to $7.05 per task; small fast 30.9% to 48.4% at $0.08 to $1.12. Terminal tasks at max: balanced 64%, small fast 33%. "
       "A full evaluation suite at max: balanced 67.04% at $21.34 per test, small fast 54.44% at $3.00. On 13 hard known-bug "
       "code-review cases the balanced model caught 6, against 8 and 10 for the strong lower-cost model in the reviewer's standard and "
       "higher-effort configurations. In six agentic coding tasks graded by a judge model (noise about 3 points), the strong lower-cost "
       "model at medium scored 85% at $2.71 per task, the balanced model at high 82% at $1.19 and the small fast model at high 79% at "
       "$0.62. In 182 graded subagent runs (exploring a codebase, fixing a named test, lint, commit messages, a small feature, a diff "
       "review and an architecture summary) the small fast model passed 70 of 70 at low and at medium; as a codebase-exploration "
       "subagent at medium it took 24.7 seconds and $0.016 against 36.8 seconds and $0.621 for the strong lower-cost model. Output "
       "speed at max: small fast 237 and balanced 141 tokens per second. The vendor describes the small fast model as built for "
       "classification, routing, extraction and subagent tasks, with the larger models better for complex agentic coding, and the "
       "balanced model as strongest at well-scoped everyday tasks, bug fixing and documents.")
m["instructions"]["tradeoff"] = PREFIX + m6["instructions"]["tradeoff"] + NEW


def rename(s):
    s = s.replace("the strong and balanced models", "the strong lower-cost and balanced models")
    return s.replace("the strong model", "the strong lower-cost model")


for key in ("balanced_model", "small_fast_model"):
    src = v8["questions"]["model"]["criteria"][key]
    m["criteria"][key] = {f: ([rename(e) for e in src[f]] if f == "examples" else rename(src[f])) for f in src}

# v6's question, tradeoff text and two options are unchanged; only the prefix and the appended paragraph are new.
assert m["instructions"]["question"] == m6["instructions"]["question"]
assert m["instructions"]["tradeoff"] == PREFIX + m6["instructions"]["tradeoff"] + NEW
for key in ("most_capable_model", "strong_lower_cost_model"):
    assert m["criteria"][key] == m6["criteria"][key]
assert list(m["criteria"]) == ["most_capable_model", "strong_lower_cost_model", "balanced_model", "small_fast_model"]
assert v82["questions"]["effort"] == v6["questions"]["effort"]
txt = json.dumps(m["criteria"]["balanced_model"]) + json.dumps(m["criteria"]["small_fast_model"]) + NEW
assert "the strong model" not in txt and "strong lower-cost" in txt
for name in ("Fable", "Opus", "Sonnet", "Haiku", "Claude", "Anthropic"):
    assert name not in json.dumps(v82), name
OUT.write_text(json.dumps(v82, indent=1, ensure_ascii=False) + "\n")
print("built", OUT)
