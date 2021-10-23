from django.urls import include, path
from django.utils.deprecation import MiddlewareMixin
from config.views import index


class HelloMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        print('Hello')


class HelloHomeMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        print('hello index')


urlpatterns = [
    path('', index, kwargs={'middleware': HelloHomeMiddleware}),
    path('', include('user.urls'), kwargs={'middleware': HelloMiddleware}),
]
