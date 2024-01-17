import pandas as pd

file = pd.read_csv("data/parcours_explorateurs.csv")

"""
Une liste qui contient les noeuds de départ (noeud_amont) <= filtrer un dataframe
Une liste qui contient les noeuds d'arrivée (noeud_aval) <= filtrer un dataframe
Un dictionnaire qui associe des noeuds amonts à des nouds avals (noeud_amont, noeud_aval)
"""

array_starting_node = file[file["type_aretes"] == "depart"]["noeud_amont"].values
array_arrival_node = file[file["type_aretes"] == "arrivee"]["noeud_aval"].values
dict_upstream_downstream = {
    row["noeud_amont"]: row["noeud_aval"] for _, row in file.iterrows()
}

for starting_node in array_starting_node:
    """
    Chaque itération de cette boucle for permet de construire le chemin d'un explorateur, pour chacun des explorateurs :
    1. On part du noeud de départ
    2. On récupère le noeud aval associé au noeud amont
    3. On ajoute le noeud aval à la fin du chemin
    4. On répète les étapes 2 et 3 jusqu'à ce que le noeud aval soit un noeud d'arrivée
    5. On affiche le chemin
    6. On passe à l'explorateur suivant
    """
    current_path = [starting_node]
    while current_path[-1] not in array_arrival_node:
        current_node = current_path[-1]
        next_node = dict_upstream_downstream[current_node]
        current_path.append(next_node)
    print(current_path)
