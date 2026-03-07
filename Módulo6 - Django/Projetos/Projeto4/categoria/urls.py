from django.urls import path
from . import views

app_name = 'categoria'

urlpatterns = [
    path('criar/', views.criar_categoria, name='criar'),
    path('<int:id>/editar/', views.editar_categoria, name='editar'),
    path('<int:id>/deletar/', views.deletar_categoria, name='deletar'),
    path('<int:id>/', views.detalhe_categoria, name='detalhe'),
    path('', views.lista_categorias, name='lista'),
]
