from django.urls import path
from . import views

app_name = 'pessoas'

urlpatterns = [
    path(app_name+'/criar/', views.criar_pessoa, name='criar'),
    path(app_name+'/<int:pessoa_id>/editar/', views.editar_pessoa, name='editar'),
    path(app_name+'/<int:pessoa_id>/deletar/', views.deletar_pessoa, name='deletar'),
    path(app_name+'/<int:pessoa_id>/', views.detalhe_pessoa, name='detalhe'),
    path(app_name+'/', views.lista_pessoas, name='lista'),
]
