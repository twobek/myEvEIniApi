from test.config.test_db_config import test_client
from src.models.universe_types import UniverseTypesROH
from src.crud.universe_types import merge_type, merge_whole_page

def test_merge_type_insert(test_client):
    merge_type(test_client, type_id=1, page=1)
    result = test_client.query(UniverseTypesROH).filter_by(type_id=1).first()
    assert result is not None
    assert result.api_page == 1
    assert result.creation_ts is None
