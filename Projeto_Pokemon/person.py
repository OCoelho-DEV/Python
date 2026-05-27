from pokemon import *
import random

NAMES = [
    "John", "William", "James", "Michael", "Robert", "David",
    "Joseph", "Daniel", "Matthew", "Andrew", "Gary"
]

class Person:
    def __init__(self, name=None, pokemons=[]):
        self.name = name if name else random.choice(NAMES)
        self.pokemons = pokemons

    def show_pokemons(self):
        if not self.pokemons:
            print(f"{self} Don't have pokemons")
            return
        
        print(f'{self} Pokemons:')
        for poke in self.pokemons:
            print(f'- {poke}')

    def __str__(self):
        return self.name
    
class Player(Person):
    person_type = 'player'
    
    def catch_pokemon(self, poke):
        self.pokemons.append(poke)
        print(f'{self} catched {poke}!')

class Enemy(Person):
    person_type = 'enemy'

    def __init__(self, name=None, pokemons=[]):
        if not pokemons:
            pokemons = random.sample(POKEMONS, random.randint(1, 3))
        super().__init__(name, pokemons)