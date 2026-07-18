import pytest
from engine.db.ddl_identity_projection import project_ddl_identity

def test_projects_provider_shapes_and_orders():
    value=[{'kind':'view','name':'v'},{'kind':'table','name':'b','columns':[{'name':'z','data_type':'int','nullable':True},{'name':'a','type':'text'}], 'constraints':['x']}]
    assert project_ddl_identity(value)==[
        {'kind':'table','name':'b','columns':[{'name':'a','type':'text'},{'name':'z','type':'int'}]},
        {'kind':'view','name':'v','columns':[]},
    ]

def test_view_omitted_empty_equivalent_and_unexamined_ignored():
    assert project_ddl_identity([{'kind':'view','name':'v','definition':'a'}]) == project_ddl_identity([{'kind':'view','name':'v','columns':[],'definition':'b'}])

@pytest.mark.parametrize('value',[[], {}, [{'kind':'table','name':'t'}], [{'kind':'table','name':' t','columns':[{'name':'c','type':'x'}]}], [{'kind':'table','name':'t','columns':[{}]}], [{'kind':'table','name':'t','columns':[{'name':'c','type':''}]}], [{'kind':'table','name':'t','columns':[{'name':'c','type':'x','data_type':'y'}]}], [{'kind':'table','name':'t','columns':[{'name':'c','type':'x'},{'name':'c','type':'x'}]}], [{'kind':'table','name':'t','columns':[{'name':'c','type':'x'}]},{'kind':'table','name':'t','columns':[{'name':'d','type':'x'}]}], ['bad']])
def test_rejects_malformed(value):
    with pytest.raises(ValueError): project_ddl_identity(value)
