import pytest


@pytest.mark.django_db
def test_hello_home(client):
    response = client.get('/')
    assert response.status_code == 200
