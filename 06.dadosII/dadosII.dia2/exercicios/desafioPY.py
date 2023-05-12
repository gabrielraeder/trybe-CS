lista = [3, 4, 7, 4, 3]


def pairs(numbers: list[int]):
    somas = {}
    for index in range(len(numbers) - 1):
        soma = numbers[index] + numbers[index + 1]
        if soma not in somas:
            somas[soma] = [(index, index + 1)]
        else:
            if index != somas[soma][-1][1]:
                somas[soma].append((index, index + 1))
    for item in somas:
        if len(somas[item]) == 2:
            return [(numbers[i1], numbers[i2]) for i1, i2 in somas[item]]
    return -1


print(pairs(lista))
