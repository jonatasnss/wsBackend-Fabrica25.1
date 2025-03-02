from django.db import models
from django.contrib.auth.models import User

class Colecao(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='colecoes')
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Coleção'
        verbose_name_plural = 'Coleções'
        ordering = ['-data_criacao']
    
    def __str__(self):
        return self.nome

class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    ano = models.CharField(max_length=10)
    diretor = models.CharField(max_length=200, blank=True)
    genero = models.CharField(max_length=200, blank=True)
    sinopse = models.TextField(blank=True)
    poster_url = models.URLField(blank=True)
    imdb_id = models.CharField(max_length=20, unique=True)
    data_adicao = models.DateTimeField(auto_now_add=True)
    colecoes = models.ManyToManyField(Colecao, related_name='filmes', blank=True)
    
    class Meta:
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'
        ordering = ['-data_adicao']
    
    def __str__(self):
        return f"{self.titulo} ({self.ano})"