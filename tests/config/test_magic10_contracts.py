"""Complete synthetic interface proofs; no kernel, classifier or release admission."""
import copy
import hashlib
import json
from pathlib import Path

import pytest

from engine.config.registry_loader import SchemaValidationError, _capture_mechanics_config, _validate_mechanics_domain, _validate_initial_mechanics, _validate_local_schema, _validate_result_fixture, _validate_result_augmentation, _validate_thresholds
from tests.config.helpers import catalog_root, write_canonical

# Independently transcribed from the approved complete Instruction §6 table.
EXPECTED_SIGNALS = [('harmony', 'rapport_delta', 'coherence_bp_v1', ['19-49', '26-44', '27-50', '37-40']),
 ('harmony', 'resonance_strength', 'coherence_bp_v1', ['05-15', '06-59', '12-22', '13-33']),
 ('heat', 'spark_intensity', 'activation_bp_v1', ['06-59', '25-51', '30-41', '39-55']),
 ('heat', 'momentum_flux', 'activation_bp_v1', ['03-60', '20-34', '29-46', '35-36']),
 ('communication',
  'signal_clarity',
  'expression_bp_v1',
  ['04-63', '17-62', '23-43', '24-61', '47-64']),
 ('communication',
  'exchange_density',
  'expression_bp_v1',
  ['11-56', '12-22', '13-33', '20-57', '26-44']),
 ('alignment', 'vector_cohesion', 'coherence_bp_v1', ['02-14', '07-31', '10-20', '10-34']),
 ('alignment', 'axis_agreement', 'coherence_bp_v1', ['19-49', '27-50', '28-38', '32-54']),
 ('comfort', 'soothe_index', 'coherence_bp_v1', ['06-59', '12-22', '19-49', '37-40']),
 ('comfort', 'buffer_resilience', 'coherence_bp_v1', ['05-15', '10-57', '27-50', '34-57']),
 ('consistency',
  'pattern_integrity',
  'coherence_bp_v1',
  ['05-15', '09-52', '16-48', '17-62', '18-58']),
 ('consistency', 'variance_stability', 'coherence_bp_v1', ['03-60', '29-46', '32-54', '42-53']),
 ('expansion', 'growth_tendency', 'activation_bp_v1', ['03-60', '18-58', '32-54', '42-53']),
 ('expansion', 'horizon_reach', 'activation_bp_v1', ['11-56', '28-38', '29-46', '35-36']),
 ('creativity', 'novelty_factor', 'activation_bp_v1', ['01-08', '03-60', '23-43', '25-51']),
 ('creativity',
  'expression_flow',
  'expression_bp_v1',
  ['10-20', '11-56', '12-22', '16-48', '35-36']),
 ('drive', 'willpower_current', 'activation_bp_v1', ['02-14', '21-45', '25-51', '26-44', '32-54']),
 ('drive', 'focus_pressure', 'activation_bp_v1', ['09-52', '18-58', '20-34', '28-38', '42-53']),
 ('balance',
  'equilibrium_score',
  'twice_min_owner_mass_v1',
  ['02-14', '07-31', '21-45', '26-44', '32-54', '37-40']),
 ('balance',
  'counterweight_ratio',
  'companionship_em_mass_v1',
  ['05-15', '06-59', '10-20', '13-33', '27-50', '39-55'])]
EXPECTED_PROFILES = [
    {"profile_id": "activation_bp_v1", "responses": {"none": 0, "companionship": 5000, "dominance": 7500, "compromise": 2500, "electromagnetic": 10000}},
    {"profile_id": "coherence_bp_v1", "responses": {"none": 0, "companionship": 10000, "dominance": 5000, "compromise": 2500, "electromagnetic": 7500}},
    {"profile_id": "expression_bp_v1", "responses": {"none": 0, "companionship": 7500, "dominance": 5000, "compromise": 2500, "electromagnetic": 10000}},
]
EXPECTED_CATEGORIES = ['harmony', 'heat', 'communication', 'alignment', 'comfort', 'consistency', 'expansion', 'creativity', 'drive', 'balance']


@pytest.fixture
def candidate(tmp_path: Path):
    return _capture_mechanics_config(catalog_root(tmp_path))


def complete_results():
    pure = {'schema': 'magic10_result.v1', 'config_id': 'm10-channel-state-v1.0.0',
            'release_id': 'a'*64, 'pair_key': 'b'*64,
            'signals': [{'signal_id': row[1], 'q': 0 if i % 2 == 0 else 200} for i, row in enumerate(EXPECTED_SIGNALS)],
            'categories': [{'category_id': category, 'score': 0 if i % 2 == 0 else 100, 'band': 'Cool' if i % 2 == 0 else 'Glow'} for i, category in enumerate(EXPECTED_CATEGORIES)]}
    internal = copy.deepcopy(pure)
    internal['schema'] = 'magic10_compat_result.v1'
    for row in internal['categories']:
        row.update(shared_key='shared.'+row['category_id'], personal_lo_to_hi_key='lo.'+row['category_id'], personal_hi_to_lo_key='hi.'+row['category_id'])
    return pure, internal


def test_complete_initial_configuration_has_all_exact_sources_and_defaults(candidate) -> None:
    data = candidate.config
    assert set(data) == {'category_weights', 'config_id', 'profiles', 'response_scale', 'result_schema', 'rounding', 'schema', 'signal_scale', 'signals', 'sources'}
    assert data['profiles'] == EXPECTED_PROFILES
    expected_signals = []
    for _, signal_id, operation, ids in EXPECTED_SIGNALS:
        row = {'signal_id': signal_id, 'channels': [{'channel_id': name, 'weight': 1} for name in ids]}
        if operation.endswith('_bp_v1'):
            row.update(operation='weighted_state_sum_v1', profile_id=operation)
        else:
            row['operation'] = operation
        expected_signals.append(row)
    assert data['signals'] == expected_signals
    assert sum(len(row['channels']) for row in data['signals']) == 90
    assert data['category_weights'] == [{'category_id': name, 'reducer': 'weighted_mean_half_unit_v1', 'weights': [1, 1]} for name in EXPECTED_CATEGORIES]
    expected_paths = {'caps': 'catalog/magic10_caps.json', 'categories': 'catalog/magic10.json', 'channels': 'catalog/channels_v1.json', 'thresholds': 'math/thresholds.json'}
    for key, path in expected_paths.items():
        assert data['sources'][key] == {'path': path, 'sha256': hashlib.sha256((candidate.root/path).read_bytes()).hexdigest()}
    assert not hasattr(candidate, 'release_id')
    assert not hasattr(candidate, 'admitted')


def _numeric_paths(data):
    yield ('response_scale',)
    yield ('signal_scale',)
    for i, profile in enumerate(data['profiles']):
        for state in profile['responses']:
            yield ('profiles', i, 'responses', state)
    for i, signal in enumerate(data['signals']):
        for j, _ in enumerate(signal['channels']):
            yield ('signals', i, 'channels', j, 'weight')
    for i in range(len(data['category_weights'])):
        for j in (0, 1):
            yield ('category_weights', i, 'weights', j)


def _set_path(data, path, value):
    target = data
    for key in path[:-1]:
        target = target[key]
    target[path[-1]] = value


@pytest.mark.parametrize('wrong_type', [True, False, 1.0, '1'])
def test_every_config_numeric_position_rejects_coercible_types(candidate, wrong_type) -> None:
    paths = list(_numeric_paths(candidate.config))
    assert len(paths) == 127
    for path in paths:
        altered = copy.deepcopy(candidate.config)
        original = altered
        for key in path:
            original = original[key]
        replacement = float(original) if type(wrong_type) is float else str(original) if type(wrong_type) is str else wrong_type
        _set_path(altered, path, replacement)
        with pytest.raises(SchemaValidationError) as error:
            _validate_mechanics_domain(candidate, altered, candidate.registry)
        assert error.value.code == 'SCHEMA_VALIDATION_FAILED', path


@pytest.mark.parametrize('weight', [1, 3])
def test_legal_weight_domain_does_not_authorize_tuning_initial_defaults(candidate, weight: int) -> None:
    data = copy.deepcopy(candidate.config)
    data['signals'][0]['channels'][0]['weight'] = weight
    data['category_weights'][0]['weights'][0] = weight
    _validate_mechanics_domain(candidate, data, candidate.registry)
    if weight == 1:
        _validate_initial_mechanics(candidate, data, candidate.registry)
    else:
        with pytest.raises(SchemaValidationError) as error:
            _validate_initial_mechanics(candidate, data, candidate.registry)
        assert error.value.code == 'INITIAL_SIGNAL_MAP_MISMATCH'


@pytest.mark.parametrize('weight', [0, 4, -1])
def test_channel_and_category_weight_bounds_refuse(candidate, weight: int) -> None:
    for path in [('signals', 0, 'channels', 0, 'weight'), ('category_weights', 0, 'weights', 0)]:
        data = copy.deepcopy(candidate.config)
        _set_path(data, path, weight)
        with pytest.raises(SchemaValidationError):
            _validate_mechanics_domain(candidate, data, candidate.registry)


def test_response_zero_is_valid_for_none_and_inequalities_are_independent(candidate) -> None:
    assert all(row['responses']['none'] == 0 for row in candidate.config['profiles'])
    for i in range(3):
        data = copy.deepcopy(candidate.config)
        data['profiles'][i]['responses']['none'] = 1
        with pytest.raises(SchemaValidationError):
            _validate_mechanics_domain(candidate, data, candidate.registry)
    data = copy.deepcopy(candidate.config)
    data['profiles'][0]['responses']['dominance'] = 5000
    with pytest.raises(SchemaValidationError) as error:
        _validate_mechanics_domain(candidate, data, candidate.registry)
    assert error.value.code == 'PROFILE_INEQUALITY_MISMATCH'
    data['profiles'][0]['responses']['dominance'] = 7000
    _validate_mechanics_domain(candidate, data, candidate.registry)
    with pytest.raises(SchemaValidationError) as error:
        _validate_initial_mechanics(candidate, data, candidate.registry)
    assert error.value.code == 'INITIAL_PROFILE_MISMATCH'


@pytest.mark.parametrize('value', [0, 10000])
def test_response_domain_schema_boundaries_are_distinct_from_relations(candidate, value: int) -> None:
    data = copy.deepcopy(candidate.config)
    data['profiles'][0]['responses']['dominance'] = value
    _validate_local_schema(candidate, 'schemas/magic10_mechanics_v1.schema.json', data)
    with pytest.raises(SchemaValidationError):
        _validate_initial_mechanics(candidate, data, candidate.registry)


@pytest.mark.parametrize('mutation,expected', [
    ('signal-order', 'SIGNAL_ORDER_MISMATCH'), ('category-order', 'CATEGORY_ORDER_MISMATCH'),
    ('profile-order', 'PROFILE_ROSTER_MISMATCH'), ('duplicate-member', 'SIGNAL_MEMBERSHIP_INVALID'),
    ('overlap', 'SIGNAL_CATEGORY_OVERLAP'), ('source-hash', 'MECHANICS_SOURCE_MISMATCH'),
    ('operation', 'SCHEMA_VALIDATION_FAILED'), ('balance-profile', 'SCHEMA_VALIDATION_FAILED'),
    ('config-id', 'INITIAL_CONFIG_ID_MISMATCH'),
])
def test_complete_relational_constraints(candidate, mutation: str, expected: str) -> None:
    data = copy.deepcopy(candidate.config)
    if mutation == 'signal-order':
        data['signals'][0], data['signals'][1] = data['signals'][1], data['signals'][0]
    elif mutation == 'category-order':
        data['category_weights'][0], data['category_weights'][1] = data['category_weights'][1], data['category_weights'][0]
    elif mutation == 'profile-order':
        data['profiles'][0], data['profiles'][1] = data['profiles'][1], data['profiles'][0]
    elif mutation == 'duplicate-member':
        data['signals'][0]['channels'][1] = dict(data['signals'][0]['channels'][0], weight=3)
    elif mutation == 'overlap':
        data['signals'][1]['channels'][0]['channel_id'] = '19-49'
        data['signals'][1]['channels'].sort(key=lambda row: row['channel_id'])
    elif mutation == 'source-hash':
        data['sources']['channels']['sha256'] = '0'*64
    elif mutation == 'operation':
        data['signals'][0]['operation'] = 'other'
    elif mutation == 'balance-profile':
        data['signals'][-1]['profile_id'] = 'activation_bp_v1'
    elif mutation == 'config-id':
        data['config_id'] = 'other'
    with pytest.raises(SchemaValidationError) as error:
        _validate_initial_mechanics(candidate, data, candidate.registry)
    assert error.value.code == expected


@pytest.mark.parametrize('location', ['top', 'rounding', 'sources', 'source', 'profile', 'responses', 'signal', 'member', 'category'])
def test_every_governed_config_object_is_closed(candidate, location: str) -> None:
    data = copy.deepcopy(candidate.config)
    locations = {'top': data, 'rounding': data['rounding'], 'sources': data['sources'], 'source': data['sources']['caps'],
                 'profile': data['profiles'][0], 'responses': data['profiles'][0]['responses'], 'signal': data['signals'][0],
                 'member': data['signals'][0]['channels'][0], 'category': data['category_weights'][0]}
    locations[location]['extra'] = 'forbidden'
    with pytest.raises(SchemaValidationError) as error:
        _validate_initial_mechanics(candidate, data, candidate.registry)
    assert error.value.code == 'SCHEMA_VALIDATION_FAILED'


@pytest.mark.parametrize('slot', ['clamp', 'edges'])
@pytest.mark.parametrize('value', [True, 1.0, '1'])
def test_threshold_numeric_fields_do_not_coerce(slot: str, value: object) -> None:
    for position in range(2 if slot == 'clamp' else 4):
        data = {'clamp': [0, 100], 'edges': [24, 49, 74, 100], 'rounding': 'ROUND_HALF_UP', 'version': '1'}
        data[slot][position] = value
        with pytest.raises(SchemaValidationError):
            _validate_thresholds(data)


@pytest.mark.parametrize('edges', [[24, 24, 74, 100], [24, 49, 74, 99], [-1, 49, 74, 100], [24, 49, 74], [24, 49, 74, 100, 100]])
def test_threshold_order_bounds_and_cardinality_are_closed(edges: list) -> None:
    with pytest.raises(SchemaValidationError):
        _validate_thresholds({'clamp': [0, 100], 'edges': edges, 'rounding': 'ROUND_HALF_UP', 'version': '1'})


def test_complete_pure_and_internal_fixtures_and_relation(candidate) -> None:
    pure, internal = complete_results()
    _validate_result_fixture(candidate, pure)
    _validate_result_fixture(candidate, internal)
    _validate_result_augmentation(candidate, pure, internal)


@pytest.mark.parametrize('schema', [{}, [], None, True, 1, 'unknown'])
def test_result_schema_identity_refuses_wrong_types_with_typed_error(candidate, schema) -> None:
    pure, _ = complete_results()
    pure['schema'] = schema
    with pytest.raises(SchemaValidationError) as exc_info:
        _validate_result_fixture(candidate, pure)
    assert exc_info.value.code == 'RESULT_SCHEMA_IDENTITY_MISMATCH'


@pytest.mark.parametrize('value', [True, False, 1.0, '1', -1, 201])
def test_all_signal_result_numeric_slots_are_strict(candidate, value: object) -> None:
    for i in range(20):
        pure, _ = complete_results()
        pure['signals'][i]['q'] = value
        with pytest.raises(SchemaValidationError):
            _validate_result_fixture(candidate, pure)


@pytest.mark.parametrize('value', [True, False, 1.0, '1', -1, 101])
def test_all_category_result_numeric_slots_are_strict(candidate, value: object) -> None:
    for i in range(10):
        pure, _ = complete_results()
        pure['categories'][i]['score'] = value
        with pytest.raises(SchemaValidationError):
            _validate_result_fixture(candidate, pure)


@pytest.mark.parametrize('key,value', [('release_id', 'A'*64), ('pair_key', 'a'*63), ('pair_key', 'a'*64+'\n'), ('config_id', ''), ('config_id', 'other')])
def test_result_identity_fields_are_exact(candidate, key: str, value: str) -> None:
    pure, _ = complete_results()
    pure[key] = value
    with pytest.raises(SchemaValidationError):
        _validate_result_fixture(candidate, pure)


@pytest.mark.parametrize('mutation', ['signals', 'categories', 'q', 'score', 'band', 'release_id', 'pair_key'])
def test_augmentation_cannot_change_pure_values_order_or_identity(candidate, mutation: str) -> None:
    pure, internal = complete_results()
    if mutation in {'signals', 'categories'}:
        internal[mutation][0], internal[mutation][1] = internal[mutation][1], internal[mutation][0]
    elif mutation == 'q':
        internal['signals'][0]['q'] = 1
    elif mutation == 'score':
        internal['categories'][0]['score'] = 1
    elif mutation == 'band':
        internal['categories'][0]['band'] = 'Warm'
    else:
        internal[mutation] = 'c'*64
    with pytest.raises(SchemaValidationError):
        _validate_result_augmentation(candidate, pure, internal)


@pytest.mark.parametrize('key', ['shared_key', 'personal_lo_to_hi_key', 'personal_hi_to_lo_key'])
def test_internal_keys_are_required_nonempty_and_forbidden_in_pure(candidate, key: str) -> None:
    pure, internal = complete_results()
    internal['categories'][0][key] = ''
    with pytest.raises(SchemaValidationError):
        _validate_result_fixture(candidate, internal)
    del internal['categories'][0][key]
    with pytest.raises(SchemaValidationError):
        _validate_result_fixture(candidate, internal)
    pure['categories'][0][key] = 'forbidden'
    with pytest.raises(SchemaValidationError):
        _validate_result_fixture(candidate, pure)


@pytest.mark.parametrize('location', ['top', 'signal', 'category'])
def test_result_objects_reject_public_or_request_metadata(candidate, location: str) -> None:
    pure, internal = complete_results()
    for data in (pure, internal):
        target = data if location == 'top' else data['signals' if location == 'signal' else 'categories'][0]
        target['viewer_id'] = 'forbidden'
        with pytest.raises(SchemaValidationError):
            _validate_result_fixture(candidate, data)


def test_missing_mechanics_source_cannot_use_a_generated_snapshot(tmp_path: Path) -> None:
    root = catalog_root(tmp_path)
    (root/'catalog/magic10_mechanics_v1.json').unlink()
    path = root/'artifacts/thresholds/magic10_config.json'
    write_canonical(path, {'schema': 'magic10_config.v1'})
    with pytest.raises(SchemaValidationError) as error:
        _capture_mechanics_config(root)
    assert error.value.code == 'MISSING_FILE'


@pytest.mark.parametrize('location,key', [
    ('rounding', 'signal'), ('sources', 'caps'), ('source', 'path'),
    ('profile', 'profile_id'), ('responses', 'none'), ('signal', 'operation'),
    ('member', 'weight'), ('category-weight', 'weights'),
])
def test_mechanics_nested_duplicate_keys_refuse_before_parsing_loss(candidate, location: str, key: str) -> None:
    """Every nested config object rejects keys an ordinary parser would discard."""
    data = candidate.config
    containers = {
        'rounding': data['rounding'], 'sources': data['sources'], 'source': data['sources']['caps'],
        'profile': data['profiles'][0], 'responses': data['profiles'][0]['responses'],
        'signal': data['signals'][0], 'member': data['signals'][0]['channels'][0],
        'category-weight': data['category_weights'][0],
    }
    container = containers[location]
    fragment = json.dumps(container, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode('utf-8')
    duplicate = json.dumps(key).encode('utf-8') + b':' + json.dumps(container[key], sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode('utf-8') + b','
    path = candidate.root / 'catalog/magic10_mechanics_v1.json'
    before = path.read_bytes()
    assert fragment in before
    changed = before.replace(fragment, b'{' + duplicate + fragment[1:], 1)
    assert len(changed) == len(before) + len(duplicate)
    assert json.loads(changed) == data  # A plain JSON parse would hide this defect.
    path.write_bytes(changed)
    with pytest.raises(SchemaValidationError) as error:
        _capture_mechanics_config(candidate.root)
    assert error.value.code == 'DUPLICATE_JSON_KEY'
    assert path.read_bytes() == changed


@pytest.mark.parametrize('internal', [False, True])
@pytest.mark.parametrize('collection', ['signals', 'categories'])
@pytest.mark.parametrize('mutation,validator', [
    ('missing', 'minItems'), ('extra', 'maxItems'), ('duplicate-row', 'uniqueItems'),
])
def test_pure_and_internal_result_collection_cardinality_and_duplicates(candidate, internal: bool, collection: str, mutation: str, validator: str) -> None:
    pure, augmented = complete_results()
    data = augmented if internal else pure
    _validate_result_fixture(candidate, data)
    rows = data[collection]
    if mutation == 'missing':
        rows.pop()
    elif mutation == 'extra':
        rows.append(copy.deepcopy(rows[0]))
    else:
        rows[-1] = copy.deepcopy(rows[0])
    with pytest.raises(SchemaValidationError) as error:
        _validate_result_fixture(candidate, data)
    assert error.value.code == 'SCHEMA_VALIDATION_FAILED'
    assert error.value.__cause__.validator == validator
    assert list(error.value.__cause__.path) == [collection]


@pytest.mark.parametrize('internal', [False, True])
@pytest.mark.parametrize('collection,id_key,code', [
    ('signals', 'signal_id', 'RESULT_SIGNAL_ORDER_MISMATCH'),
    ('categories', 'category_id', 'RESULT_CATEGORY_ORDER_MISMATCH'),
])
def test_result_duplicate_id_cannot_hide_behind_distinct_row_values(candidate, internal: bool, collection: str, id_key: str, code: str) -> None:
    pure, augmented = complete_results()
    data = augmented if internal else pure
    _validate_result_fixture(candidate, data)
    rows = data[collection]
    rows[-1][id_key] = rows[0][id_key]
    assert rows[-1] != rows[0]
    schema_path = 'schemas/magic10_compat_result_v1.schema.json' if internal else 'schemas/magic10_result_v1.schema.json'
    _validate_local_schema(candidate, schema_path, data)
    with pytest.raises(SchemaValidationError) as error:
        _validate_result_fixture(candidate, data)
    assert error.value.code == code
