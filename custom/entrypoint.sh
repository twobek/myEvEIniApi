#!/bin/bash
# set environment variable to test
export EVE_APP_ENV=test
# Run integration tests
pytest test/test_PostgresIntegration.py
pytest test/connections/test_db_connection.py

# Start Flask application
exec "$@"
