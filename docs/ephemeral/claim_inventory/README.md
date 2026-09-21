---
artifact_type: TOOL_NOTE
artifact_version: "1.0"
created_date: 2026-09-21
authority: Product Owner authorization, 2026-09-21
subject: Deterministic claim inventory for changed documentation
---

# Claim inventory

A pre-push check that every claim-bearing line a change introduces is **owned by something**.

```sh
python3 docs/ephemeral/claim_inventory/claim_inventory.py --range origin/main..HEAD
python3 docs/ephemeral/claim_inventory/claim_inventory.py            # uncommitted work
```

## What it checks, and what it does not

It finds each line a change adds or modifies that states a digest, a count, a size, a dotted
revision or a percentage, and requires it to be either inside a `<!-- generated: … -->` block, or
listed in `allow.json` with a note naming what recomputes it or why it is fixed.

**It does not verify that any value is correct**, and it cannot — it has no idea what the number
means. It converts *a reader must notice a stale figure* into *an author must say, in writing, who
owns this figure*. Limits, stated because an unstated limit is how the guards in this package kept
over-claiming: Markdown only, so a figure in a docstring is out of scope; only the paths given by
`--paths`; and "generated" means marker-delimited and nothing else.

## Why it exists

Three consecutive review cycles on #425 produced three stale claims while the evidence itself
stayed correct — a validator-difference summary falsified by a later retirement, a
`regenerated at <commit>` attribution four commits out of date, and a corpus byte total that was
never summed. Each was a sentence describing a derivable value, sitting beside blocks that were
derived. Re-reading every summary after every change was tried, and failed four times in one round.

## The allow-list is keyed on the exact line text

That is the design, not an implementation detail: edit the line and its entry stops matching, so
the claim comes back for accounting. Entries are checked in **both** directions — an entry whose
line no longer exists is reported too, because a dead entry is how an allow-list grows quietly into
a blanket exemption.

## Controls, all fired

| injected | result |
|---|---|
| the three claims that actually went stale, at the commits that introduced them | all three reported |
| a new prose claim added to a brief | reported |
| an allow-listed line edited | reported **twice** — as an unaccounted claim and as a stale entry |
| a dead allow-list entry | reported |

## Two defects of its own, found by running it

Both were the same shape as the findings it exists to catch, which is worth recording rather than
hiding. It first took line numbers from `git diff` of an old range and then read the file from
**disk**, so every number indexed into content the commit never had. And a bare revision is not a
range — `git diff <rev>` compares the **working tree** against it — so reading that revision
reproduced the same mismatch from the other direction. Both were caught by the tool reporting lines
that were plainly inside a marker block, not by re-reading the code.

It also originally recognised generated regions by **shape**, carrying its own copy of the
recorder's table and fence patterns. Two copies of one rule is how the guard drift in this package
began, so the regions are now marker-delimited in the document and both tools read that one
declaration.
