#!/usr/bin/env python3
"""Generate GUARDS.md from guards.py, the per-guard synthetic evaluation, report.json and guard_tests.json.

Round 2 (P-55, P-61, P-62, P-63): decision labels for G-K24, G-K39 and G-K55; the W-4 coverage (T14) and RS-40 (T15)
results; LPR-30-2 guarded by G-K55; the NAM-002 section as exact EXECUTE commands, with the lane-parent and
parent-title checks and the control run on the old registry."""
import contextlib, io, json, os, re, sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import guards as G  # noqa: E402

with contextlib.redirect_stdout(io.StringIO()):
    import guard_tests as T  # noqa: E402  (re-runs the synthetic suite; prints nothing here)
REP = json.load(open(HERE + "/report.json", encoding="utf-8"))
STRICT = open(HERE + "/strict_tbd.out", encoding="utf-8").read().strip()
GT = json.load(open(HERE + "/guard_tests.json", encoding="utf-8"))
RA = json.load(open(HERE + "/row_assertions.json", encoding="utf-8"))

DEC = {"K08": "P-17", "K19": {"PR-10": "P-06"}, "K26": "P-08, P-42", "K35": {"QA-10": "P-03", "PR-20": "P-02, P-40",
       "PR-50": "P-02, P-40", "*": "P-02"}, "K36": "P-02", "K39": {"RS-40": "P-04, P-62", "*": "P-04"}, "K40": "P-04", "K47": "P-15 (revised)",
       "K52": "P-18, P-42", "K53": "P-38, P-42", "K54": "P-19, P-42", "K14": "P-13", "K22": "P-01 (unchanged)",
       "K50": "P-14 (unchanged)", "K02": "P-05 (rows unchanged)", "K24": "P-61", "K55": "P-55"}
DRY = {  # live-body evidence from the r1 dry runs (plan/r1/dry/*/report.json); keyed by a row of the group
    "K08": {"OPS-10": "dry D: amended + P-17 alternative fires before on OPS-10 (5 sites) and OPS-20 (5), silent after, fires on both OPS injections; the amended pattern alone misses both OPS sites",
            "IA-10": "dry E1: amended fires before on PR-10 (4 sites) and PR-20 (5), silent after, fires on injection; dry F (QA-10): G-K08 fires before, silent after"},
    "K19": {"PR-10": "dry E1: the P-06 fragment fires before (1, the RS-10 package line), silent after; the first-round fragment misses the body",
            "PR-20": "dry E1: R-26-FRAME CHECK 2 before (the LPR-20-6 and LPR-20-7 lines), 0 after"},
    "K21": "dry E1/E2: fires before and is silent after on RS-20; BRANCH-RECV CHECK 1 before, 0 after on PR-35 and RS-40",
    "K22": "dry E1/E2: matches after on PR-35, PR-40 and RS-20 (RECV placed once), fires on removal",
    "K26": {"DOC-10": "dry C: fires 1 before on DOC-10, 0 after", "DOC-20": "dry C: fires 2 before on DOC-20, 0 after",
            "RS-40": "dry E2: the two RS-40 alternatives fire 2 before, 0 after"},
    "K35": {"QA-10": "dry F: the plain P-03 pattern fires before, silent after",
            "PR-20": "dry E1: PR-20's claim is 'Do not mutate the repository ...' (engine OWN_AT corrected)"},
    "K36": "dry B, C, E1, E2: the first-round text failed on every OWN row; the engine places the P-02 text once per row",
    "K40": {"PR-35": "dry E2: R-A5 hits 1 on PR-35 (base text); RS-40 has no A5 sentence, so P-04 drops RS-40"},
    "K47": "dry F tested the first P-15 pattern with the insertion between the sentences; the revised pattern and placement (P-15 revised) are to be confirmed by the re-run, including that QA-110 has one 'Do not fix it here.'",
    "K53": "dry E2 found the phrase in PR-40's RS-20 package (the P-38 finding); R-26-RSP expects 1 hit on PR-40",
    "K54": "dry D (OPS-30): the sentence is deleted and absent after; dry F (QA-10): P-19 twin, 1 hit",
    "K52": "dry B: candidate fires before (package site only), silent after LCL-30-2, fires on its injection",
    "K24": "pass 2 (plan/r1/dry2): the engine places canonical W-4 on every one of the 20 rows (placement W-4 = 2 on OPS-30, "
           "PR-10, PR-20, PR-30 and QA-10; 1 on the 15 CL and S3 rows); W-4 contains this pattern and no line break, so the "
           "pattern matches each edited body. The pass-2 guard check ran G-K24 on the first 5 rows only; on the 15 new rows "
           "it runs at EXECUTE in land.py plan's precheck and land.py check (T14)",
    "K39": {"GCFPE-MGMT-10": "pass 2 (dry2 P4, P5): fires before, silent after and fires on its injection on GCFPE-MGMT-10 and PR-35",
            "RS-40": "P-62: dry E2 found no A5 sentence in RS-40 (P-04), so the guard is silent there and fires if the retired "
                     "sentence comes back (T15); pass 2 ran without it on RS-40, so its live-body check is land.py plan's "
                     "precheck and land.py check at EXECUTE"},
    "K55": "pass 2 (dry2 P4, PR-30): fires before, silent after, fires on its injection",
}


def pick_note(table, gid, rows):
    v = table.get(gid, "")
    if isinstance(v, dict):
        hits = []
        for r in rows:
            if r in v and v[r] not in hits:
                hits.append(v[r])
        return "; ".join(hits) if hits else v.get("*", "")
    return v


def cell(s):
    return str(s).replace("|", "\\|").replace("\n", " ")


def code(s):
    s = str(s)
    return "``" + (" " if s.startswith("`") or s.endswith("`") else "") + s.replace("|", "\\|") + \
        (" " if s.startswith("`") or s.endswith("`") else "") + "``"


def rowdoc(row):
    base = T.CANON_BLOCK_CLAT8 if row in G.CLAT8 else T.CANON_BLOCK
    return base + "\n\n" + "\n\n".join(a for _, a, _ in T.docs[row])


def evaluate(gid, kind, pat, rows, regs):
    n_fire = n_silent = n_match = n_fail = 0
    for row in rows:
        doc = rowdoc(row)
        s = regs[row]
        if kind == "forbidden_regex":
            n_silent += not re.search(pat, doc, re.M)
            n_fire += bool(re.search(pat, s, re.M)) and bool(re.search(pat, doc + "\n" + s + "\n", re.M))
        else:
            n_match += bool(re.search(pat, doc, re.M))
            put_back = re.sub(pat, s.replace("\\", "\\\\"), doc, flags=re.M)
            n_fail += (not re.search(pat, put_back, re.M)) and (not re.search(pat, re.sub(pat, "", doc, flags=re.M), re.M))
    k = len(rows)
    if kind == "forbidden_regex":
        canon = [c[:20] for c in T.CANON if re.search(pat, c, re.M)]
        auth = [src for src, a in T.AUTH if re.search(pat, a, re.M)]
        nc, na = len(T.CANON), len(T.AUTH)
        txt = f"silent on {nc - len(canon)}/{nc} canonical and {na - len(auth)}/{na} authored texts"
        if canon:
            txt += "; fires on canonical C-LAT's decide paragraph (intended: ITEM-37 removes it from these rows)" if gid == "K51" else f"; canonical hits {canon}"
        if auth:
            txt += (f"; fires on the {len(auth)} authored texts that carry the unfilled URL placeholder (intended until EXECUTE fills it)"
                    if gid == "K44" else f"; authored hits {auth}")
        return f"fires on its regression {n_fire}/{k} rows; silent on the after-document {n_silent}/{k}; {txt}"
    return (f"matches the after-document {n_match}/{k} rows; fails when the retired wording replaces the new text "
            f"and when its match is removed, {n_fail}/{k}")


lines = []
A = lines.append
A("# Registry guards — MODIFICATION-20260923-closeout-residuals (PLAN repair r1, round 2)")
A("")
A("Generated by `build_guards_md.py` from `guards.py`, `report.json`, `guard_tests.json` and `row_assertions.json` in this")
A("folder. The machine source for the spec's registry section is `row_assertions.json` (the shape the dry run's")
A("`load_guards()` reads); this page is its readable form. No prompt body was read; every regression below is at most")
A("15 words (P-12).")
A("")
A("## Build")
A("")
src = REP["source"]
A(f"- Base: the live registry `docs/prompt_ecosystem_management/project-prompt-contract-registry.md`, {src['live_bytes']} bytes, "
  f"sha256 `{src['live_sha256']}`; equal to the HEAD blob and to the first-round `registry.head.md`.")
A(f"- `apply_registry.py` builds `registry.new.md` ({REP['new_lines']} lines, sha256 `{REP['new_sha256']}`), ALL_CHECKS_OK = "
  f"{REP['ALL_CHECKS_OK']}; `registry.diff` (unified, against the live file, sha256 `{REP['diff_sha256']}`, "
  f"{REP['diff']['lines']} lines) round-trips through `patch` to the same bytes.")
A("- A TBD guard stops the build: `apply_registry.py --tbd K52` exits 1 with `" + STRICT[:60] + "…` (`strict_tbd.out`).")
A(f"- Assertions: {REP['assertions_total'][0]} → {REP['assertions_total'][1]}. Guard entries added "
  f"{REP['op_counts']['guard entries added']}; 165 release guards replaced in place; 8 required 'Decide it during work' "
  f"entries removed.")
A(f"- Validation: installed governance-audit validator (byte-identical copy) and the r1 final copy both `valid: true`, no "
  f"problems; each of the 55 rows parses alone as YAML and equals the loader's row; the registry deriver "
  f"(`registry_deriver.py` sha256 `{REP['deriver']['sha256'][:16]}…`) reports no drift on the repository parts and on the r1 "
  f"reindexed parts, with both audit copies; 55 rows kept in set and order; lanes change only by the parent map.")
A(f"- Synthetic suite (`guard_tests.py`, Python {GT['T1_python']}): ALL_OK = {GT['ALL_OK']}. T2 {GT['T2_checks_run']} rule/row "
  f"checks, T4 {GT['T4_case_regressions_run']} swapped regressions, T8 {GT['T8_regression_runs']} registry regressions, T12 "
  f"{GT['T12_dryrun_load_guards_runs']} dry-run-format runs, 0 failures; longest regression "
  f"{GT['T8_max_words']['REGRESSIONS']} words (case injections {GT['T8_max_words']['CASES']}).")
_t14 = GT["T14_P61_W4"]
_t15 = GT["T15_P62_RS40"]
_p1 = REP["W-4 required on the 21 ITEM-29 rows"]
_pl = ", ".join(f"{r} {v['pass-2 dry-run placement W-4']}" for r, v in _t14["rows"].items())
A("- Round 2 (DECISIONS P-55 to P-70; review wf_045af16b-3ed):")
A(f"  - P-61: G-K24 (required W-4, CTR-002) is on {len(_t14['G-K24 rows'])} rows, every ITEM-29 row but PR-40: "
  f"{', '.join(_t14['G-K24 rows'])}. PR-40 keeps the parent's G25B `{G.G25B_REQ}` (CTR-002), which canonical W-4 "
  f"satisfies (T14: W-4 matches G-K24 {_t14['W-4 canonical matches G-K24 / G25B'][0]}, G25B "
  f"{_t14['W-4 canonical matches G-K24 / G25B'][1]}); so PR-40 carries no G-K24. `report.json` "
  f"'W-4 required on the 21 ITEM-29 rows ok' = {REP['W-4 required on the 21 ITEM-29 rows ok']}. T14 over the "
  f"{_t14['rows_count']} rows: each row's one W-4 guard matches its document, fails when W-4 is removed and when the "
  f"retired wording replaces it; the engine's R-A7-S1b, R-A7-S2, R-A7-CL and R-A7-S3 new texts all carry canonical W-4; "
  f"pass-2 placement W-4 >= 1 on all 21 ({_pl}); failures {_t14['failures']}.")
A(f"  - P-62: G-K39 (forbidden, the retired storage sentence) is back on RS-40, G-K40 is not "
  f"(`report.json` 'RS-40 carries G-K39 and no G-K40' = {REP['RS-40 carries G-K39 and no G-K40']}; T15 {_t15}).")
A("  - P-55: G-K55's decision label is P-55; it guards LPR-30-2, the last unguarded LOCAL edit at a REAL site.")
A(f"  - P-63: `nam002_live.py` also checks lane parents and parent titles (below); T7 = {GT['T7_ok']}.")
A("")
A("## Guards")
A("")
A("Kind: F = forbidden_regex, R = required_regex. Rule code as placed. A per-row guard lists one table row per distinct")
A("pattern. 'Synthetic result' is computed per row on a document of the 75 canonical texts plus that row's after-texts")
A("(C-LAT's decide paragraph left out on the 8 ITEM-37 rows): a forbidden regression is appended as its own line, as")
A("the dry run injects it; a required regression replaces the new text with the retired wording.")
A("")
A("| id | kind | code | decision | rows | pattern | regression (≤15 words) | synthetic result | live-body evidence (dry run) |")
A("|---|---|---|---|---|---|---|---|---|")
keys = T.KEYS
for gid, rules, part, kind, value, rid, sel in G.GUARDS:
    rows_all = keys if sel == G.ALL55 else list(sel)
    k = "F" if kind == "forbidden_regex" else "R"
    if value == G.TBD:
        A(f"| G-{gid} | {k} | {rid} | {pick_note(DEC, gid, ['CL-30'])} | CL-30 | **TBD** (build refuses); candidate {code(G.CL30_A2_CANDIDATE)} | "
          f"{cell(G.REGRESSIONS[gid]['*'])} | candidate: fires on the pre-edit clause, silent after LCL-30-2, silent on the CL-30 "
          f"document and on every canonical and authored text | {cell(pick_note(DRY, gid, ['CL-30']))} |")
        continue
    groups = {}
    for r in rows_all:
        groups.setdefault(value[r] if isinstance(value, dict) else value, []).append(r)
    for pat, rws in groups.items():
        regs = {r: (G.REGRESSIONS[gid].get(r) or G.REGRESSIONS[gid].get("*")) for r in rws}
        rtxt = sorted(set(regs.values()), key=lambda x: list(regs.values()).index(x))
        rcell = cell(rtxt[0]) if len(rtxt) == 1 else " / ".join(
            f"{', '.join(r for r in regs if regs[r] == t)}: {cell(t)}" for t in rtxt)
        rows_cell = "all 55" if sel == G.ALL55 else ", ".join(rws)
        A(f"| G-{gid} | {k} | {rid} | {pick_note(DEC, gid, rws)} | {rows_cell} | {code(pat)} | {rcell} | "
          f"{cell(evaluate(gid, kind, pat, rws, regs))} | {cell(pick_note(DRY, gid, rws))} |")
for label, rid in G.RELEASE_LABELS:
    pat = G.NEW_HDR + label + G.NEW_END
    regs = {r: G.RELEASE_INJ[label] for r in keys}
    A(f"| PART-17 ({label}) | F | {rid} | P-16 | all 55 (in place of the window guard, same list position) | {code(pat)} | "
      f"{cell(G.RELEASE_INJ[label])} | {cell(evaluate('P17', 'forbidden_regex', pat, keys, regs))}; T6: the three together catch "
      f"{code('**`Prompt version`**: x')} and {code('3. **`Set`**: x')} and stay silent on {code('- Settings: x')}, "
      f"{code('Set up the run:')} and mid-line mentions | dry B/C/D/E1/E2/F: silent on the edited bodies; their injections were "
      f"prose descriptions, now literal label lines |")
A("")
A("Removed on 8 rows (ITEM-37): required `Decide it during work` (CTR-002) on PR-10, PR-20, PR-40, RS-10, RS-20, DOC-10, DOC-20,")
A("IA-30; its forbidden twin is G-K51; the required Material regex stays on all 10 C-LAT rows; PR-30 and PR-35 keep both.")
A("")
A("## Other registry changes")
A("")
pv = REP["parent_value_counts"]
A(f"- PART-10 (ITEM-22): {pv['lane_ids']} lane `notion_parent_id` + {pv['row_ids']} row `expected_parent_id` = "
  f"{pv['lane_ids'] + pv['row_ids']} IDs, and {pv['lane_titles']} lane + {pv['row_titles']} row titles = "
  f"{pv['lane_titles'] + pv['row_titles']} titles, all on the six 091426.1 hubs; {pv['old_ids_left']} old IDs left anywhere in the "
  f"file (PR-35 has no `expected_parent_title`).")
A("- CL-40 `mutations.allowed` gains one entry (ruling 5 Q1 (A)); `forbidden` unchanged:")
A(f"  `{REP['CL-40 mutations.allowed added'][0]}`")
A("- PR-40 `inputs` (P-01; follows the PR-40 body): the PR_REFS entry becomes the LPR-40-4 text, and P-01's sentence")
A("  becomes its own entry right before the W-4 entry, mirroring LPR-40-5 (after the last Inputs bullet, before W-4):")
for x in REP["PR-40 inputs"]["added"]:
    A(f"  - `{x}`")
A("- Rows whose `session_role`, `creator_role` or other fields equal the graph are unchanged (the graph parts carry no")
A("  `inputs`, so the PR-40 input change creates no graph drift; the deriver confirms no drift).")
A("")
A("## Assertions per row")
A("")
A("| row | before | after (draft) | new guard entries | release replaced in place | removed |")
A("|---|---|---|---|---|---|")
for r, v in REP["per_row_assertions"].items():
    extra = ""  # round 2: G-K52 is placed, so CL-30's counts already include it
    A(f"| {r} | {v['before']} | {v['after']}{extra} | {v['new_guard_entries']}{extra} | {v['release_replaced_in_place']} | {v['removed']} |")
A("")

# ---- tail sections ---------------------------------------------------------------------------------------
t10 = GT["T10_P15"]
A("## G-K52 (P-18, P-42): the CL-30 slot")
A("")
A("The task asked for a TBD placeholder that stops the build. DECISIONS P-42 (added after the task was issued) names 'the")
A("CL-30 P-18 guard' among the new guards from the dry run, and P-18 says it is drafted in the dry run from the full read.")
A("Dry run B drafted it (`plan/r1/dry/B/report.json`, `proposed_guard`): forbidden `decision lineage; existing ADR/conflict")
A("history`, TOP-001; on the live body it fires only at the outgoing ADR package (the Next-step sentence joins with commas; the")
A("intake and register sections say 'conflict/ADR') and is silent after LCL-30-2. It is placed. The TBD mechanism stays:")
A("`apply_registry.py --tbd K52` (or `CL30_A2_FORBID = TBD` in `guards.py`) makes the build refuse (`strict_tbd.out`), and")
A("`--allow-tbd` builds a draft without the entry. Synthetic: " + json.dumps(GT["T11_K52"], ensure_ascii=False) + ".")
A("")
A("## PART-10 (ITEM-22): NAM-002, lane parents and parent titles on a live snapshot, EXECUTE procedure")
A("")
A("When: X3.6 (spec §9), after the registry commit (X3.1) and before any Notion write (P-77). A failure here stops")
A("EXECUTE with nothing outside the branch (P-57). Nothing is written to Notion and no prompt body is read: a hub page is a control page, and its child list")
A("gives page IDs and titles only. `nam002_live.py` runs three checks from one `childlist.json` (its docstring states them):")
A("")
A("- NAM-002 (the governance audit's own rule): each row's page is listed under the hub its `expected_parent_id` names.")
A("- Lane parents (P-63): each of the 16 lanes' `notion_parent_id` is the one hub that holds that lane's rows.")
A("- Parent titles (P-63): each of the 70 parent titles (16 lane `notion_parent_title`, 54 row `expected_parent_title`;")
A("  PR-35 has none) equals the fetched title of the hub it refers to. Findings are one per hub, so one wrong hub title is")
A("  exactly one finding.")
A("")
A("1. Fetch the six 091426.1 hub pages with `notion-fetch`, each by ID. From each fetch record the page title, the as-of")
A("   timestamp, and the direct child pages it lists (child page ID, 32 hex undashed, and child title):")
A("")
A("   | hub id | expected title | lanes | rows expected under it |")
A("   |---|---|---|---|")
from collections import defaultdict as _dd
_rows = _dd(list); _lanes = _dd(list)
for _r in T.new["prompts"]:
    _rows[_r["expected_parent_id"]].append(_r["prompt_key"])
for _l in T.new["lanes"]:
    _lanes[_l["notion_parent_id"]].append(_l["lane"])
for _o, _ot, _n, _nt, _ln, _rn in G.PARENT_MAP:
    A(f"   | `{_n}` | {_nt} | {', '.join(_lanes[_n])} | {len(_rows[_n])}: {', '.join(_rows[_n])} |")
A("")
A("2. Write `$SCRATCH/nam002/childlist.json` in the shape the script documents; every hub carries its fetched `title`")
A("   (a hub without one is unusable input, exit 2). Keep every child; a child that is not a registry row does not enter")
A("   the snapshot:")
A("   `{\"captured_at\": \"<UTC>\", \"hubs\": [{\"id\": \"<hub id>\", \"title\": \"<fetched page title>\", \"fetched\": \"<as-of>\", \"children\": [{\"id\": \"<page id>\", \"title\": \"<child title>\"}]}]}`")
A("3. Obtain the pre-change registry for the control run from `$BASE`, the `main` commit X0.2 restarted the branch from")
A("   and recorded (it carries the merged record PR; X0.3(a) checked its registry). Stop if the hash differs:")
A("")
A("   ```sh")
A("   git show $BASE:docs/prompt_ecosystem_management/project-prompt-contract-registry.md > $SCRATCH/reg-old.md")
A("   sha256sum $SCRATCH/reg-old.md   # 8b4e46ed2dc24442e3dadc416dfe4c810a048788bf03c799808927a54c2677d4, 322556 bytes")
A("   ```")
A("")
A("4. Run the four checks. Each run's JSON goes to a file by redirection, not a pipe, so `$?` is the script's own status.")
A("   `--audit-root` is required at EXECUTE: `EV/registry/` carries no copy of the audit scripts.")
A("")
A("   ```sh")
A("   export PYTHONDONTWRITEBYTECODE=1 TMPDIR=$SCRATCH/tmp")
A("   EV=docs/ephemeral/modifications/evidence/closeout-residuals/plan")
A("   AUD=$INST/amthor-workspace-governance-audit")
A("   REG=docs/prompt_ecosystem_management/project-prompt-contract-registry.md   # the working tree after X3.1: sha256 " + REP["new_sha256"][:8] + "…")
A("   CL=$SCRATCH/nam002/childlist.json")
A("   python3 $EV/registry/nam002_live.py $REG $CL --audit-root $AUD --snapshot-out $SCRATCH/nam002/snapshot.json > $SCRATCH/nam002/run1-committed.json; echo \"exit $?\"")
A("   python3 $EV/registry/nam002_live.py $REG $CL --audit-root $AUD --inject ESC-10=3db4590a05eb81d59059eb6b95ed5fcf > $SCRATCH/nam002/run2-inject-parent.json; echo \"exit $?\"")
A("   python3 $EV/registry/nam002_live.py $REG $CL --audit-root $AUD --inject-title 3db4590a05eb81cd938de84cfffead9c=Escalation > $SCRATCH/nam002/run3-inject-title.json; echo \"exit $?\"")
A("   python3 $EV/registry/nam002_live.py $SCRATCH/reg-old.md $CL --audit-root $AUD > $SCRATCH/nam002/run4-control-old.json; echo \"exit $?\"")
A("   ```")
A("")
A("   Expected (each from the run's `summary` and `expectation_met`; any other result stops PART-10):")
A("")
A("   | run | expected summary | `expectation_met` | exit |")
A("   |---|---|---|---|")
A("   | 1, the committed registry | NAM-002 0 over 55 sources; no unplaced row; `other_errors` 0; `lane_parent_findings` 0; `title_findings` 0; `title_references` {compared 70, mismatched 0} | true | 0 |")
A("   | 2, `--inject ESC-10=<Change Flow hub>` (a real hub, the wrong one for ITEM-22's source row) | exactly one NAM-002, on ESC-10 | true | 0 |")
A("   | 3, `--inject-title <Escalation hub>=Escalation` (the hub's pre-091426.1 title) | exactly one title finding, on hub `3db4590a05eb81cd938de84cfffead9c`; `title_references.mismatched` 5 (its lane and 4 rows) | true | 0 |")
A("   | 4, control: the old registry `8b4e46ed…` | NAM-002 55; `lane_parent_findings` 16; `title_findings` 6 (every hub); `title_references` {compared 70, mismatched 70} | false | 1 |")
A("")
A("   NAM-001 (a WARNING on a prompt-title difference) is recorded and does not fail the gate: prompt titles are outside")
A("   PART-10. Runs 2 and 3 are must-fail cases: each checks only its own injected finding, and each passes only when")
A("   that one finding is produced; run 1 must pass first. Runs 2 and 3 cannot be combined (argparse exits 2).")
A("5. Copy `childlist.json`, the snapshot and the four results to `docs/ephemeral/modifications/evidence/closeout-residuals/execute/nam002/`")
A("   (hub and child IDs and titles only; P-83), with each run's exit status, for the X6.4 evidence commit.")
A("")
A("How the script reads the snapshot: `build_snapshot()` makes one source per registry row, `{\"source_id\": <row")
A("notion_page_id>, \"kind\": \"notion_page\", \"complete\": true, \"in_scope\": true, \"title\": <child title>, \"parent\": <hub id>}`.")
A("No source has a `path`, so `_read_snapshot_text` returns None: no text is read, no assertion and no SRC-003 runs.")
A("`audit_governance()` compares `parent` with `expected_parent_id` as a plain string (installed")
A("`audit_workspace_governance.py:604-605`; r1 final copy `:620-621`). A registry page found under no hub is left out")
A("(the audit then raises INV-001, and the run reports it as unplaced); a page listed under two hubs stops the run. The")
A("lane-parent and title checks read the same child lists and the registry fields only.")
A("")
_t7 = GT["T7_NAM002"]
A("PLAN prototype (`guard_tests.py` T7, and the CLI runs in `nam002_proof/`): the child list is built in memory from the new")
A("registry's own parent IDs and titles (`nam002_proof/make_childlist.py`; equal to the ANALYZE parent map), so it is")
A("circular by construction. Results, as NAM-002 / lane-parent / title findings / mismatched title references:")
for _k, _v in _t7.items():
    A(f"- {_k}: {_v['NAM-002']} / {_v['lane_parent_findings']} / {_v['title_findings']} / {_v['title_references']['mismatched']} of "
      f"{_v['title_references']['compared']}" + (f"; NAM-002 rows {_v['NAM-002_rows']}" if _v['NAM-002'] == 1 else "")
      + (f"; title hubs {_v['title_hubs']}" if _v['title_findings'] == 1 else ""))
A(f"- `expectation_met`: {json.dumps(GT['T7_expectation_met'])}; T7 = {GT['T7_ok']}.")
_cm = json.load(open(HERE + "/nam002_proof/cli_matrix.json", encoding="utf-8"))
_codes = {}
for _k, _v in _cm["runs"].items():
    _codes.setdefault(_k.split(" | ", 1)[1], set()).add((_v["exit"], _v["NAM-002"], _v["lane_parent_findings"], _v["title_findings"]))
A(f"- Command line (`nam002_proof/run_cli.py` -> `cli_matrix.json`, ALL_OK = {_cm['ALL_OK']}): the four runs with each of three")
A("  audit roots (the byte-identical `wga_scripts` copy, the installed audit, the r1 final copy) give, as exit / NAM-002 /")
A("  lane-parent / title findings: " + "; ".join(f"{k} " + " or ".join(f"{a}/{b}/{c}/{d}" for a, b, c, d in sorted(v))
                                           for k, v in _codes.items()) + ". Unusable input exits 2: "
  + ", ".join(f"{k} ({v['exit']})" for k, v in _cm["unusable_input"].items()) + ".")
A("Non-prompt findings from the minimal run manifest and workspace registry (" + ", ".join(_t7["new registry"]["non_prompt_findings"]) +
  ") are not prompt findings and do not enter the gate.")
A("")
A("## GUARD-001: the r1 LOCAL edits and their guards")
A("")
A("Anchor-level, from `plan/r1/engine/locals.json` (sha256 `" + GT["inputs"]["r1_engine_locals_sha256"][:16] + "…`): a registry")
A("guard on the row fires on the edit's anchor or shares at least 4 consecutive words with it, and is silent on its new text;")
A("an insertion counts when a required guard matches its new text. An edit whose span runs past its anchor can be guarded")
A("beyond it; the dry run on the live body is authoritative. " + str(GT["T9_local_edits"]) + " edits; 0 guards fire on a new text.")
A("")
A("| edit(s) | guard | evidence |")
A("|---|---|---|")
_cov = [
    ("LPR-10-4", "G-K19 PR-10 (P-06), in the eol span", "dry E1: fires before at this line, silent after"),
    ("LPR-20-6, LPR-20-7", "G-K19 PR-20 fragments, in the eol spans", "dry E1: R-26-FRAME CHECK 2 before (these lines), 0 after"),
    ("LPR-20-8", "G-K08 amended (`Complete RS-\\d+ package`)", "dry E1: amended G-K08 fires before, reads 0 on that line after"),
    ("LPR-40-2", "G-K19 PR-40 `dependency, acceptance and evidence history; completed work`, in the eol span", "CHECK 0 after (dry E2); fires-before per alternative to confirm in the re-run"),
    ("LOPS-10-2, LOPS-20-1", "G-K08 OPS extension (P-17)", "dry D: fires before at 'Complete return to ESC-30', silent after"),
    ("LPR-35-1", "G-K21 `reviews/checks already observed, unresolved items`, in the eol span", "dry E2: BRANCH-RECV CHECK 1 before, 0 after"),
    ("LCL-30-2", "G-K52 (P-18, P-42)", "dry B: fires before, silent after"),
    ("LOPS-30-1, LQA-10-P19", "G-K54 (P-42)", "dry D and F: the sentence is removed; guard fires on it and not on the section after"),
    ("LDOC-10-1, LDOC-20-1, LDOC-20-2", "G-K26 (DOC fragments appended, P-08, P-42)", "dry C: 1 before on DOC-10, 2 on DOC-20, 0 after"),
    ("LPR-20-5, LRS-40-3", "G-K23 ('Nathan's ... invocation asserts')", "on all 55 rows"),
    ("LRS-40-2", "site level only: G-K23 through LRS-40-3 in the same MERGE_PENDING bullet", "T13: no row guard fires on its phrase alone; G-K23 fires on the pre-edit bullet"),
    ("LCF-C/E-20-2, LCF-C/E-30-3, LCF-C/E-40-3", "none: each inserts the frame close '; the artifacts hold the rest'", "nothing retired to forbid; the sentence's retired content is guarded by G-K19 through its sibling replace edit (LCF-*-20-1/-20-3, -30-2, -40-2)"),
    ("LCF-C/E-30-1, LCF-C/E-40-1", "site level: the same sentence's G-K19 fragment, edited by LCF-*-30-2 / -40-2", "no guard on the head verb itself"),
    ("LPR-30-2", "G-K55 (P-55)", "fires on the anchor, silent on the new text (below)"),
    ("LGCFPE-MGMT-10-PROPOSED-1", "not a registry row", "PART-11 gate"),
]
for _e, _g, _v in _cov:
    A(f"| {_e} | {cell(_g)} | {cell(_v)} |")
A("")
_cand = {"PR-30": r"outside the approved Plan, return the metadata\b"}
_inj = {"PR-30": T.LX["LPR-30-2"]["anchor"]}
A("G-K55 (P-55), placed on PR-30; it was the one LOCAL site at a REAL site that no guard reached:")
A("")
for _rw, _p in _cand.items():
    _fire = bool(re.search(_p, _inj[_rw]))
    _silent_new = not re.search(_p, T.LX["LPR-30-2"]["new_text"])
    _clean = not any(re.search(_p, t_) for t_ in T.CANON + [a_ for _, a_ in T.AUTH])
    _code = next(g[5] for g in G.GUARDS if g[0] == "K55")
    A(f"- {_rw}: forbidden {code(_p)} ({_code}): fires on the anchor {_fire}; silent on the new text {_silent_new}; silent on "
      f"every canonical and authored text {_clean}.")
A("")
A("## Conflicts and open points")
A("")
A("1. **G-K47 (P-15 revised) is not site-scoped.** `Do not fix it here\\.(?! This applies ...)` fires on any other 'Do not fix")
A("   it here.' in QA-110 (T10: " + json.dumps(t10["G-K47 on a second, unrelated 'Do not fix it here.' line (fires: the pattern is not site-scoped)"]) + " on a")
A("   synthetic second line). Applied as written; the re-run must read G-K47 = 0 on the edited QA-110. If it does not, the")
A("   site-scoped variant " + code(t10["site-scoped variant"]) + " fires before, is silent after and ignores other lines (T10).")
A("   The first-round placement (between the sentences) would fail the revised pattern; the r1 engine uses the revised one.")
A("2. **G-K52 filled** from the dry run under P-18/P-42, though the task asked for TBD (above); one flag restores the refusal.")
A("3. **G-K26 stays one alternation on its 6 rows** with the DOC fragments appended (P-42), not split per row. RS-40's")
A("   LRS-40-2 phrase is guarded only through its bullet (G-K23 on LRS-40-3's phrase, T13).")
A("4. **G-K19 alternatives outside the engine CHECK.** PR-20's `current stage and suspended boundary, ...` and PR-40's `all")
A("   completed review work; attempts; limitations` are not in the r1 R-26-FRAME CHECK, and PR-40's second fragment is")
A("   shortened there. If absent from the live bodies they are silent, dead alternatives; not changed (no decision).")
A("5. **PR-40 input.** 'with P-01's sentence' is read as: the PR_REFS entry follows LPR-40-4, and P-01's sentence is its")
A("   own entry before W-4, mirroring LPR-40-5. If only the PR_REFS change is meant, drop the one inserted line. P-37 keeps")
A("   the CANON_CONFLICT_REGISTER intake entry, and it is untouched.")
A("6. **G-K21** stays one 4-row alternation (the per-row split was decided for G-K35 only).")
A("7. **Release-line checks** agree: the three PART-17 patterns are the per-label split of R-ITEM23's single pattern, which")
A("   equals the r1 engine's `RELEASE` string (T6). flowmaster-validate's `PROMPT_BODY_RELEASE_HEADER` is the skills")
A("   package's to align (P-16).")
A("8. **Dry-run re-run.** The dry runs so far used the first-round guard file (prose PART-17 injections, first-round G-K36,")
A("   G-K40 on RS-40, no G-K52..54). `dryrun.py`'s defaults now read this folder's `row_assertions.json` and `registry.new.md`.")

open(HERE + "/GUARDS.md", "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("GUARDS.md lines:", len(lines))
