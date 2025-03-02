<div align="center">
    <h1>CineVerso 🎥</h1>
    <p>Aplicativo web Django para gerenciar coleções de filmes, com integração à API do OMDB.</p>
    <p>
        <a href="#sobre-o-projeto">Sobre o Projeto</a> •
        <a href="#pre-requisitos">Pré Requisitos</a> •
        <a href="#configuracoes">Configurações</a> •
        <a href="#funcionalidades">Funcionalidades</a> •
        <a href="#autor">Autor</a> •
        <a href="#considerações">Considerações</a>
    </p>
    <h2><a id="demo"></a>Demo (LEIA TUDO PARA EXECUTAR) </h2>
    <img alt="GIF" title="GIF do Readme" src="./github/AnimacaoGIF.gif"/>
</div>

## <a id="sobre-o-projeto"></a>Sobre o Projeto

CineVerso é uma aplicação web desenvolvida com Django que permite aos usuários:

- [x] Pesquisar filmes usando a API do OMDB
- [x] Criar coleções personalizadas de filmes
- [x] Gerenciar suas coleções (adicionar/remover filmes, editar detalhes)
- [x] Visualizar informações detalhadas sobre os filmes

## <a id="pre-requisitos"></a>Pré Requisitos

- [x] Python 3.8+
- [x] Django 4.2+
- [x] Requests
- [x] Conexão com a internet para acessar a API do OMDB

## <a id="configuracoes"></a>Configurações


1. Crie uma pasta usando "mkdir" chamada "project"
   ```
   E mova todos os arquivos para a pasta " project "
   ```

2. Crie um ambiente virtual e ative:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
3. Execute: 
   ```
   pip install requests
   (Lembrando sempre de estar na pasta "cd project)
   ```
4. Execute:
   ```
   pip install -r requirements.txt
   pip install django

   ```

5. Execute as migrações:
   ```
   python manage.py migrate
   ```

6. Crie um Usuário:
   ```
   python manage.py createsuperuser
   ```

7. Inicie o servidor:
   ```
   python manage.py runserver
   ```

8. Acesse a aplicação em `http://127.0.0.1:8000`

## <a id="funcionalidades"></a>Funcionalidades

- **Pesquisa de Filmes**: Busca filmes na API do OMDB
- **Coleções Personalizadas**: Crie e gerencie suas próprias coleções de filmes
- **Detalhes dos Filmes**: Visualize informações detalhadas sobre cada filme

## <a id="tecnologias"></a>Tecnologias
- Python
- Django
- HTML
- CSS
- Bootstrap 5
- OMDB API

---

Feito por 👨‍💻 Jonatas Nogueira ❤️