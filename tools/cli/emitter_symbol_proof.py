#!/usr/bin/env python3
"""Produce deterministic proof that governed CLI emits via the canonical emitter."""
from __future__ import annotations

import argparse
import ast
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import DeterminismEnvError, ensure_determinism_env

DEFAULT_CLI_PATH = Path("engine/cli/main.py")
CANONICAL_EMITTERS = {"emitter.emit_public", "emit_reader_public_envelope"}
GOVERNED_HANDLERS = {
    "showcompat": "showcompat",
    "aux-preview": "aux_preview",
    "bg:resolve": "bg_resolve",
}
HANDLER_EMITTER_ALLOWLIST = {
    "showcompat": frozenset({"emitter.emit_public", "emit_reader_public_envelope"}),
    "aux-preview": frozenset(),
    "bg:resolve": frozenset({"emitter.emit_public"}),
}
OPTIONAL_EMITTER_HANDLERS = {"aux-preview"}


@dataclass(frozen=True)
class HandlerProof:
    handler: str
    function: str
    emitters: tuple[str, ...]
    optional: bool

    def render(self) -> str:
        suffix = " (exempt)" if (not self.emitters and self.optional) else ""
        emitter_list = ",".join(self.emitters) if self.emitters else "<none>"
        return f"{self.handler}:{self.function}:{emitter_list}{suffix}"


class _EmitterVisitor(ast.NodeVisitor):
    def __init__(self, targets: set[str]) -> None:
        self.current: str | None = None
        self.calls: dict[str, set[str]] = {name: set() for name in targets}

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        previous = self.current
        self.current = node.name
        self.generic_visit(node)
        self.current = previous

    def visit_Call(self, node: ast.Call) -> None:
        if self.current in self.calls:
            emitter_name = _canonical_name(node.func)
            if emitter_name in CANONICAL_EMITTERS:
                self.calls[self.current].add(emitter_name)
        self.generic_visit(node)


def _canonical_name(func: ast.AST) -> str | None:
    if isinstance(func, ast.Attribute) and isinstance(func.value, ast.Name):
        return f"{func.value.id}.{func.attr}"
    if isinstance(func, ast.Name):
        return func.id
    return None


def _parse_cli(path: Path, targets: Mapping[str, str]) -> Iterable[HandlerProof]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    visitor = _EmitterVisitor(set(targets.values()))
    visitor.visit(tree)
    for handler, func_name in sorted(targets.items()):
        emitters = tuple(sorted(visitor.calls.get(func_name, ())))
        yield HandlerProof(
            handler=handler,
            function=func_name,
            emitters=emitters,
            optional=handler in OPTIONAL_EMITTER_HANDLERS,
        )


def _render_proof(proofs: Sequence[HandlerProof]) -> str:
    lines = ["CLI Emitter Symbol Proof", "canonical_emitters:" + ",".join(sorted(CANONICAL_EMITTERS))]
    allowlist_line = ",".join(
        f"{handler}={'|'.join(sorted(HANDLER_EMITTER_ALLOWLIST[handler])) or '<none>'}"
        for handler in sorted(HANDLER_EMITTER_ALLOWLIST)
    )
    lines.append("handler_emitter_allowlist:" + allowlist_line)
    failures = []
    for proof in proofs:
        expected = HANDLER_EMITTER_ALLOWLIST.get(proof.handler, frozenset())
        actual = set(proof.emitters)
        if proof.optional:
            if not actual.issubset(expected):
                failures.append(proof)
            continue
        if actual != expected:
            failures.append(proof)
    lines.append(f"summary:{'FAIL' if failures else 'PASS'}")
    for proof in proofs:
        lines.append(proof.render())
    lines.append("")
    return "\n".join(lines)


def _failures(proofs: Sequence[HandlerProof]) -> list[HandlerProof]:
    failures: list[HandlerProof] = []
    for proof in proofs:
        expected = HANDLER_EMITTER_ALLOWLIST.get(proof.handler, frozenset())
        actual = set(proof.emitters)
        if proof.optional:
            if not actual.issubset(expected):
                failures.append(proof)
            continue
        if actual != expected:
            failures.append(proof)
    return failures


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="CLI emitter proof generator")
    parser.add_argument(
        "--cli-path",
        dest="cli_path",
        type=Path,
        default=DEFAULT_CLI_PATH,
        help="CLI module to analyze (default: engine/cli/main.py)",
    )
    parser.add_argument(
        "--output",
        dest="output",
        type=Path,
        default=Path("artifacts/cli/guards/emitter_symbol_proof.txt"),
        help="Path for the proof artifact",
    )
    args = parser.parse_args(argv)

    try:
        ensure_determinism_env()
    except DeterminismEnvError as exc:  # pragma: no cover - CLI exit path
        raise SystemExit(str(exc)) from exc

    proofs = list(_parse_cli(args.cli_path, GOVERNED_HANDLERS))
    proof_body = _render_proof(proofs)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(proof_body, encoding="utf-8")
    failures = _failures(proofs)
    return 1 if failures else 0


if __name__ == "__main__":  # pragma: no cover - script entrypoint
    raise SystemExit(main())
