from django.urls import path
from . import views

app_name = 'pessoas'

urlpatterns = [
    path('criar/', views.criar_pessoa, name='criar'),
    path('<int:pessoa_id>/editar/', views.editar_pessoa, name='editar'),
    path('<int:pessoa_id>/deletar/', views.deletar_pessoa, name='deletar'),
    path('<int:pessoa_id>/', views.detalhe_pessoa, name='detalhe'),
    path('', views.lista_pessoas, name='lista'),
]
