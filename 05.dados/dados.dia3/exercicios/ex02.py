# Em um jogo de baralho, as cartas estão representadas por um array numérico.
# Para iniciar o jogo, devemos embaralhar as cartas. Faremos isto dividindo
# uma porção de cartas em 2 e depois mesclando as duas porções.
# from random import choice


# def shuffle(arr):
#     mid = len(arr) // 2
#     first = arr[:mid]
#     second = arr[mid:]
#     shuffled = []
#     while len(first) > 0 and len(second) > 0:
#         first_choice = choice(first)
#         second_choice = choice(second)
#         shuffled.append(first_choice)
#         shuffled.append(second_choice)
#         first.remove(first_choice)
#         second.remove(second_choice)
#     return shuffled


def shuffle(items):
    answer = []
    div_cards_by_two = len(items) // 2
    for offset in range(div_cards_by_two):
        answer.extend(items[offset::div_cards_by_two])
    return answer


cartas = [1, 4, 4, 7, 6, 6]
print(shuffle(cartas))
