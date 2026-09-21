---
artifact_type: PROMPT_ECOSYSTEM_CONTROLLED_CONVENTION
artifact_version: "1.0"
created_date: 2026-09-21
status: BINDING
authority: Product Owner direction 2026-09-21; derived from findings F2 (round 23), the wrong-package install, and the round-27 §10 review
supersedes_location: docs/ephemeral/gcfpe.round23/freeze.py — the script previously lived there, which was the wrong home
---

# Skill identity, freeze digests, and install verification

How a skill tree is named, how a release is frozen, and what each identity does and does not prove.
Cited by every repair round; it names no release and outlives all of them, so it lives here rather
than in `docs/ephemeral/`.

## The digest recipe

`freeze.py` in this directory. Walk regular files, skip the `EXCLUDE` set, sort paths by their UTF-8
bytes, and sha256 the concatenation of `"<path>\n<sha256-of-contents>\n"` for each.

```
python3 docs/prompt_ecosystem_management/freeze.py <directory>
```

**Root it at the skill directory, never at the synced tree.** This is not a preference:

| rooting | what it measures |
|---|---|
| a skill directory | that skill's content — the identity a repair round is about |
| the whole synced tree | every installed skill, including ones this project does not own |

Round 26 watched a whole-tree digest move from `2fa5b848…` to `c607cedc…` with nothing of this
project's touched: the sync layer had updated an unrelated Anthropic skill. **A whole-tree digest is
hostage to strangers.** Quote per-skill digests.

`manifest.json` is excluded because it is the sync layer's own bookkeeping and carries a
`lastUpdated` epoch the installer rewrites. Round 23 hashed it and published digests that did not
reproduce in another container or, once a sync touched the file, in the same one. **A freeze digest
covers skill content and never the machinery that delivers it.**

## What each identity proves

| identity | answers | does **not** answer |
|---|---|---|
| freeze digest of a skill directory | what are these bytes? | whether they are the bytes anyone approved |
| `SKILL_TREE_SHA256`, declared in `SKILL.md` and checked at runtime | have these bytes changed since packaging? | **whether this is the version that was approved** |
| the digest named in a §10 verdict | which bytes were authorised | nothing about what is installed |

**A coherently built wrong package self-certifies.** Measured on 2026-09-21: a superseded package,
checked against its own declaration, returns no error — because a correct build declares itself
correctly. `SKILL_TREE_SHA256` is a tamper and integrity check. It is not a version check, and it
would not have caught the wrong-package install that motivated building it.

## Install verification — the rule this exists to serve

**An install is complete when the installed tree measures the digest the §10 verdict named. Not when
the gates come back green.** Every gate — the hash-pin chain, the fixture suites, the self-identity
check, the independent review — passes happily against a superseded version.

The comparison is one command and it is the only control for the wrong-package case:

```
python3 docs/prompt_ecosystem_management/freeze.py <installed>/<skill>   # equals the verdict's digest?
```

Check every skill the change touched, **and every skill it deliberately did not** — an unchanged
skill proving unchanged is evidence; assuming it is not. A mismatch is reported, never reconciled:
name which package is installed, name which was expected, hand the difference back.

On 2026-09-21 a withdrawn package was installed in place of its successor, under the identical
filename the packager requires, and ran for a full round behind green gates. **Two `.skill` files
for the same skill are always indistinguishable by name**, so the digest comparison is the control,
and delivery hygiene — digest first in the caption, one package per message — only reduces the odds.

## Recording the values

A round's report names the baseline digest, the repaired digest, the package digest and
`SKILL_TREE_SHA256`. A freeze record names every installed skill, the contract, the graph proof
token and the repository controls. Both are release-scoped and belong in `docs/ephemeral/`; **this
convention is not.**
