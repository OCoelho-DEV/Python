class Pokemon:
    def __init__(self, specie, name=None, level=1):
        self.specie = specie
        self.name = name if name else specie
        self.level = level

    def __str__(self):
        aux = '' if self.name == self.specie else f'({self.specie})'
        return f'[{self.poke_type}] {self.name}{aux} Lv.{self.level}'
    
    def attack(self, enemy):
        print(f'{self} uses {self.attack_name} on {enemy}!')

class EletricPokemon(Pokemon):
    poke_type = 'Electric'
    attack_name = 'thunderbolt'
    
class FirePokemon(Pokemon):
    poke_type = 'Fire'
    attack_name = 'fireball'
    
class WaterPokemon(Pokemon):
    poke_type = 'Water'
    attack_name = 'water jet'
    
my_poke = FirePokemon('Charmander', 'Rafa')
other_poke = EletricPokemon('Pikachu')
my_friend_pokemon = WaterPokemon('Mudkip', level=50)
my_poke.attack(my_friend_pokemon)
my_friend_pokemon.attack(other_poke)
other_poke.attack(my_poke)
