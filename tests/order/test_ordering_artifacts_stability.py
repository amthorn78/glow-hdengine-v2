from __future__ import annotations

from pathlib import Path

from engine.order import artifacts as order_artifacts


ARTIFACT_DIR = Path("artifacts/engine/order")


def test_ordering_artifacts_match_generators():
    ctx = order_artifacts.load_ordering_context(Path.cwd())

    expected_channels = order_artifacts.render_json_snapshot(order_artifacts.channels_sorted(ctx))
    expected_categories = order_artifacts.render_json_snapshot(order_artifacts.categories_sorted(ctx))
    expected_props = order_artifacts.render_props_log(order_artifacts.props_total_order_lines(ctx))
    expected_abba = order_artifacts.abba_identity_digest(ctx)

    assert (ARTIFACT_DIR / "channels_sorted.snapshot.json").read_bytes() == expected_channels
    assert (ARTIFACT_DIR / "categories_iter.snapshot.json").read_bytes() == expected_categories
    assert (ARTIFACT_DIR / "props_total_order.log").read_bytes() == expected_props
    assert (ARTIFACT_DIR / "abba_identity.bytes").read_bytes() == expected_abba
