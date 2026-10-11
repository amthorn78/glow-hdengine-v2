#!/usr/bin/env python3
"""Candidate-page edit rehearsal, landing check and guard self-test for
MODIFICATION-20261011-gcfpe-mb008-to-promotion (PLAN, PART-02 and PART-03). Adapted from the parent
Modification's plan-successor-2/body_check.py: the same span, landing, guard and registry logic, with this
Modification's edits.json and guards.json, and a registry row for every candidate member (PE has none).
Two changes to the logic, for insertion operations, whose replacement carries the old span's start anchor (the
TypeSafe text after C-PLACE, and PE-SCAN): an operation has LANDED when its replacement occurs once and its start
anchor occurs only inside the page's replacements; and a page's batch is safe when each old_str occurs exactly
once in the text at the moment update_content applies it in order, and afterwards only inside its own new_str.
A replacement operation behaves exactly as in the parent script.

  body_check.py selftest                       every guard against its synthetic fixtures, and the span
                                               resolver's apply-once behaviour on synthetic text
  body_check.py plan  [--no-ops] [--prompts P ...] [--fetched-after T]
                                               on the newest fetch of each page: refuse a moved revision,
                                               resolve every operation's span exactly once, apply in memory,
                                               and run every guard before and after
  body_check.py check [--prompts P ...] [--fetched-after T]
                                               after landing, on a fresh fetch only: the revision moved,
                                               every operation landed by its anchor counts, and every guard
                                               passing
  body_check.py registry --audit-root DIR [--emit]
                                               each guard in the registry's own audit_assertions form, run
                                               by the shipped governance-audit engine on every fixture and on
                                               each page before and after the in-memory edits; it must agree
                                               with the guard everywhere. --emit prints only the assertions

Bodies are read only as D22 transient reads: the newest `notion-fetch` result for each page in this session's
own harness records (transcript, tool results, subagents), captured at or after --fetched-after (an ISO UTC time
taken just before the fetches) and within --since-minutes. Each check uses only the read in hand: no earlier
read is reused, and no body is hashed, compared with another read or written. The report carries counts, ids
and booleans only. `plan` without --no-ops also prints each
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


def _recent_lines(path: str, cutoff_iso: str):
    """A JSONL record's entries newest first, stopping at the first entry older than the cutoff, so earlier
    reads held in the record are never read again (D22 condition 4)."""
    with open(path, "rb") as fh:
        fh.seek(0, os.SEEK_END)
        pos, tail = fh.tell(), b""
        while pos > 0:
            step = min(1 << 20, pos)
            pos -= step
            fh.seek(pos)
            lines = (fh.read(step) + tail).split(b"\n")
            tail = lines.pop(0) if pos > 0 else b""
            for raw in reversed(lines):
                if not raw.strip():
                    continue
                try:
                    obj = json.loads(raw)
                except ValueError:
                    continue
                ts = obj.get("timestamp") if isinstance(obj, dict) else None
                if isinstance(ts, str) and ts < cutoff_iso:
                    return
                yield obj


def all_fetches(page_id: str, root: str, session: str, since_minutes: int, fetched_after: str = "") -> list:
    """Every captured fetch of the page at or after the cutoff, oldest first: (captured, as_of, body). The cutoff
    is --fetched-after when given, else --since-minutes ago. A saved result written before the cutoff is never
    opened, and a transcript is read only back to the cutoff."""
    page = page_id.replace("-", "")
    cutoff = time.time() - since_minutes * 60
    if fetched_after:
        cutoff = max(cutoff, datetime.strptime(fetched_after, "%Y-%m-%dT%H:%M:%S.%fZ")
                     .replace(tzinfo=timezone.utc).timestamp())
    cutoff_iso = datetime.fromtimestamp(cutoff, timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    base = os.path.join(root, "*", session)
    files = glob.glob(base + ".jsonl") + glob.glob(base + "/tool-results/*") \
        + glob.glob(base + "/subagents/**/*.jsonl", recursive=True) \
        + glob.glob(base + "/subagents/**/tool-results/*", recursive=True)
    found = {}
    for f in files:
        if os.path.getmtime(f) < cutoff:
            continue
        if f.endswith(".jsonl"):
            entries = _recent_lines(f, cutoff_iso)
        else:
            try:
                raw = open(f, encoding="utf-8").read()
                entries = [json.loads(raw)] if page in raw else []
            except (OSError, ValueError):
                continue
        for obj in entries:
            ts = obj.get("timestamp") if isinstance(obj, dict) else None
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
                if not captured or captured < cutoff_iso:
                    continue
                # one capture can appear in several records (transcript and tool-result file): keep one per body
                key = (head.group(2), m.group(1))
                if key not in found or captured > found[key][0]:
                    found[key] = (captured, head.group(2), m.group(1))
    return sorted(found.values(), key=lambda c: c[0])


def latest_fetch(page_id: str, root: str, session: str, since_minutes: int, fetched_after: str = ""):
    got = all_fetches(page_id, root, session, since_minutes, fetched_after)
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
    """UNTOUCHED: the span resolves and the replacement is absent. LANDED: the replacement occurs once and the
    start anchor occurs only inside it (for a replacement operation, not at all). Anything else is CONFLICT, and
    nothing is applied to it."""
    span, _ = resolve(text, op)
    new = expand(op["new"])
    new_n = occ(text, new)
    if span is not None and new_n == 0:
        return "UNTOUCHED"
    if new_n == 1 and occ(text, op["start"]) == occ(new, op["start"]):
        return "LANDED"
    return "CONFLICT"


def landed(text: str, op: dict, page_ops: list) -> dict:
    """An operation has landed when, on this read alone, its replacement is present and its old span's start
    and end anchors survive only where the page's replacements carry them. The plan proves each anchor occurs
    exactly once in the unedited page, so any truncated, shifted or partial replacement leaves an anchor
    count off. Uses no other read (D22)."""
    news = [expand(o["new"]) for o in page_ops]
    want = lambda s: sum(occ(n, s) for n in news)
    new = expand(op["new"])
    row = {"new": occ(text, new) == want(new) >= 1, "start": occ(text, op["start"]) == want(op["start"])}
    if op.get("end") is not None:
        row["end"] = occ(text, op["end"]) == want(op["end"])
    # an insertion keeps the start anchor, so a second send would leave every count above unchanged; the text it
    # adds around the anchor must occur only where the page's replacements carry it
    if op["start"] in new:
        i = new.find(op["start"])
        for key, part in (("inserted_before", new[:i].strip()), ("inserted_after", new[i + len(op["start"]):].strip())):
            if part:
                row[key] = occ(text, part) == want(part)
    row["landed"] = all(row.values())
    return row


def apply_all(text: str, ops: list) -> tuple[str, list]:
    """Apply each UNTOUCHED operation once, in order; returns the text and one row per operation."""
    rows = []
    for o in ops:
        before = state(text, o)
        span, why = resolve(text, o)
        applied = before == "UNTOUCHED" and span is not None
        old = text[span[0]:span[1]] if applied else None
        # update_content applies a page's operations in order and refuses an old_str that is absent or repeated
        count_at_application = occ(text, old) if applied else None
        if applied:
            text = text[:span[0]] + expand(o["new"]) + text[span[1]:]
        rows.append({"id": o["id"], "state_before": before, "refusal": why, "applied": applied, "old_str": old,
                     "new_str": expand(o["new"]) if applied else None,
                     "old_str_count_at_application": count_at_application})
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
REGISTRY_ROWS = {p for p in EDITS["pages"] if p != "PE"}  # every candidate member; PE has no registry row


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


def registry(audit_root: str, root: str, session: str, since: int, fetched_after: str = "") -> dict:
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
        got = latest_fetch(meta["page_id"], root, session, since, fetched_after)
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
             # check's anchor-count landing on one read: an exact edit lands; a replacement that kept the old
             # span's tail or head, or never happened, does not
             "anchor_landing_exact": landed(t1, op, [op])["landed"],
             "anchor_landing_refuses_kept_tail": not landed(
                 t0.replace("Alpha begins here. Middle words", "Beta replaces it."), op, [op])["landed"],
             "anchor_landing_refuses_kept_head": not landed(
                 t0.replace("Middle words and ends here.", "Beta replaces it."), op, [op])["landed"],
             "anchor_landing_refuses_untouched": not landed(t0, op, [op])["landed"]}
    # an insertion operation, whose replacement keeps the start anchor: untouched, landed once, never applied twice
    ins = {"id": "SYN-2", "start": "Alpha begins here.", "end": None, "new": "Alpha begins here. Gamma follows."}
    t2, r2 = apply_all(t0, [ins])
    t3, r3 = apply_all(t2, [ins])
    synth.update({"insert_untouched": state(t0, ins) == "UNTOUCHED",
                  "insert_applied_once": r2[0]["applied"] and r2[0]["old_str_count_at_application"] == 1,
                  "insert_landed": state(t2, ins) == "LANDED",
                  "insert_second_send_refused": not r3[0]["applied"] and t3 == t2,
                  "insert_anchor_landing": landed(t2, ins, [ins])["landed"],
                  "insert_landing_refuses_untouched": not landed(t0, ins, [ins])["landed"],
                  "insert_landing_refuses_doubled": not landed(t2.replace("Gamma follows.", "Gamma follows. Gamma follows."),
                                                               ins, [ins])["landed"],
                  # a replacement operation that lands still reads LANDED, as in the parent script
                  "replace_landed_unchanged": state(t1, op) == "LANDED"})
    ok &= all(synth.values())
    return {"mode": "selftest", "guards": len(GUARDS["guards"]), "fixture_rows": rows, "span_resolver": synth, "ok": ok}


def run(mode: str, prompts, no_ops: bool, root: str, session: str, since: int, fetched_after: str = "") -> dict:
    out, ops_payload, all_ok = [], [], True
    for prompt, meta in EDITS["pages"].items():
        if prompts and prompt not in prompts:
            continue
        fetches = all_fetches(meta["page_id"], root, session, since, fetched_after)
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
                    op = next(o for o in ops if o["id"] == r["id"])
                    r["end_unique_in_original"] = op.get("end") is None or occ(body, op["end"]) == 1
                    r["old_str_once_at_application"] = r.pop("old_str_count_at_application") == 1
                    r["old_str_only_in_own_new_after"] = occ(text, r["old_str"]) == occ(r["new_str"], r["old_str"])
                    r["span_has_markup"] = any(m in r["old_str"] for m in ("<", "](", "\\"))
                    if not no_ops:
                        ops_payload.append({"id": r["id"], "page_id": meta["page_id"], "old_str": r["old_str"],
                                            "new_str": r["new_str"]})
            row["ops"] = [{k: v for k, v in r.items() if k not in ("old_str", "new_str")} for r in op_rows]
            row["batch_safe"] = all(r.get("old_str_unique_in_original") and r.get("old_str_once_at_application")
                                    and r.get("old_str_only_in_own_new_after")
                                    and r.get("end_unique_in_original") and not r.get("span_has_markup")
                                    for r in op_rows if r["applied"])
            row["guards_after"] = {g["id"]: dict(zip(("count", "pass"), guard_pass(text, g))) for g in guards_for(prompt)}
            row["landed_state_after"] = {o["id"]: state(text, o) for o in ops}
            # X5's landing check run on this same read with the edits applied in memory: a correct landing must
            # pass it, or EXECUTE would stop after writing
            row["check_would_pass"] = all(landed(text, o, ops)["landed"] for o in ops)
            row["ok"] = (row["revision_matches_plan"] and all(r["applied"] for r in op_rows) and row["batch_safe"]
                         and all(v["pass"] for v in row["guards_after"].values())
                         and all(v == "LANDED" for v in row["landed_state_after"].values())
                         and row["check_would_pass"])
        else:
            row["revision_moved"] = as_of != meta["expected_last_edited"]
            row["ops"] = {o["id"]: landed(body, o, ops) for o in ops}
            row["guards"] = {g["id"]: dict(zip(("count", "pass"), guard_pass(body, g))) for g in guards_for(prompt)}
            row["ok"] = (row["revision_moved"] and all(v["landed"] for v in row["ops"].values())
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
    ap.add_argument("--fetched-after", default="",
                    help="ISO UTC time taken just before the fetches; older reads are never used")
    ap.add_argument("--harness-root", default=os.path.expanduser("~/.claude/projects"))
    ap.add_argument("--session", default=os.environ.get("CLAUDE_CODE_SESSION_ID"))
    a = ap.parse_args()
    if a.mode == "selftest":
        res = selftest()
    elif a.mode == "registry" and a.emit:
        res = {"record_type": "MB008_PLAN_REGISTRY_GUARDS", "source": "guards.json via body_check.py registry",
               "assertions": registry_assertions(), "ok": True}
    elif a.mode == "registry":
        if not (a.audit_root and a.session):
            print(json.dumps({"error": "registry needs --audit-root and a session"}))
            return 2
        res = registry(a.audit_root, a.harness_root, a.session, a.since_minutes, a.fetched_after)
    else:
        if not a.session:
            print(json.dumps({"error": "SESSION_UNKNOWN: set CLAUDE_CODE_SESSION_ID or --session"}))
            return 2
        res = run(a.mode, a.prompts, a.no_ops, a.harness_root, a.session, a.since_minutes, a.fetched_after)
    print(json.dumps(res, indent=1, ensure_ascii=False))
    return 0 if res["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
