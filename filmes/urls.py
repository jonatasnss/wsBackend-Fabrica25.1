from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pesquisar/', views.pesquisar_filmes, name='pesquisar_filmes'),
    path('filme/<str:imdb_id>/', views.detalhes_filme, name='detalhes_filme'),
    path('filme/<str:imdb_id>/adicionar/', views.adicionar_filme, name='adicionar_filme'),
    path('colecoes/', views.listar_colecoes, name='listar_colecoes'),
    path('colecoes/criar/', views.criar_colecao, name='criar_colecao'),
    path('colecoes/<int:colecao_id>/', views.detalhes_colecao, name='detalhes_colecao'),
    path('colecoes/<int:colecao_id>/editar/', views.editar_colecao, name='editar_colecao'),
    path('colecoes/<int:colecao_id>/excluir/', views.excluir_colecao, name='excluir_colecao'),
    path('filme/<str:imdb_id>/adicionar-colecao/<int:colecao_id>/', views.adicionar_filme_colecao, name='adicionar_filme_colecao'),
    path('filme/<str:imdb_id>/remover-colecao/<int:colecao_id>/', views.remover_filme_colecao, name='remover_filme_colecao'),
]