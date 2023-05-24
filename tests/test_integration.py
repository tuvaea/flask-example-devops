# TODO: More of an integrationtest, move when necessary.

from common import login
from test_unit import *
from datetime import datetime

"""
Test for checking if unauthenticated users
can access the private page.
"""
def test_private_login(client):
    login(client, "test", "123456")
    response = client.get("/private/")

    assert response.status_code == 200, "Response code should be 200. Client is not authorized"
    assert b'<h1>Private Page</h1>' in response.data, "Could not enter private page"


"""
Tests if an admin can sign in through the forms.
Passes if the response status code is 200
and that the username is displayed in the navigation bar
"""
def test_admin_login(client):
    # Sends a POST login requests and returns
    # the response recieved after the 302 redirect
    response = login(client, "admin", "admin")

    assert response.status_code == 200, "Response code should be 200. Client is authorized"
    assert b"<b>ADMIN</b>" in response.data, "Test not found in navigation bar" # Not the best way, but the website contains no cookies or such


"""
Tests if a user can sign in and post a note.
Passes if the new note and time posted was found
on the /private/ page.
"""
def test_add_note(client):
    test_login_user(client)

    note = b'This is the second test note.'

    client.post("/write_note", data={
        "text_note_to_take": note,
    }, follow_redirects=True)

    time = datetime.now().replace(microsecond=0) # Get the time the post was created withouth the milliseconds
    time = time.strftime("%Y-%m-%d %H:%M:%S").encode("utf-8") # Convert to utf-8 byte string

    response = client.get("/private/")

    print(response)
    assert note in response.data, "Note was not posted/found." # Passes only if a part of the text is found on the screen. Should be fixed.
    assert time in response.data, "Time of the post does not match. Could" # Tests if the date is correct, to make sure it is not an old post

