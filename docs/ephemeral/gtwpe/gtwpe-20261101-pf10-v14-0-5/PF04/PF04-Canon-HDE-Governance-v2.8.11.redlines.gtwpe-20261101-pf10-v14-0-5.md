# PF04-Canon-HDE-Governance v2.8.11 — redlines — gtwpe-20261101-pf10-v14-0-5 (T-01 follow-up: Appendix D.4 header-snapshot pointers)

## 1. Package identity

| Field | Value |
| :---- | :---- |
| Redlines file | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.11.redlines.gtwpe-20261101-pf10-v14-0-5.md` |
| Proof log | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.11.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md` |
| Preparation outcome | `READY`. Save completeness is recorded in the proof log's save-verification receipt. |
| Run identity | `gtwpe-20261101-pf10-v14-0-5/T-01/drain-4`, prepared 2026-11-02. It follows `drain-3`, whose redlines produced the baseline below. |
| Authorization | Nathan, 2026-11-02, in the T-16 document session, choosing "option 1" for the four untracked D.4 header snapshots: find the matching tracked snapshots and correct D.4 in a fourth follow-up |
| Prompt | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1 (Notion page `3f44590a05eb8172a314fe6b958bb9ff`, page last edited 2026-10-09T11:05:22.094Z), fetched live when this step began |
| Originating preparer | The executing document agent in the Claude Code session Nathan started for T-16 (https://claude.ai/code/session_01Q789u2ywt3AZEqAwzRmdCR). That session also prepared `drain-3`; T-01's own session prepared `drain-1` and `drain-2`. No subagent, reviewer or other session took part. |
| Baseline | The revised PF04 v2.8.11 that TW-APPLY-10 produced from `drain-3`: `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.11.md` at commit `6c979d6`; in-document title `PF04-Canon-HDE-Governance`; version v2.8.11; git blob `be4f1a09fb6a70a820a69bb75a6085a63f1606f3`; SHA-256 `043110c99a7101df8b8044fa6b980e763e57026b44ca2a73f075d17f378c019f`; 603,605 bytes; 4,895 lines |
| Authority note | The current authoritative PF04 on `main` (`84d6d1cad95c67788336d174dc4b8922d9bb0cb2`) is still v2.8.8 (blob `0c3ce100f942`). As `drain-2` and `drain-3` did, this package is chained on the latest unpublished output, so one revised PF carries all four runs. It applies only to the v2.8.11 bytes above. If v2.8.11 changes before publication, the package returns to its preparer for reconciliation. |
| Source | None beyond the chained revision's source. The corrections rest on Nathan's authorization, on repository inspection at `main` `84d6d1c` and on the owning canon named below, not on a further source file. The chained revision's source is `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5; git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`; unchanged on `main` `84d6d1c`. |
| Selected source unit | None. This is an authorized correction, not a drain of a further addendum. |
| Supporting reading | HDE Schemas and Artifacts §8.6.3.3, "Aux Narrative (text) — header snapshots" (`docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.7.md` on `main`, lines 3009–3012); HDE Narratives Guide, "Evidence scope (EPIC-010)" (`docs/pfcanon/PF17-Canon-HDE-Narratives-Guide-v1.5.4.md`, lines 1071–1072): "Aux evidence captures exactly **two** header snapshots: `aux_text_200.snap` and `aux_suppression_200.snap`; Aux HEAD/304 captures are out of scope (A7 is Catalog-only)"; HDE CLI/API Vendor Ref (`docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.4.md`, lines 2696–2697), which lists the same two snapshots; PF03 Technical Writing Best Practices v1.8.8 (editorial standard) |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md`; task T-01 |
| Branch and PR | `claude/gtwpe-triage-authoring-j94ewf`; draft PR amthorn78/glow-hdengine-v2#826 |
| Expected final output | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.12.md`, with its `.proof-log.md` beside it; TW-APPLY-10 derives the name |
| Apply diagnostic path | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-apply-diagnostic.gtwpe-20261101-pf10-v14-0-5.md` |

## 2. Application contract

* Every operation resolves independently against the unchanged v2.8.11 baseline in §1. Apply all three in one pass by their baseline-bound positions; nothing is rematched on mutated text.
* Operations used: `REPLACE` (two) and `INSERT` (one). No `DELETE`, `FIND AND REPLACE` or `FIND_AND_REPLACE` operation is used.
* `REPLACE`: the old block occurs exactly once in the whole baseline and is replaced by the replacement block. Nothing outside the old block is consumed.
* `INSERT`: the BEFORE anchor and the AFTER anchor each occur exactly once in the whole baseline and are contiguous. Their boundary is the gap. Neither anchor changes. The inserted text supplies every newline at the gap.
* Payload literals use the same convention as the earlier T-01 packages. Each literal sits in a fenced block that opens with a line of exactly four backticks followed by `text` and closes with a line of exactly four backticks. The literal is the bytes strictly between the line feed that ends the opening fence line and the line feed that immediately precedes the closing fence line. Trailing spaces are significant. Every literal states its UTF-8 byte length and SHA-256; a mismatch is an authoring defect for the preparer.
* Non-overlap: the three operations are far apart (baseline lines 2810, 4789–4791 and 4807–4808), and the insertion gap touches no replaced span.
* Document-control fields are reserved for TW-APPLY-10. No redline edits baseline lines 5–10. Baseline values: `PF04-Canon-HDE-Governance`, `v2.8.11`, `Canon`, `2026-11-02`, `BN 14.0.5`, `` `INV-f2ac55d77ce9aacc` ``. The source that justifies this update, as the chained revision records it, is `PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5; this correction adds no further source file, so the gate stays `BN 14.0.5`.
* Change history. RL-03 adds the PF04 §9.3.1 entry that §9.3 requires. It names v2.8.12 (v2.8.11 bumped once by the log's patch scheme) and 2026-11-02, the preparation date. If TW-APPLY-10 derives a different version, the package returns to its preparer.
* Hygiene. As `drain-3` recorded, the lineage's hygiene state is the one T-01's `drain-1` established, and `drain-3` added no marker. No hygiene redline is included.

## 3. Redlines

### RL-01 — REPLACE

- Operation: `REPLACE`
- Ledger rows: T-01; Nathan's "option 1" of 2026-11-02
- Change type (report classification): CONSISTENCY (routing pointers aligned with the tracked Aux snapshots)
- Location (baseline heading path): "# **Appendix D — Evidence Index (titles/paths only) \[Required-Now\]**" > "## **D.4 Endpoint Catalog & transport proofs (Reader A7)**", list "**Aux Narrative (text) snapshots (headers-only).**", its second to fourth items
- Baseline lines (informative only, not a locator): 4789–4791. Line 4788, `aux_text_200.snap`, is not part of the old block and stays unchanged.
- Scope: whole PF; expected occurrences: old block 1; observed: old block 1 / 1
- Controlling basis: Nathan's authorization; repository inspection at `main` `84d6d1c`: `tests/transport/headers/` tracks `aux_text_200.snap`, `aux_suppression_200.snap` and `no_store_writers_errors.snap` (with path proofs for the two Aux snapshots); the Human Evidence Index maps `transport.aux.headers.text` and `transport.aux.headers.suppression` to the two Aux snapshots; GitHub's path-filtered commit list for `main` at `84d6d1c` returns no commit for `tests/transport/headers/aux_head.snap`, `aux_304.snap`, `aux_suppression.snap` or `error_headers_utf8.snap`. HDE Schemas and Artifacts §8.6.3.3 and HDE CLI/API Vendor Ref list exactly `aux_text_200.snap` and `aux_suppression_200.snap`. HDE Narratives Guide: "Aux evidence captures exactly **two** header snapshots [..]; Aux HEAD/304 captures are out of scope". PF04 §9.4 refreshes Appendix D pointers when they are affected.
- Effect: The Aux list names exactly the two tracked snapshots. `aux_suppression.snap` becomes `aux_suppression_200.snap`; the `aux_head.snap` and `aux_304.snap` pointers are removed, with no counterpart, because Aux HEAD and 304 captures are out of scope.

- Old block (135 bytes, SHA-256 `1ab13aeea8687dad5fcff5b715cd3f98eb0197c53288b6eb22726b99194fe650`):

````text
* `tests/transport/headers/aux_head.snap`  
* `tests/transport/headers/aux_304.snap`  
* `tests/transport/headers/aux_suppression.snap`
````

- Replacement block (52 bytes, SHA-256 `4a7fce1eb54b47289bbfbafcd6b427eebea8d7063ca61d2a63ac7f0cb658d118`):

````text
* `tests/transport/headers/aux_suppression_200.snap`
````

### RL-02 — REPLACE

- Operation: `REPLACE`
- Ledger rows: T-01; Nathan's "option 1" of 2026-11-02
- Change type (report classification): CONSISTENCY (routing pointer to an untracked snapshot removed)
- Location (baseline heading path): "# **Appendix D — Evidence Index (titles/paths only) \[Required-Now\]**" > "## **D.4 Endpoint Catalog & transport proofs (Reader A7)**", list "**Writer/error posture (headers-only).**"
- Baseline lines (informative only, not a locator): 4807–4808
- Scope: whole PF; expected occurrences: old block 1; observed: old block 1 / 1
- Controlling basis: Nathan's authorization; repository inspection at `main` `84d6d1c`: `tests/transport/headers/` tracks `aux_text_200.snap`, `aux_suppression_200.snap` and `no_store_writers_errors.snap` (with path proofs for the two Aux snapshots); the Human Evidence Index maps `transport.aux.headers.text` and `transport.aux.headers.suppression` to the two Aux snapshots; GitHub's path-filtered commit list for `main` at `84d6d1c` returns no commit for `tests/transport/headers/aux_head.snap`, `aux_304.snap`, `aux_suppression.snap` or `error_headers_utf8.snap`. `tests/transport/headers/no_store_writers_errors.snap` holds a `[success]` and an `[error]` section, the error section recording `content-type: application/json; charset=utf-8`, and `tests/transport/test_writers_errors_headers.py` reads it. No PF canon document other than PF04 names `error_headers_utf8.snap`.
- Effect: The writer and error list names only the tracked snapshot, which already carries the error headers. The list's other entry is unchanged.

- Old block (110 bytes, SHA-256 `c7f42b8152913972a9e84a30bc10a53c1440ff12a5b42b059152f124e30eb69e`):

````text
* `tests/transport/headers/error_headers_utf8.snap`  
* `tests/transport/headers/no_store_writers_errors.snap`
````

- Replacement block (56 bytes, SHA-256 `f1a39c3df53322cb3ab5a3b357d375147d9da28468a55184359cc5323449c005`):

````text
* `tests/transport/headers/no_store_writers_errors.snap`
````

### RL-03 — INSERT

- Operation: `INSERT`
- Ledger rows: PF04 §9.3 change-history rule, for RL-01 and RL-02
- Change type (report classification): DOC_HYGIENE (required change-history entry)
- Location (baseline heading path): "# **9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]**" > "> ## **9.3 Doc-Delta entries (what to record for any normative change)**" > "> ### **9.3.1 PF04 Governance Change Log \[Required-Now\]**"
- Baseline lines (informative only, not a locator): gap between 2810 and 2811
- Scope: whole PF; expected occurrences: gap 1 (BEFORE and AFTER each 1, and contiguous 1); observed: BEFORE 1, AFTER 1, gap 1 / 1, 1, 1
- Controlling source: PF04 §9.3 and §9.3.1 (every normative PF04 change adds a Doc-Delta entry; NON_EPIC class; `GOV-YYYYMMDD-<shortslug>`, unique within §9.3.1) and the §9.4 template fields
- Effect: Adds the v2.8.12 entry after the v2.8.11 entry, in the log's own format, with a new unique ID `GOV-20261102-gtwpe-pf04-headersnaps`.

- BEFORE anchor (313 bytes, SHA-256 `15cbfa059ec80b88812949e59c1168598df741e1a1fd459296538a01e4ba5f14`):

````text
> Change Log entry (one line): v2.8.11 | GOV-20261102-gtwpe-pf04-a7path | NON_EPIC | Scope: Appendix D.4 encoding-invariance proof pointer corrected to the tracked path | Targets: Appendix D.4 | Acceptance: None | Evidence: None | Freeze-pack: No | Canonical record: PF04 §9.3.1 / GOV-20261102-gtwpe-pf04-a7path

````

- AFTER anchor (57 bytes, SHA-256 `66c397ea614cb823ef0c1a7d7b7d6c495c250953ed3b8f37b56f4db9b11fa094`):

````text


> ---

> ## **9.4 Doc-Delta template \[Required-Now\]**
````

- Inserted text (3499 bytes, SHA-256 `ecf1294d58423aa1b1be08470663429b43141336fc44512d09207698d690d3c6`):

````text

v2.8.12 | GOV-20261102-gtwpe-pf04-headersnaps | NON_EPIC | Scope: Appendix D.4 header-snapshot pointers aligned with the tracked Aux and writer/error snapshots | Targets: Appendix D.4 | Acceptance: None | Evidence: None | Freeze-pack: No | Canonical record: PF04 §9.3.1 / GOV-20261102-gtwpe-pf04-headersnaps

> DOC-DELTA-ID: GOV-20261102-gtwpe-pf04-headersnaps
>
> Date / Author: 2026-11-02 / executing document agent in Nathan's T-16 document session, under Nathan's authorization of 2026-11-02 to correct the T-01 document
>
> PF04 version: v2.8.12
>
> Record class: NON_EPIC
>
> Epic ID: NOT APPLICABLE - NON_EPIC
>
> Draft / binding surface: NOT APPLICABLE - NON_EPIC
>
> Stable record surface: PF04 §9.3.1 / GOV-20261102-gtwpe-pf04-headersnaps
>
> Scope: Acceptance/Evidence; Governance/Documentation
>
> Targets (section anchors): Appendix D.4
>
> Summary (≤ 5 bullets):
>
> 1) Correct the Aux suppression snapshot pointer from `tests/transport/headers/aux_suppression.snap` to `tests/transport/headers/aux_suppression_200.snap`, the snapshot that HDE Schemas and Artifacts, HDE CLI/API Vendor Ref and HDE Narratives Guide list.
>
> 2) Remove the `tests/transport/headers/aux_head.snap` and `tests/transport/headers/aux_304.snap` pointers. Neither file has a commit in the history of `main`, and HDE Narratives Guide keeps Aux HEAD and 304 captures out of scope, with exactly two Aux header snapshots.
>
> 3) Remove the `tests/transport/headers/error_headers_utf8.snap` pointer. The file has no commit in the history of `main`; the writer and error headers, including the error `Content-Type`, are captured in `tests/transport/headers/no_store_writers_errors.snap`, which D.4 keeps.
>
> Acceptance impact (binary gates to update or verify): None. The A7 transport gate, the Aux evidence scope and the writer and error no-store posture are unchanged; only the routing pointers now name tracked snapshots. No new or satisfied token, QA verdict, OPS result or acceptance decision is claimed.
>
> Evidence updates (titles and paths only): No governed evidence artifact, golden, script, header snapshot, CI job, Human Evidence Index, hash sentinel, Machine Mirror or path proof is created or regenerated by this document revision. The Appendix D routing pointers are refreshed to `tests/transport/headers/aux_text_200.snap`, `tests/transport/headers/aux_suppression_200.snap` and `tests/transport/headers/no_store_writers_errors.snap`.
>
> Freeze-pack impact: No; this document revision cuts, recomputes, activates and promotes no release and changes no release member.
>
> Routing (titles only confirmations): HDE Schemas and Artifacts owns the header-snapshot paths and the Evidence Index. HDE Narratives Guide owns the Aux evidence scope. HDE CLI/API Vendor Ref owns the transport bytes.
>
> Rollout plan: Nathan's authorized publication of the complete revised PF is a separate manual action. No runtime staging, canary, deployment or pointer flip is performed by this revision. A document backout uses the retained v2.8.11 source through ordinary authorized publication. Runtime monitoring and rollback retain their existing owners and controls.
>
> Change Log entry (one line): v2.8.12 | GOV-20261102-gtwpe-pf04-headersnaps | NON_EPIC | Scope: Appendix D.4 header-snapshot pointers aligned with the tracked Aux and writer/error snapshots | Targets: Appendix D.4 | Acceptance: None | Evidence: None | Freeze-pack: No | Canonical record: PF04 §9.3.1 / GOV-20261102-gtwpe-pf04-headersnaps

````

END OF REDLINES
