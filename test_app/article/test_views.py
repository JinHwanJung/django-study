import pytest


@pytest.mark.django_db
def test_api_user_articles(client):
    response = client.get('/users/1/articles')
    assert response.status_code == 200
