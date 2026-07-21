import json
from tools.evidence import generate_hde_epic038_direct_db_selection as mod

def test_direct_selection_tmp_generation_is_canonical(tmp_path):
    out=tmp_path/'direct.json'
    assert mod.main(['--out', str(out)]) == 0
    data=out.read_bytes()
    assert data.endswith(b'\n') and not data.endswith(b'\n\n')
    parsed=json.loads(data)
    assert parsed['schema']=='hde_epic038.direct_db_selection.v1'
    assert parsed['result']=='PASS'
    assert [c['case'] for c in parsed['cases']] == ['healthy_direct','missing_database_url','unavailable_database_url','retired_keys_present']
    assert parsed['cases'][3]['attempts'] == []
    assert all(c['alternate_transport_attempts'] == 0 for c in parsed['cases'])
