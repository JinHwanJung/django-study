from django.urls import path, include
from rest_framework.routers import DefaultRouter
from article.views import ArticleViewSet


router = DefaultRouter(trailing_slash=False)
router.register('articles', ArticleViewSet)


def middleware_articles2(request, view_func, view_args, view_kwargs):
    print('*' * 10)
    print('middleware_articles2')
    print(request, view_func, view_args, view_kwargs)
    print('*'*10)


urlpatterns = [
    path('', include(router.urls), kwargs={'middleware': middleware_articles2}),
]
