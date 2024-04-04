#!/bin/bash

# Run integration tests
pytest test/test_prod_PostgresIntegration.py
pytest test/connections/test_db_connections.py

# Start Flask application
exec "$@"
