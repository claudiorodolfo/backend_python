from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('criar/', views.criar_produto, name='criar'),
    path('<int:id>/editar/', views.editar_produto, name='editar'),
    path('<int:id>/deletar/', views.deletar_produto, name='deletar'),
    path('<int:id>/', views.detalhe_produto, name='detalhe'),
    path('', views.lista_produtos, name='lista'),
]
