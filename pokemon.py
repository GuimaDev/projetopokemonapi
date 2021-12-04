import requests
import json

from requests import api


class pokemonClass:
    def __init__(self, nome, habilidades, peso):
        self.nome = nome
        self.habilidades = habilidades
        self.peso = peso


def pegar_pokemon():
    pokeList = requests.get('https://pokeapi.co/api/v2/pokemon/')

    resultadospokemons = pokeList.json()['results']
    listafiltradapokemons = []

    for pokemon in resultadospokemons:
        listafiltradapokemons.append(pokemon)

    for pokeobjeto in listafiltradapokemons:
        pokeresulto = requests.get(pokeobjeto['url'])
        pokemon = pokemonClass(pokeresulto.json()['species']['name'], pokeresulto.json()[
                               'abilities'], pokeresulto.json()['weight'])

        print(
            f'Nome: {pokemon.nome} -  Habilidades: {pokemon.habilidades} - Peso: {pokemon.peso} - ')


pegar_pokemon()
