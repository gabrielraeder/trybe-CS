# Exercício 3 Execute os algoritmos de ordenação por seleção e inserção,
# para as entradas de dados ordenadas, inversamente ordenadas e aleatórias.
# Em seguida, compare-os. Faça testes para entradas
# de tamanho 10.000, 100.000, 1.000.000.
from cronometro import Cronometro

from random import shuffle


def selection_sort(numbers: list):
    length = len(numbers)
    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length):
            if numbers[min_index] > numbers[j]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers


def insertion_sort(numbers):
    length = len(numbers)
    for index in range(1, length):
        key = numbers[index]
        previous = index - 1
        while previous >= 0 and numbers[previous] > key:
            numbers[previous + 1] = numbers[previous]
            previous -= 1
        numbers[previous + 1] = key
    return numbers


ordenados = list(range(100))
inversamente_ordenados = list(reversed(range(100)))
aleatorios = ordenados[:]  # copia dos ordenados
shuffle(aleatorios)  # embaralha eles
with Cronometro("selection_sort - aleatorios"):
    a = selection_sort(aleatorios)

with Cronometro("insertion_sort - aleatorios"):
    a = insertion_sort(aleatorios)

with Cronometro("selection_sort - inversamente_ordenados"):
    a = selection_sort(inversamente_ordenados)

with Cronometro("insertion_sort - inversamente_ordenados"):
    a = insertion_sort(inversamente_ordenados)
