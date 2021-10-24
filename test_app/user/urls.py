from django.urls import path, include
from django.utils.deprecation import MiddlewareMixin
from rest_framework.routers import DefaultRouter, SimpleRouter
from user.views import UserViewSet


router = SimpleRouter(trailing_slash=False)
router.register('users', UserViewSet)


def middleware_users2(request, view_func, view_args, view_kwargs):
    print('*' * 10)
    print('middleware_users2')
    print(request, view_func, view_args, view_kwargs)
    print('*'*10)


def middleware_articles(request, view_func, view_args, view_kwargs):
    print('*' * 10)
    print('middleware_articles')
    print(request, view_func, view_args, view_kwargs)
    print('*'*10)


urlpatterns = [
    path('', include(router.urls), kwargs={'middleware': middleware_users2}),
    path('users/<int:user_id>/', include('article.urls'), kwargs={'middleware': middleware_articles}),
]
