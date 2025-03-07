import pytest
from src import db
from src.models.universe_types_roh import UniverseTypesROH
from src.crud.universe_types_roh import merge_universe_types_roh,UniverseTypesRohError

from datetime import datetime

@pytest.mark.usefixtures("db_session")
@pytest.mark.parametrize("type_ids, timestamp, results",
    [
        #positiv test with an list of Type_ids
        ([1001,1002,1003],datetime(2024,11,11,12),
         [{"type_id":1001,"creation_ts":"2024-11-11 12:00:00"},{"type_id":1002,"creation_ts":"2024-11-11 12:00:00"},
           {"type_id":1003,"creation_ts":"2024-11-11 12:00:00"}]
         ),

        #test wihtout a datetime
        ([1001,1002,1003],None,UniverseTypesRohError),

        #test with list not consisting of only ints
        ([1001,'werner',1002],datetime(2024,11,11,13),
         [{"type_id": 1001, "creation_ts": "2024-11-11 13:00:00"},
          {"type_id": 1002, "creation_ts": "2024-11-11 13:00:00"},
          {"type_id": 1003, "creation_ts": "2024-11-11 13:00:00"}]
         )
    ]
)
def test_merge_universe_types_roh(db_session, type_ids, timestamp, results):

    if isinstance(results, dict):
        merge_universe_types_roh(type_ids, timestamp)
        for obj in results:
            tmp_obj = db_session.query(UniverseTypesROH).filter_by(type_id=obj["type_id"]).first()
            assert tmp_obj.creation_ts == datetime.strptime(obj["creation_ts"], "%Y-%m-%d %H:%M:%S")
            db_session.remove(tmp_obj);

    elif isinstance(results, type) and issubclass(results, Exception):
        with pytest.raises(UniverseTypesRohError):
            merge_universe_types_roh(type_ids, timestamp)


