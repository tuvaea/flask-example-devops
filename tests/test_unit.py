import pytest
from flask import url_for


def test_app(app):
    # 'with' is a context manager and automaticly
    # sets and cleans up the test client
    with app.test_client() as client:
        respone = client.get('/')
        assert respone.status_code == 200, "Response code should be 200."
