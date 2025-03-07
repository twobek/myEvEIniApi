import pytest
from unittest.mock import patch
from src.services.universe_types_service import UniverseTypesService
from src.models.universe_types_roh import UniverseTypesROH

@pytest.mark.usefixtures("db_session")
@patch("src.services.universe_types_service.APIConnector.call_api")
def test_fetch_and_store_universe_types(mock_call_api, db_session):
    """Test fetching and storing universe type IDs from the API."""

    # Step 1: Mock API response with fake type IDs
    mock_call_api.return_value = [2001, 2002, 2003]

    # Step 2: Call the service method
    service = UniverseTypesService()
    service.fetch_and_store_universe_types()

    # Step 3: Verify records exist in DB
    records = db_session.query(UniverseTypesROH).all()
    assert len(records) == 3
    assert {r.type_id for r in records} == {2001, 2002, 2003}

    # Step 4: Mock API returning duplicate IDs
    mock_call_api.return_value = [2001, 2002, 2004]
    service.fetch_and_store_universe_types()

    # Step 5: Ensure new ID is added but duplicates are not
    records = db_session.query(UniverseTypesROH).all()
    assert len(records) == 4
    assert {r.type_id for r in records} == {2001, 2002, 2003, 2004}