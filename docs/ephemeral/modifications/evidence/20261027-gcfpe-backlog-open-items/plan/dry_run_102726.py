#!/usr/bin/env python3
"""PLAN dry run (D26-A step 1) for MODIFICATION-20261027-gcfpe-backlog-open-items (PLAN assembly A5).

Adapted from docs/ephemeral/modifications/evidence/20261011-gcfpe-mb008-to-promotion/plan/dry_run.py. It runs the A1 to
A4 tools of this plan, in order, on scratch copies, and records every gate's own top-level flags by name. It never
writes to Notion, an installed skill directory, docs/graph/parts, the selected registry, docs/pfcanon or a prompt body.
Prompt bodies are D22 transient reads of this session's own harness records (body_check.py's reader, subagents
included); bodies travel between processes only on a pipe, never in a file; the receipt carries counts, ids and
booleans only.

    PYTHONDONTWRITEBYTECODE=1 CLAUDE_CODE_SESSION_ID=<session> python3 dry_run_102726.py run \\
        <installed-skills-root> <scratch> <fetched-after> [--map <successor map>] [--receipt <dry-run.json>]
    PYTHONDONTWRITEBYTECODE=1 python3 dry_run_102726.py selftest <scratch>

<fetched-after> is an ISO UTC time (with milliseconds) taken just before this session fetched every page in
edits.json and the eleven control pages. --map defaults to plan/successor-map-standin.json; with a stand-in map
(stand_in: true) every receipt says so and names each stand-in. EXECUTE's real map is
execute/successor-pages-102726.1.json; the tools refuse a stand-in map where the precedent refused one.

Gates: N0 identities, N1 guard/resolver/map self-tests, N2 body rehearsal on the fresh reads, N3 registry form vs
the shipped audit engine, N4 graph builds, N5 R1 successor, contracts and regenerator proof, N6 the 102726.1 profile,
N8 the four packages and their own gates (run before N7, which needs the built trees), N7 all 56 bodies through the
built 102726.1 profile with the edits applied in memory, N9 the registry with every row's assertions run on the
edited bodies, N10 activation render and control check. `selftest` shows that each check this file adds (beyond the
tools it calls) fails on an injected defect.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[5]
EVID = HERE.parent
SESSION = os.environ.get("CLAUDE_CODE_SESSION_ID", "")
PY = sys.executable
FREEZE = REPO / "docs/prompt_ecosystem_management/freeze.py"
SURFACES = REPO / "docs/prompt_ecosystem_management/authoritative-surfaces.md"
DECISIONS = REPO / "docs/prompt_ecosystem_management/gcfpe.decision-record.md"
W7 = HERE / "work/W7.json"
TSV = HERE / "members-100926.1.tsv"
CONTROLS = ["3d24590a05eb81ce942ad994cfca9fa1", "3db4590a05eb81de9736ea69bac61016", "3db4590a05eb81d59059eb6b95ed5fcf",
            "3db4590a05eb8195a2ccf7c0959a8b6e", "3db4590a05eb814d96d3dcfa8835f96d", "3db4590a05eb81cd938de84cfffead9c",
            "3db4590a05eb811b9c14f2ae89c28df7", "3db4590a05eb812f87caed515836687f"]   # as A4's receipt script
CF_REL = "references/gcfpe-20261027.1-102726.1-direct-handoff-contract.json"


# ------------------------------------------------------------------------------------------------- helpers
def run(args, cwd=None, inp=None, env_extra=None, timeout=3600):
    env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1", **(env_extra or {})}
    r = subprocess.run([str(a) for a in args], cwd=cwd, input=inp, capture_output=True, text=True, env=env, timeout=timeout)
    return r.returncode, r.stdout, r.stderr


def js(text: str):
    text = (text or "").strip()
    if not text:
        return None
    try:
        return json.loads(text)
    except ValueError:
        pass
    for line in reversed(text.splitlines()):  # some tools print progress lines before one JSON line
        try:
            return json.loads(line)
        except ValueError:
            continue
    i = text.find("{")
    try:
        return json.loads(text[i:]) if i >= 0 else None
    except ValueError:
        return None


def jrun(args, **kw):
    c, o, e = run(args, **kw)
    return c, (js(o) or {"_unparsed_tail": (o + e)[-400:]})


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def freeze(p: Path) -> str:
    return run([PY, FREEZE, p])[1].strip().splitlines()[-1]


def expected_digests() -> dict:
    """The nine installed skills W7 lists, with the digests W7 measured (tooling.packages_*), read from W7.json."""
    t = json.loads(W7.read_text(encoding="utf-8"))["tooling"]
    out = {r["package"]: r["freeze_digest_before"] for r in t["packages_that_change"]}
    out.update({r["package"]: r["digest"] for r in t["packages_unchanged"]})
    return out


def d29_token() -> dict:
    """D29's graph proof token as authoritative-surfaces.md records it (the sha256 is recorded as a prefix)."""
    line = next(l for l in SURFACES.read_text(encoding="utf-8").splitlines() if l.startswith("| Graph proof token"))
    m = re.search(r"(\d+) nodes · (\d+) edges · (\d+) state_routes · ([\d,]+) bytes · sha256 ([0-9a-f]+)", line)
    return {"nodes": int(m.group(1)), "edges": int(m.group(2)), "state_routes": int(m.group(3)),
            "bytes": int(m.group(4).replace(",", "")), "sha256_prefix": m.group(5)}


def build_token(out: str) -> dict:
    m = re.search(r"build: (\d+) nodes, (\d+) edges, (\d+) state_routes", out)
    n = re.search(r"embedded JSON (\d+) bytes\s+sha256 ([0-9a-f]{64})", out)
    return {"nodes": int(m.group(1)) if m else None, "edges": int(m.group(2)) if m else None,
            "state_routes": int(m.group(3)) if m else None, "bytes": int(n.group(1)) if n else None,
            "sha256": n.group(2) if n else None, "validation_pass": "validation PASS" in out}


def token_matches(tok: dict, want: dict) -> bool:
    return (tok["nodes"], tok["edges"], tok["state_routes"], tok["bytes"]) == \
        (want["nodes"], want["edges"], want["state_routes"], want["bytes"]) and \
        bool(tok["sha256"]) and tok["sha256"].startswith(want["sha256_prefix"]) and tok["validation_pass"]


def body_classes(errors: list) -> list:
    return sorted({e.split(":")[0] for e in errors if e.startswith("PROMPT")})


def markdown_form(text: str) -> str:
    """DIAGNOSTIC ONLY, never a gate input: the fetched text with Notion's inline markup (<code>, <b>/<strong>,
    <i>/<em>, the escaped underscore) rewritten as Markdown, the rendering the 100926.1 registry's inherited
    assertions and the profile's backtick-only checks were written for."""
    text = re.sub(r"</?code>", "`", text)
    text = re.sub(r"</?(?:b|strong)>", "**", text)
    text = re.sub(r"</?(?:i|em)>", "*", text)
    return text.replace("\\_", "_")


def probe_contract(src: Path, dst: Path, standin_map: dict, probe_map: dict) -> int:
    """A scratch copy of the built contract whose member_registry page identities are the probe ids, so the
    probe-edited bodies are judged against the contract EXECUTE builds from the real map (no body text)."""
    c = json.loads(src.read_text(encoding="utf-8"))
    n = 0
    for pid, row in (c.get("member_registry") or {}).items():
        old_id = (standin_map["members"].get(pid) or {}).get("page_id")
        new_id = (probe_map["members"].get(pid) or {}).get("page_id")
        if not old_id or not new_id or old_id == new_id:
            continue
        row["notion_url"] = f"https://app.notion.com/p/{new_id}?pvs=204"
        row["notion_page_id"] = f"{new_id[:8]}-{new_id[8:12]}-{new_id[12:16]}-{new_id[16:20]}-{new_id[20:]}"
        n += 1
    dst.write_text(json.dumps(c, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return n


def without_matches(text: str, value: str) -> str:
    """The text with every line the pattern matches removed (the precedent registry_assemble.py's helper)."""
    for _ in range(400):
        m = re.search(value, text, flags=re.MULTILINE)
        if not m:
            return text
        s = text.rfind("\n", 0, m.start()) + 1
        e = text.find("\n", max(m.end() - 1, m.start()))
        e = len(text) if e < 0 else e + 1
        text = text[:s] + text[max(e, s + 1):]
    return text


def without_literal(text: str, lit: str) -> str:
    return "\n".join(l for l in text.split("\n") if lit not in l)


# the profile's body-scoped error families (prompt body checks and the QA closure body checks); every other error is
# a contract-level check, and under the probe contract only the three families its partial rebind disturbs may occur
BODY_SCOPED_PREFIXES = ("PROMPT_", "QA_")
PROBE_REBIND_CLASSES = {"GRAPH_NODE_CONTRACT", "MEMBER_BINDING", "PRODUCTION_CONTRACT_SEMANTIC_BUNDLE_MISMATCH"}
ASSERT_KINDS = ("required_literals", "forbidden_literals", "required_regex", "forbidden_regex")
INJECT_FORBIDDEN = [("SRC-001", "Prompt version:", "\nPrompt version: 102726.1\n"),
                    ("CTR-001", "CONTROL_NOTION", "\nCONTROL_NOTION\n")]


def row_assertions(A, row: dict, after: str) -> dict:
    """Every assertion on the row, run by the shipped engine on the edited body; each required assertion with its
    matches removed must be reported, and each release-wide forbidden assertion must be reported on a violating line."""
    aa = row.get("audit_assertions") or {}
    findings = A._evaluate_assertions(row, after, "transient")
    fired, missed = 0, []
    for kind in ("required_regex", "required_literals"):
        for raw in aa.get(kind) or []:
            broken = without_matches(after, raw["value"]) if kind == "required_regex" else \
                without_literal(after, raw if isinstance(raw, str) else raw.get("value", ""))
            if A._evaluate_assertions({"prompt_key": row["prompt_key"], "audit_assertions": {kind: [raw]}}, broken, "inject"):
                fired += 1
            else:
                missed.append(kind + ":" + str((raw.get("guard") if isinstance(raw, dict) else None) or "")[:30])
    for rule, needle, line in INJECT_FORBIDDEN:
        carried = [x for x in aa.get("forbidden_regex") or [] if x["rule_id"] == rule
                   and re.search(x["value"], needle, flags=re.MULTILINE)]
        if not carried:
            missed.append("NOT_CARRIED:" + rule)
            continue
        if A._evaluate_assertions({"prompt_key": row["prompt_key"], "audit_assertions": {"forbidden_regex": carried}},
                                  after + line, "inject"):
            fired += 1
        else:
            missed.append("FORBIDDEN_NOT_FIRED:" + rule)
    failing_ids = sorted({str(f.get("rule_id") or f.get("assertion") or "?") + ":" + str(f.get("guard") or "")
                          for f in findings})
    return {"assertions": sum(len(aa.get(k) or []) for k in ("required_literals", "forbidden_literals", "required_regex",
                                                            "forbidden_regex")),
            "findings_after": len(findings), "finding_ids": failing_ids[:12], "injected_fired": fired,
            "injected_missed": missed, "ok": not findings and not missed}


def load_engine(audit_root: Path):
    import importlib.util
    spec = importlib.util.spec_from_file_location("audit_engine_a5", audit_root / "scripts/audit_workspace_governance.py")
    mod = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(audit_root / "scripts"))
    spec.loader.exec_module(mod)
    return mod


# ------------------------------------------------------------------------------------------------- the run
def run_all(installed: Path, scratch: Path, fetched_after: str, map_path: Path) -> dict:
    if "/skills/synced/" in str(scratch.resolve()):
        raise SystemExit("refusing a scratch directory under the synced install directory")
    if scratch.exists():
        shutil.rmtree(scratch)
    base, a2, a3 = scratch / "base", scratch / "a2", scratch / "a3"
    for d in (base, a2, a3):
        d.mkdir(parents=True)
    smap = json.loads(map_path.read_text(encoding="utf-8"))
    stand_in = smap.get("stand_in") is True
    sm = ["--stand-in-ok"] if stand_in else []
    gates: dict = {}
    stand_ins: list = []
    if stand_in:
        stand_ins.append(f"successor map {map_path.name}: {smap.get('stand_in_rule') or 'each successor = its predecessor'}")
    for d in sorted(installed.iterdir()):
        if d.is_dir():
            shutil.copytree(d, base / d.name, ignore=shutil.ignore_patterns("__pycache__"))
    ggc = base / "glow-graph-contract/scripts/graph_parts.py"
    tmp = {"TMPDIR": str(scratch)}

    # N0 identities ------------------------------------------------------------------------------------------
    want = expected_digests()
    rows = []
    for k, v in want.items():
        r = {"skill": k, "expected": v, "installed": freeze(installed / k), "copy": freeze(base / k)}
        r["ok"] = r["expected"] == r["installed"] == r["copy"]
        rows.append(r)
    c, o, e = run([PY, ggc, "build", REPO / "docs/graph/parts", scratch / "main-100926.1.md"], env_extra=tmp)
    tok, d29 = build_token(o), d29_token()
    gates["N0_identities"] = {"skills": rows, "skills_9": len(rows) == 9, "graph_build_exit": c, "graph_token": tok,
                              "d29_token": d29, "graph_token_equals_d29": token_matches(tok, d29),
                              "ok": len(rows) == 9 and all(r["ok"] for r in rows) and c == 0 and token_matches(tok, d29)}

    # N1 guard, resolver, binding and map self-tests --------------------------------------------------------
    n1 = {}
    c, st = jrun([PY, HERE / "body_check.py", "selftest"])
    n1["body_check.selftest"] = {"exit": c, "ok": st.get("ok"), "guards": st.get("guards"), "fixture_rows": st.get("fixture_rows"),
                                 "fixture_rows_failing": st.get("fixture_rows_failing"),
                                 "span_resolver_false": [k for k, v in (st.get("span_resolver_and_additions") or {}).items() if v is False]}
    c, st = jrun([PY, HERE / "binding_pass.py", "selftest"])
    n1["binding_pass.selftest"] = {"exit": c, "ok": st.get("ok"), "false": [k for k, v in (st.get("checks") or {}).items() if v is False]}
    c, st = jrun([PY, HERE / "successor_map_102726.py", "selftest", TSV, scratch / "map-selftest"])
    n1["successor_map_102726.selftest"] = {"exit": c, "selftest_ok": st.get("selftest_ok"),
                                           "false": [k for k, v in (st.get("rows") or {}).items() if v is False]}
    c, st = jrun([PY, HERE / "successor_map_102726.py", "check", map_path, TSV, *sm])
    n1["successor_map_102726.check"] = {"exit": c, "ok": st.get("ok", c == 0)}
    c2, _ = jrun([PY, HERE / "successor_map_102726.py", "check", map_path, TSV])
    n1["stand_in_map_refused_without_flag"] = (c2 != 0) if stand_in else "NOT_APPLICABLE_REAL_MAP"
    c, st = jrun([PY, HERE / "binding_pass.py", "validate", "--successor-map", map_path])
    n1["binding_pass.validate"] = {"exit": c, "ok": st.get("ok")}
    for tool in ("assemble_edits.py", "assemble_guards.py"):
        c, st = jrun([PY, HERE / tool, "--check"])
        n1[tool + " --check"] = {"exit": c, **{k: v for k, v in st.items() if k != "mode"}}
    c, st = jrun([PY, HERE / "body_check.py", "plan", "--no-ops"])
    n1["body_check.plan_without_map_refused"] = c == 2 and "SUCCESSOR_MAP_REQUIRED" in json.dumps(st)
    n1["ok"] = (n1["body_check.selftest"]["ok"] is True and n1["binding_pass.selftest"]["ok"] is True
                and n1["successor_map_102726.selftest"]["selftest_ok"] is True and n1["successor_map_102726.check"]["exit"] == 0
                and n1["stand_in_map_refused_without_flag"] in (True, "NOT_APPLICABLE_REAL_MAP")
                and n1["binding_pass.validate"]["ok"] is True
                and n1["assemble_edits.py --check"].get("edits_json_current") is True
                and n1["assemble_guards.py --check"].get("guards_json_current") is True
                and n1["body_check.plan_without_map_refused"])
    gates["N1_selftests"] = n1

    # N2 body rehearsal on the fresh reads --------------------------------------------------------------------
    bc_common = ["--successor-map", map_path, "--since-minutes", "900", "--fetched-after", fetched_after]
    c, pl = jrun([PY, HERE / "body_check.py", "plan", "--no-ops", *bc_common])
    pages = pl.get("pages", [])
    edits = json.loads((HERE / "edits.json").read_text(encoding="utf-8"))
    moved = [p["prompt"] for p in pages if "error" not in p and not p.get("revision_matches_plan")]
    moved_ops_resolve = {p["prompt"]: (not p["ops_not_applied"] and p["batch_safe"]) for p in pages if p.get("prompt") in moved}
    failing_rows = [{"prompt": p["prompt"], "guard": g, "count_before": p["guards_before"][g]["count"],
                     "count_after": p["guards_after"][g]["count"]}
                    for p in pages if "error" not in p for g in p["guards_failing_after"]]
    mg = next((p for p in pages if p.get("prompt") == "GCFPE-MGMT-10"), {})
    c_rp2, pl2 = jrun([PY, HERE / "body_check.py", "plan", "--no-ops", *bc_common, "--with-conditional", "R-P2"])
    pe2 = next((p for p in pl2.get("pages", []) if p.get("prompt") == "PE"), {})
    gates["N2_body_rehearsal"] = {
        "body_check.plan.exit": c, "body_check.plan.ok": pl.get("ok"), "stand_in": pl.get("stand_in"),
        "pages_read": sum(1 for p in pages if "error" not in p), "pages_total": len(pages),
        "pages_in_edits_json": len(edits["pages"]), "no_fetch_found": [p["prompt"] for p in pages if "error" in p],
        "pages_ok": pl.get("pages_ok"),
        "ops": sum(len(p.get("ops", [])) for p in pages), "ops_applied": sum(sum(o["applied"] for o in p.get("ops", [])) for p in pages),
        "binding_ops": sum(p.get("binding_ops", 0) for p in pages),
        "binding_identity_under_stand_in": sum(p.get("binding_identity_under_stand_in", 0) for p in pages),
        "revisions_match_pins": sum(bool(p.get("revision_matches_plan")) for p in pages),
        "revisions_moved_since_pins": moved, "moved_pages_ops_still_resolve": moved_ops_resolve,
        "batch_safe": sum(bool(p.get("batch_safe")) for p in pages),
        "check_would_pass": sum(bool(p.get("check_would_pass")) for p in pages),
        "binding_current_after": sum(bool(p.get("binding_current_after")) for p in pages),
        "probe_ok": sum(bool((p.get("probe") or {}).get("ok")) for p in pages),
        "guard_rows": sum(len(p.get("guards_after", {})) for p in pages),
        "guard_rows_failing_before": sum(sum(not v["pass"] for v in p.get("guards_before", {}).values()) for p in pages),
        "guard_rows_failing_after": len(failing_rows), "guard_rows_failing_after_detail": failing_rows,
        "failing_rows_all_preexisting_text": all(r["count_after"] <= r["count_before"] for r in failing_rows),
        "failing_pages": sorted({r["prompt"] for r in failing_rows}),
        "gcfpe_mgmt10": {"ops": len(mg.get("ops", [])), "binding_ops": mg.get("binding_ops"),
                         "binding_stale_lines": mg.get("binding_stale_lines"), "guards_failing_after": mg.get("guards_failing_after"),
                         "revision_matches_pin": mg.get("revision_matches_plan"), "needs_no_edit":
                             len(mg.get("ops", [])) == 0 and mg.get("binding_stale_lines") == 0 and mg.get("ok") is True},
        "with_R-P2": {"exit": c_rp2, "ok": pl2.get("ok"), "pe_ok": pe2.get("ok"), "pe_ops": len(pe2.get("ops", [])),
                      "pe_guards_failing_after": pe2.get("guards_failing_after")},
        "ok": c == 0 and pl.get("ok") is True}

    # N3 registry form vs the shipped audit engine --------------------------------------------------------------
    c, rg = jrun([PY, HERE / "body_check.py", "registry", "--audit-root", base / "amthor-workspace-governance-audit", *bc_common])
    dis = rg.get("pages_disagreeing", [])
    form_disagree = [d for d in dis if d.get("before_registry_pass") != d.get("before_guard_pass")
                     or d.get("after_registry_pass") != d.get("after_guard_pass")]
    gates["N3_registry_form"] = {
        "body_check.registry.exit": c, "body_check.registry.ok": rg.get("ok"), "fixture_rows": rg.get("fixture_rows"),
        "fixtures_disagreeing": len(rg.get("fixtures_disagreeing", [])), "page_rows": rg.get("page_rows"),
        "page_rows_not_ok": len(dis), "page_rows_where_registry_form_and_guard_disagree": len(form_disagree),
        "page_rows_not_ok_only_because_guard_fails_after": len(dis) - len(form_disagree),
        "registry_form_agrees_everywhere": not rg.get("fixtures_disagreeing") and not form_disagree,
        "ok": c == 0 and rg.get("ok") is True}

    # N4 graph builds -----------------------------------------------------------------------------------------
    ga = HERE / "graph_assemble_102726.py"
    cand, prod = a2 / "candidate-parts", a2 / "production-parts"
    shutil.copytree(REPO / "docs/graph/parts", cand)
    c_ap, ap = jrun([PY, ga, "apply", cand, map_path, *sm])
    c_ri, _, _ = run([PY, ggc, "reindex", cand], env_extra=tmp)
    c_ck, ck = jrun([PY, ga, "check", cand, REPO / "docs/graph/parts", map_path, *sm])
    c_b1, o1, _ = run([PY, ggc, "build", cand, a2 / "candidate-102726.1.md"], env_extra=tmp)
    c_r1, rt1 = jrun([PY, ga, "routes", a2 / "candidate-102726.1.md"])
    c_fl, _ = jrun([PY, ga, "flip", cand, prod])
    c_ck2, ck2 = jrun([PY, ga, "check", prod, REPO / "docs/graph/parts", map_path, "--flipped", *sm])
    c_b2, o2, _ = run([PY, ggc, "build", prod, a2 / "production-102726.1.md"], env_extra=tmp)
    c_r2, rt2 = jrun([PY, ga, "routes", a2 / "production-102726.1.md"])
    c_st, stg = jrun([PY, ga, "selftest", REPO / "docs/graph/parts", map_path, scratch / "graph-selftest", ggc, *sm])
    gates["N4_graph"] = {
        "apply.apply_ok": ap.get("apply_ok"), "reindex_exit": c_ri, "check_candidate.check_ok": ck.get("check_ok"),
        "check_candidate.errors": ck.get("errors"), "candidate_build": build_token(o1),
        "routes_candidate.routes_ok": rt1.get("routes_ok"), "routes_candidate_false": [k for k, v in (rt1.get("flags") or {}).items() if not v],
        "check_production.check_ok": ck2.get("check_ok"), "check_production.errors": ck2.get("errors"),
        "production_build": build_token(o2), "routes_production.routes_ok": rt2.get("routes_ok"),
        "selftest.selftest_ok": stg.get("selftest_ok"), "selftest_false": [k for k, v in (stg.get("rows") or {}).items() if not v],
        "stand_in_used": ap.get("stand_in_used"),
        "ok": all(x == 0 for x in (c_ap, c_ri, c_ck, c_b1, c_r1, c_fl, c_ck2, c_b2, c_r2, c_st))
        and ck.get("check_ok") is True and ck2.get("check_ok") is True and rt1.get("routes_ok") is True
        and rt2.get("routes_ok") is True and stg.get("selftest_ok") is True
        and build_token(o1)["validation_pass"] and build_token(o2)["validation_pass"]}
    if stand_in:
        stand_ins.append("graph and contract digests depend on the stand-in successor URLs; EXECUTE re-measures them")

    # N5 R1 successor, contracts and regenerator proof ----------------------------------------------------------
    r1 = a2 / "r1"
    r1.mkdir(parents=True, exist_ok=True)   # the R1 builder writes into an existing --out-dir
    c_r1b, r1b = jrun([PY, EVID / "build_r1_successor_20261027.py", base, REPO, "--out-dir", r1, "--expect-decision-record", DECISIONS])
    c_r1s, r1s = jrun([PY, EVID / "build_r1_successor_20261027.py", "selftest", base, REPO, scratch / "r1-selftest"])
    plan_file = a2 / "PLAN-20261027.standin.md"
    plan_file.write_text("STAND-IN for docs/ephemeral/modifications/MODIFICATION-20261027-gcfpe-backlog-open-items PLAN-20261027.md\n",
                         encoding="utf-8")
    stand_ins.append("PLAN file: a scratch stand-in for PLAN-20261027.md (fills @PLAN_SHA256 / @PLAN_BYTES)")
    c_v, vv = jrun([PY, HERE / "contracts_102726.py", "values", REPO, "--check"])
    oracle = r1 / "oracle-glow-hde-canonical-change-flow-r1-20261027.json"
    c_cr, cr = jrun([PY, HERE / "contracts_102726.py", "run", REPO, base, a2, a2 / "candidate-102726.1.md",
                     a2 / "production-102726.1.md", oracle, plan_file, *(["--stand-in"] if stand_in else [])])
    if (a2 / "contracts/graph-100926.1.md").exists():
        shutil.copyfile(a2 / "contracts/graph-100926.1.md", a2 / "graph-100926.1.md")
    gates["N5_contracts_regenerator"] = {
        "r1_build.exit": c_r1b, "r1_build.build_ok": r1b.get("build_ok", (r1b.get("build") or {}).get("build_ok")),
        "r1_build.rows": r1b.get("rows", (r1b.get("build") or {}).get("rows")),
        "r1_build.decision_record_match": r1b.get("decision_record_match", (r1b.get("build") or {}).get("decision_record_match")),
        "r1_selftest.selftest_ok": r1s.get("selftest_ok"),
        "release_values.check": {"exit": c_v, **{k: v for k, v in vv.items() if k != "mode"}},
        "contracts.run.ok": cr.get("ok"), "Q1_PASS": (cr.get("Q1") or {}).get("Q1_PASS"),
        "Q5_checks_false": [k for k, v in (cr.get("Q5_checks") or {}).items() if not v],
        "injected_refusals_false": [k for k, v in (cr.get("injected_refusals") or {}).items() if not v],
        "contract_digests": {k: {x: v.get(x) for x in ("exit", "bytes", "sha256")} for k, v in (cr.get("contracts") or {}).items()},
        "ok": c_r1b == 0 and c_r1s == 0 and c_v == 0 and c_cr == 0 and cr.get("ok") is True}

    # N6 the 102726.1 profile ------------------------------------------------------------------------------------
    c_p, pr = jrun([PY, HERE / "make_profile_20261027.py", "dryrun", base, scratch / "profile",
                    "--production-md", a2 / "production-102726.1.md",
                    "--production-contract", a2 / "contracts/gcfpe-20261027.1-102726.1-production-contract.json",
                    "--r1-dir", r1, "--plan", plan_file, "--map", map_path, *sm])
    prun = pr.get("profile_run") or {}
    gates["N6_profile_102726"] = {
        "make_profile.dryrun.exit": c_p, "make_profile.dryrun.ok": pr.get("ok"),
        "substitutions": (pr.get("build") or {}).get("substitutions"), "profile_errors": prun.get("errors"),
        "unexpected_errors": prun.get("unexpected_errors"), "expected_pending": prun.get("expected_pending"),
        "regressions_false": [k for k, v in (pr.get("regressions") or {}).items() if not v],
        "ok": c_p == 0 and pr.get("ok") is True and not prun.get("unexpected_errors")}

    # N8 package redlines, build and the packages' own gates (before N7, which uses the built trees) --------------
    c8, _, e8 = run([PY, HERE / "a3_package_dryrun_102726.py", base, a3, "--a2", a2, "--map", map_path,
                     "--receipt", scratch / "a3-packages.json"], timeout=7200)
    p8 = json.loads((scratch / "a3-packages.json").read_text(encoding="utf-8")) if (scratch / "a3-packages.json").exists() else {}
    gates["N8_packages"] = {
        "a3_package_dryrun.exit": c8, "stderr_tail": e8.strip()[-300:] or None,
        **{f"{g}.ok": (p8.get(g) or {}).get("ok") for g in ("G1_redlines", "G2_build", "G3_suite", "G4_release_validators",
                                                             "G5_contracts", "G6_injections")},
        "G3_suite.ok_except_preexisting": (p8.get("G3_suite") or {}).get("ok_except_preexisting"),
        "G3_suite.findings_preexisting_in_installed_suite": (p8.get("G3_suite") or {}).get("findings_preexisting_in_installed_suite"),
        "G3_suite.findings_from_this_change": (p8.get("G3_suite") or {}).get("findings_from_this_change"),
        "G4.cf_validate_gcfpe_20261027": (p8.get("G4_release_validators") or {}).get("cf_validate_gcfpe_20261027"),
        "G4.cf_validate_diagnostic_with_cl05_parent": (p8.get("G4_release_validators") or {}).get("cf_validate_gcfpe_20261027_diagnostic_with_cl05_parent"),
        "real_errors": p8.get("real_errors"), "built_digests": (p8.get("G2_build") or {}).get("built_digests"),
        "ok": bool(p8) and all((p8.get(g) or {}).get("ok") is True for g in
                                ("G1_redlines", "G2_build", "G4_release_validators", "G5_contracts", "G6_injections"))
        and (p8.get("G3_suite") or {}).get("ok_except_preexisting") is True and not p8.get("real_errors")}

    # N7 all 56 bodies through the built 102726.1 profile, unedited and edited ----------------------------------
    sys.path.insert(0, str(HERE))
    import body_check as B  # noqa: E402
    B.use_map(str(map_path))
    root = os.path.expanduser("~/.claude/projects")
    suite = a3 / "suite"
    fv, cf = suite / "flowmaster-validate", suite / "change-flow"
    members = [k for k in B.EDITS["pages"] if k != "PE"]
    variants = {"before": None, "after_stand_in_map": B.STATE["map"]}
    probe_map = B.bp.probe(B.STATE["map"]) if B.STATE["stand_in"] else None
    if probe_map is not None:
        variants["after_probe_ids"] = probe_map
    n7 = {"members": len(members)}
    if not (fv / "scripts/validate_gcfpe_20261027.py").exists():
        n7.update(error="NO_BUILT_VALIDATOR: N8's build did not produce flowmaster-validate/scripts/validate_gcfpe_20261027.py", ok=False)
    else:
        for name, m in variants.items():
            shared = dict(B.SHARED, **B.bp.shared_from_map(m)) if m is not None else B.SHARED
            bodies, unfetched = {}, []
            for prompt in members:
                got = B.latest_fetch(B.EDITS["pages"][prompt]["page_id"], root, SESSION, 900, fetched_after)
                if not got:
                    unfetched.append(prompt)
                    continue
                text = got[2]
                if m is not None:
                    ops, _ = B.page_ops(prompt, text, m, [], shared)
                    text, _ = B.apply_all(text, ops, shared)
                bodies[prompt] = text
            contract = cf / CF_REL
            if name == "after_probe_ids":
                contract = scratch / "probe-contract-102726.1.json"
                n7["probe_contract_members_rebound"] = probe_contract(cf / CF_REL, contract, B.STATE["map"], m)
            forms = {"fetched": bodies}
            if name == (("after_probe_ids" if probe_map is not None else "after_stand_in_map")):
                forms["markdown_form_diagnostic"] = {k: markdown_form(v) for k, v in bodies.items()}
            for form, payload in forms.items():
                c7, res = jrun([PY, "scripts/validate_gcfpe_20261027.py", cf, "--contract", contract, "--bodies-stdin"],
                               cwd=fv, inp=json.dumps(payload))
                errs = res.get("errors", []) or []
                berrs = [e for e in errs if e.startswith("PROMPT")]
                key = name if form == "fetched" else name + "__markdown_form_diagnostic"
                scoped = [e for e in errs if e.startswith(BODY_SCOPED_PREFIXES)]
                contract_errs = [e for e in errs if not e.startswith(BODY_SCOPED_PREFIXES)]
                n7[key] = {"exit": c7, "bodies_supplied": len(payload), "unfetched": unfetched,
                           "bodies_validated": len(res.get("prompt_bodies_validated", []) or []),
                           "not_evaluated": res.get("prompt_body_checks_not_evaluated"),
                           "errors_total": len(errs), "body_scoped_errors": len(scoped),
                           "body_scoped_error_classes": sorted({e.split(":")[0] for e in scoped}),
                           "body_scoped_error_ids": sorted({":".join(e.split(":")[:3]) for e in scoped})
                           if len(scoped) <= 80 else sorted({":".join(e.split(":")[:2]) for e in scoped})[:80],
                           "contract_level_errors": len(contract_errs),
                           "contract_level_error_classes": sorted({e.split(":")[0] for e in contract_errs}),
                           "body_error_classes": body_classes(errs), "body_errors": len(berrs)}
        after = n7.get("after_probe_ids") or n7["after_stand_in_map"]
        n7["stand_in_note"] = ("after_stand_in_map applies every operation with the stand-in map (successor = predecessor), so "
                               "PROMPT_BINDING_SUPERSEDED fires on every surviving binding by construction; after_probe_ids "
                               "applies them with binding_pass.probe() synthetic successor ids against a scratch copy of the "
                               "built contract whose member_registry page identities are the same probe ids, and is the gating "
                               "variant; the __markdown_form_diagnostic row is diagnostic only") if probe_map else None
        n7["probe_rebind_contract_classes_expected"] = sorted(PROBE_REBIND_CLASSES)
        n7["ok"] = (after["bodies_validated"] == 56 and after["body_scoped_errors"] == 0 and not after["not_evaluated"]
                    and n7["after_stand_in_map"]["contract_level_errors"] == 0
                    and set(after["contract_level_error_classes"]) <= PROBE_REBIND_CLASSES
                    and n7["before"]["body_scoped_errors"] > 0)
    gates["N7_bodies_through_profile"] = n7

    # N9 the registry, with every row's assertions run on the edited bodies -------------------------------------
    c9, _, e9 = run([PY, HERE / "a3_registry_dryrun_102726.py", base, a3, "--a2", a2, "--map", map_path,
                     "--receipt", scratch / "a3-registry.json"], timeout=3600)
    r9 = json.loads((scratch / "a3-registry.json").read_text(encoding="utf-8")) if (scratch / "a3-registry.json").exists() else {}
    regfile = a3 / "registry-dryrun/candidate-registry.md"
    n9 = {"a3_registry_dryrun.exit": c9, "a3_registry_dryrun.ok": r9.get("ok"),
          **{f"{k}.ok": (r9.get(k) or {}).get("ok") for k in ("build_candidate", "check_candidate",
                                                              "assertions_candidate_synthetic_inject", "build_selected",
                                                              "check_selected", "compare")},
          "rebuild_byte_identical": r9.get("rebuild_byte_identical"), "selftest.selftest_ok": (r9.get("selftest") or {}).get("selftest_ok")}
    if regfile.exists():
        A = load_engine(a3 / "registry-dryrun/amthor-workspace-governance-audit")
        data = A.load_data(str(regfile))
        m = probe_map if probe_map is not None else B.STATE["map"]
        shared = dict(B.SHARED, **B.bp.shared_from_map(m))
        rows9, before_fail = [], 0
        A_sel = load_engine(installed / "amthor-workspace-governance-audit")
        sel_rows = {r["prompt_key"]: r for r in A_sel.load_data(str(REPO / "docs/prompt_ecosystem_management/project-prompt-contract-registry.md"))["prompts"]}
        for row in data["prompts"]:
            key = row["prompt_key"]
            meta = B.EDITS["pages"].get(key)
            got = B.latest_fetch(meta["page_id"], root, SESSION, 900, fetched_after) if meta else None
            if not got:
                rows9.append({"prompt": key, "error": "NO_FETCH_FOUND", "ok": False})
                continue
            ops, _ = B.page_ops(key, got[2], m, [], shared)
            edited, _ = B.apply_all(got[2], ops, shared)
            r = row_assertions(A, row, edited)
            before_fail += bool(A._evaluate_assertions(row, got[2], "transient"))
            # each finding classified: INHERITED when the selected 100926.1 registry carries the same assertion on
            # the same row and the installed engine reports it on today's unedited body; NEW otherwise
            srow = sel_rows.get(key)
            sel_vals = {(x.get("value") if isinstance(x, dict) else x) for kind in ASSERT_KINDS
                        for x in ((srow or {}).get("audit_assertions") or {}).get(kind) or []}
            sel_fail = {str((f.get("observed") or {}).get("summary")) for f in
                        (A_sel._evaluate_assertions(srow, got[2], "transient") if srow else [])}
            guard_of = {(x.get("value") if isinstance(x, dict) else x): (x.get("guard") if isinstance(x, dict) else None)
                        for kind in ASSERT_KINDS for x in (row.get("audit_assertions") or {}).get(kind) or []}
            inh, new_ids = 0, []
            for f in A._evaluate_assertions(row, edited, "transient"):
                summ = str((f.get("observed") or {}).get("summary"))
                val = summ.split(": ", 1)[1] if ": " in summ else summ
                if val in sel_vals and summ in sel_fail:
                    inh += 1
                else:
                    new_ids.append(f"{f.get('rule_id')}:{guard_of.get(val) or 'unguarded'}")
            md_findings = len(A._evaluate_assertions(row, markdown_form(edited), "transient"))
            rows9.append({"prompt": key, **r, "findings_inherited": inh, "findings_new": len(new_ids),
                          "new_finding_ids": sorted(new_ids), "findings_markdown_form_diagnostic": md_findings})
        n9.update({"body_rows": len(rows9), "body_rows_ok": sum(r["ok"] for r in rows9),
                   "assertions_evaluated": sum(r.get("assertions", 0) for r in rows9),
                   "findings_after_total": sum(r.get("findings_after", 0) for r in rows9),
                   "injected_fired": sum(r.get("injected_fired", 0) for r in rows9),
                   "injected_missed": sum(len(r.get("injected_missed", [])) for r in rows9),
                   "rows_failing_before_edits": before_fail,
                   "findings_inherited_total": sum(r.get("findings_inherited", 0) for r in rows9),
                   "rows_with_inherited": sum(1 for r in rows9 if r.get("findings_inherited")),
                   "findings_new_total": sum(r.get("findings_new", 0) for r in rows9),
                   "rows_with_new": sorted(r["prompt"] for r in rows9 if r.get("findings_new")),
                   "markdown_form_diagnostic": {
                       "note": "diagnostic only, not a gate: the edited bodies with Notion inline markup rewritten as Markdown",
                       "findings_total": sum(r.get("findings_markdown_form_diagnostic", 0) for r in rows9),
                       "rows_with_findings": sum(1 for r in rows9 if r.get("findings_markdown_form_diagnostic"))},
                   "failing_rows": [{k: r.get(k) for k in ("prompt", "findings_after", "findings_inherited", "findings_new",
                                                           "new_finding_ids", "injected_missed", "error")}
                                    for r in rows9 if not r["ok"]],
                   "bodies_edited_with": "probe ids" if probe_map is not None else "the map"})
    else:
        n9["body_rows"] = 0
    n9["ok"] = (c9 == 0 and r9.get("ok") is True and n9.get("body_rows") == 56 and n9.get("body_rows_ok") == 56
                and n9.get("rows_failing_before_edits", 0) > 0)
    gates["N9_registry"] = n9
    stand_ins.append("registry: page revisions are edits.json's pins and the catalog id is the 100926.1 catalog's (A3)")

    # N10 activation render and control check ----------------------------------------------------------------------
    cc, ar = HERE / "control_check_102726.py", HERE / "activation_render_102726.py"
    c_ops, opsck = jrun([PY, HERE / "make_activation_ops_102726.py", "check"])
    c_cs, ccs = jrun([PY, cc, "selftest", "--successor-map", map_path])
    today = {}
    for ph in ("candidate", "activation", "archived"):
        c, d = jrun([PY, cc, "check", "--successor-map", map_path, "--phase", ph, "--pages", *CONTROLS,
                     "--fetched-after", fetched_after, "--since-minutes", "900"])
        today[ph] = {"exit": c, "ok": d.get("ok"), "pages_read": sum(1 for p in d.get("pages", []) if "error" not in p),
                     "failed_checks_total": d.get("failed_checks_total"), "findings_total": d.get("findings_total")}
    c, d = jrun([PY, cc, "check", "--successor-map", map_path, "--phase", "sweep", "--fetched-after", fetched_after,
                 "--since-minutes", "900"])
    today["sweep"] = {"exit": c, "ok": d.get("ok"), "pages_read": sum(1 for p in d.get("pages", []) if "error" not in p),
                      "failed_checks_total": d.get("failed_checks_total")}
    c_rs, ars = jrun([PY, ar, "selftest", "--successor-map", map_path, "--parts", cand])
    c_ch, ch = jrun([PY, ar, "plan", "--chain", "--standin-values", "--successor-map", map_path, "--parts", cand,
                     "--phase", "sweep", "--fetched-after", fetched_after, "--since-minutes", "900"])
    phases = ch.get("phases", [])
    gates["N10_activation"] = {
        "make_activation_ops.check": {"exit": c_ops, "ok": opsck.get("ok"), "file_equals_rebuild": opsck.get("file_equals_rebuild")},
        "control_check.selftest": {"exit": c_cs, "ok": ccs.get("ok"), "cases": f"{ccs.get('cases_passed')}/{ccs.get('cases_total')}",
                                   "archive_set_102726": ccs.get("archive_set_102726")},
        "control_check.today_expected_to_fail": today,
        "fires_on_today_reads": all(v["exit"] != 0 for v in today.values()),
        "control_pages_read_candidate_phase": today["candidate"]["pages_read"],
        "activation_render.selftest": {"exit": c_rs, "ok": ars.get("ok"), "cases": f"{ars.get('cases_passed')}/{ars.get('cases_total')}"},
        "activation_render.chain": {"exit": c_ch, "ok": ch.get("ok"), "stand_in": ch.get("stand_in"),
                                    "stand_in_marker_values": ch.get("stand_in_marker_values"), "totals": ch.get("totals"),
                                    "moves": ch.get("moves"), "map_parts_errors": ch.get("map_parts_errors"),
                                    "pins_match": sum(bool(v.get("revision_matches_pin")) for v in (ch.get("pages") or {}).values()),
                                    "pins_total": len(ch.get("pages") or {}),
                                    "read_only_pins_match": all(v.get("revision_matches_pin") for v in (ch.get("read_only_pins") or {}).values()),
                                    "phases": [{"phase": p["phase"], "pages_judged": p["control"].get("pages_judged"),
                                                "pages_ok": p["control"].get("pages_ok"), "findings": p["control"].get("findings"),
                                                "refused": sum(len(v["refused"]) for v in p["pages"].values())} for p in phases]},
        "ok": c_ops == 0 and c_cs == 0 and ccs.get("ok") is True and all(v["exit"] != 0 for v in today.values())
        and c_rs == 0 and ars.get("ok") is True and c_ch == 0 and ch.get("ok") is True}
    if stand_in:
        stand_ins.append("activation: binding_pass.probe() synthetic ids and the named stand-in marker values (A4)")

    order = ["N0_identities", "N1_selftests", "N2_body_rehearsal", "N3_registry_form", "N4_graph", "N5_contracts_regenerator",
             "N6_profile_102726", "N7_bodies_through_profile", "N8_packages", "N9_registry", "N10_activation"]
    return {"record_type": "GCFPE_102726_PLAN_DRY_RUN", "modification": "MODIFICATION-20261027-gcfpe-backlog-open-items",
            "worker": "A5", "date_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "repository_head": run(["git", "-C", REPO, "rev-parse", "HEAD"])[1].strip(), "fetched_after": fetched_after,
            "successor_map": str(map_path.relative_to(REPO)) if map_path.is_relative_to(REPO) else str(map_path),
            "stand_in_used": stand_in, "stand_ins": stand_ins,
            "gates": {k: gates[k] for k in order}, "gate_ok": {k: gates[k]["ok"] for k in order},
            "ok": all(gates[k]["ok"] for k in order),
            "d22": "transient reads of this session's harness records; bodies passed on pipes only; no body text in this receipt"}


# ------------------------------------------------------------------------------------------------- self-test
def selftest(scratch: Path) -> dict:
    """Each check this file adds fails on an injected defect."""
    if scratch.exists():
        shutil.rmtree(scratch)
    scratch.mkdir(parents=True)
    rows = {}
    # freeze digest comparison: a changed byte changes the digest
    d = scratch / "skill"
    (d / "x").mkdir(parents=True)
    (d / "x/a.txt").write_text("a\n", encoding="utf-8")
    f1 = freeze(d)
    (d / "x/a.txt").write_text("b\n", encoding="utf-8")
    rows["freeze_detects_changed_byte"] = freeze(d) != f1
    # graph token comparison
    want = d29_token()
    good = {"nodes": want["nodes"], "edges": want["edges"], "state_routes": want["state_routes"], "bytes": want["bytes"],
            "sha256": want["sha256_prefix"] + "0" * (64 - len(want["sha256_prefix"])), "validation_pass": True}
    rows["token_accepts_match"] = token_matches(good, want)
    rows["token_rejects_edge_count"] = not token_matches(dict(good, edges=good["edges"] + 1), want)
    rows["token_rejects_sha"] = not token_matches(dict(good, sha256="f" * 64), want)
    rows["token_rejects_failed_validation"] = not token_matches(dict(good, validation_pass=False), want)
    rows["build_token_parses"] = build_token("build: 3 nodes, 4 edges, 3 state_routes\n  embedded JSON 10 bytes  sha256 "
                                             + "a" * 64 + "\nvalidation PASS")["edges"] == 4
    # digests come from W7, nine of them
    rows["nine_expected_digests_from_w7"] = len(expected_digests()) == 9

    # body-assertion evaluation (N9) on synthetic text through a minimal engine stand-in with the shipped semantics
    class Eng:
        @staticmethod
        def _evaluate_assertions(row, text, mode):
            out = []
            aa = row["audit_assertions"]
            for r in aa.get("required_regex") or []:
                if not re.search(r["value"], text, flags=re.MULTILINE):
                    out.append({"rule_id": r["rule_id"], "guard": r.get("guard")})
            for r in aa.get("forbidden_regex") or []:
                if re.search(r["value"], text, flags=re.MULTILINE):
                    out.append({"rule_id": r["rule_id"], "guard": r.get("guard")})
            return out
    row = {"prompt_key": "X", "audit_assertions": {
        "required_regex": [{"rule_id": "CTR-002", "value": "(?m)^Keep this line$", "guard": "G-T"}],
        "forbidden_regex": [{"rule_id": "SRC-001", "value": "(?m)^Prompt version:"},
                            {"rule_id": "CTR-001", "value": "CONTROL_NOTION"}]}}
    ok_text = "a\nKeep this line\nb\n"
    rows["row_assertions_clean_passes"] = row_assertions(Eng, row, ok_text)["ok"]
    rows["row_assertions_missing_required_fails"] = not row_assertions(Eng, row, "a\nb\n")["ok"]
    rows["row_assertions_forbidden_present_fails"] = not row_assertions(Eng, row, ok_text + "Prompt version: 1\n")["ok"]
    no_forb = {"prompt_key": "X", "audit_assertions": {"required_regex": row["audit_assertions"]["required_regex"]}}
    rows["row_assertions_uncarried_forbidden_fails"] = not row_assertions(Eng, no_forb, ok_text)["ok"]
    vacuous = {"prompt_key": "X", "audit_assertions": {"required_regex": [{"rule_id": "CTR-002", "value": "(?m)^$|x?"}],
                                                       "forbidden_regex": row["audit_assertions"]["forbidden_regex"]}}
    rows["row_assertions_vacuous_required_fails"] = not row_assertions(Eng, vacuous, ok_text)["ok"]
    rows["body_classes_parse"] = body_classes(["PROMPT_BINDING_SUPERSEDED:PR-10:CF-C-10", "OTHER:x"]) == ["PROMPT_BINDING_SUPERSEDED"]
    rows["markdown_form_rewrites_markup"] = markdown_form("a <code>X</code> <b>B</b> <i>c</i> d\\_e") == "a `X` **B** *c* d_e"
    old_id, new_id = "a" * 32, "b" * 32
    src = scratch / "c.json"
    src.write_text(json.dumps({"member_registry": {"K": {"notion_url": f"https://app.notion.com/p/{old_id}?pvs=204"},
                                                   "S": {"notion_url": "u"}}}), encoding="utf-8")
    n = probe_contract(src, scratch / "p.json", {"members": {"K": {"page_id": old_id}, "S": {"page_id": "c" * 32}}},
                       {"members": {"K": {"page_id": new_id}, "S": {"page_id": "c" * 32}}})
    pc = json.loads((scratch / "p.json").read_text(encoding="utf-8"))["member_registry"]
    rows["probe_contract_rebinds_only_changed_members"] = (n == 1 and new_id in pc["K"]["notion_url"]
                                                          and pc["S"]["notion_url"] == "u")
    ok = all(rows.values())
    shutil.rmtree(scratch)
    return {"mode": "selftest", "rows": rows, "selftest_ok": ok}


def main() -> int:
    a = sys.argv[1:]
    if not a or a[0] not in ("run", "selftest"):
        sys.exit(__doc__)
    if a[0] == "selftest":
        res = selftest(Path(a[1]))
        print(json.dumps(res, indent=1))
        return 0 if res["selftest_ok"] else 1
    if not SESSION:
        sys.exit("set CLAUDE_CODE_SESSION_ID")
    installed, scratch, fetched_after = Path(a[1]), Path(a[2]), a[3]
    map_path = Path(a[a.index("--map") + 1]) if "--map" in a else HERE / "successor-map-standin.json"
    rec = run_all(installed, scratch, fetched_after, map_path.resolve())
    rec["dry_run_selftest"] = selftest(scratch.parent / (scratch.name + "-selftest"))
    rec["gate_ok"]["dry_run_selftest"] = rec["dry_run_selftest"]["selftest_ok"]
    rec["ok"] = rec["ok"] and rec["dry_run_selftest"]["selftest_ok"]
    out = json.dumps(rec, indent=1, ensure_ascii=False, default=str) + "\n"
    if "--receipt" in a:
        Path(a[a.index("--receipt") + 1]).write_text(out, encoding="utf-8")
    print(json.dumps(rec["gate_ok"] | {"ok": rec["ok"]}, indent=1))
    return 0 if rec["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
