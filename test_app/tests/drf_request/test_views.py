import pytest


@pytest.fixture(autouse=True)
def override_urlconf(settings):
    settings.ROOT_URLCONF = 'tests.drf_request.urls'


def test_get(client):
    client.get('/test?a=10&b=20')


def test_post(client):
    client.post('/test', data={'c': 30, 'd': 40})
