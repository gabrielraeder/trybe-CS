def substitute(numbers: list):
    last_position = len(numbers) - 1
    for i in range(last_position - 1, -1, -1):
        if numbers[i] < numbers[i + 1]:
            numbers[i] = numbers[i + 1]


lista = [2, 3, 4, 3, 5, 2, 1]
print(lista)

substitute(lista)

print(lista)
