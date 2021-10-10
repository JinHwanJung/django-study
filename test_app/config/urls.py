from django.contrib import admin
from django.urls import path, include

from config.views import index

urlpatterns = [
    path('', index),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('secret-admin/', admin.site.urls),
]
