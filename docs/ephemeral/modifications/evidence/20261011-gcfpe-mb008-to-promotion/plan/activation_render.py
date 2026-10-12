#!/usr/bin/env python3
"""Activation rendering for MODIFICATION-20261011-gcfpe-mb008-to-promotion (PLAN §7, X6a, X15, X16; P-B1-R, DIFF-1,
DIFF-2 and L-9 of the PLAN diff check).

  activation_render.py plan  --parts P [--pages ID ...] [--set @KEY=VALUE ...] [--pin ID=TS ...] [--fetched-after T]
                             [--emit]
        On the newest fresh read of each page in activation-ops.json: refuse a revision other than its pin; build its
        operations (the file's own, plus the generated ones: each member row's title and binding from the candidate
        parts, and the frontmatter rule); apply them in memory, refusing an anchor that does not resolve exactly once or
        a batch that is not safe; then run control_check.py's checks on the rendered text with the page's planned
        title. Also renders the two new pages (the catalog, checked like a control page with --catalog, and the
        register entry) from the parts and the 2026-10-09 registry proposal. --emit adds each operation's old_str and
        new_str and the new pages' content, for EXECUTE's writes: terminal only, never redirected into the repository.
  activation_render.py check --parts P [--pages ID ...] [--set ...] [--fetched-after T]
        After the writes, on fresh reads: every operation LANDED by its anchor counts, and control_check.py's checks pass
        on the page as it is.
  activation_render.py selftest --parts P
        the renderer on synthetic pages: a clean page renders and passes; a missing anchor, a doubled anchor, an
        unfilled marker and a rendered page that keeps a retired value each fail.

Control-page text is read as a transient read of this session's harness records (control_check.latest); the report
carries counts, ids and booleans. Run with PYTHONDONTWRITEBYTECODE=1 and CLAUDE_CODE_SESSION_ID set.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import body_check as B  # noqa: E402
import control_check as C  # noqa: E402

OPS = json.loads((HERE / "activation-ops.json").read_text(encoding="utf-8"))
EVIDENCE = HERE.parent.parent
PROPOSAL = EVIDENCE / "20261009-gcfpe-latest-alpha-analysis/execute/candidate-registry-nonderived.json"
MARKER = re.compile(r"@[A-Z][A-Z0-9_]+(?::[A-Z0-9-]+)?")
REGISTER, FI = "3d24590a05eb81ce942ad994cfca9fa1", "3db4590a05eb81de9736ea69bac61016"


def nodes(parts_dir: str) -> dict:
    out = {}
    for f in sorted(Path(parts_dir, "prompts").glob("*.json")):
        part = json.loads(f.read_text(encoding="utf-8"))
        out[part["id"]] = part["node"]
    return out


def fill(text: str, values: dict, parts: dict) -> str:
    def one(m):
        key = m.group(0)
        if key.startswith("@SUCC_URL:"):
            node = parts.get(key.split(":", 1)[1])
            return node["candidate_url"].split("?")[0] if node else key
        return str(values[key]) if key in values else key
    return MARKER.sub(one, text)


def frontmatter(text: str) -> list:
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return []
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), 0)
    return lines[1:end]


def generated(pid: str, page: dict, text: str, parts: dict) -> list:
    out = []
    if page.get("frontmatter_rule"):
        fm = frontmatter(text)
        for old, new in OPS["frontmatter_rule"].items():
            if old in fm:
                out.append({"id": f"FM:{old.split(':')[0]}", "start": old, "end": None, "new": new})
        if page.get("frontmatter_title"):
            old, new = page["frontmatter_title"]
            out.append({"id": "FM:title", "start": old, "end": None, "new": new})
    if page.get("member_rows"):
        for key, node in parts.items():
            pred = node["predecessor"]
            pred_id = pred["notion_page_id"].replace("-", "")
            title_cell = f"<td>{pred['title']}</td>"
            url_cell = f"<td>`https://app.notion.com/p/{pred_id}?pvs=204`</td>"
            if title_cell in text:
                out.append({"id": f"ROW:{key}:title", "start": title_cell, "end": None, "new": f"<td>{node['title']}</td>"})
            if url_cell in text:
                out.append({"id": f"ROW:{key}:url", "start": url_cell, "end": None, "new": f"<td>`{node['candidate_url']}`</td>"})
    return out


def apply(text: str, ops: list, values: dict, parts: dict):
    """Each operation in order: its span must resolve exactly once in the text as it stands, and its old_str must occur
    afterwards only inside its own new_str. Returns (text, rows)."""
    rows = []
    for op in ops:
        new = fill(op["new"], values, parts)
        row = {"id": op["id"], "applied": False, "refusal": None}
        left = MARKER.findall(new)
        if left:
            row["refusal"] = "UNFILLED_MARKER"
            rows.append(row)
            continue
        span, why = B.resolve(text, op)
        if span is None:
            row["refusal"] = why
            rows.append(row)
            continue
        old = text[span[0]:span[1]]
        after = text[:span[0]] + new + text[span[1]:]
        row["old_str_once_at_application"] = B.occ(text, old) == 1
        row["old_str_only_in_own_new_after"] = B.occ(after, old) == B.occ(new, old)
        row["applied"] = row["old_str_once_at_application"] and row["old_str_only_in_own_new_after"]
        if row["applied"]:
            text = after
            row["old_str"], row["new_str"] = old, new
        else:
            row["refusal"] = "BATCH_UNSAFE"
        rows.append(row)
    return text, rows


def catalog_text(parts: dict, values: dict) -> str:
    prop = json.loads(PROPOSAL.read_text(encoding="utf-8"))["prompts"]
    rows = []
    for r in prop:
        node = parts[r["prompt_key"]]
        rows += ["<tr>", f"<td>`{r['prompt_key']}`</td>", f"<td>{node['title']}</td>", f"<td>`{r['lane']}`</td>",
                 f"<td>`{node['candidate_url']}`</td>", "<td>`100926.1`</td>", "</tr>"]
    lines = [
        "---", "artifact_type: GCFPE_SELECTED_CATALOG", 'artifact_version: "100926.1"',
        'title: "Glow HDE Complete Prompt Set — GCFPE-20261009.1 — 100926.1"', "selected_release: GCFPE-20261009.1",
        'prompt_version_family: "100926.1"', "selected_member_count: 55", "status: REGISTER_CONTROLLED",
        "selection_authority: GCFPE Membership and Release Register",
        'selection_authority_url: "<mention-page url="https://app.notion.com/p/3d24590a05eb81ce942ad994cfca9fa1"/>"',
        'selection_rule: "This catalog is operative if and only if the register selects GCFPE-20261009.1 / 100926.1 / 55. It does not assert its own selection."',
        "activation_authority: Nathan / Product Owner", "activated_at: @ACTIVATION_DATE",
        "predecessor_release: GCFPE-20260914.1", 'predecessor_version_family: "091426.1"',
        "predecessor_catalog: 3db4590a05eb81738ef1d846e3c0df8c", "mutation_posture: SELECTED_PRODUCTION",
        "source_modification: MODIFICATION-20261011-gcfpe-mb008-to-promotion", "promotion_authorized: true",
        "validation_status: VALIDATED",
        'validation_evidence: "the D24 skill review and the independent post-flight recorded in MODIFICATION-20261011-gcfpe-mb008-to-promotion; the register states their verdicts and records"',
        "---", "# Glow HDE Complete Prompt Set — GCFPE-20261009.1", "Release: `GCFPE-20261009.1`  ",
        "Prompt version family: `100926.1`  ", "Exact selected member count: `55`  ",
        'Selection status: `REGISTER_CONTROLLED` — resolve selection from <mention-page url="https://app.notion.com/p/3d24590a05eb81ce942ad994cfca9fa1"/>. This page does not assert its own selection.',
        "It lists a `100926.1` successor for each of the 55 predecessor logical IDs; `GCFPE-MGMT-10`'s is the D20 three-mode body. No member was added or removed.",
        "## Selected membership", '<table header-row="true">', "<tr>", "<td>ID</td>", "<td>Selected prompt</td>",
        "<td>Lane</td>", "<td>Binding</td>", "<td>current_version</td>", "</tr>", *rows, "</table>",
        "## Release rule",
        "A release's membership and each member's current version live in the register and this catalog; bodies carry no release-bound header line (`D23-G`). All 55 members are `100926.1`.",
    ]
    return fill("\n".join(lines), values, parts)


def register_entry_text(parts: dict, values: dict) -> str:
    ev = "docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion"
    steps = [("X15", "successor bindings prepared and read back", "pending"),
             ("X16", "this register's selection updated last", "pending"),
             ("X17", "the six packages installed; installed digests equal the reviewed ones", "pending"),
             ("X18", "production validation on the activated state", "pending"),
             ("X19", "the 57 predecessor pages archived intact, by move", "pending")]
    lines = [
        "---", "artifact_type: GCFPE_RELEASE_REGISTER_ENTRY", 'artifact_version: "20261009.1"',
        'title: "GCFPE Membership and Release Register Entry — GCFPE-20261009.1"', "selected_release: GCFPE-20261009.1",
        'prompt_version_family: "100926.1"', "selected_member_count: 55", "status: REGISTER_CONTROLLED",
        "selection_authority: GCFPE Membership and Release Register",
        'selection_authority_url: "<mention-page url="https://app.notion.com/p/3d24590a05eb81ce942ad994cfca9fa1">GCFPE Membership and Release Register</mention-page>"',
        "activation_authority: Nathan / Product Owner", "activated_at: @ACTIVATION_DATE",
        "predecessor_release: GCFPE-20260914.1", 'predecessor_version_family: "091426.1"',
        "mutation_posture: SELECTED_PRODUCTION", "source_modification: MODIFICATION-20261011-gcfpe-mb008-to-promotion",
        "promotion_authorized: true", "validation_status: VALIDATED", "---",
        "# Register transaction — GCFPE-20261009.1",
        f"Nathan / Product Owner approved promotion of the exact snapshot in `{ev}/execute/PROMOTION-PACKET.md` on @PROMOTION_APPROVED_AT; the words are quoted in §E of `MODIFICATION-20261011-gcfpe-mb008-to-promotion`. Each step below is recorded when it completes and is read back; a step not marked done has not happened.",
        '<table header-row="true">', "<tr>", "<td>step</td>", "<td>what</td>", "<td>state</td>", "</tr>",
    ]
    for s, what, state in steps:
        lines += ["<tr>", f"<td>{s}</td>", f"<td>{what}</td>", f"<td>{state}</td>", "</tr>"]
    lines += ["</table>"]
    return fill("\n".join(lines), values, parts)


def run_plan(a, check_mode=False) -> dict:
    parts = nodes(a.parts)
    values = dict(item.split("=", 1) for item in a.set)
    pins = dict(item.split("=", 1) for item in a.pin)
    archive, members = C.archive_set(a.parts), C.hub_members(a.parts)
    root, session = os.path.expanduser("~/.claude/projects"), os.environ.get("CLAUDE_CODE_SESSION_ID")
    out, ok = [], True
    for pid, page in OPS["pages"].items():
        if a.pages and pid not in a.pages:
            continue
        got = C.latest(pid, root, session, a.since_minutes, a.fetched_after)
        if got is None:
            out.append({"page": pid, "error": "NO_FETCH_FOUND", "ok": False})
            ok = False
            continue
        text = got[3]
        ops = page["ops"] + generated(pid, page, text, parts)
        row = {"page": pid, "step": page["step"], "name": page["name"], "as_of": got[1],
               "ops_listed": len(page["ops"]), "ops_generated": len(ops) - len(page["ops"])}
        if check_mode:
            filled = [{**o, "new": fill(o["new"], values, parts)} for o in page["ops"]]
            states = {o["id"]: B.state(text, o) for o in filled}
            row["landed"] = sum(s == "LANDED" for s in states.values())
            row["not_landed"] = sorted(k for k, s in states.items() if s != "LANDED")
            rendered, title = text, got[2]
            row["revision_moved"] = got[1] != pins.get(pid, page["pin"])
        else:
            pin = pins.get(pid, page["pin"])
            row["revision_matches_pin"] = got[1] == pin
            rendered, rows = apply(text, ops, values, parts)
            row["applied"] = sum(r["applied"] for r in rows)
            row["refused"] = [{"id": r["id"], "refusal": r["refusal"]} for r in rows if not r["applied"]]
            row["batch_safe"] = not row["refused"]
            title = page["title"] or got[2]
            if a.emit:
                row["ops_payload_for_execute"] = [{"id": r["id"], "old_str": r["old_str"], "new_str": r["new_str"]}
                                                  for r in rows if r["applied"]]
        if "check" in page:
            present = [fill(s, values, parts) for s in page["check"]["present"]]
            row["inventory_check"] = (all(s in rendered for s in present)
                                      and not any(s in rendered for s in page["check"]["absent"]))
            row["ok"] = row["inventory_check"]
        else:
            res = C.check_text(pid, title, rendered, archive, members, "activation", "")
            row["findings_after"] = res["findings"]
            row["finding_sections"] = sorted({f["section"] for f in res["finding_rows"]})
            row["positives"] = {k: res[k] for k in ("title_ok", "successors_missing", "current_selection_ok") if k in res}
            row["ok"] = res["ok"]
        if check_mode:
            row["ok"] = row["ok"] and not row["not_landed"] and row["revision_moved"]
        else:
            row["ok"] = row["ok"] and row["revision_matches_pin"] and row["batch_safe"]
        ok &= row["ok"]
        out.append(row)
    new_pages = {}
    if not check_mode and not a.pages:
        cat = catalog_text(parts, values)
        res = C.check_text("CATALOG", OPS["new_pages"]["CATALOG"]["title"], cat, archive, members, "activation", "CATALOG")
        new_pages["CATALOG"] = {"findings": res["findings"], "catalog_successors_missing": res.get("catalog_successors_missing"),
                                "markers_left": MARKER.findall(cat), "ok": res["ok"] and not MARKER.findall(cat)}
        ent = register_entry_text(parts, values)
        new_pages["REGISTER_ENTRY"] = {"markers_left": MARKER.findall(ent), "ok": not MARKER.findall(ent)}
        if a.emit:
            new_pages["CATALOG"]["content"], new_pages["REGISTER_ENTRY"]["content"] = cat, ent
        ok &= all(v["ok"] for v in new_pages.values())
    return {"mode": "check" if check_mode else "plan", "pages": out, "new_pages": new_pages, "ok": ok,
            "d22": "transient reads of this session's harness records; control pages only; counts, ids and booleans"}


def selftest(parts_dir: str) -> dict:
    parts = nodes(parts_dir)
    archive, members = C.archive_set(parts_dir), C.hub_members(parts_dir)
    key, node = next((k, n) for k, n in parts.items() if k != "GCFPE-MGMT-10")
    pred = node["predecessor"]
    pid = pred["notion_page_id"].replace("-", "")
    page = {"member_rows": True, "ops": []}
    base = (f"## Selected topology\n<td>{pred['title']}</td>\n<td>`https://app.notion.com/p/{pid}?pvs=204`</td>\n"
            "## Native flow changes\nThe register selected `GCFPE-20260914.1` once.\n")
    good_op = {"id": "S1", "start": "The register selected `GCFPE-20260914.1` once.", "end": None,
               "new": "The register selects `GCFPE-20261009.1` (@ACTIVATION_DATE)."}
    vals = {"@ACTIVATION_DATE": "2026-10-12"}

    def render(text, ops, values):
        t, rows = apply(text, ops + generated("SYN", page, text, parts), values, parts)
        res = C.check_text("SYN", "SYN", t, archive, {}, "activation", "")
        return t, rows, res
    t1, r1, c1 = render(base, [good_op], vals)
    cases = {
        "clean_page_renders_and_passes": all(r["applied"] for r in r1) and c1["findings"] == 0 and len(r1) == 3,
        "missing_anchor_refused": not render(base, [{**good_op, "start": "absent anchor"}], vals)[1][0]["applied"],
        "doubled_anchor_refused": not render(base + "The register selected `GCFPE-20260914.1` once.\n", [good_op], vals)[1][0]["applied"],
        "unfilled_marker_refused": render(base, [good_op], {})[1][0]["refusal"] == "UNFILLED_MARKER",
        "kept_retired_value_fails": render(base, [], vals)[2]["findings"] > 0,
        "second_render_changes_nothing": not any(r["applied"] for r in apply(t1, [good_op] + generated("SYN", page, t1, parts), vals, parts)[1]),
    }
    return {"mode": "selftest", "cases": cases, "ok": all(cases.values())}


def main() -> int:
    ap = argparse.ArgumentParser(prog="activation_render.py")
    sub = ap.add_subparsers(dest="mode", required=True)
    for name in ("plan", "check"):
        p = sub.add_parser(name)
        p.add_argument("--parts", required=True)
        p.add_argument("--pages", nargs="*")
        p.add_argument("--set", action="append", default=[], help="@KEY=VALUE")
        p.add_argument("--pin", action="append", default=[], help="PAGE_ID=LAST_EDITED (PE at X15: its X6 revision)")
        p.add_argument("--fetched-after", default="")
        p.add_argument("--since-minutes", type=int, default=600)
        p.add_argument("--emit", action="store_true")
    s = sub.add_parser("selftest")
    s.add_argument("--parts", required=True)
    a = ap.parse_args()
    res = selftest(a.parts) if a.mode == "selftest" else run_plan(a, check_mode=(a.mode == "check"))
    print(json.dumps(res, indent=1, ensure_ascii=False))
    return 0 if res["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
