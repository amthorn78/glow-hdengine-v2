---
artifact_type: PROMPT_ECOSYSTEM_MANAGEMENT_ROOT
artifact_version: "1.1"
created_date: 2026-09-17
status: BINDING
authority: Product Owner decision, 2026-09-17
---

# docs/prompt_ecosystem_management

Persistent infrastructure for managing prompt ecosystems. This directory is not
release-specific and is not a runtime artifact store. It exists because the
prompt-management ecosystem is intended to become reusable infrastructure — for
this ecosystem first, and for others later — and reusable infrastructure needs a
stable home rather than being scattered among release-specific artifacts.

## The architecture

| Layer | Home | Why |
|---|---|---|
| Durable prompt behaviour | Notion, authored in place | The prompt is the behaviour. It is edited where it lives. **Only prompts intended as durable, reusable Notion-managed assets** — see `notion-write-boundary.md`. |
| Machine-readable prompt contracts and ecosystem-management infrastructure | **here** | Versioned, diffable, reviewable through pull request |
| Ephemeral run artifacts, reports, ledgers | `docs/ephemeral/` | Working store, pruned manually |
| Maintained machine-readable graph source | `docs/graph/` | Per-prompt parts, rebuilt by script |
| PFCanon | `docs/pfcanon/` | Read-only |
| Operational index, navigation, status | Notion | Discovery and human management |

**Repository is the persistent versioned authority. Notion is the operational
layer.** They do not duplicate each other byte for byte. Where a document here has
no useful Notion representation and that makes it hard to find, it is indexed from
the appropriate Notion management surface rather than copied into it.

Google Drive is not an authority for this material. Removing Drive from the
architecture does not create a documentation gap: anything that previously needed a
persistent operational document still needs one, and its home is now here.

## What belongs here

Schemas, registries, validation contracts, controlled conventions, architecture
records and decision records that outlive any single release.

## What does not

Release-scoped run evidence, batch reports, ledgers and checkpoints. Those are
`docs/ephemeral/`. A document that names a release in its identity and dies with it
is ephemeral, not infrastructure.

That test is mechanical. Apply it before choosing a path, not after — a session working
in `docs/ephemeral/gcfpe.roundNN/` writes everything into that folder because that is
where its hands already are, and **round-scoped is where the work happened, not what the
artifact is.**

| this | goes here |
|---|---|
| a procedure, convention, schema, registry, tool or decision record | `docs/prompt_ecosystem_management/` |
| a round report, freeze snapshot, §10 verdict, ledger, filled prompt instance, dated finding | `docs/ephemeral/` |
| maintained machine-readable graph source | `docs/graph/` |
| PFCanon | `docs/pfcanon/`, read-only |
| durable, reusable prompt behaviour | Notion, authored in place |
| a one-off, handoff, correction, recovery or development-flow prompt | **not Notion.** The handoff itself, or `docs/ephemeral/` if worth keeping — see `notion-write-boundary.md` |

**For a procedure, the repository document is normative and the Notion entry is the
operational index** that helps someone find it and know when it applies. Where the two
disagree, the repository governs and the Notion entry is a defect to be corrected.

## Validation posture

This material is **not part of the Glow application runtime**. It is excluded from
application CI — `docs/prompt_ecosystem_management/**` is in `ci.yml`'s `paths-ignore`,
alongside the other documentation paths — because nothing here affects the application
build or test surface. `epic-closeout-validation.yml` is `workflow_dispatch` only and
needs no exclusion.

**Three places have to agree, and they did not.** `paths-ignore` only skips the workflow
when *every* changed file matches it; any other file in the same diff runs the job, and
the job then reaches two checkers that keep their own path lists:
`ci/checks/classify_ci_changes.py` raised `CI_CHANGE_SURFACE_UNCLASSIFIED` on an
unrecognised documentation path and killed the run before a single test executed, and
`ci/checks/check_direct_db_contract.py` read governance documents as source. Both now
recognise the four documentation paths. **Adding a fifth documentation path means
updating all three.**

**Excluded from application CI is not exempt from validation.** Prompt-ecosystem
validation — registry structure, prompt inventory consistency, controlled values,
reference integrity, release binding, drift — is a separate concern with a separate
mechanism: the `amthor-workspace-governance-audit` skill, which exists to audit
declared project prompt contracts and versioned registries and is run on demand
rather than on push.

That separation is deliberate and is why the `paths-ignore` entry is safe here: an
agent-run validator is not affected by a workflow trigger filter, so placing a
document in this directory does not make it invisible to the validation that applies
to it. No second CI system is introduced. If ecosystem validation ever does need to
run on push, it gets its own narrowly scoped workflow rather than being folded into
the application's.

## Contents

| File | What it is |
|---|---|
| `authoritative-surfaces.md` | Where the persistent truth lives — repository paths, Notion pages, release baseline. **Start here.** |
| `gcfpe.decision-record.md` | Product Owner decisions governing the prompt ecosystem, with their consequences |
| `project-prompt-contract-registry.md` | The approved machine-readable per-prompt contract registry |
| `execution-and-delegation-model.md` | How work is divided: the coordinator's role, what may be delegated, the reporting contract, and verification isolation |
| `ecosystem-change-management.md` | **How a change to this ecosystem is made routine**: the five-step change lifecycle, the defect-class catalogue, the standing instruments, the definition of done, and what needs Product Owner authorization |
| `postflight-procedure.md` | **How an independent post-flight is run**: scope set by what stops the change flow, cheap checks before bodies, bodies streamed and never persisted, the struck checks and their rulings |
| `skill-identity-and-freeze.md` | Skill digests, what each identity proves, and why an install is not complete until its digest is compared |
| `freeze.py` | The digest recipe itself. Root it at a skill directory, never at the synced tree |
| `prompt-corpus-policy.md` | **The Prompt Corpus Storage and Fidelity Policy**, recorded verbatim — the prompt corpus is never mirrored, exported, hashed or cached to disk |
| `notion-write-boundary.md` | **Which prompts belong in Notion and when a Notion write is authorized** — the default is read-only; executing a prompt is not a reason to write |
| `prompt-validation-procedure.md` | How prompt bodies are validated without a corpus mirror — read the page, pipe the body on stdin — and the rule that a recorded identity must be compared, not printed |
| `skill-packaging-and-delivery.md` | How a skill is packaged and handed over, mandatory independent validation, and why every delivered artifact except a `.skill` file must be uniquely named |
| `reviewer-prompt-template.md` | The canonical reviewer prompt. Every skill handover fills this template rather than composing one |
| `session-working-rules.md` | How a session works rather than what it produces: source-read minimalism, tracking as part of the work, and the worker communication rules |
| `pe-succession/` | Session succession records, newest last. **`pe35-to-pe36.md` is current** — it carries the charter change from repair campaign to general maintenance |
