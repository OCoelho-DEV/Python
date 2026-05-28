import random

class Pokemon:
    poke_type = "Unknown"
    attack_name = None
    def __init__(self, specie, name=None, level=None):
        self.specie = specie
        self.name = name if name else specie
        self.level = level if level else random.randint(1,100)
        self.damage = self.level * 5
        self.hp = self.level * 15
        self.total_hp = self.hp

    @property
    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        aux = '' if self.name == self.specie else f'({self.specie})'
        return( f'[{self.poke_type}] {self.name}{aux} Lv.{self.level} \
[❤️  HP {self.hp}/{self.total_hp}]')
    
    def attack(self, enemy):
        critical_chance = random.random() <= 0.1
        dodge_chance = random.random() <= 0.15
        total_damage = self.damage
        if critical_chance:
            print("✨ CRITICAL HIT! ✨")
            total_damage *= 2
        
        if dodge_chance:
            print(f'💨 {enemy} dodged the attack!')
            return
        
        enemy.hp -= total_damage
        enemy.hp = max(enemy.hp, 0)

        print(f'{self} uses {self.attack_name} on {enemy}!')
        print(f'💔 {enemy} lost {total_damage} HP ({enemy.hp}/ \
{enemy.total_hp}) ❤️')


class ElectricPokemon(Pokemon):
    poke_type = 'Electric'
    attack_name = 'thunderbolt ⚡'


class FirePokemon(Pokemon):
    poke_type = 'Fire'
    attack_name = 'fireball 🔥'


class WaterPokemon(Pokemon):
    poke_type = 'Water'
    attack_name = 'water jet 💧'


class GrassPokemon(Pokemon):
    poke_type = 'Grass'
    attack_name = 'leaf storm 🍃'


class IcePokemon(Pokemon):
    poke_type = 'Ice'
    attack_name = 'ice shard ❄️'


class RockPokemon(Pokemon):
    poke_type = 'Rock'
    attack_name = 'rock smash 🪨'


class PsychicPokemon(Pokemon):
    poke_type = 'Psychic'
    attack_name = 'mind blast 🧠'


class DarkPokemon(Pokemon):
    poke_type = 'Dark'
    attack_name = 'shadow claw 🌑'


class DragonPokemon(Pokemon):
    poke_type = 'Dragon'
    attack_name = 'dragon breath 🐉'


class FightingPokemon(Pokemon):
    poke_type = 'Fighting'
    attack_name = 'mega punch 👊'


POKEMONS = [

    # FIRE
    FirePokemon("Charmander"),
    FirePokemon("Vulpix"),
    FirePokemon("Growlithe"),
    FirePokemon("Ponyta"),

    # WATER
    WaterPokemon("Squirtle"),
    WaterPokemon("Psyduck"),
    WaterPokemon("Poliwag"),
    WaterPokemon("Magikarp"),

    # ELECTRIC
    ElectricPokemon("Pikachu"),
    ElectricPokemon("Magnemite"),
    ElectricPokemon("Electabuzz"),
    ElectricPokemon("Voltorb"),

    # GRASS
    GrassPokemon("Bulbasaur"),
    GrassPokemon("Oddish"),
    GrassPokemon("Bellsprout"),
    GrassPokemon("Exeggcute"),

    # ICE
    IcePokemon("Lapras"),
    IcePokemon("Jynx"),
    IcePokemon("Snorunt"),

    # ROCK
    RockPokemon("Geodude"),
    RockPokemon("Onix"),
    RockPokemon("Rhyhorn"),

    # PSYCHIC
    PsychicPokemon("Abra"),
    PsychicPokemon("Drowzee"),
    PsychicPokemon("MrMime"),

    # DARK
    DarkPokemon("Umbreon"),
    DarkPokemon("Houndour"),

    # DRAGON
    DragonPokemon("Dratini"),
    DragonPokemon("Bagon"),

    # FIGHTING
    FightingPokemon("Machop")
]