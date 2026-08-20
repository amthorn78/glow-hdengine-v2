from __future__ import annotations

import runpy
from pathlib import Path

import pytest

from ci.checks import classify_ci_changes as classifier
from tools.evidence import refresh_epic024_step_logs_manifest as refresh_impl
from tools.evidence import refresh_step_logs_manifest as refresh_wrapper
from tools.evidence import strict_json_schema


ROOT = Path(__file__).resolve().parents[2]


def test_evidence_helper_owner_registry_is_exhaustive_and_exact() -> None:
    tracked = {
        path.relative_to(ROOT).as_posix()
        for path in (ROOT / "tools/evidence").rglob("*")
        if path.is_file()
        and not path.is_symlink()
        and path.suffix.lower() == ".py"
        and not path.name.lower().startswith("generate_")
    }
    mapped = set(classifier._EVIDENCE_HELPER_TEST_OWNERS)
    blocked = classifier._EVIDENCE_HELPERS_REQUIRING_OWNER

    assert mapped | blocked == tracked
    assert not mapped & blocked
    assert all(
        classifier._EVIDENCE_HELPER_OWNERSHIP_TEST in owners
        for owners in classifier._EVIDENCE_HELPER_TEST_OWNERS.values()
    )

    for source, owners in sorted(classifier._EVIDENCE_HELPER_TEST_OWNERS.items()):
        assert owners, source
        for owner in owners:
            path = ROOT / owner
            assert path.is_file(), (source, owner)
            assert not path.is_symlink(), (source, owner)
        assert classifier._evidence_helper_owner_targets(ROOT, source)


@pytest.mark.parametrize(
    ("value", "schema", "expected"),
    (
        (True, {"type": "integer"}, False),
        (1, {"type": "integer", "minimum": 1, "maximum": 1}, True),
        (1.0, {"type": "integer"}, True),
        (1.5, {"type": "integer"}, False),
        ("x", {"unknown": True}, False),
        ("x", {"$ref": "https://example.invalid/schema"}, False),
        ("x", {"$ref": "#/$defs/missing", "$defs": {}}, False),
        (
            "x",
            {
                "$ref": "#/$defs/loop",
                "$defs": {"loop": {"$ref": "#/$defs/loop"}},
            },
            False,
        ),
        ("x", {"type": "string", "pattern": "["}, False),
        ("2026-07-21", {"type": "string", "format": "date-time"}, False),
        (
            "2026-07-21t12:00:00.125-07:30",
            {"type": "string", "format": "date-time"},
            True,
        ),
        ("2026-02-29T12:00:00Z", {"type": "string", "format": "date-time"}, False),
        (
            ["a", "b"],
            {
                "type": "array",
                "prefixItems": [{"const": "a"}],
                "items": False,
            },
            False,
        ),
        (
            {"kind": "ok"},
            {
                "type": "object",
                "required": ["kind"],
                "properties": {"kind": {"const": "ok"}},
                "additionalProperties": False,
            },
            True,
        ),
        (
            {},
            {
                "type": "object",
                "required": ["kind"],
                "properties": {"kind": {"const": "ok"}},
                "additionalProperties": False,
            },
            False,
        ),
        (
            {"kind": "wrong"},
            {
                "type": "object",
                "required": ["kind"],
                "properties": {"kind": {"const": "ok"}},
                "additionalProperties": False,
            },
            False,
        ),
        (
            {"kind": "ok", "extra": True},
            {
                "type": "object",
                "required": ["kind"],
                "properties": {"kind": {"const": "ok"}},
                "additionalProperties": False,
            },
            False,
        ),
        (
            {"kind": "a", "a": 1},
            {
                "type": "object",
                "properties": {
                    "kind": {"enum": ["a", "b"]},
                    "a": {"type": "integer"},
                    "b": {"type": "integer"},
                },
                "if": {
                    "properties": {"kind": {"const": "a"}},
                    "required": ["kind"],
                },
                "then": {"required": ["a"]},
                "else": {"required": ["b"]},
                "additionalProperties": False,
            },
            True,
        ),
        (
            {"kind": "a"},
            {
                "type": "object",
                "properties": {
                    "kind": {"enum": ["a", "b"]},
                    "a": {"type": "integer"},
                    "b": {"type": "integer"},
                },
                "if": {
                    "properties": {"kind": {"const": "a"}},
                    "required": ["kind"],
                },
                "then": {"required": ["a"]},
                "else": {"required": ["b"]},
                "additionalProperties": False,
            },
            False,
        ),
        (
            "abc",
            {
                "allOf": [
                    {"type": "string", "minLength": 3},
                    {"type": "string", "maxLength": 3},
                ],
                "anyOf": [{"const": "abc"}, {"const": "xyz"}],
            },
            True,
        ),
        (
            "abcd",
            {
                "allOf": [
                    {"type": "string", "minLength": 3},
                    {"type": "string", "maxLength": 3},
                ],
                "anyOf": [{"const": "abc"}, {"const": "xyz"}],
            },
            False,
        ),
        (
            "def",
            {
                "allOf": [
                    {"type": "string", "minLength": 3},
                    {"type": "string", "maxLength": 3},
                ],
                "anyOf": [{"const": "abc"}, {"const": "xyz"}],
            },
            False,
        ),
        (
            {"kind": "b"},
            {
                "type": "object",
                "properties": {
                    "kind": {"enum": ["a", "b"]},
                    "a": {"type": "integer"},
                    "b": {"type": "integer"},
                },
                "if": {
                    "properties": {"kind": {"const": "a"}},
                    "required": ["kind"],
                },
                "then": {"required": ["a"]},
                "else": {"required": ["b"]},
                "additionalProperties": False,
            },
            False,
        ),
        (
            {"name": "bound"},
            {
                "$defs": {
                    "record": {
                        "type": "object",
                        "required": ["name"],
                        "properties": {"name": {"const": "bound"}},
                        "additionalProperties": False,
                    }
                },
                "$ref": "#/$defs/record",
            },
            True,
        ),
    ),
)
def test_strict_json_schema_fails_closed(value, schema, expected: bool) -> None:
    assert strict_json_schema.is_valid(value, schema) is expected


def test_refresh_step_logs_wrapper_delegates_cli_dispatch(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    assert refresh_wrapper.main is refresh_impl.main
    calls: list[tuple[str, ...] | None] = []

    def fake_main(argv=None) -> int:
        calls.append(None if argv is None else tuple(argv))
        return 23

    monkeypatch.setattr(refresh_impl, "main", fake_main)
    with pytest.raises(SystemExit) as excinfo:
        runpy.run_path(
            str(ROOT / "tools/evidence/refresh_step_logs_manifest.py"),
            run_name="__main__",
        )

    assert excinfo.value.code == 23
    assert calls == [None]
