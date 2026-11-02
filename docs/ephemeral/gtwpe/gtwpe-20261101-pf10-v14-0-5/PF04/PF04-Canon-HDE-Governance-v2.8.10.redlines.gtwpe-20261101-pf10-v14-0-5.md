# PF04-Canon-HDE-Governance v2.8.10 — redlines — gtwpe-20261101-pf10-v14-0-5 (T-01 follow-up: Appendix D.4 encoding-invariance pointer)

## 1. Package identity

| Field | Value |
| :---- | :---- |
| Redlines file | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.10.redlines.gtwpe-20261101-pf10-v14-0-5.md` |
| Proof log | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.10.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md` |
| Preparation outcome | `READY`. Save completeness is recorded in the proof log's save-verification receipt. |
| Run identity | `gtwpe-20261101-pf10-v14-0-5/T-01/drain-3`, prepared 2026-11-02. It follows T-01's `drain-2`, whose redlines produced the baseline below. |
| Authorization | Nathan, 2026-11-02, in the T-16 document session: "I authorize you to apply the correction to the T-01 document (PF04)". The correction is the one the T-16 redlines proof log reports as D-10: PF04 Appendix D.4 names the untracked `artifacts/proofs/encoding_invariance.txt`. |
| Prompt | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1 (Notion page `3f44590a05eb8172a314fe6b958bb9ff`, page last edited 2026-10-09T11:05:22.094Z), fetched live when this step began |
| Originating preparer | The executing document agent in the Claude Code session Nathan started for T-16 (https://claude.ai/code/session_01Q789u2ywt3AZEqAwzRmdCR), acting on T-01's document under the authorization above. T-01's own session prepared `drain-1` and `drain-2`. No subagent, reviewer or other session took part. |
| Baseline | The revised PF04 v2.8.10 that TW-APPLY-10 produced from T-01's `drain-2`: `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.10.md` at commit `8d4c686`; in-document title `PF04-Canon-HDE-Governance`; version v2.8.10; git blob `3ef2b20e6006be94e132d7063bd5047751457eca`; SHA-256 `37d58278ce65c2a736a12c391496143315edebdab24600c8418353b921a81438`; 600,876 bytes; 4,859 LF-terminated lines |
| Authority note | The current authoritative PF04 on `main` (`84d6d1cad95c67788336d174dc4b8922d9bb0cb2`) is still v2.8.8 (blob `0c3ce100f942`), because v2.8.9 and v2.8.10 are unpublished. As T-01's `drain-2` did, this package is chained on T-01's latest output, so that one revised PF carries all three runs. It applies only to the v2.8.10 bytes above. If v2.8.10 changes before publication, the package returns to its preparer for reconciliation. |
| Source | None beyond the chained revision's source. The correction rests on Nathan's authorization and on repository inspection at `main` `84d6d1c` (proof log §3), not on a further source file. The chained revision's source is `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5; git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`; unchanged on `main` `84d6d1c`. |
| Selected source unit | None. This is an authorized correction, not a drain of a further addendum. |
| Supporting reading | HDE Schemas and Artifacts §8.6.3.3 "Reader, CLI, compat, and conjunction evidence", "Endpoint Catalog and A7 proofs" (`docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.7.md` on `main`, lines 2996–3007), which lists `artifacts/proofs/success_encoding_invariance.txt` (optional); PF03 Technical Writing Best Practices v1.8.8 (editorial standard) |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md`; task T-01 |
| Branch and PR | `claude/gtwpe-triage-authoring-j94ewf`; draft PR amthorn78/glow-hdengine-v2#826 |
| Expected final output | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.11.md`, with its `.proof-log.md` beside it; TW-APPLY-10 derives the name |
| Apply diagnostic path | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-apply-diagnostic.gtwpe-20261101-pf10-v14-0-5.md` |

## 2. Application contract

* Every operation resolves independently against the unchanged v2.8.10 baseline in §1. Apply both in one pass by their baseline-bound positions; nothing is rematched on mutated text.
* Operations used: `REPLACE` (one) and `INSERT` (one). No `DELETE`, `FIND AND REPLACE` or `FIND_AND_REPLACE` operation is used.
* `REPLACE`: the old block occurs exactly once in the whole baseline and is replaced by the replacement block. Nothing outside the old block is consumed.
* `INSERT`: the BEFORE anchor and the AFTER anchor each occur exactly once in the whole baseline and are contiguous. Their boundary is the gap. Neither anchor changes. The inserted text supplies every newline at the gap.
* Payload literals use the same convention as T-01's `drain-1` and `drain-2` packages. Each literal sits in a fenced block that opens with a line of exactly four backticks followed by `text` and closes with a line of exactly four backticks. The literal is the bytes strictly between the line feed that ends the opening fence line and the line feed that immediately precedes the closing fence line. Trailing spaces are significant. Every literal states its UTF-8 byte length and SHA-256; a mismatch is an authoring defect for the preparer.
* Non-overlap: the two operations are far apart (baseline lines 2774 and 4748), and the insertion gap touches no replaced span.
* Document-control fields are reserved for TW-APPLY-10. No redline edits baseline lines 5–10. Baseline values: `PF04-Canon-HDE-Governance`, `v2.8.10`, `Canon`, `2026-11-02`, `BN 14.0.5`, `` `INV-f2ac55d77ce9aacc` ``. The source that justifies this update, as the chained revision records it, is `PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5; this correction adds no further source file, so the gate stays `BN 14.0.5`.
* Change history. RL-02 adds the PF04 §9.3.1 entry that §9.3 requires. It names v2.8.11 (v2.8.10 bumped once by the log's patch scheme) and 2026-11-02, the preparation date. If TW-APPLY-10 derives a different version, the package returns to its preparer.
* Hygiene. T-01's `drain-1` found no `Draft` status language, TODO, unresolved drafting note or editorial comment to remove outside canon-required template text and history, and its pre-existing ellipsis forms are path patterns, not drafting markers (`drain-1` proof log, observation O-2 and the hygiene paragraph). The baseline differs from the original only by T-01's verified payloads. No hygiene redline is included.

## 3. Redlines

### RL-01 — REPLACE

- Operation: `REPLACE`
- Ledger rows: T-01; the correction Nathan authorized on 2026-11-02 (T-16 redlines proof log, D-10)
- Change type (report classification): CONSISTENCY (routing pointer corrected to the tracked path)
- Location (baseline heading path): "# **Appendix D — Evidence Index (titles/paths only) \[Required-Now\]**" > "## **D.4 Endpoint Catalog & transport proofs (Reader A7)**", list "**Catalog/A7 artifacts.**", its last item
- Baseline lines (informative only, not a locator): 4748
- Scope: whole PF; expected occurrences: old block 1; observed: old block 1 / 1
- Controlling basis: Nathan's authorization; repository inspection at `main` `84d6d1c`: `artifacts/proofs/encoding_invariance.txt` is not tracked; `artifacts/proofs/success_encoding_invariance.txt` is tracked, is written by `tools/evidence/generate_a7_transport_proofs.py` and is the Human Evidence Index row `a7.success_encoding_invariance`; `tests/transport/test_a7_transport_proofs.py::test_obsolete_encoding_invariance_absent` asserts that the old path stays absent. HDE Schemas and Artifacts §8.6.3.3 lists `artifacts/proofs/success_encoding_invariance.txt` (optional). PF04 §9.4: "PF04 Appendix D is an informative routing aid and is refreshed when its pointers are affected."
- Effect: The D.4 pointer names the tracked proof. The item's label, its "Optional" qualifier and the rest of D.4 are unchanged.

- Old block (83 bytes, SHA-256 `365260c8786926a370f20b374c78422eee66e9561d25aef18202b983b7f6f116`):

````text
* Optional encoding-invariance proof — `artifacts/proofs/encoding_invariance.txt`
````

- Replacement block (91 bytes, SHA-256 `25c16a0a39726783dea7cfee739a9f1c8a74364dbcf49650f3854b7f2843d7a7`):

````text
* Optional encoding-invariance proof — `artifacts/proofs/success_encoding_invariance.txt`
````

### RL-02 — INSERT

- Operation: `INSERT`
- Ledger rows: PF04 §9.3 change-history rule, for RL-01
- Change type (report classification): DOC_HYGIENE (required change-history entry)
- Location (baseline heading path): "# **9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]**" > "> ## **9.3 Doc-Delta entries (what to record for any normative change)**" > "> ### **9.3.1 PF04 Governance Change Log \[Required-Now\]**"
- Baseline lines (informative only, not a locator): gap between 2774 and 2775
- Scope: whole PF; expected occurrences: gap 1 (BEFORE and AFTER each 1, and contiguous 1); observed: BEFORE 1, AFTER 1, gap 1 / 1, 1, 1
- Controlling source: PF04 §9.3 and §9.3.1 (every normative PF04 change adds a Doc-Delta entry; NON_EPIC class; `GOV-YYYYMMDD-<shortslug>`, unique within §9.3.1) and the §9.4 template fields
- Effect: Adds the v2.8.11 entry after the v2.8.10 entry, in the log's own format, with a new unique ID `GOV-20261102-gtwpe-pf04-a7path`.

- BEFORE anchor (358 bytes, SHA-256 `6d4f946b3f22d2d29ff0b6d5dbec8fe83a66b274481d704e94fe62e98a48e6c9`):

````text
> Change Log entry (one line): v2.8.10 | GOV-20261102-gtwpe-pf04-route | NON_EPIC | Scope: Vendor route selection by the configured base's terminal v1 or v2 segment; terminal-v1 legacy selection, not fallback | Targets: §11.1.1, §11.1.6 | Acceptance: None | Evidence: None | Freeze-pack: No | Canonical record: PF04 §9.3.1 / GOV-20261102-gtwpe-pf04-route

````

- AFTER anchor (57 bytes, SHA-256 `66c397ea614cb823ef0c1a7d7b7d6c495c250953ed3b8f37b56f4db9b11fa094`):

````text


> ---

> ## **9.4 Doc-Delta template \[Required-Now\]**
````

- Inserted text (2721 bytes, SHA-256 `01acd7388cd70a2e7104c1a96dd5069c552cf2816c314ed11be0d27f28fdee08`):

````text

v2.8.11 | GOV-20261102-gtwpe-pf04-a7path | NON_EPIC | Scope: Appendix D.4 encoding-invariance proof pointer corrected to the tracked path | Targets: Appendix D.4 | Acceptance: None | Evidence: None | Freeze-pack: No | Canonical record: PF04 §9.3.1 / GOV-20261102-gtwpe-pf04-a7path

> DOC-DELTA-ID: GOV-20261102-gtwpe-pf04-a7path
>
> Date / Author: 2026-11-02 / executing document agent in Nathan's T-16 document session, under Nathan's authorization of 2026-11-02 to correct the T-01 document
>
> PF04 version: v2.8.11
>
> Record class: NON_EPIC
>
> Epic ID: NOT APPLICABLE - NON_EPIC
>
> Draft / binding surface: NOT APPLICABLE - NON_EPIC
>
> Stable record surface: PF04 §9.3.1 / GOV-20261102-gtwpe-pf04-a7path
>
> Scope: Acceptance/Evidence; Governance/Documentation
>
> Targets (section anchors): Appendix D.4
>
> Summary (≤ 5 bullets):
>
> 1) Correct the Appendix D.4 routing pointer for the optional encoding-invariance proof from `artifacts/proofs/encoding_invariance.txt`, which is not tracked, to `artifacts/proofs/success_encoding_invariance.txt`, the path that HDE Schemas and Artifacts lists and the Human Evidence Index records.
>
> Acceptance impact (binary gates to update or verify): None. The A7 transport gate and its proof obligations are unchanged; only the routing pointer now names the tracked proof. No new or satisfied token, QA verdict, OPS result or acceptance decision is claimed.
>
> Evidence updates (titles and paths only): No governed evidence artifact, golden, script, header snapshot, CI job, Human Evidence Index, hash sentinel, Machine Mirror or path proof is created or regenerated by this document revision. The Appendix D routing pointer is refreshed to `artifacts/proofs/success_encoding_invariance.txt`.
>
> Freeze-pack impact: No; this document revision cuts, recomputes, activates and promotes no release and changes no release member.
>
> Routing (titles only confirmations): HDE Schemas and Artifacts owns the A7 proof paths and the Evidence Index. HDE CLI/API Vendor Ref owns the transport bytes.
>
> Rollout plan: Nathan's authorized publication of the complete revised PF is a separate manual action. No runtime staging, canary, deployment or pointer flip is performed by this revision. A document backout uses the retained v2.8.10 source through ordinary authorized publication. Runtime monitoring and rollback retain their existing owners and controls.
>
> Change Log entry (one line): v2.8.11 | GOV-20261102-gtwpe-pf04-a7path | NON_EPIC | Scope: Appendix D.4 encoding-invariance proof pointer corrected to the tracked path | Targets: Appendix D.4 | Acceptance: None | Evidence: None | Freeze-pack: No | Canonical record: PF04 §9.3.1 / GOV-20261102-gtwpe-pf04-a7path

````

END OF REDLINES
