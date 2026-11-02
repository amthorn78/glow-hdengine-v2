# PF04-Canon-HDE-Governance v2.8.9 — redlines — gtwpe-20261101-pf10-v14-0-5 (T-01 follow-up: vendor route selection)

## 1. Package identity

| Field | Value |
| :---- | :---- |
| Redlines file | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.9.redlines.gtwpe-20261101-pf10-v14-0-5.md` |
| Proof log | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.9.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md` |
| Preparation outcome | `READY`. Save completeness is recorded in the proof log's save-verification receipt. |
| Run identity | `gtwpe-20261101-pf10-v14-0-5/T-01/drain-2`, prepared 2026-11-02. It follows `drain-1`, whose redlines produced the baseline below. |
| Authorization | Nathan, 2026-11-02, choosing option A ("yes, proceed with A"): drain 2.1 D-2 (ledger row C-02) into PF04, which no task routed it to |
| Prompt | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1 (Notion page `3f44590a05eb8172a314fe6b958bb9ff`, page last edited 2026-10-09T11:05:22.094Z) |
| Originating preparer | The executing document agent in the Claude Code session Nathan started for T-01 (session `session_01Q789tyrM8bruo2RGNCMLM8`). No subagent, reviewer or other session took part. |
| Baseline | The revised PF04 v2.8.9 that TW-APPLY-10 produced from `drain-1`: `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.9.md` at commit `b489215f82aa156ae49a66284330afb47aa00c21`; in-document title `PF04-Canon-HDE-Governance`; version v2.8.9; git blob `cc46c5ac0108fc5a3a2eed1e0fdeb4b9518a2e76`; SHA-256 `a92dda98a5b2037e90f898033674721a12e21243242131b3fa063ab3e167125c`; 596,102 bytes; 4,821 LF-terminated lines |
| Authority note | The current authoritative PF04 on `main` (`84d6d1cad95c67788336d174dc4b8922d9bb0cb2`) is still v2.8.8 (blob `0c3ce100f942`), because v2.8.9 is unpublished. This package is chained on v2.8.9 so that one revised PF carries both runs. It applies only to the v2.8.9 bytes above. If v2.8.9 changes before publication, the package returns to its preparer for reconciliation. |
| Source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5; git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`; unchanged on `main` `84d6d1c` |
| Selected source unit | 2.1 D-2 (lines 277–344), with the 2.1 context (lines 205–224 and 491–516) |
| Supporting reading | HDE CLI/API Vendor Ref §7.1.10 "Endpoint policy (explicit version-gated dual lineage)" on `main` (`docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.4.md`, blob `53e6a9028dfa`); PF03 Technical Writing Best Practices v1.8.8 (editorial standard) |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md`; task T-01; row C-02 (PF04's share) added to T-01 by Nathan's direction above; context C-06 |
| Branch and PR | `claude/gtwpe-triage-authoring-j94ewf`; draft PR amthorn78/glow-hdengine-v2#826 |
| Expected final output | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.10.md`, with its `.proof-log.md` beside it; TW-APPLY-10 derives the name |
| Apply diagnostic path | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-apply-diagnostic.gtwpe-20261101-pf10-v14-0-5.md` |

## 2. Application contract

* Every operation resolves independently against the unchanged v2.8.9 baseline in §1. Apply all five in one pass by their baseline-bound positions; nothing is rematched on mutated text.
* Operations used: `REPLACE` (four) and `INSERT` (one). No `DELETE`, `FIND AND REPLACE` or `FIND_AND_REPLACE` operation is used.
* `REPLACE`: the old block occurs exactly once in the whole baseline and is replaced by the replacement block. Nothing outside the old block is consumed.
* `INSERT`: the BEFORE anchor and the AFTER anchor each occur exactly once in the whole baseline and are contiguous. Their boundary is the gap. Neither anchor changes. The inserted text supplies every newline at the gap.
* Payload literals use the same convention as the `drain-1` package. Each literal sits in a fenced block that opens with a line of exactly four backticks followed by `text` and closes with a line of exactly four backticks. The literal is the bytes strictly between the line feed that ends the opening fence line and the line feed that immediately precedes the closing fence line. Trailing spaces are significant. Every literal states its UTF-8 byte length and SHA-256; a mismatch is an authoring defect for the preparer.
* Non-overlap: the five spans are disjoint, and the insertion gap touches no replaced span.
* Document-control fields are reserved for TW-APPLY-10. No redline edits baseline lines 5–10. Baseline values: `PF04-Canon-HDE-Governance`, `v2.8.9`, `Canon`, `2026-11-02`, `BN 14.0.5`, `` `INV-f2ac55d77ce9aacc` ``. The source that justifies this update is `PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5, the only source.
* Change history. RL-05 adds the PF04 §9.3.1 entry that §9.3 requires. It names v2.8.10 (v2.8.9 bumped once by the log's patch scheme) and 2026-11-02, the preparation date. If TW-APPLY-10 derives a different version, the package returns to its preparer.
* Hygiene. The baseline carries no `Draft` status language, TODO, unresolved drafting note or editorial comment outside canon-required template or history text (`drain-1` proof log §6; the baseline differs from the original only by verified payloads). No hygiene redline is included.

## 3. Redlines

### RL-01 — REPLACE

- Operation: `REPLACE`
- Ledger rows: C-02 (2.1 D-2, PF04's share), added to T-01 by Nathan's direction of 2026-11-02; context C-06
- Change type (report classification): CANON_UPDATE
- Location (baseline heading path): "# **11\. Vendor Ingest Governance (HDAPI) \[Required-Now\] / \[Speculative\]**" > "## **11.1 Vendor request governance and exact-byte ownership \[Required-Now\]**" > "### **11.1.1 Vendor route family, resource path, and base URL posture**", list item beginning "* **Base-URL and route-policy governance:**"
- Baseline lines (informative only, not a locator): 4075
- Scope: whole PF; expected occurrences: old block 1; observed: old block 1 / 1
- Controlling source: HDE Build Notes v14.0.5, 2.1 D-2 (lines 277-344): "What governs", "Selection", "No fallback" and "The two canon rules fit together"; supporting HDE CLI/API/Vendor Ref §7.1.10 on main
- Effect: States the single permitted terminal-segment classification and its scope, keeps the remaining version-string prohibitions and routes exact bytes to PF05.

- Old block (341 bytes, SHA-256 `580a7361289765d1b4041a60019b55df52fd9c2a1204f4c4add5b7ee935b30da`):

````text
* **Base-URL and route-policy governance:** one explicit route policy MUST select the route family. Ambiguous configuration MUST fail closed before network I/O. Runtime code MUST NOT infer auth family or resource policy from string checks for vendor API-version path segments. Exact base-URL and resource-path behavior is governed by PF05.  
````

- Replacement block (1297 bytes, SHA-256 `d6d9d1340d01271144e97ee52f22a334e3ed57482eec48cdd1b4aab49fc169cb`):

````text
* **Base-URL and route-policy governance:** one explicit route policy MUST select the route family for every resolver-selected vendor acquisition: `bg:resolve --source vendor`, and compat chart acquisition by `hdctl showcompat` and conjunction. Ambiguous configuration MUST fail closed before network I/O. The single permitted reading of a version from the configured base is one exact, case-sensitive comparison of its validated terminal segment against `v1` and `v2`, made once before any route is built: `v2` selects the chart route family and `v1` selects the retained legacy BodyGraph route family. Every other base, including an unversioned base, another version, a nonterminal or case-variant marker and multiple markers, fails closed before credential projection or any network I/O; no non-v2 base reaches the legacy route by fallback. The selected route's resource, payload family and credential projection then come from its contract metadata. Runtime code MUST NOT otherwise infer auth family or resource policy from vendor API-version strings: no version route constants, no appended or normalized version, no auth selected by path prefix and no other runtime behavior keyed on a version string. Exact base-URL boundary, refusal codes and resource-path behavior are governed by PF05.  
````

### RL-02 — REPLACE

- Operation: `REPLACE`
- Ledger rows: C-02 (2.1 D-2, PF04's share), added to T-01 by Nathan's direction of 2026-11-02; context C-06
- Change type (report classification): CANON_UPDATE
- Location (baseline heading path): "# **11\. Vendor Ingest Governance (HDAPI) \[Required-Now\] / \[Speculative\]**" > "## **11.1 Vendor request governance and exact-byte ownership \[Required-Now\]**" > "### **11.1.1 Vendor route family, resource path, and base URL posture**", paragraph beginning "**`bg:resolve --source vendor` route-policy governance.**"
- Baseline lines (informative only, not a locator): 4078
- Scope: whole PF; expected occurrences: old block 1; observed: old block 1 / 1
- Controlling source: HDE Build Notes v14.0.5, 2.1 D-2: "The v1 path is retained legacy selection, not fallback", "Classification label" and "Left undecided" (retirement)
- Effect: Renames the v1 category, records the unchanged evidence label and the retirement rule; the rest of the paragraph is unchanged.

- Old block (452 bytes, SHA-256 `2e2e0ccc98f2bcc98b2674407b6b6bddec84493fc608c319d7f3be818698f7ab`):

````text
**`bg:resolve --source vendor` route-policy governance.** `bg:resolve --source vendor` remains an HD Engine workflow for resolving BodyGraph details. Future claims that this workflow works as a canonical vendor-backed BodyGraph-resolution path require an explicit vendor-route policy. The policy must classify the selected behavior as v2 chart-backed BodyGraph resolution, explicit legacy BodyGraph fallback, dual-route policy, or unsupported nonclaim.
````

- Replacement block (768 bytes, SHA-256 `0109d9bc0beed38e4588598087d90761a547f6789215ff3a9bb28ef74681d04c`):

````text
**`bg:resolve --source vendor` route-policy governance.** `bg:resolve --source vendor` remains an HD Engine workflow for resolving BodyGraph details. Future claims that this workflow works as a canonical vendor-backed BodyGraph-resolution path require an explicit vendor-route policy. The policy must classify the selected behavior as v2 chart-backed BodyGraph resolution, terminal-v1 legacy BodyGraph selection, dual-route policy, or unsupported nonclaim. Terminal-v1 selection is retained legacy selection, not fallback. Governed evidence keeps its existing classification label `explicit_legacy_fallback` unchanged as a wire value; the label names that selection and makes no fallback claim. Retiring the v1 legacy route needs its own separately versioned decision.
````

### RL-03 — REPLACE

- Operation: `REPLACE`
- Ledger rows: C-02 (2.1 D-2, PF04's share), added to T-01 by Nathan's direction of 2026-11-02; context C-06
- Change type (report classification): CONSISTENCY
- Location (baseline heading path): "# **11\. Vendor Ingest Governance (HDAPI) \[Required-Now\] / \[Speculative\]**" > "## **11.1 Vendor request governance and exact-byte ownership \[Required-Now\]**" > "### **11.1.1 Vendor route family, resource path, and base URL posture**", paragraph beginning "A future mapped-cache persistence slice MUST NOT simply turn on writes."
- Baseline lines (informative only, not a locator): 4086
- Scope: whole PF; expected occurrences: old block 1; observed: old block 1 / 1
- Controlling source: HDE Build Notes v14.0.5, 2.1 D-2: "No fallback", the retained v1 selection, and "Consequences" (the EPIC038 mapped-cache predicate runs on a terminal v1 base)
- Effect: Replaces the last clause only.

- Old block (659 bytes, SHA-256 `8b79e7ed222231f44cbfafaa93bdd4c0e7c54aeb68f373f28f925b923ac3ec96`):

````text
A future mapped-cache persistence slice MUST NOT simply turn on writes. It must design and prove a safe persistence path that writes adapter-mapped HDE data, not raw HumanDesignAPI v2 envelopes, raw vendor response bodies, raw request bodies, plaintext secrets, or uncontrolled vendor payloads. The proof must cover mapped-cache write, mapped-cache read-back, canonical-equivalence between pre-write mapped output and post-read cached output for governed fields, idempotence for repeated writes of the same normalized identity, no raw vendor-payload persistence, closed-rails refusal before outbound I/O, and preservation of explicit legacy fallback behavior.
````

- Replacement block (667 bytes, SHA-256 `9915ed694677a5261896d66e90eb5ac340dec40d1bc65b62186f12b1d8ed5022`):

````text
A future mapped-cache persistence slice MUST NOT simply turn on writes. It must design and prove a safe persistence path that writes adapter-mapped HDE data, not raw HumanDesignAPI v2 envelopes, raw vendor response bodies, raw request bodies, plaintext secrets, or uncontrolled vendor payloads. The proof must cover mapped-cache write, mapped-cache read-back, canonical-equivalence between pre-write mapped output and post-read cached output for governed fields, idempotence for repeated writes of the same normalized identity, no raw vendor-payload persistence, closed-rails refusal before outbound I/O, and preservation of the retained terminal-v1 legacy selection.
````

### RL-04 — REPLACE

- Operation: `REPLACE`
- Ledger rows: C-02 (2.1 D-2, PF04's share), added to T-01 by Nathan's direction of 2026-11-02; context C-06
- Change type (report classification): CONSISTENCY
- Location (baseline heading path): "# **11\. Vendor Ingest Governance (HDAPI) \[Required-Now\] / \[Speculative\]**" > "## **11.1 Vendor request governance and exact-byte ownership \[Required-Now\]**" > "**11.1.6 Acceptance (binary)**" list, item 1 (the "11.1.6" label is a bold list line under "### **11.1.5 Rails coupling (pointer)**", not a Markdown heading)
- Baseline lines (informative only, not a locator): 4139
- Scope: whole PF; expected occurrences: old block 1; observed: old block 1 / 1
- Controlling source: HDE Build Notes v14.0.5, 2.1 D-2: "The two canon rules fit together" (the single permitted reading; every other version-string inference stays prohibited)
- Effect: Aligns the acceptance item with RL-01.

- Old block (132 bytes, SHA-256 `ced072e7456d90f62f96f07082de2efd4d9429c7ceb94321663444c679236b96`):

````text
1. **Explicit route policy:** one route policy is selected, and no route or auth family is inferred from an API-version substring.  
````

- Replacement block (207 bytes, SHA-256 `47b0843f1d92826ee06d579dbc44d8f0b2f421603813f996b3d1949f5a89d6e4`):

````text
1. **Explicit route policy:** one route policy is selected by the single permitted terminal-segment classification of §11.1.1, and no route or auth family is otherwise inferred from an API-version string.  
````

### RL-05 — INSERT

- Operation: `INSERT`
- Ledger rows: PF04 §9.3 change-history rule, for C-02
- Change type (report classification): DOC_HYGIENE (required change-history entry)
- Location (baseline heading path): "# **9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]**" > "> ## **9.3 Doc-Delta entries (what to record for any normative change)**" > "> ### **9.3.1 PF04 Governance Change Log \[Required-Now\]**"
- Baseline lines (informative only, not a locator): gap between 2736 and 2737
- Scope: whole PF; expected occurrences: gap 1 (BEFORE and AFTER each 1, and contiguous 1); observed: BEFORE 1, AFTER 1, gap 1 / 1, 1, 1
- Controlling source: PF04 §9.3 and §9.3.1 (every normative PF04 change adds a Doc-Delta entry; NON_EPIC class; GOV-YYYYMMDD-<shortslug>, unique)
- Effect: Adds the v2.8.10 entry after the v2.8.9 entry, in the log's own format.

- BEFORE anchor (612 bytes, SHA-256 `c9970ccbc5a3ae3dd4fd7d793345ff59bf03126dd1e3d56a83c1771e6497bc84`):

````text
> Change Log entry (one line): v2.8.9 | GOV-20261102-gtwpe-pf04 | NON_EPIC | Scope: Live compat test for every Epic and Product Owner-only waiver; GATE:CORE-DET evidence and retired entries; compat namespace as a dev/admin surface; sanity-pipeline log-path bound; governed gate check rows; planning-document and PF-version independence; v2 close-run evidence and tracked-issue IDs | Targets: §2.0.10, §2.0.19, §3.4, §4.1.4, §4.1.8, §9.1.2, §9.1.3, §12.2, Appendices B.2/D.1/D.3 | Acceptance: LOGS_KEYS_ONLY_OK | Evidence: None | Freeze-pack: No | Canonical record: PF04 §9.3.1 / GOV-20261102-gtwpe-pf04

````

- AFTER anchor (57 bytes, SHA-256 `66c397ea614cb823ef0c1a7d7b7d6c495c250953ed3b8f37b56f4db9b11fa094`):

````text


> ---

> ## **9.4 Doc-Delta template \[Required-Now\]**
````

- Inserted text (3418 bytes, SHA-256 `8d75c68a5c4a8b257377dce5906be1e6ab7699f814a61d5f4d6cbf97c6acd274`):

````text

v2.8.10 | GOV-20261102-gtwpe-pf04-route | NON_EPIC | Scope: Vendor route selection by the configured base's terminal v1 or v2 segment; terminal-v1 legacy selection, not fallback | Targets: §11.1.1, §11.1.6 | Acceptance: None | Evidence: None | Freeze-pack: No | Canonical record: PF04 §9.3.1 / GOV-20261102-gtwpe-pf04-route

> DOC-DELTA-ID: GOV-20261102-gtwpe-pf04-route
>
> Date / Author: 2026-11-02 / executing document agent in Nathan's T-01 document session (follow-up for vendor route selection)
>
> PF04 version: v2.8.10
>
> Record class: NON_EPIC
>
> Epic ID: NOT APPLICABLE - NON_EPIC
>
> Draft / binding surface: NOT APPLICABLE - NON_EPIC
>
> Stable record surface: PF04 §9.3.1 / GOV-20261102-gtwpe-pf04-route
>
> Scope: Vendor Ingest; Governance/Documentation
>
> Targets (section anchors): §11.1.1, §11.1.6
>
> Summary (≤ 5 bullets):
>
> 1) For every resolver-selected vendor acquisition (`bg:resolve --source vendor`, and compat chart acquisition by `hdctl showcompat` and conjunction), state the single permitted classification of the configured base's terminal segment: `v2` selects the chart route family, `v1` the retained legacy BodyGraph route family, and every other base fails closed before credential projection or any network I/O.
> 2) Name terminal-v1 selection as retained legacy selection, not fallback; keep the governed-evidence label `explicit_legacy_fallback` unchanged; leave v1 retirement to a separately versioned decision.
> 3) Align the mapped-cache proof obligation and the §11.1.6 route-policy acceptance item with that classification.
>
> Acceptance impact (binary gates to update or verify): §11.1.6 item 1 accepts the single terminal-segment classification and still rejects any other route or auth inference from an API-version string. The other vendor-governance acceptance items and the A3, A4, A7 and rails gates are unchanged. No new or satisfied token, QA verdict, OPS result or acceptance decision is claimed.
>
> Evidence updates (titles and paths only): No governed evidence artifact, golden, script, header snapshot, CI job, Human Evidence Index, hash sentinel, Machine Mirror or path proof is created or regenerated by this document revision. The governed-evidence label `explicit_legacy_fallback` and the evidence that carries it are unchanged.
>
> Freeze-pack impact: No; this document revision cuts, recomputes, activates and promotes no release and changes no release member.
>
> Routing (titles only confirmations): HDE CLI/API Vendor Ref owns route selection bytes, the configured-base boundary and the refusal codes. HDE Mechanics Guide owns the remaining version-string prohibitions. HDE Build Notes supplies the scoped override.
>
> Rollout plan: Nathan's authorized publication of the complete revised PF is a separate manual action. No runtime staging, canary, deployment or pointer flip is performed by this revision. A document backout uses the retained v2.8.9 source through ordinary authorized publication. Runtime monitoring and rollback retain their existing owners and controls.
>
> Change Log entry (one line): v2.8.10 | GOV-20261102-gtwpe-pf04-route | NON_EPIC | Scope: Vendor route selection by the configured base's terminal v1 or v2 segment; terminal-v1 legacy selection, not fallback | Targets: §11.1.1, §11.1.6 | Acceptance: None | Evidence: None | Freeze-pack: No | Canonical record: PF04 §9.3.1 / GOV-20261102-gtwpe-pf04-route

````

END OF REDLINES
