import requests
import json



class pokemonClass:

    def __init__(self, url, nome, habilidades, tipo, peso):
        self.nome = nome
        self.url = url
        self.habilidades = habilidades
        self.peso = peso
        self.tipo = tipo

    def __str__(self):

      return  f'Nome:{self.nome} - url: {self.url} - tipo:{self.tipo} - Habilidades: {self.habilidades} - Peso: {self.peso}'  



def url_pokemon(url: str) -> object:
      pokemon = requests.get(url)

      return pokemon   


def pegar_pokemon():
    pokeList = requests.get('https://pokeapi.co/api/v2/pokemon/')

    resultadosPokemons = pokeList.json()['results']
    
    pokemonList = []
    for pokemon in resultadosPokemons:
        url = pokemon['url']
        nome = pokemon['name']
        pokeobjeto =  url_pokemon(pokemon['url']).json()
        habilidades = [i['ability']['name'] for i in pokeobjeto['abilities']] 
        peso = pokeobjeto['weight']
        tipo = [i['type']['name'] for i in pokeobjeto['types']]

        pokemonList.append(pokemonClass(url,nome,habilidades,tipo,peso))


    return pokemonList



pokemonObjeto = pegar_pokemon()

for pokedex in pokemonObjeto:
  print(pokedex)








