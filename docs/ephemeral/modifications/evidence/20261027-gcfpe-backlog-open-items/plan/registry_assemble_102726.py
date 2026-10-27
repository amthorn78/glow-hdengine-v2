#!/usr/bin/env python3
"""The GCFPE-PCR-20261027.1 Project Prompt Contract Registry (102726.1 / 56), assembled for
MODIFICATION-20261027-gcfpe-backlog-open-items (PLAN, PART-24; W7 tooling.precedent_scripts "plan/registry_assemble.py",
W7-D9). Adapted from docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/plan/registry_assemble.py.

  registry_assemble_102726.py build --stage candidate|selected --base-registry B --audit-root A --graph-contract G
                                    --parts P --map M --revisions R --out FILE [--stand-in-ok] [--set @MARKER=VALUE ...]
        Rows, in the base registry's order with CL-05 inserted before CL-20:
          1. B is the selected GCFPE-PCR-20261009.1 registry on `main` (W7-D9; no proposal file); the build refuses any
             other registry_id, status or row count;
          2. for each SUCCESSOR in the map (M, successor_map_102726.py's checks): notion_page_id, notion_url,
             expected_title and source_snapshot.notion_url from the map; controlling_sources and supersedes moved to
             the successor (supersedes = the 100926.1 page); KEPT rows (GCFPE-MGMT-10) keep theirs;
          3. CL-05's row is W5 RE-4's registry_row with its markers filled from the map, and its assertions copied by
             script from the CL-C-10 row as RE-4 lists them (each selector must match exactly one assertion);
          4. hand-authored field edits, count-checked: W4's QA-80 inputs item; W5 RE-4 other_rows (CL-C-10 and CL-E-10
             inputs gain CLOSE_MUTATION_SET_RESULT); W5's header member fact (the disposition's "all 55 rows");
          5. outputs[].states, outputs[].consumers and required_interfaces from the shipped registry_deriver's derive()
             on P (the candidate parts); a row with several outputs keeps the base split and is refused if the union
             moved;
          6. expected_parent_title and lane titles retitled by registry-header-102726.1.json's title_suffix, refused
             outside control_titles;
          7. source_snapshot.page_last_edited_at from R (EXECUTE: the landing-check report; PLAN: a stand-in);
          8. this plan's guards in registry form (body_check.py `registry --emit`, on the map) appended to
             audit_assertions, an identical assertion once.
        The header is B's with registry-header-102726.1.json's set applied and the stage's values filled. The YAML is
        written by yaml.safe_dump and read back by the audit's own load_data; refused unless equal; refused with any
        unfilled `@` marker.
  registry_assemble_102726.py check --stage S --registry FILE --audit-root A --graph-contract G --parts P
        validate_project_registry: no error; registry_deriver drift(): none; 56 rows, 56 ACTIVE; header values as
        registry-header states; no `@` marker; parent titles in control_titles.
  registry_assemble_102726.py assertions --registry FILE --audit-root A --synthetic --inject
        PLAN form (no body is read): through the shipped engine, each row's required assertions are reported on a
        text that lacks them, and the two release-wide forbidden assertions (SRC-001 `Prompt version:` and CTR-001
        CONTROL_NOTION) are not reported on that text and are reported when a violating line is added. Body-level
        assertions (every page as read, every operation LANDED) are EXECUTE's and A5's: the precedent's body mode
        is kept (--landed / --page / --shared) and is not run in PLAN.
  registry_assemble_102726.py compare CANDIDATE SELECTED --audit-root A
        the stages differ only at status, approved_by and approved_at.
  registry_assemble_102726.py selftest --base-registry B --audit-root A --graph-contract G --parts P --map M
                                       --revisions R --scratch DIR [--stand-in-ok] [--set ...]
        each injected defect is refused or reported.

Writes only --out (and, for selftest, DIR). Run with PYTHONDONTWRITEBYTECODE=1.
"""
from __future__ import annotations

import argparse
import copy
import importlib.util
import json
import os
import re
import shutil
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
HEADER = json.loads((HERE / "registry-header-102726.1.json").read_text(encoding="utf-8"))
W4 = json.loads((HERE / "work/W4.json").read_text(encoding="utf-8"))
W5 = json.loads((HERE / "work/W5.json").read_text(encoding="utf-8"))
RE4 = next(e for e in W5["repo_edits"] if e.get("id") == "RE-4")
MARKER = re.compile(r"@[A-Z][A-Z0-9_]+")
ASSERTION_KEYS = ("required_literals", "forbidden_literals", "required_regex", "forbidden_regex")
BASE_REGISTRY_ID, BASE_ROWS = "GCFPE-PCR-20261009.1", 55
OLD_REL, NEW_REL, OLD_VER, NEW_VER = "GCFPE-20261009.1", "GCFPE-20261027.1", "100926.1", "102726.1"
ROWS = 56
ADDED, INSERT_BEFORE = "CL-05", "CL-20"


def _module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(path.parent))
    try:
        spec.loader.exec_module(mod)
    finally:
        sys.path.pop(0)
    return mod


def audit(root: str):
    return _module(Path(root) / "scripts" / "audit_workspace_governance.py", "audit_workspace_governance")


def deriver(root: str):
    return _module(Path(root) / "scripts" / "registry_deriver.py", "registry_deriver")


def smap_module():
    return _module(HERE / "successor_map_102726.py", "successor_map_102726")


def plan_assertions(map_path: str) -> dict:
    """body_check.py registry --emit, on the map (the merged guards in registry form)."""
    import subprocess
    # PYTHONHASHSEED=0: binding_pass.regenerated_guards builds G-W8-NAME-1's alternation from a set, so its order (not
    # its matches) follows the hash seed; a fixed seed makes the emitted registry bytes reproducible (A3 finding).
    p = subprocess.run([sys.executable, str(HERE / "body_check.py"), "registry", "--successor-map", map_path, "--emit"],
                       capture_output=True, text=True,
                       env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "PYTHONHASHSEED": "0"})
    if p.returncode != 0:
        sys.exit(f"registry_assemble: body_check.py registry --emit failed: {p.stdout[-300:]}{p.stderr[-300:]}")
    out = json.loads(p.stdout)
    return out["assertions"], bool(out.get("stand_in"))


def fill(value, values: dict):
    if isinstance(value, dict):
        return {k: fill(v, values) for k, v in value.items()}
    if isinstance(value, list):
        return [fill(v, values) for v in value]
    if isinstance(value, str):
        if value in values:
            return fill(values[value], values)
        return MARKER.sub(lambda m: str(values[m.group(0)]) if m.group(0) in values else m.group(0), value)
    return value


def markers_left(value) -> list:
    return sorted(set(MARKER.findall(json.dumps(value, ensure_ascii=False, default=str))))


def stage_values(stage: str, extra: dict) -> dict:
    values = dict(HEADER["stages"][stage])
    values.update(extra)
    return values


def retitle(title: str) -> str:
    old, new = HEADER["title_suffix"]["old"], HEADER["title_suffix"]["new"]
    if not title.endswith(old) and not title.endswith(new):
        sys.exit(f"registry_assemble: parent title outside the release: {title}")
    out = title[: -len(old)] + new if title.endswith(old) else title
    if out not in HEADER["control_titles"].values():
        sys.exit(f"registry_assemble: parent title not in control_titles: {out}")
    return out


def _put(obj, path, value):
    for key in path[:-1]:
        obj = obj[key]
    obj[path[-1]] = value


def _add(assertions: dict, extra: dict) -> int:
    added = 0
    for key in ("required_regex", "forbidden_regex"):
        have = {(a["rule_id"], a["value"]) for a in assertions.get(key) or []}
        for a in extra.get(key, []):
            if (a["rule_id"], a["value"]) not in have:
                assertions.setdefault(key, []).append(a)
                have.add((a["rule_id"], a["value"]))
                added += 1
    return added


def url(page_id: str, pvs: bool = False) -> str:
    return f"https://app.notion.com/p/{page_id}" + ("?pvs=204" if pvs else "")


def replace_one(items: list, old: str, new: str, what: str) -> list:
    hits = [i for i, x in enumerate(items) if x == old]
    if len(hits) != 1:
        sys.exit(f"registry_assemble: {what}: expected one item {old[:60]!r}, found {len(hits)}")
    out = list(items)
    out[hits[0]] = new
    return out


def yaml_item(text: str) -> str:
    """A rendered YAML list item (`  - a\\n    b`) as its folded value."""
    t = text.strip()
    if t.startswith("- "):
        t = t[2:]
    return " ".join(t.split())


# ---------------------------------------------------------------------------------------- the CL-05 row
def cl05_row(base_rows: dict, smap: dict) -> dict:
    spec = copy.deepcopy(RE4["registry_row"])
    row_map = smap["members"][ADDED]
    pid = row_map["page_id"]
    marker = "<CL-05 102726.1 page id>"

    def sub(v):
        if isinstance(v, str):
            return v.replace(marker, pid)
        if isinstance(v, list):
            return [sub(x) for x in v]
        if isinstance(v, dict):
            return {k: sub(x) for k, x in v.items()}
        return v
    row = {k: sub(v) for k, v in spec.items() if k not in ("audit_assertions", "outputs", "required_interfaces", "source_snapshot")}
    if row["expected_title"] != row_map["title"]:
        sys.exit("registry_assemble: CL-05's RE-4 title differs from the map's")
    row["outputs"] = [{"artifact": o["artifact"], "states": [], "consumers": []} for o in spec["outputs"]]
    row["required_interfaces"] = []
    row["source_snapshot"] = {"completeness": "COMPLETE", "notion_url": url(pid, True), "page_last_edited_at": None,
                              "representation": "NOTION_READBACK_METADATA_ONLY_NO_BODY_COPY"}
    src = base_rows["CL-C-10"]["audit_assertions"]
    a = {"forbidden_literals": [], "forbidden_regex": copy.deepcopy(src.get("forbidden_regex") or [])}
    if len(a["forbidden_regex"]) != 34:
        sys.exit(f"registry_assemble: RE-4 copies CL-C-10's 34 forbidden_regex; found {len(a['forbidden_regex'])}")
    lit_sel = [("PF10", "CTR-002"), ("NEXT_PROMPT_HANDOFF", "TOP-001"), ("Canon relied on", "AF-024-CANON")]
    a["required_literals"] = []
    for value, rule in lit_sel:
        hits = [x for x in src.get("required_literals") or []
                if (x.get("value") if isinstance(x, dict) else x) == value and (not isinstance(x, dict) or x.get("rule_id") == rule)]
        if len(hits) != 1:
            sys.exit(f"registry_assemble: CL-C-10 required_literals {value}/{rule}: {len(hits)} matches")
        a["required_literals"].append(copy.deepcopy(hits[0]))
    rx_sel = [("value", "docs/pfcanon/"), ("value", "never\\s+carries\\s+the\\s+only\\s+copy"),
              ("value", "The final response ends with the `?NEXT_PROMPT_HANDOFF`? block\\."),
              ("value", "never\\s+as\\s+a\\s+subagent\\s+of\\s+another\\s+session"), ("guard", "G-TS-1"), ("guard", "G-TS-2")]
    a["required_regex"] = []
    for field, needle in rx_sel:
        hits = [x for x in src.get("required_regex") or []
                if (needle in str(x.get("value")) if field == "value" else x.get("guard") == needle)]
        if len(hits) != 1:
            sys.exit(f"registry_assemble: CL-C-10 required_regex selector {needle!r}: {len(hits)} matches")
        a["required_regex"].append(copy.deepcopy(hits[0]))
    row["audit_assertions"] = a
    return row


# ---------------------------------------------------------------------------------------------- assemble
def assemble(a) -> tuple[dict, dict]:
    A, D, SM = audit(a.audit_root), deriver(a.graph_contract), smap_module()
    smap = SM.load(a.map, str(HERE / "members-100926.1.tsv"), a.stand_in_ok)
    base = A.load_data(Path(a.base_registry))
    if base.get("registry_id") != BASE_REGISTRY_ID or base.get("status") != "APPROVED" or len(base["prompts"]) != BASE_ROWS:
        sys.exit("registry_assemble: the base is not the selected GCFPE-PCR-20261009.1 registry (55 rows, APPROVED)")
    plan, plan_stand_in = plan_assertions(a.map)
    parts = D.load_parts(a.parts)
    revisions = load_revisions(a.revisions)
    values = stage_values(a.stage, dict(item.split("=", 1) for item in a.set))
    base_rows = {r["prompt_key"]: r for r in base["prompts"]}
    order = [r["prompt_key"] for r in base["prompts"]]
    if set(smap["members"]) != set(order) | {ADDED}:
        sys.exit("registry_assemble: the map's members are not the base rows plus CL-05")
    order.insert(order.index(INSERT_BEFORE), ADDED)
    report = {"successor_rows": 0, "kept_rows": [], "added_rows": [], "hand_edits": [], "plan_assertions_added": 0}
    qa80_old = yaml_item(next(e for e in W4["repo_edits"] if e.get("part") == "PART-10" and e.get("old"))["old"])
    qa80_new = yaml_item(next(e for e in W4["repo_edits"] if e.get("part") == "PART-10" and e.get("old"))["new"])
    rows = []
    for key in order:
        m = smap["members"][key]
        if key == ADDED:
            row = cl05_row(base_rows, smap)
            report["added_rows"].append(key)
            template = base_rows["CL-C-10"]
        else:
            row = copy.deepcopy(base_rows[key])
            template = base_rows[key]
            if m["disposition"] == "SUCCESSOR":
                if row["notion_page_id"] != m["predecessor_page_id"]:
                    sys.exit(f"registry_assemble: {key}: the base row's page is not the map's predecessor")
                old_url = row["notion_url"]
                row["notion_page_id"], row["notion_url"], row["expected_title"] = m["page_id"], url(m["page_id"]), m["title"]
                cs = row["controlling_sources"]
                for old, new in ((OLD_REL, NEW_REL), (OLD_VER, NEW_VER), (old_url + "?pvs=204", url(m["page_id"], True))):
                    cs = replace_one(cs, old, new, f"{key} controlling_sources")
                row["controlling_sources"] = cs
                row["supersedes"] = [old_url + "?pvs=204"]
                row["superseded_by"] = None
                row["source_snapshot"]["notion_url"] = url(m["page_id"], True)
                report["successor_rows"] += 1
            elif m["disposition"] == "KEPT":
                if row["notion_page_id"] != m["page_id"]:
                    sys.exit(f"registry_assemble: {key}: KEPT row's page differs from the map")
                report["kept_rows"].append(key)
            else:
                sys.exit(f"registry_assemble: {key}: unexpected disposition {m['disposition']}")
        if key == "QA-80":
            row["inputs"] = replace_one(row["inputs"], qa80_old, qa80_new, "QA-80 inputs (W4 PART-10)")
            report["hand_edits"].append("QA-80 inputs (W4 PART-10)")
        if key in ("CL-C-10", "CL-E-10"):
            if "CLOSE_MUTATION_SET_RESULT" in row["inputs"]:
                sys.exit(f"registry_assemble: {key} already lists CLOSE_MUTATION_SET_RESULT")
            row["inputs"] = row["inputs"] + ["CLOSE_MUTATION_SET_RESULT"]
            report["hand_edits"].append(f"{key} inputs gain CLOSE_MUTATION_SET_RESULT (W5 RE-4 other_rows)")
        derived = D.derive(parts[key])
        outs = row["outputs"]
        if len(outs) == 1:
            outs[0]["states"], outs[0]["consumers"] = derived["states"], derived["consumers"]
        else:
            if (sorted({s for o in outs for s in o["states"]}) != derived["states"]
                    or sorted({c for o in outs for c in o["consumers"]}) != derived["consumers"]):
                sys.exit(f"registry_assemble: {key} has several outputs and its derivation moved; split it in PLAN")
        row["required_interfaces"] = derived["required_interfaces"]
        if "expected_parent_title" in row:
            row["expected_parent_title"] = retitle(row["expected_parent_title"])
        if key not in revisions:
            sys.exit(f"registry_assemble: no revision for {key}")
        row["source_snapshot"]["page_last_edited_at"] = revisions[key]
        if plan.get(key, {}).get("registry_row"):
            report["plan_assertions_added"] += _add(row["audit_assertions"], plan[key]["audit_assertions"])
        ordered = {k: row[k] for k in template if k in row}
        ordered.update({k: v for k, v in row.items() if k not in ordered})
        rows.append(ordered)
    header = {k: copy.deepcopy(v) for k, v in base.items() if k != "prompts"}
    for path, value in HEADER["set"]:
        _put(header, path, fill(value, values))
    d = header["workspace_skill_registry_disposition"]
    if d.count("all 55 rows below") != 1:
        sys.exit("registry_assemble: the disposition's member count moved")
    header["workspace_skill_registry_disposition"] = d.replace("all 55 rows below", f"all {ROWS} rows below")
    report["hand_edits"].append("header workspace_skill_registry_disposition: all 56 rows (W5 RE-4 member facts)")
    for lane in header["lanes"]:
        lane["notion_parent_title"] = retitle(lane["notion_parent_title"])
        if HEADER["control_titles"].get(lane["notion_parent_id"]) != lane["notion_parent_title"]:
            sys.exit(f"registry_assemble: lane {lane['lane']} parent id and title disagree with control_titles")
    data = {k: (rows if k == "prompts" else header[k]) for k in base}
    report["stand_in_used"] = bool(smap.get("stand_in")) or plan_stand_in
    return data, report


def render(data: dict, stage: str, extra: dict) -> str:
    import yaml
    values = stage_values(stage, extra)
    lines = [MARKER.sub(lambda m: "null" if values.get(m.group(0), m.group(0)) is None
                        else str(fill(m.group(0), values)), line) for line in HEADER["preamble"]]
    body = yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=100)
    return "\n".join(lines) + "\n```yaml\n" + body + "```\n"


def load_revisions(path: str) -> dict:
    rep = json.loads(Path(path).read_text(encoding="utf-8"))
    if "pages" in rep and isinstance(rep["pages"], list):  # a body_check.py check report (EXECUTE)
        return {p["prompt"]: p["as_of"] for p in rep["pages"] if "as_of" in p}
    return rep.get("revisions", rep)


def build(a) -> dict:
    extra = dict(item.split("=", 1) for item in a.set)
    A = audit(a.audit_root)
    data, report = assemble(a)
    left = markers_left(data)
    if left:
        sys.exit(f"registry_assemble: unfilled markers: {left}")
    text = render(data, a.stage, extra)
    if markers_left(text.split("```yaml", 1)[0]):
        sys.exit("registry_assemble: unfilled marker in the preamble")
    out = Path(a.out)
    out.write_text(text, encoding="utf-8")
    back = A.load_data(out)
    same = json.dumps(back, sort_keys=True, default=str) == json.dumps(data, sort_keys=True, default=str)
    if not same:
        out.unlink()
        sys.exit("registry_assemble: the written YAML does not read back as assembled; nothing kept")
    return {"mode": "build", "stage": a.stage, "written": str(out), "bytes": out.stat().st_size,
            "rows": len(data["prompts"]), "read_back_equal": same, **report, "ok": True}


def check(a) -> dict:
    A, D = audit(a.audit_root), deriver(a.graph_contract)
    data = A.load_data(a.registry)
    problems = A.validate_project_registry(data)
    errors = [p for p in problems if p["level"] == "error"]
    drift, rows_without_part = D.drift(data, D.load_parts(a.parts))
    values = stage_values(a.stage, {})
    expect = {}
    for path, value in HEADER["set"]:
        v = fill(value, values)
        if not markers_left(v):
            expect[".".join(map(str, path))] = v

    def get(path):
        obj = data
        for k in path.split("."):
            obj = obj[int(k)] if isinstance(obj, list) else obj[k]
        return obj
    header_ok = {p: get(p) == v for p, v in expect.items()}
    rows = data["prompts"]
    res = {"mode": "check", "stage": a.stage,
           "validator_errors": len(errors), "validator_error_codes": sorted({p.get("code", "") for p in errors}),
           "validator_warnings": len(problems) - len(errors),
           "deriver_drift": drift, "rows_without_part": rows_without_part,
           "rows": len(rows), "rows_active": sum(r.get("lifecycle") == "ACTIVE" for r in rows),
           "row_keys_unique": len({r["prompt_key"] for r in rows}) == len(rows),
           "cl05_before_cl20": (lambda ks: ADDED in ks and INSERT_BEFORE in ks and ks.index(ADDED) + 1 == ks.index(INSERT_BEFORE))(
               [r["prompt_key"] for r in rows]),
           "header_values_ok": all(header_ok.values()), "header_values_failing": [p for p, ok in header_ok.items() if not ok],
           "markers_left": markers_left(data),
           "release_literals_left": sorted({r["prompt_key"] for r in rows if r["prompt_key"] != "GCFPE-MGMT-10" and any(
               x in json.dumps({k: r[k] for k in ("expected_title", "controlling_sources", "expected_parent_title") if k in r},
                               ensure_ascii=False) for x in (OLD_REL, OLD_VER))}),
           "parent_titles_in_control_titles": all(r.get("expected_parent_title", next(iter(HEADER["control_titles"].values())))
                                                  in HEADER["control_titles"].values() for r in rows)}
    res["ok"] = (not errors and drift == [] and rows_without_part == [] and res["rows"] == ROWS and res["rows_active"] == ROWS
                 and res["row_keys_unique"] and res["cl05_before_cl20"] and res["header_values_ok"]
                 and not res["markers_left"] and not res["release_literals_left"] and res["parent_titles_in_control_titles"])
    return res


INJECT_FORBIDDEN = [("SRC-001", "Prompt version:", "\nPrompt version: 102726.1\n"),
                    ("CTR-001", "CONTROL_NOTION", "\nCONTROL_NOTION\n")]


def assertions(a) -> dict:
    A = audit(a.audit_root)
    data = A.load_data(a.registry)
    if not a.synthetic:
        return {"mode": "assertions", "ok": False,
                "error": "PLAN runs the synthetic form only; body-level assertions are A5's and EXECUTE's (precedent body mode)"}
    base_text = "Synthetic text for the registry injection proof; no prompt body is read.\n"
    rows_out, ok = [], True
    for row in data["prompts"]:
        key = row["prompt_key"]
        aa = row["audit_assertions"]
        n_req = len(aa.get("required_regex") or []) + len(aa.get("required_literals") or [])
        fired, missed = 0, []
        for kind in ("required_regex", "required_literals"):
            for raw in aa.get(kind) or []:
                if A._evaluate_assertions({"prompt_key": key, "audit_assertions": {kind: [raw]}}, base_text, "inject"):
                    fired += 1
                else:
                    missed.append(f"{kind}:{(raw.get('guard') if isinstance(raw, dict) else None) or str(raw)[:50]}")
        forb = 0
        for rule, needle, line in INJECT_FORBIDDEN:
            carried = [x for x in aa.get("forbidden_regex") or []
                       if x["rule_id"] == rule and re.search(x["value"], needle, flags=re.MULTILINE)]
            if not carried:
                missed.append("NOT_CARRIED:" + needle)
                continue
            clean = A._evaluate_assertions({"prompt_key": key, "audit_assertions": {"forbidden_regex": carried}}, base_text, "inject")
            hit = A._evaluate_assertions({"prompt_key": key, "audit_assertions": {"forbidden_regex": carried}},
                                         base_text + line, "inject")
            if hit and not clean:
                forb += 1
            else:
                missed.append(needle)
        r = {"prompt": key, "required": n_req, "required_reported": fired, "forbidden_injected_reported": forb,
             "assertions": sum(len(aa.get(k) or []) for k in ASSERTION_KEYS), "missed": missed,
             "ok": not missed and fired == n_req and forb == 2 and n_req > 0}
        ok &= r["ok"]
        rows_out.append(r)
    return {"mode": "assertions", "form": "SYNTHETIC_INJECT", "engine": "amthor-workspace-governance-audit _evaluate_assertions",
            "rows": len(rows_out), "rows_ok": sum(r["ok"] for r in rows_out),
            "failing_rows": [r for r in rows_out if not r["ok"]], "per_row": rows_out, "ok": ok and len(rows_out) == ROWS,
            "d22": "no prompt body is read or written; body-level assertions are A5's"}


def compare(a) -> dict:
    A = audit(a.audit_root)
    c, s = A.load_data(a.candidate), A.load_data(a.selected)
    allowed = {"status", "approved_by", "approved_at"}
    diffs = []

    def walk(x, y, path):
        if isinstance(x, dict) and isinstance(y, dict):
            for k in sorted(set(x) | set(y)):
                walk(x.get(k, "<absent>"), y.get(k, "<absent>"), path + [str(k)])
        elif isinstance(x, list) and isinstance(y, list) and len(x) == len(y):
            for i, (u, v) in enumerate(zip(x, y)):
                walk(u, v, path + [str(i)])
        elif json.dumps(x, default=str) != json.dumps(y, default=str):
            diffs.append(".".join(path))
    walk(c, s, [])
    ct = Path(a.candidate).read_text(encoding="utf-8").split("```yaml", 1)[0].splitlines()
    st = Path(a.selected).read_text(encoding="utf-8").split("```yaml", 1)[0].splitlines()
    pre = [i for i, (x, y) in enumerate(zip(ct, st)) if x != y]
    pre_ok = len(ct) == len(st) and all(ct[i].split(":")[0] in ("status", "approved_by", "approved_at") for i in pre)
    return {"mode": "compare", "differing_paths": diffs, "preamble_lines_differing": pre, "ok": set(diffs) <= allowed and pre_ok}


def selftest(a) -> dict:
    W = Path(a.scratch)
    if W.exists():
        shutil.rmtree(W)
    W.mkdir(parents=True)
    rows = {}
    A = audit(a.audit_root)

    def refused(mutate_ns=None, fn=build) -> bool:
        b = argparse.Namespace(**vars(a))
        b.out, b.stage = str(W / "x.md"), "candidate"
        if mutate_ns:
            mutate_ns(b)
        try:
            fn(b)
        except SystemExit:
            return True
        return False
    b = argparse.Namespace(**vars(a)); b.stage, b.out = "candidate", str(W / "clean.md")
    rows["clean_build_passes"] = build(b)["ok"]
    b2 = argparse.Namespace(**vars(a)); b2.registry, b2.stage = b.out, "candidate"
    rows["clean_check_passes"] = check(b2)["ok"]

    def bad_base(ns):
        p = W / "base-wrong.md"
        t = Path(a.base_registry).read_text(encoding="utf-8").replace("registry_id: GCFPE-PCR-20261009.1", "registry_id: GCFPE-PCR-20260914.1", 1)
        p.write_text(t, encoding="utf-8")
        ns.base_registry = str(p)
    rows["refuses_non_selected_base"] = refused(bad_base)

    def missing_rev(ns):
        r = json.loads(Path(a.revisions).read_text(encoding="utf-8"))
        r.get("revisions", r).pop("QA-80")
        p = W / "rev-missing.json"
        p.write_text(json.dumps(r), encoding="utf-8")
        ns.revisions = str(p)
    rows["refuses_missing_revision"] = refused(missing_rev)

    def unfilled(ns):
        ns.set = [s for s in ns.set if not s.startswith("@CATALOG_ID=")]
    rows["refuses_unfilled_marker"] = refused(unfilled)

    def map_missing_member(ns):
        m = json.loads(Path(a.map).read_text(encoding="utf-8"))
        m["members"].pop("QA-80")
        p = W / "map-missing.json"
        p.write_text(json.dumps(m), encoding="utf-8")
        ns.map = str(p)
    rows["refuses_map_missing_member"] = refused(map_missing_member)
    # check: an edited row (a derived consumer moved) is drift; a 55-row registry fails; a stale title fails
    text = Path(b.out).read_text(encoding="utf-8")
    data = A.load_data(Path(b.out))

    def check_on(mut) -> dict:
        d = copy.deepcopy(data)
        mut(d)
        import yaml
        p = W / "mut.md"
        p.write_text(text.split("```yaml", 1)[0] + "```yaml\n" + yaml.safe_dump(d, sort_keys=False, allow_unicode=True, width=100) + "```\n", encoding="utf-8")
        c = argparse.Namespace(**vars(a)); c.registry, c.stage = str(p), "candidate"
        return check(c)
    rows["check_reports_derivation_drift"] = bool(check_on(lambda d: d["prompts"][0]["outputs"][0]["consumers"].append("PR-50"))["deriver_drift"])
    r55 = check_on(lambda d: d["prompts"].pop(next(i for i, r in enumerate(d["prompts"]) if r["prompt_key"] == "CL-05")))
    rows["check_fails_55_rows"] = r55["ok"] is False and r55["rows"] == 55
    rows["check_fails_inactive_row"] = check_on(lambda d: d["prompts"][3].__setitem__("lifecycle", "RETIRED"))["ok"] is False
    rows["check_fails_stale_title"] = bool(check_on(lambda d: next(r for r in d["prompts"] if r["prompt_key"] == "QA-80").__setitem__(
        "expected_title", "QA-80 — Revise Whole-Change QA Plan — 100926.1"))["release_literals_left"])
    rows["check_fails_header_value"] = check_on(lambda d: d["observation"].__setitem__("selected_member_count", 55))["ok"] is False
    # assertions: a row with no required assertion, and a row missing a release-wide forbidden one, are reported
    def assert_on(mut) -> dict:
        d = copy.deepcopy(data)
        mut(d)
        import yaml
        p = W / "mut-a.md"
        p.write_text(text.split("```yaml", 1)[0] + "```yaml\n" + yaml.safe_dump(d, sort_keys=False, allow_unicode=True, width=100) + "```\n", encoding="utf-8")
        c = argparse.Namespace(**vars(a)); c.registry, c.synthetic = str(p), True
        return assertions(c)
    c = argparse.Namespace(**vars(a)); c.registry, c.synthetic = b.out, True
    rows["clean_assertions_pass"] = assertions(c)["ok"]
    rows["assertions_report_dropped_forbidden"] = assert_on(lambda d: d["prompts"][0]["audit_assertions"].__setitem__(
        "forbidden_regex", [x for x in d["prompts"][0]["audit_assertions"]["forbidden_regex"] if x["rule_id"] != "SRC-001"]))["ok"] is False
    rows["assertions_report_vacuous_required"] = assert_on(lambda d: d["prompts"][1]["audit_assertions"]["required_regex"].append(
        {"rule_id": "CTR-002", "value": "(?s).*"}))["ok"] is False
    shutil.rmtree(W, ignore_errors=True)
    return {"mode": "selftest", "rows": rows, "selftest_ok": all(rows.values())}


def main() -> int:
    ap = argparse.ArgumentParser(prog="registry_assemble_102726.py")
    sub = ap.add_subparsers(dest="mode", required=True)

    def inputs(p):
        for k in ("--base-registry", "--audit-root", "--graph-contract", "--parts", "--map", "--revisions"):
            p.add_argument(k, required=True)
        p.add_argument("--stand-in-ok", action="store_true")
        p.add_argument("--set", action="append", default=[], help="@MARKER=VALUE")
    b = sub.add_parser("build")
    b.add_argument("--stage", choices=["candidate", "selected"], required=True)
    b.add_argument("--out", required=True)
    inputs(b)
    c = sub.add_parser("check")
    c.add_argument("--stage", choices=["candidate", "selected"], required=True)
    for k in ("--registry", "--audit-root", "--graph-contract", "--parts"):
        c.add_argument(k, required=True)
    s = sub.add_parser("assertions")
    s.add_argument("--registry", required=True)
    s.add_argument("--audit-root", required=True)
    s.add_argument("--synthetic", action="store_true")
    s.add_argument("--inject", action="store_true")
    m = sub.add_parser("compare")
    m.add_argument("candidate"); m.add_argument("selected")
    m.add_argument("--audit-root", required=True)
    t = sub.add_parser("selftest")
    t.add_argument("--scratch", required=True)
    t.add_argument("--graph-contract-check", default=None)
    inputs(t)
    a = ap.parse_args()
    if a.mode == "build":
        res = build(a)
    elif a.mode == "selftest":
        res = selftest(a)
        res["ok"] = res["selftest_ok"]
    else:
        res = {"check": check, "assertions": assertions, "compare": compare}[a.mode](a)
    print(json.dumps(res, indent=1, ensure_ascii=False, default=str))
    return 0 if res["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
