from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from .models import Colecao, Filme
from .omdb_api import buscar_filme, obter_detalhes_filme

def home(request):
    colecoes = Colecao.objects.all()[:5]
    filmes_recentes = Filme.objects.all().order_by('-data_adicao')[:8]
    
    context = {
        'colecoes': colecoes,
        'filmes_recentes': filmes_recentes,
    }
    return render(request, 'filmes/home.html', context)

@login_required
def pesquisar_filmes(request):
    resultados = []
    termo_pesquisa = ""
    
    if request.method == 'GET' and 'termo' in request.GET:
        termo_pesquisa = request.GET.get('termo')
        if termo_pesquisa:
            api_key = settings.OMDB_API_KEY
            if not api_key:
                messages.error(request, 'Chave da API OMDB não configurada. Contate o administrador.')
            else:
                resultados = buscar_filme(termo_pesquisa, api_key)
    
    context = {
        'resultados': resultados,
        'termo_pesquisa': termo_pesquisa,
    }
    return render(request, 'filmes/pesquisar.html', context)

@login_required
def adicionar_filme(request, imdb_id):
    api_key = settings.OMDB_API_KEY
    if not api_key:
        messages.error(request, 'Chave da API não configurada')
        return redirect('pesquisar_filmes')
        
    detalhes = obter_detalhes_filme(imdb_id, api_key)
    
    if detalhes.get('Response') == 'True':
        filme, criado = Filme.objects.get_or_create(
            imdb_id=imdb_id,
            defaults={
                'titulo': detalhes.get('Title', ''),
                'ano': detalhes.get('Year', ''),
                'poster_url': detalhes.get('Poster', ''),
                'diretor': detalhes.get('Director', ''),
                'genero': detalhes.get('Genre', ''),
                'sinopse': detalhes.get('Plot', ''),
            }
        )
        
        if criado:
            messages.success(request, f'Filme "{filme.titulo}"!')
        else:
            messages.info(request, f'O filme "{filme.titulo}" já está no sistema.')
            
        return redirect('detalhes_filme', imdb_id=imdb_id)
    else:
        messages.error(request, 'Não foi possível encontrar nada.')
        return redirect('pesquisar_filmes')

@login_required
def detalhes_filme(request, imdb_id):
    filme = get_object_or_404(Filme, imdb_id=imdb_id)
    colecoes_usuario = Colecao.objects.filter(usuario=request.user)
    
    context = {
        'filme': filme,
        'colecoes_usuario': colecoes_usuario,
    }
    return render(request, 'filmes/detalhes_filme.html', context)

@login_required
def listar_colecoes(request):
    """Lista todas as coleções do usuário"""
    colecoes = Colecao.objects.filter(usuario=request.user)
    
    context = {
        'colecoes': colecoes,
    }
    return render(request, 'filmes/colecoes.html', context)

@login_required
def criar_colecao(request):
    """Cria uma nova coleção"""
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao', '')
        
        if nome:
            colecao = Colecao.objects.create(
                nome=nome,
                descricao=descricao,
                usuario=request.user
            )
            messages.success(request, f'Coleção "{colecao.nome}" criada com sucesso!')
            return redirect('listar_colecoes')
        else:
            messages.error(request, 'O nome da coleção é obrigatório.')
    
    return render(request, 'filmes/criar_colecao.html')

@login_required
def detalhes_colecao(request, colecao_id):
    """Exibe os detalhes de uma coleção"""
    colecao = get_object_or_404(Colecao, id=colecao_id, usuario=request.user)
    filmes = colecao.filmes.all()
    
    context = {
        'colecao': colecao,
        'filmes': filmes,
    }
    return render(request, 'filmes/detalhes_colecao.html', context)

@login_required
def adicionar_filme_colecao(request, imdb_id, colecao_id):
    """Adiciona um filme a uma coleção"""
    filme = get_object_or_404(Filme, imdb_id=imdb_id)
    
    if request.method == 'GET' and 'colecao_id' in request.GET:
        colecao_id = request.GET.get('colecao_id')
        
    colecao = get_object_or_404(Colecao, id=colecao_id, usuario=request.user)
    
    colecao.filmes.add(filme)
    messages.success(request, f'Filme "{filme.titulo}" adicionado à coleção "{colecao.nome}"!')
    
    return redirect('detalhes_colecao', colecao_id=colecao_id)

@login_required
def remover_filme_colecao(request, imdb_id, colecao_id):
    filme = get_object_or_404(Filme, imdb_id=imdb_id)
    colecao = get_object_or_404(Colecao, id=colecao_id, usuario=request.user)
    
    colecao.filmes.remove(filme)
    messages.success(request, f'Filme "{filme.titulo}" removido da coleção "{colecao.nome}"!')
    
    return redirect('detalhes_colecao', colecao_id=colecao_id)

@login_required
def editar_colecao(request, colecao_id):
    colecao = get_object_or_404(Colecao, id=colecao_id, usuario=request.user)
    
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao', '')
        
        if nome:
            colecao.nome = nome
            colecao.descricao = descricao
            colecao.save()
            messages.success(request, f'Coleção "{colecao.nome}" atualizada!')
            return redirect('detalhes_colecao', colecao_id=colecao_id)
        else:
            messages.error(request, 'O nome da coleção é obrigatório.')
    
    context = {
        'colecao': colecao,
    }
    return render(request, 'filmes/editar_colecao.html', context)

@login_required
def excluir_colecao(request, colecao_id):
    colecao = get_object_or_404(Colecao, id=colecao_id, usuario=request.user)
    
    if request.method == 'POST':
        nome_colecao = colecao.nome
        colecao.delete()
        messages.success(request, f'Coleção "{nome_colecao}" excluída!')
        return redirect('listar_colecoes')
    
    context = {
        'colecao': colecao,
    }
    return render(request, 'filmes/excluir_colecao.html', context)