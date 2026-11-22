"""HDE-EPIC043 WU-PR-04: the v2 proof family's item index, pinned (HDE-DIST008.1).

One row per item of the HDE-DIST008.1 Magic10 v2 re-target note (F-01 to F-10)
and per item of the subtask description that the note does not replace (F-11 to
F-28, with F-21 split into its manifest-row and release-binding parts). Each row
names its passing cases and its refused mutations by ``path::function``, its
basis, and when its v2 evidence falls due: ``now``; ``WU-PR-09`` (the switch, for
surface-bound items whose v2 run starts there); ``WU-PR-10`` (the cut maxima and
``M10-G002`` to ``M10-G008``); ``WU-PR-13`` (the candidate run, where F-06 and F-08
were re-targeted to the admitted release).

The pin proves every item has at least one passing case and one refused
mutation, every node resolves to a top-level test function, and every mutation
lives in the family directory. It makes the family a runnable gate:
``python -m pytest -q -p no:cacheprovider tests/m10_v2`` runs all of it. A second
pin (HDE-EPIC043 WU-PR-13) refuses a broad exception handler in any module that
holds a mutation case, so a mutation case can pass only on a failed assertion or
the product's own typed refusal, never on an unrelated crash.
"""
from __future__ import annotations

import ast
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
FAMILY = "tests/m10_v2/"
K = "tests/m10_v2/test_family_kernel.py"
S = "tests/m10_v2/test_family_signals_calculation.py"
I = "tests/m10_v2/test_family_identity_and_reader.py"
C = "tests/m10_v2/test_family_config_rejection.py"
G = "tests/m10_v2/test_family_goldens.py"
U = "tests/m10_v2/test_family_surface.py"


def _row(item_id, item, passing, mutations, basis, due):
    return {"id": item_id, "item": item, "passing": passing, "mutations": mutations, "basis": basis, "due": due}


FAMILY_INDEX = (
    _row("F-01", "Per-member channels, centers, components, motor_to_throat, Type from the Gate set only, aura classes; union",
         (f"{K}::test_f01_member_and_union_mechanics",
          "tests/m10_v2/test_kernel_mechanics.py::test_derived_type_and_member_mechanics",
          "tests/m10_v2/test_kernel_mechanics.py::test_type_cases_cover_every_type_aura_class_and_predicate_value",
          "tests/m10_v2/test_kernel_mechanics.py::test_union_mechanics_when_only_the_union_defines_centers",
          "tests/m10_v2/test_kernel_mechanics.py::test_derived_type_ignores_a_contradicting_stored_vendor_type"),
         (f"{K}::test_f01_mutation_aura_class_is_refused", f"{K}::test_f01_mutation_motor_to_throat_route_is_refused"),
         "fixture bundle", "now"),
    _row("F-02", "The four center outcomes for every center, with owner; motor→Throat",
         (f"{K}::test_f02_every_outcome_on_every_center", f"{K}::test_f02_witnesses_cover_every_center",
          "tests/m10_v2/test_kernel_mechanics.py::test_center_and_motor_throat_outcomes",
          "tests/m10_v2/test_kernel_mechanics.py::test_outcome_cases_cover_each_outcome_and_owner"),
         (f"{K}::test_f02_mutation_shared_and_mutual_swapped_is_refused",),
         "fixture bundle", "now"),
    _row("F-03", "Twenty signals in per-mille under the three v2 operations; zero results; half-up boundaries",
         (f"{S}::test_f03_signals_in_per_mille",
          "tests/m10_v2/test_signals.py::test_zero_when_every_channel_state_is_none",
          "tests/m10_v2/test_signals.py::test_ordinary_signal_maximum_is_800_or_833_never_1000",
          "tests/m10_v2/test_signals.py::test_ordinary_signal_midpoint",
          "tests/m10_v2/test_signals.py::test_rhu_rounds_half_up_on_its_own_integer_arguments",
          "tests/m10_v2/test_signals.py::test_no_ordinary_signal_has_an_exact_half_real_input",
          "tests/m10_v2/test_signals.py::test_equilibrium_score",
          "tests/m10_v2/test_signals.py::test_counterweight_ratio"),
         (f"{S}::test_f03_mutation_half_down_rounding_is_refused", f"{S}::test_f03_mutation_companionship_not_mutual_is_refused"),
         "fixture bundle", "now"),
    _row("F-04", "C_k, Z_k and T_k for all ten categories, every pair rule, the clamp of T_k to 0..1000",
         (f"{S}::test_f04_components_and_pair_rules",
          "tests/m10_v2/test_calculation_components.py::test_channel_component_on_real_pairs",
          "tests/m10_v2/test_calculation_components.py::test_center_component_mapped",
          "tests/m10_v2/test_calculation_components.py::test_center_component_balance_counts_the_nine_centers_only",
          "tests/m10_v2/test_calculation_components.py::test_type_component_and_every_pair_rule",
          "tests/m10_v2/test_calculation_components.py::test_every_rule_is_shown_holding_and_not_holding",
          "tests/m10_v2/test_calculation_components.py::test_type_component_clamp_on_its_own_arguments",
          "tests/m10_v2/test_calculation_components.py::test_type_component_clamp_cannot_act_on_an_admitted_bundle"),
         (f"{S}::test_f04_mutation_unclamped_type_component_is_refused", f"{S}::test_f04_mutation_dropped_pair_rule_is_refused"),
         "fixture bundle", "now"),
    _row("F-05", "Score rule: C_k = 0 and Z_k = 0 scores 0; otherwise one ROUND_HALF_UP of 60/25/15, clamped 0..100",
         (f"{S}::test_f05_score_rule",
          "tests/m10_v2/test_calculation_components.py::test_zero_rule_and_score",
          "tests/m10_v2/test_calculation_components.py::test_score_clamp_on_its_own_arguments",
          "tests/m10_v2/test_calculation_components.py::test_score_clamp_cannot_act_on_an_admitted_bundle"),
         (f"{S}::test_f05_mutation_type_scoring_alone_is_refused", f"{S}::test_f05_mutation_rounding_down_is_refused"),
         "fixture bundle", "now"),
    _row("F-06", "Band assignment from each category's own inclusive maxima at every edge",
         (f"{S}::test_f06_band_at_every_edge_against_the_cut_maxima",
         f"{S}::test_f06_band_at_every_edge_of_every_category",
          "tests/m10_v2/test_calculation_bands.py::test_band_at_every_edge_of_each_category",
          "tests/m10_v2/test_calculation_bands.py::test_real_pairs_land_in_their_own_categorys_bands",
          "tests/m10_v2/test_calculation_bands.py::test_test_maxima_differ_by_category"),
         (f"{S}::test_f06_mutation_exclusive_maxima_at_the_cut_is_refused", f"{S}::test_f06_mutation_exclusive_maxima_is_refused"),
         "active release", "WU-PR-13"),
    _row("F-07", "Integer-only arithmetic; no viewer preferences, presets or caller weights",
         (f"{S}::test_f07_integer_only_and_exactly_four_inputs",
          "tests/m10_v2/test_kernel_static_guards.py::test_no_binary_floating_point_in_the_package",
          "tests/m10_v2/test_calculation_result.py::test_calculation_reads_no_file_and_takes_exactly_four_inputs"),
         (f"{S}::test_f07_mutation_a_float_operation_is_flagged", f"{S}::test_f07_mutation_a_caller_weight_input_is_refused"),
         "static", "now"),
    _row("F-08", "pair_key under the v2 config_id, the magic10:v2: cache key, the v2 release, result and compat schema closure, q 0..1000",
         (f"{I}::test_f08_identity_cache_key_and_schema_closure_on_the_admitted_release",
          f"{I}::test_f08_identity_cache_key_and_schema_closure",
          "tests/m10_v2/test_calculation_result.py::test_pair_key_is_the_v2_identity",
          "tests/m10_v2/test_calculation_result.py::test_result_validates_and_follows_the_governed_order",
          "tests/m10_v2/test_compat_result.py::test_cache_key_is_the_loader_key_and_differs_from_v1",
          "tests/m10_v2/test_compat_result.py::test_schema_accepts_q_at_both_ends",
          "tests/m10_v2/test_compat_result.py::test_schema_refuses_q_outside_its_integer_domain"),
         (f"{I}::test_f08_mutation_pair_key_without_the_release_is_refused",
          f"{I}::test_f08_mutation_v1_cache_key_prefix_on_the_admitted_release_is_refused",
          f"{I}::test_f08_mutation_pair_key_without_config_id_is_refused", f"{I}::test_f08_mutation_cache_key_prefix_is_refused"),
         "active release", "WU-PR-13"),
    _row("F-09", "Configuration-mutation rejection under the v2 loader rules",
         (f"{C}::test_f09_configuration_mutation_rejection",),
         (f"{C}::test_f09_mutation_owning_schema_not_applied_is_refused",),
         "temporary root", "now"),
    _row("F-10", "The v2 goldens M10-G001 to M10-G008 in both pair orders at the cut maxima; M10-G001 is 0 in every category, Cool",
         (f"{G}::test_goldens_document_holds_m10_g001_to_m10_g008", f"{G}::test_m10_g001_in_both_pair_orders",
          f"{G}::test_m10_g002_and_m10_g004_in_both_pair_orders", f"{G}::test_m10_g003_owner_split_with_the_owners_swapped",
          f"{G}::test_m10_g006_band_boundaries_at_each_categorys_cut_maxima",
          f"{G}::test_every_golden_matches_the_cut_release_in_both_pair_orders",
          "tests/config/test_config_artifacts.py::test_compare_goldens_admits_the_real_root"),
         (f"{G}::test_m10_g001_mutation_changed_band_is_refused", f"{G}::test_m10_g001_mutation_channel_completing_pair_is_refused",
          f"{G}::test_m10_g004_mutation_changed_score_is_refused", f"{G}::test_m10_g006_mutation_fixture_maxima_are_refused",
          f"{G}::test_mutation_order_dependent_core_is_refused_as_pair_order"),
         "active release", "WU-PR-10"),
    _row("F-11", "The complete five-state truth table over Channel endpoint-ownership patterns",
         (f"{K}::test_f11_f12_five_states_over_all_36_channels",
          "tests/m10_v2/test_kernel_channel_states.py::test_exhaustive_channel_state_table"),
         (f"{K}::test_f11_f12_mutation_compromise_reported_as_dominance_is_refused",),
         "fixture bundle", "now"),
    _row("F-12", "All 36 Channels in every reachable state",
         (f"{K}::test_f11_f12_five_states_over_all_36_channels",
          "tests/m10_v2/test_kernel_channel_states.py::test_channel_roster_matches_the_bundle"),
         (f"{K}::test_f11_f12_mutation_compromise_reported_as_dominance_is_refused",),
         "fixture bundle", "now"),
    _row("F-13", "Every default Channel-to-signal row",
         (f"{S}::test_f13_every_default_channel_to_signal_row",
          "tests/m10_v2/test_signals.py::test_register_ids_pairs_maps_and_operations_are_unchanged"),
         (f"{S}::test_f13_mutation_dropped_row_is_refused", f"{S}::test_f13_mutation_moved_channel_is_refused"),
         "fixture bundle", "now"),
    _row("F-14", "Gate normalization: the canonical domain accepted; missing, empty, duplicate, malformed or out-of-range refused",
         (f"{K}::test_f14_gate_normalization_and_mask_domain",
          "tests/m10_v2/test_kernel_refusals.py::test_mask_outside_the_domain_is_refused",
          "tests/m10_v2/test_kernel_mechanics.py::test_domain_boundary_masks_are_accepted"),
         (f"{K}::test_f14_mutation_zero_mask_accepted_is_refused",),
         "fixture bundle", "now"),
    _row("F-15", "Complete-matrix atomicity",
         (f"{S}::test_f15_complete_matrix_or_refusal",),
         (f"{S}::test_f15_mutation_partial_matrix_is_refused",),
         "fixture bundle", "now"),
    _row("F-16", "AB/BA identity",
         (f"{S}::test_f16_ab_ba_identity",
          "tests/m10_v2/test_calculation_result.py::test_result_is_symmetric_deterministic_and_immutable",
          "tests/m10_v2/test_compat_result.py::test_bytes_are_canonical_symmetric_and_repeatable"),
         (f"{S}::test_f16_mutation_order_dependent_kernel_is_refused",),
         "fixture bundle", "now"),
    _row("F-17", "Two-run identity",
         (f"{S}::test_f17_two_run_identity",
          "tests/m10_v2/test_calculation_result.py::test_result_is_symmetric_deterministic_and_immutable"),
         (f"{S}::test_f17_mutation_run_dependent_kernel_is_refused",),
         "fixture bundle", "now"),
    _row("F-18", "Absence of UID hashing and Type-only fallback",
         ("tests/m10_v2/test_no_legacy_scorers.py::test_no_uid_hash_scorer_in_production",
          "tests/m10_v2/test_no_legacy_scorers.py::test_no_production_module_imports_a_removed_module",
          "tests/m10_v2/test_no_legacy_scorers.py::test_the_removed_files_are_absent"),
         ("tests/m10_v2/test_no_legacy_scorers.py::test_each_guard_fails_on_a_constructed_positive_and_passes_a_clean_root",),
         "static", "WU-PR-09"),
    _row("F-19", "Production no-import and no-symbol-use proof for the historical numeric-Gate compromise helper",
         ("tests/m10_v2/test_no_legacy_scorers.py::test_no_numeric_gate_compromise_helper_in_production",),
         ("tests/m10_v2/test_no_legacy_scorers.py::test_each_guard_fails_on_a_constructed_positive_and_passes_a_clean_root",),
         "static", "now"),
    _row("F-20", "Corrected reader.v1 schema closure; numeric-free public Reader proof",
         (f"{I}::test_f20_reader_projection_is_numeric_free",
          "tests/m10_v2/test_compat_reader_projection.py::test_projection_matches_its_schema_and_is_numeric_free",
          "tests/m10_v2/test_compat_reader_projection.py::test_projection_depends_on_bands_alone"),
         (f"{I}::test_f20_mutation_a_numeric_field_is_refused",),
         "fixture bundle", "now"),
    _row("F-21", "Manifest and release-binding rejection, manifest-row part (v2 loader)",
         (f"{C}::test_f21_manifest_row_rejection",),
         (f"{C}::test_f21_mutation_unchecked_manifest_rows_is_refused",),
         "temporary root", "now"),
    _row("F-21b", "Manifest and release-binding rejection, release-binding part (admission)",
         (f"{U}::test_f21b_release_binding_rejection",),
         (f"{U}::test_f21b_mutation_unbound_member_admitted_is_refused",),
         "active release", "WU-PR-10"),
    _row("F-22", "Valid identical self-pair short-circuit: no core, narrative, cache or pair_key",
         (f"{U}::test_f22_self_pair_short_circuit",),
         (f"{U}::test_f22_mutation_self_pair_evaluated_is_refused",),
         "active release", "WU-PR-09"),
    _row("F-23", "Same canonical identity with unequal normalized projections rejected as ERR_READER_INVALID_CHART",
         (f"{U}::test_f23_same_identity_unequal_projection_is_refused",),
         (f"{U}::test_f23_mutation_inconsistent_self_treated_as_self_is_refused",),
         "active release", "WU-PR-09"),
    _row("F-24", "Distinct-person equal-mask intrinsic identity: equal fingerprints and one identity-free pair_key",
         (f"{U}::test_f24_equal_masks_of_distinct_people_share_one_identity_free_pair_key",
          f"{I}::test_f24_equal_masks_give_one_identity_free_v2_pair_key"),
         (f"{U}::test_f24_mutation_identity_in_the_pair_preimage_is_refused",
          f"{I}::test_f24_mutation_identity_in_the_v2_preimage_is_refused"),
         "active release and fixture bundle", "WU-PR-09"),
    _row("F-25", "Equal-mask personal-key orientation by ASCII canonical UUID tie-break, with AB/BA byte identity",
         (f"{U}::test_f25_equal_mask_orientation_by_uuid_tie_break",),
         (f"{U}::test_f25_mutation_request_order_kept_on_a_tie_is_refused",),
         "active release", "WU-PR-09"),
    _row("F-26", "Independent public Reader idempotence; a self-pair and an equal-mask pair never share bytes or idempotence_hash",
         (f"{U}::test_f26_self_pair_and_equal_mask_pair_never_share_public_bytes",),
         (f"{U}::test_f26_mutation_eligibility_outside_the_preimage_is_refused",),
         "active release", "WU-PR-09"),
    _row("F-27", "CLI, internal HTTP, compat and Reader-projection parity",
         (f"{U}::test_f27_cli_internal_http_compat_and_reader_parity",),
         (f"{U}::test_f27_mutation_one_surface_diverges_is_refused",),
         "active release", "WU-PR-09"),
    _row("F-28", "Exact PF05 error token and HTTP mapping for every fail-closed condition",
         (f"{U}::test_f28_token_and_status_mapping_agree", f"{U}::test_f28_surfaces_emit_the_mapped_token_and_status"),
         (f"{U}::test_f28_mutation_reader_status_out_of_mapping_is_refused", f"{U}::test_f28_mutation_http_status_out_of_mapping_is_refused"),
         "active release", "WU-PR-09"),
)

ITEM_IDS = tuple(f"F-{number:02d}" for number in range(1, 29)) + ("F-21b",)
BASES = {"fixture bundle", "temporary root", "test maxima", "active release", "static", "active release and fixture bundle"}
DUE = {"now", "WU-PR-09", "WU-PR-10", "WU-PR-13"}


def _top_level_tests(path: str) -> set[str]:
    tree = ast.parse((ROOT / path).read_text(encoding="utf-8"), filename=path)
    return {node.name for node in tree.body if isinstance(node, ast.FunctionDef) and node.name.startswith("test_")}


def _check_index(index) -> None:
    assert sorted(row["id"] for row in index) == sorted(ITEM_IDS)
    for row in index:
        assert row["passing"] and row["mutations"], row["id"]
        assert row["basis"] in BASES and row["due"] in DUE, row["id"]
        for node in (*row["passing"], *row["mutations"]):
            path, _, function = node.partition("::")
            assert path.startswith("tests/") and (ROOT / path).is_file(), node
            assert function in _top_level_tests(path), node
        assert all(node.startswith(FAMILY) for node in row["mutations"]), row["id"]


def test_every_item_has_a_passing_case_and_a_refused_mutation() -> None:
    _check_index(FAMILY_INDEX)


def test_the_index_pin_refuses_an_item_without_a_mutation() -> None:
    broken = tuple({**row, "mutations": ()} if row["id"] == "F-15" else row for row in FAMILY_INDEX)
    with pytest.raises(AssertionError):
        _check_index(broken)


def test_the_index_pin_refuses_a_node_that_does_not_resolve() -> None:
    broken = tuple(
        {**row, "passing": (*row["passing"], f"{K}::test_missing_case")} if row["id"] == "F-01" else row
        for row in FAMILY_INDEX
    )
    with pytest.raises(AssertionError):
        _check_index(broken)


# --- HDE-EPIC043 WU-PR-13: no mutation case passes on an unrelated crash ------------------------

BROAD_HANDLER_NAMES = {"Exception", "BaseException"}


def broad_handlers(source: str) -> list[int]:
    """The lines of handlers that would turn an arbitrary exception into a refused mutation."""
    lines = []
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.ExceptHandler):
            types = node.type.elts if isinstance(node.type, ast.Tuple) else [node.type]
            if node.type is None or any(isinstance(item, ast.Name) and item.id in BROAD_HANDLER_NAMES for item in types):
                lines.append(node.lineno)
    return lines


def mutation_modules(index) -> tuple[str, ...]:
    return tuple(sorted({node.partition("::")[0] for row in index for node in row["mutations"]}))


def test_no_mutation_module_converts_an_arbitrary_exception() -> None:
    paths = mutation_modules(FAMILY_INDEX)
    assert paths
    assert {path: broad_handlers((ROOT / path).read_text(encoding="utf-8")) for path in paths} == {path: [] for path in paths}


def test_the_handler_pin_refuses_a_broad_handler() -> None:
    assert broad_handlers("try:\n    pass\nexcept Exception as exc:\n    pass\n") == [3]
    assert broad_handlers("try:\n    pass\nexcept (KeyError, BaseException):\n    pass\n") == [3]
    assert broad_handlers("try:\n    pass\nexcept:\n    pass\n") == [3]
    assert broad_handlers("try:\n    pass\nexcept KeyError:\n    pass\n") == []
