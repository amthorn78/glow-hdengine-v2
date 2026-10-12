#!/usr/bin/env python3
"""The 100926.1 Project Prompt Contract Registry, assembled for MODIFICATION-20261011-gcfpe-mb008-to-promotion
(PLAN, PART-05 and PART-07; R-A2 and L-23 of PLAN review round 1).

  registry_assemble.py build --stage candidate|selected --audit-root A --graph-contract G --parts P
                             --revisions R --out FILE [--set KEY=VALUE ...]
        Writes one registry Markdown file. Rows, in the selected registry's order:
          1. the 2026-10-09 non-derived proposal's row (20261009-gcfpe-latest-alpha-analysis), except
             GCFPE-MGMT-10, whose row is mgmt10-registry-row.json with its markers filled;
          2. outputs[].states, outputs[].consumers and required_interfaces from the shipped registry_deriver's
             derive() on the final parts. A row with several outputs keeps the selected registry's split, and the
             build refuses when that split's union is not the derived value;
          3. expected_parent_title retitled by registry-header's title_suffix, refused outside control_titles;
          4. source_snapshot.page_last_edited_at from R: X6's `body_check.py check` report (each page's as_of);
          5. the parent Modification's guards (its committed candidate-registry-guards.json) and this plan's
             guards (body_check.py registry_assertions) appended to audit_assertions, an identical assertion once.
        The header is the selected 091426.1 registry's, with registry-header-100926.1.json's set and delete
        applied and the stage's values filled. The YAML is written by yaml.safe_dump and read back by the
        audit's own load_data; the build refuses unless the read-back equals what was assembled, and refuses any
        unfilled `@` marker.
  registry_assemble.py check --stage S --registry FILE --audit-root A --graph-contract G --parts P
        validate_project_registry: no error; registry_deriver drift(): none; 55 ACTIVE rows; every header value
        as registry-header states for the stage; no `@` marker left.
  registry_assemble.py assertions --registry FILE --audit-root A [--fetched-after T] [--page K=ID@TS]
                                  [--shared K=V] [--inject]
        every row's audit_assertions run by the shipped engine (_evaluate_assertions) on the newest fresh read of
        its page with this plan's operations applied in memory (D22: body_check.py's transient reads; counts and
        ids only). --inject also proves each row's assertions fire: each required assertion, with every line it
        matches removed, and two release-wide forbidden assertions (D23-G's `Prompt version:` line and
        CONTROL_NOTION), with a violating line added, must each be reported.
  registry_assemble.py compare CANDIDATE SELECTED --audit-root A
        the two stages differ only at the paths registry-header names for the stage values.

Writes only --out. Run with PYTHONDONTWRITEBYTECODE=1.
"""
from __future__ import annotations

import argparse
import copy
import importlib.util
import json
import os
import re
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
EVIDENCE = HERE.parent.parent
SELECTED_REGISTRY = HERE.parents[5] / "docs" / "prompt_ecosystem_management" / "project-prompt-contract-registry.md"
PROPOSAL = EVIDENCE / "20261009-gcfpe-latest-alpha-analysis" / "execute" / "candidate-registry-nonderived.json"
PARENT_GUARDS = EVIDENCE / "20261010-gcfpe-candidate-skill-analysis" / "execute" / "candidate-registry-guards.json"
HEADER = json.loads((HERE / "registry-header-100926.1.json").read_text(encoding="utf-8"))
MGMT_ROW = json.loads((HERE / "mgmt10-registry-row.json").read_text(encoding="utf-8"))
MGMT = "GCFPE-MGMT-10"
MARKER = re.compile(r"@[A-Z][A-Z0-9_]+")
ASSERTION_KEYS = ("required_literals", "forbidden_literals", "required_regex", "forbidden_regex")


def _module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(path.parent))
    spec.loader.exec_module(mod)
    return mod


def audit(root: str):
    return _module(Path(root) / "scripts" / "audit_workspace_governance.py", "audit_workspace_governance")


def deriver(root: str):
    return _module(Path(root) / "scripts" / "registry_deriver.py", "registry_deriver")


def body_check():
    return _module(HERE / "body_check.py", "body_check")


def fill(value, values: dict):
    """Every marker in a string replaced from values; a string that is exactly one marker takes its value's type."""
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


def _add(assertions: dict, extra: dict) -> None:
    for key in ("required_regex", "forbidden_regex"):
        have = {(a["rule_id"], a["value"]) for a in assertions.get(key) or []}
        for a in extra.get(key, []):
            if (a["rule_id"], a["value"]) not in have:
                assertions.setdefault(key, []).append(a)
                have.add((a["rule_id"], a["value"]))


def assemble(stage: str, audit_root: str, gc_root: str, parts_dir: str, revisions: dict, extra: dict) -> dict:
    A, D = audit(audit_root), deriver(gc_root)
    selected = A.load_data(SELECTED_REGISTRY)
    proposal = json.loads(PROPOSAL.read_text(encoding="utf-8"))["prompts"]
    parent = json.loads(PARENT_GUARDS.read_text(encoding="utf-8"))["assertions"]
    plan = body_check().registry_assertions()
    parts = D.load_parts(parts_dir)
    sel_rows = {r["prompt_key"]: r for r in selected["prompts"]}
    order = [r["prompt_key"] for r in selected["prompts"]]
    if order != [r["prompt_key"] for r in proposal]:
        sys.exit("registry_assemble: the proposal's rows are not the selected registry's rows in its order")
    values = stage_values(stage, extra)
    rows = []
    for base in proposal:
        key = base["prompt_key"]
        row = copy.deepcopy(MGMT_ROW["row"]) if key == MGMT else copy.deepcopy(base)
        if key == MGMT:
            row = fill(row, values)
        derived = D.derive(parts[key])
        outs = row["outputs"]
        if len(outs) == 1:
            outs[0]["states"], outs[0]["consumers"] = derived["states"], derived["consumers"]
        else:
            split = sel_rows[key]["outputs"]
            if [o["artifact"] for o in split] != [o["artifact"] for o in outs]:
                sys.exit(f"registry_assemble: {key} outputs differ from the selected registry's")
            if (sorted({s for o in split for s in o["states"]}) != derived["states"]
                    or sorted({c for o in split for c in o["consumers"]}) != derived["consumers"]):
                sys.exit(f"registry_assemble: {key} has several outputs and its derivation moved; split it in PLAN")
            for o, s in zip(outs, split):
                o["states"], o["consumers"] = list(s["states"]), list(s["consumers"])
        row["required_interfaces"] = derived["required_interfaces"]
        if "expected_parent_title" in row:
            row["expected_parent_title"] = retitle(row["expected_parent_title"])
        if key not in revisions:
            sys.exit(f"registry_assemble: no revision for {key}")
        row["source_snapshot"]["page_last_edited_at"] = revisions[key]
        if key in parent and parent[key]["registry_row"]:
            _add(row["audit_assertions"], parent[key]["audit_assertions"])
        if plan.get(key, {}).get("registry_row"):
            _add(row["audit_assertions"], plan[key]["audit_assertions"])
        # the order the 091426.1 registry writes a row in, then any key it lacks
        ordered = {k: row[k] for k in sel_rows[key] if k in row}
        ordered.update({k: v for k, v in row.items() if k not in ordered})
        rows.append(ordered)
    if any("xtract" in line for r in rows for line in r.get("evidence_contract", [])):
        sys.exit("registry_assemble: a row mentions an extraction; body_extraction_convention cannot be deleted")
    header = {k: copy.deepcopy(v) for k, v in selected.items() if k != "prompts"}
    for path, value in HEADER["set"]:
        _put(header, path, fill(value, values))
    for path, _reason in HEADER["delete"]:
        target = header
        for k in path[:-1]:
            target = target[k]
        del target[path[-1]]
    for lane in header["lanes"]:
        lane["notion_parent_title"] = retitle(lane["notion_parent_title"])
        if HEADER["control_titles"].get(lane["notion_parent_id"]) != lane["notion_parent_title"]:
            sys.exit(f"registry_assemble: lane {lane['lane']} parent id and title disagree with control_titles")
    data = {}
    for k in selected:
        if k == "prompts":
            data[k] = rows
        elif k in header:
            data[k] = header[k]
    return data


def render(data: dict, stage: str, extra: dict, A) -> str:
    import yaml
    values = stage_values(stage, extra)
    lines = []
    for line in HEADER["preamble"]:
        lines.append(MARKER.sub(lambda m: "null" if values.get(m.group(0), m.group(0)) is None
                                else str(fill(m.group(0), values)), line))
    body = yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=100)
    return "\n".join(lines) + "\n```yaml\n" + body + "```\n"


def load_revisions(path: str) -> dict:
    rep = json.loads(Path(path).read_text(encoding="utf-8"))
    if "pages" in rep:  # a body_check.py check report
        return {p["prompt"]: p["as_of"] for p in rep["pages"] if "as_of" in p}
    return rep


def build(a) -> int:
    extra = dict(item.split("=", 1) for item in a.set)
    A = audit(a.audit_root)
    data = assemble(a.stage, a.audit_root, a.graph_contract, a.parts, load_revisions(a.revisions), extra)
    left = markers_left(data)
    if left:
        sys.exit(f"registry_assemble: unfilled markers: {left}")
    text = render(data, a.stage, extra, A)
    if markers_left(text.split("```yaml", 1)[0]):
        sys.exit("registry_assemble: unfilled marker in the preamble")
    out = Path(a.out)
    out.write_text(text, encoding="utf-8")
    back = A.load_data(out)
    same = json.dumps(back, sort_keys=True, default=str) == json.dumps(data, sort_keys=True, default=str)
    if not same:
        out.unlink()
        sys.exit("registry_assemble: the written YAML does not read back as assembled; nothing kept")
    print(json.dumps({"written": str(out), "bytes": out.stat().st_size, "rows": len(data["prompts"]),
                      "read_back_equal": same}))
    return 0


def check(a) -> dict:
    A, D = audit(a.audit_root), deriver(a.graph_contract)
    data = A.load_data(a.registry)
    problems = A.validate_project_registry(data)
    errors = [p for p in problems if p["level"] == "error"]
    drift, rows_without_part = D.drift(data, D.load_parts(a.parts))
    expect = {}
    values = stage_values(a.stage, {})
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
    res = {
        "mode": "check", "stage": a.stage,
        "validator_errors": len(errors), "validator_warnings": len(problems) - len(errors),
        "deriver_drift": drift, "rows_without_part": rows_without_part,
        "rows": len(rows), "rows_active": sum(r.get("lifecycle") == "ACTIVE" for r in rows),
        "header_values_ok": all(header_ok.values()), "header_values_failing": [p for p, ok in header_ok.items() if not ok],
        "deleted_absent": all(path[0] not in data for path, _ in HEADER["delete"]),
        "markers_left": markers_left(data),
        "parent_titles_in_control_titles": all(r.get("expected_parent_title", next(iter(HEADER["control_titles"].values())))
                                               in HEADER["control_titles"].values() for r in rows),
    }
    res["ok"] = (not errors and drift == [] and rows_without_part == [] and res["rows"] == 55 and res["rows_active"] == 55
                 and res["header_values_ok"] and res["deleted_absent"] and not res["markers_left"]
                 and res["parent_titles_in_control_titles"])
    return res


def _without_matches(text: str, value: str) -> str:
    """The text with every line the pattern matches in removed, so a required assertion has nothing left."""
    for _ in range(200):
        m = re.search(value, text, flags=re.MULTILINE)
        if not m:
            return text
        s = text.rfind("\n", 0, m.start()) + 1
        e = text.find("\n", max(m.end() - 1, m.start()))
        e = len(text) if e < 0 else e + 1
        if e <= s:
            e = s + 1
        text = text[:s] + text[e:]
    return text


INJECT_FORBIDDEN = [("SRC-001", "Prompt version:", "\nPrompt version: 100926.1\n"),
                    ("CTR-001", "CONTROL_NOTION", "\nCONTROL_NOTION\n")]


def assertions(a) -> dict:
    A = audit(a.audit_root)
    B = body_check()
    for item in a.page:
        key, rest = item.split("=", 1)
        pid, ts = rest.split("@", 1)
        B.EDITS["pages"][key] = {"page_id": pid, "expected_last_edited": ts}
    for item in a.shared:
        key, val = item.split("=", 1)
        B.SHARED[key] = val
    data = A.load_data(a.registry)
    root, session = os.path.expanduser("~/.claude/projects"), os.environ.get("CLAUDE_CODE_SESSION_ID")
    rows_out, ok = [], True
    for row in data["prompts"]:
        key = row["prompt_key"]
        meta = B.EDITS["pages"].get(key)
        got = B.latest_fetch(meta["page_id"], root, session, a.since_minutes, a.fetched_after) if meta else None
        if got is None:
            rows_out.append({"prompt": key, "error": "NO_FETCH_FOUND"})
            ok = False
            continue
        after, _ = B.apply_all(got[2], [o for o in B.EDITS["ops"] if o["prompt"] == key])
        findings = A._evaluate_assertions(row, after, "transient")
        r = {"prompt": key, "as_of": got[1],
             "assertions": sum(len(row["audit_assertions"].get(k) or []) for k in ASSERTION_KEYS),
             "findings_after": len(findings),
             "failing": sorted({f["observed"][:90] for f in findings})}
        if a.inject:
            fired, missed = 0, []
            for raw in row["audit_assertions"].get("required_regex") or []:
                broken = _without_matches(after, raw["value"])
                if A._evaluate_assertions({"prompt_key": key, "audit_assertions": {"required_regex": [raw]}},
                                          broken, "inject"):
                    fired += 1
                else:
                    missed.append(raw.get("guard") or raw["value"][:60])
            for rule, needle, line in INJECT_FORBIDDEN:
                carried = [x for x in row["audit_assertions"].get("forbidden_regex") or []
                           if x["rule_id"] == rule and re.search(x["value"], needle, flags=re.MULTILINE)]
                if not carried:
                    missed.append("NOT_CARRIED:" + needle)
                    continue
                if A._evaluate_assertions({"prompt_key": key, "audit_assertions": {"forbidden_regex": carried}},
                                          after + line, "inject"):
                    fired += 1
                else:
                    missed.append(needle)
            r["injected_fired"], r["injected_missed"] = fired, missed
        r["ok"] = not findings and not r.get("injected_missed")
        ok &= r["ok"]
        rows_out.append(r)
    return {"mode": "assertions", "engine": "amthor-workspace-governance-audit _evaluate_assertions",
            "rows": rows_out, "ok": ok,
            "d22": "transient reads of this session's harness records; no body text in this report"}


def compare(a) -> dict:
    A = audit(a.audit_root)
    c, s = A.load_data(a.candidate), A.load_data(a.selected)
    allowed = {"status", "approved_by", "approved_at", "authority_sources.1.url", "authority_sources.1.pending"}
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
    res = {"mode": "compare", "differing_paths": diffs, "preamble_lines_differing": pre,
           "ok": set(diffs) <= allowed and pre_ok}
    return res


def main() -> int:
    ap = argparse.ArgumentParser(prog="registry_assemble.py")
    sub = ap.add_subparsers(dest="mode", required=True)
    b = sub.add_parser("build")
    b.add_argument("--stage", choices=["candidate", "selected"], required=True)
    for k in ("--audit-root", "--graph-contract", "--parts", "--revisions", "--out"):
        b.add_argument(k, required=True)
    b.add_argument("--set", action="append", default=[], help="@MARKER=VALUE")
    c = sub.add_parser("check")
    c.add_argument("--stage", choices=["candidate", "selected"], required=True)
    for k in ("--registry", "--audit-root", "--graph-contract", "--parts"):
        c.add_argument(k, required=True)
    s = sub.add_parser("assertions")
    s.add_argument("--registry", required=True)
    s.add_argument("--audit-root", required=True)
    s.add_argument("--fetched-after", default="")
    s.add_argument("--since-minutes", type=int, default=600)
    s.add_argument("--page", action="append", default=[])
    s.add_argument("--shared", action="append", default=[])
    s.add_argument("--inject", action="store_true")
    m = sub.add_parser("compare")
    m.add_argument("candidate")
    m.add_argument("selected")
    m.add_argument("--audit-root", required=True)
    a = ap.parse_args()
    if a.mode == "build":
        return build(a)
    res = {"check": check, "assertions": assertions, "compare": compare}[a.mode](a)
    print(json.dumps(res, indent=1, ensure_ascii=False))
    return 0 if res["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
