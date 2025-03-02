import requests

def buscar_filme(termo, api_key):
    
    url = f"http://www.omdbapi.com/?apikey={api_key}&s={termo}&type=movie"
    
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(f"Erro ao buscar filmes: {e}")
        return {"Response": "False", "Error": "Erro ao conectar com a API OMDB"}

def obter_detalhes_filme(imdb_id, api_key):
    
    url = f"http://www.omdbapi.com/?apikey={api_key}&i={imdb_id}&plot=full"
    
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(f"Erro ao obter oss detalhes: {e}")
        return {"Response": "False", "Error": "Erro ao conectar com a API"}