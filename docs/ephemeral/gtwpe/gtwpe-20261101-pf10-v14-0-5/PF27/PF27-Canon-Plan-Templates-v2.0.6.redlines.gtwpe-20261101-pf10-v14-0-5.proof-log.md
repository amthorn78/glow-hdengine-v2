# Proof log: PF27-Canon-Plan-Templates v2.0.6 redlines, run gtwpe-20261101-pf10-v14-0-5 (task T-07)

## 1. Artifact and identity

| Field | Value |
| :---- | :---- |
| Artifact this log documents | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF27/PF27-Canon-Plan-Templates-v2.0.6.redlines.gtwpe-20261101-pf10-v14-0-5.md` |
| This proof log | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF27/PF27-Canon-Plan-Templates-v2.0.6.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md` |
| Run identity | `gtwpe-20261101-pf10-v14-0-5/T-07/prep-r3` |
| Revision | `prep-r3` supersedes `prep-r2` (commit `bf5bb084b1581ac39c64f93be8ea29b1112549ca`, applied as `apply-r1` in commit `4a033d4b4115ff2e5817c5e3f2c9b44d4102a862`), after the Product Owner ruled CCR-5 on 2026-11-02 (§2). `prep-r2` superseded `prep-r1` (commit `7061dc8ad82e30128b1902ab125cbbb764b71aea`, never applied). §12 records both corrections. |
| Originating preparer | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1, Notion page `3f44590a05eb8172a314fe6b958bb9ff`, fetched live at the start of each preparation step, the last time for `prep-r3` (page last edited 2026-10-09T11:05:22Z, unchanged), run in the Claude Code cloud session https://claude.ai/code/session_01Q789tyeqMDbVqbUtqxA64b, which Nathan started for T-07 on 2026-11-02. No subagent, reviewer or other session took part. |
| Authorized step sequence | Nathan's handoff authorizes TW-DRAIN-10, then TW-APPLY-10 100926.1 (Notion page `3f44590a05eb81eebff6e3afa3d9aa5b`) in this same session after a READY / COMPLETE_PACKAGE result. `prep-r3` and its application follow the Product Owner's ruling given in this session after `apply-r1`. |
| Preparation outcome | `READY` |
| Save outcome | Recorded in §13 after both files were read back. |
| Correction route | An Apply diagnostic returns to this preparer, in this session, under a new revision identity (`prep-r4` and later). |

## 2. Inputs and source roles

| Input | Identity | Role |
| :---- | :---- | :---- |
| Target (original) | `docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.6.md`; in-document title `PF27-Canon-Plan-Templates`; version v2.0.6; Status Canon; Effective date 2026-10-26; git blob `c21096d78b9865bf5aa0c531eee701e462d71a50`; SHA-256 `850dc1a3c8294a0e0521f02cb7300fb05233beccb1ecadf611b41e8ea9adfb00` over the whole blob; 323,765 bytes; 3,938 lines; LF endings | The one current PF27 Markdown under `docs/pfcanon/` on `main`. Baseline `origin/main` `e2b7427ff418ca8f08f05587c4a541308a76da56`. At `prep-r3`, `origin/main` was `84d6d1cf`; its two later commits (amthorn78/glow-hdengine-v2#824 and amthorn78/glow-hdengine-v2#825) touch only `docs/ephemeral/HDE-M10V2-*` files and leave PF27 and PF10 byte-identical (same blobs). |
| Change source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`; HDE Build Notes v14.0.5, effective 2026.11.01; git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`; 385,734 bytes; 1,976 lines | The only substantive change source. One unlettered logical version. |
| Product Owner ruling (decision, not a change source) | Nathan, in this session, 2026-11-02, after reading the `apply-r1` report's observation that R-3 and §3B stated different orderings: "close pack should go after the decision to close is confirmed" | Rules CCR-5 (addendum 2.5, line 856) as its alternative (A): R-3 stands as written, the closure decision precedes the close-pack write, and the permanent documents are drained to match. It resolves the conflict that held §3B (H-06) and is recorded here, quoted, as TW-DRAIN-10 requires of a material-conflict decision. The change source for the §3B redlines stays 2.2 R-3. |
| Editorial standard | `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md`; blob `504712df548a02f3aa4e7b8c37027385e46a3878`; SHA-256 `df685f3a66aa18fdcacb697b340263cb59fc682564fa59c50b3d9b9ca735c462`; 633 lines | Read in full (lines 1–633). Applied to authored wording only; not a change source. |
| Governing decision | `docs/prompt_ecosystem_management/gtwpe/gtwpe.decision-record.md` (blob `1c65c85339cb`, the same on `main` and on the branch), GTWPE-D3 "Every PF10 addendum is drained, and a prompt in the run evaluates the drain targets", read in full (lines 114–170), with GTWPE-D4 (172–226) | Nathan's standing ruling: "all pf docs should be updated based on context and scope, not whether or not the addenda specify a drain target"; "No document is gated on a drain target or a specification, PF20 and PF30 aside. Every eligible document is updated on context and scope, PF27 among them"; a change is already represented only on a pass's verified finding. It decides how the selected units map onto PF27. |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md`: the handoff pins `142feb35144d8795f927e0c78b665ace52279064`; also read at later branch heads, the last at `4967dc4`. They add the 2026-11-02 correction banner, §8 (T-11 to T-18) and other tasks' completion rows. T-07's task row, its rows C-02, C-08, C-09, C-26 (supporting C-06) and the H-06 and H-07 rows are unchanged. | Routing and provenance only. Not a change source and not a Last Update Gate. Its banner quotes Nathan's 2026-11-02 direction: "Just because there is not routing in a sections is NOT grounds for exclusion. You are supposed to analyze by context." |
| Supporting canon (read, not drained) | `docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.8.md` (blob `0c3ce100f942`), §3.4 "Open rails (controlled)", lines 1171–1243, read in full; `docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.4.md` (blob `53e6a9028dfa`), §7.1.10 "Endpoint policy (explicit version-gated dual lineage)", lines 3472–3504, read in full | Ownership checks for the routing sentences in RL-01, RL-04, RL-08 and RL-09. Neither is edited. |
| Handoff | Nathan's inline handoff of 2026-11-02 ("GTWPE document session — T-07 — Plan Templates (drain, then apply)") | Control instructions: target, selected units, holds, branch, outputs, the decision to drain 2.2 R-3 as written, and the instruction to keep the Live QA Plan template's own placeholders. |

## 3. Coverage

Target. Read completely, lines 1–3938, in twelve recorded windows (line range, bytes): 1–300 (28,897); 301–600 (22,102); 601–900 (33,849); 901–1060 (20,092); 1061–1200 (39,350); 1201–1385 (27,843); 1385–1599 (22,612); 1600–1899 (22,292); 1900–2269 (29,228); 2266–2705 (19,284); 2706–3225 (19,933); 3226–3938 (38,388). The windows overlap at lines 1385 and 2266–2269 and leave no gap. Every window ended at a complete line; the last ends at the file's final LF.

Context scan of the target: exact-term searches of the whole target for each selected rule's terms, then a read of every hit's section from the full reading above. For D-2: `fallback`, `bodygraphs`, `PROVIDER_ROUTE`, `terminal`, `route famil`, `base URL`, `/v1`, `/v2`. For 2.2: `docs/ephemeral`, `planning document`, `version`, `file name`, `digest`, `SHA-256`, `pin`, `close-pack writer`, `close pack`, `full validation`, `required PR CI`; for `prep-r3`, also `DO_NOT_CLOSE`, `close mutation set`, `closure decision`, `close pull request`, `CL-05` and `CL-E-10`. For 2.15: `Live QA`, `live vendor`, `live test`, `open-rails`, `open rails`, `closed-rails`, `exempt`, `waive`, `synthetic`, `showcompat`, `/internal/version`, `TOOLING_BLOCKED`, and each template's verdict, decision and record-field blocks. §5 gives each finding.

Selected source units, each read completely (PF10 lines):

| Unit | Lines | Row |
| :---- | :---- | :---- |
| 2.1 heading, timestamp, "Decision and approval status" | 205–224 | C-06 |
| 2.1 D-1 (read in passing; not selected) | 225–276 | none (C-01, not T-07) |
| 2.1 D-2 | 277–344 (205–344: 13,633 bytes) | C-02 |
| 2.1 "Scope, exclusions and nonclaims", "Dependencies and unresolved obligations", "Evidence" | 491–516 | C-06 |
| 2.2 heading, "Decision and approval status", "The defect that prompted it", R-1, R-2 | 517–546 | C-08 (R-1 is C-07, see §5) |
| 2.2 R-3 | 547–551 (491–551: 7,237 bytes) | C-09 |
| 2.15 heading to R-6 | 1650–1804 (11,087 bytes) | C-26 |

Supporting reading, labeled as such and not drained: 2.2 lines 552–588 (6,048 bytes; line 581 names the Plan Templates drainage targets); 2.5 lines 765–780 and line 856 (R-3 governs as written; CCR-5 and its alternatives (A) and (B)); 2.9 lines 1150–1170 (line 1161: the CCR-5 ruling bounded to HDE-EPIC041); 2.15 lines 1805–1868 (4,159 bytes; the CRD exclusion at lines 1825 and 1835 and the drainage target list at lines 1845–1849); 2.16 R-3, lines 1936–1950. No unrelated addendum was read to rebuild triage.

Coverage state: complete for the target and for every selected unit.

## 4. Redlines prepared

Eighteen `REPLACE` operations. IDs RL-01 to RL-15 keep their `prep-r2` meaning (RL-10's Exit text is revised); RL-16 to RL-18 are new in `prep-r3`. The redlines file lists them in ID order; its batch table lists them in original order. Sixteen replace one unique original line; RL-08 replaces lines 1450–1453 and RL-16 lines 2226–2227, each as one region.

| Redline | Row | Target location (original line) | What it does | Source basis |
| :---- | :---- | :---- | :---- | :---- |
| RL-01 | C-02 | "Purpose & scope" > "Exact technical facts and secret safety", row "Version literals" (112) | Adds the configured base's terminal `v1` or `v2` classification, owned by HDE CLI/API/Vendor Ref §7.1.10, to the closed list of classifications under which a plan may show a version literal. | D-2, lines 290–297 and 313 |
| RL-02 | C-08 | "Purpose & scope" > "Canon precedence for template use" (287) | Adds R-2's premise that PF versions and file names may change; keeps the title-only rule for HDE Build Notes and adds its reason; requires other PF references by current title, section where needed, never file name or version; applies the rules to an ADR a derived artifact carries; keeps the provenance sentence and states that a derived artifact that must remain valid pins no PF file name, version or digest. | 2.2 R-2 bullets 1, 2 and 4 (lines 542, 543, 545); line 581 |
| RL-03 | C-26 | §1 "Live QA Plan" > "Front matter" (326) | Adds the template field `Live test:` with RAN, WAIVED and MISSING, using allowed `<PLACEHOLDER>` markers for the evidence references and for the Product Owner's quoted words and date. | 2.15 R-4, lines 1763–1771 |
| RL-04 | C-26 | §1 "Live QA Plan" > "Open-Rails Live QA Requirement for production-affecting epics" (389, its last line) | Appends a new H3 "Live compat test for every Epic (required)": R-1's live compat test (live vendor compat and deployed-service check, pass predicates, findings, SYN-A and SYN-B, the own-surfaces step, what does not satisfy it); the CRD boundary; routing of execution, controls and the Ops-evidence posture to HDE Governance §3.4 (R-6); the blocked-live-test rule (R-5); the Product Owner-only waiver (R-2); the live-test line for the plan and its review with the approval block (R-4); and the naming rule (R-3). | 2.15, lines 1666–1681 and R-1 to R-6 (1704–1803); supporting 1825, 1835; target at 1849 |
| RL-05 | C-26 | §1 > "Close-out deliverables" > "What “QA RCA & Doc Delta summary” means" (973) | Adds a content bullet: the summary carries the live-test line and, with MISSING, gives no PASS verdict. | 2.15 R-4, lines 1769 and 1780 |
| RL-06 | C-26 | "Review guardrails" > "Hard blockers for plan approval/execution", bullet "Valid Live QA Plan approval blockers" (1168) | Adds "a missing live compat test with no recorded Product Owner waiver (a `Live test:` line that reads `MISSING`)" to the closed list of valid approval blockers. | 2.15 R-4, lines 1777–1778 and 1784 |
| RL-07 | C-09 | "Review guardrails" > "CI lane classification and automated budget-control discipline" (1312) | Adds R-3 as written as a new paragraph after the administrative-closeout paragraph. | 2.2 R-3, lines 549–550; line 581 |
| RL-08 | C-26 | §2 "HDE-EPIC-Specification" > "Epic Record Template (Normative)" > "Contract and Compatibility Posture (MUST)" (1450–1453) | The "Open-rails QA declaration", "Implementation preservation" and "Review posture" bullets also carry the live compat test every Epic's QA runs, waivable only by the Product Owner; the production-functional and broader open-rails rules stay as written; "Open-rails triggering surfaces" (1451) is unchanged inside the region. | 2.15, lines 1666–1681, 1706, 1743, 1777 |
| RL-09 | C-02 | Same section, bullet "`bg:resolve --source vendor` route-policy posture" (1459) | Keeps the four categories and adds that "explicit legacy fallback" reads as the terminal-v1 legacy selection, which is not a fallback, and routes route selection and the configured-base boundary to HDE CLI/API/Vendor Ref §7.1.10. | D-2, lines 288, 316, 323 |
| RL-10 | C-26, C-09 | §3B "Close Mutation Set Task Record (Template)" > "Record fields (required)" (2261) | The Exit field becomes the Product Owner's merge of the close pull request (revised in `prep-r3`), and the record gains the field `Live test:`; with MISSING, the close mutation set is not close-PR-ready. | 2.15 R-4, lines 1770 and 1781; 2.2 R-3 line 549 under the CCR-5 ruling |
| RL-11 | C-26 | §8 "QA Pass Review Record" > "Required structure (paste-ready)", Review Summary (3120) | Adds a conditional field: when the record is the run's QA evidence review, it carries the live-test line, and with MISSING the evidence is not acceptable. | 2.15 R-4, lines 1768 and 1779 |
| RL-12 | C-26 | §9 "Final QA Closeout Review + QA RCA" > "Scope" (3218) | Adds the first-line rule: when no live test ran, the report's first line is `No live test ran.` and it names the waiver or the missing test. | 2.15 R-3, line 1759 |
| RL-13 | C-26 | §9 > "Required structure (paste-ready)", QA Closeout Summary (3232) | Adds the field `Live test:` after "Epic reviewed". | 2.15 R-4, line 1769 |
| RL-14 | C-26 | §9 > "Required structure (paste-ready)", QA Verdict and Recommendation (3447) | Keeps the four verdict values and adds "(not PASS when the live-test line reads `MISSING`)". | 2.15 R-4, line 1780 |
| RL-15 | C-26 | §10 "Epic Closure Review + Retrospective" > "Required structure (paste-ready)", Closure Decision (3560) | Adds the field `Live test:`; with MISSING, the closure decision is not CLOSE. | 2.15 R-4, lines 1771 and 1782 |
| RL-16 | C-09 | §3B > "Entries and exit (normative)" (2226–2227) | Entry: a closure decision of `CLOSE`; the close mutation set, the close pack included, is written only after that decision confirms the close. The `DO_NOT_CLOSE` entry is removed. Exit: the Product Owner's merge of the close pull request. Line 2228 is unchanged. | 2.2 R-3 line 549; CCR-5 (A), Product Owner ruling of 2026-11-02 |
| RL-17 | C-09 | §3B > "Authority and actor (normative)" (2239) | The task starts only after the closure authority (Isis) has decided to close the change and does not revisit that decision; the Product Owner alone merges. | Same |
| RL-18 | C-09 | §3B > "Record fields (required)", Entry (2255) | Entry field: the closure decision of `CLOSE` for the change, by exact source. | Same |

Change-type classification (report labels only): RL-01 and RL-06 CONSISTENCY; RL-02 CANON_UPDATE with CONSISTENCY; RL-03, RL-04, RL-05, RL-07 and RL-11 to RL-15 NEW_CANON; RL-08 CANON_UPDATE; RL-09 CLARIFY; RL-10 NEW_CANON with CONSISTENCY; RL-16 to RL-18 CONSISTENCY. RL-01, RL-06, RL-08 and RL-10 to RL-15 are context drainage under GTWPE-D3. No DOC_HYGIENE or DELETION redline is prepared; RL-16 removes the `DO_NOT_CLOSE` entry inside a `REPLACE`, on the ruling.

## 5. Change and disposition ledger

Every change in the selected units, with its disposition and, where no change is made, the verified finding and its location.

**2.1 D-2 (C-02), lines 277–344**

| Element | Disposition |
| :---- | :---- |
| "What governs", "Selection", "The base", "No fallback" (281–289) | Owned by HDE CLI/API/Vendor Ref §7.1.10, which already states the selection, the configured-base boundary and "retained legacy selection, not fallback" (supporting reading). RL-09 routes to it. |
| "The v1 path is retained legacy selection, not fallback" (288) | RL-09. |
| The single permitted classification; contract metadata; the remaining prohibitions (290–297) | RL-01 for the "Version literals" row (112). The rows "Active resource paths" (111) and "Authentication selection" (113) already agree: the configured base owns the version boundary, and authentication comes from contract or route metadata, never from `/v1` or `/v2` string inspection. Verified, no change. |
| Classification label `explicit_legacy_fallback` (298) | RL-09 keeps the PF27 category name, matching D-2's choice to keep the label unchanged. |
| Basis (300–308) | Explanatory. No change. |
| Supersession of HDE Mechanics Guide, HDE Users Guide, HDE CLI/API/Vendor Ref (312–315) | Other targets (T-05, T-08, T-02). |
| Plan Templates route-policy category (316) and drainage target (323) | RL-09. |
| AGENTS.md (324) | H-05. Not a PF target. |
| Consequences for tests and evidence (328–339); v1 retirement left undecided (343) | No PF27 content bears on them. RL-09 says nothing about retirement. |
| Other PF27 text on fallback and the base | Verified, no change. "Future proof requirement" (1458), "Route-family proof requirement" (1462) and "Mapped-cache proof requirement" (1470) ask a plan to state what fallback remains; while Candidate CRD Items List item 9 is open, D-2's basis (304–305) records that the current classifier still reaches the legacy route from non-v1 bases, so the question stays live. "Base URL key" (110) and the Check Blocks preflight (776) are presence-only; the base-boundary contract stays with HDE CLI/API/Vendor Ref §7.1.10, and stating its fail-closed behavior as current would claim a delivery that item 9 has not made. |

**2.1 context (C-06), lines 205–224 and 491–516**: supporting. D-2 takes effect as canon on publication (line 211), so RL-01 and RL-09 do not wait for item 9 (H-10). Neither states implementation state. The scope, nonclaims and evidence are not drained.

**2.2 (C-08, C-09), lines 517–551**

| Element | Disposition |
| :---- | :---- |
| Heading, timestamp, decision (517–523) | Context. |
| "Status. Proposed." (524) | Not drained. v14.0.5 publishes the addendum, so its rules are active (ledger §2 status reading). |
| Relation to other canon (525) | Context. |
| The defect that prompted it (527–531) | History. No change. |
| R-1 (533–538), row C-07 | Context scan, verified no change: no PF27 template makes code, a test, a tool, CI, a workflow, a schema, a governed artifact, a close pack, a manifest, an Index or Mirror row or a path proof read or bind a path under `docs/ephemeral/`. The close report and manifest fields (1744–1773) bind close-pack artifacts and governed evidence; §3B's record fields (2250–2262) bind the close pack, its ledgers and same-run evidence; "Canon precedence for template use" (283–285) places derived documents under `docs/ephemeral/` without making anything depend on them; the Live QA Plan provenance lock (888–906) governs plan text, which R-1 permits (a prose citation of a planning document is a reference only). |
| R-2 bullet 1, versions may change (542) | RL-02. |
| R-2 bullet 2, no pin (543) | RL-02. Context scan, verified no other change: no template asks for a PF file name, version or digest; the step-log header's `pf_refs` takes exact in-document titles (571); the Live QA canon set is titles-only (334); §12's governing-source map is title-only for HDE Build Notes (3861). |
| R-2 bullet 3, tool resolution; validation does not re-read canon (544) | Tool behavior. No PF27 template defines a tool's canon resolution. Verified, no change. |
| R-2 bullet 4, citations (545) | RL-02. |
| R-3 bullet 1, the writer writes only at close, after the QA verdict and the closure decision exist (549) | RL-07, as written. In §3B, under the Product Owner's CCR-5 ruling: RL-16 (Entries and exit), RL-17 (Authority and actor), RL-18 (Entry field) and RL-10 (Exit field). Context scan, verified no other change: §3B "Definition" (2222) states no ordering; "Close-tooling repair" (2241–2248) names the writer's owner tests without placing them in a CI lane; §10's closure review "MUST NOT require a pre-existing close report, close manifest, or equivalent decision-restatement artifact" (3459), which agrees with the ruling; §10's "Open closure items or questions for the Lead" (3617) lists close-pack baseline existence among decisions before PO closeout, which follows the closure decision and so agrees; Spec Preflight B (1733–1749) lists close-pack artifacts for the close stage without ordering them, and stays held as H-07. See O-4 for the §1 summary location. |
| R-3 bullet 2, the writer's test is a close-stage test (550) | RL-07. |

**2.15 (C-26), lines 1650–1804**

| Element | Disposition |
| :---- | :---- |
| Heading, timestamp, decision (1650–1664) | Context. |
| "Status. Proposed." (1665) | Not drained (ledger §2 status reading). |
| Relation to other canon (1666–1681) | RL-04 and RL-08: the minimum live test no longer depends on a touches-production finding. The preserved controls are routed to HDE Governance §3.4. |
| The failure that prompted it (1683–1702) | HDE-EPIC041 history. Not drained into PF27 (ledger C-27 and T-10). |
| R-1 (1704–1739) | RL-04 (all elements, with UUIDs, derivations, birth data, write path and authorization, and the missing-fixture rule); RL-08 for the Epic Specification. The Ops task that stores SYN-A and SYN-B is history and is not named in the template. The §1 Open-Rails subsection (363–389) stays as the template's statement of HDE Governance §3.4 for the Epic's own surfaces. |
| R-2 (1741–1753) | RL-04 "Waiver (Product Owner only)"; RL-08 ("only the Product Owner may waive the test or any part of it"). The exemption text that stays in §1 (385) and §2 (1450) governs the Epic's own production-affecting surfaces under HDE Governance §3.4, which R-1 (1726) keeps governing. |
| R-3 (1755–1759) | RL-04 naming rule; RL-12 first-line rule in §9. Context scan, verified no change: §2 "Live QA requirement (closeout statement only)" (1627–1634) states that Live QA is required for close, which R-3 now gives its meaning; the template name "Live QA Plan" and the other uses of "Live QA" describe QA that R-1 requires to include the live test. |
| R-4 live-test line (1763–1771) and table (1774–1782) | QA plan: RL-03, RL-04. Plan review: RL-04, RL-06. QA evidence review: RL-11 (conditional). Final QA report and RCA: RL-05 (§1 summary), RL-13, RL-14 (§9). Close mutation set result: RL-10 (§3B). Closure decision: RL-15 (§10). QA readiness, the QA task set and the QA execution result have no PF27 template: PF27 has no readiness or task-set template, and its step-log header and step-logs manifest are governed per-check evidence, not the run's result record. Verified, no change. |
| R-4 "Who may override" (1784) | RL-04 ("No agent may override this block"), RL-06. |
| R-4 prompts (1785) | Prompt instruction, not template text. Owner GCFPE management (H-11). Not drained. |
| R-5 (1787–1790) | RL-04, blocked-live-test paragraph. |
| R-6 (1792–1803) | RL-04 routes execution and controls to HDE Governance §3.4 and states that the live test's result is Ops evidence there. The §1 Open-Rails subsection's control list (369–383) stays. |

**Supporting units**: 2.9 line 1161 records the CCR-5 "(B) now, bounded" ruling for HDE-EPIC041 only; it is history and is not drained as a general rule. The Product Owner's 2026-11-02 ruling selects (A) for the general rule. 2.16 R-3 (1940–1948) records that SYN-A and SYN-B are stored and registered; RL-04 states the requirement and the missing-fixture rule and makes no claim about current storage.

## 6. Held items

| Hold | What is held | Status in `prep-r3` |
| :---- | :---- | :---- |
| H-06, CCR-5 | §3B "Entries and exit (normative)" (target lines 2224–2228) and the §3B text that follows from it | Released for PF27 by the Product Owner's ruling of 2026-11-02 (§2) and drafted as RL-16, RL-17, RL-18 and RL-10. The same ruling bears on Change Process Guide §3.5.1 (T-03) and Glow QA Guide §3.1.3 (T-06), which those tasks held as H-06 and this task does not edit (O-1). |
| H-07, CCR-1 / P-2 | Spec Preflight B "Close-pack baseline declared (planning gate)", which lists the acceptance map (target lines 1733–1749). Unchanged. | Still held. It waits for the Product Owner's decision whether a tokenless Epic needs an acceptance map (2.10 line 1299). No source text exists to drain. |

## 7. Outside dependencies

None blocks this package.

* The concurrent T-01 (HDE Governance), T-03 (Change Process Guide) and T-06 (Glow QA Guide) drains of 2.15 are not inputs. RL-04 and RL-08 cite HDE Governance §3.4 for the existing open-rails requirement, exemption content and execution controls, which §3.4 already states in v2.8.8 (lines 1192–1206).
* Candidate CRD Items List item 9 (H-10) is open. RL-01 and RL-09 do not depend on its delivery (§5, C-06).
* The §3B redlines do not depend on a new HDE Build Notes addendum: under alternative (A), R-3 stands as written and is the source.

## 8. Constraints, assumptions and interpretations

* Mapping by context. GTWPE-D3 decides that no document is gated on a drain target. The selected source units are the handoff's; their mapping onto PF27 sections is by context and scope. The ledger's section anchors ("bg:resolve --source vendor route-policy posture", "Canon precedence for template use", "CI lane classification", §1 "Live QA Plan") and 2.15's own drainage list (1849) locate changes but do not limit them.
* The CCR-5 ruling and §3B. "Close pack should go after the decision to close is confirmed" places the close mutation set after a closure decision of CLOSE, which is R-3's first bullet as written. Four consequences follow in §3B and are drafted as such. The entry is that decision (RL-16, RL-18). The `DO_NOT_CLOSE` entry is removed, because it existed only for a closure decision that judged a missing, incomplete or defective close mutation set, which the closure decision no longer judges (RL-16). The exit becomes the Product Owner's merge of the close pull request, which §3B "Dev, not Ops" (2232) already names as the point where the task's work lands (RL-16, RL-10). The closure authority no longer judges the task's result at the closure decision (RL-17). "The task never reopens implementation, QA, or the closure decision" (2228) and the Nonclaims field (2262) stay.
* Redline format. TW-DRAIN-10 requires literal fenced payloads; PF03 §8 says "When the operator supplies a redline format, follow it exactly", so its no-fence default does not apply to this redlines file. No fence enters PF27.
* New heading style. RL-04's heading has no outer bold, as PF03 §8 "Structure and presentation" requires. Most PF27 headings are bold-wrapped; §3B's are not. PF27's review guardrails treat heading styling as non-material.
* Placeholders. The existing template placeholders are kept unchanged, as the handoff requires. RL-03 adds only allowed `<PLACEHOLDER>` markers ("Template-safe placeholders and omission syntax"). RL-14 keeps the four verdict values.
* RL-04 placement. The new H3 follows the last line of the Open-Rails subsection (line 389) and precedes its `---` rule, so no existing heading, title or order changes. Line 389 belongs logically to the empty H4 "PF10 overrides / conflicts (if any)" at line 361, which the Open-Rails H3 at line 363 separates from its content; that pre-existing structure is unchanged.
* Record mapping for R-4. The final QA report and RCA maps to §1's QA RCA & Doc Delta summary and to §9; the close mutation set result to §3B's record; the closure decision to §10's Closure Decision. §8 reviews a check or check cluster, so its field is conditional on the record being the run's QA evidence review.
* CRD boundary. 2.15 excludes CRDs (1835) and leaves to the Product Owner whether a runtime-changing CRD runs the R-1 test (1825). PF27's CRD profile reuses this template with CRD substituted for Epic, so RL-04 states that reuse for a CRD does not by itself apply these rules. RL-08 is inside the Epic Specification template.
* RL-09 wording. D-2 says the category "reads as" the terminal-v1 legacy selection and keeps the matching evidence label unchanged, so the category keeps its name and gains its reading.
* Citation form. New text names other PF documents by their in-document titles (`PF04-Canon-HDE-Governance`, `PF05-Canon-HDE-CLI-API-Vendor-Ref`) with a section, and HDE Build Notes is not cited by addendum, consistent with PF03 §3 "Canonical ownership" and with RL-02.
* Pronouns. The source refers to the Product Owner as "he"; the drafted text names the role instead.
* Not a current-state claim. No redline states current repository, deployment or QA state.

## 9. Observations for Nathan (not drafted)

* O-1. Change Process Guide §3.5.1 and Glow QA Guide §3.1.3 still place the close mutation set before the closure decision. Their tasks (T-03, T-06) held that text as H-06 and have already applied their revisions (v2.5.6 and v3.0.8) without it. The 2026-11-02 ruling is recorded only in this task's files; the ledger's H-06 row and those two documents are outside this task.
* O-2. R-4 gives a plan the values RAN (with evidence references), WAIVED or MISSING. It does not say which value a plan carries for a live test it includes but has not yet run. RL-03 and RL-04 reproduce the rule as written.
* O-3. "Review guardrails" > "Explicit non-blockers" repeats one bullet at lines 1199 and 1200. Removing it needs a source or Nathan's authorization; it is not a placeholder or drafting marker. Unchanged.
* O-4. §1 "Close-out deliverables" lets the QA RCA & Doc Delta summary "live as a section of the epic close report, or a governed artifact referenced by it" (line 1005). The summary carries the readiness / closeout recommendation; under the ruling the close report is written after the closure decision, so only the second option can carry a summary the closure decision relies on. The text does not contradict the ruling and is unchanged.

## 10. Producer validation

Method: a script built every OLD block from the unchanged original by line number, built every NEW block from its OLD block where the OLD text is kept, and checked the batch before the file was written. A second, independent parser then read the saved redlines file, extracted each fenced block, and repeated the checks against the original.

| Check | Result |
| :---- | :---- |
| Operation dialect | Eighteen `REPLACE`; no `FIND_AND_REPLACE`, so the RL-045 count rule does not arise |
| OLD occurrence, expected / observed | 1 / 1 for each of RL-01 to RL-18 |
| OLD alignment | Each OLD starts at a line start and ends before the LF that ends its stated last line; each equals its stated line or line range |
| Stated lines equal resolved lines | 112, 287, 326, 389, 973, 1168, 1312, 1450–1453, 1459, 2226–2227, 2239, 2255, 2261, 3120, 3218, 3232, 3447, 3560 |
| Spans (character offsets, original order) | RL-01 8497–8772; RL-02 27086–27420; RL-03 30064–30143; RL-04 35357–35434; RL-05 88968–89193; RL-06 134106–134961; RL-07 161547–162110; RL-08 176395–178345; RL-09 180321–180705; RL-16 242168–242453; RL-17 243383–243488; RL-18 244786–244940; RL-10 245520–245578; RL-11 278628–278711; RL-12 284474–284820; RL-13 284997–285019; RL-14 295485–295549; RL-15 300089–300119 |
| Overlap, shared boundary, insertion in a replaced span, redline anchored on another's output | None |
| Payload hygiene | No U+2026, no three-period sequence, no fence, no CR in any NEW block |
| Saved-file round trip | Every fenced block in the saved file matches its stated SHA-256 and byte length, and re-resolves to count 1 in the original |
| One-pass simulation | Applying all eighteen against the original, in descending offset order, gives 331,980 bytes and 3,980 lines (SHA-256 `f6f2cbc70d0210527e73cd6ccfbd29d9d9ead046b0194e1cedba2e93d6328b14`). Each NEW block occurs exactly once in the result. This simulation changes no header field; TW-APPLY-10 derives the document-control fields. |

The validation scripts ran in the session scratchpad and are not committed.

## 11. Header provenance for TW-APPLY-10

* Baseline header schema (lines 1–15), in order: `# **0\) Document Control**`, `## **Header**`, then `**Title:**` PF27-Canon-Plan-Templates; `**Version:**` v2.0.6; `**Status:**` Canon; `**Effective date:**` 2026-10-26; `**Last Update Gate:**` BN 13.8.8; HDE-CRD-0002-specification-v1.1-approved.md; HDE-CRD-0002-QA70-qa-plan-review-v1.0.md; `**Invocation tag:**` INV-f2ac55d77ce9aacc. Each field is its own paragraph.
* Sources that justify this update, in source order: `PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5. It is the only source. The Product Owner's ruling decides a conflict and is not a source file.
* Internal restatements of the document's own version or date outside the header: none (a search for `2.0.6` and `2026-10-26` finds only header lines 7 and 11).
* Change log or revision history: the target has none, and none is prepared.
* Status language and drafting markers: Status is Canon, not stale. A search for TODO, FIXME, `???`, TBD, draft-status wording and editorial notes found only template rules and template fields, which canon requires; no hygiene redline is needed.
* No redline touches the header.

## 12. Correction record

**`prep-r1` to `prep-r2`**

* What `prep-r1` was. Six redlines, saved and verified as `READY` / `COMPLETE_PACKAGE` (redlines file SHA-256 `0bb360b2fa126207207216a4b48f3fb42da211cd78ba487a243868a3b64ce15f`) and committed as "docs(ephemeral): add T-07 PF27 redlines and proof log (gtwpe-20261101-pf10-v14-0-5)" (`7061dc8a`). The defect below was found before that commit was first pushed; it reaches the branch only as history, and it was not given to TW-APPLY-10.
* The defect, this preparer's own. `prep-r1` mapped the selected units only onto the ledger's section anchors. It left PF27 sections that 2.15 bears on in context (the Epic Specification's open-rails bullets; the §3B, §8, §9 and §10 records; the Live QA Plan approval-blocker list) as observations "outside the assigned selection", and it disposed of 2.15 R-2, R-5 and R-6 as "not PF27's share" because 2.15's drainage list sends them to HDE Governance. Both are drain-target gates, which GTWPE-D3 rules out. It also left the D-2 "Version literals" row unexamined.
* How it was found. Before the push, the fetch of the shared branch brought the ledger's 2026-11-02 correction banner (commit `a3632c0e533c1dfbad2f215c368210a65ecceb21`), which cites GTWPE-D3. GTWPE-D3 was then read in full; it had not been read for `prep-r1`.
* The correction. The whole target was rescanned on context for every selected rule, nine redlines were added, r1's RL-03 (r2's RL-04) gained R-2, R-5 and R-6, and the batch was revalidated as a whole.
* ID map, r1 to r2: RL-01 to RL-02; RL-02 to RL-03; RL-03 to RL-04 (extended); RL-04 to RL-05; RL-05 to RL-07; RL-06 to RL-09.

**`prep-r2` to `prep-r3`**

* What `prep-r2` was. Fifteen redlines (redlines file SHA-256 `e547b3353dbaae69d8bd86d740d759da957204c1683a4ec61248997e3bf69212`, commit `bf5bb084`), applied as `apply-r1` (revised PF SHA-256 `dbbea67326c03ad925b54b50e25c6a4b22b1d75b7d8a447dfa1a4358a650325f`, commit `4a033d4b`). It held §3B under H-06 and reported that R-3 and §3B stated different orderings.
* The new input. The Product Owner's ruling of 2026-11-02 (§2) resolved CCR-5 for R-3 as written. That is a decision input, not a defect in `prep-r2`.
* The correction. RL-16, RL-17 and RL-18 drain §3B to match R-3; RL-10's Exit field is revised to agree; every other redline is unchanged. The batch was revalidated as a whole (§10).

## 13. Save verification receipt

Written after the redlines file was saved in the working tree and read back from disk, on 2026-11-02.

| File | Verification |
| :---- | :---- |
| Redlines file | Read back from disk: 52,241 bytes, 571 lines, SHA-256 `3e6a36a493ea829394eda9a4127dc02dca5e2f6126bf745f372410929aad1f7d`, ending with the line `END OF REDLINES` and a final LF. The independent parser re-validated the saved bytes: eighteen redlines, each block matching its stated hash and length, each OLD at count 1, no overlap, and a one-pass result byte-identical to the simulation in §10. |
| This proof log | Read back in full after it was written; one count in §8 was then corrected, and this receipt row and the line below were added and read back. A comparison of the saved `prep-r3` blocks with the pushed `prep-r2` blocks confirmed that only RL-10 changed and that RL-16 to RL-18 are new. |

Save completeness: `COMPLETE_PACKAGE`. Preparation outcome: `READY`. The package is ready for TW-APPLY-10 with the unchanged original, these two files, ledger rows C-02, C-08, C-09 and C-26, the selected source units in §3, branch `claude/gtwpe-triage-authoring-j94ewf`, final-output directory `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF27/` and diagnostic path `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF27/PF27-apply-diagnostic.gtwpe-20261101-pf10-v14-0-5.md`. The commit that holds the pair is given in the ledger row and the session's final response.
