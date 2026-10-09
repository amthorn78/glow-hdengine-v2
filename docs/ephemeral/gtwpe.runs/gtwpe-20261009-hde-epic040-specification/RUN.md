# RUN — GTWPE-FLOW-10 — `gtwpe-20261009-hde-epic040-specification`

## Run identity
- Run ID: `gtwpe-20261009-hde-epic040-specification`
- Flow prompt: GTWPE-FLOW-10 — Run the Technical Writing Flow — 100726.2, Notion page `3f24590a05eb813aa28ed6da399447d0`
- Execution prompt: `inputs/execution-prompt.md` (this run directory)
- Run directory: `docs/ephemeral/gtwpe.runs/gtwpe-20261009-hde-epic040-specification/`
- Branch: `docs/20261009-gtwpe-run-hde-epic040-specification`
- Intake commit (`origin/main`): `0c4dddece401c457b2429ddc9cb8f2e819b4a943`
- Pull request: #594 — `https://github.com/amthorn78/glow-hdengine-v2/pull/594` (draft, opened at B1)

## Notion edit times read at B1
- `AI Prompts / HDE TW` (`3c74590a05eb8176baf8cb59f1631f3c`): `2026-10-07T18:30:00.000Z`
- `AI Prompts / HDE TW / GTWPE — Glow Technical Writing Prompt Ecosystem` (`3ea4590a05eb818c915bdfd3d150c44b`): `2026-10-07T18:28:00.000Z`

## Inputs (B1)
- Governing specification: `docs/ephemeral/HDE-EPIC040-specification-v1.1-approved.md` (blob `e203c84c91e5584d55fcca03beadad00b57f4539`)
- Sources:
  - `docs/ephemeral/HDE-EPIC040-CL-E-10-closure-decision-v1.2.md` (blob `34c17fc52a751b7a4627165673cc2d08336daa66`)
  - `PF10-HDE-Build-Notes` in `docs/pfcanon/` → `docs/pfcanon/PF10-HDE-Build-Notes-v13.5.md` (blob `5937f0186298423052864822ec10500d9602115d`)

## Canon sources (base blob at intake)
- `docs/pfcanon/PF10-HDE-Build-Notes-v13.5.md` — `5937f0186298423052864822ec10500d9602115d`

## Triage
- Pass: TW-TRIAGE-10 — Identify PF10 Drain Targets — 100726.1 (Notion `3f24590a05eb8129b8e5e8328f9a3c3d`), read for this pass.
- Triage file: `passes/triage/01-tw-triage-10/triage.md` (this run directory).
- Outcome: every change accounted for (38 PF10 addenda; closure decision §5; spec §10.3 ADR C040-01–04). No change is held back (HDE-EPIC040 is shown `CHANGE_CLOSED`; the general PF10-* addenda are repo-wide rules).

## Routed documents (B1 step 6)

Route: general `Canon` PF → TW-DRAIN-10 → TW-APPLY-10; each PF09 phase file → TW-DRAIN-20 → TW-APPLY-10; PF20 → TW-RECORD-10.

| Document (canon name) | Canon path | Base blob | Route |
| --- | --- | --- | --- |
| HDE Math Spec | `docs/pfcanon/PF01-Canon-HDE-Math-Spec-v1.3.7.md` | `ba07b5606153cadd033e41b1a8aafb967af10ea1` | TW-DRAIN-10 |
| HDE Architecture | `docs/pfcanon/PF02-Canon-HDE-Architecture-v2.4.5.md` | `f74aace7d277047c9a0198043cdd89289288f11c` | TW-DRAIN-10 |
| HDE Governance | `docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.6.md` | `4b591acb98b4aeba001703eeecb64dccd9248afe` | TW-DRAIN-10 |
| HDE CLI/API Vendor Ref | `docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.2.md` | `787d21b9672b04095fe97d6722db3389e450ce21` | TW-DRAIN-10 |
| Change Process Guide | `docs/pfcanon/PF06-Canon-Change-Process-Guide-v2.5.3.md` | `f88834dae33ed5b1cb9a43e2349748fb9e2f00de` | TW-DRAIN-10 |
| Glow Infrastructure | `docs/pfcanon/PF07-Canon-Glow-Infrastructure-v2.3.2.md` | `023ecf8eb7bdd9e7b1debb275b853b157fb61efb` | TW-DRAIN-10 |
| HDE Schemas and Artifacts | `docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.5.md` | `743dd905132a2e9c1269dcffb55a440164af7bac` | TW-DRAIN-10 |
| HDE Mechanics Guide | `docs/pfcanon/PF14-Canon-HDE-Mechanics-Guide-v3.5.7.md` | `c23677cb3c7d06630f99dee16ecb5ad3ef3b42f6` | TW-DRAIN-10 |
| Glow QA Guide | `docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.5.md` | `fbc43d2b7270acb47b5f8e765af60d62e35b8418` | TW-DRAIN-10 |
| Reality Audits | `docs/pfcanon/PF23-Canon-Reality-Audits-v1.2.1.md` | `8552b26c62f4df4aef85d9d749c601a9db012dd3` | TW-DRAIN-10 |
| Plan Templates | `docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.4.md` | `ef3ddbf236a37a8bf5d2946ded25254cf0f25529` | TW-DRAIN-10 |
| HDE Build Checklist — Calcination | `docs/pfcanon/PF09.1-Canon-HDE-Build-Checklist-Calcination-v1.1.5.md` | `f586506c53cae5a7524bead233ff6d1009937f1f` | TW-DRAIN-20 |
| HDE Build Checklist — Separation | `docs/pfcanon/PF09.3-Canon-HDE-Build-Checklist-Separation-v1.1.5.md` | `593c06bb6ae889ebb39f1f5c1f32231838d71eec` | TW-DRAIN-20 |
| HDE Build Checklist — Conjunction | `docs/pfcanon/PF09.4-Canon-HDE-Build-Checklist-Conjunction-v1.2.md` | `5a97004918e15b5f5783869fd1d2de7d68b4df9f` | TW-DRAIN-20 |
| HDE Build Checklist — Fermentation | `docs/pfcanon/PF09.5-Canon-HDE-Build-Checklist-Fermentation-v1.5.md` | `f735f1636b2dc201365d73c592ee7e581059fde4` | TW-DRAIN-20 |
| HDE Build Checklist — Coagulation | `docs/pfcanon/PF09.7-Canon-HDE-Build-Checklist-Coagulation-v1.1.5.md` | `74f117ed417dae49e53c0636358a0dc6f7cbbfb4` | TW-DRAIN-20 |
| HDE Phased Epics (Epic record) | `docs/pfcanon/PF20-Reference-HDE-Phased-Epics-v1.9.5.md` | `cccc0a48396bae8d28dfe31d66c1f8a3f113694a` | TW-RECORD-10 |

## Held-back changes
- None. HDE-EPIC040 is `CHANGE_CLOSED`; no change belongs to an unclosed epic or CRD.

## Changes that cannot drain in this run (no eligible home)
- Addendum 2.1 operating rules (Notion board location/roles/routing/pointer policy): no fixed eligible home (undecided).
- Addendum 2.8 (FORM-001), addendum 2.14 (spec format authority), DD-12, and the PF10-internal legs of 2.29 and 2.38: PF10 itself is never a target.
- CC-4 (closure-evidence prompt path): process, routed to GCFPE-MGMT-10, not PF canon.
- DD-05, DD-08, DD-09, DD-10, DD-11: repository (non-PF) documents.
- DD-06: ephemeral record (no drain target).

## Passes
- `01-tw-triage-10` (TW-TRIAGE-10, 100726.1): inputs = every input file (PF10, closure decision, specification, PF03); output = `passes/triage/01-tw-triage-10/triage.md`; return = triage file path; committed with the routing update below.

## Boundaries
- B1 Scope: complete (intake, Notion edit times, branch/run dir/PR, triage, routing).
- B2 Redlines / B3 Drafts / B4 Document control / B5 Consistency / B6 Complete: not reached.

## Stop (S1 — capacity)
- Signal: S1 (capacity). B2–B6 require reading each of 17 target documents completely and running its drain/record + apply passes at full quality, which cannot be finished in this session's remaining context.
- What is done: B1 intake (branch `docs/20261009-gtwpe-run-hde-epic040-specification`, run directory, RUN.md, inputs, draft PR #594), the triage pass and its file, and the routing of 17 documents with base blobs.
- What is not: B2 redlines, B3 drafts, B4–B6 checks and review for the 17 routed documents.
- Resume point: continue at B2 (Redlines), one writing pass at a time, from the routed-document table above; each pass re-checks the base blobs recorded here against `origin/main`.

## Harness prompt-body reads
- GTWPE-FLOW-10 (100726.2), Notion `3f24590a05eb813aa28ed6da399447d0`, read at B1.
- TW-TRIAGE-10 (100726.1), Notion `3f24590a05eb8129b8e5e8328f9a3c3d`, read for the triage pass.
- (No TW prompt body was written to a file, hashed, or compared; each is read live from Notion per pass.)
