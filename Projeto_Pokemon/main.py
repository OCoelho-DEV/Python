from pokemon import *
from person import *
import os
import pickle

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

def save_game(player):
    try:
        with open('Projeto_Pokemon/database.db', 'wb') as file:
            pickle.dump(player, file)
            print('Saved game with success')
    except Exception as error:
        print('Error at save game:', error)

def load_game():
    try:
        with open('Projeto_Pokemon/database.db','rb') as file:
            player = pickle.load(file)
            print('Loaded player with succes')
            return player
    except:
        print('Error at load game:')


if __name__ == "__main__":
    print('-----------------------------------------')
    print("Welcome to the Pokémon Terminal RPG")
    print('-----------------------------------------')
    player = load_game()
    if not player:
        name = input("Hello, what is your name: ")
        player = Player(name)

        print(
            f"Hello {player}, this is a world inhabited by Pokémon. "
            "From now on, your mission is to become a Pokémon Master!"
        )

        print(
            "Catch as many Pokémon as you can and battle your enemies."
        )

        player.show_money()

        if player.pokemons:
            print("I can see you already have some Pokémon.")
            player.show_pokemons()

        else:
            print(
                "You don't have any Pokémon yet, so you need to choose one."
            )

            choose_starter_pokemon(player)

        print(
            "Great! Now that you have your first Pokémon, "
            "face your childhood arch-rival Gary!"
        )

        gary = Enemy(
            name="Gary",
            pokemons=[WaterPokemon("Squirtle", level=1)]
        )

        player.battle(gary)
        save_game(player)

    while True:
        print("--------------------------------------")
        print("What would you like to do?")
        print("1 - Explore the world")
        print("2 - Battle an enemy")
        print("3 - View Pokédex")
        print("4 - Buy Pokeballs")
        print("0 - Exit game")
        if player.money == 0 and player.pokeballs == 0 and \
            not player.pokemons:
            print('You lost all!')
            player.earn_money(100)
            print('Blessed by god!!!')
        choice = input("Your choice: ")

        match choice:

            case "0":
                print("Closing the game...")
                break

            case "1":
                player.explore()
                save_game(player)

            case "2":
                random_enemy = Enemy()
                player.battle(random_enemy)
                save_game(player)

            case "3":
                player.show_pokemons()
            
            case "4":
                player.show_money()
                print('Pokeball costs 10 Coins')
                amount = input('Amount of pokeballs: ')
                player.buy_pokeballs(amount)
                save_game(player)

            case _:
                print("Invalid choice")