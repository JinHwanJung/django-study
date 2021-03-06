import pytest


@pytest.mark.django_db
def test_api_user_list(client):
    response = client.get('/users')
    assert response.status_code == 200
