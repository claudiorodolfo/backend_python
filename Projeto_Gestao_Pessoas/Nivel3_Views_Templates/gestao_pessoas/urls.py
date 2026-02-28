"""
URL configuration for gestao_pessoas project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pessoas.urls')),
]
