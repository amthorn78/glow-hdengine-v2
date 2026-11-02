# Redlines: PF02-Canon-HDE-Architecture v2.4.7 (gtwpe-20261101-pf10-v14-0-5, T-09)

## Identity

| Field | Value |
| :---- | :---- |
| Run identity | `gtwpe-20261101-pf10-v14-0-5` / T-09 / preparation revision `r1` |
| Prompt | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1 (Notion page `3f44590a05eb8172a314fe6b958bb9ff`) |
| Preparer | The T-09 document session Nathan started (Claude Code, https://claude.ai/code/session_01Q789u3YHoFbcNNPspHj1tZ), 2026-11-02 |
| Preparation outcome | `READY` |
| Target (original baseline) | `docs/pfcanon/PF02-Canon-HDE-Architecture-v2.4.7.md`, in-document title `PF02-Canon-HDE-Architecture`, version v2.4.7; read at `origin/main` `e2b7427ff418ca8f08f05587c4a541308a76da56`; git blob `9a23eec67198b86768d3b7fcef2e1b864cb9d998`; SHA-256 `fc0001e215e5a42bcf91f1e043f0f88a94867e00edae2ab387535869b855a149`; 142,444 bytes; 1,624 lines |
| Change source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5; git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`; addendum 2.4 (lines 673–753) and addendum 2.5 (lines 754–883) |
| Triage ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md` at `142feb35144d8795f927e0c78b665ace52279064`; task T-09; rows C-13, C-14; supporting C-12, C-16, C-21 |
| Proof log | `PF02-Canon-HDE-Architecture-v2.4.7.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md`, beside this file |

## Document-control fields for TW-APPLY-10

These redlines do not edit the header. TW-APPLY-10 derives the revised document-control values under its header contract.

- Native header schema of the baseline, in order: `**Title:**` `PF02-Canon-HDE-Architecture`; `**Version:**` `v2.4.7`; `**Status:**` `Canon`; `**Effective date:**` `2026-10-26`; `**Last Update Gate:**` `BN 13.8.8`; `**Invocation tag:**` `INV-f2ac55d77ce9aacc`.
- Version scheme in use: `v<major>.<minor>.<patch>`. A patch bump gives v2.4.8.
- Sources that justify the update, in source order: `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, version v14.0.5.
- PF02 has no change log, revision history or Doc-Delta entry format, so no history redline is prepared.
- PF02 carries no `Draft` status language, placeholder, TODO, drafting note or instruction to a future writer that this rule would remove. Lines 181 and 1225 mention placeholders as canon rules, not as markers.

## Redlines

### RL-01

- Redline number: RL-01
- Findings or source items: DELTA-001 (HDE Build Notes addendum 2.4, lines 707, 723 and 729; addendum 2.5, line 853). Ledger rows C-13 and C-14.
- Change type: CANON_UPDATE
- Operation: `REPLACE`
- Target document: PF02-Canon-HDE-Architecture
- Section path: `# 1\. Architectural Principles \[Required-Now\]` > `## 1.1 Single homes`
- Original location: line 198, the paragraph that begins `**Non-BodyGraph chart loader classification \[Required-Now\].**`
- Scope: whole document. Expected occurrences of the old block: 1.
- Controlling basis: HDE Build Notes v14.0.5, addendum 2.5 "Required canon drainage", DELTA-001: "after delivery and acceptance, replace \"remains current repository reality until separately remediated\" with the delivered boundary". Addendum 2.4 records the removal of `engine/charts/loader.py` with no shim.
- Rationale: the paragraph describes a module that no longer exists as current repository reality. HDE-EPIC041 delivered and closed the boundary (addendum 2.10), so the paragraph keeps its normative classification and states the inspected current boundary instead.
- Action: `REPLACE` ONCE the exact old block below with the exact replacement block below. The old block is the whole of line 198 without its line ending. The blank lines before and after it (lines 197 and 199) are not part of the old block and stay unchanged.
- Uniqueness: section-path matches=1; old block matches in the whole document=1.

Old block (exact literal; the content between the fence lines, without the newline that precedes the closing fence):

````text
**Non-BodyGraph chart loader classification \[Required-Now\].** At repository commit `5ef911fec556a6c24bda8196b085f43c2da02150`, `engine/charts/loader.py` is implementation drift, not a sanctioned Engine I/O seam. Environment and rails evaluation, provider selection, chart acquisition, clocks, correlation context, operational logging, and filesystem writes belong to Adapter-owned application or infrastructure orchestration and must use the existing sanctioned BodyGraph resolver/ingest boundary where vendor or database acquisition is required. Pure chart validation or normalization may remain under Engine ownership only as explicit data-in/data-out computation with no time, randomness, environment, network, provider, logging, or filesystem side effects. The checked-in loader remains current repository reality until separately remediated; this classification does not claim that relocation, caller migration, or removal has occurred. The BodyGraph seam carve-out does not relax purity for Engine Core, sampler core, or other deterministic compute modules.
````

Replacement block (exact literal; the content between the fence lines, without the newline that precedes the closing fence; its two internal blank lines separate three paragraphs):

````text
**Non-BodyGraph chart loader classification \[Required-Now\].** Non-BodyGraph chart loading is not a sanctioned Engine I/O seam. Environment and rails evaluation, provider selection, chart acquisition, clocks, correlation context, operational logging, and filesystem writes belong to Adapter-owned application or infrastructure orchestration and must use the existing sanctioned BodyGraph resolver/ingest boundary where vendor or database acquisition is required. Pure chart validation or normalization may remain under Engine ownership only as explicit data-in/data-out computation with no time, randomness, environment, network, provider, logging, or filesystem side effects. The BodyGraph seam carve-out does not relax purity for Engine Core, sampler core, or other deterministic compute modules.

**Current repository behavior \[Implemented\].** At repository commit `e2b7427ff418ca8f08f05587c4a541308a76da56`, `adapter/chart_orchestration.py` is the Adapter-owned chart orchestration entry. It owns the `SAFE_MODE` read, both clocks, the correlation identifier, the repository-root-anchored pinned-list reads, fixture chart acquisition, and one keys-only log line per call to an injectable sink; it writes no file and delegates validation and normalization to the pure Engine interface. `engine/charts/pure.py`, the only tracked file under `engine/charts/`, holds that interface. `engine/charts/loader.py`, which this classification identified as implementation drift at repository commit `5ef911fec556a6c24bda8196b085f43c2da02150`, is removed with no compatibility shim. A tracked import-guard test is written to fail if that module path or an import of it returns; guard and purity-test mechanics are owned by **HDE-Mechanics Guide**. The supported chart path acquires only a fixture chart, so it makes no vendor or database acquisition and does not engage the BodyGraph resolver/ingest boundary.

**Static inspection cannot establish.** Static repository bytes do not establish runtime reachability, test passage, deployment, or production enablement for the chart path.
````

## Batch validation summary

- One actionable redline. No other operation exists, so no overlap, shared gap or chained locator is possible.
- RL-01 resolves to one span in the unchanged original: line 198, bytes as recorded in the proof log.
- The replacement block does not contain the old block, and contains no ellipsis character and no three consecutive full stops.

END OF REDLINES
