from django.contrib import admin
from .models import Colecao, Filme

@admin.register(Colecao)
class ColecaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'usuario', 'data_criacao')
    list_filter = ('usuario', 'data_criacao')
    search_fields = ('nome', 'descricao', 'usuario__username')
    date_hierarchy = 'data_criacao'

@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ano', 'diretor', 'data_adicao')
    list_filter = ('ano', 'genero', 'data_adicao')
    search_fields = ('titulo', 'diretor', 'genero', 'sinopse')
    date_hierarchy = 'data_adicao'
    filter_horizontal = ('colecoes',)