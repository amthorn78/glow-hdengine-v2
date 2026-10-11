#!/usr/bin/env python3
"""Candidate-page edit rehearsal, landing check and guard self-test for
MODIFICATION-20261010-gcfpe-candidate-skill-analysis (PLAN successor 2).

  body_check.py selftest                       every guard against its synthetic fixtures, and the span
                                               resolver's apply-once behaviour on synthetic text
  body_check.py plan  [--no-ops] [--prompts P ...]
                                               on the newest fetch of each page: refuse a moved revision,
                                               resolve every operation's span exactly once, apply in memory,
                                               and run every guard before and after
  body_check.py check [--prompts P ...]        after landing, on a fresh fetch: the revision moved, every
                                               operation LANDED, every guard passing, and the page equal to
                                               the newest pre-edit read of the pinned revision with exactly
                                               the planned operations applied (in memory)
  body_check.py registry --audit-root DIR [--emit]
                                               each guard in the registry's own audit_assertions form, run
                                               by the shipped governance-audit engine on every fixture and on
                                               each page before and after the in-memory edits; it must agree
                                               with the guard everywhere. --emit prints only the assertions

Bodies are read only as D22 transient reads: the newest `notion-fetch` result for each page in this session's
own harness records (transcript, tool results, subagents), within --since-minutes. Nothing is hashed or
written, and the report carries counts, ids and booleans only. `plan` without --no-ops also prints each
operation's old_str and new_str for EXECUTE's update_content calls; never redirect that output into the
repository. Run from anywhere with PYTHONDONTWRITEBYTECODE=1; CLAUDE_CODE_SESSION_ID names the session.
"""
from __future__ import annotations

import argparse
import glob
import importlib.util
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
EDITS = json.loads((HERE / "edits.json").read_text(encoding="utf-8"))
GUARDS = json.loads((HERE / "guards.json").read_text(encoding="utf-8"))
SHARED = EDITS["shared_texts"]
FETCH_HEAD = re.compile(r'Here is the result of "fetch" for the Page with URL https://[^/\s]+/p/([0-9a-f-]{32,36}) '
                        r'as of (\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z):')


def expand(text: str) -> str:
    for key in sorted(SHARED, key=len, reverse=True):
        text = text.replace("@" + key, SHARED[key])
    return text


def occ(text: str, s: str) -> int:
    n, i = 0, text.find(s)
    while i >= 0:
        n += 1
        i = text.find(s, i + 1)
    return n


# --- transient read of the newest fetch (D22) ---------------------------------------------------------
def _texts(obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "text" and isinstance(v, str):
                yield v
            else:
                yield from _texts(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from _texts(v)


def all_fetches(page_id: str, root: str, session: str, since_minutes: int) -> list:
    """Every captured fetch of the page in the window, oldest first: (captured, as_of, body)."""
    page = page_id.replace("-", "")
    cutoff = time.time() - since_minutes * 60
    cutoff_iso = datetime.fromtimestamp(cutoff, timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    base = os.path.join(root, "*", session)
    files = glob.glob(base + ".jsonl") + glob.glob(base + "/tool-results/*") \
        + glob.glob(base + "/subagents/**/*.jsonl", recursive=True) \
        + glob.glob(base + "/subagents/**/tool-results/*", recursive=True)
    found = {}
    for f in files:
        if os.path.getmtime(f) < cutoff:
            continue
        try:
            raw = open(f, encoding="utf-8").read()
        except OSError:
            continue
        if page not in raw:
            continue
        units = raw.splitlines() if f.endswith(".jsonl") else [raw]
        for line in units:
            try:
                obj = json.loads(line)
            except ValueError:
                continue
            ts = obj.get("timestamp") if isinstance(obj, dict) else None
            if f.endswith(".jsonl") and not (isinstance(ts, str) and ts >= cutoff_iso):
                continue
            for t in _texts(obj):
                inner = t
                if not inner.startswith("Here is the result of"):
                    try:
                        inner = json.loads(t)["text"]
                    except (ValueError, KeyError, TypeError):
                        continue
                head = FETCH_HEAD.match(inner)
                if not head or head.group(1).replace("-", "") != page:
                    continue
                m = re.search(r"<content>\n?(.*)</content>", inner, re.S)
                if not m:
                    continue
                captured = ts if f.endswith(".jsonl") else datetime.fromtimestamp(
                    os.path.getmtime(f), timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
                # one capture can appear in several records (transcript and tool-result file): keep one per body
                key = (head.group(2), m.group(1))
                if key not in found or (captured or "") > found[key][0]:
                    found[key] = (captured or "", head.group(2), m.group(1))
    return sorted(found.values(), key=lambda c: c[0])


def latest_fetch(page_id: str, root: str, session: str, since_minutes: int):
    got = all_fetches(page_id, root, session, since_minutes)
    return got[-1] if got else None  # (captured, as_of, body) or None


# --- spans and operations -------------------------------------------------------------------------------
def resolve(text: str, op: dict):
    s = op["start"]
    n = occ(text, s)
    if n != 1:
        return None, f"START_COUNT_{n}"
    i = text.find(s)
    if op.get("end") is None:
        return (i, i + len(s)), None
    line_end = text.find("\n", i)
    line_end = len(text) if line_end < 0 else line_end
    j = text.find(op["end"], i + len(s))
    if j < 0 or j + len(op["end"]) > line_end:
        return None, "END_NOT_ON_LINE"
    return (i, j + len(op["end"])), None


def state(text: str, op: dict) -> str:
    span, _ = resolve(text, op)
    new_n = occ(text, expand(op["new"]))
    if span is not None and new_n == 0:
        return "UNTOUCHED"
    if span is None and new_n == 1:
        return "LANDED"
    return "CONFLICT"


def apply_all(text: str, ops: list) -> tuple[str, list]:
    """Apply each UNTOUCHED operation once, in order; returns the text and one row per operation."""
    rows = []
    for o in ops:
        before = state(text, o)
        span, why = resolve(text, o)
        applied = before == "UNTOUCHED" and span is not None
        old = text[span[0]:span[1]] if applied else None
        if applied:
            text = text[:span[0]] + expand(o["new"]) + text[span[1]:]
        rows.append({"id": o["id"], "state_before": before, "refusal": why, "applied": applied, "old_str": old,
                     "new_str": expand(o["new"]) if applied else None})
    return text, rows


# --- guards ---------------------------------------------------------------------------------------------
def units(text: str, unit: str):
    for line in text.split("\n"):
        if unit == "line":
            yield line
        else:
            yield from (s for s in re.split(r"(?<=[.!?])\s+", line) if s)


def guard_count(text: str, g: dict) -> int:
    n = 0
    for u in units(text, g["unit"]):
        if all(re.search(p, u) for p in g["all"]) and not any(re.search(p, u) for p in g.get("except", [])):
            n += 1
    return n


def guard_pass(text: str, g: dict) -> tuple[int, bool]:
    c = guard_count(text, g)
    return c, (c == 0 if g["kind"] == "forbidden" else c == g["expect"])


def guards_for(prompt: str):
    return [g for g in GUARDS["guards"] if prompt in g["prompts"]]


# --- registry form ----------------------------------------------------------------------------------------
# One character inside a body_check sentence unit: units split after . ! or ? followed by whitespace.
SENT_CH = r"(?:[^.!?\n]|[.!?](?!\s))"
REGISTRY_ROWS = {"QA-50", "CF-C-30", "CF-E-30", "IA-30", "QA-70", "RS-20", "ESC-40"}  # PE has no registry row


def _scoped(p: str) -> tuple[str, bool]:
    """A guard pattern as a self-contained group; a leading (?i) is scoped to it, a leading ^ is reported."""
    ci = p.startswith("(?i)")
    core = p[4:] if ci else p
    anchored = core.startswith("^")
    core = core[1:] if anchored else core
    return (f"(?i:{core})" if ci else f"(?:{core})"), anchored


def to_registry(g: dict) -> dict:
    """The guard as one regex the audit engine runs with re.search(.., re.MULTILINE) over the whole page. A
    forbidden guard becomes forbidden_regex (no unit may match). A required guard becomes required_regex, which
    proves presence (at least one unit); the exactly-once count stays with this script's guard."""
    ch = "." if g["unit"] == "line" else SENT_CH
    start = "(?m)^" if g["unit"] == "line" else r"(?m)(?:^|(?<=[.!?])\s+)"
    parts = []
    for p in g.get("except", []):
        core, anchored = _scoped(p)
        parts.append(f"(?!{core})" if anchored else f"(?!{ch}*{core})")
    for p in g["all"]:
        core, anchored = _scoped(p)
        parts.append(f"(?={core})" if anchored else f"(?={ch}*{core})")
    key = "forbidden_regex" if g["kind"] == "forbidden" else "required_regex"
    return {key: {"rule_id": "CTR-001" if key == "forbidden_regex" else "CTR-002", "value": start + "".join(parts)}}


def registry_assertions() -> dict:
    out = {}
    for prompt in EDITS["pages"]:
        a = {"forbidden_regex": [], "required_regex": []}
        for g in guards_for(prompt):
            for k, v in to_registry(g).items():
                a[k].append({**v, "guard": g["id"]})
        out[prompt] = {"registry_row": prompt in REGISTRY_ROWS, "audit_assertions": a}
    return out


def _engine(audit_root: str):
    sys.dont_write_bytecode = True
    script = os.path.join(audit_root, "scripts", "audit_workspace_governance.py")
    spec = importlib.util.spec_from_file_location("audit_workspace_governance", script)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod._evaluate_assertions


def _registry_pass(evaluate, g: dict, text: str) -> bool:
    (k, v), = to_registry(g).items()
    return not evaluate({"prompt_key": g["id"], "audit_assertions": {k: [v]}}, text, "transient")


def registry(audit_root: str, root: str, session: str, since: int) -> dict:
    evaluate = _engine(audit_root)
    fixtures, pages, ok = [], [], True
    for g in GUARDS["guards"]:
        for want, fxs in (("pass", g["fixtures"]["pass"]), ("fail", g["fixtures"]["fail"])):
            for k, fx in enumerate(fxs):
                text = expand(fx)
                agree = _registry_pass(evaluate, g, text) == guard_pass(text, g)[1] == (want == "pass")
                ok &= agree
                fixtures.append({"guard": g["id"], "fixture": f"{want}[{k}]", "agrees": agree})
    for prompt, meta in EDITS["pages"].items():
        got = latest_fetch(meta["page_id"], root, session, since)
        if got is None:
            pages.append({"prompt": prompt, "error": "NO_FETCH_FOUND"})
            ok = False
            continue
        before = got[2]
        after, _ = apply_all(before, [o for o in EDITS["ops"] if o["prompt"] == prompt])
        for g in guards_for(prompt):
            row = {"prompt": prompt, "guard": g["id"], "as_of": got[1]}
            for label, text in (("before", before), ("after", after)):
                reg, grd = _registry_pass(evaluate, g, text), guard_pass(text, g)[1]
                row[f"{label}_registry_pass"], row[f"{label}_guard_pass"] = reg, grd
            row["agrees"] = (row["before_registry_pass"] == row["before_guard_pass"]
                             and row["after_registry_pass"] == row["after_guard_pass"] and row["after_guard_pass"])
            ok &= row["agrees"]
            pages.append(row)
    return {"mode": "registry", "engine": "amthor-workspace-governance-audit _evaluate_assertions",
            "fixtures": fixtures, "pages": pages, "ok": ok,
            "d22": "transient reads of this session's harness records; no body text in this report"}


# --- modes ----------------------------------------------------------------------------------------------
def selftest() -> dict:
    rows, ok = [], True
    for g in GUARDS["guards"]:
        for want, fixtures in (("pass", g["fixtures"]["pass"]), ("fail", g["fixtures"]["fail"])):
            for k, fx in enumerate(fixtures):
                c, passed = guard_pass(expand(fx), g)
                good = passed if want == "pass" else not passed
                ok &= good
                rows.append({"guard": g["id"], "fixture": f"{want}[{k}]", "count": c, "as_expected": good})
    # span resolver on synthetic text: untouched, landed, refused on a second send, refused on ambiguity
    op = {"id": "SYN-1", "start": "Alpha begins here.", "end": "and ends here.", "new": "Beta replaces it."}
    t0 = "x\nAlpha begins here. Middle words and ends here. Tail.\ny"
    span, _ = resolve(t0, op)
    t1 = t0[:span[0]] + op["new"] + t0[span[1]:]
    synth = {"untouched": state(t0, op) == "UNTOUCHED", "landed": state(t1, op) == "LANDED",
             "second_send_refused": resolve(t1, op)[0] is None,
             "ambiguous_refused": resolve(t0 + "\nAlpha begins here. and ends here.", op)[1] == "START_COUNT_2",
             "cross_line_refused": resolve("Alpha begins here.\nand ends here.", op)[1] == "END_NOT_ON_LINE",
             # check's in-memory landed equality: holds for the exact edit, fails on any other change
             "landed_equality_holds": apply_all(t0, [op])[0] == t1,
             "landed_equality_detects_extra_change": apply_all(t0, [op])[0] != t1.replace("Tail.", "Tail!"),
             "landed_equality_detects_partial_edit": apply_all(t0, [op])[0] != t0}
    ok &= all(synth.values())
    return {"mode": "selftest", "guards": len(GUARDS["guards"]), "fixture_rows": rows, "span_resolver": synth, "ok": ok}


def run(mode: str, prompts, no_ops: bool, root: str, session: str, since: int) -> dict:
    out, ops_payload, all_ok = [], [], True
    for prompt, meta in EDITS["pages"].items():
        if prompts and prompt not in prompts:
            continue
        fetches = all_fetches(meta["page_id"], root, session, since)
        if not fetches:
            out.append({"prompt": prompt, "error": "NO_FETCH_FOUND"})
            all_ok = False
            continue
        captured, as_of, body = fetches[-1]
        ops = [o for o in EDITS["ops"] if o["prompt"] == prompt]
        row = {"prompt": prompt, "fetch_captured": captured, "as_of": as_of}
        if mode == "plan":
            row["revision_matches_plan"] = as_of == meta["expected_last_edited"]
            row["guards_before"] = {g["id"]: dict(zip(("count", "pass"), guard_pass(body, g))) for g in guards_for(prompt)}
            text, op_rows = apply_all(body, ops)
            # One update_content call carries every operation of the page, so each old_str must name its span
            # alone in the unedited page and be gone afterwards; spans carrying mention or link markup are
            # reported, because replacing them would drop a native reference.
            for r in op_rows:
                if r["applied"]:
                    r["old_str_unique_in_original"] = occ(body, r["old_str"]) == 1
                    r["old_str_absent_after"] = occ(text, r["old_str"]) == 0
                    r["span_has_markup"] = any(m in r["old_str"] for m in ("<", "](", "\\"))
                    if not no_ops:
                        ops_payload.append({"id": r["id"], "page_id": meta["page_id"], "old_str": r["old_str"],
                                            "new_str": r["new_str"]})
            row["ops"] = [{k: v for k, v in r.items() if k not in ("old_str", "new_str")} for r in op_rows]
            row["batch_safe"] = all(r.get("old_str_unique_in_original") and r.get("old_str_absent_after")
                                    and not r.get("span_has_markup") for r in op_rows if r["applied"])
            row["guards_after"] = {g["id"]: dict(zip(("count", "pass"), guard_pass(text, g))) for g in guards_for(prompt)}
            row["landed_state_after"] = {o["id"]: state(text, o) for o in ops}
            row["ok"] = (row["revision_matches_plan"] and all(r["applied"] for r in op_rows) and row["batch_safe"]
                         and all(v["pass"] for v in row["guards_after"].values())
                         and all(v == "LANDED" for v in row["landed_state_after"].values()))
        else:
            row["op_states"] = {o["id"]: state(body, o) for o in ops}
            row["guards"] = {g["id"]: dict(zip(("count", "pass"), guard_pass(body, g))) for g in guards_for(prompt)}
            row["revision_moved"] = as_of != meta["expected_last_edited"]
            # Silent-wrong-edit check, in memory only: the landed page must equal the newest pre-edit read of
            # the pinned revision with exactly the planned operations applied. Nothing is stored or hashed.
            pre = [f for f in fetches[:-1] if f[1] == meta["expected_last_edited"]]
            row["pre_edit_read_found"] = bool(pre)
            if pre:
                expected, _ = apply_all(pre[-1][2], ops)
                row["rest_unchanged"] = expected == body
                a, b = expected.split("\n"), body.split("\n")
                row["differing_lines"] = sum(1 for x, y in zip(a, b) if x != y) + abs(len(a) - len(b))
            else:
                row["rest_unchanged"] = False
            row["ok"] = (row["revision_moved"] and row["pre_edit_read_found"] and row["rest_unchanged"]
                         and all(v == "LANDED" for v in row["op_states"].values())
                         and all(v["pass"] for v in row["guards"].values()))
        all_ok &= row["ok"]
        out.append(row)
    result = {"mode": mode, "pages": out, "ok": all_ok,
              "d22": "transient reads of this session's harness records; no body text in this report"}
    if mode == "plan" and not no_ops:
        result["ops_payload_for_execute"] = ops_payload
    return result


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["selftest", "plan", "check", "registry"])
    ap.add_argument("--audit-root")
    ap.add_argument("--emit", action="store_true")
    ap.add_argument("--no-ops", action="store_true")
    ap.add_argument("--prompts", nargs="*")
    ap.add_argument("--since-minutes", type=int, default=60)
    ap.add_argument("--harness-root", default=os.path.expanduser("~/.claude/projects"))
    ap.add_argument("--session", default=os.environ.get("CLAUDE_CODE_SESSION_ID"))
    a = ap.parse_args()
    if a.mode == "selftest":
        res = selftest()
    elif a.mode == "registry" and a.emit:
        res = {"record_type": "PLAN_SUCCESSOR_2_REGISTRY_GUARDS", "source": "guards.json via body_check.py registry",
               "assertions": registry_assertions(), "ok": True}
    elif a.mode == "registry":
        if not (a.audit_root and a.session):
            print(json.dumps({"error": "registry needs --audit-root and a session"}))
            return 2
        res = registry(a.audit_root, a.harness_root, a.session, a.since_minutes)
    else:
        if not a.session:
            print(json.dumps({"error": "SESSION_UNKNOWN: set CLAUDE_CODE_SESSION_ID or --session"}))
            return 2
        res = run(a.mode, a.prompts, a.no_ops, a.harness_root, a.session, a.since_minutes)
    print(json.dumps(res, indent=1, ensure_ascii=False))
    return 0 if res["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
