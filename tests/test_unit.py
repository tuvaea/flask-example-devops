"""
Unit tests
"""
from flask import session


def login(client, name, pw):
    return client.post("/login", data={
        "id": name,
        "pw": pw,
    }, follow_redirects=True)


def test_root(client):
    response = client.get('/')
    assert response.status_code == 200, "Response code should be 200."


def test_public(client):
    response = client.get('/public/')
    assert response.status_code == 200, "Response code should be 200."


def test_login(client):
    # Sends a POST login requests and returns
    # the response recieved after the 302 redirect
    response = login(client, "test", "123456")

    assert response.status_code == 200, "Response code should be 200. Client is not authorized"
    assert b"<b>TEST</b>" in response.data, "Test not found in navigation bar" # Not the best way, but the website contains no cookies or such


def test_admin_login(client):
    # Sends a POST login requests and returns
    # the response recieved after the 302 redirect
    response = login(client, "admin", "admin")

    assert response.status_code == 200, "Response code should be 200. Client is authorized"
    assert b"<b>ADMIN</b>" in response.data, "Test not found in navigation bar" # Not the best way, but the website contains no cookies or such


"""
Test for checking if unauthenticated users
can access the private page.
"""
def test_private(client):
    login(client, "test", "123456")
    response = client.get("/private/")

    assert response.status_code == 200, "Response code should be 200. Client is not authorized"
    assert b'<h1>Private Page</h1>' in response.data, "Could not enter private page"


# TODO: More of an integrationtest, move when necessary. Add datetime check
def test_add_note(client):
    login(client, "test", "123456")

    test_private(client)

    note = b'This is the second test note.'

    client.post("/write_note", data={
        "text_note_to_take": note,
    }, follow_redirects=True)

    response = client.get("/private/")

    print(response)
    assert note in response.data, "Note was not posted/found." # Passes only if a part of the text is found on the screen. Should be fixed.

