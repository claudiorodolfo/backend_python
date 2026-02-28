from django.urls import path
from .views import home

app_name = 'pessoas'

urlpatterns = [
    path("", home),
]
