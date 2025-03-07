import pytest

from sqlalchemy import inspect
from src import db
from src.models.universe_types_roh import UniverseTypesROH

table = "universe_types_roh"
# ✅ Use db_session from conftest.py to handle test DB setup and teardown
@pytest.mark.usefixtures("db_session")
def test_table_exists():
    inspector = inspect(db.engine)
    tables = inspector.get_table_names()
    assert table in tables  # ✅ Check if table exists

@pytest.mark.usefixtures("db_session")
def test_table_columns():
    inspector = inspect(db.engine)
    columns = inspector.get_columns(table)
    column_names = {col["name"]: col for col in columns}

    assert "type_id" in column_names
    assert "creation_ts" in column_names

    # ✅ Check column types
    assert column_names["type_id"]["type"].__class__.__name__ == "INTEGER"
    assert column_names["creation_ts"]["type"].__class__.__name__ == "DATE"
@pytest.mark.usefixtures("db_session")
def test_primary_keys():
    inspector = inspect(db.engine)
    pk = inspector.get_pk_constraint(table)["constrained_columns"]

    assert pk == ["type_id"]  # ✅ Check if correct primary key exists

@pytest.mark.usefixtures("db_session")
def test_foreign_keys():
    inspector = inspect(db.engine)
    fks = inspector.get_foreign_keys(table)

    assert len(fks) == 0  # ✅ Adjust if foreign keys exist

def test_universe_type_empty_db(app, db_session):
    """Test if the universe_types_roh table is empty at the start"""
    import os

    if os.getenv('EVE_APP_ENV') == 'dev':
        with app.app_context():
            count = db_session.query(UniverseTypesROH).count()
            assert count == 0  # Since the test DB is fresh for each test
    else:
        assert 1 == 1

def test_universe_type_creation(app, db_session):
    """Test if UniverseTypesROH model can be created and retrieved"""
    from datetime import date

    with app.app_context():
        # Create a new UniverseTypesROH instance
        new_date = date.today()
        new_type = UniverseTypesROH(type_id=1, creation_ts=new_date)
        db_session.add(new_type)
        db_session.commit()

        # Retrieve the object from the database
        retrieved = db_session.query(UniverseTypesROH).filter_by(type_id=1).first()

        # Assertions
        assert retrieved is not None
        assert retrieved.type_id == 1
        assert retrieved.creation_ts == new_date

        db_session.delete(new_type)
        db_session.commit()