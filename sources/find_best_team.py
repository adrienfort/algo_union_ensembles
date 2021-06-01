# @params - nb_pokemons (int)
#           team (int array)
# Get the indexs of unchoosen pokemon.
# @return - int array
def get_options(nb_pokemons, team):
    options = []

    for i in range(nb_pokemons):
        if team.count(i) == 0:
            options.append(i)
    return options


# @params - attacks_cpy (array of int arrays)
#           team (int array)
#           options (int array)
# Compare options and choose the best.
# @return - index of the best pokemon to choose
def get_best_move(attacks_tab, team, options):
    move = 0
    move_index = 0
    counts = []
    count = 0

    for i in range(len(options)):
        count = 0
        for j in range(len(team)):
            count += attacks_tab[team[j]][options[i]]
        counts.append(count)
    for k in range(len(counts)):
        if (counts[k] > move):
            move = counts[k]
            move_index = options[k]
    return move_index


# @params - attacks_tab (array of int arrays)
#           nb_pokemons (int)
#           row (int)
#           col (int)
# Find the best team starting from (row, col).
# @return - int array
def get_best_team(attacks_tab, nb_pokemons, row, col):
    team = []
    options = []
    move = 0

    team.append(row)
    for i in range(1, 6):
        options = get_options(nb_pokemons, team)
        move = get_best_move(attacks_tab, team, options)
        team.append(move)
    return team


# @params - pokemons (Pokemon array)
#           team (int array)
# Calculate the union of the pokemons's attacks present in the team
# @return - int
def get_team_union(pokemons, team):
    attacks = []
    attack = 0

    for i in range(len(team)):
        pokemon = pokemons[team[i]]
        for j in range(len(pokemon.attacks)):
            attack = pokemon.attacks[j]
            if (attacks.count(attack) == 0):
                attacks.append(attack)
    return len(attacks)


# @params - pokemons (Pokemon array)
#           team_1 (int array)
#           team_2 (int array)
# Calculate the number of different attacks of team_1 and team_2.
# Compare it.
# @return - -1 if team_1 better, 0 if equal, 1 if team_2 better
def compare_teams(pokemons, team_1, team_2):
    union_1 = get_team_union(pokemons, team_1)
    union_2 = get_team_union(pokemons, team_2)
    comparaison = 1

    if union_1 > union_2:
        comparaison = -1
    elif union_1 == union_2:
        comparaison = 0
    return comparaison


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
                    team_1 = team_2.copy()
    return team_1
