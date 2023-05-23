def test_root(client):
    response = client.get('/')
    assert response.status_code == 200, "Response code should be 200."

def test_
