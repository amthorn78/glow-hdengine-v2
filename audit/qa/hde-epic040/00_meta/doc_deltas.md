# HDE-EPIC040 Step-0B doc deltas (QA_PLAN v1.0, docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.0.md)

## BLOCKERS

none

## CAVEATS

| ID | Class | Delta | Drain target (title) | Owner | Drives decision |
| --- | --- | --- | --- | --- | --- |
| DD-01 | CAVEAT | QA Codespaces inventory lists retired `DB_BRIDGE_URL` (QA50-F14) | PF07-Canon-Glow-Infrastructure §2.4 | PF07 maintainer | No |
| DD-02 | CAVEAT | PF07 §2.8 forbids git operations and QA-time scripts; PF19 §3.4.9 and PF27 permit read-only observations and embedded harness calls (C040-09, PROPOSED) | PF07-Canon-Glow-Infrastructure §2.8 | PF07 maintainer | No |
| DD-03 | CAVEAT | PF19 §§3.4.3, 3.6, 10.8 and AGENTS.md name ChatGPT Library or Google Drive for authored plans and canon; D7 and the QA prompts use `docs/ephemeral/` and `docs/pfcanon/` (QA50-F13) | PF19-Canon-Glow-QA-Guide §§3.4.3, 3.6, 10.8; AGENTS.md | PF19 maintainer; repository docs owner | No |
| DD-04 | CAVEAT | PF05 §7.1.11 `--allow-prod-vendor` is not implemented (QA50-B01) | PF05-Canon-HDE-CLI-API-Vendor-Ref §7.1.11 | PF05 and CLI owners | No |
| DD-05 | CAVEAT | AGENTS.md cites "PF10 §2.8" for the bounded PF-copy rule; its v13.3.9 home is PF19 §10.8 (QA50-F12) | AGENTS.md | Repository docs owner | No |
| DD-06 | CAVEAT | Guide §8 names `6e4b3a1` as the attestation candidate; the attestation binds `6f53d82` (QA50-F11) | None (ephemeral record) | Isis | No |
| DD-07 | CAVEAT, carried | C040-05 to C040-08 drainage pending (RA-18) | Per register, QA Audit §11 | Named maintainers | No |
| DD-08 | CAVEAT, carried | `showcompat` help says Reader v1 (O-P07-01) | Repository CLI help | Whole-change IA | No |
| DD-09 | CAVEAT, carried | `APP_ENV` asymmetry between dev `GET /reader` and conjunction routes (O-P07-04, RA-06) | O-P07-04 record | Whole-change IA | No |
| DD-10 | CAVEAT, carried | `ci/checks/check_mirror_schema.sh` is Python; AGENTS.md invocation (RA-13) | AGENTS.md | Repository docs owner | No |
| DD-11 | CAVEAT, carried | `docs/ADAPTER_009.md:174` says `body_not_allowed`; code emits `invalid_json` (FND-017) | `docs/ADAPTER_009.md` | Compat docs owner | No |
| DD-12 | CAVEAT, carried | PF10 v13.3.9 §2.28 line references to §2.19 and §2.20 are off by two | PF10-HDE-Build-Notes §2.28 | PF10 drain owner | No |

