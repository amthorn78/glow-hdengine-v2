"""Freeze digest of a skill tree, rooted where the claim is.

Recipe, stated so it can be reproduced rather than trusted: walk regular files only, take each
path relative to the tree root with forward slashes, **skip the sync-infrastructure paths in
EXCLUDE**, sort the remainder by their UTF-8 bytes, and sha256 the concatenation of
"<path>\\n<sha256-of-contents>\\n" for each. The count printed is the number of files hashed,
which is one fewer than the tree's file count.

`manifest.json` is excluded because it is the sync layer's own bookkeeping, not skill content.
It carries a `lastUpdated` epoch that the installer rewrites on every sync, so hashing it makes
the digest a per-container, per-sync value rather than an identity. SF10-10's first version of
this recipe did hash it, which reproduced the exact defect the recipe was introduced to remove:
the round-23 report published 318-file digests that do not reproduce in another container, and
did not reproduce in this one once a sync touched the manifest. Found by SFR-01 in §10 review
and confirmed by falsification here. The rule generalises: a freeze digest covers skill content
and never the machinery that delivers it.
"""
import hashlib
import sys
from pathlib import Path

# Sync-layer bookkeeping, rooted at the skill tree. Never skill content.
EXCLUDE = {"manifest.json"}

root = Path(sys.argv[1]).resolve()
paths = sorted(
    (
        rel
        for rel in (p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file())
        if rel not in EXCLUDE
    ),
    key=lambda s: s.encode("utf-8"),
)
h = hashlib.sha256()
for rel in paths:
    h.update(rel.encode("utf-8") + b"\n")
    h.update(hashlib.sha256((root / rel).read_bytes()).hexdigest().encode("ascii") + b"\n")
print(f"{len(paths)} {h.hexdigest()}")
