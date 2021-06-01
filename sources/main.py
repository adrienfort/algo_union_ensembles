from .pokemon import Pokemon
from .find_best_team import find_best_team


# @params - attack_1 (int array)
#           attack_2 (int array)
# Compare these arrays and count the number of uncommon values.
# @return - int
def compare_attacks(attacks_1, attacks_2):
    len_1 = len(attacks_1)
    len_2 = len(attacks_2)
    counter = 0

    for i in range(len_1):
        if attacks_2.count(attacks_1[i]) == 0:
            counter += 1
    for i in range(len_2):
        if attacks_1.count(attacks_2[i]) == 0:
            counter += 1
    return counter


# @params - list_pokemons (str array)
#           nb_pokemons (int)
# Build an array of Pokemons.
# @return - array of Pokemons
def get_pokemons_from_list(list_pokemons, nb_pokemons):
    pokemons = []
    tab = []
    str_attacks = []
    int_attacks = []

    for i in range(nb_pokemons):
        tab = list_pokemons[i].rstrip('\n').split(',', 1)
        str_attacks = tab[1].split(',')
        int_attacks = list(map(int, str_attacks))
        int_attacks.sort()
        pokemons.append(Pokemon(name=tab[0], attacks=int_attacks))
    return pokemons


# @params - pokemons (Pokemons array)
#           nb_pokemons (int)
# Build a tab filling by the number of uncommon attacks between two pokemons.
# @return - array of int arrays
def get_attacks_diff_tab(pokemons, nb_pokemons):
    tab = [[0 for i in range(nb_pokemons)] for j in range(nb_pokemons)]
    attacks_1 = []
    attacks_2 = []

    for row in range(nb_pokemons):
        attacks_1 = pokemons[row].attacks
        for col in range(nb_pokemons):
            attacks_2 = pokemons[col].attacks
            if row == col:
                tab[row][col] = -1
            else:
                tab[row][col] = compare_attacks(attacks_1, attacks_2)
    return tab


# @params - /
# Open and read the 'documents/pokemons' file.
# Stock its lines in a list.
# Build an array of Pokemons from the list.
# Launch the algorithme and print its results.
# @return - /
def main():
    file = open('documents/pokemons')
    list_pokemons = file.readlines()
    nb_pokemons = len(list_pokemons)
    pokemons = []
    attacks_tab = []
    team = []

    if nb_pokemons < 6:
        print("You must have at least 6 pokemons")
        return 84
    pokemons = get_pokemons_from_list(list_pokemons, nb_pokemons)
    attacks_tab = get_attacks_diff_tab(pokemons, nb_pokemons)
    team = find_best_team(pokemons, nb_pokemons, attacks_tab)
    print(team)
    # for i in range(6):
    #     print(team[i])
    return 0
