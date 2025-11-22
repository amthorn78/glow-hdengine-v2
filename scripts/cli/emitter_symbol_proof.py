"""Document canonical emitter call sites for Reader/CLI."""
from __future__ import annotations

import subprocess
from pathlib import Path

EMITTER_SYMBOL = "emit_public"
TARGETS = [
    "engine/cli/main.py",
    "engine/runtime/public.py",
    "presenter/reader_v1/emitter.py",
]


def main() -> int:
    out_dir = Path("artifacts/cli/guards")
    out_dir.mkdir(parents=True, exist_ok=True)
    proof = []
    proof.append("Canonical emitter symbol: engine.presenter.emitter.emit_public\n")
    for target in TARGETS:
        result = subprocess.run(["rg", EMITTER_SYMBOL, target], capture_output=True, text=True, check=False)
        proof.append(f"== {target} ==\n")
        proof.append(result.stdout or "<no matches>\n")
    proof_path = out_dir / "emitter_symbol_proof.txt"
    proof_path.write_text("".join(proof), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
