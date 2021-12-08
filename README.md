# projetopokemonapi
Projeto Desafio Dev Junior Python
 
# Eai tudo certo?
 
## Me Felipe Guimarães
 
Aspirante a Desenvolvedor Python em busca de oportunidades para crescer na àrea de Programação.
 
 
Nesse projeto busquei aplicar meus conhecimetos sobre a linguagem para acessar a api "https://pokeapi.co/api/v2/" para obter os dados 
( NOME; URL,tipo, habilidade e peso) dos 20 primeiros pokemons, através da classe 'PokemonClass' armazenada nos objetos interados nas funções pegar_pokemon e 
url_pokemon. através de for varrendo dentro do array 'Results' trazendo informações via terminal. Sei que é o inicio dessa jornada! CATCH UP! 


## PokemonClass:
  - Classe criada com duas funções ' def __init__(self, url, nome, habilidades, tipo, peso):' e def __str__(self):
   
  - FUNÇÃO def__init__(): objetos criados para serem populados com dados da API
   
 ## - FUNÇÃO def __str__(self):
      retorno dos objetos em string
   
## -  FUNÇÃO: def get_pokemon(url: str) -> object:
       retorna url dentro de 'Results' (lista da primeira conexão com https://pokeapi.co/api/v2/) onde ficam informações dos Pokémons.
   
 ## -  FUNÇÃO def pegar_pokemon(): 
       Conexão com def "https://pokeapi.co/api/v2/", filtra os dados 'Results', onde no primeiro laço FOR filtra as informações de cada pokemon agrupando em uma  lista vazia ' PokemonList'após varrer todo o array returna a lista dos dados agrupados.
   
## - " for pokedex in pokemonObjeto:
  print(pokedex)" listamos todas as posições da lista com um ultimo laço FOR imprimindo no terminal os dados dos pokemons atrelados aos objetos:
   
 ##  - Exemplo: 
   ' Nome: bulbasaur - url: https://pokeapi.co/api/v2/pokemon/1/ - tipo:['grass', 'poison'] - Habilidades: ['overgrow', 'chlorophyll'] - Peso: 69'
   
    
   
  Mais informações: contato.felipeguimaraes@gmail.com/ https://github.com/GuimaDev/

- Obrigado por Visitar meu Repositório!
 

