from django.urls import path, include
from rest_framework.routers import DefaultRouter
from test_app.article.views import ArticleViewSet
from test_app.constants import MIDDLEWARE_KEY, DIVISION_LINE

router = DefaultRouter(trailing_slash=False)
router.register('articles', ArticleViewSet)


def middleware_articles2(request, view_func, view_args, view_kwargs):
    print(DIVISION_LINE)
    print('middleware_articles2')
    print(request, view_func, view_args, view_kwargs)
    print(DIVISION_LINE)


urlpatterns = [
    path('', include(router.urls), kwargs={MIDDLEWARE_KEY: middleware_articles2}),
]
