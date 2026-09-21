#!/usr/bin/env python3
"""Propose a typed `pf10_dependency` for every state_routes row, for Product Owner review.

    classify.py --contract <direct-handoff-contract.json> --out <dir> [--limit N]

WHY THIS EXISTS.  Option A in the round-20 decision briefs cannot be called a D14-acceptable
guard while the property that selects which branches the rule governs -- whether a condition
compares PF10 against an addendum-derived expectation -- lives only in free-text `condition`.
Review said so, correctly, and a paraphrase evades any vocabulary selector.  A typed enum on
each row fixes that, and this script proposes the enum's values.

WHAT THIS IS NOT.  The model does a one-time reading task.  It is NOT the guard: nothing here
lands in a contract, gates anything, or counts as D14 coverage.  The sequence is
    classify (here) -> Product Owner review -> the approved enum lands as a typed field
    -> the guard is thereafter a plain deterministic enum check, with no model and no network.
A probabilistic classifier could not be the guard and is not offered as one.

PRE-REGISTERED BEFORE THE RUN, because the measured record for this screen says both of its
past failures were the QUESTION rather than the answer, and that controls embedded in the
production run are what made its output interpretable:
  * the four options and their rubrics, below, fixed;
  * three confidence bands, not two -- the uncertain band caught the true case the flag
    threshold missed in both earlier validation runs;
  * CLEAR >= 0.80, UNCERTAIN 0.50-0.80, UNRESOLVED < 0.50;
  * eight synthetic controls with known labels, two per class, with two carried in EVERY batch,
    so no batch's output is interpretable only by assuming the instrument worked;
  * ONE revision to the rubric, made after a 20-row validation batch and before the full run, and
    recorded rather than quietly applied: five rows came back UNRESOLVED on conditions reading
    "missing source, authority, or review mode", because `SOURCE_AVAILABILITY` did not say it meant
    PF10 specifically while this contract uses a bare "source" for the change's own artifact.  That
    is an under-specified option of mine, statable without reference to which answers I preferred.
    The validation batch is VOID and is not carried into the proposal; the full run below is the
    only run recorded.  No further revision was made after seeing results.
  * a lexical selector run alongside and reported as a union, because the same record shows the
    screen catches paraphrase that regex cannot and misses terse literal forms that regex
    catches trivially.  Neither mechanism covers both.
"""
import argparse
import collections
import hashlib
import json
import pathlib
import sys
import urllib.request

sys.dont_write_bytecode = True

ENDPOINT = "https://api.typesafe.ai/v1/systemone"
MODEL = "jev-latest"
BATCH = 20
CLEAR, UNCERTAIN = 0.80, 0.50

OPTIONS = {
    "NONE": "The condition does not involve PF10, HDE Build Notes or any addendum to them at all. "
            "This INCLUDES a condition whose only blocker is a generic source, authority, identity, "
            "owner or review-mode problem that does not name PF10, Build Notes or an addendum -- in "
            "this contract's vocabulary a bare 'source' means the change's own source artifact, not "
            "the governing document.",
    "READ_ONLY": "PF10, Build Notes or an addendum is read, cited, or required to be present, and "
                 "nothing is compared against it. Includes a prohibition on acting outside it.",
    "SOURCE_AVAILABILITY": "The outcome turns on PF10, Build Notes or an addendum SPECIFICALLY being "
                           "unresolvable, unavailable, ambiguous or unreadable -- that governing "
                           "document cannot be obtained, so no comparison happens. A generic "
                           "source/authority blocker that does not name it is NONE, not this.",
    "COMPARISON": "PF10, Build Notes or an addendum is compared against some other expectation, "
                  "version or derived statement, and a DIFFERENCE between them decides the "
                  "outcome. Includes any paraphrase of 'check the current text against the "
                  "approved one and act on the mismatch'.",
}
INSTRUCTIONS = ("Classify how the routing condition in `condition` depends on the governing source "
                "document PF10 (also called HDE Build Notes, together with its addenda). Judge only "
                "the dependency on that source, not whether the branch is terminal and not whether "
                "the condition is reasonable.")

# Known labels, written to be answerable from the text alone.  Two are deliberate paraphrases with
# no shared vocabulary, since paraphrase evasion is the whole reason a typed field is needed.
CONTROLS = [
    ("ctl_cmp_literal", "COMPARISON",
     "compare the current controlled PF10 Markdown against the approved addendum and stop on any mismatch"),
    ("ctl_cmp_para", "COMPARISON",
     "the specification has drifted from the appendix ratified by the Product Owner; hold the change until the divergence is reconciled"),
    ("ctl_src_literal", "SOURCE_AVAILABILITY",
     "the unique current controlled PF10 Markdown cannot be resolved; make no inference from the failure"),
    ("ctl_src_para", "SOURCE_AVAILABILITY",
     "the governing build note could not be retrieved at all, so no determination is possible"),
    ("ctl_ro_literal", "READ_ONLY",
     "cite PF10 by title and section only; never invent an approval or bypass its controls"),
    ("ctl_ro_para", "READ_ONLY",
     "the governing note must be present and quoted in the handoff, and nothing in it may be restated as a decision"),
    ("ctl_none_1", "NONE",
     "valid CRD class selection and complete sanitized source"),
    ("ctl_none_2", "NONE",
     "a true completed-cycle or Product Owner terminal return"),
]

# The blocking states the decision briefs enumerate alongside the terminal rows.  Recorded in the
# artifact so the "terminal or blocking" claim is auditable from the output rather than from prose.
BLOCKING_STATES = {"BLOCKED", "AWAITING_THOTH_REMEDIATION", "RESCOPE_PROPOSAL_PENDING_REVIEW",
                   "PLAN_PENDING_REVISED", "AWAITING_PO_PROCEED"}

# The complementary lexical selector: names the source, AND comparison language.  Deliberately the
# kind of selector the briefs call a vocabulary filter -- it is reported beside the screen, not
# trusted alone.
SOURCE_WORDS = ("pf10", "build note", "addendum", "addenda", "appendix")
COMPARE_WORDS = ("compare", "comparison", "mismatch", "differ", "difference", "divergen",
                 "drift", "discrepan", "reconcile", "against the approved", "inconsisten")


def lexical(text: str) -> str:
    low = text.lower()
    named = any(w in low for w in SOURCE_WORDS)
    compared = any(w in low for w in COMPARE_WORDS)
    if named and compared:
        return "COMPARISON"
    if named:
        return "NAMES_SOURCE"
    return "NO_MATCH"


def ask(state: dict, questions: dict) -> dict:
    body = json.dumps({"state": state, "model": MODEL, "questions": questions}).encode()
    req = urllib.request.Request(ENDPOINT, data=body,
                                 headers={"Content-Type": "application/json"})
    # No Authorization header: the credential is attached by the environment's proxy after the
    # request leaves this machine, and must never enter it.
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.loads(r.read())


def band(conf: float) -> str:
    return "CLEAR" if conf >= CLEAR else ("UNCERTAIN" if conf >= UNCERTAIN else "UNRESOLVED")


def rows_of(contract: pathlib.Path) -> list[dict]:
    sr = json.loads(contract.read_text(encoding="utf-8"))["state_routes"]
    out = []
    for prompt, lst in sorted(sr.items()):
        for r in lst:
            out.append({"id": f"{prompt}__{r['branch_id']}", "prompt": prompt,
                        "branch_id": r["branch_id"], "condition": r.get("condition") or "",
                        "terminal": bool(r.get("terminal_for_invocation")),
                        "state": r.get("state")})
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--contract", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    rows = rows_of(pathlib.Path(args.contract))
    if args.limit:
        rows = rows[:args.limit]
    out_dir = pathlib.Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    results, control_results, usage = {}, [], collections.Counter()
    served: set[str] = set()
    subjects = [(r["id"], r["condition"]) for r in rows]
    for i in range(0, len(subjects), BATCH):
        chunk = subjects[i:i + BATCH]
        # Two controls per batch, rotating, so every batch carries its own evidence that the
        # instrument answered as specified on cases whose labels are known.
        ctl = [CONTROLS[(i // BATCH * 2 + k) % len(CONTROLS)] for k in (0, 1)]
        state, questions = {}, {}
        for key, text in chunk + [(c[0], c[2]) for c in ctl]:
            state[key] = {"condition": text}
            questions[key] = {"type": "choice",
                              "instructions": {"question": INSTRUCTIONS,
                                               "condition": f"`{key}.condition`"},
                              "criteria": OPTIONS}
        resp = ask(state, questions)
        # The response must answer EXACTLY what was asked.  Accepting only the keys that came
        # back meant an omitted subject or control was silently dropped: `controls_total` was
        # computed from what arrived, so a missing control read as "27/27 correct" while the
        # renderer still called the reduced set "every state_routes row".  A harness reporting
        # success over fewer subjects than it claimed.
        want_keys, got_keys = set(questions), set(resp["answers"])
        if want_keys != got_keys:
            raise SystemExit(
                f"batch {i // BATCH + 1} did not answer what was asked: "
                f"{len(want_keys - got_keys)} missing {sorted(want_keys - got_keys)[:5]}, "
                f"{len(got_keys - want_keys)} unexpected {sorted(got_keys - want_keys)[:5]}")
        # The SERVED model is observed, not assumed.  It was never captured, and the renderer
        # supplied `jev-1.13.0` as a hard-coded default -- publishing an identity nothing had
        # read, for a run made against the `jev-latest` alias which can resolve elsewhere.
        served.add(resp["model"])
        for k, v in resp["usage"].items():
            if isinstance(v, int):
                usage[k] += v
        for key, ans in resp["answers"].items():
            rec = {"choice": ans["choice"], "confidence": ans["confidence"],
                   "band": band(ans["confidence"]), "probabilities": ans["probabilities"]}
            known = dict((c[0], c[1]) for c in CONTROLS).get(key)
            if known is not None:
                control_results.append({"id": key, "expected": known, **rec,
                                        "correct": ans["choice"] == known})
            else:
                results[key] = rec
        print(f"batch {i // BATCH + 1}: {len(chunk)} rows + 2 controls", file=sys.stderr)

    if len(served) != 1:
        raise SystemExit(f"the batches were served by {len(served)} different models "
                         f"({sorted(served)}); a single proposal cannot claim one provenance")

    by_id = {r["id"]: r for r in rows}
    for key, rec in results.items():
        rec["lexical"] = lexical(by_id[key]["condition"])
        rec["prompt"] = by_id[key]["prompt"]
        rec["branch_id"] = by_id[key]["branch_id"]
        rec["terminal"] = by_id[key]["terminal"]
        # `state` is PERSISTED.  The proposal's central claim is about rows that are terminal OR
        # in a blocking state, and the enrichment dropped the state it had already read -- so a
        # reviewer could not audit whether a candidate was BLOCKED.  A conclusion whose evidence
        # was computed and then discarded.
        rec["state"] = by_id[key]["state"]
        rec["condition"] = by_id[key]["condition"]

    payload = {
        "artifact_type": "PF10_DEPENDENCY_PROPOSAL",
        "status": "PROPOSAL_FOR_PRODUCT_OWNER_REVIEW",
        "nonclaims": [
            "Not a landed contract field. Not a guard. Not D14 coverage.",
            "No QA verdict, acceptance, PF09 movement, OPS or closure is claimed.",
            "The model performed a one-time reading task; the guard that would follow is a "
            "deterministic enum check with no model and no network.",
        ],
        "model_requested": MODEL,
        "model_served": sorted(served)[0],
        # The external input's exact identity, so a reviewer can tell whether the contract this
        # was classified from is the contract they are holding.
        "contract": {"path": str(args.contract),
                     "sha256": hashlib.sha256(
                         pathlib.Path(args.contract).read_bytes()).hexdigest()},
        "blocking_states": sorted(BLOCKING_STATES),
        "pre_registered": {"options": sorted(OPTIONS), "clear_at": CLEAR,
                           "uncertain_at": UNCERTAIN, "batch": BATCH,
                           "controls": len(CONTROLS), "controls_per_batch": 2},
        "rows_classified": len(results),
        "controls": control_results,
        "controls_correct": sum(1 for c in control_results if c["correct"]),
        "controls_total": len(control_results),
        "usage": dict(usage),
        "results": results,
    }
    (out_dir / "pf10_dependency.proposal.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")

    tally = collections.Counter(r["choice"] for r in results.values())
    bands = collections.Counter(r["band"] for r in results.values())
    print(f"\nrows: {len(results)}  controls: {payload['controls_correct']}/{payload['controls_total']}")
    print(f"labels: {dict(tally)}")
    print(f"bands:  {dict(bands)}")
    print(f"usage:  {dict(usage)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
