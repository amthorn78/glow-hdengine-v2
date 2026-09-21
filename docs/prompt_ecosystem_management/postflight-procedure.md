---
artifact_type: PROMPT_ECOSYSTEM_CONTROLLED_CONVENTION
artifact_version: "1.0"
created_date: 2026-09-21
status: BINDING
authority: Product Owner direction 2026-09-21, amending §11 of the six-batch repair plan
replaces: the post-flight method used through 2026-09-15, which is prohibited rather than deprecated
---

# Independent post-flight — the standing procedure

How an independent post-flight of a prompt-ecosystem release is run. Release-scoped instances —
the filled prompt, the resulting report — belong in `docs/ephemeral/`. **This procedure does not.**

## What post-flight is for

**Someone who did not author the work looks at it and can say no.** That is the entire value, and it
is the only control in this project that has repeatedly caught real defects — the round-26 review
returned four blocking findings after the author had declared the round sound.

It is not an evidence-production exercise. The 2026-09-15 run emitted roughly **17.7 MB** of
manifests to report **one error**.

## Scope is set by the goal

The prompts exist to run the Glow change flow. **Audit for what stops the flow:**

- a handoff naming a receiver that does not exist, or naming it wrongly
- an artifact required at a stage before anything produces it
- a terminal branch that emits a continuation, or a nonterminal branch that emits none
- two prompts disagreeing about who decides something
- a route the graph declares that the body does not carry, or the reverse

**Do not audit** wording quality, prose drift, byte-level fidelity, presentation differences, or
whether an input is labelled optional. None stop the flow, and one of them consumed three weeks.

## Method

1. **Reproduce the frozen identities first.** An auditor who cannot name the tree does not audit it.
   See `skill-identity-and-freeze.md`.
2. **Do everything that needs no prompt body, first** — graph rebuild against its proof token, the
   terminal-branch invariant (`D15`), registry-versus-graph drift, the PF10 producer set, `PR-20`'s
   declared inputs, the installed gates. **Most real defects have lived here, not in the prose.**
3. **Then stream the bodies, lane by lane**, so no single context holds the corpus. Read one page,
   pipe it to the shipped validator with `--bodies-stdin`, run that row's `audit_assertions`,
   discard it.
4. **Read the coverage fields, never `ok` alone.** A run that validated nothing returns `ok: true`
   and is not a pass.
5. **Carry forward findings only** — prompt id, verdict, the exact quoted clause, the page
   timestamp. Never the body.

## The corpus constraint binds the method

The **Prompt Corpus Storage and Fidelity Policy** governs how a post-flight is conducted, not only
what it concludes. The auditor may not write prompt bodies to disk, hash them, compare them
byte-for-byte, produce an evidence bundle containing body content or body digests, or require a
complete local corpus.

**If a procedure the auditor is told to follow conflicts with this, that procedure is defective:
report it and stop. Do not work around it.**

The 2026-09-15 run's own words — *"all 67 live Notion candidate bodies match … their complete local
counterparts under documented presentation normalization"* — describe the prohibited artifact, and
that normalization produced three weeks of byte-fidelity disputes about copies of pages that were
never in question. The instrument's own evidence contract still mandates it, which is why an auditor
must be empowered to refuse.

## The timestamp baseline

Every Notion fetch returns `page_last_edited_at`. **It is page metadata, not content; recording it
is permitted and is not a body hash.**

A post-flight returns every prompt's value as a table. **After that, an audit sweeps timestamps and
re-reads only the pages that moved.** The full pass is paid once. Until the registry carries edit
state per row, each full pass re-establishes it.

## Checks struck from the original §11, with their rulings

| check | why it is gone |
|---|---|
| manual-drain handshake | the PF10 drainage lifecycle was retired by `D6`. A check that can only pass is not a check |
| Drive artifact routing | Drive was retired as a storage authority by `D7` |
| required/optional input classification | nothing in the ecosystem records which inputs are optional; dispositioned unfalsifiable 2026-09-21 |
| byte-for-byte body identity against a stored copy | prohibited, and the source of the defect class above |

## Independence and authority

Fresh session. **Not the author, not the §10 skill reviewer.** Read-only: repairs nothing, installs
nothing, merges nothing, promotes nothing; each finding returns to its owner.

Verdict vocabulary is fixed — **`PASS`**, **`PASS WITH WARNINGS`**, **`FAIL`**, **`INDETERMINATE`**.
`PASS` or `PASS WITH WARNINGS` with no mandatory open finding permits a promotion decision packet.
`FAIL` or `INDETERMINATE` returns findings to the owning gate and authorises no promotion, archival,
PF10 drainage or Alpha resumption.

Each finding states the prompt or control, the exact defect, the evidence as a quoted clause, the
smallest correction, and **whether it stops the flow or merely offends the record.**
