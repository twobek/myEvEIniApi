import datetime

from src import db
from src.models.universe_types_roh import UniverseTypesROH
from datetime import datetime

class UniverseTypesRohError(Exception):
    def __init__(self, message, *args):
        super().__init__(message, *args)
        self.message = message
def merge_universe_types_roh(type_ids: list[int], new_time: datetime):
    """Insert new type IDs into the database if they do not exist."""
    new_entries = []

    for type_id in type_ids:
        uni_type = db.session.query(UniverseTypesROH).filter_by(type_id=type_id).first()

        if not uni_type:
            new_entries.append(UniverseTypesROH(type_id=type_id, creation_ts=new_time))
        else:
            update_creation_ts_with_obj(uni_type, new_time)


    if new_entries:
        db.session.bulk_save_objects(new_entries)  # Efficient bulk insert
        db.session.commit()

def update_creation_ts_universe_type_roh(type_id: int, new_timestamp:datetime):
    """Update creation_ts in universe_type_roh"""

    type_obj = db.session.query(UniverseTypesROH).filter_by(type_id=type_id).first()

    if type_obj:
        return update_creation_ts_with_obj(type_obj, new_timestamp)

    else:
        raise ValueError(f"Record with type_id {type_id} not found")
        return None

def update_creation_ts_with_obj(uni_obj:UniverseTypesROH, new_time:datetime):
    # Update the value
    uni_obj.creation_ts = new_time

    # Commit the changes to the database
    db.session.commit()

    # Refresh the object to reflect changes
    db.session.refresh(uni_obj)

    return uni_obj

def delete_universe_elements_roh(type_ids: list[int]):

    for type_id in type_ids:
        delete_universe_element_roh(type_id)

def delete_universe_element_roh(type_id: int):

    if isinstance(type_id, int):
        type_obj = db.session.query(UniverseTypesROH).filter_by(type_id=type_id).first()

        if type_obj:
            delete_universe_elements_roh_obj(type_obj)

def delete_universe_elements_roh_obj(uni_obj:UniverseTypesROH):

    db.session.delete(uni_obj)

    db.session.commit()