from django.urls import include, path
from django.utils.deprecation import MiddlewareMixin
from config.views import index
from test_app.helper import add_test_app_directory_prefix


def middleware_index(request, view_func, view_args, view_kwargs):
    print('*' * 10)
    print('middleware_index')
    print(request, view_func, view_args, view_kwargs)
    print('*'*10)


def middleware_users(request, view_func, view_args, view_kwargs):
    print('*' * 10)

    print('middleware_users')
    print(request, view_func, view_args, view_kwargs)
    print('*'*10)


urlpatterns = [
    path('', index, kwargs={'middleware': middleware_index}),
    path('',
         include(add_test_app_directory_prefix('user.urls')),
         kwargs={'middleware': middleware_users}
         ),
]
