"""Freeze digest of a skill tree, rooted where the claim is.

Recipe, stated so it can be reproduced rather than trusted: walk regular files only, take each
path relative to the tree root with forward slashes, sort those paths by their UTF-8 bytes, and
sha256 the concatenation of "<path>\\n<sha256-of-contents>\\n" for each. The count is the number
of files hashed.
"""
import hashlib
import sys
from pathlib import Path

root = Path(sys.argv[1]).resolve()
paths = sorted((p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()),
               key=lambda s: s.encode('utf-8'))
h = hashlib.sha256()
for rel in paths:
    h.update(rel.encode('utf-8') + b'\n')
    h.update(hashlib.sha256((root / rel).read_bytes()).hexdigest().encode('ascii') + b'\n')
print(f'{len(paths)} {h.hexdigest()}')
