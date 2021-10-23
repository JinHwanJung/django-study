import pytest


@pytest.mark.django_db
def test_hello_home(client):
    response = client.get('/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_api_user_list(client):
    response = client.get('/users')
    assert response.status_code == 200


@pytest.mark.django_db
def test_api_user_articles(client):
    response = client.get('/users/1/articles')
    assert response.status_code == 200
