from copy import deepcopy


# @params - attacks_tab (array of int arrays)
#           nb_pokemons (int)
#           row (int)
#           col (int)
# Find the best team starting from (row, col).
# @return - int array
def get_best_team(attacks_tab, nb_pokemons, row, col):
    return []


# @params - pokemons (Pokemon array)
#           team_1 (int array)
#           team_2 (int array)
# Calculate the number of different attacks of team_1 and team_2.
# Compare it.
# @return - -1 if team_1 better, 0 if equal, 1 if team_2 better
def compare_teams(pokemons, team_1, team_2):
    return 0


# @params - pokemons (Pokemons array),
#           nb_pokemons (int)
#           attacks_tab (array of int arrays)
# Get the names of the pokemons in order to have the most complete team.
# @return - str array
def find_best_team(pokemons, nb_pokemons, attacks_tab):
    team_1 = []
    team_2 = []

    for row in range(nb_pokemons):
        for col in range(nb_pokemons):
            if row != col:
                team_2 = get_best_team(attacks_tab, nb_pokemons, row, col)
                if compare_teams(pokemons, team_1, team_2) > 0:
                    team_1 = deepcopy(team_2)
    return team_1
