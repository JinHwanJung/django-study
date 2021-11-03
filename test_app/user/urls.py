from django.urls import path, include
from rest_framework.routers import SimpleRouter

from test_app.constants import DIVISION_LINE, MIDDLEWARE_KEY
from test_app.helper import add_test_app_directory_prefix
from test_app.user.views import UserViewSet


router = SimpleRouter(trailing_slash=False)
router.register('users', UserViewSet)


def middleware_users2(request, view_func, view_args, view_kwargs):
    print(DIVISION_LINE)
    print('middleware_users2')
    print(request, view_func, view_args, view_kwargs)
    print(DIVISION_LINE)


def middleware_articles(request, view_func, view_args, view_kwargs):
    print(DIVISION_LINE)
    print('middleware_articles')
    print(request, view_func, view_args, view_kwargs)
    print(DIVISION_LINE)


urlpatterns = [
    path('', include(router.urls), kwargs={MIDDLEWARE_KEY: middleware_users2}),
    path('users/<int:user_id>/',
         include(add_test_app_directory_prefix('article.urls')),
         kwargs={MIDDLEWARE_KEY: middleware_articles}
         ),
]
