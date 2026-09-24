#!/usr/bin/env python3
"""EXECUTE suite gate for MODIFICATION-20260923-closeout-residuals (PLAN decisions P-56 and P-60).

Every expected exit code and key result is embedded below; the gate exits 0 only when every row is ok.

    --set pre    Once, at X1.3 before the reindex, on the working tree. The new builder must refuse today's
                 docs/graph/parts with exactly the 7 bookkeeping errors, and the parts must be today's
                 (freeze 56 980af73e...). Needs --pkg-root.
    --set pkg    At X4.2: after commit 1, the reindex, the contract-template move and registry.diff. Every suite
                 of EV/skills/results/suites_final.json, re-expressed on --pkg-root, --cand and the repository's
                 own (now reindexed) docs/graph/parts: the build must exit 0 with the proof token ae2bd159...;
                 the pre-reindex build is re-run on the parts at --pre-rev read from git (not the working tree);
                 registry_deriver runs with the patched audit (1.13.0) and with --inst's installed audit
                 (1.12.0). Needs --pkg-root. The pkg-root must first give freeze 323 047ca742...
    --set post   At X7.4: the same as pkg on --inst (then the installed patched tree) and main's reindexed parts,
                 without the pre-reindex rows and the 1.12.0-audit rows.

The first rows are preconditions (freeze recipe hash, whole-root freeze, seven package freezes); when one
fails, the remaining rows are not run and the gate fails. The last row re-takes the whole-root freeze, so a
suite that wrote into the skill tree fails the gate.

The gate writes only under --out (logs, build outputs, a copy of the parts for the idempotence check, the
extracted pre-reindex parts) and under --cand when it builds the candidate root. It never writes the
repository or a skill tree: it refuses an --out or --cand inside either. Children run with
PYTHONDONTWRITEBYTECODE=1, and with TMPDIR=<out>/tmp when TMPDIR is unset.

usage: PYTHONDONTWRITEBYTECODE=1 TMPDIR=<scratch>/tmp python3 run_gate.py --set pre|pkg|post --out <scratch-dir>
       [--repo <repo>] [--pkg-root <patched full skills root>] [--inst <installed skills root>] [--cand <dir>]
       [--pre-rev <commit>]
exit 0 every row ok; 1 any row not ok; 2 unusable arguments.
"""
import argparse
import hashlib
import io
import json
import os
import shutil
import subprocess
import sys
import tarfile
from pathlib import Path

sys.dont_write_bytecode = True

INST_DEFAULT = "/root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502"
# A commit on main whose docs/graph/parts are the pre-reindex parts (freeze 56 980af73e...): origin/main at PLAN
# time (#477). The parts last changed on main at d848942 (#474). PLAN's own HEAD 705568e is not used: it is not an
# ancestor of main, and a squash merge of the record PR would leave it unreachable.
PRE_REV_DEFAULT = "77d98ddf2bab9e37bd09fdf8f894e166ca23788e"

FREEZE_RECIPE = "docs/prompt_ecosystem_management/freeze.py"
FREEZE_RECIPE_SHA256 = "3d6a38f3544868cbaa8118b60c381789625ab3c4095e863d96260caba4bbe2c9"
ROOT_FREEZE = "323 047ca74293082dd1d824c1e74f2aef17945bea1f609f365afcc31106b4de00ae"  # manifest final_root_freeze
PACKAGE_FREEZE = {  # manifest execute.1.expected_after_patch
    "flowmaster-validate": "31 0ca2a74d50a57803e2c4b8426a84f43877f68f6d1c93731d54368f413e5c5626",
    "change-flow": "22 9a551af36e042e56a48045297ac316b4102a4eb21f31622853c8be700e223f47",
    "glow-graph-contract": "9 e241bb9a67c4470895fc666a25d0f97d8df7e8e2df06539de5deaf12bc46467c",
    "session-relay-flowmaster": "5 c8a5b22432a44f57fb12bc508169f85aa3d0ca3298b793590c364eb9a2afc8e4",
    "glow-hde-pr-development": "4 265f9170d8459fc477287c320f0bbdd8eaaf0e6ba1dd4ee513275a76a22f8f7a",
    "amthor-workspace-governance-audit": "15 c214e8741e9c54d395cfbd1379cbc7947e6c07beee5bd03aca433dc5dda937ab",
    "glow-po-reporting": "1 7e04368a63e40c99e31ede3eda9ba88cfbbb9915a48b46cdc39027da7cef68e1",
}
INSTALLED_AUDIT_1_12_0_FREEZE = "15 819915e4a57184fd3af0c783f13e102892eb7182d0c951727869655d11ae078d"  # execute.1
PARTS_FREEZE_PRE = "56 980af73e656e20740663ae1dbfa8780eff61b41e2f754c5719c743e4647cae50"
PARTS_FREEZE_REINDEXED = "56 84dbb1fe5e7566b871ddc436bcbc875a772dcc695be221d2b4d45a18a470027f"
CONTRACT_SHA256 = "dbae180bb5c2f73e3f27a46601bfb5cbe7321e5431dbaba8763b1a576cd9343c"  # 4.1.1
GRAPH_SHA256 = "ae2bd159f0ba947c2e470f96579fadfbf060f74423aa974ae1194ac16bb2484d"  # the graph proof token
GRAPH_MD_SHA256, GRAPH_MD_BYTES = "a70a93263f2943be45450a210f62a82a2a27abfd49a259d04f838e469ba0cc24", 575672
BUILD_LINES = ["build: 55 nodes, 229 edges, 55 state_routes",
               f"       embedded JSON 575074 bytes  sha256 {GRAPH_SHA256}"]
PRE_REINDEX_ERRORS = [  # suites_final.json graph_parts.build.today_parts (stderr, in order)
    "VALIDATION FAILED:",
    "  global.json: 13 _other_edge_indices for 3 _other_edges",
    "  prompts/CF-C-10: 4 edge_indices for 5 edges",
    "  prompts/ESC-40: 3 edge_indices for 5 edges",
    "  prompts/PR-35: 4 edge_indices for 5 edges",
    "  prompts/QA-70: 5 edge_indices for 4 edges",
    "  prompts/RS-40: 5 edge_indices for 6 edges",
    "  edge indices are not exactly 0..228, each once (235 indices for 229 edges)",
    "  run `graph_parts.py reindex <parts-dir>` to re-derive them from the assembled order",
]
C091 = "references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json"
CALIAS = "references/gcfpe-current-direct-handoff-contract.json"
CAND_SOURCE = "references/gcfpe-20260914.1-091426.1-candidate-graph-contract.json"  # in change-flow (and flowmaster-validate)
CAND_GRAPH = "graph/GCFPE-20260914.1-Candidate-Graph-Contract.json"  # profile frozen_graph.relative_to_candidate_root
ITEM11_CASES = ["historical-alias-bodies-stdin-supplied-body-named-result",
                "historical-alias-bodies-stdin-absent-body-not-evaluated"]
REGISTRY = "docs/prompt_ecosystem_management/project-prompt-contract-registry.md"
AUDIT = "amthor-workspace-governance-audit"
AUDIT_MARKER = "**WORKSPACE_GOVERNANCE_AUDITOR_REVISION:** "
MARKER_FILE = ".run_gate"

PY = sys.executable
ROWS = []


def sha256_file(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def find_repo(start):
    for d in [start, *start.parents]:
        if (d / ".git").exists() and (d / "docs/graph/parts").is_dir():
            return d
    return None


def inside(path, root):
    try:
        Path(path).resolve().relative_to(Path(root).resolve())
        return True
    except ValueError:
        return False


class Gate:
    def __init__(self, args, env, logdir):
        self.args, self.env, self.logdir = args, env, logdir

    def record(self, name, cmd, cwd, exit_code, expected_exit, expected, observed):
        mismatches = [k for k in expected if observed.get(k) != expected[k]]
        if exit_code != expected_exit:
            mismatches.insert(0, "exit")
        row = {"name": name, "cmd": cmd, "cwd": cwd, "exit": exit_code, "expected_exit": expected_exit,
               "expected": expected, "observed": observed, "mismatches": mismatches, "ok": not mismatches}
        ROWS.append(row)
        print(f"[{'ok ' if row['ok'] else 'NOT'}] {name}: exit {exit_code}/{expected_exit}"
              + (f"; mismatches {mismatches}" if mismatches else ""), file=sys.stderr)
        return row["ok"]

    def run(self, name, cmd, expected_exit, expected, summarise, cwd=None):
        cmd = [str(c) for c in cmd]
        r = subprocess.run(cmd, capture_output=True, text=True, env=self.env, cwd=cwd)
        (self.logdir / f"{name}.out").write_text(
            r.stdout + ("\n--- stderr ---\n" + r.stderr if r.stderr else ""), encoding="utf-8")
        try:
            observed = summarise(r.stdout, r.stderr)
        except Exception as exc:  # an unreadable output is a failed row, never a silent pass
            observed = {"summary_error": f"{type(exc).__name__}: {exc}"}
        return self.record(name, cmd, str(cwd) if cwd else None, r.returncode, expected_exit, expected, observed)

    def freeze(self, name, tree, expected):
        recipe = self.args.repo / FREEZE_RECIPE
        return self.run(name, [PY, recipe, tree], 0, {"stdout": expected},
                        lambda o, e: {"stdout": o.strip(), "stderr": e.strip()})


# ---------- summarisers ----------

def lines(o, e):
    return {"stdout_lines": o.rstrip("\n").split("\n") if o else [], "stderr_lines": e.rstrip("\n").split("\n") if e else []}


def suite_sum(o, e):
    d = json.loads(o)
    cov = d.get("change_contract_coverage") or {}
    cand = cov.get("gcfpe_20260914_candidate") or {}
    cfix = cov.get("gcfpe_20260914_candidate_fixtures") or {}
    cur = cov.get("gcfpe_current_direct_handoff") or {}
    cfix_cases = cfix.get("cases") or []
    return {"verdict": d["verdict"], "suite_ok": d.get("suite_ok"), "findings": len(d["findings"]),
            "warnings": len(d.get("warnings", [])), "advisories": len(d.get("advisories", [])),
            "finding_rules": sorted({f["rule_id"] for f in d["findings"]}),
            "validator_revision": d.get("validator_revision"),
            "current.ok": cur.get("ok"), "current.contract_sha256": cur.get("contract_sha256"),
            "current.frozen_graph_sha256": cur.get("frozen_graph_sha256"),
            "candidate.status": cand.get("status"), "candidate.ok": cand.get("ok"),
            "candidate.errors": cand.get("errors"), "candidate.contract_sha256": cand.get("contract_sha256"),
            "candidate.frozen_graph_sha256": cand.get("frozen_graph_sha256"),
            "candidate_fixtures.status": cfix.get("status"),
            "candidate_fixtures.cases_passed": (f"{sum(1 for c in cfix_cases if c.get('passed'))}/{len(cfix_cases)}"
                                                if cfix_cases else None)}


def fixtures_sum(o, e):
    d = json.loads(o)
    cases = d.get("cases") or d.get("results") or []
    ok = lambda c: c.get("passed", c.get("expectation_met"))  # noqa: E731
    keys = ("case_count", "total", "fixture_suite_ok", "validator_revision", "section_13_passed",
            "section_13_fixture_count", "passed_expectations", "failed_expectations", "receiver_case_count")
    s = {k: d[k] for k in keys if k in d}
    s["cases_passed"] = f"{sum(1 for c in cases if ok(c))}/{len(cases)}"
    s["not_passed"] = [c.get("name") or c.get("id") for c in cases if not ok(c)]
    by_name = {c.get("name"): c for c in cases}
    s["item11_cases"] = {n: (bool(ok(by_name[n])) if n in by_name else "ABSENT") for n in ITEM11_CASES}
    return s


def direct_sum(o, e):
    d = json.loads(o)
    return {k: d.get(k) for k in ("ok", "errors", "contract_sha256", "frozen_graph_sha256", "frozen_graph_edge_count",
                                  "prompt_body_checks_not_evaluated", "candidate_root")}


def relay_sum(o, e):
    d = json.loads(o[: o.rindex("}") + 1])
    return {"status": d["status"], "cases": len(d["cases"]), "not_ok": [c["name"] for c in d["cases"] if not c["ok"]]}


def last_line(o, e):
    return {"last_line": (o + e).strip().split("\n")[-1]}


def deriver_sum(o, e):
    d = json.loads(o)
    return {k: v for k, v in d.items() if k != "derived"}


# ---------- the sets ----------

def preconditions(g, tree):
    recipe = g.args.repo / FREEZE_RECIPE
    ok = g.record("freeze_recipe.sha256", ["sha256", str(recipe)], None, 0, 0,
                  {"sha256": FREEZE_RECIPE_SHA256}, {"sha256": sha256_file(recipe) if recipe.is_file() else None})
    if not ok:
        return False
    ok = g.freeze("freeze.skills_root", tree, ROOT_FREEZE) and ok
    for skill, digest in PACKAGE_FREEZE.items():
        ok = g.freeze(f"freeze.{skill}", tree / skill, digest) and ok
    return ok


def build_cand(g, tree):
    """Build the candidate root from the tree's change-flow if missing; verify it either way."""
    cand, src = g.args.cand, tree / "change-flow" / CAND_SOURCE
    bundled = tree / "flowmaster-validate" / CAND_SOURCE
    target = cand / CAND_GRAPH
    built, error = False, None
    if not cand.exists():
        try:
            target.parent.mkdir(parents=True)
            shutil.copyfile(src, target)
            built = True
        except OSError as exc:  # recorded as a failed row, never raised past the gate
            error = f"{type(exc).__name__}: {exc}"
    same = lambda a, b: a.is_file() and b.is_file() and a.read_bytes() == b.read_bytes()  # noqa: E731
    observed = {"built_now": built, "error": error,
                "files": sorted(p.relative_to(cand).as_posix() for p in cand.rglob("*") if p.is_file()),
                "graph_sha256": sha256_file(target) if target.is_file() else None,
                "equals_flowmaster_validate_bundled_graph": same(target, bundled),
                "equals_change_flow_candidate_graph": same(target, src)}
    return g.record("candidate_root", [f"(internal) if missing: mkdir -p {target.parent} && cp {src} {target}; "
                                       f"then sha256 and byte-compare with {bundled}"], None, 0, 0,
                    {"error": None, "files": [CAND_GRAPH], "graph_sha256": GRAPH_SHA256,
                     "equals_flowmaster_validate_bundled_graph": True, "equals_change_flow_candidate_graph": True},
                    observed)


def skill_suites(g, tree):
    fv, cf = tree / "flowmaster-validate", tree / "change-flow"
    vf = [PY, fv / "scripts/validate_flowmaster.py", "--skills-root", tree, "--strict-warnings"]
    common = {"verdict": "FLOWMASTER_SUITE_PASS", "suite_ok": True, "findings": 0, "warnings": 0, "advisories": 0,
              "finding_rules": [], "validator_revision": "3.3.1", "current.ok": True,
              "current.contract_sha256": CONTRACT_SHA256, "current.frozen_graph_sha256": GRAPH_SHA256}
    g.run("validate_flowmaster.default", vf, 0,
          {**common, "candidate.status": "NOT_REQUESTED", "candidate_fixtures.status": "NOT_REQUESTED"}, suite_sum)
    g.run("validate_flowmaster.candidate", vf + ["--gcfpe-contract", cf / C091, "--gcfpe-candidate-root", g.args.cand], 0,
          {**common, "candidate.ok": True, "candidate.errors": [], "candidate.contract_sha256": CONTRACT_SHA256,
           "candidate.frozen_graph_sha256": GRAPH_SHA256, "candidate_fixtures.cases_passed": "236/236"}, suite_sum)
    g.run("run_change_flow_fixtures", [PY, fv / "scripts/run_change_flow_fixtures.py"], 0,
          {"total": 32, "fixture_suite_ok": True, "passed_expectations": 32, "failed_expectations": 0,
           "cases_passed": "32/32", "not_passed": []}, fixtures_sum)
    fx236 = {"case_count": 236, "fixture_suite_ok": True, "validator_revision": "3.3.1", "section_13_passed": 37,
             "section_13_fixture_count": 37, "cases_passed": "236/236", "not_passed": []}
    g.run("run_gcfpe_current_fixtures.default", [PY, fv / "scripts/run_gcfpe_current_fixtures.py", cf], 0, fx236,
          fixtures_sum)
    # The historical schema-3.1 alias run is the one that executes ITEM-11's two --bodies-stdin cases.
    g.run("run_gcfpe_current_fixtures.historical_alias",
          [PY, fv / "scripts/run_gcfpe_current_fixtures.py", cf, "--contract", cf / CALIAS], 0,
          {"case_count": 84, "fixture_suite_ok": True, "receiver_case_count": 40, "cases_passed": "84/84",
           "not_passed": [], "item11_cases": {n: True for n in ITEM11_CASES}}, fixtures_sum)
    g.run("run_gcfpe_20260914_fixtures",
          [PY, fv / "scripts/run_gcfpe_20260914_fixtures.py", cf, "--contract", cf / C091], 0, fx236, fixtures_sum)
    direct = {"ok": True, "errors": [], "contract_sha256": CONTRACT_SHA256, "frozen_graph_sha256": GRAPH_SHA256,
              "frozen_graph_edge_count": 229, "prompt_body_checks_not_evaluated": ["ALL_BODY_LEVEL_CHECKS"],
              "candidate_root": None}
    g.run("validate_gcfpe_20260914.candidate_root",
          [PY, fv / "scripts/validate_gcfpe_20260914.py", cf, "--contract", cf / C091, "--candidate-root", g.args.cand],
          0, direct, direct_sum)
    g.run("validate_gcfpe_20260914.no_root", [PY, fv / "scripts/validate_gcfpe_20260914.py", cf, "--contract", cf / C091],
          0, direct, direct_sum)
    g.run("validate_gcfpe_current", [PY, fv / "scripts/validate_gcfpe_current.py", cf], 0, direct, direct_sum)
    g.run("change_flow_own_validator", [PY, cf / "scripts/validate_gcfpe_20260914.py"], 0,
          {"last_line": "PASS: change-flow GCFPE-20260914.1 contract and Markdown-only source policy"}, last_line,
          cwd=cf)
    g.run("relay_self_test", [PY, tree / "session-relay-flowmaster/scripts/validate_relay_manifest.py", "--self-test"], 0,
          {"status": "PASS", "cases": 232, "not_ok": []}, relay_sum)
    g.run("pr_skill_validator", [PY, tree / "glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py"], 0,
          {"last_line": "PASS: Glow HDE PR development skill structural contract"}, last_line)
    g.run("governance_audit_run_fixture_suite", [PY, "run_fixture_suite.py"], 0, {"last_line": "OK"}, last_line,
          cwd=tree / AUDIT / "scripts")


def pre_reindex_build(g, tree, parts, name, out_md):
    gp = tree / "glow-graph-contract/scripts/graph_parts.py"
    return g.run(name, [PY, gp, "build", parts, out_md], 1,
                 {"stdout_lines": [], "stderr_lines": PRE_REINDEX_ERRORS, "output_written": False},
                 lambda o, e: {**lines(o, e), "output_written": Path(out_md).exists()})


def reindexed_build(g, tree, parts, out_md):
    gp = tree / "glow-graph-contract/scripts/graph_parts.py"

    def summarise(o, e):
        s = lines(o, e)
        s["validation_pass_line"] = bool(s["stdout_lines"]) and s["stdout_lines"][-1].startswith("       validation PASS -> ")
        s["stdout_lines"] = s["stdout_lines"][:-1]  # the PASS line carries the output path, checked above
        s["graph_md_sha256"] = sha256_file(out_md) if Path(out_md).is_file() else None
        s["graph_md_bytes"] = Path(out_md).stat().st_size if Path(out_md).is_file() else None
        return s

    return g.run("graph_parts.build.repo_parts", [PY, gp, "build", parts, out_md], 0,
                 {"stdout_lines": BUILD_LINES, "stderr_lines": [], "validation_pass_line": True,
                  "graph_md_sha256": GRAPH_MD_SHA256, "graph_md_bytes": GRAPH_MD_BYTES}, summarise)


def reindex_idempotent(g, tree, parts, work):
    copy = work / "parts-copy"
    shutil.copytree(parts, copy)
    gp = tree / "glow-graph-contract/scripts/graph_parts.py"
    return g.run("graph_parts.reindex.copy_idempotent", [PY, gp, "reindex", copy], 0,
                 {"stdout_lines": ["reindex: 229 edges; 0 file(s) rewritten"], "stderr_lines": []}, lines)


def extract_pre_parts(g, work):
    """The parts at --pre-rev, read from git into the scratch work dir (read-only on the repository)."""
    dest = work / "pre-reindex"
    cmd = ["git", "-C", str(g.args.repo), "archive", "--format=tar", g.args.pre_rev, "docs/graph/parts"]
    r = subprocess.run(cmd, capture_output=True)
    if r.returncode == 0:
        with tarfile.open(fileobj=io.BytesIO(r.stdout)) as t:
            if hasattr(tarfile, "data_filter"):
                t.extractall(dest, filter="data")
            else:  # pragma: no cover - older Python without extraction filters
                t.extractall(dest)
    g.record("parts_pre_reindex.git_archive", cmd, None, r.returncode, 0, {},
             {"stderr": r.stderr.decode("utf-8", "replace").strip()})
    return dest / "docs/graph/parts", r.returncode == 0


def deriver(g, tree, audit_dir, parts, name, revision, audit_freeze=None):
    rd = tree / "glow-graph-contract/scripts/registry_deriver.py"
    reg = g.args.repo / REGISTRY
    try:
        skill_md = (audit_dir / "SKILL.md").read_text(encoding="utf-8")
    except OSError:
        skill_md = ""
    rev = next((l.split(AUDIT_MARKER, 1)[1].strip() for l in skill_md.split("\n") if AUDIT_MARKER in l), None)
    extra = {"audit_revision": rev, "registry_sha256": sha256_file(reg) if reg.is_file() else None}
    if audit_freeze is not None:
        r = subprocess.run([PY, str(g.args.repo / FREEZE_RECIPE), str(audit_dir)], capture_output=True, text=True,
                           env=g.env)
        extra["audit_freeze"] = r.stdout.strip()
    expected = {"rows": 55, "parts": 55, "drift": [], "rows_without_part": [], "audit_revision": revision}
    if audit_freeze is not None:
        expected["audit_freeze"] = audit_freeze
    return g.run(name, [PY, rd, audit_dir, reg, parts, "--derive"], 0, expected,
                 lambda o, e: {**deriver_sum(o, e), **extra})


def main():
    ap = argparse.ArgumentParser(prog="run_gate.py", description=__doc__.split("\n\n")[0])
    ap.add_argument("--set", required=True, choices=("pre", "pkg", "post"), dest="set_")
    ap.add_argument("--repo", type=Path)
    ap.add_argument("--pkg-root", type=Path)
    ap.add_argument("--inst", type=Path, default=Path(INST_DEFAULT))
    ap.add_argument("--cand", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--pre-rev", default=PRE_REV_DEFAULT)
    args = ap.parse_args()

    def usage(msg):
        print(json.dumps({"set": args.set_, "usage_error": msg}))
        return 2

    args.repo = (args.repo or find_repo(Path(__file__).resolve().parent) or Path("/nonexistent")).resolve()
    if not (args.repo / "docs/graph/parts").is_dir() or not (args.repo / ".git").exists():
        return usage(f"no repository with docs/graph/parts at {args.repo}")
    if args.set_ in ("pre", "pkg") and not args.pkg_root:
        return usage("--pkg-root is required for --set pre and --set pkg")
    tree = (args.pkg_root if args.set_ in ("pre", "pkg") else args.inst).resolve()
    args.inst = args.inst.resolve()
    if not tree.is_dir():
        return usage(f"no skills tree at {tree}")
    args.out = args.out.resolve()
    args.cand = (args.cand or args.out / "cand").resolve()
    guarded = [args.repo, tree, args.inst]
    for label, p in (("--out", args.out), ("--cand", args.cand)):
        if any(inside(p, root) or inside(root, p) for root in guarded):
            return usage(f"{label} {p} overlaps the repository or a skill tree")

    work = args.out / args.set_
    if work.exists():
        if not (work / MARKER_FILE).is_file():
            return usage(f"{work} exists and was not made by this gate; refusing to clear it")
        shutil.rmtree(work)
    (work / "logs").mkdir(parents=True)
    (work / MARKER_FILE).write_text("run_gate.py work directory\n", encoding="utf-8")
    env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
    if not env.get("TMPDIR"):
        (args.out / "tmp").mkdir(parents=True, exist_ok=True)
        env["TMPDIR"] = str(args.out / "tmp")
    g = Gate(args, env, work / "logs")
    parts = args.repo / "docs/graph/parts"

    not_run = []
    if preconditions(g, tree):
        if args.set_ == "pre":
            g.freeze("parts.freeze", parts, PARTS_FREEZE_PRE)
            pre_reindex_build(g, tree, parts, "graph_parts.build.pre_reindex_working_tree", work / "g-before.md")
        else:
            if build_cand(g, tree):
                skill_suites(g, tree)
            else:
                not_run.append("the 13 skill suites (candidate root not usable)")
            g.freeze("parts.freeze", parts, PARTS_FREEZE_REINDEXED)
            reindexed_build(g, tree, parts, work / "graph.md")
            reindex_idempotent(g, tree, parts, work)
            deriver(g, tree, tree / AUDIT, parts, "registry_deriver.patched_audit.repo_parts", "1.13.0")
            if args.set_ == "pkg":
                pre_parts, extracted = extract_pre_parts(g, work)
                if extracted and g.freeze("parts_pre_reindex.freeze", pre_parts, PARTS_FREEZE_PRE):
                    pre_reindex_build(g, tree, pre_parts, "graph_parts.build.pre_reindex_parts", work / "g-before.md")
                    deriver(g, tree, tree / AUDIT, pre_parts, "registry_deriver.patched_audit.pre_reindex_parts", "1.13.0")
                else:
                    not_run.append("pre-reindex rows (the parts at --pre-rev are unavailable or not today's)")
                inst_audit = args.inst / AUDIT
                deriver(g, tree, inst_audit, parts, "registry_deriver.installed_audit_1.12.0.repo_parts", "1.12.0",
                        INSTALLED_AUDIT_1_12_0_FREEZE)
                if extracted and (pre_parts / "prompts").is_dir():
                    deriver(g, tree, inst_audit, pre_parts, "registry_deriver.installed_audit_1.12.0.pre_reindex_parts",
                            "1.12.0", INSTALLED_AUDIT_1_12_0_FREEZE)
        g.freeze("freeze.skills_root.after", tree, ROOT_FREEZE)
    else:
        not_run.append("every row after the preconditions")

    ok = all(r["ok"] for r in ROWS) and not not_run
    summary = {"gate": "MODIFICATION-20260923-closeout-residuals run_gate.py", "set": args.set_,
               "repo": str(args.repo), "tree": str(tree), "inst": str(args.inst), "cand": str(args.cand),
               "out": str(work), "pre_rev": args.pre_rev if args.set_ == "pkg" else None,
               "rows_total": len(ROWS), "rows_ok": sum(1 for r in ROWS if r["ok"]),
               "rows_not_ok": [r["name"] for r in ROWS if not r["ok"]], "not_run": not_run, "ok": ok,
               "rows": ROWS}
    text = json.dumps(summary, indent=1, ensure_ascii=False) + "\n"
    (args.out / f"gate_{args.set_}.json").write_text(text, encoding="utf-8")
    sys.stdout.write(text)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
