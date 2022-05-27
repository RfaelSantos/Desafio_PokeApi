import os
import requests

class Pokemon():
    def __init__(self, name, url, weight, abilities, types):
        self.name = name
        self.url = url
        self.weight = weight
        self.abilities = abilities
        self.types = types
        
url = 'https://pokeapi.co/api/v2/pokemon?limit=20&offset=0'

def conectList(url):
    res = requests.get(url)

    if res.status_code == 200:
        return res.json()
    else:
        print('Não possível realizar a conexão!')

def getAbilities(res):  
    ab_list = []
    for i in res['abilities']:
        ab_list.append(i['ability']['name'])
    return ab_list

def getType(res):
    tp_list = []
    for x in res['types']:
        tp_list.append(x['type']['name'])
        return tp_list

def getData(res):
    url = res['url']
    poke = requests.get(url).json()
    name = poke['name']
    abilities = getAbilities(poke)
    types = getType(poke)
    weight = poke['weight']
    pokemon = Pokemon(name, url, weight, abilities, types)
    print('Name: ', pokemon.name)
    print('URL: ', pokemon.url)
    print('Abilities: ', pokemon.abilities)
    print('Types: ', pokemon.types)
    print('Weight: ', pokemon.weight)

res = conectList(url)
print('******************************************************************')
print('********************** LISTA DE POKÉMONS *************************')
print('******************************************************************')
print('\n')

loopControl = 'y'
while loopControl.lower() == 'y':
    for i in range(len(res['results'])):
        print(f"id: {i} - {res['results'][i]['name']}")
    print('\n')

    option = int(input('Digite o id do Pokémon que deseja obter mais informações: '))
    print('\n')

    while option < 0 or option > len(res['results']):
        print('O id digitado não corresponde a lista de pokemons apresentada acima...\n')
        option = int(input('Por favor, digite o id novamente: '))

    getData(res['results'][option])

    loopControl = input("\nDeseja realizar a consulta de um novo Pokémon? digite 'y' para realizar uma nova consulta, ou 'n' para sair do programa: ")
    os.system('cls')




