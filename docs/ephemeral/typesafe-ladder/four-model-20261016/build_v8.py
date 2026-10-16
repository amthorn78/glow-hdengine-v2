"""Build request-v8.json from request-v6.json and request-hd-v3.json from request-hd-v1.json.

The effort Score (six rungs: low, medium, high, extra high, max, ultracode) is copied unchanged,
and the build asserts that it is identical, so every rung reading stays comparable with v6 and
hd-v1. Only the model Choice changes: it gains two options and its texts are rewritten from the
evidence verified on 2026-10-16 (evidence-20261016.md beside this file). No product names appear
in either request.

usage: python3 build_v8.py request-v6.json request-hd-v1.json OUT_DIR
"""
import copy, json, sys
from pathlib import Path

V6, HD1, OUT = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
KEYS = ["most_capable_model", "strong_model", "balanced_model", "small_fast_model"]

# ---------------------------------------------------------------- v8 (Glow app sessions)
V8_MODEL = {
    "type": "choice",
    "instructions": {
        "question": "Which model should run the AI coding session described in `action`, at whatever rung it needs?",
        "tradeoff": (
            "Four models share the same six rungs. List prices per million input and output tokens: the most capable model $10 and $50; "
            "the strong model $4 and $20; the balanced model $2 and $10; the small fast model $0.10 and $0.50 for prompts up to 100,000 tokens "
            "($0.50 and $2.50 above). Independent index by rung, low to max, with cost per task: small fast 29, 34, 38, 41, 43 at $0.02, $0.05, "
            "$0.08, $0.12, $0.21; balanced 36, 41, 47, 52, 56 at $0.35, $0.48, $0.88, $2.01, $5.46; strong 42, 51, 54, 56, 58 at $0.55, $1.34, "
            "$1.82, $3.46, $5.98; most capable 47, 49, 51, 53, 53 at $2.37, $2.98, $3.91, $5.98, $7.63. An editor's agentic-coding benchmark by rung, "
            "low to max: small fast 30.9% to 48.4% at $0.08 to $1.12 per task; balanced 35.8% to 55.5% at $0.37 to $7.05; strong 43.7% to 57.8% at "
            "$1.17 to $13.43; most capable 45.1% to 51.8% at $5.44 to $17.28. Terminal tasks at max: balanced 64%, strong 60%, most capable 52%, "
            "small fast 33%. A multimodal repository-repair benchmark: strong 70.2%, most capable 61.3%, balanced 58.3%, small fast 44.0%. A full "
            "evaluation suite at max: balanced 67.04% at $21.34 per test, strong 66.97% at $32.14, most capable 65.83% at $28.71, small fast 54.44% "
            "at $3.00. On 13 hard known-bug code-review cases the balanced model caught 6, and the strong model 8 in the reviewer's standard "
            "configuration and 10 in its higher-effort one. In six agentic coding tasks "
            "graded by a judge model (noise about 3 points), the strong model at medium scored 85% at $2.71 per task, the balanced model at high 82% at $1.19 and the small "
            "fast model at high 79% at $0.62. In 182 graded subagent runs (exploring a codebase, fixing a named test, lint, commit messages, a small "
            "feature, a diff review and an architecture summary) the small fast model passed 70 of 70 at low and at medium; as a codebase-exploration subagent at medium it took 24.7 seconds "
            "and $0.016 against 36.8 seconds and $0.621 for the strong model. Output speed at max: small fast 237, balanced 141, strong 97 and most "
            "capable 71 tokens per second. The vendor describes the small fast model as built for classification, routing, extraction and subagent "
            "tasks, with the strong and balanced models better for complex agentic coding, and the balanced model as strongest at well-scoped "
            "everyday tasks, bug fixing and documents. Between the two larger models: in a 179-task coding benchmark (effort unstated, harness "
            "versions differed) the strong model cost $116 against $672 with a median of 2.2 against 7.2 minutes per task, but passed 68.7% against "
            "87.2% of functional tests with 51 confirmed memorisation shortcuts against 17; in a controlled orchestration benchmark at high, the most "
            "capable model as orchestrator cost 1.9 to 3.0 times more for the same 4 of 4 tickets on a 35,000-line project and scored lower in blind "
            "review than the strong model alone. On subscription "
            "plans the most capable model draws on a 50% cap of weekly limits."
        ),
    },
    "criteria": {
        "most_capable_model": {
            "what": ("Work where even a strong model often falls short and a miss is costly or would pass unnoticed: demanding reasoning; long "
                     "autonomous work with several dependent phases; open-ended diagnosis where the cause is not yet known; designing and building a new "
                     "system with many interacting parts; the first independent review of a large new system, or of a large change that adds new "
                     "architecture, new components, new provider products or a new guard whose scope later work relies on, whose verdicts the next "
                     "phases build on; the first run of new code against a live external service with a real secret; or work on which the strong model "
                     "at a higher rung has already fallen short."),
            "not_for": ("Work whose task list is already written and on which the strong model largely succeeds: applying named fixes, reviewing a "
                        "correction pass against the findings it claims to fix, checking results against a list, even when the code is large or "
                        "security-sensitive; there 2.5 times the strong model's price and its slower turns buy little, and on an independent index "
                        "the strong model at high already outscores this one at max."),
            "examples": [
                "Find why a background job intermittently loses data after two earlier fixes failed",
                "Build a new payment integration and run it against the provider's sandbox for the first time",
                "First security review of a new 10,000-line service that later phases will build on",
            ],
        },
        "strong_model": {
            "what": ("Well-specified agentic coding and code review where a miss would reach a merge, a live system or later work: long-running "
                     "coding sessions on a known task list across a large or security-sensitive codebase, applying named fixes each with a test "
                     "there, reviewing a correction pass against the findings it claims to fix, the exact-head review that gates a merge, a repeat "
                     "review of a component already reviewed once. Independent measurements put it first of the four on the general index at max and on a "
                     "multimodal repository-repair benchmark, and in one reviewer's tests it caught 8 and 10 of 13 hard known bugs (standard and "
                     "higher-effort configurations) where the balanced model caught 6."),
            "not_for": ("Open-ended diagnosis or design, the first review of a large new system or of a large change that adds new components, "
                        "products or guards whose verdicts others build on, long work with several dependent phases that includes a first live run "
                        "of new code, or work on which this model at a higher rung has already fallen short; and bounded, low-stakes or mechanical "
                        "steps that the balanced or small fast model completes at a half or a fortieth of the price per token."),
            "examples": [
                "Fix five review findings that each name a file and a defect, adding a test for each",
                "Review a correction pass against the findings it says it fixed",
                "Run the exact-head code and security review that gates the merge of an already-reviewed component",
            ],
        },
        "balanced_model": {
            "what": ("Well-scoped everyday coding and document work where the existing tests or a later review still catch a miss and little rests "
                     "on this session alone: fixing a bug named in an issue in code of moderate size, a bounded feature built from a written "
                     "specification, filling a template, summarising results, writing or updating documents and handoff notes. On independent "
                     "measurements at max it matches or leads the strong model on a full evaluation suite, long-horizon office deliverables and "
                     "terminal tasks, at half the price per token and about 1.5 times the output speed."),
            "not_for": ("Reviews whose verdict gates the merge of large or security-sensitive code, where it caught 6 of 13 hard known bugs against "
                        "8 and 10 for the strong model; first reviews or first live runs whose results later work builds on; open-ended diagnosis or "
                        "design; long work with several dependent phases; or work on which this model has already fallen short."),
            "examples": [
                "Fix a reported crash in one module when the issue names the input that triggers it, adding a regression test",
                "Write the changelog entry and update the setup guide for a feature that has already been reviewed and merged",
                "Implement a small settings screen from an approved specification, with the usual review to follow",
            ],
        },
        "small_fast_model": {
            "what": ("Narrowly scoped, mechanical or high-volume steps on which nothing later rests, including subagent steps whose output a parent "
                     "session checks: recording given answers, relaying a message, running a named command and reporting its output, searching or "
                     "exploring a codebase and returning locations, sorting, routing or extracting items into given categories, lint fixes and "
                     "commit messages. The vendor builds it for classification, routing, extraction and subagent tasks; in 182 graded subagent runs "
                     "it passed 70 of 70 at low and at medium, and it generates output about 1.7 times as fast as the balanced model at a twentieth "
                     "of its price per token."),
            "not_for": ("Agentic coding beyond a narrow checked step, code review, diagnosis, design, first reviews or live runs, or any work whose "
                        "miss reaches a merge or later phases: on terminal tasks at max it scores 33% against 60% and 64% for the strong and "
                        "balanced models, and on a full evaluation suite 54.44% against about 67%."),
            "examples": [
                "As a subagent, return the paths of every test file that mentions a named fixture, for the parent session to read",
                "Sort 400 log lines into the five error categories the parent session supplied",
                "Write the commit message for a diff that has already been reviewed",
            ],
        },
    },
}

# ---------------------------------------------------------------- hd-v3 (Human Design jobs)
HD3_MODEL = {
    "type": "choice",
    "instructions": {
        "question": "Which model should run the Human Design report-production job described in `action`, at whatever rung it needs?",
        "tradeoff": (
            "Four models share the same six rungs. List prices per million input and output tokens: the most capable model $10 and $50; the strong "
            "model $4 and $20; the balanced model $2 and $10; the small fast model $0.10 and $0.50 for prompts up to 100,000 tokens ($0.50 and $2.50 "
            "above). Output speed at max: small fast 237, balanced 141, strong 97 and most capable 71 tokens per second. On an independent "
            "knowledge-work evaluation (blind-graded professional tasks, Elo) by rung, low to max: small fast 1123, 1275, 1418, 1513, 1618 at $0.01 to "
            "$0.22 per task; balanced 1175, 1323, 1549, 1728, 1838 at $0.21 to $6.84; strong 1235, 1584, 1704, 1831, 1866, $8.92 at max; most capable "
            "1469, 1545, 1635, 1732, 1754, $9.77 at max. Office deliverables at max: balanced 1817, strong 1803, most capable 1672, small fast 1577; at "
            "medium: strong 1625, most capable 1528, balanced 1441, small fast 1372. Reading long documents: 85% for the most capable and strong "
            "models and 83% for the balanced and small fast models at max. On a closed-book knowledge test at max, the share of unknown answers given "
            "wrongly instead of declined: small fast 40%, balanced 47%, strong 59%, most capable 73%. Legal deliverables from case files with every "
            "criterion met and no material hallucination, at max: most capable 6.4%, strong 4.2%, balanced 2.8%, small fast 0.6%; material "
            "hallucinations per deliverable: strong 0.59, balanced 1.03, most capable 1.32, small fast 1.61. Legal research: most capable 55.3%, "
            "strong 50.5%, balanced 48.1%, small fast 43.3%; tax work 49.2%, 45.6%, 42.0%, 31.9%. In one practitioner test of drafting a 1,000- to "
            "1,300-word article from a supplied brief, three drafts each at their default levels, 2 of 3 drafts by the balanced model added claims "
            "the brief did not supply, against 0 of 3 by the strong model. Between the two larger models, writing quality is close: the most capable model leads a judged creative-writing test "
            "(2162 against 2050) and a long-form test (85.3 against 84.6, neither degrading over eight chapters), while the strong model leads crowd "
            "votes on creative writing, long queries and instruction following (1516 against 1482, 1526 against 1510, 1517 against 1498); the most "
            "capable model leads on single-pass expert writing from supplied source documents (73.8 against 65.8). Reviewers found the most capable "
            "model stayed faithful to source material but overran explicit length limits, and the strong model, as an editor, sometimes produced a "
            "revision that ignored its own diagnosis. The vendor describes the small fast model as built for classification, routing, extraction and "
            "subagent tasks, and the balanced model as strongest at well-scoped everyday tasks and documents."
        ),
    },
    "criteria": {
        "most_capable_model": {
            "what": ("Work where the depth of one pass of expert synthesis from source material decides the outcome and later work builds on it: "
                     "the first report of a new type, template or prompt version on this platform; a two-person composite whose relationship "
                     "mechanics must be reconciled across both charts when that report type has not been produced here before; interpretation that "
                     "weighs conflicting statements across several reference works where no later check can judge it; a client's open questions "
                     "whose framing is not given; or work on which the strong model at a higher rung has already fallen short."),
            "not_for": ("Work on an accepted template and accepted inputs with acceptance and QA behind it, or work with a written checklist or "
                        "named defects: standard readings and composites of a type already produced here, repairs of named defects, checks of a "
                        "published document against its source, controller steps that run written scripts, recording and filing. There 2.5 times "
                        "the strong model's price and slower turns buy little, and on independent knowledge-work evaluations the strong model at "
                        "extra high already outscores this one at max."),
            "examples": [
                "Write the first parent-child composite report produced on this platform, for a paying client, from a complete packet",
                "Reconcile two reference works that disagree about a gate's meaning before a report section is written",
                "Rewrite a report section after two repairs by the strong model failed acceptance",
            ],
        },
        "strong_model": {
            "what": ("Long client-facing report work on an accepted template, with acceptance and QA behind it: drafting a standard single-person "
                     "reading, or a composite of a type already produced here, from a complete packet; repairing defects named at acceptance and "
                     "reviewing such a repair; a production controller run with live chart and geocoding calls. It leads the four on blind-graded "
                     "professional tasks at max (1866) and has the fewest material hallucinations per legal deliverable (0.59 against 1.03 to 1.61), "
                     "and in one brief-following test it added no unsupplied claims where the balanced model did in 2 of 3 drafts."),
            "not_for": ("The first report of a new type or template whose structure later reports copy, open-ended interpretation where no later "
                        "check can catch an error, or work on which this model at a higher rung has already fallen short; and short checked steps, "
                        "records, summaries and comparisons that the balanced or small fast model completes at a half or a fortieth of the price "
                        "per token."),
            "examples": [
                "Write a standard single-person reading for a returning client on the accepted template",
                "Fix four acceptance defects that each name a section and the failed requirement",
                "Run the controller for a routine request of three reports on accepted templates",
            ],
        },
        "balanced_model": {
            "what": ("Bounded document work with a checklist or a deterministic check behind it, where a miss is caught before a client reads it: "
                     "comparing a published document against its source with a written checklist, summarising a run's results for the run log, "
                     "filling template fields from accepted data, drafting run notes or a short internal summary. It is level with the strong model "
                     "on office deliverables (1817 against 1803 at max) and close on reading long documents (83% against 85%), at half the price per "
                     "token and about 1.5 times the output speed."),
            "not_for": ("Writing a full client reading or composite whose statements a client reads and acts on, a first report of any type, "
                        "interpretation from conflicting sources, or repairs whose evidence must be weighed: in a brief-following test 2 of 3 of its "
                        "drafts added claims the brief did not supply, against none for the strong model."),
            "examples": [
                "List every difference between a published Google Doc and its accepted Markdown source, using the formatting checklist",
                "Write the run log entry for a completed production run from its acceptance and QA records",
                "Fill the report header fields from the accepted client intake record",
            ],
        },
        "small_fast_model": {
            "what": ("Mechanical, high-volume or extraction steps on which nothing later rests: recording a delivery date or a link, filing, "
                     "renaming files, relaying a message, running a named script, copying fields from chart data into a table that a deterministic "
                     "check then compares, sorting or routing requests into given categories. The vendor builds it for classification, routing, "
                     "extraction and subagent tasks, at a twentieth of the balanced model's price per token and about 1.7 times its output speed."),
            "not_for": ("Writing, repairing or reviewing any client-facing text, interpretation, checking a report's claims, or any controller step "
                        "with live calls: on blind-graded professional tasks it scores 1618 at max against 1838 to 1866 for the balanced and strong "
                        "models, and its legal deliverables averaged 1.61 material hallucinations each against 0.59 for the strong model."),
            "examples": [
                "File an accepted report's Google Doc link on the client's Notion page",
                "Sort this week's intake requests into the four report types the intake form defines",
                "Rename a run's output files to the naming convention in the run plan",
            ],
        },
    },
}


def build(src, model_q):
    old = json.loads(src.read_text())
    new = copy.deepcopy(old)
    assert set(old["questions"]) == {"effort", "model"}, sorted(old["questions"])
    assert len(old["questions"]["effort"]["criteria"]) == 6 and old["questions"]["effort"]["criteria"][5].startswith("ultracode:")
    new["questions"]["model"] = model_q
    assert new["questions"]["effort"] == old["questions"]["effort"], "the effort Score must be unchanged"
    assert list(new["questions"]["model"]["criteria"]) == KEYS
    for name in ("Fable", "Opus", "Sonnet", "Haiku", "Claude", "Anthropic"):
        assert name not in json.dumps(new), f"product name {name} in the request"
    return new


def write(obj, path):
    path.write_text(json.dumps(obj, indent=1, ensure_ascii=False) + "\n")


OUT.mkdir(parents=True, exist_ok=True)
write(build(V6, V8_MODEL), OUT / "request-v8.json")
write(build(HD1, HD3_MODEL), OUT / "request-hd-v3.json")
print("built", OUT / "request-v8.json", OUT / "request-hd-v3.json")
