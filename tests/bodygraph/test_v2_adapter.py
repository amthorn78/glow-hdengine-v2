from __future__ import annotations

from engine.bodygraph.v2_adapter import CHART_RESULT_REQUIRED_FIELDS, V2ChartAdapterContext, adapt_v2_chart_payload


def chart_result_payload() -> dict[str, object]:
    payload: dict[str, object] = {field: f"value:{field}" for field in CHART_RESULT_REQUIRED_FIELDS}
    payload.update({
        "activations": {"design": {}, "personality": {}},
        "centers": ["G", "Sacral"],
        "channelsLong": ["The Channel of Charisma (20-34)"],
        "channelsShort": ["20-34"],
        "gates": ["20", "34"],
    })
    return payload


def context(**overrides: str) -> V2ChartAdapterContext:
    values = {
        "person_uid": "person-001",
        "user_id": "123e4567-e89b-12d3-a456-426614174000",
        "vendor": "hdapi",
        "vendor_version": 2,
        "input_fingerprint": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "route_family": "recommended_v2_chart",
        "route": "charts",
        "payload_family": "ChartResult",
    }
    values.update(overrides)
    return V2ChartAdapterContext(**values)


def test_context_backed_chart_result_maps_without_raw_payload() -> None:
    result = adapt_v2_chart_payload({"timestamp": "2026-07-05T00:00:00.000Z", "success": True, "message": "Chart generated", "errorCode": "", "type": "ChartResult", "data": chart_result_payload()}, context())
    assert result.status == "mapped"
    assert result.code == "ADAPTER_MAPPED"
    rendered = result.as_dict()
    assert rendered["resolved"]["person_uid"] == "person-001"
    assert rendered["resolved"]["person"] == {"person_uid": "person-001"}
    assert rendered["cache"] == {
        "input_fingerprint": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "payload": rendered["resolved"],
        "payload_posture": "adapter_mapped_no_raw_vendor_payload",
        "user_id": "123e4567-e89b-12d3-a456-426614174000",
        "vendor": "hdapi",
        "vendor_version": 2,
    }
    assert "activations" not in rendered["cache"]["payload"]["bodygraph"]
    assert "data" not in rendered


def test_unwrapped_chart_result_maps_without_envelope() -> None:
    result = adapt_v2_chart_payload(chart_result_payload(), context())
    assert result.status == "mapped"
    assert result.code == "ADAPTER_MAPPED"
    assert result.as_dict()["resolved"]["person_uid"] == "person-001"


def test_cache_metadata_must_match_persistence_contract() -> None:
    assert adapt_v2_chart_payload(chart_result_payload(), context(user_id="user-001")).code == "ADAPTER_CONTEXT_INSUFFICIENT"
    assert adapt_v2_chart_payload(chart_result_payload(), context(input_fingerprint="sha256:fixture")).code == "ADAPTER_CONTEXT_INSUFFICIENT"
    assert adapt_v2_chart_payload(chart_result_payload(), context(vendor_version=0)).code == "ADAPTER_CONTEXT_INSUFFICIENT"


def test_missing_internal_identity_context_fails_closed() -> None:
    result = adapt_v2_chart_payload({"timestamp": "2026-07-05T00:00:00.000Z", "success": True, "message": "Chart generated", "errorCode": "", "type": "ChartResult", "data": chart_result_payload()}, context(person_uid=""))
    assert result.status == "unsupported"
    assert result.code == "ADAPTER_CONTEXT_INSUFFICIENT"
    assert "person_uid" in result.missing_internal_contract_fields


def test_missing_vendor_detail_fields_fail_closed() -> None:
    data = chart_result_payload()
    data.pop("birthDateUtc")
    data.pop("authority")
    result = adapt_v2_chart_payload({"timestamp": "2026-07-05T00:00:00.000Z", "success": True, "message": "Chart generated", "errorCode": "", "type": "ChartResult", "data": data}, context())
    assert result.code == "ADAPTER_VENDOR_DETAIL_INSUFFICIENT"
    assert result.status == "unsupported"
    assert {"authority", "birthDateUtc"} <= set(result.missing_vendor_detail_fields)


def test_malformed_vendor_detail_shapes_fail_closed() -> None:
    data = chart_result_payload()
    data["centers"] = "G"
    data["activations"] = "not-an-object"
    result = adapt_v2_chart_payload(data, context())
    assert result.code == "ADAPTER_VENDOR_DETAIL_INSUFFICIENT"
    assert {"activations", "centers"} <= set(result.missing_vendor_detail_fields)


def test_chart_simple_result_reports_detail_insufficient_on_simple_route() -> None:
    result = adapt_v2_chart_payload(
        {"timestamp": "2026-07-05T00:00:00.000Z", "success": True, "message": "Chart generated", "errorCode": "", "type": "ChartSimpleResult", "data": {"type": "Generator", "profile": "1/3", "gates": [], "channelsShort": [], "centers": {}}},
        context(payload_family="ChartSimpleResult", route="charts/simple"),
    )
    assert result.code == "ADAPTER_VENDOR_DETAIL_INSUFFICIENT"
    assert "birthDateUtc" in result.missing_vendor_detail_fields


def test_chart_route_rejects_chart_simple_family() -> None:
    result = adapt_v2_chart_payload(
        {"timestamp": "2026-07-05T00:00:00.000Z", "success": True, "message": "Chart generated", "errorCode": "", "type": "ChartSimpleResult", "data": {"type": "Generator", "profile": "1/3", "gates": [], "channelsShort": [], "centers": {}}},
        context(payload_family="ChartSimpleResult"),
    )
    assert result.code == "ADAPTER_ROUTE_PAYLOAD_FAMILY_MISMATCH"


def test_malformed_payload_and_missing_data_fail_closed() -> None:
    assert adapt_v2_chart_payload([], context()).code == "ADAPTER_MALFORMED_PAYLOAD"
    assert adapt_v2_chart_payload({"timestamp": "2026-07-05T00:00:00.000Z", "success": True, "message": "Chart generated", "errorCode": "", "type": "ChartResult", "data": None}, context()).code == "ADAPTER_MISSING_DATA"


def test_unsupported_payload_family_fails_closed() -> None:
    result = adapt_v2_chart_payload({"timestamp": "2026-07-05T00:00:00.000Z", "success": True, "message": "Chart generated", "errorCode": "", "type": "OtherResult", "data": {}}, context(payload_family="OtherResult"))
    assert result.code == "ADAPTER_UNSUPPORTED_PAYLOAD_FAMILY"


def test_vendor_request_route_label_maps() -> None:
    result = adapt_v2_chart_payload(chart_result_payload(), context(route="vendor.hdapi.post:/charts"))
    assert result.status == "mapped"
    assert result.code == "ADAPTER_MAPPED"


def test_incomplete_standard_response_envelope_fails_closed() -> None:
    result = adapt_v2_chart_payload({"data": chart_result_payload()}, context())
    assert result.status == "unsupported"
    assert result.code == "ADAPTER_MALFORMED_ENVELOPE"


def test_success_envelope_requires_string_error_code() -> None:
    result = adapt_v2_chart_payload(
        {"timestamp": "2026-07-05T00:00:00.000Z", "success": True, "message": "Chart generated", "errorCode": None, "type": "ChartResult", "data": chart_result_payload()},
        context(),
    )
    assert result.status == "unsupported"
    assert result.code == "ADAPTER_MALFORMED_ENVELOPE"


def test_failed_standard_response_envelope_fails_closed() -> None:
    result = adapt_v2_chart_payload(
        {"timestamp": "2026-07-05T00:00:00.000Z", "success": False, "message": "Invalid birthdate", "errorCode": "INVALID_BIRTHDATE", "type": "ChartResult", "data": chart_result_payload()},
        context(),
    )
    assert result.status == "unsupported"
    assert result.code == "ADAPTER_VENDOR_ENVELOPE_UNSUCCESSFUL"


def test_route_payload_family_mismatch_fails_closed() -> None:
    result = adapt_v2_chart_payload(chart_result_payload(), context(route="charts/simple", payload_family="ChartResult"))
    assert result.status == "unsupported"
    assert result.code == "ADAPTER_ROUTE_PAYLOAD_FAMILY_MISMATCH"


def test_wrong_route_family_fails_closed() -> None:
    result = adapt_v2_chart_payload({"timestamp": "2026-07-05T00:00:00.000Z", "success": True, "message": "Chart generated", "errorCode": "", "type": "ChartResult", "data": chart_result_payload()}, context(route_family="legacy_bodygraph"))
    assert result.code == "ADAPTER_WRONG_ROUTE_FAMILY"


def test_partial_payload_fails_closed() -> None:
    result = adapt_v2_chart_payload({"timestamp": "2026-07-05T00:00:00.000Z", "success": True, "message": "Chart generated", "errorCode": "", "type": "ChartResult", "data": {"type": "Generator"}}, context())
    assert result.code == "ADAPTER_VENDOR_DETAIL_INSUFFICIENT"
    assert "profile" in result.missing_vendor_detail_fields
