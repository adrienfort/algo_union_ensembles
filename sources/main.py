from .pokemon import Pokemon


def get_pokemons_from_list(list_pokemons, nb_pokemons):
    pokemons = []
    tab = ""

    for i in range(nb_pokemons):
        tab = list_pokemons[i].split(',', 1)
        pokemons.append(Pokemon(name=tab[0], attacks=tab[1]))
    return pokemons


def main():
    file = open('documents/pokemons')
    list_pokemons = file.readlines()
    nb_pokemons = len(list_pokemons)
    pokemons = []

    if nb_pokemons < 6:
        print("You must have at least 6 pokemons")
        return 84
    pokemons = get_pokemons_from_list(list_pokemons, nb_pokemons)
    for i in range(nb_pokemons):
        print(pokemons[i].name)
    return 0
