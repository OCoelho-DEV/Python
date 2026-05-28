import random

class Pokemon:
    poke_type = "Unknown"
    def __init__(self, specie, name=None, level=None):
        self.specie = specie
        self.name = name if name else specie
        self.level = level if level else random.randint(1,100)

    def __str__(self):
        aux = '' if self.name == self.specie else f'({self.specie})'
        return f'[{self.poke_type}] {self.name}{aux} Lv.{self.level}'
    
    def attack(self, enemy):
        print(f'{self} uses {self.attack_name} on {enemy}!')

class ElectricPokemon(Pokemon):
    poke_type = 'Electric'
    attack_name = 'thunderbolt'
    
class FirePokemon(Pokemon):
    poke_type = 'Fire'
    attack_name = 'fireball'
    
class WaterPokemon(Pokemon):
    poke_type = 'Water'
    attack_name = 'water jet'

POKEMONS = [
    FirePokemon("Charmander"),
    FirePokemon("Vulpix"),
    WaterPokemon("Squirtle"),
    WaterPokemon("Psyduck"),
    ElectricPokemon("Pikachu"),
    ElectricPokemon("Magnemite")
]