from django.urls import path

from tests.drf_request.views import TestView

urlpatterns = [
    path('test', TestView.as_view())
]