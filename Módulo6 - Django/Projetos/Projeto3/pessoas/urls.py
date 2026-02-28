from django.urls import path
from . import views

app_name = 'pessoas'

urlpatterns = [
    path('criar/', views.criar_pessoa, name='criar'),
    path('<int:pk>/editar/', views.editar_pessoa, name='editar'),
    path('<int:pk>/deletar/', views.deletar_pessoa, name='deletar'),
    path('<int:pk>/', views.detalhe_pessoa, name='detalhe'),
    path('', views.lista_pessoas, name='lista'),
]
