import os
import sys

# Get the parent directory of the current file (conftest.py)
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add the parent directory to the Python path
sys.path.insert(0, parent_dir)

import pytest
from flask import Flask
from app import create_app

# Config files for the tests
@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # Clean up code happens after yield

    # Set up of the application before test happens here

    with app.test_client() as client:
        yield client

    # Tear down of the application after test happens here

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()