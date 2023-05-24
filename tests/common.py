"""
Common functions used in the unit and
integrations tests
"""


"""
Genereal function used in the tests to perform
a login action using the forms
"""
def login(client, name, pw):
    return client.post("/login", data={
        "id": name,
        "pw": pw,
    }, follow_redirects=True)

def setUser(client, username):
    with client.session_transaction() as session:
        session["current_user"] = username