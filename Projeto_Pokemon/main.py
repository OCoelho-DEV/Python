from pokemon import *
from person import *
import os

def choose_starter_pokemon(player: Player):
    print(f"Hello, {player}! Now you can choose the Pokémon \
that will accompany you on this journey!")
    
    pikachu = ElectricPokemon('Pikachu', level=1)
    charmander = FirePokemon('Charmander', level=1)
    squirtle = WaterPokemon('Squirtle', level=1)

    print('You have 3 choices:')
    print(f'1 - {pikachu}')
    print(f'2 - {charmander}')
    print(f'3 - {squirtle}')

    starters = {
        '1': pikachu,
        '2': charmander,
        '3': squirtle
    }
    while True:
        choice = input('Choose your pokemon: ')
        if choice in starters:
            os.system('cls' if os.name == 'nt' else 'clear')
            player.catch_pokemon(starters[choice])
            break
        else:
            print('Invalid choice')

p1 = Player("Rafael")
choose_starter_pokemon(p1)
p1.show_pokemons()