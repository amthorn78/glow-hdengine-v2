#!/usr/bin/env python3
"""Release values, the glow-graph-contract patch and the 102726.1 direct-handoff contracts
(MODIFICATION-20261027-gcfpe-backlog-open-items, PART-13 and PART-24; W7 tooling Q1 and Q5, W7-D5, C-7, C-11).

  contracts_102726.py values <repo-root> [--check]
        write plan/release-values-102726.1.json from W7.json repo_edits RE-W7-01 (copied, never retyped). --check
        exits 1 unless the file on disk is byte-identical. C-7: merge_pending_requirements carries the real-input
        P1 condition; C-11: the 2026-09-23 oracle and map join historical_non_executable_references.
  contracts_102726.py fill <release-values> <graph.md> <plan-file> <out> --map M [--plan-path P] [--stand-in]
        fill @PLAN_PATH, @PLAN_SHA256, @PLAN_BYTES (from <plan-file>), @GRAPH_MEMBER_RULE (the graph's
        candidate.member_rule) and @CL05_PARENT_ID (C-19: the successor map's CL-05 parent_id; never typed); refuse a
        graph whose node ids, member count or R1 pins disagree with the file, and refuse any marker left unfilled.
        --stand-in records that <plan-file> stands in for the frozen PLAN and admits a stand-in map.
  contracts_102726.py patch-ggc <installed-glow-graph-contract> <out-dir> [--patch-file F]
        copy the installed skill to <out-dir> and apply W5's SR-GG-1..3 (W5.json skill_redlines) and C-19's bounded
        regenerator exception (C19_GG_REDLINES) with exact counts; a second application is refused. With
        --patch-file, also write the unified diff (base/ -> work/).
  contracts_102726.py run <repo-root> <skills-root> <scratch> <candidate.md> <production.md> <oracle-20261027>
        <plan-file> --map M [--stand-in]
        Q1: the patched regenerator regenerates the shipped 100926.1 contract byte for byte (both bundled copies).
        Q5: the candidate and production 102726.1 contracts, with their checks, and the injected refusals (an
        unfilled marker, the 100926.1 release-values file against this build, an oracle the graph does not pin, a
        graph pin the patched regenerator does not know, the unpatched regenerator against this build) and C-19's
        (another member's staged parent, another field of CL-05, CL-05 without its parent, a map without CL-05's
        parent).

C-19 (repair R2): CL-05, the sole added member, has no template-carried staged parent. The release-values file sets
member_registry.CL-05.staged_parent_id and notion_page_manifest.CL-05.parent_id from @CL05_PARENT_ID, which `fill`
takes from the successor map's CL-05 parent_id, and the patched regenerator admits exactly those two paths for the
graph's sole added node when the template does not carry it (and requires them). The 55 carried members keep their
template-carried values, as 100926.1 did; `run` lists that.

Writes only <out>, <out-dir>, <scratch> and, for `values`, plan/release-values-102726.1.json. Run with
PYTHONDONTWRITEBYTECODE=1.
"""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
REL = "docs/ephemeral/modifications/evidence/20261027-gcfpe-backlog-open-items/plan"
PLAN_PATH = "docs/ephemeral/modifications/evidence/20261027-gcfpe-backlog-open-items/PLAN-20261027.md"
TEMPLATE = "docs/graph/contract-template/gcfpe-20260914.1-091426.1-direct-handoff-contract-4.0.6.json"
DECISIONS = "docs/prompt_ecosystem_management/gcfpe.decision-record.md"
PRED_VALUES = ("docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/execute/contracts/"
               "release-values-100926.1.filled.json")
PRED_CONTRACT = "references/gcfpe-20261009.1-100926.1-direct-handoff-contract.json"
PRED_SHA, PRED_BYTES = "cd291f17ac832cc0aad62b5cc7e554bd6d524e18de7aea7f2f4fec5a1651317f", 631061
ORACLE_0923 = "references/glow-hde-canonical-change-flow-r1-20260923.json"
NEW_ORACLE_SHA = "f1b221e91cd3c22ce9923d555671bce0e7af25335b69dabab60e097f3fa8d46d"
MARKER_RE = re.compile(r'"@[A-Z0-9_]+"')
TSV = HERE / "members-100926.1.tsv"
CL05_PARENT_OPS = [["set", ["member_registry", "CL-05", "staged_parent_id"], "@CL05_PARENT_ID"],
                   ["set", ["notion_page_manifest", "CL-05", "parent_id"], "@CL05_PARENT_ID"]]
# C-19: the bounded regenerator exception, applied after W5's SR-GG-1..3 here and through plan/package-redlines.json in
# the glow-graph-contract package build (make_package_redlines_102726.py imports this list; it is typed once).
C19_GG_REDLINES = [
    {"id": "R2-C19-GG-1", "file": "scripts/regenerate_contract.py", "count": 1,
     "old": ("def regenerate(template: dict, graph: dict, graph_bytes: bytes, value_table=()) -> dict:\n"
             "    out = copy.deepcopy(template)\n"),
     "new": ("def added_member_parent_paths(template: dict, graph: dict) -> set:\n"
             "    \"\"\"MODIFICATION-20261027-gcfpe-backlog-open-items C-19: the one bounded exception to the rule that no value-table\n"
             "    entry targets member_registry. A sole added node the template does not carry has no template-carried staged\n"
             "    parent, so a release-values file may set exactly its member_registry staged_parent_id and notion_page_manifest\n"
             "    parent_id, and regenerate() then requires both. Every carried member keeps its template-carried values.\"\"\"\n"
             "    added = [m for m in (graph.get(\"proofs\") or {}).get(\"sole_added_node\") or []\n"
             "             if m not in (template.get(\"member_registry\") or {})]\n"
             "    return {p for m in added for p in ((\"member_registry\", m, \"staged_parent_id\"),\n"
             "                                       (\"notion_page_manifest\", m, \"parent_id\"))}\n"
             "\n\n"
             "def regenerate(template: dict, graph: dict, graph_bytes: bytes, value_table=()) -> dict:\n"
             "    out = copy.deepcopy(template)\n")},
    {"id": "R2-C19-GG-2", "file": "scripts/regenerate_contract.py", "count": 1,
     "old": ("    mirrored = mirrored_paths(graph)\n"
             "    for op in value_table:\n"
             "        assert op[1][0] != \"member_registry\""),
     "new": ("    mirrored = mirrored_paths(graph)\n"
             "    added_parent = added_member_parent_paths(template, graph)\n"
             "    for op in value_table:\n"
             "        if op[0] == \"set\" and tuple(op[1]) in added_parent:\n"
             "            continue  # C-19: the sole added member's staged parent, and nothing else of it\n"
             "        assert op[1][0] != \"member_registry\"")},
    {"id": "R2-C19-GG-3", "file": "scripts/regenerate_contract.py", "count": 1,
     "old": "    assert set(out[\"member_registry\"]) == {n[\"id\"] for n in graph[\"nodes\"]}, \"member set != graph node set\"\n",
     "new": ("    for member in sorted({p[1] for p in added_parent}):\n"
             "        parent = out[\"member_registry\"][member].get(\"staged_parent_id\")\n"
             "        assert isinstance(parent, str) and re.fullmatch(r\"[0-9a-f]{32}\", parent), \\\n"
             "            f\"added member {member} has no staged parent\"\n"
             "        assert out[\"notion_page_manifest\"][member].get(\"parent_id\") == parent, \\\n"
             "            f\"added member {member}: manifest parent differs from its staged parent\"\n"
             "    assert set(out[\"member_registry\"]) == {n[\"id\"] for n in graph[\"nodes\"]}, \"member set != graph node set\"\n")},
]
LIFECYCLE_KEYS = {"contract_id", "status", "selection_status", "selection_claim", "selected_member_count",
                  "promoted_at", "selected_release", "selected_prompt_version"}


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def graph_obj(path: str) -> dict:
    lines = Path(path).read_text(encoding="utf-8").split("\n")
    s = next(i for i, l in enumerate(lines) if l == "```json")
    e = max(i for i, l in enumerate(lines) if l == "```")
    return json.loads("\n".join(lines[s + 1:e]))


# ---------------------------------------------------------------- values
def values(repo: str, *flags: str) -> int:
    w7 = json.loads((Path(repo) / REL / "work/W7.json").read_text(encoding="utf-8"))
    re1 = next(r for r in w7["repo_edits"] if r["id"] == "RE-W7-01")
    assert re1["path"] == REL + "/release-values-102726.1.json"
    doc = copy.deepcopy(re1["content"])
    ops = {tuple(op[1]): op for op in doc["ops"]}
    # C-7: the real-input P1 condition, inserted after the two review requirements (W1-Q1, W7-D5).
    mpr = ops[("pr_development_contract", "merge_pending_requirements")][2]
    assert mpr.count("no open P1 thread on a real input") == 1 and len(mpr) == 7
    # C-11: the 2026-09-23 pair joins the historical references.
    hist = ops[("historical_non_executable_references",)][2]
    assert hist[-2:] == ["glow-hde-canonical-change-flow-r1-20260923.json",
                         "glow-hde-canonical-change-flow-r1-runtime-map-20260923.json"]
    assert ops[("sole_added_member",)][2] == "CL-05" and len(ops[("candidate_prompt_ids",)][2]) == 56
    # C-19: CL-05's staged parent and manifest parent, filled from the successor map by `fill` (bounded regenerator
    # exception for the sole added member; the 55 carried members keep their template-carried values).
    assert not any(tuple(op[1][:2]) in (("member_registry", "CL-05"), ("notion_page_manifest", "CL-05")) for op in doc["ops"])
    doc["ops"] += CL05_PARENT_OPS
    doc["sources"]["member_registry.CL-05.staged_parent_id, notion_page_manifest.CL-05.parent_id"] = (
        "C-19: the sole added member has no template-carried parent; @CL05_PARENT_ID is the successor map's CL-05 "
        "parent_id (the HDE Change Flow hub it is moved under, C-9), filled by contracts_102726.py fill. The 55 carried "
        "members keep their template-carried staged_parent_id and parent_id, as 100926.1 did.")
    doc["sources"]["record"] = ("Written by contracts_102726.py values from W7.json repo_edits RE-W7-01; coordinator "
                                "decisions C-7 (merge_pending_requirements) and C-11 (historical references) checked; "
                                "C-19's two CL-05 parent ops added (repair R2).")
    text = json.dumps(doc, indent=1, ensure_ascii=False) + "\n"
    out = Path(repo) / REL / "release-values-102726.1.json"
    if "--check" in flags:
        same = out.exists() and out.read_text(encoding="utf-8") == text
        print(json.dumps({"release_values_file_current": same}))
        return 0 if same else 1
    out.write_text(text, encoding="utf-8")
    print(json.dumps({"written": str(out), "ops": len(doc["ops"]),
                      "markers": sorted(set(MARKER_RE.findall(json.dumps(doc["ops"]))))}))
    return 0


# ---------------------------------------------------------------- fill
def map_parent(map_path: str, stand_in_ok: bool) -> str:
    """C-19: CL-05's parent from the checked successor map (successor_map_102726.load), never typed."""
    spec = importlib.util.spec_from_file_location("successor_map_102726", HERE / "successor_map_102726.py")
    SM = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(SM)
    smap = SM.load(map_path, str(TSV), stand_in_ok)
    parent = smap["members"]["CL-05"]["parent_id"]
    assert isinstance(parent, str) and re.fullmatch(r"[0-9a-f]{32}", parent), "the map carries no CL-05 parent_id"
    return parent


def fill_doc(doc: dict, graph: dict, plan_file: Path, plan_path: str, cl05_parent: str) -> dict:
    pb = plan_file.read_bytes()
    subst = {"@PLAN_PATH": plan_path, "@PLAN_SHA256": sha(pb), "@PLAN_BYTES": len(pb),
             "@GRAPH_MEMBER_RULE": graph["candidate"]["member_rule"], "@CL05_PARENT_ID": cl05_parent}

    def walk(v):
        if isinstance(v, str) and v in subst:
            return subst[v]
        if isinstance(v, list):
            return [walk(x) for x in v]
        if isinstance(v, dict):
            return {k: walk(x) for k, x in v.items()}
        return v
    out = copy.deepcopy(doc)
    out["ops"] = walk(out["ops"])
    left = sorted(set(MARKER_RE.findall(json.dumps(out["ops"]))))
    assert not left, f"unfilled markers: {left}"
    assert (out["release"], out["version_family"]) == (graph["candidate"]["release"], graph["candidate"]["version_family"])
    ops = {tuple(op[1]): op for op in out["ops"]}
    ids = sorted(n["id"] for n in graph["nodes"])
    assert ops[("candidate_prompt_ids",)][2] == ids, "candidate_prompt_ids differ from the graph's node ids"
    assert ops[("graph_proofs", "member_count")][2] == len(ids) == graph["candidate"]["member_count"]
    pi = graph["protected_identities"]
    assert ops[("protected_identities", "r1_rows")][2] == pi["r1_rows"]
    assert ops[("protected_identities", "r1_material_rows")][2] == pi["r1_material_rows"]
    assert [ops[("sole_added_member",)][2]] == graph["proofs"]["sole_added_node"], "sole_added_member"
    return out


def fill(values_path: str, graph_md: str, plan_file: str, out: str, *flags: str) -> int:
    plan_path = flags[flags.index("--plan-path") + 1] if "--plan-path" in flags else PLAN_PATH
    if "--map" not in flags:
        raise SystemExit("fill: --map is required (C-19: @CL05_PARENT_ID comes from the successor map)")
    map_path = flags[flags.index("--map") + 1]
    doc = json.loads(Path(values_path).read_text(encoding="utf-8"))
    parent = map_parent(map_path, "--stand-in" in flags)
    filled = fill_doc(doc, graph_obj(graph_md), Path(plan_file), plan_path, parent)
    filled["filled"] = {"plan_file_stand_in": "--stand-in" in flags, "plan_path": plan_path,
                        "cl05_parent_from_map": Path(map_path).name}
    Path(out).write_text(json.dumps(filled, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"fill_ok": True, "written": out, "stand_in_used": "--stand-in" in flags}))
    return 0


# ---------------------------------------------------------------- patch
def patch_ggc(installed: str, out_dir: str, *flags: str) -> int:
    src, dst = Path(installed), Path(out_dir)
    if dst.exists():
        raise SystemExit(f"patch-ggc: {dst} exists")
    w5 = json.loads((HERE / "work/W5.json").read_text(encoding="utf-8"))
    reds = [r for r in w5["skill_redlines"] if r["id"] in ("SR-GG-1", "SR-GG-2", "SR-GG-3")]
    assert [r["id"] for r in reds] == ["SR-GG-1", "SR-GG-2", "SR-GG-3"]
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns("__pycache__"))
    rows = apply_redlines(dst, reds + C19_GG_REDLINES)
    if "--patch-file" in flags:
        pf = Path(flags[flags.index("--patch-file") + 1])
        tmp = dst.parent / (dst.name + "-diff")
        if tmp.exists():
            shutil.rmtree(tmp)
        (tmp / "base").mkdir(parents=True)
        shutil.copytree(src, tmp / "base/glow-graph-contract", ignore=shutil.ignore_patterns("__pycache__"))
        shutil.copytree(dst, tmp / "work/glow-graph-contract")
        r = subprocess.run(["diff", "-ruN", "base/glow-graph-contract", "work/glow-graph-contract"], cwd=tmp,
                           capture_output=True, text=True)
        pf.write_text(r.stdout, encoding="utf-8")
        shutil.rmtree(tmp)
    print(json.dumps({"patch_ok": all(r["landed"] for r in rows), "rows": rows}))
    return 0 if all(r["landed"] for r in rows) else 1


def apply_redlines(root: Path, reds: list) -> list:
    rows = []
    for r in reds:
        p = root / r["file"]
        text = p.read_text(encoding="utf-8")
        if text.count(r["new"]):
            raise SystemExit(f"{r['id']}: already applied")
        n = text.count(r["old"])
        if n != r["count"]:
            raise SystemExit(f"{r['id']}: old string occurs {n} times, expected {r['count']}")
        p.write_text(text.replace(r["old"], r["new"]), encoding="utf-8")
        rows.append({"id": r["id"], "file": r["file"], "landed": p.read_text(encoding="utf-8").count(r["new"]) == 1})
    return rows


# ---------------------------------------------------------------- run (Q1, Q5)
def run(repo: str, skills: str, scratch: str, cand_md: str, prod_md: str, oracle: str, plan_file: str,
        *flags: str) -> int:
    R, S, W = Path(repo), Path(skills), Path(scratch) / "contracts"
    if "--map" not in flags:
        raise SystemExit("run: --map is required (C-19)")
    map_path = str(Path(flags[flags.index("--map") + 1]).resolve())  # the subprocesses run with cwd=<repo-root>
    if W.exists():
        shutil.rmtree(W)
    W.mkdir(parents=True)
    rec: dict = {"stand_in_used": "--stand-in" in flags,
                 "stand_ins": ("graph builds from the stand-in successor map; plan file " + plan_file
                               + " stands in for the frozen PLAN-20261027.md") if "--stand-in" in flags else None}
    ggc = W / "glow-graph-contract"
    q = subprocess.run([sys.executable, __file__, "patch-ggc", str(S / "glow-graph-contract"), str(ggc)],
                       capture_output=True, text=True)
    rec["patch"] = json.loads(q.stdout) if q.returncode == 0 else {"patch_ok": False, "stderr": q.stderr[-400:]}
    q = subprocess.run([sys.executable, __file__, "patch-ggc", str(S / "glow-graph-contract"), str(ggc)],
                       capture_output=True, text=True)
    rec["patch_second_application_refused"] = q.returncode != 0
    try:
        apply_redlines(ggc, [r for r in json.loads((HERE / "work/W5.json").read_text(encoding="utf-8"))["skill_redlines"]
                             if r["id"] == "SR-GG-2"])
        rec["patch_reapply_in_place_refused"] = False
    except SystemExit:
        rec["patch_reapply_in_place_refused"] = True
    recipe = ggc / "scripts/contract_recipe.py"
    gp = S / "glow-graph-contract/scripts/graph_parts.py"
    env = {"PYTHONDONTWRITEBYTECODE": "1", "PATH": "/usr/bin:/bin", "TMPDIR": str(W)}

    def go(args) -> tuple[int, str]:
        r = subprocess.run([sys.executable, *map(str, args)], capture_output=True, text=True, env=env, cwd=R)
        return r.returncode, r.stdout + r.stderr

    # Q1: the shipped 100926.1 contract, byte for byte, with the patched regenerator.
    sel = W / "graph-100926.1.md"
    code, out = go([gp, "build", R / "docs/graph/parts", sel])
    shipped = [S / "change-flow" / PRED_CONTRACT, S / "flowmaster-validate" / PRED_CONTRACT]
    code1, out1 = go([recipe, sel, R / TEMPLATE, S / "flowmaster-validate" / ORACLE_0923, R / DECISIONS,
                      W / "contract-100926.1.json", "--contract-revision", "4.2.0", "--primary-skill-revision", "1.4.0",
                      "--release-values", R / PRED_VALUES, "--check", *shipped])
    p1 = W / "contract-100926.1.json"
    rec["Q1"] = {"main_build": out.split("\n")[0:2], "recipe_exit": code1, "equal_lines": out1.count("EQUAL    "),
                 "different_lines": out1.count("DIFFERENT"),
                 "sha256": sha(p1.read_bytes()) if p1.exists() else None,
                 "bytes": p1.stat().st_size if p1.exists() else None}
    rec["Q1"]["Q1_PASS"] = (code1 == 0 and rec["Q1"]["equal_lines"] == 2 and rec["Q1"]["sha256"] == PRED_SHA
                            and rec["Q1"]["bytes"] == PRED_BYTES)

    # Q5: fill the release values from the candidate graph, generate both contracts.
    rv = HERE / "release-values-102726.1.json"
    filled = W / "release-values-102726.1.filled.json"
    si = ["--stand-in"] if "--stand-in" in flags else []
    code_f, out_f = go([__file__, "fill", rv, cand_md, plan_file, filled, "--map", map_path] + si)
    rec["fill"] = {"exit": code_f, "out": out_f.strip()[-300:]}
    contracts = {}
    for name, md in (("candidate", cand_md), ("production", prod_md)):
        out_p = W / f"gcfpe-20261027.1-102726.1-{name}-contract.json"
        c, o = go([recipe, md, R / TEMPLATE, oracle, R / DECISIONS, out_p, "--contract-revision", "4.3.0",
                   "--primary-skill-revision", "1.5.0", "--release-values", filled])
        contracts[name] = {"exit": c, "sha256": sha(out_p.read_bytes()) if out_p.exists() else None,
                           "bytes": out_p.stat().st_size if out_p.exists() else None, "path": str(out_p)}
        if c:
            contracts[name]["error"] = o[-600:]
    rec["contracts"] = contracts
    ok_written = all(v["exit"] == 0 for v in contracts.values())
    checks = {"both_written": ok_written}
    if ok_written:
        c = {k: json.loads(Path(v["path"]).read_text(encoding="utf-8")) for k, v in contracts.items()}
        checks["no_promoted_at"] = all("promoted_at" not in x for x in c.values())
        checks["contract_ids"] = (c["candidate"]["contract_id"] == "GCFPE-20261027.1-102726.1-DIRECT-HANDOFF-CANDIDATE"
                                  and c["production"]["contract_id"] == "GCFPE-20261027.1-102726.1-DIRECT-HANDOFF-SELECTED")
        checks["candidate_prompt_ids_56"] = all(len(x["candidate_prompt_ids"]) == 56
                                                and sorted(x["member_registry"]) == x["candidate_prompt_ids"]
                                                for x in c.values())
        checks["heads"] = all((x["target_release"], x["prompt_version"], x["candidate_member_count"],
                               x["predecessor_release"], x["predecessor_prompt_version"],
                               x["selected_member_count_during_staging"], x["sole_added_member"],
                               x["contract_revision"], x["pr_development_contract"]["primary_skill_revision"])
                              == ("GCFPE-20261027.1", "102726.1", 56, "GCFPE-20261009.1", "100926.1", 55, "CL-05",
                                  "4.3.0", "1.5.0") for x in c.values())
        checks["r1_pins"] = all((x["protected_identities"]["r1_oracle_sha256"], x["protected_identities"]["r1_rows"],
                                 x["protected_identities"]["r1_material_rows"]) == (NEW_ORACLE_SHA, 47, 21)
                                for x in c.values())
        checks["route_edge_count_240"] = all(x["graph_proofs"]["route_edge_count"] == 240 and len(x["route_edges"]) == 240
                                             for x in c.values())
        checks["qa_closure_via_cl05"] = all(x["route_graph"]["crd_qa_pass_closure"] == ["QA-120", "CL-05", "CL-C-10", "CL-20"]
                                            and x["qa_closure_contract"]["pass_receivers"] == {"CRD": "CL-05", "EPIC": "CL-05"}
                                            for x in c.values())
        checks["merge_pending_real_input_p1"] = all("no open P1 thread on a real input" in
                                                    x["pr_development_contract"]["merge_pending_requirements"]
                                                    for x in c.values())
        checks["historical_refs_include_20260923"] = all(
            "glow-hde-canonical-change-flow-r1-20260923.json" in x["historical_non_executable_references"]
            for x in c.values())
        checks["candidate_member_rule_from_graph"] = all(
            x["candidate_member_rule"] == graph_obj(cand_md)["candidate"]["member_rule"] for x in c.values())
        checks["lifecycle"] = (c["candidate"]["status"] == "UNSELECTED_CANDIDATE"
                               and c["production"]["status"] == "SELECTED_PRODUCTION"
                               and "selected_release" not in c["candidate"]
                               and c["production"].get("selected_release") == "GCFPE-20261027.1")
        sys.path.insert(0, str(S / "flowmaster-validate/scripts"))
        spec = importlib.util.spec_from_file_location("v1009", S / "flowmaster-validate/scripts/validate_gcfpe_20261009.py")
        v = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(v)

        def view(x):
            y = v.release_semantic_view(x)
            for k in LIFECYCLE_KEYS:
                y.pop(k, None)
            y["source_snapshot"]["frozen_candidate_graph"].pop("sha256", None)
            return y
        checks["release_semantic_equal"] = view(c["candidate"]) == view(c["production"])
        # C-19: CL-05's two parent fields come from the map; the 55 carried members keep the template's values
        parent = map_parent(map_path, "--stand-in" in flags)
        tpl = json.loads((R / TEMPLATE).read_text(encoding="utf-8"))
        checks["cl05_parent_from_map"] = all(x["member_registry"]["CL-05"].get("staged_parent_id") == parent
                                             and x["notion_page_manifest"]["CL-05"].get("parent_id") == parent
                                             for x in c.values())
        carried = sorted(k for k in c["production"]["member_registry"] if k in tpl["member_registry"])
        checks["carried_parents_template_values"] = len(carried) == 55 and all(
            x["member_registry"][k]["staged_parent_id"] == tpl["member_registry"][k]["staged_parent_id"]
            and x["notion_page_manifest"][k]["parent_id"] == tpl["notion_page_manifest"][k]["parent_id"]
            for x in c.values() for k in carried)
        rec["c19_listed"] = {"added_member_parent": {"member": "CL-05", "source": "successor map CL-05.parent_id",
                                                     "value": parent, "stand_in": "--stand-in" in flags},
                             "carried_members_template_values": len(carried),
                             "note": "the 55 carried members keep their template-carried staged_parent_id and "
                                     "notion_page_manifest parent_id, as 100926.1 did (C-19)"}
    rec["Q5_checks"] = checks

    # Injected refusals.
    inj = {}
    unfilled = W / "unfilled.json"
    shutil.copyfile(rv, unfilled)
    c, o = go([recipe, cand_md, R / TEMPLATE, oracle, R / DECISIONS, W / "x.json", "--contract-revision", "4.3.0",
               "--primary-skill-revision", "1.5.0", "--release-values", unfilled])
    inj["unfilled_marker_refused_by_regenerator"] = c != 0 and "unfilled markers" in o
    doc = json.loads(rv.read_text(encoding="utf-8"))
    doc["ops"].append(["set", ["x"], "@UNKNOWN_MARKER"])
    (W / "rv-extra.json").write_text(json.dumps(doc), encoding="utf-8")
    c2, o2 = go([__file__, "fill", W / "rv-extra.json", cand_md, plan_file, W / "y2.json", "--map", map_path] + si)
    inj["fill_refuses_unknown_marker"] = c2 != 0 and "unfilled markers" in o2
    doc = json.loads(rv.read_text(encoding="utf-8"))
    for op in doc["ops"]:
        if op[1] == ["candidate_prompt_ids"]:
            op[2] = op[2][:-1]
    (W / "rv-55.json").write_text(json.dumps(doc), encoding="utf-8")
    c3, o3 = go([__file__, "fill", W / "rv-55.json", cand_md, plan_file, W / "y3.json", "--map", map_path] + si)
    inj["fill_refuses_55_member_ids"] = c3 != 0 and "candidate_prompt_ids" in o3
    c, o = go([recipe, cand_md, R / TEMPLATE, oracle, R / DECISIONS, W / "x.json", "--contract-revision", "4.3.0",
               "--primary-skill-revision", "1.5.0", "--release-values", R / PRED_VALUES])
    inj["predecessor_release_values_refused"] = c != 0 and "names another release" in o
    c, o = go([recipe, cand_md, R / TEMPLATE, S / "flowmaster-validate" / ORACLE_0923, R / DECISIONS, W / "x.json",
               "--contract-revision", "4.3.0", "--primary-skill-revision", "1.5.0", "--release-values", filled])
    inj["oracle_not_pinned_by_graph_refused"] = c != 0 and "oracle digest" in o
    g = Path(cand_md).read_text(encoding="utf-8").replace(NEW_ORACLE_SHA, "0" * 64)
    (W / "bad-pin.md").write_text(g, encoding="utf-8")
    c, o = go([recipe, W / "bad-pin.md", R / TEMPLATE, oracle, R / DECISIONS, W / "x.json", "--contract-revision",
               "4.3.0", "--primary-skill-revision", "1.5.0", "--release-values", filled])
    inj["unknown_graph_pin_refused"] = c != 0 and "graph G16 not applied" in o
    c, o = go([S / "glow-graph-contract/scripts/contract_recipe.py", cand_md, R / TEMPLATE, oracle, R / DECISIONS,
               W / "x.json", "--contract-revision", "4.3.0", "--primary-skill-revision", "1.5.0", "--release-values",
               filled])
    inj["unpatched_regenerator_refuses_102726"] = c != 0
    # C-19 injections: the exception admits CL-05's two parent paths only, and requires them
    fdoc = json.loads(filled.read_text(encoding="utf-8")) if filled.exists() else {"ops": []}

    def regen_with(mutate, name):
        d = copy.deepcopy(fdoc)
        mutate(d)
        (W / name).write_text(json.dumps(d), encoding="utf-8")
        return go([recipe, cand_md, R / TEMPLATE, oracle, R / DECISIONS, W / "x.json", "--contract-revision", "4.3.0",
                   "--primary-skill-revision", "1.5.0", "--release-values", W / name])
    c, o = regen_with(lambda d: d["ops"].append(["set", ["member_registry", "QA-10", "staged_parent_id"], "0" * 32]),
                      "rv-other-parent.json")
    inj["c19_other_member_parent_refused"] = c != 0 and "mirrored path" in o
    c, o = regen_with(lambda d: d["ops"].append(["set", ["member_registry", "CL-05", "title"], "x"]), "rv-cl05-title.json")
    inj["c19_other_cl05_field_refused"] = c != 0 and "mirrored path" in o
    c, o = regen_with(lambda d: d.__setitem__("ops", [op for op in d["ops"] if op[1][:2] not in
                                                      (["member_registry", "CL-05"], ["notion_page_manifest", "CL-05"])]),
                      "rv-no-cl05-parent.json")
    inj["c19_cl05_without_parent_refused"] = c != 0 and "has no staged parent" in o
    c, o = regen_with(lambda d: [op.__setitem__(2, "0" * 32) for op in d["ops"] if op[1] == ["notion_page_manifest", "CL-05", "parent_id"]],
                      "rv-cl05-parent-split.json")
    inj["c19_manifest_parent_mismatch_refused"] = c != 0 and "manifest parent differs" in o
    m = json.loads(Path(map_path).read_text(encoding="utf-8"))
    m["members"]["CL-05"]["parent_id"] = None
    (W / "map-no-cl05-parent.json").write_text(json.dumps(m), encoding="utf-8")
    c, o = go([__file__, "fill", rv, cand_md, plan_file, W / "y4.json", "--map", W / "map-no-cl05-parent.json"] + si)
    inj["c19_fill_refuses_map_without_cl05_parent"] = c != 0 and "PARENT_ID_FORM:CL-05" in o
    c, o = go([__file__, "fill", rv, cand_md, plan_file, W / "y5.json"] + si)
    inj["c19_fill_refuses_without_map"] = c != 0 and "--map is required" in o
    rec["injected_refusals"] = inj
    rec["patched_regenerator_sha256"] = sha((ggc / "scripts/regenerate_contract.py").read_bytes())
    rec["ok"] = (rec["patch"].get("patch_ok") is True and rec["patch_second_application_refused"]
                 and rec["patch_reapply_in_place_refused"] and rec["Q1"]["Q1_PASS"] and code_f == 0
                 and all(checks.values()) and all(inj.values()))
    print(json.dumps(rec, indent=1))
    return 0 if rec["ok"] else 1


COMMANDS = {"values": values, "fill": fill, "patch-ggc": patch_ggc, "run": run}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        sys.exit(__doc__)
    sys.exit(COMMANDS[sys.argv[1]](*sys.argv[2:]))
