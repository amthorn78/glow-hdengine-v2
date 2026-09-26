"""Independent literals transcribed from approved C040-06 / PR01 Instruction §§4–5."""
import json
import hashlib
from pathlib import Path

import pytest

from engine.config.registry_loader import RegistryConfigError, SchemaValidationError, _capture_registry_config, load_registry_config, validate_channel_gates
from tests.config.helpers import catalog_root, write_canonical

EXPECTED_CHANNELS = {'01-08': ([1, 8], ['g', 'throat'], 'individual', 'knowing'),
 '02-14': ([2, 14], ['g', 'sacral'], 'individual', 'knowing'),
 '03-60': ([3, 60], ['root', 'sacral'], 'individual', 'knowing'),
 '04-63': ([4, 63], ['ajna', 'head'], 'collective', 'logic'),
 '05-15': ([5, 15], ['g', 'sacral'], 'collective', 'logic'),
 '06-59': ([6, 59], ['sacral', 'solar_plexus'], 'tribal', 'defense'),
 '07-31': ([7, 31], ['g', 'throat'], 'collective', 'logic'),
 '09-52': ([9, 52], ['root', 'sacral'], 'collective', 'logic'),
 '10-20': ([10, 20], ['g', 'throat'], 'individual', 'integration'),
 '10-34': ([10, 34], ['g', 'sacral'], 'individual', 'centering'),
 '10-57': ([10, 57], ['g', 'spleen'], 'individual', 'integration'),
 '11-56': ([11, 56], ['ajna', 'throat'], 'collective', 'sensing'),
 '12-22': ([12, 22], ['solar_plexus', 'throat'], 'individual', 'knowing'),
 '13-33': ([13, 33], ['g', 'throat'], 'collective', 'sensing'),
 '16-48': ([16, 48], ['spleen', 'throat'], 'collective', 'logic'),
 '17-62': ([17, 62], ['ajna', 'throat'], 'collective', 'logic'),
 '18-58': ([18, 58], ['root', 'spleen'], 'collective', 'logic'),
 '19-49': ([19, 49], ['root', 'solar_plexus'], 'tribal', 'ego'),
 '20-34': ([20, 34], ['sacral', 'throat'], 'individual', 'integration'),
 '20-57': ([20, 57], ['spleen', 'throat'], 'individual', 'knowing'),
 '21-45': ([21, 45], ['ego', 'throat'], 'tribal', 'ego'),
 '23-43': ([23, 43], ['ajna', 'throat'], 'individual', 'knowing'),
 '24-61': ([24, 61], ['ajna', 'head'], 'individual', 'knowing'),
 '25-51': ([25, 51], ['ego', 'g'], 'individual', 'centering'),
 '26-44': ([26, 44], ['ego', 'spleen'], 'tribal', 'ego'),
 '27-50': ([27, 50], ['sacral', 'spleen'], 'tribal', 'defense'),
 '28-38': ([28, 38], ['root', 'spleen'], 'individual', 'knowing'),
 '29-46': ([29, 46], ['g', 'sacral'], 'collective', 'sensing'),
 '30-41': ([30, 41], ['root', 'solar_plexus'], 'collective', 'sensing'),
 '32-54': ([32, 54], ['root', 'spleen'], 'tribal', 'ego'),
 '34-57': ([34, 57], ['sacral', 'spleen'], 'individual', 'integration'),
 '35-36': ([35, 36], ['solar_plexus', 'throat'], 'collective', 'sensing'),
 '37-40': ([37, 40], ['ego', 'solar_plexus'], 'tribal', 'ego'),
 '39-55': ([39, 55], ['root', 'solar_plexus'], 'individual', 'knowing'),
 '42-53': ([42, 53], ['root', 'sacral'], 'collective', 'sensing'),
 '47-64': ([47, 64], ['ajna', 'head'], 'collective', 'sensing')}

EXPECTED_METADATA = {'01-08': ('narrative', ['narrative'], []),
 '02-14': ('bonding_feel', ['bonding_feel', 'rhythm'], []),
 '03-60': ('rhythm', ['rhythm'], ['format']),
 '04-63': ('narrative', ['narrative'], []),
 '05-15': ('bonding_feel', ['bonding_feel', 'rhythm'], []),
 '06-59': ('narrative', ['narrative'], []),
 '07-31': ('narrative', ['narrative'], []),
 '09-52': ('rhythm', ['rhythm'], ['format']),
 '10-20': ('talk', ['talk'], []),
 '10-34': ('bonding_feel', ['bonding_feel', 'rhythm'], []),
 '10-57': ('bonding_feel', ['bonding_feel', 'rhythm'], []),
 '11-56': ('talk', ['narrative', 'talk'], []),
 '12-22': ('action_voice', ['action_voice', 'talk'], ['direct_mt']),
 '13-33': ('narrative', ['narrative'], []),
 '16-48': ('action_voice', ['action_voice', 'talk'], []),
 '17-62': ('talk', ['narrative', 'talk'], []),
 '18-58': ('rhythm', ['rhythm'], []),
 '19-49': ('rhythm', ['rhythm'], []),
 '20-34': ('action_voice', ['action_voice', 'talk'], ['direct_mt']),
 '20-57': ('narrative', ['narrative'], []),
 '21-45': ('action_voice', ['action_voice', 'talk'], ['direct_mt']),
 '23-43': ('talk', ['narrative', 'talk'], []),
 '24-61': ('narrative', ['narrative'], []),
 '25-51': ('bonding_feel', ['bonding_feel', 'rhythm'], []),
 '26-44': ('narrative', ['narrative'], []),
 '27-50': ('narrative', ['narrative'], []),
 '28-38': ('rhythm', ['rhythm'], []),
 '29-46': ('bonding_feel', ['bonding_feel', 'rhythm'], []),
 '30-41': ('rhythm', ['rhythm'], []),
 '32-54': ('rhythm', ['rhythm'], []),
 '34-57': ('narrative', ['narrative'], []),
 '35-36': ('action_voice', ['action_voice', 'talk'], ['direct_mt']),
 '37-40': ('narrative', ['narrative'], []),
 '39-55': ('rhythm', ['rhythm'], []),
 '42-53': ('rhythm', ['rhythm'], ['format']),
 '47-64': ('narrative', ['narrative'], [])}

EXPECTED_GATE_CENTERS = {1: 'g',
 2: 'g',
 3: 'sacral',
 4: 'ajna',
 5: 'sacral',
 6: 'solar_plexus',
 7: 'g',
 8: 'throat',
 9: 'sacral',
 10: 'g',
 11: 'ajna',
 12: 'throat',
 13: 'g',
 14: 'sacral',
 15: 'g',
 16: 'throat',
 17: 'ajna',
 18: 'spleen',
 19: 'root',
 20: 'throat',
 21: 'ego',
 22: 'solar_plexus',
 23: 'throat',
 24: 'ajna',
 25: 'g',
 26: 'ego',
 27: 'sacral',
 28: 'spleen',
 29: 'sacral',
 30: 'solar_plexus',
 31: 'throat',
 32: 'spleen',
 33: 'throat',
 34: 'sacral',
 35: 'throat',
 36: 'solar_plexus',
 37: 'solar_plexus',
 38: 'root',
 39: 'root',
 40: 'ego',
 41: 'root',
 42: 'sacral',
 43: 'ajna',
 44: 'spleen',
 45: 'throat',
 46: 'g',
 47: 'ajna',
 48: 'spleen',
 49: 'solar_plexus',
 50: 'spleen',
 51: 'ego',
 52: 'root',
 53: 'root',
 54: 'root',
 55: 'solar_plexus',
 56: 'throat',
 57: 'spleen',
 58: 'root',
 59: 'sacral',
 60: 'root',
 61: 'head',
 62: 'throat',
 63: 'head',
 64: 'head'}

def test_all_source_facts_and_product_metadata_are_exact(tmp_path: Path) -> None:
    root = catalog_root(tmp_path)
    capture = _capture_registry_config(root)
    cfg = capture.config
    assert list(cfg.channels) == list(EXPECTED_CHANNELS)
    assert {key: gate.center for key, gate in cfg.gates.items()} == EXPECTED_GATE_CENTERS
    for key, (gates, centers, primary, substream) in EXPECTED_CHANNELS.items():
        channel = cfg.channels[key]
        assert (list(channel.gates), list(channel.centers), channel.circuit_primary, channel.substream) == (gates, centers, primary, substream)
        assert (channel.primary_domain, list(channel.domains), list(channel.flags)) == EXPECTED_METADATA[key]
    assert {key for key, channel in cfg.channels.items() if channel.substream == 'integration'} == {'10-20', '10-57', '20-34', '34-57'}
    for relative, source in capture.sources.items():
        assert source.raw == (root / relative).read_bytes()
        assert source.sha256 == hashlib.sha256(source.raw).hexdigest()
        assert source.size_bytes == len(source.raw)
    capture.verify_unchanged()


@pytest.mark.parametrize('pair', [[2, 14], [5, 15], [6, 59], [7, 31], [9, 52], [10, 57], [47, 64]])
def test_numeric_gate_order_accepts_without_repair(pair: list[int]) -> None:
    assert validate_channel_gates(pair, f'{pair[0]:02d}-{pair[1]:02d}') == tuple(pair)
    with pytest.raises(SchemaValidationError) as error:
        validate_channel_gates(list(reversed(pair)))
    assert error.value.code == 'CHANNEL_GATE_ORDER_MISMATCH'


@pytest.mark.parametrize('pair', [[True, 8], [1.0, 8], ['1', 8], [0, 8], [1, 65], [1, 1], [1], [1, 8, 9]])
def test_gate_pairs_reject_wrong_type_range_and_cardinality(pair: list) -> None:
    with pytest.raises(SchemaValidationError):
        validate_channel_gates(pair)


@pytest.mark.parametrize('identity', ['1-08', '01-8', '０１-０８', '08-01', '01-08\n', '01-09'])
def test_gate_ids_are_exact_ascii_and_bound_to_pair(identity: str) -> None:
    with pytest.raises(SchemaValidationError):
        validate_channel_gates([1, 8], identity)


@pytest.mark.parametrize('field,value,code', [
    ('substream', 'centering', 'CHANNEL_ASSIGNMENT_MISMATCH'),
    ('circuit_primary', 'tribal', 'CHANNEL_ASSIGNMENT_MISMATCH'),
    ('primary_domain', 'talk', 'CHANNEL_PRODUCT_METADATA_MISMATCH'),
    ('centers', ['throat', 'g'], 'CHANNEL_CENTER_PROJECTION_MISMATCH'),
    ('substream', None, 'SCHEMA_VALIDATION_FAILED'),
    ('substream', 'missing', 'SCHEMA_VALIDATION_FAILED'),
    ('gates', [1.0, 8], 'SCHEMA_VALIDATION_FAILED'),
])
def test_allowed_vocabulary_does_not_replace_exact_assignment(tmp_path: Path, field: str, value: object, code: str) -> None:
    root = catalog_root(tmp_path)
    path = root / 'catalog/channels_v1.json'
    data = json.loads(path.read_bytes())
    data['channels'][0][field] = value
    write_canonical(path, data)
    with pytest.raises(RegistryConfigError) as error:
        load_registry_config(root)
    assert error.value.code == code


@pytest.mark.parametrize('change', ['missing', 'extra', 'duplicate', 'reordered'])
def test_exact_catalog_roster_refuses_changes(tmp_path: Path, change: str) -> None:
    root = catalog_root(tmp_path)
    path = root / 'catalog/channels_v1.json'
    data = json.loads(path.read_bytes())
    rows = data['channels']
    if change == 'missing':
        rows.pop()
    elif change == 'extra':
        rows.append(rows[-1])
    elif change == 'duplicate':
        rows[-1] = rows[0]
    else:
        rows[0], rows[1] = rows[1], rows[0]
    write_canonical(path, data)
    with pytest.raises(RegistryConfigError):
        load_registry_config(root)


def test_coherent_gate_and_channel_reassignment_cannot_validate_itself(tmp_path: Path) -> None:
    root = catalog_root(tmp_path)
    gate_path, channel_path = root / 'catalog/gates_v1.json', root / 'catalog/channels_v1.json'
    gates, channels = json.loads(gate_path.read_bytes()), json.loads(channel_path.read_bytes())
    # Swap Center facts while preserving each Center's aggregate count.
    gates['gates'][0]['center'], gates['gates'][7]['center'] = gates['gates'][7]['center'], gates['gates'][0]['center']
    mapping = {row['gate']: row['center'] for row in gates['gates']}
    for row in channels['channels']:
        row['centers'] = sorted({mapping[gate] for gate in row['gates']})
    write_canonical(gate_path, gates)
    write_canonical(channel_path, channels)
    with pytest.raises(SchemaValidationError) as error:
        load_registry_config(root)
    assert error.value.code == 'CHANNEL_CENTER_IDENTITY_MISMATCH'


@pytest.mark.parametrize('name', ['top-duplicate', 'nested-duplicate', 'bom', 'invalid-utf8', 'surrogate', 'crlf', 'no-lf', 'two-lf', 'space', 'key-order', 'nan', 'overflow'])
def test_raw_sources_refuse_before_information_is_lost(tmp_path: Path, name: str) -> None:
    root = catalog_root(tmp_path)
    path = root / 'catalog/channels_v1.json'
    raw = path.read_bytes()
    reordered = json.loads(raw)
    reordered['channels'][0] = dict(reversed(list(reordered['channels'][0].items())))
    mutations = {
        'top-duplicate': raw.replace(b'{"channels":', b'{"channels":[],"channels":', 1),
        'nested-duplicate': raw.replace(b'"id":"01-08"', b'"id":"01-08","id":"01-08"', 1),
        'bom': b'\xef\xbb\xbf' + raw, 'invalid-utf8': b'\xff' + raw,
        'surrogate': raw.replace(b'"knowing"', b'"\\ud800"', 1),
        'crlf': raw[:-1] + b'\r\n', 'no-lf': raw[:-1], 'two-lf': raw+b'\n', 'space': b' ' + raw,
        'key-order': json.dumps(reordered, sort_keys=False, separators=(',', ':'), ensure_ascii=False).encode()+b'\n',
        'nan': raw.replace(b'"gates":[1,8]', b'"gates":[NaN,8]', 1),
        'overflow': raw.replace(b'"gates":[1,8]', b'"gates":[1e999,8]', 1),
    }
    assert mutations[name] != raw
    path.write_bytes(mutations[name])
    with pytest.raises(SchemaValidationError) as error:
        load_registry_config(root)
    assert error.value.code in {'DUPLICATE_JSON_KEY', 'INVALID_UTF8', 'INVALID_JSON', 'INVALID_UNICODE', 'NONCANONICAL_JSON', 'NONFINITE_JSON'}
    assert path.read_bytes() == mutations[name]


@pytest.mark.parametrize('container', ['array', 'object'])
def test_overdeep_raw_source_refuses_with_typed_error(tmp_path, container):
    root = catalog_root(tmp_path)
    path = root / 'catalog/channels_v1.json'
    raw = (b'[' * 1100 + b'0' + b']' * 1100 + b'\n') if container == 'array' else (
        b'{"a":' * 1100 + b'0' + b'}' * 1100 + b'\n')
    path.write_bytes(raw)
    with pytest.raises(SchemaValidationError) as error:
        load_registry_config(root)
    assert error.value.code == 'INVALID_JSON'
    assert path.read_bytes() == raw


@pytest.mark.parametrize('location', ['properties', 'identity'])
@pytest.mark.parametrize('value', [[], None, True])
def test_consumer_schema_invalid_identity_shape_refuses_with_typed_error(tmp_path, location, value):
    from engine.config.registry_loader import _LocalCapture, _validate_local_schema
    root = catalog_root(tmp_path)
    relative = 'docs/schemas/config_bundle_fe.json'
    path = root / relative
    schema = json.loads(path.read_bytes())
    if location == 'properties':
        schema['properties'] = value
    else:
        schema['properties']['schema'] = value
    path.write_text(json.dumps(schema, indent=2) + '\n')
    with pytest.raises(SchemaValidationError) as error:
        _validate_local_schema(_LocalCapture(root), relative, {})
    assert error.value.code == 'INVALID_SCHEMA'


@pytest.mark.parametrize('kind', ['file', 'ancestor', 'schema', 'missing-schema'])
def test_selected_root_refuses_unsafe_or_missing_dependencies(tmp_path: Path, kind: str) -> None:
    root = catalog_root(tmp_path / 'root')
    if kind == 'ancestor':
        (root / 'catalog').rename(tmp_path / 'moved')
        (root / 'catalog').symlink_to(tmp_path / 'moved', target_is_directory=True)
    else:
        path = root / ('schemas/channels_v1.schema.json' if 'schema' in kind else 'catalog/channels_v1.json')
        data = path.read_bytes()
        path.unlink()
        if kind != 'missing-schema':
            target = tmp_path / 'external.json'
            target.write_bytes(data)
            path.symlink_to(target)
    with pytest.raises(SchemaValidationError) as error:
        load_registry_config(root)
    assert error.value.code in {'UNSAFE_SOURCE_PATH', 'MISSING_FILE'}


def test_source_capture_detects_later_change_and_base_needs_no_mechanics_release(tmp_path: Path) -> None:
    root = catalog_root(tmp_path)
    (root / 'catalog/magic10_mechanics_v1.json').unlink()
    capture = _capture_registry_config(root)
    assert capture.config.manifest.version == '1.3.0'
    assert not any('mechanics' in name for name in capture.sources)
    path = root / 'catalog/magic10_seeds.json'
    data = json.loads(path.read_bytes())
    data['harmony']['seed_version'] += '-test'
    write_canonical(path, data)
    with pytest.raises(SchemaValidationError) as error:
        capture.verify_unchanged()
    assert error.value.code == 'SOURCE_CHANGED'


def test_remote_schema_reference_is_refused_locally(tmp_path: Path) -> None:
    root = catalog_root(tmp_path)
    path = root / 'schemas/channels_v1.schema.json'
    data = json.loads(path.read_bytes())
    data['$ref'] = 'https://invalid.example/schema.json'
    write_canonical(path, data)
    with pytest.raises(SchemaValidationError) as error:
        load_registry_config(root)
    assert error.value.code == 'NONLOCAL_SCHEMA_REFERENCE'


def test_source_read_refuses_an_ancestor_swapped_after_precheck(tmp_path: Path, monkeypatch) -> None:
    import os
    from engine.config import registry_loader
    root = catalog_root(tmp_path / 'root')
    actual_open = os.open
    swapped = False

    def swap_before_directory_open(path, flags, *args, **kwargs):
        nonlocal swapped
        if path == 'catalog' and not swapped and 'dir_fd' in kwargs:
            swapped = True
            (root / 'catalog').rename(tmp_path / 'external_catalog')
            (root / 'catalog').symlink_to(tmp_path / 'external_catalog', target_is_directory=True)
        return actual_open(path, flags, *args, **kwargs)

    monkeypatch.setattr(registry_loader.os, 'open', swap_before_directory_open)
    with pytest.raises(SchemaValidationError) as error:
        load_registry_config(root)
    assert swapped
    assert error.value.code == 'SOURCE_READ_FAILED'


@pytest.mark.parametrize('field', ['min', 'max'])
@pytest.mark.parametrize('coercion', [float, str, bool])
def test_each_caps_bound_rejects_coercion_in_its_executable_home(tmp_path: Path, field: str, coercion) -> None:
    root = catalog_root(tmp_path)
    path = root / 'catalog/magic10_caps.json'
    original = json.loads(path.read_bytes())
    for category in original:
        altered = json.loads(json.dumps(original))
        altered[category]['bounds'][field] = coercion(altered[category]['bounds'][field])
        write_canonical(path, altered)
        with pytest.raises(SchemaValidationError) as error:
            load_registry_config(root)
        assert error.value.code == 'INVALID_MAGIC10'
