"""Helpers for canonical ordering and explicitly declared arrays-as-sets."""
from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from typing import Any

from engine.serializer.canon import sercanon


class SetIdentityConflict(ValueError):
    """Two non-identical members declared the same set identity."""


def _first_divergence(left: Any, right: Any, path: str = "$") -> str:
    if isinstance(left, Mapping) and isinstance(right, Mapping):
        for key in sorted(set(left) | set(right)):
            child = f"{path}.{key}"
            if key not in left or key not in right:
                return child
            if sercanon(left[key], sort_keys=True) != sercanon(right[key], sort_keys=True):
                return _first_divergence(left[key], right[key], child)
    elif isinstance(left, list) and isinstance(right, list):
        for index, (a, b) in enumerate(zip(left, right)):
            if sercanon(a, sort_keys=True) != sercanon(b, sort_keys=True):
                return _first_divergence(a, b, f"{path}[{index}]")
        if len(left) != len(right):
            return f"{path}[{min(len(left), len(right))}]"
    return path


def canonicalize_declared_set(
    seq: Sequence[Any], *, identity: str | Callable[[Any], Any] | None
) -> list[Any]:
    """Deduplicate and ASCII-sort a schema/PF-declared set without changing values."""
    if identity is None:
        if any(isinstance(item, Mapping) for item in seq):
            raise ValueError("set_object_identity_required")
        identity_fn = lambda item: item
    elif isinstance(identity, str):
        def identity_fn(item: Any) -> Any:
            if not isinstance(item, Mapping) or identity not in item:
                raise ValueError(f"set_identity_field_missing:{identity}")
            return item[identity]
    else:
        identity_fn = identity

    retained: dict[bytes, tuple[bytes, Any]] = {}
    for item in seq:
        raw_identity = identity_fn(item)
        if not isinstance(raw_identity, (str, int, float, bool)) or raw_identity is None:
            raise ValueError("set_identity_must_be_scalar")
        # Canonical scalar bytes preserve JSON type as well as value.  Stringifying
        # would collapse distinct identities such as 1 and "1".
        key = sercanon(raw_identity, sort_keys=True)
        element_bytes = sercanon(item, sort_keys=True)
        prior = retained.get(key)
        if prior is None:
            retained[key] = (element_bytes, item)
        elif prior[0] != element_bytes:
            field = _first_divergence(prior[1], item)
            identity_text = key.decode("utf-8").rstrip("\n")
            raise SetIdentityConflict(
                f"set_identity_conflict:{identity_text}:first_divergent_field:{field}"
            )
    return [retained[key][1] for key in sorted(retained)]


def dedupe_sort(seq: list[str]) -> list[str]:
    return canonicalize_declared_set(seq, identity=None)


def canonicalize_array(seq: list[str]) -> list[str]:
    """Compatibility surface for existing schema-declared scalar string sets."""
    return dedupe_sort(seq)


def sort_pairs(a: tuple[str, str], b: tuple[str, str]) -> int:
    return (a > b) - (a < b)


def ensure_total_order(items: list[str], cmp: Callable[[str, str], int]) -> list[str]:
    return sorted(items, key=lambda x: x)
