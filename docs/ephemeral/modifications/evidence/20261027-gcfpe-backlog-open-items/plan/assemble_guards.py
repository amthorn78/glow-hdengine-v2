#!/usr/bin/env python3
"""Assemble plan/guards.json for MODIFICATION-20261027-gcfpe-backlog-open-items (MODE = PLAN, assembly A1).

Merges every design worker's guards (plan/work/W1, W2, W3a, W3b, W4, W5, W6, W7, W8 .json) into the precedent's
guards.json format, with the coordinator's amendments (plan/coordinator-decisions.md):

  C-5 Q-1  W3b's named exceptions to G-HP-2 and G-HP-5 are adopted: where W3a and W3b both carry a guard id, W3b's
           text is kept (it is W3a's with those exceptions added) and the prompt lists are united; one entry per id.
  C-5 Q-3  G-HP-6 runs on every member of the successor release and PE.
  C-5 Q-4  PE's 'Run state, recovery, and completion' sentence is a named exception (already in W3b's G-HP-2, G-HP-5).
  C-5 Q-5  OPS-30 joins G-HP-R3.
  C-5 Q-6  every pattern is escape-tolerant for Notion's rendered underscore: an underscore in a pattern matches
           "\\?_" (an optional backslash, then the underscore), and an underscore inside a character class admits a
           backslash too. The worker's own pattern is kept beside it as `source_all` / `source_except`.
  C-8 Q1   QA-10's two EH-1 sentences join PART-10: QA-10 is in G-W4-10-5 already; the presence half is a QA-10
           entry of the same rule (G-W4-10-4-QA10), expecting the two sentences W4's ops write there.

Repair R1 (coordinator decisions C-15, C-16, C-17, C-22):

  C-15     one text form for every check: body_check.py runs every guard on normalize_fetch.normalize(read), so every
           pattern is re-expressed for the Markdown form by translation, never retyped (markdown_form below):
           `<code>` and `</code>` become a backtick, `<b>` and `</b>` become `\\*\\*`, `<i>` and `</i>` become
           `\\*`. The worker's own pattern stays in `source_all` / `source_except`. The C-5 Q-6 escape-tolerance rewrite
           is kept: it is unnecessary once `\\_` is normalized, and harmless (`\\\\?_` still matches `_`).
  C-16     the A5 failing rows judged by PART-07's test: a conforming line gets a named exception, with its reason, from
           C16_EXCEPTIONS below; a contradicting line gets a PART-07 operation in assemble_edits.py (set "C16").
  C-17     G-W2-BC-7 follows PR-20's reworded W2-PR-20-BC-1 ("as the PR Instruction states it").
  C-22     CL-05 joins G-HP-1 to G-HP-5.

Repair of PLAN review round 1 (coordinator decision C-24):

  C-24     L-C1 is an accepted risk (D26-A rule 4), so IA-30's delta-review guards return to the frozen cut of ITEM-14
           and ITEM-15, "every work unit a material Plan delta adds or changes": G-W2-EM-2 is cut by work unit, and
           G-W2-BC-4 follows W2-IA-30-BC-2, which loses its "including a unit whose acceptance criterion or outcome
           ..." clause (C24_GUARDS below; the operations' texts are assemble_edits.py's C24_OVERRIDES).

G-W7-BIND-1 and G-W8-NAME-1 are kept as the workers wrote them and marked `regenerate`: body_check.py replaces their
patterns with the ones binding_pass.py derives from the successor map (W7-D8). Guards on surfaces that are not
prompt bodies (the Hub, the register, repository files) are merged with `surface` set; body_check runs a guard only
on a page entry of edits.json, and the fixture self-test runs every guard.

  PYTHONDONTWRITEBYTECODE=1 python3 assemble_guards.py          write guards.json beside this file
  PYTHONDONTWRITEBYTECODE=1 python3 assemble_guards.py --check  rebuild in memory and compare
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
sys.path.insert(0, str(HERE))
from normalize_fetch import normalize  # noqa: E402
WORK = HERE / "work"
WORKERS = ["W1", "W2", "W3a", "W3b", "W4", "W5", "W6", "W7", "W8"]
CORE = ("id", "part", "rule", "kind", "expect", "unit", "prompts", "all", "except", "fixtures")


# A word boundary that reads Notion's escaped underscore as part of the word, as an unescaped underscore is:
# "NOT\\_READY" has no boundary after "NOT", just as "NOT_READY" has none. A position is word-like when it holds a
# word character or the backslash of "\\_".
BOUNDARY = (r"(?:(?:(?<=\w)|(?<=\\)(?=_))(?!\w|\\_)|(?<!\w)(?:(?<!\\)|(?!_))(?=\w|\\_))")


def escape_tolerant(p: str) -> str:
    """Rewrite a regex so every literal underscore also matches Notion's escaped form `\\_`.

    Outside a character class, `\\b` becomes BOUNDARY, and `_` and `\\_` become `\\\\?_`; a pattern that already reads `\\\\?_` is left alone.
    Inside a class that admits `_`, a backslash is admitted too; a negated class is left as it is, since the
    backslash of `\\_` is not the excluded underscore. Everything else is copied unchanged."""
    out, i, n, in_class, class_has_us, class_has_bs, negated = [], 0, len(p), False, False, False, False
    while i < n:
        c = p[i]
        if c == "\\" and i + 1 < n:
            pair = p[i:i + 2]
            if pair == "\\\\" and p[i + 2:i + 4] == "?_" and not in_class:
                out.append("\\\\?_")
                i += 4
                continue
            if pair == "\\_" and not in_class:
                out.append("\\\\?_")
            elif pair == "\\b" and not in_class:
                out.append(BOUNDARY)
            else:
                out.append(pair)
                if in_class and pair == "\\_":
                    class_has_us = True
                if in_class and pair == "\\\\":
                    class_has_bs = True
            i += 2
            continue
        if in_class:
            if c == "]":
                if class_has_us and not class_has_bs and not negated:
                    out.append("\\\\")
                in_class = False
                out.append(c)
            else:
                if c == "_":
                    class_has_us = True
                out.append(c)
            i += 1
            continue
        if c == "[":
            in_class, class_has_us, class_has_bs = True, False, False
            negated = p[i + 1:i + 2] == "^"
            if negated:
                out.append("[^")
                i += 2
            else:
                out.append("[")
                i += 1
            if p[i:i + 1] == "]":  # a leading ] is literal
                out.append("]")
                i += 1
            continue
        out.append("\\\\?_" if c == "_" else c)
        i += 1
    return "".join(out)


# C-16 (repair R1): the conforming A5 failing rows, judged by PART-07's stated test (scope-measurement.md section 2;
# D23-B; D27): a line that names artifacts by path, or speaks of something other than a handoff, gets a named exception
# with its reason. Each literal is the start of the line's sentence in the normalized (Markdown) form, so the exception
# is anchored and narrow; each carries a pass fixture (the excepted form) and a fail fixture (a contradicting sentence
# of the same opening that the exception must not mask), the injected-failure self-test of the exception.
C16_EXCEPTIONS = [
    {"guard": "G-HP-1", "prompts_seen": ["CL-C-10"],
     "literal": "Each runnable direct-native package names its destination, receiving role/name and exact "
                "task/artifact binding, and input artifacts by repository path; the artifacts hold the rest.",
     "why": "C-16, conforming: CL-C-10's package sentence names the destination, receiving role and input artifacts "
            "by repository path and leaves the rest to the artifacts, which is W3a's HP_PACKAGE form; 'direct-native' "
            "names the route, not a complete input package",
     "fail": "Each runnable direct-native package carries the complete native input package and its lineage."},
    {"guard": "G-HP-4", "prompts_seen": ["CL-C-10", "CL-E-10"],
     "literal": "Required tools, stores, environment and access limitations: Use only approved evidence stores, "
                "permitted read-only repository/environment evidence access and supplied manual permissions.",
     "why": "C-16, conforming: the field is in the prompt's own Inputs section and limits the closure prompt's own "
            "access; it is not a per-branch handoff field restating a destination prompt's tools (G-HP-4's rule, "
            "findings.md V2 second layer)",
     "fail": "Required tools, stores, environment and access limitations: preserve the destination's tools, recovery "
             "and terminal behavior."},
    {"guard": "G-HP-5", "prompts_seen": ["DOC-10"],
     "literal": "Preserve exact `CHANGE_CLASS`, `CHANGE_ID`, `DOCUMENTATION_UNIT_ID`, actual PR/Ops "
                "task/result/receipt lineage, repository baseline, producer/acceptance/operator/session identities,",
     "why": "C-16, conforming: DOC-10's own Required inputs; the documentation record keeps the actual producer, "
            "acceptance, operator and session identities as recorded facts (D23-A artifact content), and no handoff "
            "is told to carry them",
     "fail": "Preserve exact session identity and session continuity in the DOC-20 handoff."},
    {"guard": "G-HP-2", "prompts_seen": ["QA-110"],
     "literal": "Markdown at paths under `docs/ephemeral/` in the repository, commit and push them on the working "
                "branch,",
     "why": "C-16, conforming: storage rule (PF04 section 9.1.3; D23-A): the handoff is one of the artifacts written "
            "and committed on the working branch; it names the artifact store, not handoff content (as the existing "
            "'committed and pushed on the working branch' exception)",
     "pass": "Write the checkpoint and handoff as Markdown at paths under `docs/ephemeral/` in the repository, commit "
             "and push them on the working branch, preserve versions, and return their repository paths.",
     "fail": "Write the handoff so that it carries the working branch and head commit to QA-120."},
]


def _c16_exceptions(merged: dict, notes: list) -> None:
    for e in C16_EXCEPTIONS:
        g = merged[e["guard"]]
        lit = e["literal"]
        pat = ("^" if e["guard"] != "G-HP-2" else "") + re.escape(lit)
        g["except"] = list(g.get("except", [])) + [pat]
        g["except_why"] = list(g.get("except_why", [])) + [e["why"]]
        pass_fx = e.get("pass") or (lit if lit.endswith(".") else lit + " and the rest.")
        g["fixtures"] = dict(g["fixtures"], **{"pass": list(g["fixtures"]["pass"]) + [pass_fx],
                                               "fail": list(g["fixtures"]["fail"]) + [e["fail"]]})
        # body_check selftest removes this exception and requires the pass fixture to fail then (the exception is
        # what admits the line), and requires the fail fixture to fail with it (the exception is narrow)
        g["c16_exceptions"] = list(g.get("c16_exceptions", [])) + [
            {"except_index": len(g["except"]) - 1, "pass_fixture": pass_fx, "fail_fixture": e["fail"],
             "prompts_seen": e["prompts_seen"]}]
        notes.append(f"C-16: {e['guard']} named exception ({', '.join(e['prompts_seen'])})")


# C-24 (repair of PLAN review round 1, R-2): IA-30's delta-review guards, per work unit (ITEM-14, ITEM-15)
C24_GUARDS = {
    "G-W2-BC-4": {
        "rule": "PF04 §9.7.7 Gates in IA-30's material Plan-delta review, for every work unit the delta adds or changes (R-A1; ITEM-14)",
        "all": ["(?i)\\bfor every work unit the delta adds or changes, check its business case\\b"],
        "except": [],
        "fixtures": {"pass": ["For every work unit the delta adds or changes, check its business case as the initial Plan "
                              "review does, and deny the delta for a unit without one."],
                     "fail": ["Check the delta's affected dependencies, risks, exclusions, and conflicts.",
                              "For every acceptance criterion the delta adds or changes, check the business case of its "
                              "unit."]},
        "note": "C-24: follows W2-IA-30-BC-2 without the L-C1 clause (L-C1 is an accepted risk)"},
    "G-W2-EM-2": {
        "rule": "D30-A in IA-30's material Plan-delta review, for every work unit the delta adds or changes (ITEM-15)",
        "all": ["(?i)^For every work unit the delta adds or changes, an acceptance criterion that depends on emulating "
                "an external system\\b", "(?i)\\bground for this decision\\b"],
        "except": [],
        "fixtures": {"pass": ["- DELTA_DENY: return exact delta redlines to the same IA author through IA-40. For every "
                              "work unit the delta adds or changes, an acceptance criterion that depends on emulating an "
                              "external system is a ground for this decision; its redline asks for a pin or a stated "
                              "precondition instead."],
                     "fail": ["- DELTA_DENY: return exact delta redlines to the same IA author through IA-40. No addendum.",
                              "- DELTA_DENY: return exact delta redlines to the same IA author through IA-40. An "
                              "acceptance criterion the delta adds or changes that depends on emulating an external "
                              "system is a ground for this decision."]},
        "note": "C-24: cut by work unit (the frozen ITEM-15 reading); the acceptance-criterion cut of L-C1 is reverted"},
}


MARKUP_TO_MARKDOWN = (("</code>", "`"), ("<code>", "`"), ("</b>", "\\*\\*"), ("<b>", "\\*\\*"),
                      ("</i>", "\\*"), ("<i>", "\\*"))


def markdown_form(p: str) -> str:
    """C-15: a pattern written for the fetch's inline markup, translated to the normalized (Markdown) form. Only the
    four tag literals are mapped; every other character of the pattern is kept."""
    for old, new in MARKUP_TO_MARKDOWN:
        p = p.replace(old, new)
    return p


def _count(text: str, g: dict) -> int:
    """body_check.py's unit count on the normalized text (C-15), with the patterns in their Markdown form."""
    text = normalize(text)
    pats = [markdown_form(p) for p in g["all"]]
    exc = [markdown_form(p) for p in g.get("except", [])]
    units = text.split("\n") if g["unit"] == "line" else [s for ln in text.split("\n")
                                                          for s in re.split(r"(?<=[.!?])\s+", ln) if s]
    return sum(1 for u in units if all(re.search(p, u) for p in pats) and not any(re.search(p, u) for p in exc))


def surface(prompts: list) -> str:
    if any(p.startswith("repo:") for p in prompts):
        return "repository"
    if any(p in ("HUB", "REGISTER") for p in prompts):
        return "notion-control"
    return "prompt-body"


def build() -> dict:
    tsv = [l.split("\t")[0] for l in (HERE / "members-100926.1.tsv").read_text(encoding="utf-8").splitlines() if l.strip()]
    release_members = sorted(tsv + ["CL-05"])
    merged: dict = {}
    order: list = []
    for w in WORKERS:
        for g in json.loads((WORK / f"{w}.json").read_text(encoding="utf-8"))["guards"]:
            gid = g["id"]
            if gid in merged:
                prev = merged[gid]
                if w == "W3b" and prev["source"] == "W3a":  # C-5 Q-1: W3b's amended text, prompts united
                    prompts = sorted(set(prev["prompts"]) | set(g["prompts"]))
                    merged[gid] = dict(g, source="W3a+W3b (W3b's text, C-5 Q-1)", prompts=prompts)
                    continue
                raise SystemExit(f"duplicate guard id {gid} from {prev['source']} and {w}")
            merged[gid] = dict(g, source=w)
            order.append(gid)
    notes = []
    # C-5 Q-3: G-HP-6 on every member and PE
    merged["G-HP-6"]["prompts"] = release_members + ["PE"]
    notes.append("C-5 Q-3: G-HP-6 prompts = the 56 release members and PE")
    # C-5 Q-5: OPS-30 joins G-HP-R3
    merged["G-HP-R3"]["prompts"] = sorted(set(merged["G-HP-R3"]["prompts"]) | {"OPS-30"})
    notes.append("C-5 Q-5: G-HP-R3 gains OPS-30")
    # C-22: CL-05 joins G-HP-1 to G-HP-5 (W3b's prompt lists predate the CL-05 successor)
    for gid in ("G-HP-1", "G-HP-2", "G-HP-3", "G-HP-4", "G-HP-5"):
        merged[gid]["prompts"] = sorted(set(merged[gid]["prompts"]) | {"CL-05"})
    notes.append("C-22: CL-05 joins G-HP-1 to G-HP-5")
    # C-17: PR-20's W2-PR-20-BC-1 is reworded to "as the PR Instruction states it" (assemble_edits.py), and G-W2-BC-7
    # moves to match: the same substitution on its pattern and fixtures, so the guard still pins the operation's text
    g7 = merged["G-W2-BC-7"]
    old7, new7 = "as the instruction carries it", "as the PR Instruction states it"
    assert sum(p.count(old7) for p in g7["all"]) == 1, "C-17 guard anchor"
    g7["all"] = [p.replace(old7, new7) for p in g7["all"]]
    g7["fixtures"] = {k: [f.replace(old7, new7) for f in v] for k, v in g7["fixtures"].items()}
    g7["note"] = "C-17: pattern and fixtures follow W2-PR-20-BC-1's rewording ('as the PR Instruction states it')"
    notes.append("C-17: G-W2-BC-7 follows W2-PR-20-BC-1 ('as the PR Instruction states it')")
    _c16_exceptions(merged, notes)
    # C-24: the coordinator's override set for the two IA-30 delta-review guards (rule, pattern and fixtures replaced
    # whole, so neither keeps a pattern for the reverted L-C1 clause); assemble_edits.py's C24_OVERRIDES write the text
    for gid, over in C24_GUARDS.items():
        assert merged[gid]["source"] == "W2" and merged[gid]["prompts"] == ["IA-30"], f"C-24 guard {gid}"
        merged[gid] = dict(merged[gid], **over)
        notes.append(f"C-24: {gid} cut by work unit (the frozen ITEM-14 / ITEM-15 reading; L-C1 stays listed)")
    # C-8 Q1: the presence half on QA-10 (W4's option (a): 'G-W4-10-4 extended to QA-10'); QA-10 carries both EH-1
    # sentences, each matching the rule's pattern, so its entry expects 2, and G-W4-10-4 itself keeps expect 1
    base = merged["G-W4-10-4"]
    merged["G-W4-10-4-QA10"] = {
        "id": "G-W4-10-4-QA10", "part": "PART-10", "rule": base["rule"] + " (QA-10, W4 EH-1 under C-8 Q1)",
        "kind": "required", "expect": 2, "unit": "sentence", "prompts": ["QA-10"], "all": list(base["all"]),
        "fixtures": {"pass": ["An already approved base is never replaced in-flight, except that an approved QA Plan a "
                              "delivered change may have made stale is reviewed at QA-70 against that change. An "
                              "approved QA Plan that a delivered change may have made stale is reviewed at QA-70 "
                              "against that change instead."],
                     "fail": ["An already approved base is never replaced in-flight."],
                     "fail_count_only": ["It is reviewed at QA-70 against that change. It is reviewed at QA-70 "
                                         "against that change. It is reviewed at QA-70 against that change."]},
        "source": "A1 from W4 (C-8 Q1)"}
    order.insert(order.index("G-W4-10-4") + 1, "G-W4-10-4-QA10")
    notes.append("C-8 Q1: G-W4-10-4-QA10 (expect 2 on QA-10)")
    # the binding guards run on PE too (C-1 gives PE a successor and the binding pass covers it)
    for gid in ("G-W7-BIND-1", "G-W8-NAME-1"):
        merged[gid]["prompts"] = sorted(set(merged[gid]["prompts"]) | {"PE"})
        merged[gid]["regenerate"] = "successor_map"
    # W7's pass[1] cites PR-50's 100926.1 page, which under C-1 has a successor, so the regenerated guard forbids it:
    # it moves to fail, and a mention of PR-50's successor (filled from the map) takes its place
    fx = merged["G-W7-BIND-1"]["fixtures"]
    pr50 = '- <mention url="https://app.notion.com/p/3f44590a05eb81d29748eb21df73b02c" />'
    if pr50 in fx["pass"]:
        fx["pass"] = [f for f in fx["pass"] if f != pr50] + ['- <mention url="@SUCC_URL_PR-50" />']
        fx["fail"] = fx["fail"] + [pr50]
        notes.append("G-W7-BIND-1: W7's PR-50 pass fixture moved to fail (C-1 gives PR-50 a successor)")
    notes.append("G-W7-BIND-1 and G-W8-NAME-1: PE added; patterns regenerated from the successor map by body_check")
    # A required guard's registry form proves presence only (the precedent's to_registry). A worker's fail fixture
    # that is present but at a count other than `expect` (a doubled sentence, one of two table rows) is therefore a
    # count-only failure: it moves to fail_count_only, where the precedent's registry check expects the guard to fail
    # it and the registry form to pass it. The classification is by count, computed here, not by reading.
    moved = 0
    for gid in order:
        g = merged[gid]
        if g.get("kind") != "required":
            continue
        keep, count_only = [], list(g["fixtures"].get("fail_count_only", []))
        for fx in g["fixtures"]["fail"]:
            c = _count(fx, g)
            (count_only if c >= 1 else keep).append(fx)
        if len(count_only) != len(g["fixtures"].get("fail_count_only", [])):
            moved += len(count_only) - len(g["fixtures"].get("fail_count_only", []))
            g["fixtures"] = dict(g["fixtures"], fail=keep, fail_count_only=count_only)
    notes.append(f"{moved} required-guard fail fixtures present at a count other than expect moved to fail_count_only")
    guards = []
    for gid in order:
        g = merged[gid]
        out = {k: g[k] for k in CORE if k in g}
        out.setdefault("except", [])
        out["source"] = g["source"]
        out["surface"] = surface(out["prompts"])
        for k in ("regenerate", "except_why", "note", "c16_exceptions"):
            if k in g:
                out[k] = g[k]
        md_all = [markdown_form(p) for p in out["all"]]
        md_exc = [markdown_form(p) for p in out["except"]]
        tol_all = [escape_tolerant(p) for p in md_all]
        tol_exc = [escape_tolerant(p) for p in md_exc]
        if tol_all != out["all"] or tol_exc != out["except"]:
            out["source_all"], out["source_except"] = out["all"], out["except"]
            out["all"], out["except"] = tol_all, tol_exc
            out["escape_tolerant_rewrite"] = tol_all != md_all or tol_exc != md_exc
            if md_all != out["source_all"] or md_exc != out["source_except"]:
                out["markdown_form_translated"] = True  # C-15
        guards.append(out)
    return {
        "record_type": "GCFPE_102726_PLAN_BODY_GUARDS",
        "modification": "MODIFICATION-20261027-gcfpe-backlog-open-items",
        "date": "2026-10-27",
        "purpose": ("Behavior guards for the body operations in edits.json and the central head and binding "
                    "operations (D14, GUARD-001), merged from the nine design workers; each carries its source "
                    "worker. Forbidden guards are a broad match minus named exceptions (D26-E, SCOPE-001); required "
                    "guards prove the repair text present. They become candidate registry assertions (PART-24)."),
        "semantics": ("A unit is a line, or a sentence within a line (split after . ! or ? followed by whitespace). A "
                      "unit matches when every `all` pattern matches it and no `except` pattern does. A forbidden "
                      "guard passes at 0 matching units; a required guard passes at exactly `expect` matching units "
                      "per prompt. Every guard runs on the normalized (Markdown) form of the text, "
                      "normalize_fetch.normalize (C-15): <code>/<b>/<i> become backticks, ** and *, an escaped "
                      "underscore becomes _, mentions are unchanged; patterns are written for that form (translated "
                      "from the workers' fetch-form tags, never retyped). Every pattern is also escape-tolerant "
                      "(C-5 Q-6), which normalization makes unnecessary and harmless. Fixtures expand every @KEY shared "
                      "text and are normalized too. Only counts are reported (D22)."),
        "fixture_rule": ("Fixtures are synthetic text, not prompt bodies. Each `pass` fixture must satisfy the guard "
                         "and each `fail` fixture must violate it; `fail_count_only` is a required guard's text present "
                         "at a count other than `expect` (the guard fails it, its registry form, which proves presence "
                         "only, passes it). body_check.py selftest also runs each fixture with its underscores escaped as "
                         "Notion renders them, and in the fetch's own form (inline markup as tags), and each must give "
                         "the same verdict."),
        "amendments": notes,
        "guards": guards,
    }


def main() -> int:
    g = build()
    text = json.dumps(g, indent=1, ensure_ascii=False) + "\n"
    target = HERE / "guards.json"
    if "--check" in sys.argv:
        same = target.exists() and target.read_text(encoding="utf-8") == text
        print(json.dumps({"mode": "check", "guards_json_current": same}))
        return 0 if same else 1
    target.write_text(text, encoding="utf-8")
    by: dict = {}
    for x in g["guards"]:
        by[x["source"]] = by.get(x["source"], 0) + 1
    print(json.dumps({"mode": "write", "guards": len(g["guards"]), "by_source": by,
                      "escape_rewritten": sum(1 for x in g["guards"] if x.get("escape_tolerant_rewrite")),
                      "surfaces": {s: sum(1 for x in g["guards"] if x["surface"] == s)
                                   for s in ("prompt-body", "notion-control", "repository")}}, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
