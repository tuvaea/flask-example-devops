"""
Unit tests
"""
from flask import session


def test_root(client):
    response = client.get('/')
    assert response.status_code == 200, "Response code should be 200."


def test_public(client):
    response = client.get('/public/')
    assert response.status_code == 200, "Response code should be 200."




# TODO: Make to seperate tests for authorized and unauthorized
def test_private(client):
    response = client.get('/private/')

    if "current_user" in session.keys():
        assert response.status_code == 200, "Response code should be 200. Client is authorized"
    elif "current_user" not in session.keys():
        assert response.status_code == 401, "Response code should be 401. Client should not be authorized"


# TODO: Make to seperate tests for authorized and unauthorized
def test_admin(client):
    response = client.get('/admin/')

    if session.get("current_user", None) == "ADMIN":
        assert response.status_code == 200, "Response code should be 200. Client is authorized"
    elif session.get("current_user", None) != "ADMIN":
        assert response.status_code == 401, "Response code should be 401. Client should not be authorized"



def test_login(client):
    # Sends a POST login requests and returns
    # the response recieved after the 302 redirect
    response = client.post("/login", data={
            "id": "test",
            "pw": "123456",
        }, follow_redirects=True)
    print(response)

    assert response.status_code == 200, "Response code should be 200. Client is authorized"


def test_admin_login(client):
    # Sends a POST login requests and returns
    # the response recieved after the 302 redirect
    response = client.post("/login", data={
        "id": "admin",
        "pw": "admin",
    }, follow_redirects=True)
    print(response)

    assert response.status_code == 200, "Response code should be 200. Client is authorized"
