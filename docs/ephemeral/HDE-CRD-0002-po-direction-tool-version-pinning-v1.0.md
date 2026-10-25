---
artifact_type: PRODUCT_OWNER_DIRECTION
artifact_id: HDE-CRD-0002-PO-DIRECTION-TOOL-VERSION-PINNING
artifact_version: "1.0"
predecessor: none
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
subject: tool and dependency version pinning
decision_owner: Nathan / Product Owner
decided_at: 2026-10-25 (UTC), in the HDE-CRD-0002 QA-100 execution session below (recorded 2026-10-25T00:15:00Z)
recorded_by: the HDE-CRD-0002 QA-100 executor, Claude Code CLI agent (Claude Opus 5.5), local session abab87ae-fdb9-4eb6-b2b9-de5380cee6cb (id taken from the session scratchpad path). Recorder only; the direction is the Product Owner's
drainage: REQUIRED. The Product Owner directs that this be drained to PF canon (§5); state PENDING_DRAINAGE
repository_head_read: origin/main 2e03a2686af87ab0607c6cfb9afb4ad79bcdb171
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md (SHA-256 42459e54e4a14eb89a1cd3be80eae8458a5b1c2c50e1fca1b1ce9882b05e6f9b); searched, silent on tool-version pinning
pf10_addendum_created: none (QA-100 is not an addendum producer; this record edits no PF file)
---

# HDE-CRD-0002 — Product Owner direction: do not pin tool versions (v1.0)

## 1. Product Owner's words (verbatim)

> "Make a PO note which should be drained to canon: we should not be pinning tool versions. This app is still under development and should use the latest technology as much as possible. We should adapt. It has never been in production so "legacy" is not a valid reason to stay with old versions. Function matters, not tool versions."

Earlier in the same session, after QA check 3 (`qa-03-attestation-debian`) was published `TOOLING_BLOCKED` because no system interpreter in the venue matched the Plan's construction, the Product Owner said:

> "We need to just run a moon loop and pass T03. I am not going to be blocked on a python version as long as the product functions"

## 2. Direction, as given

| # | Direction |
| :- | :- |
| D-1 | Tool versions are not pinned. |
| D-2 | The app uses the latest technology as much as possible. |
| D-3 | The project adapts to current tools; it does not hold tools back. |
| D-4 | "Legacy" is not a valid reason to stay on old versions: the app is still under development and has never been in production. |
| D-5 | Function matters, not tool versions. |

## 3. Canon position when this was recorded

Searched on `main` at `2e03a268` (`git grep` over `docs/pfcanon/`): `Python 3.1x` and `CPython 3`, `setuptools`, pinned tool/dependency/version/interpreter, `exact version`, `latest`, `upgrade`, and `legacy` near version, tool or dependency.

- **No PF section requires or forbids pinning tool or dependency versions.** Canon is silent on the subject, so this direction does not conflict with it.
- PF29-Canon-HDE-Users-Guide §3.1 "Preferred setup from a clean checkout" states a floor: "Python 3.10 or newer and an environment that already provides setuptools>=68 and wheel". A floor is not a pin.
- PF06-Canon-Change-Process-Guide §0.4 and §0.6.2, and PF14-Canon-HDE-Mechanics-Guide §1.6.3, define the canonical **determinism pins**: the environment variables `LC_ALL=C`, `LANG=C`, `TZ=UTC`. They forbid adding "extra pins" as requirements. §0.6.2 adds: "Determinism is achieved by ordering, not interpreter knobs."
- HDE Build Notes v13.7.8 records interpreter versions only as observed facts of past runs, for example "CPython 3.12.3 with CI's install", not as requirements.

## 4. Where versions are pinned today (facts at `2e03a268`; this record changes none of them)

| Locus | Pin |
| :- | :- |
| `.github/workflows/ci.yml:85` and `.github/workflows/epic-closeout-validation.yml:65` | `python-version: '3.12'` |
| `requirements.txt` | `psycopg[binary]>=3.1,<3.3`; `Flask>=2.3,<3.0`; `gunicorn>=21,<22`; `jsonschema==4.23.0` |
| `requirements-dev.txt` | `jsonschema==4.23.0`; `pytest>=7.4,<9.0`; `pytest-cov>=4.1,<5.0`; `pytest-mock>=3.12,<4.0` |
| `README.md:184` (pre-push check prerequisites) | "Python 3.12" |
| QA Plan v1.2 (`docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v1.2.md`) §3.2 E-L and §7 rule A | "CPython 3.12"; readiness `python --version` prints 3.12.x |
| QA Plan v1.2 §3.2 E-D, and QA task collection v1.0 NZ-02 | E-D is built from a distribution interpreter: `/usr/bin/python3` in the Plan, a fixed candidate list in NZ-02 |

`pyproject.toml` sets `requires-python = ">=3.10"` and build requirement `setuptools>=68`. Both are floors, not pins.

Venue observation from this session: the Product Owner's workstation runs Ubuntu 26.04, whose system Python is 3.14.4. CPython 3.12 was available only as a uv-managed build. The E-D condition for check 3 could not be met with any system interpreter, and was met through the Moon Loop instead (QA-100 execution results, check 3).

## 5. Drainage

| Field | Value |
| :- | :- |
| Target | PF canon: a permanent rule on tool and dependency versions. No current section owns the subject. Candidate homes are PF04-Canon-HDE-Governance (engineering policy), PF29-Canon-HDE-Users-Guide §3.1 (stated prerequisites), PF07-Canon-Glow-Infrastructure §10 "Service start declarations" (the runtime interpreter) and PF19-Canon-Glow-QA-Guide (QA environment classes). The Product Owner chooses |
| Route | An HDE Build Notes addendum produced by one of the six native decision prompts (CF-C-30, CF-E-30, IA-30, QA-70, RS-20, ESC-40) for a qualifying approval, or the Product Owner's own canon transfer. QA-100 produces no addendum and edits no PF file (`AGENTS.md`, "PF canon is read-only unless the prompt explicitly directs a change") |
| Owner | Product Owner |
| State | `PENDING_DRAINAGE` |

## 6. Effect now, and what it does not change

- **For HDE-CRD-0002.** This is an in-flight Product Owner direction for the change (`AGENTS.md`, "Canon-first rule"). Canon is silent on the subject, so nothing in PF canon overrides it.
- **QA-110.** It is context for Kronos's review of check 3. That check passed through a Product Owner-directed Moon Loop whose E-D interpreter differs from the Plan's construction, while the predicates stayed unchanged. Kronos decides at QA-110 whether to accept it.
- **Not changed by this record:**
  - The approved QA Plan v1.2, which is immutable.
  - Any check status or predicate.
  - The repository pins of §4.

  Removing those pins is implementation work. It goes through the ordinary PR route, which the Product Owner assigns. Changing a QA Plan environment class is a Plan revision (QA-80, then QA-70) or a bounded Product Owner rescope.

## 7. Points to settle at drainage (recorder's reading; for the Product Owner to confirm)

1. **"Never been in production."** A Railway environment named `production` hosts a deployed service (PF07-Canon-Glow-Infrastructure §2.2). The words are read as "no production release to users": the work is pre-App (PF19-Canon-Glow-QA-Guide §3.3). They are not read as "no deployed service".
2. **Scope.** The canonical determinism pins (`LC_ALL`, `LANG`, `TZ`) are environment settings for byte stability, not tool versions. They are read as outside D-1.
3. **Byte-identity evidence.** The direction does not say how governed byte-identity evidence should treat a change of tool version. Examples are the release attestation, which records a wheel build, and the canonical JSON gates.

## Canon relied on

Searched on `main` at `2e03a268`; the sections read are cited where used:
- PF29-Canon-HDE-Users-Guide v1.0.2 §3.1 (read in full);
- PF06-Canon-Change-Process-Guide v2.5.4 §0.4 (its determinism-pins line) and §0.6.2 (its non-canonical-pins and determinism-by-ordering paragraphs);
- PF14-Canon-HDE-Mechanics-Guide v3.5.8 §1.6.3 (its canonical-pins line);
- PF07-Canon-Glow-Infrastructure v2.3.3 (searched for interpreter and dependency terms; §2.2 "Environment facts" and §10 "Service start declarations");
- HDE Build Notes v13.7.8 (searched; silent on the subject).

Repository rules: `AGENTS.md` "Canon-first rule" and "PF canon is read-only unless the prompt explicitly directs a change".

## Provenance

Recorded during GCFPE-USE-HDE-CRD-0002-QA-100-20261024-01 (QA-100 — Execute Bounded QA Task — 100926.1, https://app.notion.com/p/3f44590a05eb8182a201f0e177dad431; release GCFPE-20261009.1). The QA-100 execution results record cites this direction.
