def reverse(lista: list):
    return lista if len(lista) <= 1 else [lista[-1], *reverse(lista[:-1])]


print(reverse([1, 2, 3, 4, 5]))
