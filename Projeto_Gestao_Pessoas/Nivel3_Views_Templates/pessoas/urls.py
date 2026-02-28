"""
URLs do app pessoas.
"""
from django.urls import path
from . import views

app_name = 'pessoas'

urlpatterns = [
    path('', views.lista_pessoas, name='lista'),
    path('<int:pessoa_id>/', views.detalhe_pessoa, name='detalhe'),
]
