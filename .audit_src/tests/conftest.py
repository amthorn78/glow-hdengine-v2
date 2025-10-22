import sys, pathlib
# Ensure the repository root is importable during pytest collection
ROOT = pathlib.Path(__file__).resolve().parents[1]
p = str(ROOT)
if p not in sys.path:
    sys.path.insert(0, p)
