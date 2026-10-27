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


def _count(text: str, g: dict) -> int:
    """body_check.py's unit count, on the worker's own (pre-rewrite) patterns."""
    units = text.split("\n") if g["unit"] == "line" else [s for ln in text.split("\n")
                                                          for s in re.split(r"(?<=[.!?])\s+", ln) if s]
    return sum(1 for u in units if all(re.search(p, u) for p in g["all"])
               and not any(re.search(p, u) for p in g.get("except", [])))


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
        for k in ("regenerate", "except_why", "note"):
            if k in g:
                out[k] = g[k]
        tol_all = [escape_tolerant(p) for p in out["all"]]
        tol_exc = [escape_tolerant(p) for p in out["except"]]
        if tol_all != out["all"] or tol_exc != out["except"]:
            out["source_all"], out["source_except"] = out["all"], out["except"]
            out["all"], out["except"] = tol_all, tol_exc
            out["escape_tolerant_rewrite"] = True
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
                      "per prompt. Every pattern is escape-tolerant (C-5 Q-6). Fixtures expand every @KEY shared "
                      "text. Only counts are reported (D22)."),
        "fixture_rule": ("Fixtures are synthetic text, not prompt bodies. Each `pass` fixture must satisfy the guard "
                         "and each `fail` fixture must violate it; `fail_count_only` is a required guard's text present "
                         "at a count other than `expect` (the guard fails it, its registry form, which proves presence "
                         "only, passes it). body_check.py selftest also runs each fixture with its underscores escaped as "
                         "Notion renders them, and it must give the same verdict."),
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
