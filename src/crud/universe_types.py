from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from src.models.universe_types import UniverseTypesROH

def get_all_types(db: Session):
    return db.query(UniverseTypesROH).all()

def create_type(db: Session, type_id: int):
    db_type = UniverseTypesROH(type_id=type_id)
    db.add(db_type)
    db.commit()
    db.refresh(db_type)
    return db_type

def merge_type(db: Session, type_id: int, page: int, commit: bool = True) -> None:
    """
        Upserts a single type_id. If the type_id exists, it updates the api_page and sets creation_ts to None.
        If it doesn't exist, it inserts a new record with creation_ts as None.

        Args:
            db (Session): SQLAlchemy database session.
            type_id (int): The type_id to be upserted.
            page (int): The page number to set for the type_id.
            commit (bool): Whether to commit the transaction. Defaults to True.
    """
    try:
        # Check if the type_id exists
        db_type = db.query(UniverseTypesROH).filter(UniverseTypesROH.type_id == type_id).first()

        if db_type:
            # Update existing record
            db_type.api_page = page
            db_type.creation_ts = None
        else:
            # insert new record
            db_type = UniverseTypesROH(type_id=type_id, creation_ts=None, api_page=page)
            db.add(db_type)

        if commit:
            db.commit()
    except SQLAlchemyError as e:
        if commit:
            db.rollback()
        raise e
def merge_whole_page(db: Session, type_id_list: list, page: int) -> None:
    """
        Upserts multiple type_ids from a list for a given page number. Uses merge_type function to handle each type_id.

        Args:
            db (Session): SQLAlchemy database session.
            type_id_list (list): List of type_ids to be upserted.
            page (int): The page number to set for the type_ids.
    """
    try:
        for type_id in type_id_list:
            merge_type(db, type_id, page, False)
        db.commit()

    except Exception as e:
        raise e
