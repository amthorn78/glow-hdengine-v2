from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

import pytest

from engine.config.registry_loader import (
    ADMITTED_RELEASE_BUILT_AT_UTC,
    ADMITTED_RELEASE_ROSTER,
    ADMITTED_RELEASE_VERSION,
    _load_active_mechanics_bundle_from_root,
)
from engine.runtime.identity import _manifest_release_id_from_bytes
from engine.serializer import canon
from scripts import cut_release_manifest as cutter
from tests.config.helpers import synthetic_complete_release_root, write_canonical

# The fifteen members of the pre-PR06 release manifest (version 1.0.0), used
# as the existing-row baseline that a roster cut must complete to 45 members.
_PRE_PR06_MEMBERS = (
    "adapter/http_reader.py",
    "catalog/channels_v1.json",
    "catalog/gates_v1.json",
    "catalog/magic10.json",
    "catalog/magic10_caps.json",
    "catalog/magic10_seeds.json",
    "catalog/narratives/keys.json",
    "catalog/narratives/manifest.json",
    "catalog/narratives/palettes.json",
    "catalog/narratives/suppression_map.json",
    "catalog/narratives/templates.json",
    "engine/presenter/emitter.py",
    "engine/serializer/canon.py",
    "math/thresholds.json",
    "migrations/005_identity.sql",
)
_CUT = {"version": ADMITTED_RELEASE_VERSION, "built_at_utc": ADMITTED_RELEASE_BUILT_AT_UTC}


def _closed(monkeypatch) -> None:
    for name, value in {
        "SAFE_MODE": "1",
        "ALLOW_NETWORK": "0",
        "LC_ALL": "C",
        "LANG": "C",
        "TZ": "UTC",
    }.items():
        monkeypatch.setenv(name, value)


def _baseline_manifest(root: Path, members: tuple[str, ...] = _PRE_PR06_MEMBERS) -> Path:
    """Write a pre-PR06-shaped manifest with stale rows into a fixture root."""
    manifest = root / "catalog/manifest.json"
    write_canonical(
        manifest,
        {
            "root": "catalog/",
            "version": "1.0.0",
            "built_at_utc": "2025-12-26T00:00:00Z",
            "files": [
                {"path": name, "sha256": "0" * 64, "size": 0} for name in sorted(members)
            ],
        },
    )
    return manifest


@pytest.fixture
def complete_root(tmp_path, monkeypatch) -> Path:
    _closed(monkeypatch)
    return synthetic_complete_release_root(tmp_path)


def test_release_cut_updates_only_manifest_and_reaches_read_only_fixed_point(
    tmp_path,
    monkeypatch,
):
    _closed(monkeypatch)
    source = tmp_path / "payload.sql"
    source.write_bytes(b"new release bytes\n")
    catalog = tmp_path / "catalog"
    catalog.mkdir()
    manifest = catalog / "manifest.json"
    manifest.write_bytes(
        canon.sercanon(
            {
                "root": "catalog/",
                "version": "1.0.0",
                "built_at_utc": "2025-12-26T00:00:00Z",
                "files": [
                    {
                        "path": "payload.sql",
                        "sha256": "0" * 64,
                        "size": 0,
                    }
                ],
            },
            sort_keys=True,
        )
    )

    assert cutter.cut_manifest(
        manifest,
        version="1.1.0",
        built_at_utc="2026-07-23T00:00:00Z",
    ) == 0
    payload = json.loads(manifest.read_bytes())
    assert set(payload) == {"root", "version", "built_at_utc", "files"}
    assert payload["version"] == "1.1.0"
    assert payload["built_at_utc"] == "2026-07-23T00:00:00Z"
    assert payload["files"] == [
        {
            "path": "payload.sql",
            "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
            "size": len(source.read_bytes()),
        }
    ]
    before = {path.name for path in tmp_path.rglob("*") if path.is_file()}
    assert cutter.cut_manifest(
        manifest,
        version="1.1.0",
        built_at_utc="2026-07-23T00:00:00Z",
        check=True,
    ) == 0
    assert {path.name for path in tmp_path.rglob("*") if path.is_file()} == before


def test_release_cut_rejects_implicit_or_malformed_identity_inputs(
    tmp_path,
    monkeypatch,
):
    _closed(monkeypatch)
    manifest = tmp_path / "manifest.json"
    manifest.write_text("{}\n", encoding="utf-8")

    assert cutter.main(
        [
            "--manifest",
            str(manifest),
            "--version",
            "latest",
            "--built-at-utc",
            "now",
        ]
    ) == 1


def test_release_cut_accepts_full_semver_and_rejects_leading_zero(
    tmp_path,
    monkeypatch,
):
    _closed(monkeypatch)
    source = tmp_path / "payload.sql"
    source.write_bytes(b"payload\n")
    catalog = tmp_path / "catalog"
    catalog.mkdir()
    manifest = catalog / "manifest.json"
    payload = {
        "root": "catalog/",
        "version": "1.0.0",
        "built_at_utc": "2025-12-26T00:00:00Z",
        "files": [{"path": "payload.sql", "sha256": "0" * 64, "size": 0}],
    }
    manifest.write_bytes(canon.sercanon(payload, sort_keys=True))

    assert cutter.cut_manifest(
        manifest,
        version="1.2.3-rc.1+build.5",
        built_at_utc="2026-07-23T00:00:00Z",
    ) == 0
    with pytest.raises(ValueError, match="release_version_invalid"):
        cutter.cut_manifest(
            manifest,
            version="01.2.3",
            built_at_utc="2026-07-23T00:00:00Z",
        )


@pytest.mark.parametrize(
    ("mutation", "message"),
    (
        ("root", "release_manifest_root_invalid"),
        ("empty", "release_manifest_files_invalid"),
        ("extra", "release_manifest_entry_invalid"),
        ("duplicate", "release_manifest_entry_path_unsafe"),
        ("self", "release_manifest_entry_path_unsafe"),
        ("traversal", "release_manifest_entry_path_unsafe"),
        ("backslash", "release_manifest_entry_path_unsafe"),
    ),
)
def test_release_cut_rejects_manifest_roster_mutations(
    tmp_path,
    monkeypatch,
    mutation,
    message,
):
    _closed(monkeypatch)
    source = tmp_path / "payload.sql"
    source.write_bytes(b"payload\n")
    catalog = tmp_path / "catalog"
    catalog.mkdir()
    manifest = catalog / "manifest.json"
    entry = {"path": "payload.sql", "sha256": "0" * 64, "size": 0}
    payload = {
        "root": "catalog/",
        "version": "1.0.0",
        "built_at_utc": "2025-12-26T00:00:00Z",
        "files": [entry],
    }
    if mutation == "root":
        payload["root"] = "alternate/"
    elif mutation == "empty":
        payload["files"] = []
    elif mutation == "extra":
        entry["unknown"] = True
    elif mutation == "duplicate":
        payload["files"].append(dict(entry))
    elif mutation == "self":
        entry["path"] = "catalog/manifest.json"
    elif mutation == "backslash":
        entry["path"] = "catalog\\payload.sql"
    else:
        entry["path"] = "../outside"
    manifest.write_bytes(canon.sercanon(payload, sort_keys=True))

    with pytest.raises(ValueError, match=message):
        cutter.cut_manifest(
            manifest,
            version="1.0.1",
            built_at_utc="2026-07-23T00:00:00Z",
        )


def test_release_cut_rejects_noncanonical_input(tmp_path, monkeypatch):
    _closed(monkeypatch)
    source = tmp_path / "payload.sql"
    source.write_bytes(b"payload\n")
    catalog = tmp_path / "catalog"
    catalog.mkdir()
    manifest = catalog / "manifest.json"
    manifest.write_text(
        json.dumps(
            {
                "root": "catalog/",
                "version": "1.0.0",
                "built_at_utc": "2025-12-26T00:00:00Z",
                "files": [
                    {"path": "payload.sql", "sha256": "0" * 64, "size": 0}
                ],
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="release_manifest_not_canonical"):
        cutter.cut_manifest(
            manifest,
            version="1.0.1",
            built_at_utc="2026-07-23T00:00:00Z",
        )


def test_release_cut_rejects_symlinked_source(tmp_path, monkeypatch):
    _closed(monkeypatch)
    source = tmp_path / "payload.sql"
    source.write_bytes(b"payload\n")
    linked = tmp_path / "linked.sql"
    linked.symlink_to(source.name)
    catalog = tmp_path / "catalog"
    catalog.mkdir()
    manifest = catalog / "manifest.json"
    manifest.write_bytes(
        canon.sercanon(
            {
                "root": "catalog/",
                "version": "1.0.0",
                "built_at_utc": "2025-12-26T00:00:00Z",
                "files": [
                    {"path": "linked.sql", "sha256": "0" * 64, "size": 0}
                ],
            },
            sort_keys=True,
        )
    )

    with pytest.raises(ValueError, match="release_manifest_source_symlink"):
        cutter.cut_manifest(
            manifest,
            version="1.0.1",
            built_at_utc="2026-07-23T00:00:00Z",
        )


def test_release_cut_private_publisher_receives_validated_bytes_and_check_never_calls_it(tmp_path, monkeypatch):
    _closed(monkeypatch)
    source = tmp_path / "payload.sql"
    source.write_bytes(b"actual callback source\n")
    manifest = tmp_path / "catalog/manifest.json"
    manifest.parent.mkdir()
    original = canon.sercanon({
        "root": "catalog/", "version": "1.0.0", "built_at_utc": "2025-12-26T00:00:00Z",
        "files": [{"path": "payload.sql", "sha256": "0" * 64, "size": 0}],
    }, sort_keys=True)
    manifest.write_bytes(original)
    before = manifest.read_bytes(), manifest.stat().st_mtime_ns
    publications = []

    def publisher(path, content):
        publications.append((path, content))

    inputs = {"version": "1.0.1", "built_at_utc": "2026-07-23T00:00:00Z", "_publish": publisher}
    assert cutter.cut_manifest(manifest, check=True, **inputs) == 1
    assert not publications
    assert (manifest.read_bytes(), manifest.stat().st_mtime_ns) == before
    assert cutter.cut_manifest(manifest, **inputs) == 0
    assert len(publications) == 1
    path, content = publications[0]
    assert path == manifest
    rendered = json.loads(content)
    assert rendered["version"] == inputs["version"]
    assert rendered["built_at_utc"] == inputs["built_at_utc"]
    assert rendered["files"] == [{"path": "payload.sql", "sha256": hashlib.sha256(source.read_bytes()).hexdigest(), "size": len(source.read_bytes())}]
    assert content == canon.sercanon(rendered, sort_keys=True)
    assert (manifest.read_bytes(), manifest.stat().st_mtime_ns) == before
    # Only the injected publisher performs publication; the cutter must neither
    # bypass it nor invoke it when verifying an already current manifest.
    manifest.write_bytes(content)
    before = manifest.read_bytes(), manifest.stat().st_mtime_ns
    assert cutter.cut_manifest(manifest, check=True, **inputs) == 0
    assert len(publications) == 1
    assert (manifest.read_bytes(), manifest.stat().st_mtime_ns) == before


def test_refresh_cut_validates_member_format_without_a_roster(tmp_path, monkeypatch):
    """Format validation precedes hashing in both modes; an unsupported member refuses."""
    _closed(monkeypatch)
    source = tmp_path / "payload.txt"
    source.write_bytes(b"payload\n")
    manifest = tmp_path / "catalog/manifest.json"
    manifest.parent.mkdir()
    original = canon.sercanon({
        "root": "catalog/", "version": "1.0.0", "built_at_utc": "2025-12-26T00:00:00Z",
        "files": [{"path": "payload.txt", "sha256": "0" * 64, "size": 0}],
    }, sort_keys=True)
    manifest.write_bytes(original)

    with pytest.raises(
        ValueError,
        match="release_manifest_member_format_invalid:payload.txt:UNSUPPORTED_MEMBER_FORMAT",
    ):
        cutter.cut_manifest(manifest, version="1.0.1", built_at_utc="2026-07-23T00:00:00Z")
    assert manifest.read_bytes() == original


def test_roster_cut_constructs_exactly_the_admitted_roster(complete_root: Path) -> None:
    helper_manifest = (complete_root / "catalog/manifest.json").read_bytes()
    manifest = _baseline_manifest(complete_root)
    assert cutter.cut_manifest(manifest, roster=ADMITTED_RELEASE_ROSTER, check=True, **_CUT) == 1
    assert cutter.cut_manifest(manifest, roster=ADMITTED_RELEASE_ROSTER, **_CUT) == 0

    raw = manifest.read_bytes()
    payload = json.loads(raw)
    assert set(payload) == {"root", "version", "built_at_utc", "files"}
    assert payload["root"] == "catalog/"
    assert payload["version"] == ADMITTED_RELEASE_VERSION
    assert payload["built_at_utc"] == ADMITTED_RELEASE_BUILT_AT_UTC
    assert len(payload["files"]) == 45
    assert tuple(row["path"] for row in payload["files"]) == ADMITTED_RELEASE_ROSTER
    assert "catalog/manifest.json" not in {row["path"] for row in payload["files"]}
    for row in payload["files"]:
        body = (complete_root / row["path"]).read_bytes()
        assert set(row) == {"path", "sha256", "size"}
        assert row["sha256"] == hashlib.sha256(body).hexdigest()
        assert row["size"] == len(body)
    assert raw == canon.sercanon(payload, sort_keys=True)
    assert raw == helper_manifest
    release_id = hashlib.sha256(raw).hexdigest()
    assert _manifest_release_id_from_bytes(raw) == release_id
    # Fixed point in both modes; a later member change breaks it.
    assert cutter.cut_manifest(manifest, roster=ADMITTED_RELEASE_ROSTER, check=True, **_CUT) == 0
    assert cutter.cut_manifest(manifest, check=True, **_CUT) == 0
    assert manifest.read_bytes() == raw
    assert _load_active_mechanics_bundle_from_root(complete_root).release_id == release_id
    member = complete_root / "migrations/005_identity.sql"
    member.write_bytes(member.read_bytes() + b"-- changed\n")
    assert cutter.cut_manifest(manifest, roster=ADMITTED_RELEASE_ROSTER, check=True, **_CUT) == 1


def test_roster_cut_refuses_each_missing_member_in_turn(complete_root: Path) -> None:
    manifest = _baseline_manifest(complete_root)
    before = manifest.read_bytes()
    for name in ADMITTED_RELEASE_ROSTER:
        member = complete_root / name
        body = member.read_bytes()
        member.unlink()
        with pytest.raises(ValueError, match="release_manifest_source_missing"):
            cutter.cut_manifest(manifest, roster=ADMITTED_RELEASE_ROSTER, **_CUT)
        assert manifest.read_bytes() == before
        member.write_bytes(body)
    assert cutter.cut_manifest(manifest, roster=ADMITTED_RELEASE_ROSTER, **_CUT) == 0


def test_roster_cut_refuses_a_non_input_extra_row(complete_root: Path) -> None:
    extra = complete_root / "extra/member.sql"
    extra.parent.mkdir()
    extra.write_bytes(b"select 1;\n")
    manifest = _baseline_manifest(complete_root, (*_PRE_PR06_MEMBERS, "extra/member.sql"))
    before = manifest.read_bytes()
    with pytest.raises(ValueError, match="release_manifest_extra_member:extra/member.sql"):
        cutter.cut_manifest(manifest, roster=ADMITTED_RELEASE_ROSTER, **_CUT)
    assert manifest.read_bytes() == before
    # Without a roster the existing rows are refreshed exactly as before.
    assert cutter.cut_manifest(manifest, **_CUT) == 0
    assert "extra/member.sql" in {row["path"] for row in json.loads(manifest.read_bytes())["files"]}


@pytest.mark.parametrize(
    "roster",
    (
        (),
        tuple(sorted((*ADMITTED_RELEASE_ROSTER, ADMITTED_RELEASE_ROSTER[0]))),
        tuple(reversed(ADMITTED_RELEASE_ROSTER)),
        ("/" + ADMITTED_RELEASE_ROSTER[0], *ADMITTED_RELEASE_ROSTER[1:]),
        tuple(sorted((*ADMITTED_RELEASE_ROSTER, "../outside.json"))),
        tuple(sorted((*ADMITTED_RELEASE_ROSTER, "catalog/manifest.json"))),
        tuple(sorted((*ADMITTED_RELEASE_ROSTER, "engine\\core\\core.py"))),
        tuple(sorted((*ADMITTED_RELEASE_ROSTER, ""))),
        tuple(sorted((*ADMITTED_RELEASE_ROSTER, "schemas/ü.json"))),
        (*ADMITTED_RELEASE_ROSTER[:-1], 42),
    ),
    ids=(
        "empty",
        "duplicate",
        "unsorted",
        "absolute",
        "traversal",
        "self_listing",
        "backslash",
        "empty_path",
        "non_ascii",
        "non_string",
    ),
)
def test_roster_cut_refuses_invalid_rosters(complete_root: Path, roster) -> None:
    manifest = _baseline_manifest(complete_root)
    before = manifest.read_bytes()
    with pytest.raises(ValueError, match="release_manifest_roster_invalid"):
        cutter.cut_manifest(manifest, roster=roster, **_CUT)
    assert manifest.read_bytes() == before


@pytest.mark.parametrize(
    ("path", "mutate", "code"),
    (
        (
            "schemas/gates_v1.schema.json",
            lambda raw: json.dumps(json.loads(raw), indent=2).encode("utf-8") + b"\n",
            "NONCANONICAL_JSON",
        ),
        ("math/thresholds.json", lambda raw: b"\xef\xbb\xbf" + raw, "INVALID_UTF8"),
        ("catalog/magic10.json", lambda raw: raw[:-1] + b"\xff\n", "INVALID_JSON"),
        ("engine/core/core.py", lambda raw: raw.rstrip(b"\n"), "INVALID_MEMBER_FINAL_LF"),
        ("engine/core/core.py", lambda raw: raw.rstrip(b"\n") + b"\n\n", "INVALID_MEMBER_FINAL_LF"),
        ("migrations/005_identity.sql", lambda raw: raw.replace(b"\n", b"\r\n"), "INVALID_MEMBER_FINAL_LF"),
        ("engine/cli/main.py", lambda raw: b"\xef\xbb\xbf" + raw, "INVALID_UTF8"),
        ("engine/cli/main.py", lambda raw: raw[:-1] + b"\xff\n", "INVALID_UTF8"),
        ("engine/bodygraph/gates.py", lambda raw: b"def broken(:\n", "INVALID_PYTHON_MEMBER"),
        ("migrations/005_identity.sql", lambda raw: b"\n", "EMPTY_MEMBER"),
    ),
    ids=(
        "noncanonical_json",
        "json_bom",
        "json_invalid_utf8",
        "py_missing_final_lf",
        "py_double_final_lf",
        "sql_crlf",
        "py_bom",
        "py_invalid_utf8",
        "py_syntax",
        "sql_empty",
    ),
)
def test_cut_refuses_members_that_fail_their_owning_format_before_hashing(
    complete_root: Path, path: str, mutate, code: str
) -> None:
    manifest = _baseline_manifest(complete_root)
    before = manifest.read_bytes()
    member = complete_root / path
    member.write_bytes(mutate(member.read_bytes()))
    with pytest.raises(
        ValueError,
        match=f"release_manifest_member_format_invalid:{re.escape(path)}:{code}",
    ):
        cutter.cut_manifest(manifest, roster=ADMITTED_RELEASE_ROSTER, **_CUT)
    assert manifest.read_bytes() == before


def test_roster_cut_refuses_a_symlinked_member(complete_root: Path) -> None:
    manifest = _baseline_manifest(complete_root)
    member = complete_root / "math/thresholds.json"
    real = complete_root / "math/thresholds.real.json"
    member.rename(real)
    member.symlink_to(real.name)
    with pytest.raises(ValueError, match="release_manifest_source_symlink"):
        cutter.cut_manifest(manifest, roster=ADMITTED_RELEASE_ROSTER, **_CUT)


def test_roster_check_mode_never_writes_and_publisher_receives_the_constructed_membership(
    complete_root: Path,
) -> None:
    manifest = _baseline_manifest(complete_root)
    before = manifest.read_bytes(), manifest.stat().st_mtime_ns
    publications = []

    def publisher(path, content):
        publications.append((path, content))

    assert cutter.cut_manifest(
        manifest, roster=ADMITTED_RELEASE_ROSTER, check=True, _publish=publisher, **_CUT
    ) == 1
    assert not publications
    assert (manifest.read_bytes(), manifest.stat().st_mtime_ns) == before
    assert cutter.cut_manifest(
        manifest, roster=ADMITTED_RELEASE_ROSTER, _publish=publisher, **_CUT
    ) == 0
    assert len(publications) == 1
    path, content = publications[0]
    assert path == manifest
    rendered = json.loads(content)
    assert tuple(row["path"] for row in rendered["files"]) == ADMITTED_RELEASE_ROSTER
    assert content == canon.sercanon(rendered, sort_keys=True)
    assert (manifest.read_bytes(), manifest.stat().st_mtime_ns) == before


def test_cli_roster_flag_cuts_the_admission_roster_and_reports_failures_on_stderr(
    complete_root: Path, capsys
) -> None:
    manifest = _baseline_manifest(complete_root)
    argv = [
        "--manifest", str(manifest),
        "--version", ADMITTED_RELEASE_VERSION,
        "--built-at-utc", ADMITTED_RELEASE_BUILT_AT_UTC,
    ]
    assert cutter.main([*argv, "--check", "--roster-from-admission"]) == 1
    assert cutter.main([*argv, "--roster-from-admission"]) == 0
    payload = json.loads(manifest.read_bytes())
    assert tuple(row["path"] for row in payload["files"]) == ADMITTED_RELEASE_ROSTER
    assert cutter.main([*argv, "--check", "--roster-from-admission"]) == 0
    assert cutter.main([*argv, "--check"]) == 0
    (complete_root / "math/thresholds.json").unlink()
    assert cutter.main([*argv, "--check", "--roster-from-admission"]) == 1
    assert "RELEASE_MANIFEST_CUT_FAILED:release_manifest_source_missing" in capsys.readouterr().err
