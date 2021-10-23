from django.urls import path, include
from django.utils.deprecation import MiddlewareMixin
from rest_framework.routers import DefaultRouter
from article.views import ArticleViewSet


router = DefaultRouter(trailing_slash=False)
router.register('articles', ArticleViewSet)


class HelloMiddleware4(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        print('Hello4')


class HelloMiddleware5(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        print('Hello5')


urlpatterns = [
    path('', include(router.urls), kwargs={'middleware': HelloMiddleware4}),
]


