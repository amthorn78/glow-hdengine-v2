#!/usr/bin/env python3
"""Deterministic guard that rejects ad-hoc JSON serialization on CLI surfaces."""
from __future__ import annotations

import argparse
import ast
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import DeterminismEnvError, ensure_determinism_env

DEFAULT_SCOPE = (Path("engine/cli"), Path("adapter/http_reader.py"))
DISALLOWED_ATTRS = {"dumps", "dump"}


@dataclass(frozen=True)
class Violation:
    path: Path
    line: int
    kind: str

    def render(self, root: Path) -> str:
        try:
            rel = self.path.relative_to(root)
        except ValueError:
            rel = self.path
        return f"{rel}:{self.line}: {self.kind}"


class JsonCallVisitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.json_aliases: set[str] = set()
        self.dumps_aliases: set[str] = set()
        self.calls: list[int] = []

    def visit_Import(self, node: ast.Import) -> None:  # pragma: no cover - trivial
        for alias in node.names:
            if alias.name == "json":
                self.json_aliases.add(alias.asname or alias.name)
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:  # pragma: no cover - trivial
        if node.module == "json":
            for alias in node.names:
                if alias.name in DISALLOWED_ATTRS:
                    self.dumps_aliases.add(alias.asname or alias.name)
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call) -> None:
        if isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name):
            if node.func.value.id in self.json_aliases and node.func.attr in DISALLOWED_ATTRS:
                self.calls.append(node.lineno)
        if isinstance(node.func, ast.Name) and node.func.id in self.dumps_aliases:
            self.calls.append(node.lineno)
        self.generic_visit(node)


def _iter_python_files(paths: Sequence[Path]) -> Iterable[Path]:
    for base in paths:
        if base.is_file() and base.suffix == ".py":
            yield base
        elif base.is_dir():
            yield from (p for p in base.rglob("*.py") if p.is_file())


def _scan_file(path: Path) -> list[Violation]:
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(path))
    visitor = JsonCallVisitor()
    visitor.visit(tree)
    return [Violation(path=path, line=line, kind="json.dumps call") for line in visitor.calls]


def _render_log(root: Path, scope: Sequence[Path], violations: Sequence[Violation]) -> str:
    scope_entries = []
    for path in scope:
        base = path if path.is_absolute() else root / path
        try:
            rel = base.relative_to(root)
            scope_entries.append(str(rel))
        except ValueError:
            scope_entries.append(str(base.resolve()))
    lines = ["CLI Serializer Grep Guard", "scope:" + ",".join(sorted(scope_entries))]
    if violations:
        lines.append(f"summary: FAIL ({len(violations)} violation(s))")
        for violation in sorted(violations, key=lambda v: (v.path.as_posix(), v.line)):
            lines.append(violation.render(root))
    else:
        lines.append("summary: PASS (no disallowed json serialization in governed CLI scope)")
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="CLI serializer grep guard")
    parser.add_argument(
        "--paths",
        dest="paths",
        action="append",
        type=Path,
        default=[],
        help="Paths to scan (default: engine/cli)",
    )
    parser.add_argument(
        "--output",
        dest="output",
        type=Path,
        default=Path("artifacts/cli/guards/serializer_grep_guard.log"),
        help="Path for the guard log",
    )
    args = parser.parse_args(argv)

    try:
        ensure_determinism_env()
    except DeterminismEnvError as exc:  # pragma: no cover - CLI exit path
        raise SystemExit(str(exc)) from exc

    scope = [*(Path(p) if not isinstance(p, Path) else p for p in DEFAULT_SCOPE), *(args.paths or [])]
    violations: list[Violation] = []
    for file_path in _iter_python_files(scope):
        violations.extend(_scan_file(file_path))

    body = _render_log(Path.cwd(), scope, violations)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(body, encoding="utf-8")
    return 1 if violations else 0


if __name__ == "__main__":  # pragma: no cover - script entrypoint
    raise SystemExit(main())
