import pytest
import os

from src import create_app, db


@pytest.fixture(scope="session")
def app():
    """Create a test app with an in-memory SQLite database."""
    """
    TODO - after initial testing this has to be revisited to ensure only a initial creation is done to make the 
    persistence layer really persistent 
    """
    env = os.getenv('EVE_APP_ENV', 'dev')
    test_app = create_app(env)  # Ensure "test" is mapped to an in-memory DB
    with test_app.app_context():
        db.create_all()  # Create test tables
    yield test_app  # Provide the app to tests
    with test_app.app_context():
        db.drop_all()  # Tear down the DB after all tests

@pytest.fixture(scope="session")
def client(app):
    """Create a test client for sending HTTP requests."""
    return app.test_client()

@pytest.fixture(scope="function")
def db_session(app):
    """Provide a test database session that rolls back after each test."""
    session = db.session
    connection = db.engine.connect()
    transaction = connection.begin()

    yield session  # Provide session to tests

    transaction.rollback()  # Rollback changes after each test
    connection.close()