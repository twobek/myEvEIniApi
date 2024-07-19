import pytest
from src import create_app, db


@pytest.fixture(scope='module')
def test_client():
    """
    Pytest fixture to set up and tear down a Flask application configured for testing.

    This fixture sets up the application with an in-memory database and provides a test
    client for making requests.
    """
    # Set up: create a Flask app configured for testing
    flask_app = create_app('testing')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            # Create the database and the database table(s)
            db.create_all()

        yield testing_client  # this is where the testing happens!

        # Tear down: remove the database and database table(s)
        with flask_app.app_context():
            db.drop_all()
