from pokemon import *
import random
import time
import copy

NAMES = [
    "John", "William", "James", "Michael", "Robert", "David",
    "Joseph", "Daniel", "Matthew", "Andrew", "Gary"
]

class Person:
    def __init__(self, name=None, pokemons=None, money=100, pokeballs=1):
        self.name = name if name else random.choice(NAMES)
        self.pokemons = pokemons if pokemons else []
        self.money = money
        self.pokeballs = pokeballs

    def show_pokemons(self):
        if not self.pokemons:
            print(f"{self} Don't have pokemons")
            return
        
        print(f'{self} Pokemons:')
        for index, poke in enumerate(self.pokemons):
            print(f' {index + 1} - {poke}')

    def choose_pokemon(self):
        raise NotImplementedError('Implement the method in sub-classes')

    def battle(self, enemy):
        money_acumulator = 0
        print(f'\n⚔️ {self} started a battle with {enemy}!')
        time.sleep(1)

        player_team = self.pokemons
        enemy_team = enemy.pokemons

        self.show_pokemons()
        time.sleep(1)

        enemy.show_pokemons()
        time.sleep(1.5)

        while any(p.is_alive for p in player_team) and \
            any(p.is_alive for p in enemy_team):

            print("\n━━━━━━━━ NEW ROUND ━━━━━━━━")
            time.sleep(0.8)

            player_pokemon = self.choose_pokemon()
            time.sleep(0.5)

            enemy_pokemon = enemy.choose_pokemon()
            time.sleep(1)

            while player_pokemon.is_alive and enemy_pokemon.is_alive:

                print(f"\n⚔️ {player_pokemon} VS {enemy_pokemon}")
                time.sleep(1)

                player_pokemon.attack(enemy_pokemon)
                time.sleep(1.2)

                if not enemy_pokemon.is_alive:
                    print(f'\n💀 {enemy_pokemon} fainted!')
                    money_acumulator += enemy_pokemon.level
                    enemy_team.remove(enemy_pokemon)
                    time.sleep(1)
                    break

                enemy_pokemon.attack(player_pokemon)
                time.sleep(1.2)

                if not player_pokemon.is_alive:
                    print(f'\n💀 {player_pokemon} fainted!')
                    player_team.remove(player_pokemon)
                    time.sleep(1)
                    break

        time.sleep(1)

        if player_team:
            print(f'\n🏆 {self} WON THE BATTLE!')
            self.earn_money(money_acumulator)
        else:
            print(f'\n🏆 {enemy} WON THE BATTLE!')

    def __str__(self):
        return self.name

class Player(Person):
    person_type = 'player'
    
    def catch_pokemon(self, poke):
        self.pokemons.append(poke)
        print(f'✨ {self} catched {poke} ✨!')

    def choose_pokemon(self):
        self.show_pokemons()
        
        while True:
            choice = input('Choose your pokemon: ')
            try:
                choice = int(choice) - 1
                if 0 <= choice < len(self.pokemons):
                    pokemon_choosed = self.pokemons[choice]

                    if not pokemon_choosed.is_alive:
                        print('This pokemon fainted!')
                        continue

                    print(f'{self} choosed {pokemon_choosed}')
                    return pokemon_choosed
                print('Invalid Choice')
            except ValueError:
                print('Invalid Choice')

    def show_money(self):
        print(f'You have 🪙 {self.money} coins ')

    def earn_money(self, amount):
        self.money += amount
        print(f'Earned 🪙 {amount} coins')
        time.sleep(1)
        self.show_money()
    
    def buy_pokeballs(self, amount):
        pokeballs_cost = 10 * int(amount)
        if self.money >= pokeballs_cost:
            self.money -= pokeballs_cost
            self.pokeballs += int(amount)
            print(f'Now you have {self.pokeballs} pokeballs')
            return
        print('Not enought money')
        self.show_money()
        
    def explore(self):
        poke_appear_chance = random.random() <= 0.3
        if poke_appear_chance:
            tries = 0
            random_poke = copy.deepcopy(random.choice(POKEMONS))
            print(f'A sauvage pokemon appeared! {random_poke}')

            while True:
                print(f'You have {self.pokeballs} pokeballs')
                choice = input('Catch it? [Y]/[N]: ').upper()
                if self.pokeballs > 0:
                    match choice:
                        case 'Y':
                            if tries >= 3:
                                print(f'{random_poke} ran away!')
                                break
                            catch_chance = random.random() <= 0.5
                            print('Throwing pokeball...')
                            time.sleep(0.5)
                            print('Tick...')
                            time.sleep(0.8)
                            print('Tick...')
                            time.sleep(0.8)
                            print('Tick...')
                            if catch_chance:
                                self.catch_pokemon(random_poke)
                                self.show_pokemons()
                                self.pokeballs -= 1
                                break
                            else:
                                print(f'{random_poke} escaped from pokeball!')
                                tries += 1
                                self.pokeballs -= 1
                                continue
                        case 'N':
                            print('Leaving from here...')
                            break
                        case _:
                            print('Invalid option')
                            continue
                else:
                    print('Not enough pokeballs!')
                    response = input('Want to buy pokeballs? [Y]/[N]: ').upper()
                    match response:
                        case 'Y':
                            self.show_money()
                            print('Pokeball costs 10 Coins')
                            amount = input('Amount of pokeballs: ')
                            self.buy_pokeballs(amount)
                            continue
                        case 'N':
                            print('Ok, leaving from here...')
                            break
                        case _:
                            print('Invalid Option')
                            continue
        else:
            print('This exploration yielded nothing.')

class Enemy(Person):
    person_type = 'enemy'

    def __init__(self, name=None, pokemons=None):
        if not pokemons:
            pokemons = copy.deepcopy(random.sample(POKEMONS,
                                    random.randint(1, 3)))
        super().__init__(name, pokemons)

    def choose_pokemon(self):
        alive_pokemons = [
            pokemon for pokemon in
            self.pokemons if pokemon.is_alive
        ]
        pokemon_choosed = random.choice(alive_pokemons)
        print(f'{self} choosed {pokemon_choosed}')
        return pokemon_choosed

if __name__ == '__main__':
    p1 = Player("Rafael", [FirePokemon('Charmander'), POKEMONS[1]])
    e1 = Enemy()
    while True:
        p1.explore()