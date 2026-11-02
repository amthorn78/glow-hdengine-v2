# Proof log — PF04-Canon-HDE-Governance v2.8.9 redlines — gtwpe-20261101-pf10-v14-0-5 (T-01 follow-up: vendor route selection)

## 1. Artifact and identity

| Field | Value |
| :---- | :---- |
| Artifact this log documents | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.9.redlines.gtwpe-20261101-pf10-v14-0-5.md` (20,353 bytes; SHA-256 `b5804e9aa3add4973b56f4ccec4da22de985762d74be025ea88d3e6c54658d32`) |
| This log | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.9.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md` |
| Run identity | `gtwpe-20261101-pf10-v14-0-5/T-01/drain-2`, prepared 2026-11-02 |
| Preparation outcome | `READY` |
| Save completeness | Recorded in §9 after read-back. |
| Authorization | In the T-01 session's final report, Nathan was asked whether PF04 §11.1.1 should take 2.1 D-2, which no task routed to PF04. On 2026-11-02 he chose option A: "yes, proceed with A". That adds C-02's PF04 share to T-01. |
| Prompt | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1, Notion page `3f44590a05eb8172a314fe6b958bb9ff` (page last edited 2026-10-09T11:05:22.094Z), fetched live again when this step began; the page state is the same one `drain-1` used |
| Originating preparer | The executing document agent in the Claude Code session Nathan started for T-01 (session `session_01Q789tyrM8bruo2RGNCMLM8`). No subagent, reviewer or other session took part. |
| Correction route | An Apply diagnostic returns to this preparer in this session as `drain-3` |

## 2. Sources, inputs and roles

| Input | Identity | Role |
| :---- | :---- | :---- |
| Baseline | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.9.md` at `b489215f82aa156ae49a66284330afb47aa00c21`; v2.8.9; git blob `cc46c5ac0108fc5a3a2eed1e0fdeb4b9518a2e76`; SHA-256 `a92dda98a5b2037e90f898033674721a12e21243242131b3fa063ab3e167125c`; 596,102 bytes; 4,821 lines | Application baseline: TW-APPLY-10's verified output of `drain-1`, unpublished |
| Authoritative PF04 | `docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.8.md` on `main` `84d6d1cad95c67788336d174dc4b8922d9bb0cb2` (blob `0c3ce100f9429435bce8e021f36e405120159e4a`) | Current authority. v2.8.9 differs from it only by `drain-1`'s verified payloads and header fields. |
| Change source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5; blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d` | Unchanged on `main` |
| Supporting reading | HDE CLI/API Vendor Ref §7.1.10 "Endpoint policy (explicit version-gated dual lineage)", `docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.4.md` on `main` (blob `53e6a9028dfa5d79b91e9b98cc949160c5a5cefe`), lines 3472–3504 read in full | Owner of the route-selection bytes, the configured-base boundary and the refusal codes. It already states the terminal `v1`/`v2` rule and "retained legacy selection, not fallback". |
| Editorial standard | PF03 Technical Writing Best Practices v1.8.8 | Read in full in this session (`drain-1`) |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md`; task T-01 | Row C-02 routes 2.1 D-2 to PF05, PF14, PF27 and PF29 (T-02, T-05, T-07, T-08). PF04's share is added to T-01 by Nathan's direction. |

Why chained on v2.8.9: v2.8.9 is not yet published, and a package against v2.8.8 would fork a second v2.8.9. Chaining makes one revised PF, v2.8.10, that carries both runs. If v2.8.9's bytes change before publication, the authority note in the redlines file §1 returns this package for reconciliation.

## 3. Coverage

* Baseline. v2.8.9 equals the original v2.8.8, which was read completely in `drain-1` (eleven windows, 580,196 bytes), plus `drain-1`'s fourteen payloads and three header fields, all authored and verified in this session. TW-APPLY-10's preservation audit proved that composition byte for byte (574,526 untouched bytes and every payload exact). That coverage is reused against this exact baseline. In addition:
  * §11.1 of the baseline (lines 4037–4150) was re-read;
  * the whole baseline was searched for `fallback`, `API-version`, `version path`, `terminal`, `explicit_legacy_fallback`, `PROVIDER_ROUTE`, `route polic`, `route-polic`, `route family`, `route-family` and `bodygraphs`.
* Selected source unit. 2.1 D-2, lines 277–344, read in full in `drain-1`'s first window (205–396, 18,333 bytes), with the 2.1 context (205–224 and 491–516, C-06).

## 4. Change and disposition ledger

| D-2 element | Disposition | Baseline location |
| :---- | :---- | :---- |
| What governs: §7.1.10 governs route selection for `bg:resolve --source vendor` and compat chart acquisition by `showcompat` and conjunction | RL-01 | §11.1.1, line 4075 |
| Selection: terminal case-sensitive `v2` selects charts and `v1` selects bodygraphs; every other base fails before credential projection or any external I/O | RL-01. The refusal code `PROVIDER_ROUTE_UNSUPPORTED` stays with PF05. | line 4075 |
| The base: absolute HTTPS, host, no userinfo, query or fragment, ending in exactly `v1` or `v2` | Routed: RL-01 names PF05 as the owner of the exact base-URL boundary, which PF05 §7.1.10 already states | line 4075 |
| The v1 path is retained legacy selection, not fallback; no non-v2 base reaches bodygraphs by fallback | RL-01 and RL-02 | lines 4075, 4078 |
| The single permitted reading; route metadata from contract; the remaining prohibitions (version constants, appended or normalized versions, auth by path prefix, other runtime behavior keyed on a version string) | RL-01 and RL-04 | lines 4075, 4139 |
| Classification label `explicit_legacy_fallback` kept as an existing wire value that names the v1 selection | RL-02 | line 4078 |
| Mapped-cache proof obligation "preservation of explicit legacy fallback behavior" (the EPIC038 predicate runs on a terminal v1 base, per D-2's consequences) | RL-03 | line 4086 |
| Left undecided: v1 retirement needs a separate, versioned decision | RL-02 | line 4078 |
| PF04 §9.3: every normative change adds a §9.3.1 entry | RL-05 (`GOV-20261102-gtwpe-pf04-route`, v2.8.10) | after line 2736 |
| D-2 drainage targets in other documents (HDE Mechanics Guide §1.1, HDE Users Guide §11.3, §13.3 and §16, HDE CLI/API Vendor Ref §7.1.10 and §7.2.0, Plan Templates, AGENTS.md) | Out of this target: T-05, T-08, T-02, H-09, T-07 and H-05 | — |

Already consistent, so not changed:

* Line 4053: an adapter or schema proof must say "whether any legacy fallback remains". That is a question the proof answers; under D-2 the answer is none.
* Line 4076 (Determinism): auth family comes from governed route or contract metadata.
* Line 4080: appending a legacy resource to a configured v2 base is allowed only where canon explicitly supports it. PF05 §7.1.10 makes a `v2` base select charts, so the condition stays true as written.
* Line 4100 (auth-family mismatch posture): deriving auth from an API-version string is a defect, which D-2 keeps.
* §3.3 (line 1165): the canonical and compatibility base-URL variables, and failing closed on a conflict, agree with PF05.
* §3.4 (line 1222): a legacy-route observation is a bounded gap.

Nothing in D-2 belongs to an Epic or CRD that the inputs do not show closed: 2.1 records Product Owner decisions active from publication (line 211). The implementing change for code conformance is Candidate CRD Items List item 9 (H-10). The drafted text states the requirement and claims no implementation.

## 5. Constraints and interpretations

* HDE Build Notes is not cited in any payload. The existing "PF10 or permanent PF canon" phrase on line 4080 is outside every span and unchanged.
* I-1. D-2's "single permitted reading" is a narrow exception to the prohibition at line 4075, which said "MUST NOT infer auth family or resource policy from string checks for vendor API-version path segments". RL-01 keeps that prohibition for everything else, and keeps the existing "Ambiguous configuration MUST fail closed before network I/O" rule.
* I-2. "Dual-route policy" stays as a category at line 4078, because D-2 does not remove it and line 4080 still governs a configuration that needs both route families.
* I-3. RL-04 changes "API-version substring" to "API-version string" to match RL-01's wording. The meaning does not narrow.

## 6. Repository inspection

None was needed: the payloads name no repository path. Their facts come from D-2 and PF05 §7.1.10. No test or tool was run.

## 7. Producer validation

The build (`tools/build2.py`) and an independent parse of the saved file (`tools/verify_package.py`), both in the session scratchpad, agree:

| ID | Op | Baseline byte span or gap | Occurrences expected / observed | New bytes |
| :---- | :---- | :---- | :---- | ----: |
| RL-01 | REPLACE | 532939–533280 | old block 1 / 1 | 1,297 |
| RL-02 | REPLACE | 533468–533920 | old block 1 / 1 | 768 |
| RL-03 | REPLACE | 535315–535974 | old block 1 / 1 | 667 |
| RL-04 | REPLACE | 541088–541220 | old block 1 / 1 | 207 |
| RL-05 | INSERT | gap at 371282 | BEFORE 1, AFTER 1, gap 1 / 1, 1, 1 | 3,418 |

* Spans are disjoint.
* Dialects: `REPLACE` and `INSERT` only. The RL-045 rule has nothing to apply to.
* Every literal's length and SHA-256 match.
* No four-backtick run and no ellipsis.
* Simulated result, with header fields still at the baseline's values: 600,875 bytes, 4,859 lines, SHA-256 `086d09e4622e6877a50215e745d6e7b6bf04c5337f6e0838c1a805ee1ddbafe9`.

## 8. Header provenance for TW-APPLY-10

* Baseline header (lines 5–10): `PF04-Canon-HDE-Governance`, `v2.8.9`, `Canon`, `2026-11-02`, `BN 14.0.5`, `` `INV-f2ac55d77ce9aacc` ``, in the native `**Field:** value` form.
* Source, in source order: `PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5 (the only source).
* RL-05 names v2.8.10 and 2026-11-02.

## 9. Save verification

Save completeness: `COMPLETE_PACKAGE`. Both files were saved in the working tree of `claude/gtwpe-triage-authoring-j94ewf` and read back completely on 2026-11-02:

* Redlines file: 20,353 bytes, 202 lines, SHA-256 `b5804e9aa3add4973b56f4ccec4da22de985762d74be025ea88d3e6c54658d32`; byte-identical to the built package; it ends with `END OF REDLINES` and one line feed. The independent parse, run against the baseline read straight from commit `b489215`, re-resolved all five operations with the counts in §7 and reproduced the 600,875-byte simulated result.
* This proof log: read back in full after this section was written; its own hash is not recorded inside it.
