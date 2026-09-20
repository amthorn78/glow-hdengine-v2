---
artifact_type: GCFPE_REPAIR_REPORT
artifact_version: "1.0"
created_date: 2026-09-20
round: 19
release: GCFPE-20260914.1 / 091426.1 / 55
status: CLEARED_AND_INSTALLED
authority: Product Owner installation, 2026-09-20
guard_version: v11
supersedes_guard_version: v6
independent_review_verdict: GUARD_HOLDS
independent_reviewer: SFR-01
verification_executor: PE34 (prompt-engineer session)
verification_date: 2026-09-20
---

# Round 19 — v11 cleared by independent review, and installed

**`GUARD_HOLDS`.** SFR-01 returned the first verdict in this series with no defeat. The Product
Owner then installed v11. This record supersedes round 18's status line, which was
`PACKAGED_AWAITING_INDEPENDENT_REVIEW` and true when written; round 18 is left unedited under
`AUTH-001`, and this is its successor.

The guard has been written eleven times and defeated ten. **v11 is the first version to
survive an independent attack round.**

## Installation verified against the installed bytes, not the packages

**Who ran these checks.** Every identity, digest, gate run and bench run below was executed by
**PE34**, the prompt-engineer session, on 2026-09-20, after the Product Owner's installation and
after SFR-01's review closed. The Product Owner performed the installation; SFR-01 performed the
independent attack round on the packages; neither performed the post-installation verification
recorded here. PE34 did not install and cannot install.

| Check | Result |
|---|---|
| `change-flow/scripts/validate_gcfpe_20260914.py` | `660d61fe619c9dd9aa2b5646a7344084af3c8c333fc044e2e91f51e941363c63` — v11 |
| `flowmaster-validate/scripts/validate_gcfpe_20260914.py` | `535a3b161ef0996249540b46607b855c8d17d841fdd24ce3b615f97e6199bc2e` — v11 |
| `flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py` | `433d2a1611e5671aca628ff2cd3d2ea312b9efab064e5a5c67c95c8417d96f4b` — v11 |
| Previous installed build | v6: `2fdb690a…` / `bdaa21e9…` / `e3607d1b…` — no longer present |
| Synced tree | 321 files, `.pyc` 0 |
| Tree digest, `manifest.json` excluded | `c321be051b90c346a24d26524e132e7b90732953c3cc289e3def511e5fcfbaeb` (was `7a15a246…` under v6) |
| `change-flow/` subtree, 21 files | `5c58d494422e5e0fb3cfb54df26274a83c7b5bc8762ce29a16dcfbfd77ed0ef0` |
| `flowmaster-validate/` subtree, 29 files | `1f2bf7e671325ade34d2cd9b1f9448c964cbb9c7b5ed6c71874ca4ca70aadb3d` |
| Cross-copy parity of the guard block | identical, 8836 chars, `e80529aac5653adfce29fe4c40227fce` |

## The installed build was exercised, not just hashed

Run from a scratch copy of the installed tree, with `PYTHONDONTWRITEBYTECODE=1`; nothing was
executed inside the synced tree and the tree digest was re-measured unchanged afterwards.

```
G1 rc=0 PASS: change-flow GCFPE-20260914.1 contract and Markdown-only source policy
G2 rc=0 ok=True errors=[]
G3 rc=0 fixture_suite_ok=True cases=140 failing=[]
G4 rc=0 FLOWMASTER_SUITE_PASS
```

The round-18 bench, run against the **installed** build rather than the packages:
`placements run: 14  unexpected: none`.

## Digest method — a correction SFR-01 is owed

`sha256sum` hashes the path text as well as the bytes, so a per-skill subtree digest depends
on the working directory it was produced from. SFR-01 reproduced different values from inside
each skill directory and the recorded values from the tree root. **The values in round 18 and
in this record are correct and reproduce exactly, but only from the tree root with a `./`-
prefixed path**, which is now stated rather than assumed:

```
cd <synced-tree-root>
find ./change-flow -type f | LC_ALL=C sort | xargs sha256sum | sha256sum
find . -type f ! -name manifest.json | LC_ALL=C sort | xargs sha256sum | sha256sum
```

This is a method defect in the earlier record, not a numeric one. No digest changes.

## What SFR-01 verified rather than accepted

- The fixture runner diff is **one hunk** — the amended expectation plus two comment lines,
  checked by `diff` rather than by reading the description.
- All **six** checks wired in both copies, by line number: change-flow 904/908/912/916/920/924,
  flowmaster-validate 1489/1491/1493/1495/1498/1501. Nothing defined-but-unwired.
- Typed segments are injective: `["forbidden_fields","0"]` and `["forbidden_fields",0]` do not
  alias, both injected. `_UNPINNABLE` is a sentinel **object**, not a string — SFR-01 notes a
  string there would have been a clean way back in.
- All thirteen placements caught, fail-open sweep clean, every round-18 measurement reproduced.

## SFR-01 withdraws its own H remedy

SFR-01 recorded that its recommended token-shape rule on `forbidden_fields` elements was wrong
and the refutation correct: it asserted the rule "costs nothing" without running it against the
lawful contract, in which two elements are prose. It names this as the same error it had been
identifying in v1, v2 and v9 — a form pin that rejects lawful content — made while pointing at
it. The exact element pin stands as the right answer.

## A sharpened argument for the element pin, from SFR-01

On the objection that an enumeration invites quiet editing: editability was never the variable;
what matters is **what the re-stamp costs**. A hex string tells a reviewer nothing.
`EXPECTED_ADDENDUM_LIST_VALUES` re-stamps as the literal prose being admitted, so landing the H
injection requires an author to paste the prohibited gate sentence into guard source, in
English, where a reviewer reads it. That is a **stronger** property than the 45 paths, not an
equal one.

## Two latent asymmetries — neither a defeat, neither fixed

Recorded so they are not rediscovered as findings, and deliberately **not** repaired: SFR-01
declined to recommend a fix it had not measured, and this round does not add one.

1. `_branch_text` serialises values only, so `PF10` appearing in a **field name** is invisible
   to the in-surface overlay check, while layer 2's `json.dumps` sees keys. The two checks
   disagree about what a branch's text is. Injected on a real boundary edge: overlay returns
   `[]`, but the layer-1 routing pin moves, so the placement is caught by a designed layer.
2. `contract.get("route_graph", {})` makes the retired-token scan vacuous if the key is
   absent — caught by layer 4 as `removed:route_graph`.

## The three handbacks, answered

- **The routing-surface encoding.** Confirmed non-collidable, with a stronger reason than
  "impractical": `json.dumps` escapes control characters, so a serialised row can never contain
  a literal `\x1f`; a collision would require one. Separator injection through `"\n".join` is
  closed by the row-count pin. SFR-01 tried `\x1f` and `\n` in state names: both moved the
  digest with the count unchanged.
- **Layer 2's derived path.** Confirmed label-only. The allow-list is gone and `path` appears in
  exactly one statement; no `path ==`, `path in` or `path.split` anywhere. Emptiness is the
  tested property.
- **The lossy-derivation sweep.** Spent on the 33 `subset_errors` sites and the graph parity
  checks. **No lossy derivation outside the two already known.** `subset_errors` compares raw
  values; its limitation is that it is a subset test, which is E3, a different failure mode.

## Where the remaining machine-checkable risk now sits

**E3 is the whole remaining surface on the placement axis — the axis machinery covers.** It is
not all remaining risk: the vocabulary axis below is open and is covered by human review, not by
this guard. Every defeat since v7 was inside the one object the guard closes exactly. SFR-01 expects the next finding in the other thirty-three `subset_errors` sites,
and states there is no cheap sweep for them: closing them needs a decision about which are
closed governance objects, not a mechanical pass.

The vocabulary axis (D8 residuals E1, E2 and residual 1) is unchanged and remains enforced by
human review.

## What this round does not claim

- It does not close the §10 skill-fit gate. §10 requires the dedicated review to be re-run
  against the final installed snapshot; that snapshot now exists and the review has not yet
  been run.
- It makes no claim about QA, acceptance, PF09 movement, deployment or epic closure.
