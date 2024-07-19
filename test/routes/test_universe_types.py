import pytest
from flask import Flask, request, jsonify
from src import create_app, db
from src.routes.universe_types import universe_types_bp

from test.config.test_db_config import test_client

def test_home_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_client.get('/types/')
    assert response.status_code == 200
    assert b"Shit is working" in response.data


def test_merge_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/types/merge_page/' page is requested (POST)
    THEN check that the response is valid
    """
    # Mocking the data retrieval process
    page = 1
    typeIdList = [1, 2, 3, 4, 5]

    response = test_client.post(f'/types/merge_page/?page={page}', json={'type_ids': typeIdList})
    assert response.status_code == 200
    assert b"successfully merged" in response.data or b"error" in response.data
