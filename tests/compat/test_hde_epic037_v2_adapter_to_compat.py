"""EPIC037 v2 adapter-to-compat generator against the corrected evaluation seams.

Positive matrix: the synthetic complete release is injected through the
evaluation seam.  Check mode without an admitted release (reached through the
seam now that the repository root admits) validates the frozen capture-time
artifacts with their nonclaims and never regenerates them (PF10 §2.15); on the
admitted root the owner's live comparison reports those PR-04 records stale and
writes nothing.
"""
import json

import pytest

from engine.categories.registry import FROZEN_MAGIC10_ORDER
from engine.compat import compute
from engine.compat.compute import orient
from engine.config.registry_loader import SchemaValidationError
from tests.support.pr04_fixtures import CLOSED_RAILS, build_bundle, build_pack, inject_seams
from tools.evidence import generate_hde_epic037_v2_to_compat as generator

UUID_A = "123e4567-e89b-12d3-a456-426614174000"
UUID_B = "123e4567-e89b-12d3-a456-426614174001"


@pytest.fixture(scope="module")
def bundle(tmp_path_factory):
    return build_bundle(tmp_path_factory.mktemp("pr04-epic037-bundle"))


@pytest.fixture(scope="module")
def pack(tmp_path_factory):
    return build_pack(tmp_path_factory.mktemp("pr04-epic037-pack"))


@pytest.fixture
def admitted(monkeypatch, bundle, pack):
    inject_seams(monkeypatch, bundle, pack)
    return bundle


def test_mapped_v2_adapter_outputs_feed_evaluate_pair(admitted) -> None:
    pair = generator._mapped_pair()
    assert pair["a"]["resolved"]["person_uid"] == f"person-{UUID_A}"
    assert pair["a"]["cache"]["user_id"] == UUID_A
    compat = generator._compat(pair["a"], pair["b"])

    assert compat["schema"] == "magic10_compat_result.v1"
    assert compat["release_id"] == admitted.release_id
    assert [item["category_id"] for item in compat["categories"]] == list(FROZEN_MAGIC10_ORDER)
    lo, hi = orient(generator._party(pair["a"]), generator._party(pair["b"]))
    assert (lo.canonical_person_id, hi.canonical_person_id) == (UUID_A, UUID_B)
    assert compat["pair_key"] == generator._compat(pair["b"], pair["a"])["pair_key"]


def test_v2_to_compat_two_run_and_pair_order_identity(admitted) -> None:
    first = generator.canonical_json_bytes(generator._proof_payload("2026-07-05T00:00:00Z"))
    second = generator.canonical_json_bytes(generator._proof_payload("2026-07-05T00:00:00Z"))
    assert first == second
    proof = json.loads(first)
    assert proof["compat_acceptance"]["function"] == "engine.compat.compute.evaluate_pair"
    assert proof["compat_acceptance"]["result_schema"] == "magic10_compat_result.v1"

    pair = generator._mapped_pair()
    ab = generator.canonical_json_bytes(generator._compat(pair["a"], pair["b"]))
    ba = generator.canonical_json_bytes(generator._compat(pair["b"], pair["a"]))
    assert ab == ba

    outputs = generator.build_outputs("2026-07-05T00:00:00Z")
    pair_order = json.loads(outputs[generator.PAIR_ORDER])
    assert pair_order["canonical_ab_ba_bytes_identical"] is True
    assert pair_order["normalized_left_person_uid"] < pair_order["normalized_right_person_uid"]
    assert pair_order["pair_order_rule"].startswith("engine.compat.compute.orient")


def test_v2_to_compat_public_reader_boundary_fixture(admitted) -> None:
    boundary = generator._boundary(generator._mapped_pair(), "2026-07-05T00:00:00Z", generator._common("2026-07-05T00:00:00Z"))
    assert boundary["public_reader_bands_only"] is True
    assert boundary["public_reader_numeric_free"] is True
    assert boundary["forbidden_public_term_hits"] == []
    assert boundary["public_reader_category_keys"] == ["band", "id"]
    assert boundary["new_public_reader_surface"] == {"route": False, "flag": False, "payload_field": False, "transport_behavior": False, "http_home": False}
    # Public Reader evidence remains serializable as canonical JSON and records no forbidden public hits.
    assert json.loads(json.dumps(boundary, sort_keys=True))["forbidden_public_term_hits"] == []


def _refuse_admission(monkeypatch) -> None:
    """The repository root is admitted; the non-admitted branch is reached through the seam."""

    def refuse():
        raise SchemaValidationError("INCOMPLETE_RELEASE_ROSTER", "patched provider")

    monkeypatch.setattr(compute, "_BUNDLE_PROVIDER", refuse)


def test_check_mode_without_admission_validates_frozen_records_and_write_mode_refuses(monkeypatch, capsys) -> None:
    for key, value in CLOSED_RAILS.items():
        monkeypatch.setenv(key, value)
    _refuse_admission(monkeypatch)
    monkeypatch.setattr(generator, "build_outputs", lambda *a, **k: pytest.fail("live regeneration attempted"))
    monkeypatch.setattr(generator, "write_outputs", lambda *a, **k: pytest.fail("write attempted"))

    generator.main(["--check"])
    assert capsys.readouterr().out.strip() == generator.FROZEN_CHECK_LINE
    frozen = json.loads(generator.PROOF.read_bytes())
    assert frozen["compat_acceptance"]["function"] == "engine.compat.compute.conjunction_public"  # frozen capture-time record

    with pytest.raises(SystemExit, match=generator.REQUIRES_ADMITTED_RELEASE):
        generator.main([])


def test_check_mode_on_the_admitted_root_reports_the_frozen_records_stale_without_writing(monkeypatch) -> None:
    """On the admitted repository root the owner compares a live evaluation with the tracked
    PR-04 records.  Those capture-time records predate admission, so check mode reports them
    stale and writes nothing; regenerating them is the EPIC037 evidence owner's decision."""
    for key, value in CLOSED_RAILS.items():
        monkeypatch.setenv(key, value)
    monkeypatch.setattr(compute, "_BUNDLE_PROVIDER", compute.load_active_mechanics_bundle)
    tracked = [generator.PROOF, generator.TWO_RUN, generator.PAIR_ORDER, generator.BOUNDARY]
    tracked += [path.with_name(path.name + ".path_proof.txt") for path in list(tracked)]
    before = {path: path.read_bytes() for path in tracked if path.exists()}
    with pytest.raises(SystemExit) as raised:
        generator.main(["--check"])
    assert str(raised.value).startswith("STALE_HDE_EPIC037_PR04_V2_TO_COMPAT:")
    assert {path: path.read_bytes() for path in before} == before
