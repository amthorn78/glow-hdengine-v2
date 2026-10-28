#!/usr/bin/env python3
"""Package build for GCFPE-20261027.1 / 102726.1 (MODIFICATION-20261027-gcfpe-backlog-open-items, PART-24).

Adapted in PLAN (A3) from docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/execute/package_build.py,
per W7 tooling.precedent_scripts "execute/package_build.py". EXECUTE copies it to execute/package_build_102726.py and
runs it on the real successor map, the real PLAN-20261027.md and its own Q2/Q4/Q5 outputs; PLAN runs it on stand-ins.

  package_build_102726.py build <installed-copies-dir> <out-dir> --production-contract C --production-graph-md MD
      --r1-dir D --plan P --map M [--members-tsv T] [--stand-in-ok] [--with-conditional R-P1]
  package_build_102726.py check <same arguments>     rebuild into a temporary directory; exit 1 unless <out-dir> is
                                                     byte-identical
  package_build_102726.py selftest <installed-copies-dir> <scratch> <same input flags>
                                                     each injected defect must stop the build

<installed-copies-dir> holds verified scratch copies of the installed skills (never the synced install directory).
The four packages (W7-D2) are written to <out-dir>, which must not exist. In order:

  A   copy change-flow, flowmaster-validate, glow-hde-pr-development, glow-graph-contract; apply plan/package_apply.py
      (plan/package-redlines.json: every worker op, W7's, then A3-C1..C4); require every op LANDED; with --with-conditional R-P1 only,
      then apply the R-P1 conditional set (C-13: Nathan's opt-in; excluded by default)
  N   the R1 successor files (W5 SR-CF-8, SR-FV-35, SR-FV-36) from build_r1_successor_20261027.py --out-dir D: oracle
      and source matrix into flowmaster-validate, runtime map into change-flow; each digest must equal the pin the
      redlined validate_flowmaster.py carries (read from that file, never typed)
  B   bundle the 102726.1 production contract and the production graph's embedded JSON into change-flow and
      flowmaster-validate as gcfpe-20261027.1-102726.1-{direct-handoff,candidate-graph}-contract.json
  F   fixtures/gcfpe-20261027.1-102726.1/scenarios.json: the 100926.1 scenarios with their release fields moved; the
      release's new checks are contract and body mutation cases in the runner (R), not scenario rows
  P+M plan/make_profile_20261027.py build: flowmaster-validate's validate_gcfpe_20261027.py and the 102726.1 profile,
      measured from the bundled files, the PLAN file and the successor map
  R   run_gcfpe_20261027_fixtures.py from the 100926.1 runner: release literals moved, revision 3.5.0, the QA closure
      contract cases retargeted to the close-mutation-set stage, and the new mutation cases (W5 QA closure, W1 DOC-20
      inbound, member version off the map, kept member at 102726.1, 55-member contract, merge-pending real-input P1,
      old R1 pin, 2026-09-23 oracle not historical, PROMPT_BINDING_SUPERSEDED on synthetic text); and, by AM-8, the
      QA-120 source cases' anchors moved to the written body (the RCA intake sentence; the CRD class cell in either
      table rendering)
  C   change-flow's validate_gcfpe_20261027.py from its 100926.1 sibling: every release pin measured
  I   flowmaster-validate's SKILL_TREE_SHA256 recomputed, last

Every edit is a named substitution whose old text must occur exactly the stated number of times. Byte pins are
measured from the files. Prints one JSON report. Run with PYTHONDONTWRITEBYTECODE=1.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent          # plan/ (EXECUTE: execute/, with PLAN_DIR pointing at plan/)
PLAN_DIR = HERE if (HERE / "package-redlines.json").is_file() else HERE.parent / "plan"
PACKAGES = ("change-flow", "flowmaster-validate", "glow-hde-pr-development", "glow-graph-contract")
NEW = "gcfpe-20261027.1-102726.1"
OLD = "gcfpe-20261009.1-100926.1"
PLAN_PATH_IN_REPO = "docs/ephemeral/modifications/evidence/20261027-gcfpe-backlog-open-items/PLAN-20261027.md"
R1_FILES = {  # build_r1_successor_20261027.py --out-dir names -> package destination
    "oracle-glow-hde-canonical-change-flow-r1-20261027.json": ("flowmaster-validate", "references/glow-hde-canonical-change-flow-r1-20261027.json"),
    "matrix-r1-successor-source-20261027.md": ("flowmaster-validate", "references/r1-successor-source-20261027.md"),
    "map-glow-hde-canonical-change-flow-r1-runtime-map-20261027.json": ("change-flow", "references/glow-hde-canonical-change-flow-r1-runtime-map-20261027.json"),
}
ENV = {"PYTHONDONTWRITEBYTECODE": "1", "PATH": os.environ.get("PATH", "/usr/bin:/bin")}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def substitute(path: Path, subs: list, report: list) -> None:
    text = path.read_text(encoding="utf-8")
    for name, old, new, want in subs:
        got = text.count(old)
        if want is None:
            want = got if got else -1
        if got != want:
            raise SystemExit(f"{name} ({path.name}): expected {want} occurrence(s), found {got}")
        text = text.replace(old, new)
        report.append({"substitution": name, "file": path.name, "count": got})
    path.write_text(text, encoding="utf-8")


def load(path: Path, name: str):
    sys.path.insert(0, str(path.parent))
    try:
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    finally:
        sys.path.pop(0)
    return mod


def graph_block(md: Path) -> str:
    lines = md.read_text(encoding="utf-8").split("\n")
    s = next(i for i, l in enumerate(lines) if l == "```json")
    e = max(i for i, l in enumerate(lines) if l == "```")
    return "\n".join(lines[s + 1:e]) + "\n"


def pin_from(path: Path, name: str) -> str:
    """A 64-hex pin assigned to `name` in a validator, as written (the pin is read, never typed here)."""
    m = re.search(name + r'\s*=\s*\(?\s*"([0-9a-f]{64})"', path.read_text(encoding="utf-8"))
    if not m:
        raise SystemExit(f"pin {name} not found in {path.name}")
    return m.group(1)


# ------------------------------------------------------------------------------------------- F: fixtures
def write_fixtures(fv: Path) -> Path:
    raw = (fv / f"fixtures/{OLD}/scenarios.json").read_text(encoding="utf-8")
    base = json.loads(raw)
    text = raw
    for old, new in (
        ('  "suite_id": "GCFPE-20261009.1-100926.1-SECTION-13",\n', '  "suite_id": "GCFPE-20261027.1-102726.1-SECTION-13",\n'),
        ('  "release": "GCFPE-20261009.1",\n', '  "release": "GCFPE-20261027.1",\n'),
        ('  "prompt_version": "100926.1",\n', '  "prompt_version": "102726.1",\n'),
    ):
        if text.count(old) != 1:
            raise SystemExit(f"fixtures: anchor {old.strip()[:50]!r} occurs {text.count(old)} times")
        text = text.replace(old, new)
    want = dict(base, suite_id="GCFPE-20261027.1-102726.1-SECTION-13", release="GCFPE-20261027.1", prompt_version="102726.1")
    if json.loads(text) != want:
        raise SystemExit("fixtures: the edited file does not read back as intended")
    out = fv / f"fixtures/{NEW}/scenarios.json"
    out.parent.mkdir(parents=True)
    out.write_text(text, encoding="utf-8")
    return out


# ------------------------------------------------------------------------------------------ R: the runner
NEW_MUTATION_CASES = '''    # GCFPE-20261027.1 / 102726.1 (MODIFICATION-20261027-gcfpe-backlog-open-items, PART-13, PART-08, PART-24):
    # each new contract check fires on its injected regression, and the clean contract carries none of its codes.
    clean_codes = validate_contract(source)

    def fires(name: str, mutate, code_prefix: str) -> None:
        changed = copy.deepcopy(source)
        mutate(changed)
        observed = validate_contract(changed)
        cases.append({"name": name, "expected_error_prefix": code_prefix, "errors": observed,
                      "passed": any(e.startswith(code_prefix) for e in observed)
                      and not any(e.startswith(code_prefix) for e in clean_codes)})

    def qa120_class_to(c, cls, to):
        for e in c["route_edges"]:
            if e["from"] == "QA-120" and any(b.get("change_class") == cls for b in e["route_branches"]):
                e["to"] = to
        for r in c["state_routes"]["QA-120"]:
            if r.get("change_class") == cls:
                r["destinations"] = [to]

    def cl05_crd_to_epic(c):
        for r in c["state_routes"]["CL-05"]:
            if r.get("change_class") == "CRD":
                r["destinations"] = ["CL-E-10"]

    def close_set_to_esc30(c):
        for e in c["route_edges"]:
            if e["from"] == "CL-C-10" and e["to"] == "CL-05":
                e["to"] = "ESC-30"

    def doc20_inbound_pr40(c):
        e = copy.deepcopy(next(x for x in c["route_edges"] if x["from"] == "DOC-20" and x["to"] == "QA-10"))
        e["to"] = "PR-40"
        c["route_edges"].append(e)

    changed_member = next(pid for pid in sorted(SUPERSEDED_MEMBER_PAGES) if pid in source["member_registry"])
    kept_members = sorted(pid for pid, v in EXPECTED_MEMBER_VERSIONS.items() if v != source.get("prompt_version"))
    fires("reject-qa-pass-straight-to-closure", lambda c: qa120_class_to(c, "CRD", "CL-C-10"), "QA_PASS_CLASS")
    fires("reject-cl05-exit-wrong-class", cl05_crd_to_epic, "CL05_CLOSE_EXIT_ROUTES")
    fires("reject-do-not-close-close-set-to-esc30", close_set_to_esc30, "DO_NOT_CLOSE_CLOSE_SET_ROUTE:CL-C-10")
    fires("reject-close-set-as-post-closure", lambda c: c["artifact_availability_contract"]["stage_categories"].__setitem__("CL-05", "POST_CLOSURE"), "CLOSE_STAGE_CATEGORY")
    fires("reject-doc20-inbound-pr40", doc20_inbound_pr40, "PR40_MANUAL_MERGE_BOUNDARY")
    fires("reject-member-version-off-map", lambda c: c["member_registry"][changed_member].__setitem__("version", "100926.1"), f"MEMBER_BINDING:{changed_member}")
    for kept in kept_members:
        fires(f"reject-kept-member-at-102726-{kept.lower()}", lambda c, k=kept: c["member_registry"][k].__setitem__("version", "102726.1"), f"MEMBER_BINDING:{kept}")
    fires("reject-55-member-contract", lambda c: c["candidate_prompt_ids"].remove("CL-05"), "MEMBER_SET")
    fires("reject-merge-pending-without-real-input-p1", lambda c: c["pr_development_contract"]["merge_pending_requirements"].remove("no open P1 thread on a real input"), "MERGE_PENDING_REQUIREMENTS")
    fires("reject-old-r1-oracle-pin", lambda c: c["protected_identities"].__setitem__("r1_oracle_sha256", "ede635b14aa2f57c8c99e948a012e88d843338f62bc2b55349d511f52f59fb52"), "PROTECTED_IDENTITIES")
    fires("reject-20260923-oracle-not-historical", lambda c: c["historical_non_executable_references"].remove("glow-hde-canonical-change-flow-r1-20260923.json"), "HISTORICAL_NON_EXECUTABLE_REFERENCES")
    # G-W7-BIND-1 on synthetic text (no prompt body is stored): a body naming a superseded page of a changed member.
    superseded = SUPERSEDED_MEMBER_PAGES[changed_member]
    head = f"{source['member_registry']['PR-10']['title']}\\nPrompt ID: PR-10\\n"
    dashed = "-".join([superseded[:8], superseded[8:12], superseded[12:16], superseded[16:20], superseded[20:]])
    for name, text, expect in (
        ("reject-binding-superseded-mention", head + f'see <mention url="https://app.notion.com/p/{superseded}" />\\n', True),
        ("reject-binding-superseded-dashed", head + f"see https://app.notion.com/p/{dashed}\\n", True),
        ("accept-binding-other-page", head + "see https://app.notion.com/p/000000000000000000000000000000ab?pvs=204\\n", False),
    ):
        errs = validate_prompt_bodies({"PR-10": text}, source)[0]
        hit = f"PROMPT_BINDING_SUPERSEDED:PR-10:{changed_member}" in errs
        cases.append({"name": name, "passed": hit == expect, "expected_binding_superseded": expect})

'''


def runner_subs(base_text: str) -> list:
    return [
        ("R01 docstring", base_text[base_text.index('"""'):base_text.index('"""', base_text.index('"""') + 3) + 3],
         '"""Run the deterministic GCFPE-20261027.1 / 102726.1 fixtures and contract mutations.\n\n'
         'Derived from the 100926.1 runner by MODIFICATION-20261027-gcfpe-backlog-open-items (PLAN PART-24): the 54\n'
         'section-13 cases with their release fields moved; the QA closure cases retargeted to the close-mutation-set\n'
         'stage CL-05 (PART-13); and mutation cases for every new contract check and PROMPT_BINDING_SUPERSEDED. AM-8\n'
         'moved the QA-120 source-case anchors to the body PART-07 and PART-13 wrote, in either table rendering.\n"""', 1),
        ("R02 validator import", "from validate_gcfpe_20261009 import (\n",
         "from validate_gcfpe_20261027 import (\n    EXPECTED_MEMBER_VERSIONS,\n    SUPERSEDED_MEMBER_PAGES,\n"
         "    validate_prompt_bodies,\n", 1),
        ("R03 selected member count", '        "selected_member_count": 55,\n', '        "selected_member_count": 56,\n', 1),
        ("R04 QA closure map case retargeted",
         '("reject-qa-closure-map-both-to-crd", lambda c: c["qa_closure_contract"]["pass_receivers"].__setitem__("EPIC", "CL-C-10"), ["QA_CLOSURE_CONTRACT"]),',
         '("reject-qa-closure-map-both-to-crd", lambda c: c["qa_closure_contract"]["close_stage_exit_receivers"].__setitem__("EPIC", "CL-C-10"), ["QA_CLOSURE_CONTRACT"]),', 1),
        ("R05 coherent class regression moves to CL-05's exit",
         '    epic = next(r for r in changed["state_routes"]["QA-120"] if r.get("change_class") == "EPIC")\n'
         '    epic["destinations"] = ["CL-C-10"]\n'
         '    edge = next(e for e in changed["route_edges"] if e.get("from") == "QA-120" and e.get("to") == "CL-E-10")\n',
         '    epic = next(r for r in changed["state_routes"]["CL-05"] if r.get("change_class") == "EPIC")\n'
         '    epic["destinations"] = ["CL-C-10"]\n'
         '    edge = next(e for e in changed["route_edges"] if e.get("from") == "CL-05" and e.get("to") == "CL-E-10")\n', 1),
        ("R07 report revision", '        "validator_revision": "3.4.1",', '        "validator_revision": "3.5.0",', 1),
        # AM-8 (Nathan's decision after X14): the QA-120 source cases anchor on the body PART-07 and PART-13 wrote,
        # and on the class map in whichever table rendering the read carries
        ("R08 AM-8 class-cell rendering",
         '        cases.append({"name": "accept-live-source-class-specific-closure-intakes",\n'
         '                      "passed": observed == [], "errors": observed})\n',
         '        cases.append({"name": "accept-live-source-class-specific-closure-intakes",\n'
         '                      "passed": observed == [], "errors": observed})\n'
         "        # AM-8 (MODIFICATION-20261027): the class map's fetch rendering has moved both ways (pipe to HTML in\n"
         "        # the 100926.1 precedent, HTML to pipe by 2026-10-27), so the CRD class cell is taken in the rendering\n"
         "        # this read carries, as qa_pass_class_rows reads either.\n"
         '        if "<td>`CRD`</td>" in bodies["QA-120"]:\n'
         '            crd_cell = ("<td>`CRD`</td>", "")\n'
         "        else:\n"
         '            crd_cell = ("| `PASS` | `CRD` |", "| `PASS` |  |")\n', 1),
        ("R09 AM-8 RCA anchor",
         '            ("reject-source-missing-rca", "QA-120", "`QA_RCA_ID`", "`OMITTED_RCA`", "QA_PASS_BODY_INTAKE"),\n',
         "            # AM-8: QA-120's PASS handoff names the separate `QA_REPORT` and `QA_RCA` with their IDs (PART-07's\n"
         "            # HP-QA-120-01), the intake marker the validator reads; it no longer carries `QA_RCA_ID`.\n"
         '            ("reject-source-missing-rca", "QA-120", "`QA_RCA` with their IDs", "`OMITTED_RCA` with their IDs",\n'
         '             "QA_PASS_BODY_INTAKE"),\n', 1),
        ("R10 AM-8 absent class branch, either rendering",
         '            ("reject-source-absent-crd-class-branch", "QA-120", "<td>`CRD`</td>", "", "QA_PASS_BODY_CLASS_MAP"),\n',
         '            ("reject-source-absent-crd-class-branch", "QA-120", *crd_cell, "QA_PASS_BODY_CLASS_MAP"),\n', 1),
        ("R11 AM-8 duplicate class branch, either rendering",
         '        anchor = producer_lines.index("<td>`CRD`</td>")\n'
         '        start, end = anchor - 2, producer_lines.index("</tr>", anchor)\n'
         '        if producer_lines[start] != "<tr>" or producer_lines[anchor - 1] != "<td>`PASS`</td>":\n'
         '            raise ValueError("Mutation anchor absent: reject-source-duplicate-crd-class-branch")\n'
         '        crd_row = "\\n".join(producer_lines[start:end + 1])\n',
         '        if "<td>`CRD`</td>" in producer_lines:\n'
         '            anchor = producer_lines.index("<td>`CRD`</td>")\n'
         '            start, end = anchor - 2, producer_lines.index("</tr>", anchor)\n'
         '            if producer_lines[start] != "<tr>" or producer_lines[anchor - 1] != "<td>`PASS`</td>":\n'
         '                raise ValueError("Mutation anchor absent: reject-source-duplicate-crd-class-branch")\n'
         '            crd_row = "\\n".join(producer_lines[start:end + 1])\n'
         "        else:\n"
         "            # AM-8: the pipe rendering holds the row on one line\n"
         '            pipe_rows = [line for line in producer_lines if line.startswith("| `PASS` | `CRD` |")]\n'
         "            if len(pipe_rows) != 1:\n"
         '                raise ValueError("Mutation anchor absent: reject-source-duplicate-crd-class-branch")\n'
         "            crd_row = pipe_rows[0]\n", 1),
        ("R90 contract ids", "GCFPE-20261009.1-100926.1-DIRECT-HANDOFF-", "GCFPE-20261027.1-102726.1-DIRECT-HANDOFF-", None),
        ("R91 release literal", "GCFPE-20261009.1", "GCFPE-20261027.1", None),
        ("R92 version literal", '100926.1"', '102726.1"', None),
        # last, so the release renames above never touch the mutation cases' own predecessor literals
        ("R05b coherent class regression's expected code",
         '    cases.append({"name": "reject-coherent-epic-to-crd-route-regression",\n'
         '                  "passed": observed == ["QA_PASS_CLASS_EDGES", "QA_PASS_CLASS_ROUTES"],\n'
         '                  "expected_errors": ["QA_PASS_CLASS_EDGES", "QA_PASS_CLASS_ROUTES"], "errors": observed})\n',
         '    cases.append({"name": "reject-coherent-epic-to-crd-route-regression",\n'
         '                  "passed": observed == ["CL05_CLOSE_EXIT_ROUTES"],\n'
         '                  "expected_errors": ["CL05_CLOSE_EXIT_ROUTES"], "errors": observed})\n', 1),
        ("R06 new mutation cases", "    source_case_count = 0\n", NEW_MUTATION_CASES + "    source_case_count = 0\n", 1),
    ]


# -------------------------------------------------------------------- C: change-flow's 102726.1 validator
def change_flow_subs(m: dict) -> list:
    return [
        ("C01 docstring",
         '"""Deterministic checks for the GCFPE-20261009.1 / 100926.1 Change Flow contract.\n\n'
         "Derived from the 091426.1 checks by MODIFICATION-20261011-gcfpe-mb008-to-promotion (PLAN PART-01). The 100926.1\n"
         "release has no prompt URL map and no topology readback: its members' URLs and parents are the graph's, and the\n"
         "contract names its governing plan as a repository file and the 091426.1 contract as its predecessor.\n\"\"\"",
         '"""Deterministic checks for the GCFPE-20261027.1 / 102726.1 Change Flow contract.\n\n'
         "Derived from the 100926.1 checks by MODIFICATION-20261027-gcfpe-backlog-open-items (PLAN PART-24). The release adds\n"
         "CL-05, the close-mutation-set stage between QA-120 PASS and the class-matching closure decision (PART-13), names\n"
         "its governing plan as a repository file and the 100926.1 contract as its predecessor.\n\"\"\"", 1),
        ("C02 timing import", "from validate_gcfpe_artifact_timing import validate_artifact_timing_contract\n",
         "from validate_gcfpe_artifact_timing import EXPECTED_POLICY_20261027, validate_artifact_timing_contract\n", 1),
        ("C03 bundled names", "gcfpe-20261009.1-100926.1-", "gcfpe-20261027.1-102726.1-", 2),
        ("C04 graph pin", 'EXPECTED_GRAPH_SHA = "43f84f29b9921c21f63ffbe21dd36a14bd846a89ae697ba3cf38746c2f887eb1"\n',
         f'EXPECTED_GRAPH_SHA = "{m["graph_sha"]}"\n', 1),
        ("C05 plan pin", 'EXPECTED_PLAN_SHA = "4de47784d63a895fe002283965032844409a247f7c8d0c4632c97c8b9dcd4d5b"\n'
                         'EXPECTED_PLAN_BYTES = 50156\n'
                         'EXPECTED_PLAN_PATH = "docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/PLAN-20261011.md"\n',
         f'EXPECTED_PLAN_SHA = "{m["plan_sha"]}"\nEXPECTED_PLAN_BYTES = {m["plan_bytes"]}\n'
         f'EXPECTED_PLAN_PATH = "{PLAN_PATH_IN_REPO}"\n', 1),
        ("C06 predecessor contract pin",
         'EXPECTED_PREDECESSOR_CONTRACT_SHA = "dbae180bb5c2f73e3f27a46601bfb5cbe7321e5431dbaba8763b1a576cd9343c"\n',
         f'EXPECTED_PREDECESSOR_CONTRACT_SHA = "{m["predecessor_sha"]}"\n', 1),
        ("C07 routing surface", 'EXPECTED_ROUTING_SURFACE = "d3a08833964a2610f88bd754b7e7510d"\nEXPECTED_ROUTING_SURFACE_ROWS = 290\n',
         f'EXPECTED_ROUTING_SURFACE = "{m["surface"]}"\nEXPECTED_ROUTING_SURFACE_ROWS = {m["surface_rows"]}\n', 1),
        ("C08 revision", '"CHANGE_FLOW_SPECIALIZATION_REVISION: 3.4.0" in skill', '"CHANGE_FLOW_SPECIALIZATION_REVISION: 3.5.0" in skill', 1),
        ("C09 target release", 'contract["target_release"] == "GCFPE-20261009.1"', 'contract["target_release"] == "GCFPE-20261027.1"', 1),
        ("C10 contract revision", 'contract["contract_revision"] == "4.2.0"', 'contract["contract_revision"] == "4.3.0"', 1),
        ("C11 prompt family", 'contract["prompt_version"] == "100926.1"', 'contract["prompt_version"] == "102726.1"', 1),
        ("C12 predecessor release",
         'contract["predecessor_release"] == "GCFPE-20260914.1" and contract["predecessor_prompt_version"] == "091426.1"',
         'contract["predecessor_release"] == "GCFPE-20261009.1" and contract["predecessor_prompt_version"] == "100926.1"', 1),
        ("C13 candidate count", 'contract["candidate_member_count"] == 55', f'contract["candidate_member_count"] == {m["node_count"]}', 1),
        ("C14 timing policy", "require(not validate_artifact_timing_contract(contract), ",
         "require(not validate_artifact_timing_contract(contract, EXPECTED_POLICY_20261027), ", 1),
        ("C15 predecessor contract id", 'predecessor["contract_id"] == "GCFPE-20260914.1-091426.1-DIRECT-HANDOFF-SELECTED"',
         'predecessor["contract_id"] == "GCFPE-20261009.1-100926.1-DIRECT-HANDOFF-SELECTED"', 1),
        ("C16 graph contract id", 'graph["contract_id"] == "GCFPE-20261009.1-CANDIDATE-GRAPH"',
         'graph["contract_id"] == "GCFPE-20261027.1-CANDIDATE-GRAPH"', 1),
        ("C17 graph candidate count", 'graph["candidate"]["member_count"] == 55', f'graph["candidate"]["member_count"] == {m["node_count"]}', 1),
        ("C18 edge count", "        len(graph[\"edges\"]) == 235\n",
         f"        # 102726.1: 235, less DOC-20's landed-lineage edge into PR-40 (PART-08), plus CL-05's four edges and the\n"
         f"        # CL-C-10 and CL-E-10 DO_NOT_CLOSE edges to CL-05 (PART-13); measured from the bundled graph.\n"
         f"        len(graph[\"edges\"]) == {m['edge_count']}\n", 1),
        ("C19 QA closure receivers",
         '    require(contract["qa_closure_contract"]["pass_receivers"] == {"EPIC": "CL-E-10", "CRD": "CL-C-10"}, "class-specific QA closure receivers")\n'
         '    for cls, destination in {"EPIC": "CL-E-10", "CRD": "CL-C-10"}.items():\n'
         '        rows = [r for r in graph["state_routes"]["QA-120"] if r.get("change_class") == cls and r.get("state") == "PASS"]\n'
         '        require(len(rows) == 1 and rows[0]["destinations"] == [destination], f"{cls} QA PASS receiver")\n'
         '        require(rows[0]["required_artifacts"] == ["QA_REPORT", "QA_RCA"], f"{cls} complete QA closure evidence")\n',
         '    require(contract["qa_closure_contract"]["pass_receivers"] == {"EPIC": "CL-05", "CRD": "CL-05"}, "QA PASS goes to the close-mutation-set stage")\n'
         '    require(contract["qa_closure_contract"]["close_stage_exit_receivers"] == {"EPIC": "CL-E-10", "CRD": "CL-C-10"}, "class-specific closure receivers after CL-05")\n'
         '    for cls, destination in {"EPIC": "CL-E-10", "CRD": "CL-C-10"}.items():\n'
         '        rows = [r for r in graph["state_routes"]["QA-120"] if r.get("change_class") == cls and r.get("state") == "PASS"]\n'
         '        require(len(rows) == 1 and rows[0]["destinations"] == ["CL-05"], f"{cls} QA PASS receiver")\n'
         '        require(rows[0]["required_artifacts"] == ["QA_REPORT", "QA_RCA"], f"{cls} complete QA closure evidence")\n'
         '        exits = [r for r in graph["state_routes"]["CL-05"] if r.get("change_class") == cls and r.get("state") == "CLOSE_PR_READY"]\n'
         '        require(len(exits) == 1 and exits[0]["destinations"] == [destination], f"{cls} CL-05 close-PR-ready receiver")\n', 1),
        ("C20 member count", 'require(len(member_ids) == 55 and len(set(member_ids)) == 55, "55 unique member IDs")',
         f'require(len(member_ids) == {m["node_count"]} and len(set(member_ids)) == {m["node_count"]}, "{m["node_count"]} unique member IDs")', 1),
        ("C21 R1 rows", 'require(contract["protected_identities"]["r1_rows"] == 46, "46-row R1")',
         'require(contract["protected_identities"]["r1_rows"] == 47, "47-row R1")', 1),
        ("C22 pass line", 'print("PASS: change-flow GCFPE-20261009.1 contract and Markdown-only source policy")',
         'print("PASS: change-flow GCFPE-20261027.1 contract and Markdown-only source policy")', 1),
    ]


# ------------------------------------------------------------------------------------------------ build
def build(installed: Path, out: Path, a, report: list | None = None) -> dict:
    if "/skills/synced/" in str(installed.resolve()) or "/skills/synced/" in str(out.resolve()):
        raise SystemExit("refusing the synced install directory")
    if out.exists():
        raise SystemExit(f"{out} exists")
    out.mkdir(parents=True)
    report = [] if report is None else report
    for k in PACKAGES:
        shutil.copytree(installed / k, out / k, ignore=shutil.ignore_patterns("__pycache__"))
    cf, fv, pr, gg = (out / k for k in PACKAGES)
    # A: redlines (and, only on opt-in, the R-P1 conditional set)
    applied = subprocess.run([sys.executable, str(PLAN_DIR / "package_apply.py"), str(out)], capture_output=True, text=True, env=ENV)
    if applied.returncode != 0:
        raise SystemExit(f"package_apply: {applied.stdout[-600:]}{applied.stderr[-400:]}")
    landed = subprocess.run([sys.executable, str(PLAN_DIR / "package_apply.py"), str(out), "--check"], capture_output=True, text=True, env=ENV)
    rows = json.loads(landed.stdout)["rows"]
    if landed.returncode != 0 or any(r["state"] != "LANDED" for r in rows):
        raise SystemExit("package_apply --check: not every redline landed")
    report.append({"step": "A redlines", "ops": len(rows), "all_landed": True})
    conditional = []
    if a.with_conditional:
        sets = {s["set"]: s for s in json.loads((PLAN_DIR / "package-redlines.json").read_text(encoding="utf-8"))["conditional_sets"]}
        for name in a.with_conditional:
            for op in sets[name]["ops"]:
                substitute(out / op["skill"] / op["file"], [(op["id"], op["old"], op["new"], op["count"])], report)
            conditional.append(name)
    report.append({"step": "A conditional sets", "applied": conditional, "default_excluded": not conditional})
    # N: R1 successor files, checked against the pins the redlined suite carries
    r1 = Path(a.r1_dir)
    suite = fv / "scripts/validate_flowmaster.py"
    pins = {"oracle-glow-hde-canonical-change-flow-r1-20261027.json": pin_from(suite, "EXPECTED_ORACLE_SHA256"),
            "map-glow-hde-canonical-change-flow-r1-runtime-map-20261027.json": pin_from(suite, "EXPECTED_CHANGE_RUNTIME_MAP_SHA256")}
    for src, (pkg, rel) in R1_FILES.items():
        f = r1 / src
        if src in pins and sha256(f) != pins[src]:
            raise SystemExit(f"N: {src} digest {sha256(f)} differs from the suite pin {pins[src]}")
        dest = out / pkg / rel
        if dest.exists():
            raise SystemExit(f"N: {rel} already exists in {pkg}")
        shutil.copyfile(f, dest)
    report.append({"step": "N R1 successor files", "files": {rel: sha256(out / pkg / rel) for _, (pkg, rel) in R1_FILES.items()},
                   "pinned_by_suite": True})
    # B: bundle
    contract_path = Path(a.production_contract)
    gj = graph_block(Path(a.production_graph_md))
    for k in (cf, fv):
        shutil.copyfile(contract_path, k / f"references/{NEW}-direct-handoff-contract.json")
        (k / f"references/{NEW}-candidate-graph-contract.json").write_text(gj, encoding="utf-8")
    bundled_c, bundled_g = fv / f"references/{NEW}-direct-handoff-contract.json", fv / f"references/{NEW}-candidate-graph-contract.json"
    report.append({"step": "B bundle", "contract_sha256": sha256(bundled_c), "graph_sha256": sha256(bundled_g)})
    # F
    fixture_path = write_fixtures(fv)
    report.append({"step": "F fixtures", "sha256": sha256(fixture_path),
                   "count": len(json.loads(fixture_path.read_text(encoding="utf-8"))["scenarios"])})
    # P + M
    cmd = [sys.executable, str(PLAN_DIR / "make_profile_20261027.py"), "build", str(fv / "scripts/validate_gcfpe_20261009.py"),
           str(fv / "scripts/validate_gcfpe_20261027.py"), "--contract", str(bundled_c), "--graph", str(bundled_g),
           "--fixtures", str(fixture_path), "--plan", a.plan, "--map", a.map, "--members-tsv", a.members_tsv,
           "--profile-base", str(fv / f"references/{OLD}-validation-profile.json"),
           "--profile-out", str(fv / f"references/{NEW}-validation-profile.json")] + (["--stand-in-ok"] if a.stand_in_ok else [])
    made = subprocess.run(cmd, capture_output=True, text=True, env=ENV)
    if made.returncode != 0:
        raise SystemExit(f"make_profile: {made.stdout[-800:]}{made.stderr[-800:]}")
    mr = json.loads(made.stdout)
    report.append({"step": "P+M make_profile_20261027.py", "substitutions": len(mr["report"]),
                   "validator_sha256": mr["validator_sha256"], "profile": mr["profile_written"]["sha256"],
                   "stand_in_used": mr["stand_in_used"], "leftover_literal_counts": mr["leftover_literal_counts"]})
    # R
    base_runner = (fv / "scripts/run_gcfpe_20261009_fixtures.py").read_text(encoding="utf-8")
    runner = fv / "scripts/run_gcfpe_20261027_fixtures.py"
    runner.write_text(base_runner, encoding="utf-8")
    substitute(runner, runner_subs(base_runner), report)
    # C
    base_cf = cf / "scripts/validate_gcfpe_20261009.py"
    cf_mod = load(base_cf, "cf_base_validator_for_surface")
    contract = json.loads(contract_path.read_text(encoding="utf-8"))
    surface, srows = cf_mod.routing_surface(contract)
    graph_doc = json.loads(gj)
    plan = Path(a.plan)
    m = {"graph_sha": sha256(cf / f"references/{NEW}-candidate-graph-contract.json"), "plan_sha": sha256(plan),
         "plan_bytes": plan.stat().st_size, "predecessor_sha": sha256(cf / f"references/{OLD}-direct-handoff-contract.json"),
         "surface": surface, "surface_rows": srows, "edge_count": len(graph_doc["edges"]), "node_count": len(graph_doc["nodes"])}
    cf_new = cf / "scripts/validate_gcfpe_20261027.py"
    shutil.copyfile(base_cf, cf_new)
    substitute(cf_new, change_flow_subs(m), report)
    report.append({"step": "C measured", "measured": m})
    # I: self-identity, last
    for p in list(out.rglob("__pycache__")):
        shutil.rmtree(p)
    ident = load(fv / "scripts/validate_gcfpe_20261027.py", "fv_identity_102726")
    for p in list(out.rglob("__pycache__")):
        shutil.rmtree(p)
    text = (fv / "SKILL.md").read_text(encoding="utf-8")
    old_line = next(l for l in text.splitlines() if l.startswith("SKILL_TREE_SHA256: "))
    digest = ident.skill_tree_digest(fv)
    (fv / "SKILL.md").write_text(text.replace(old_line + "\n", f"SKILL_TREE_SHA256: {digest}\n", 1), encoding="utf-8")
    report.append({"step": "I self-identity", "old": old_line.split()[-1], "new": digest,
                   "verified": not ident.validate_self_identity(fv)})
    return {"stand_in_used": bool(mr["stand_in_used"]), "conditional_sets_applied": conditional, "report": report}


def tree_digest(root: Path) -> dict:
    return {p.relative_to(root).as_posix(): sha256(p) for p in sorted(root.rglob("*")) if p.is_file()}


def add_inputs(ap: argparse.ArgumentParser) -> None:
    for k in ("--production-contract", "--production-graph-md", "--r1-dir", "--plan", "--map"):
        ap.add_argument(k, required=True)
    ap.add_argument("--members-tsv", default=str(PLAN_DIR / "members-100926.1.tsv"))
    ap.add_argument("--stand-in-ok", action="store_true")
    ap.add_argument("--with-conditional", action="append", choices=["R-P1"], default=[])


def selftest(installed: Path, scratch: Path, a) -> dict:
    """Each injected defect must stop the build before an output is accepted."""
    rows = {}
    work = scratch / "package-build-selftest"
    if work.exists():
        shutil.rmtree(work)
    work.mkdir(parents=True)

    def stops(tag: str, prepare) -> bool:
        inst = work / f"{tag}-installed"
        shutil.copytree(installed, inst, ignore=shutil.ignore_patterns("__pycache__"))
        b = argparse.Namespace(**vars(a))
        prepare(inst, b)
        try:
            build(inst, work / f"{tag}-out", b)
        except SystemExit:
            return True
        finally:
            shutil.rmtree(inst, ignore_errors=True)
            shutil.rmtree(work / f"{tag}-out", ignore_errors=True)
        return False

    def moved_base(inst, b):
        p = inst / "change-flow/SKILL.md"
        p.write_text(p.read_text(encoding="utf-8").replace("CHANGE_FLOW_SPECIALIZATION_REVISION: 3.4.0", "CHANGE_FLOW_SPECIALIZATION_REVISION: 3.4.9"), encoding="utf-8")
    rows["stops_on_moved_redline_base"] = stops("moved", moved_base)

    def wrong_r1(inst, b):
        d = work / "bad-r1"
        shutil.copytree(a.r1_dir, d, dirs_exist_ok=True)
        p = d / "map-glow-hde-canonical-change-flow-r1-runtime-map-20261027.json"
        p.write_bytes(p.read_bytes() + b" ")
        b.r1_dir = str(d)
    rows["stops_on_r1_digest_off_pin"] = stops("r1", wrong_r1)

    def moved_runner(inst, b):
        p = inst / "flowmaster-validate/scripts/run_gcfpe_20261009_fixtures.py"
        p.write_text(p.read_text(encoding="utf-8").replace('"validator_revision": "3.4.1",', '"validator_revision": "3.4.2",'), encoding="utf-8")
    rows["stops_on_moved_runner_base"] = stops("runner", moved_runner)

    def moved_cf(inst, b):
        p = inst / "change-flow/scripts/validate_gcfpe_20261009.py"
        p.write_text(p.read_text(encoding="utf-8").replace('"46-row R1"', '"46 rows"'), encoding="utf-8")
    rows["stops_on_moved_change_flow_validator_base"] = stops("cf", moved_cf)

    def moved_fixture(inst, b):
        p = inst / f"flowmaster-validate/fixtures/{OLD}/scenarios.json"
        p.write_text(p.read_text(encoding="utf-8").replace('  "release": "GCFPE-20261009.1",\n', '  "release":"GCFPE-20261009.1",\n'), encoding="utf-8")
    rows["stops_on_moved_fixture_base"] = stops("fixture", moved_fixture)

    def no_standin_flag(inst, b):
        b.stand_in_ok = False
    rows["stops_on_stand_in_map_without_flag"] = stops("flag", no_standin_flag)
    rows["refuses_synced_directory"] = False
    try:
        build(Path("/root/.claude/skills/synced/x"), work / "synced-out", a)
    except SystemExit as e:
        rows["refuses_synced_directory"] = "synced" in str(e)
    shutil.rmtree(work, ignore_errors=True)
    return {"mode": "selftest", "rows": rows, "selftest_ok": all(rows.values()), "stand_in_used": a.stand_in_ok}


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("build", "check"):
        p = sub.add_parser(name)
        p.add_argument("installed"); p.add_argument("out")
        add_inputs(p)
    p = sub.add_parser("selftest")
    p.add_argument("installed"); p.add_argument("scratch")
    add_inputs(p)
    a = ap.parse_args()
    installed = Path(a.installed).resolve()
    if a.cmd == "selftest":
        res = selftest(installed, Path(a.scratch).resolve(), a)
        print(json.dumps(res, indent=1))
        return 0 if res["selftest_ok"] else 1
    out = Path(a.out).resolve()
    if a.cmd == "check":
        with tempfile.TemporaryDirectory(dir=os.environ.get("TMPDIR")) as tmp:
            build(installed, Path(tmp) / "out", a)
            want, have = tree_digest(Path(tmp) / "out"), tree_digest(out)
        diff = sorted(k for k in set(want) | set(have) if want.get(k) != have.get(k))
        print(json.dumps({"mode": "check", "equal": not diff, "differing": diff, "files": len(have)}, indent=1))
        return 0 if not diff else 1
    result = build(installed, out, a)
    print(json.dumps({"mode": "build", "out": str(out), **result}, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
