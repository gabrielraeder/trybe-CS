clara = [0, 1, 5, 9, 10]
# nota de partida: 5
# redutor: 1
# pt: 4

marco = [0, 2, 8, 9, 10]
# nota de partida: 8
# redutor: 2
# pt individual: 6

# Quem ganhou: Marco

entrada = {"Clara": clara, "Marco": marco}


def blefe(entry):
    players = list(entry.keys())
    dict_sets = {item: set(entry[item]) for item in entry}
    intersection = dict_sets[players[0]].intersection(dict_sets[players[1]])
    for i in intersection:
        dict_sets[players[0]].discard(i)
        dict_sets[players[1]].discard(i)
    player1 = max(dict_sets[players[0]]) - min(dict_sets[players[0]])
    player2 = max(dict_sets[players[1]]) - min(dict_sets[players[1]])
    if player1 == player2:
        return None
    return players[0] if player1 > player2 else players[1]


print(blefe(entrada))
