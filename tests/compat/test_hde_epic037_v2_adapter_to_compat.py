import json

from tools.evidence import generate_hde_epic037_v2_to_compat as generator


def test_mapped_v2_adapter_outputs_feed_conjunction_public() -> None:
    pair = generator._mapped_pair()
    compat = generator._compat(pair["a"]["resolved"], pair["b"]["resolved"])

    assert compat["conjunction"]["left"]["person_uid"] == "person-epic037-pr04-a"
    assert compat["conjunction"]["right"]["person_uid"] == "person-epic037-pr04-b"
    assert len(compat["conjunction"]["compat"]["categories"]) == 10
    assert compat["conjunction"]["compat"]["meta"]["invocation_tag"] == "epic037-pr04-fixture"


def test_v2_to_compat_two_run_and_pair_order_identity() -> None:
    first = generator.canonical_json_bytes(generator._proof_payload("2026-07-05T00:00:00Z"))
    second = generator.canonical_json_bytes(generator._proof_payload("2026-07-05T00:00:00Z"))
    assert first == second

    pair = generator._mapped_pair()
    ab = generator.canonical_json_bytes(generator._compat(pair["a"]["resolved"], pair["b"]["resolved"]))
    ba = generator.canonical_json_bytes(generator._compat(pair["b"]["resolved"], pair["a"]["resolved"]))
    assert ab == ba


def test_v2_to_compat_public_reader_boundary_fixture() -> None:
    boundary = generator._boundary(generator._mapped_pair(), "2026-07-05T00:00:00Z", generator._common("2026-07-05T00:00:00Z"))
    assert boundary["public_reader_bands_only"] is True
    assert boundary["public_reader_numeric_free"] is True
    assert boundary["forbidden_public_term_hits"] == []
    assert boundary["new_public_reader_surface"] == {"route": False, "flag": False, "payload_field": False, "transport_behavior": False, "http_home": False}
    # Public Reader evidence remains serializable as canonical JSON and records no forbidden public hits.
    assert json.loads(json.dumps(boundary, sort_keys=True))["forbidden_public_term_hits"] == []
