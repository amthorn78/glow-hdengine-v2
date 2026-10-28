#!/usr/bin/env python3
"""Repository edits of X1 and X26 for MODIFICATION-20261027-gcfpe-backlog-open-items (C-23, repair of PLAN review
round 1, R-1).

The edits are the design returns' own `repo_edits` (plan/work/W1.json, W6.json, W7.json, W8.json); nothing is retyped
here except one anchor, which C-23 fixes: W1's PART-02 note is stored anchored on D29's closing text, so applied as
stored it would land before `## D30`. The note's text is W1's (its `new` minus its `old`); its anchor is D30's closing
line, so it lands after D30 (C-11, Q-W7-2 (a)).

Sets:
  X1   W6-RE-19 (the v5.1.0 procedure, a new file written from v5.0.0 with seven edits), W6-RE-20, W6-RE-21, W6-RE-28,
       and W1's PART-02 note anchored on D30's closing line. No marker; lands in the controls pull request.
  X26  P7's R3 and R4: RE-W7-03 to RE-W7-10b and RE-W8-01 to RE-W8-07 on authoritative-surfaces.md, RE-W8-08 on
       notion-write-boundary.md, and RE-W7-11, the promotion entry appended to the decision record. Its @ markers are
       filled from EXECUTE's receipts with --values FILE ({"@KEY": "value"}); an unfilled marker is refused.

  repo_edits_102726.py apply --set X1|X26 --root <repo> [--values F] [--main-ref origin/main]
        Before anything is written: every `old` string occurs its stated count in the file as it stands (and once at
        its application, in order), a new file does not yet exist, and no marker is left. Then the edits are applied
        in memory, the after-check below must pass, and only then are the files written. A failed check writes
        nothing. A second apply is refused, because the `old` strings are gone.
  repo_edits_102726.py check --set X1|X26 --root <repo> --state before|after [--values F] [--main-ref origin/main]
        before: every `old` count as stated, each new file absent, every repository guard at W6's measured `before`
        count. after: each `new` string once, each `old` string only inside its own replacement, every repository
        guard passing (forbidden 0, required at `expect`), counted with body_check.py's guard functions
        (guard_count / guard_pass, which run on normalize_fetch.normalize of the text); v5.0.0 byte-equal to
        --main-ref; for X1 the note heading once and after `## D30`; for X26 the promotion heading once and the
        decision record before it byte-unchanged (the file as it stood is a prefix of the file after).
  repo_edits_102726.py selftest [--root <repo>]
        on a temporary copy of the target files: a clean X1 apply passes its after-check, and each injected defect
        fails: a missing anchor, a doubled anchor, a second apply, an existing v5.1.0, a surviving forbidden line, a
        missing required line, the note anchored as W1 stored it (before D30), an unfilled X26 marker, a changed
        v5.0.0, and an X26 entry that rewrites an earlier entry.

AM-11 (Nathan, 2026-10-28, at X26: "AM-11 as proposed (option A), outside rule 4's count"): W7 used @PROMOTION_DATE
for two dates, which D29's precedent had on one day: Nathan's approval and the transaction. In this set the two places
that date the approval, RE-W7-08's registry `APPROVED` date and RE-W7-11's "Product Owner, ..." line, carry
@PROMOTION_APPROVED_AT (the date of Nathan's exact promotion approval, W8's marker, as §E records it); every other
@PROMOTION_DATE is the date the promotion took effect. No other written text changes (AM11_SWAPS).

Repository files are not Notion reads, so normalization changes nothing on them unless they carry a literal `\\_` or
inline tag; each guard row also reports whether the raw and normalized counts differ. The reports carry counts, ids
and booleans only (D22). Run with PYTHONDONTWRITEBYTECODE=1. Never run apply on the real tree before X1 (C-12) or X26.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import body_check as bc  # noqa: E402  (guard_count, guard_pass, raw_guard_count; GUARDS)

WORK = HERE / "work"
DR = "docs/prompt_ecosystem_management/gcfpe.decision-record.md"
V500 = "docs/ephemeral/GCFPE-Direct-Handoff-and-Runtime-Artifact-Operating-Procedure-v5.0.0-20260923.md"
D30_HEAD = "## D30 — "
D30_CLOSE = "**Until those land,\n`D30` is ruled but not applied.**\n"   # C-23: W1's note is anchored here
MARKER = re.compile(r"@[A-Z][A-Z0-9_]+")
X1_IDS = ("W6-RE-19", "W6-RE-20", "W6-RE-21", "W6-RE-28")
AM11_SWAPS = {"RE-W7-08": ("`APPROVED` @PROMOTION_DATE", "`APPROVED` @PROMOTION_APPROVED_AT"),
              "RE-W7-11": ("**Product Owner, @PROMOTION_DATE**", "**Product Owner, @PROMOTION_APPROVED_AT**")}
X26_IDS = ("RE-W7-03", "RE-W7-04", "RE-W7-05", "RE-W7-06", "RE-W7-07", "RE-W7-08", "RE-W7-09", "RE-W7-10",
           "RE-W7-10b", "RE-W8-01", "RE-W8-02", "RE-W8-03", "RE-W8-04", "RE-W8-05", "RE-W8-06", "RE-W8-07",
           "RE-W8-08", "RE-W7-11")


def occ(text: str, s: str) -> int:
    n, i = 0, text.find(s)
    while i >= 0:
        n += 1
        i = text.find(s, i + 1)
    return n


def _repo_edits(w: str) -> list:
    return [e for e in json.loads((WORK / f"{w}.json").read_text(encoding="utf-8"))["repo_edits"] if isinstance(e, dict)]


def edit_set(name: str) -> list:
    """[{id, path, new_file, content_from, edits: [{old, new, count, append}]}] in application order."""
    if name == "X1":
        by = {e["id"]: e for e in _repo_edits("W6") if e.get("id") in X1_IDS}
        out = [{"id": i, "path": by[i]["path"], "new_file": bool(by[i].get("new_file")),
                "content_from": by[i].get("content_from"),
                "edits": [{"old": x["old"], "new": x["new"], "count": x["count"]} for x in by[i]["edits"]]}
               for i in X1_IDS]
        w1 = _repo_edits("W1")[0]
        assert w1["part"] == "PART-02" and w1["path"] == DR and w1["new"].startswith(w1["old"]), "W1 note shape"
        note = w1["new"][len(w1["old"]):]
        assert note.startswith("\n## Note, 2026-10-27 — "), "W1 note heading"
        out.append({"id": "W1-PART-02-NOTE", "path": DR, "new_file": False, "content_from": None,
                    "edits": [{"old": D30_CLOSE, "new": D30_CLOSE + note, "count": 1}],
                    "note_heading": note.split("\n")[1], "reanchored_from": "D29's closing text (W1.json repo_edits[0])"})
        return out
    if name == "X26":
        by = {}
        for w in ("W7", "W8"):
            for e in _repo_edits(w):
                if e.get("id") in X26_IDS:
                    by[e["id"]] = e
        out = []
        for i in X26_IDS:
            e = by[i]
            new = e["new"]
            if i in AM11_SWAPS:   # AM-11: the approval date where the text dates the approval
                was, now = AM11_SWAPS[i]
                assert new.count(was) == 1 and new.count("@PROMOTION_APPROVED_AT") == 0, f"AM-11 anchor {i}"
                new = new.replace(was, now)
            if i == "RE-W7-11":
                out.append({"id": i, "path": e["path"], "new_file": False, "content_from": None,
                            "edits": [{"old": None, "new": new, "count": None, "append": True}],
                            "heading_pattern": r"(?m)^## (?:D\d+|@PROMOTION_D) — `GCFPE-20261027\.1 / 102726\.1 / 56` is promoted"})
            else:
                out.append({"id": i, "path": e["path"], "new_file": False, "content_from": None,
                            "edits": [{"old": e["old"], "new": new, "count": e["count"]}]})
        return out
    raise SystemExit(f"unknown set {name}")


def fill(text: str | None, values: dict) -> str | None:
    if text is None:
        return None
    for k in sorted(values, key=len, reverse=True):
        text = text.replace(k, str(values[k]))
    return text


def repo_guards(paths: set) -> list:
    return [g for g in bc.GUARDS["guards"] if g.get("surface") == "repository"
            and any(p.startswith("repo:") and p[5:] in paths for p in g["prompts"])]


W6_BEFORE = None


def w6_before() -> dict:
    """W6's measured guard counts before and after its edits (W6.json guard_counts_on_fresh_reads.repo)."""
    global W6_BEFORE
    if W6_BEFORE is None:
        r = json.loads((WORK / "W6.json").read_text(encoding="utf-8"))["guard_counts_on_fresh_reads"]["repo"]
        W6_BEFORE = {gid: ba for v in r.values() for gid, ba in v["guards_before_after"].items()}
    return W6_BEFORE


def guard_rows(files: dict, state: str) -> list:
    rows = []
    for g in repo_guards(set(files)):
        path = next(p[5:] for p in g["prompts"] if p.startswith("repo:"))
        text = files.get(path)
        if text is None:
            rows.append({"guard": g["id"], "path": path, "file_present": False,
                         "ok": state == "before" and w6_before().get(g["id"], [None])[0] in (0, None)})
            continue
        c, ok = bc.guard_pass(text, g)
        raw = bc.raw_guard_count(text, g)
        want = w6_before().get(g["id"])
        row = {"guard": g["id"], "kind": g["kind"], "path": path, "count": c, "pass": ok,
               "raw_count_differs": raw != c}
        if state == "before":
            row["w6_before"] = want[0] if want else None
            row["ok"] = want is not None and c == want[0]
        else:
            row["w6_after"] = want[1] if want else None
            row["ok"] = ok and (want is None or c == want[1])
        rows.append(row)
    return rows


def git_show(root: Path, ref: str, path: str) -> bytes | None:
    r = subprocess.run(["git", "-C", str(root), "show", f"{ref}:{path}"], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def read_files(root: Path, units: list) -> dict:
    out = {}
    for u in units:
        p = root / u["path"]
        out[u["path"]] = p.read_text(encoding="utf-8") if p.exists() else None
    return out


def render(root: Path, name: str, values: dict) -> dict:
    """Apply a set in memory. Returns the before files, the after files and per-edit rows; refusals are rows."""
    units = edit_set(name)
    before = read_files(root, units)
    after = dict(before)
    rows, refusals = [], []
    for u in units:
        cur = after.get(u["path"])
        if u["new_file"]:
            if cur is not None:
                refusals.append({"id": u["id"], "refusal": "NEW_FILE_EXISTS"})
                continue
            src = root / u["content_from"]
            if not src.exists():
                refusals.append({"id": u["id"], "refusal": "CONTENT_FROM_MISSING"})
                continue
            cur = src.read_text(encoding="utf-8")
            orig = cur
        else:
            if cur is None:
                refusals.append({"id": u["id"], "refusal": "FILE_MISSING"})
                continue
            orig = before[u["path"]]
        for k, e in enumerate(u["edits"]):
            new = fill(e["new"], values)
            old = fill(e["old"], values)
            row = {"id": f"{u['id']}#{k + 1}", "path": u["path"]}
            left = sorted(set(MARKER.findall(new)))
            if left:
                row.update(refusal="UNFILLED_MARKER", markers=left)
                refusals.append(row)
                rows.append(row)
                continue
            if e.get("append"):
                row["append"] = True
                row["new_present_before"] = occ(cur, new)
                if row["new_present_before"]:
                    row["refusal"] = "APPEND_ALREADY_PRESENT"
                    refusals.append(row)
                else:
                    cur = cur + new
                rows.append(row)
                continue
            row["old_count_before"] = occ(orig, old)
            row["old_count_stated"] = e["count"]
            row["old_count_at_application"] = occ(cur, old)
            if row["old_count_before"] != e["count"] or row["old_count_at_application"] != 1 or e["count"] != 1:
                row["refusal"] = "OLD_COUNT"
                refusals.append(row)
                rows.append(row)
                continue
            cur = cur.replace(old, new, 1)
            rows.append(row)
        after[u["path"]] = cur
    return {"units": units, "before": before, "after": after, "rows": rows, "refusals": refusals}


def after_checks(root: Path, name: str, r: dict, values: dict, main_ref: str) -> dict:
    after = r["after"]
    rows = []
    for u in r["units"]:
        for k, e in enumerate(u["edits"]):
            new, old = fill(e["new"], values), fill(e["old"], values)
            text = after.get(u["path"]) or ""
            row = {"id": f"{u['id']}#{k + 1}", "new_count_after": occ(text, new)}
            if old is not None:
                row["old_count_after"] = occ(text, old)
                row["old_only_in_own_new"] = row["old_count_after"] == occ(new, old)
            row["ok"] = row["new_count_after"] == 1 and row.get("old_only_in_own_new", True)
            rows.append(row)
    res = {"edit_rows": rows, "edits_ok": all(x["ok"] for x in rows)}
    res["guards"] = guard_rows({p: t for p, t in after.items()}, "after")
    res["guards_ok"] = all(g["ok"] for g in res["guards"])
    main = git_show(root, main_ref, V500)
    cur = (root / V500).read_bytes() if (root / V500).exists() else None
    res["v500_equal_to_main"] = main is not None and cur == main
    ok = res["edits_ok"] and res["guards_ok"] and res["v500_equal_to_main"]
    if name == "X1":
        note = next(u for u in r["units"] if u["id"] == "W1-PART-02-NOTE")
        dr = after.get(DR) or ""
        lines = dr.split("\n")
        idx = [i for i, ln in enumerate(lines) if ln == note["note_heading"]]
        d30 = [i for i, ln in enumerate(lines) if ln.startswith(D30_HEAD)]
        res["note_heading_count"] = len(idx)
        res["note_after_d30"] = len(idx) == 1 and len(d30) == 1 and idx[0] > d30[0]
        res["d30_heading_count"] = len(d30)
        ok &= res["note_heading_count"] == 1 and res["note_after_d30"]
    if name == "X26":
        dr_before, dr_after = r["before"].get(DR) or "", after.get(DR) or ""
        u = next(u for u in r["units"] if u["id"] == "RE-W7-11")
        res["promotion_heading_count"] = len(re.findall(u["heading_pattern"], dr_after))
        res["earlier_entries_unchanged"] = dr_after.startswith(dr_before)
        ok &= res["promotion_heading_count"] == 1 and res["earlier_entries_unchanged"]
    res["ok"] = bool(ok)
    return res


def run_check(root: Path, name: str, state: str, values: dict, main_ref: str, before_ref: str = "") -> dict:
    units = edit_set(name)
    if state == "before":
        files = read_files(root, units)
        rows = []
        for u in units:
            if u["new_file"]:
                rows.append({"id": u["id"], "new_file_absent": files[u["path"]] is None,
                             "content_from_present": (root / u["content_from"]).exists(),
                             "ok": files[u["path"]] is None and (root / u["content_from"]).exists()})
                src = (root / u["content_from"]).read_text(encoding="utf-8") if (root / u["content_from"]).exists() else ""
            else:
                src = files[u["path"]] or ""
            for k, e in enumerate(u["edits"]):
                if e.get("append"):
                    left = sorted(set(MARKER.findall(fill(e["new"], values))))
                    rows.append({"id": f"{u['id']}#{k + 1}", "append": True, "markers_unfilled": len(left),
                                 "ok": True})
                    continue
                c = occ(src, fill(e["old"], values))
                rows.append({"id": f"{u['id']}#{k + 1}", "old_count": c, "stated": e["count"], "ok": c == e["count"]})
        # a new file's guards are measured, before, on the file it is written from (W6 measured v5.0.0 so)
        guards = guard_rows({u["path"]: (files[u["path"]] if not u["new_file"] or files[u["path"]] is not None else
                                         ((root / u["content_from"]).read_text(encoding="utf-8")
                                          if (root / u["content_from"]).exists() else None)) for u in units}, "before")
        r = render(root, name, values) if values or name == "X1" else None
        res = {"mode": "check", "set": name, "state": "before", "rows": rows, "rows_ok": all(x["ok"] for x in rows),
               "guards": guards, "guards_ok": all(g["ok"] for g in guards),
               "edits": sum(len(u["edits"]) for u in units), "files": len({u["path"] for u in units})}
        res["ok"] = res["rows_ok"] and res["guards_ok"]
        if r is not None:
            res["in_memory_apply"] = {"refusals": len(r["refusals"]),
                                      "after": {k: v for k, v in after_checks(root, name, r, values, main_ref).items()
                                                if k not in ("edit_rows", "guards")}}
            res["ok"] &= not r["refusals"] and res["in_memory_apply"]["after"]["ok"]
        return res
    # after: the files as they stand are the after state; rebuild the edit list for the counts
    r = {"units": units, "before": {}, "after": read_files(root, units)}
    if name == "X26":   # the decision record before R4 is not on disk any more: the prefix rule reads it at
        if before_ref.startswith("file:"):                 # a saved copy of the decision record before R4
            prev = Path(before_ref[5:]).read_bytes()
        else:
            prev = git_show(root, before_ref or main_ref, DR)  # --before-ref (default --main-ref: X1 merged, R4 not)
        r["before"][DR] = prev.decode("utf-8") if prev is not None else ""
    res = after_checks(root, name, r, values, main_ref)
    return {"mode": "check", "set": name, "state": "after", **res}


def run_apply(root: Path, name: str, values: dict, main_ref: str) -> dict:
    r = render(root, name, values)
    res = {"mode": "apply", "set": name, "rows": r["rows"], "refusals": r["refusals"]}
    if r["refusals"]:
        res.update(ok=False, written=0)
        return res
    chk = after_checks(root, name, r, values, main_ref)
    res["after"] = chk
    if not chk["ok"]:
        res.update(ok=False, written=0)
        return res
    n = 0
    for path, text in r["after"].items():
        if text is not None and text != r["before"].get(path):
            (root / path).parent.mkdir(parents=True, exist_ok=True)
            (root / path).write_text(text, encoding="utf-8")
            n += 1
    res.update(ok=True, written=n)
    return res


# ------------------------------------------------------------------------------------------------- self-test
STANDIN_X26 = {"@PROMOTION_D": "D31", "@PROMOTION_DATE": "2026-10-28", "@REGISTER_TIME": "00:00:00Z",
               "@N_ARCHIVED": "57", "@N_KEPT": "1", "@N_SUCCESSOR": "54", "@MAIN_SHA": "0000000",
               "@PROD_TOKEN": "56 nodes · 240 edges · 56 state_routes · STANDIN bytes · sha256 STANDIN…",
               "@POSTFLIGHT_VERDICT": "STANDIN", "@PROMOTION_APPROVAL_WORDS": "STANDIN",
               "@REGISTER_ENTRY_PAGE_ID": "e" * 32, "@CATALOG_PAGE_ID": "c" * 32, "@PE_PAGE_ID": "f" * 32,
               "@ACTIVATION_DATE": "2026-10-28", "@PROMOTION_APPROVED_AT": "2026-10-27"}   # AM-11: two dates


def _copy(root: Path, dst: Path) -> None:
    """The target files, v5.0.0 and a git repository whose HEAD and main hold them (for --main-ref and HEAD)."""
    paths = {u["path"] for s in ("X1", "X26") for u in edit_set(s) if not u["new_file"]} | {V500}
    for p in paths:
        (dst / p).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(root / p, dst / p)
    env = ["-c", "user.name=selftest", "-c", "user.email=selftest@invalid", "-c", "commit.gpgsign=false"]
    subprocess.run(["git", "init", "-q", "-b", "main", str(dst)], check=True)
    subprocess.run(["git", "-C", str(dst), "add", "-A"], check=True)
    subprocess.run(["git", "-C", str(dst), *env, "commit", "-q", "-m", "selftest"], check=True)


def selftest(root: Path) -> dict:
    cases = {}
    with tempfile.TemporaryDirectory() as t:
        base = Path(t) / "base"
        _copy(root, base)

        def fresh(tag: str) -> Path:
            d = Path(t) / tag
            shutil.copytree(base, d)
            return d
        d = fresh("clean")
        pre = run_check(d, "X1", "before", {}, "main")
        a = run_apply(d, "X1", {}, "main")
        post = run_check(d, "X1", "after", {}, "main")
        cases["clean_x1_before_ok"] = pre["ok"]
        cases["clean_x1_apply_ok"] = a["ok"] and a["written"] == 5
        cases["clean_x1_after_ok"] = post["ok"]
        cases["second_apply_refused"] = not run_apply(d, "X1", {}, "main")["ok"]
        # X26 on top of X1 (the order EXECUTE runs them), with named stand-in values
        cases["x26_unfilled_marker_refused"] = any(x.get("refusal") == "UNFILLED_MARKER"
                                                   for x in run_apply(d, "X26", {}, "main")["refusals"])
        a26 = run_apply(d, "X26", STANDIN_X26, "main")
        cases["x26_apply_with_values_ok"] = a26["ok"]
        # AM-11, each way: the approval date only where the text dates the approval, the promotion date elsewhere
        sv, dr = (d / "docs/prompt_ecosystem_management/authoritative-surfaces.md").read_text(encoding="utf-8"), (d / DR).read_text(encoding="utf-8")
        d31 = dr[dr.find("\n## D31 — "):] if "\n## D31 — " in dr else ""   # earlier entries carry their own dates
        cases["am11_approval_dates_where_approval"] = (occ(sv, "`APPROVED` 2026-10-27 |") == 1 and occ(d31, "**Product Owner, 2026-10-27**") == 1
                                                       and occ(sv, "`APPROVED` 2026-10-28") == 0 and occ(d31, "**Product Owner, 2026-10-28**") == 0
                                                       and occ(d31, "from 00:00:00Z") == 1)
        cases["am11_promotion_date_elsewhere"] = (occ(sv, "moved 2026-10-28, never copied") == 1 and occ(sv, "as built 2026-10-28 |") == 1
                                                  and occ(sv, "and 2026-10-28 by decision D31") == 1 and occ(sv, "promoted 2026-10-28 by Product Owner") == 1)
        raw = {e["id"]: e["new"] for w in ("W7", "W8") for e in _repo_edits(w) if e.get("id") in X26_IDS}
        cases["am11_changes_only_two_markers"] = all(
            u["edits"][0]["new"] == (raw[u["id"]].replace(*AM11_SWAPS[u["id"]]) if u["id"] in AM11_SWAPS else raw[u["id"]])
            and (u["id"] not in AM11_SWAPS or u["edits"][0]["new"] != raw[u["id"]]) for u in edit_set("X26"))
        d2 = fresh("am11")
        run_apply(d2, "X1", {}, "main")
        miss = run_apply(d2, "X26", {k: v for k, v in STANDIN_X26.items() if k != "@PROMOTION_APPROVED_AT"}, "main")
        cases["am11_missing_approved_at_refused"] = (not miss["ok"] and miss.get("written") == 0 and any(
            "@PROMOTION_APPROVED_AT" in x.get("markers", []) for x in miss["refusals"]))

        d = fresh("missing")
        p = d / "docs/prompt_ecosystem_management/reviewer-prompt-template.md"
        p.write_text(p.read_text(encoding="utf-8").replace('artifact_version: "1.2"', 'artifact_version: "1.2a"'), encoding="utf-8")
        snap = {q: q.read_bytes() for q in (d / "docs").rglob("*.md")}
        cases["missing_anchor_refused"] = (not run_apply(d, "X1", {}, "main")["ok"]
                                           and all(q.read_bytes() == b for q, b in snap.items())
                                           and not (d / next(u["path"] for u in edit_set("X1") if u["new_file"])).exists())
        d = fresh("doubled")
        p = d / "docs/prompt_ecosystem_management/ecosystem-change-management.md"
        p.write_text(p.read_text(encoding="utf-8") + '\nartifact_version: "1.2"\n', encoding="utf-8")
        cases["doubled_anchor_refused"] = not run_apply(d, "X1", {}, "main")["ok"]
        d = fresh("exists")
        v51 = next(u["path"] for u in edit_set("X1") if u["new_file"])
        (d / v51).write_text("x\n", encoding="utf-8")
        cases["existing_v510_refused"] = not run_apply(d, "X1", {}, "main")["ok"]
        d = fresh("forbidden")
        run_apply(d, "X1", {}, "main")
        p = d / "docs/prompt_ecosystem_management/reviewer-prompt-template.md"
        p.write_text(p.read_text(encoding="utf-8") + "\nRead the decision record D20-D26.\n", encoding="utf-8")
        cases["surviving_forbidden_line_fails"] = not run_check(d, "X1", "after", {}, "main")["guards_ok"]
        d = fresh("required")
        run_apply(d, "X1", {}, "main")
        p = d / "docs/prompt_ecosystem_management/skill-identity-and-freeze.md"
        p.write_text(p.read_text(encoding="utf-8").replace("**One revision, two trees:", "**One revision:"), encoding="utf-8")
        cases["missing_required_line_fails"] = not run_check(d, "X1", "after", {}, "main")["guards_ok"]
        d = fresh("note")
        run_apply(d, "X1", {}, "main")
        p = d / DR
        s = p.read_text(encoding="utf-8")
        note = next(u for u in edit_set("X1") if u["id"] == "W1-PART-02-NOTE")["edits"][0]["new"][len(D30_CLOSE):]
        s = s.replace(note, "")
        i = s.index(D30_HEAD)
        p.write_text(s[:i] + note.lstrip("\n") + "\n" + s[i:], encoding="utf-8")   # where W1's stored anchor puts it
        chk = run_check(d, "X1", "after", {}, "main")
        cases["note_before_d30_fails"] = not chk["ok"] and chk["note_after_d30"] is False
        d = fresh("v500")
        run_apply(d, "X1", {}, "main")
        (d / V500).write_text((d / V500).read_text(encoding="utf-8") + "x\n", encoding="utf-8")
        cases["changed_v500_fails"] = not run_check(d, "X1", "after", {}, "main")["v500_equal_to_main"]
        d = fresh("rewrite")
        run_apply(d, "X1", {}, "main")
        r = render(d, "X26", STANDIN_X26)
        r["after"][DR] = r["after"][DR].replace("## D29 — ", "## D29 (edited) — ", 1)
        cases["x26_earlier_entry_rewrite_fails"] = not after_checks(d, "X26", r, STANDIN_X26, "main")["earlier_entries_unchanged"]
    return {"mode": "selftest", "cases": cases, "cases_passed": sum(bool(v) for v in cases.values()),
            "cases_total": len(cases), "ok": all(cases.values())}


def main() -> int:
    ap = argparse.ArgumentParser(prog="repo_edits_102726.py")
    sub = ap.add_subparsers(dest="mode", required=True)
    for m in ("apply", "check"):
        p = sub.add_parser(m)
        p.add_argument("--set", required=True, choices=["X1", "X26"])
        p.add_argument("--root", required=True)
        p.add_argument("--values")
        p.add_argument("--stand-in-values", action="store_true", help="PLAN dry run only: STANDIN_X26 for X26")
        p.add_argument("--main-ref", default="origin/main")
        if m == "check":
            p.add_argument("--state", required=True, choices=["before", "after"])
            p.add_argument("--before-ref", default="", help="X26 after: the ref holding the decision record before R4, or file:<path> of a copy")
    s = sub.add_parser("selftest")
    s.add_argument("--root", default=str(HERE.parents[5]))
    a = ap.parse_args()
    if a.mode == "selftest":
        res = selftest(Path(a.root))
    else:
        values = json.loads(Path(a.values).read_text(encoding="utf-8")) if a.values else {}
        if a.stand_in_values:
            if a.mode == "apply" and (Path(a.root).resolve() == HERE.parents[5].resolve()):
                raise SystemExit("stand-in values are refused on the real tree")
            values = {**STANDIN_X26, **values}
        root = Path(a.root)
        res = run_apply(root, a.set, values, a.main_ref) if a.mode == "apply" else \
            run_check(root, a.set, a.state, values, a.main_ref, a.before_ref)
        res["stand_in_values"] = bool(a.stand_in_values)
    res["d22"] = "repository files only; counts, ids and booleans"
    print(json.dumps(res, indent=1, ensure_ascii=False))
    return 0 if res["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
