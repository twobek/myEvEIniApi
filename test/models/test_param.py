import pytest
import os

from sqlalchemy import inspect
from src import db
from src.models.universe_types import Param

table = "param"
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

    assert "type" in column_names
    assert "text" in column_names
    assert "number" in column_names
    assert "date" in column_names

    # ✅ Check column types
    assert column_names["type"]["type"].__class__.__name__ == "STRING"
    assert column_names["text"]["type"].__class__.__name__ == "TEXT"
    assert column_names["number"]["type"].__class__.__name__ == "INTEGER"
    assert column_names["date"]["type"].__class__.__name__ == "DATE"

@pytest.mark.usefixtures("db_session")
def test_primary_keys():
    inspector = inspect(db.engine)
    pk = inspector.get_pk_constraint(table)["constrained_columns"]

    assert pk == ["type"]  # ✅ Check if correct primary key exists

@pytest.mark.usefixtures("db_session")
def test_foreign_keys():
    inspector = inspect(db.engine)
    fks = inspector.get_foreign_keys(table)

    assert len(fks) == 0  # ✅ Adjust if foreign keys exist

def test_universe_type_empty_db(app, db_session):
    """Test if the param table is empty at the start"""

    if os.getenv('EVE_APP_ENV') == 'dev':
        with app.app_context():
            count = db_session.query(Param).count()
            assert count == 0  # Since the test DB is fresh for each test
    else:
        assert 1 == 1

def test_param_type_creation_with_onlyDate(app, db_session):
    """Test if param model can be created with only a date and retrieved"""
    from datetime import date

    param_type = 'test_param_date'

    with app.app_context():
        # Create a new UniverseTypesROH instance
        new_date = date.today()
        new_param = Param(type=param_type, date=new_date)
        db_session.add(new_param)
        db_session.commit()

        # Retrieve the object from the database
        retrieved = db_session.query(Param).filter_by(type=param_type).first()

        # Assertions
        assert retrieved is not None
        assert retrieved.type == param_type
        assert retrieved.date == new_date
        assert retrieved.text == None
        assert retrieved.number == None

        db_session.delete(new_param)
        db_session.commit()


def test_param_type_creation_with_onlyText(app, db_session):
    """Test if param model can be created with only a text and retrieved"""
    from datetime import date

    param_type = 'test_param_text'
    param_text = 'some shit has to stand here'

    with app.app_context():
        # Create a new Param instance
        new_param = Param(type=param_type, text=param_text)
        db_session.add(new_param)
        db_session.commit()

        # Retrieve the object from the database
        retrieved = db_session.query(Param).filter_by(type=param_type).first()

        # Assertions
        assert retrieved is not None
        assert retrieved.type == param_type
        assert retrieved.date == None
        assert retrieved.text == param_text
        assert retrieved.number == None

        db_session.delete(new_param)
        db_session.commit()

def test_param_type_creation_with_onlyNumber(app, db_session):
    """Test if param model can be created with only a number and retrieved"""
    from datetime import date

    param_type = 'test_param_number'
    param_number = 1234567890

    with app.app_context():
        # Create a new Param instance
        new_param = Param(type=param_type, number=param_number)
        db_session.add(new_param)
        db_session.commit()

        # Retrieve the object from the database
        retrieved = db_session.query(Param).filter_by(type=param_type).first()

        # Assertions
        assert retrieved is not None
        assert retrieved.type == param_type
        assert retrieved.date == None
        assert retrieved.text == None
        assert retrieved.number == param_number

        db_session.delete(new_param)
        db_session.commit()

def test_param_type_creation_with_all(app, db_session):
    """Test if param model can be created with only a number and retrieved"""
    from datetime import date

    param_type = 'test_param_text'
    param_text = 'some shit has to stand here'
    param_number = 1234567890
    param_date = date.today()

    with app.app_context():
        # Create a new Param instance
        new_param = Param(type=param_type, number=param_number, text=param_text, date=param_date)
        db_session.add(new_param)
        db_session.commit()

        # Retrieve the object from the database
        retrieved = db_session.query(Param).filter_by(type=param_type).first()

        # Assertions
        assert retrieved is not None
        assert retrieved.type == param_type
        assert retrieved.date == param_date
        assert retrieved.text == param_text
        assert retrieved.number == param_number

        db_session.delete(new_param)
        db_session.commit()

