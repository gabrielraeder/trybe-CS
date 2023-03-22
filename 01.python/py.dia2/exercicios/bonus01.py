import random
import json


def read_pokemons():
    with open("pokemons.json") as file:
        pokemons = json.load(file)["results"]
        poke_names = [pokemon["name"] for pokemon in pokemons]
    return poke_names


def choose_pokemon():
    pokemons = read_pokemons()
    pokemon = random.choice(pokemons)
    return pokemon


def which_poke():
    pokemon = choose_pokemon()
    print(pokemon)
    counter = 0
    while counter < len(pokemon):
        print(pokemon[:counter])
        counter += 1
        guess = input("Quem é esse pokemon? ").capitalize()
        if guess == pokemon:
            print("Acertou!")
            break
        else:
            print("Tente novamente")
    if guess != pokemon:
        print(f"Falhou! O pokemon era {pokemon}")


which_poke()
