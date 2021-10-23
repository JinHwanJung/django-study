from django.urls import path, include
from django.utils.deprecation import MiddlewareMixin
from rest_framework.routers import DefaultRouter, SimpleRouter
from user.views import UserViewSet


router = SimpleRouter(trailing_slash=False)
router.register('users', UserViewSet)

class HelloMiddleware2(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        print('Hello2')


class HelloMiddleware3(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        print('Hello3')

urlpatterns = [
    path('', include(router.urls), kwargs={'middleware': HelloMiddleware2}),
    path('users/<int:user_id>/', include('article.urls'), kwargs={'middleware': HelloMiddleware3}),
]
