# Union d'ensembles de nombres

#### ⚠️

Gardez le fichier `documents/pokemons` bien précieusement, il est nécéssaire pour la bonne execution du programme.

## Énoncé

Vous pouvez le trouver [ici](https://primers.xyz/3) 👀

## Solution

#### Lancement 🚀

Collez la commande suivante dans votre terminal:  
`rm -f team && ./execute_algo > team`

#### Algorithme 🤔💭💫

Voici ma solution:

1 - Récupérer le contenu du fichier 'documents/pokemons' dans une liste, de telle sort que chaque élément de la liste soit une ligne du fichier.  
2 - Construction d'un tableau de Pokémons (structure: name (string), attacks (int array)) à partir de cette liste.  
3 - Construction d'un tableau d'integer à partir des attaques des pokémons. Voici un exemple:

        Nous avons 4 pokémons:  1- Rosalie  (2 , 15, 22),
                                2- Drakofeu (15, 35, 76),
                                3- Mewtow   (35, 76, 98),
                                4- Pikatchu (2 , 15, 22, 32).

        Voici à quoi ressemblera le tableau:
                    -------------------------
                    | \ | 1  | 2  | 3  | 4  |
                    -------------------------
                    | 1 | -1 | 5  | 6  | 1  |
                    | 2 | -1 | -1 | 4  | 6  |
                    | 3 | -1 | -1 | -1 | 7  |
                    | 4 | -1 | -1 | -1 | -1 |
                    -------------------------

        Chaque case contient le nombre d'attaques formé par l'union des attaques des pokémons d'index ligne et colonne.
        Ici, dans la case 2-4, nous avons 6 car l'union des attaques des pokémons d'index 2 et 4 (Drakofeu et Pikatchu)  
        est { 2, 15, 22, 32, 35, 76 }.
        Chaque case située sur la diagonale ou en dessous contient -1, puisque nous ne les utiliserons pas par la suite.  

4 - Itération sur chaque case différente de -1 du tableau des attaques:

    a - Recherche de la meilleure combinaison:
        i   -   Initialisation d'une nouvelle équipe, dont le premier élément est le numéro de la ligne actuelle  
                (autrement dit, l'index du pokémon).
        ii  -   Itération sur l'intervalle [1, 5]:
                    j   -   Lister les index des pokémons disponibles (tous ceux qui ne sont encore dans l'équipe).
                    jj  -   Recherche d'un nouveau pokémon tel que la somme du nombre d'éléments de chacune des unions  
                            entre ses attaques et celles des pokémons de la team soit maximum.  
                            C'est ce à quoi le tableau des attaques nous sert.
                    jjj -   Insertion de l'index de ce pokémon dans la team.

    b - Comparaison de la nouvelle combinaison avec celle de référence:
        Si la nouvelle est meilleure: alors elle devient la référence.
        Sinon, la référence n'est pas modifée.

5 - Afficher les noms des pokémons de la team.
