import pytest
from .models import Article, Comment
from user.models import User


@pytest.fixture(autouse=True)
def override_urlconf(settings):
    settings.ROOT_URLCONF = 'tests.drf_url_router.urls'


def make_row(model, new_pk, **fields):
    for pk in new_pk:
        model.objects.create(id=pk, **fields)


@pytest.mark.django_db
def test(client):
    User.objects.create(id=1, username='user1')
    User.objects.create(id=2, username='user2')
    make_row(Article, new_pk=[1, 2, 3], user_id=1)
    make_row(Article, new_pk=[4, 5], user_id=2)
    make_row(Comment, new_pk=[1, 2], user_id=1, article_id=1)
    make_row(Comment, new_pk=[3], user_id=1, article_id=2)
    make_row(Comment, new_pk=[4], user_id=1, article_id=3)
    make_row(Comment, new_pk=[5, 6], user_id=2, article_id=4)

    response = client.get('/users')
    assert response.status_code == 200

    response = client.get('/users/1')
    assert response.status_code == 200

    response = client.get('/users/1/articles')
    assert response.status_code == 200

    response = client.get('/users/1/articles/3')
    assert response.status_code == 200

    response = client.get('/users/1/articles/3/comments')
    assert response.status_code == 200

    response = client.get('/users/1/articles/3/comments/4')
    assert response.status_code == 200
