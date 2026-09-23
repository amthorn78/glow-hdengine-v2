"""§9 item 9, skill-text regressions: §8a.4 (23 PR-skill), §8a.9 (8 amthor), §8b.10 skill text (36 + controls).
Each runs on a fresh scratch copy of the edited tree. Pass = exactly the expected finding set.
usage: PYTHONDONTWRITEBYTECODE=1 python3 regress_skills.py <edited-skills-root> <base-skills-root>"""
import ast, json, os, re, shutil, subprocess, sys
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
from texts import T  # noqa: E402
EDITED, BASE = Path(sys.argv[1]), Path(sys.argv[2])
REG = Path("/tmp/claude-0/e2/reg"); TMP = Path("/tmp/claude-0/e2/tmp")
ENV = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1", "TMPDIR": str(TMP)}
RESULTS = []


def rec(rid, ok, detail):
    RESULTS.append((rid, bool(ok)))
    print(("OK   " if ok else "BAD  ") + rid, str(detail)[:240])


# ---------------- non-fail-fast evaluation of the PR skill validator (§8a.0) ----------------
def pr_all_failures(root):
    tree = ast.parse((root / "glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py").read_text())
    d = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name):
            n = node.targets[0].id
            if n == "required":
                d["required"] = {k.value: v.value for k, v in zip(node.value.keys, node.value.values)}
            elif n in ("forbidden", "case_headings"):
                d[n] = [e.value for e in node.value.elts]
    skill = (root / "glow-hde-pr-development/SKILL.md").read_text()
    cases = (root / "glow-hde-pr-development/references/behavior-cases.md").read_text()
    comb = skill + "\n" + cases
    f = {f"missing {k} contract" for k, t in d["required"].items() if t not in comb}
    f |= {f"forbidden or unfinished content present: {t}" for t in d["forbidden"] if t.lower() in comb.lower()}
    f |= {f"missing behavior case: {h}" for h in d["case_headings"] if h not in cases}
    return f


def inject(t, s): return t + "\n" + s + "\n"
def delete(t, s):
    assert t.count(s) == 1, (t.count(s), s[:60]); return t.replace(s, "")
def replace(t, a, b):
    assert t.count(a) == 1, (t.count(a), a[:60]); return t.replace(a, b)


OLD27 = (BASE / "glow-hde-pr-development/SKILL.md").read_text().split("\n")[26]
assert "followed in the same session by PR-35" in OLD27
S, B = "glow-hde-pr-development/SKILL.md", "glow-hde-pr-development/references/behavior-cases.md"
F = "FAIL: forbidden or unfinished content present: "
pr_cases = [
    ("R-rev", S, lambda t: replace(t, "REVISION: 1.3.0", "REVISION: 1.2.5"), "FAIL: missing revision contract", {"missing revision contract"}),
    ("R-32", S, lambda t: inject(t, "Remain in the one dedicated PR-development session across both phases."), F + "one dedicated PR-development session", 1),
    ("R-37", S, lambda t: inject(t, T["V5"] + "."), F + T["V5"], 2),
    ("R-38", S, lambda t: inject(t, "followed by exactly one complete same-session `PR-35` handoff."), F + "same-session `PR-35` handoff", 1),
    ("R-44", S, lambda t: inject(t, "Continue in the same dedicated PR session until all applicable predicates are true:"), F + "Continue in the same dedicated PR session until all applicable predicates are true", 1),
    ("R-55", S, lambda t: inject(t, T["TEN"] + "."), F + T["TEN"], 2),
    ("R-63", S, lambda t: inject(t, "Resume the recorded phase in the same dedicated PR session, workspace/worktree, branch, open PR, current evidence and original Product Owner Proceed."), F + "same dedicated PR session, workspace/worktree, branch, open PR", 1),
    ("R-C6-27", S, lambda t: inject(t, OLD27), F + "followed in the same session by PR-35", 1),
    ("R-OLDLIST", B, lambda t: inject(t, "PR-35 returns only `MERGE_PENDING`, `RESCOPE_PENDING`, `RECOVERY_PENDING`, `REMOTE_EVIDENCE_PENDING`, or `PRODUCT_OWNER_DECISION_REQUIRED`."), F + "`MERGE_PENDING`, `RESCOPE_PENDING`", 1),
    ("R-TENFIELD", S, lambda t: inject(t, "The work unit keeps exactly one branch and one pull request, which the ten-field continuity list requires."), F + "ten-field", 1),
    ("R-CART", S, lambda t: delete(t, T["C-ART"]), "FAIL: missing artifact holds results contract", 1),
    ("R-CDEC", S, lambda t: delete(t, T["C-DEC"]), "FAIL: missing in-flight decisions contract", 1),
    ("R-CLAT", S, lambda t: delete(t, "**Decide it during work:**"), "FAIL: missing material latitude contract", 1),
    ("R-CPROC", S, lambda t: delete(t, T["C-PROCEED"]), "FAIL: missing one Proceed per plan contract", 1),
    ("R-TOP", S, lambda t: delete(t, T["A18"]), "FAIL: missing top-level PR-35 session contract", 1),
    ("R-SUB", S, lambda t: delete(t, "Subscribing is not polling, and it creates no session."), "FAIL: missing subscription is not polling contract", 1),
    ("R-DISP", S, lambda t: delete(t, " No agent merges, and no session is created by an agent."), "FAIL: missing no agent-created session contract", 1),
    ("R-NOBRANCH", S, lambda t: delete(t, "It carries no branch and no commit: "), "FAIL: missing handoff carries no branch contract", 1),
    ("R-heading", B, lambda t: replace(t, "## PR-40 rejection re-plan", "## PR-40 rejection"), "FAIL: missing behavior case: ## PR-40 rejection re-plan", 1),
    ("R-H-DEC", B, lambda t: replace(t, "## In-flight decisions", "## In-flight"), "FAIL: missing behavior case: ## In-flight decisions", 1),
    ("R-H-LAT", B, lambda t: replace(t, "## Implementor latitude", "## Latitude"), "FAIL: missing behavior case: ## Implementor latitude", 1),
    ("R-H-SUB", B, lambda t: replace(t, "## Pull request subscription", "## Subscription"), "FAIL: missing behavior case: ## Pull request subscription", 1),
    ("R-H-OBS", B, lambda t: replace(t, "## Observed merge", "## Merge observed"), "FAIL: missing behavior case: ## Observed merge", 1),
]
clean = pr_all_failures(EDITED)
r = subprocess.run([sys.executable, str(EDITED / "glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py")], capture_output=True, text=True, env=ENV)
rec("PR-clean", r.returncode == 0 and clean == set(), (r.stdout.strip(), sorted(clean)))
for name, rel, mut, expected, count in pr_cases:
    d = REG / name; shutil.rmtree(d, ignore_errors=True)
    shutil.copytree(EDITED / "glow-hde-pr-development", d / "glow-hde-pr-development")
    p = d / rel; p.write_text(mut(p.read_text(encoding="utf-8")), encoding="utf-8")
    r = subprocess.run([sys.executable, str(d / "glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py")], capture_output=True, text=True, env=ENV)
    af = pr_all_failures(d)
    n = count if isinstance(count, int) else len(count)
    ok = r.stdout.strip() == expected and r.returncode == 1 and len(af) == n and expected[6:] in af
    rec(name, ok, (r.returncode, r.stdout.strip()[:100], sorted(af)))
    shutil.rmtree(d)

# ---------------- amthor (§8a.9) ----------------
AB = EDITED / "amthor-workspace-governance-audit"
def rep(a, b):
    return lambda t: replace(t, a, b)
am_cases = [
    ("A-skill-list", "SKILL.md", rep(T["NINE"], T["TEN"])),
    ("A-interop-list", "references/interoperability-contracts.md", rep(T["NINE"], T["TEN"])),
    ("A-fixtures-list", "references/behavioral-fixtures.md", rep(T["NINE"], T["TEN"])),
    ("A-rev", "SKILL.md", rep("REVISION:** 1.12.0", "REVISION:** 1.11.3")),
    ("A-handoff-kept", "SKILL.md", rep("exactly one fenced `text` `NEXT_PROMPT_HANDOFF` block", "one fenced `text` `NEXT_PROMPT_HANDOFF` block")),
    ("A-inject-skill", "SKILL.md", lambda t: t + "\n- " + T["TEN"] + ".\n"),
    ("A-inject-interop", "references/interoperability-contracts.md", lambda t: t + "\n" + T["TEN"] + ".\n"),
    ("A-inject-fixtures", "references/behavioral-fixtures.md", lambda t: t + "\n- " + T["TEN"] + ".\n"),
]
want = {"A-handoff-kept": "test_exact_fenced_text_handoff_parity"}
for name, rel, mut in am_cases:
    d = REG / name; shutil.rmtree(d, ignore_errors=True); shutil.copytree(AB, d)
    p = d / rel; p.write_text(mut(p.read_text(encoding="utf-8")), encoding="utf-8")
    r = subprocess.run([sys.executable, "run_fixture_suite.py"], cwd=d / "scripts", capture_output=True, text=True, env=ENV)
    fails = re.findall(r"^(?:FAIL|ERROR): (\S+) \((\S+)\)", r.stderr, re.M)
    ran = re.search(r"Ran (\d+) tests", r.stderr)
    ok = [f[0] for f in fails] == [want.get(name, "test_exact_gcf17_continuity_parity")] and "FAILED (failures=1)" in r.stderr and ran and ran.group(1) == "34"
    rec(name, ok, (fails, ran.group(0) if ran else None))
    shutil.rmtree(d)

# ---------------- §8b.10 skill text ----------------
W = REG / "treeA"
END = "<!-- FLOWMASTER_SPECIALIZATION_END -->"
CF_RETIRED = [
    "one dedicated PR-development session", T["TEN"],
    "same-session PR-30 → PR-35 phase continuation", "same-session PR-35 handoff", "same-session PR-35 review/readiness",
    "same-session second phase", T["V5"],
    "historical pre-merge evidence; Nathan's later invocation asserts that Nathan manually merged",
    "A later Nathan PR-40 invocation asserts that Nathan's separate manual merge occurred",
    "One dedicated session per planned PR work unit; the same session performs both",
    "has only the manual-merge-assertion meaning",
    "The same dedicated PR session implements only that work unit",
    "Only after Nathan later asserts that the identified PR was manually merged may that invocation run",
    "GCF-14 — Create one dedicated PR session for one planned PR work unit",
]
REQ = ["PR-30 and PR-35 are two phases", T["NINE"], "run in two dedicated sessions", "never as a subagent, forked agent or workflow agent of PR-30",
       "no session is created by an agent", "One Proceed per approved per-PR plan", "It carries no branch and no commit",
       "exactly one fenced `text` `NEXT_PROMPT_HANDOFF` block", "PR_RETURN_PHASE", "PF10_BUILD_NOTES_ADDENDUM", "SOURCE_RESOLUTION_ERROR",
       "Only Nathan / Product Owner may manually invoke selected `PR-50", "ALPHA_STOPPED_PENDING_CHANGE_FLOW_REFACTOR"]


def fresh():
    shutil.rmtree(W, ignore_errors=True); shutil.copytree(EDITED, W)


def edit(rel, fn):
    p = W / rel; s = p.read_text(encoding="utf-8"); s2 = fn(s); assert s2 != s, rel; p.write_text(s2, encoding="utf-8")


def inj(rel, text): edit(rel, lambda s: s.replace(END, text + "\n\n" + END, 1))


def cf():
    r = subprocess.run([sys.executable, str(W / "change-flow/scripts/validate_gcfpe_20260914.py")], capture_output=True, text=True, env=ENV)
    return r.returncode, (r.stdout + r.stderr).strip()


def cf_all():
    s = (W / "change-flow/SKILL.md").read_text(encoding="utf-8")
    return [f"missing:{t[:30]}" for t in REQ if t not in s] + [f"retired:{t[:30]}" for t in CF_RETIRED if t.lower() in s.lower()]


def restamp():
    sys.path.insert(0, str(W / "flowmaster-validate/scripts"))
    import importlib.util
    spec = importlib.util.spec_from_file_location("vrestamp", W / "flowmaster-validate/scripts/validate_gcfpe_20260914.py")
    v = importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
    p = W / "flowmaster-validate/SKILL.md"
    p.write_text(re.sub(r"(?m)^SKILL_TREE_SHA256: [0-9a-f]{64}$", "SKILL_TREE_SHA256: " + v.skill_tree_digest(W / "flowmaster-validate"),
                        p.read_text(encoding="utf-8")), encoding="utf-8")


def suite():
    r = subprocess.run([sys.executable, str(W / "flowmaster-validate/scripts/validate_flowmaster.py"), "--skills-root", str(W)], capture_output=True, text=True, env=ENV)
    d = json.loads(r.stdout)
    errs = {k: v["errors"] for k, v in d["skills"].items() if v["errors"]}
    # The report mirrors each skill error as one FMV-SKILL-STRUCTURE-001 finding; anything else is extra.
    mirrored = sorted((k, e) for k, v in errs.items() for e in v)
    extra = [f["rule_id"] + ":" + f["evidence"][:60] for f in d["findings"]
             if not (f["rule_id"] == "FMV-SKILL-STRUCTURE-001"
                     and any(f["subject"].endswith(k + "/SKILL.md") and f["evidence"] == e for k, e in mirrored))]
    return d["verdict"], errs, extra


fresh(); rc, msg = cf(); rec("clean-cf", rc == 0 and cf_all() == [], msg)
for i, p in enumerate(CF_RETIRED, 1):
    fresh(); inj("change-flow/SKILL.md", p); rc, msg = cf()
    rec(f"R-CF-RP-{i}", rc == 1 and msg == "FAIL: retired skill clause present: " + p and len(cf_all()) == 1, msg)
fresh(); inj("change-flow/SKILL.md", CF_RETIRED[0].upper()); rc, msg = cf()
rec("R-CF-CASE", rc == 1 and msg == "FAIL: retired skill clause present: " + CF_RETIRED[0] and len(cf_all()) == 1, msg)
for rid, lit, fn in [
    ("R-CF-A18", "never as a subagent, forked agent or workflow agent of PR-30", lambda s: s.replace(" " + T["A18"], "", 1)),
    ("R-CF-NINE", T["NINE"], lambda s: s.replace(T["NINE"] + ".", "", 1)),
    ("R-CF-DISP", "no session is created by an agent", lambda s: s.replace(" No agent merges, and no session is created by an agent.", "", 1)),
    ("R-CF-PROC", "One Proceed per approved per-PR plan", lambda s: s.replace(" " + T["C-PROCEED"], "", 1)),
    ("R-CF-HND", "It carries no branch and no commit", lambda s: s.replace("It carries no branch and no commit: ", "", 1)),
]:
    fresh(); edit("change-flow/SKILL.md", fn); rc, msg = cf()
    rec(rid, rc == 1 and msg == "FAIL: missing skill clause: " + lit and len(cf_all()) == 1, msg)
fresh(); edit("change-flow/SKILL.md", lambda s: s.replace("CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.0", "CHANGE_FLOW_SPECIALIZATION_REVISION: 3.2.9", 1)); rc, msg = cf()
rec("R-CF-REV", rc == 1 and msg == "FAIL: specialization revision", msg)
fresh(); restamp(); v, e, f = suite(); rec("clean-suite", v == "FLOWMASTER_SUITE_PASS" and e == {} and f == [], (v, e, f))
for sk, rid in (("change-flow", "R-OV-1"), ("session-relay-flowmaster", "R-OV-2"), ("tw-flowmaster", "R-OV-3")):
    fresh(); edit(sk + "/SKILL.md", lambda s: s.replace(T["OVERRIDE"], "For every GCFPE stage.", 1)); restamp(); v, e, f = suite()
    rec(rid, v == "FLOWMASTER_SUITE_FAIL" and e == {sk: ["missing specialization contract: " + T["OVERRIDE"]]} and f == [], (v, e, f))
for sk, rid in (("session-relay-flowmaster", "R-TOP-R"), ("tw-flowmaster", "R-TOP-T")):
    fresh(); edit(sk + "/SKILL.md", lambda s: s.replace(" " + T["A18"], "", 1)); restamp(); v, e, f = suite()
    rec(rid, e == {sk: ["missing specialization contract: " + T["A18"]]} and f == [], (e, f))
F4 = ["same-session PR-35 handoff", "preferred live control plane", "launched as a new session", "The Product Owner's PR-40 invocation supplies merge approval"]
for sk, tag in (("session-relay-flowmaster", "R"), ("tw-flowmaster", "T")):
    for i, p in enumerate(F4, 1):
        fresh(); inj(sk + "/SKILL.md", p); restamp(); v, e, f = suite()
        rec(f"R-FB-{tag}{i}", e == {sk: ["superseded contract present: " + p]} and f == [], (e, f))
for sk, o, n, rid in (("session-relay-flowmaster", "3.1.0", "3.0.0", "R-REV-R"), ("tw-flowmaster", "1.2.0", "1.1.6", "R-REV-T")):
    fresh(); edit(sk + "/SKILL.md", lambda s, o=o, n=n: s.replace("_REVISION: " + o, "_REVISION: " + n, 1)); restamp(); v, e, f = suite()
    label = {"R-REV-R": "SESSION_RELAY_FLOWMASTER", "R-REV-T": "TW_FLOWMASTER"}[rid]
    rec(rid, e == {sk: [f"missing specialization contract: {label}_SPECIALIZATION_REVISION: {o}"]} and f == [], (e, f))
shutil.rmtree(W, ignore_errors=True)
total = len(RESULTS); good = sum(ok for _, ok in RESULTS)
print(f"SKILL_REGRESSIONS {good} of {total} exact")
