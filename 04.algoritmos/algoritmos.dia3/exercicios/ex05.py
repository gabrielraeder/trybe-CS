def binary_search_iteractive(numbers, target):
    # definir os índices
    start = 0
    end = len(numbers) - 1

    while (
        start <= end
    ):  # os índices podem ser no máximo iguais, o início não pode ultrapassar
        #  o fim
        mid = (start + end) // 2  # encontro o meio

        if (
            numbers[mid] == target
        ):  # se o elemento do meio for o alvo, devolve a posição do meio
            return mid

        if (
            target < numbers[mid]
        ):  # se o elemento for menor, atualiza o índice do fim
            end = mid - 1
        else:  # caso contrário, atualiza o índice do inicio
            start = mid + 1

    return -1  # Não encontrou? Retorna -1


def binary_search_recursive(arr, target, start, end):
    if end >= start:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            return binary_search_recursive(arr, start, mid - 1, target)

        else:
            return binary_search_recursive(arr, mid + 1, end, target)

    else:
        return -1


numbers = [2, 3, 4, 10, 40]
target = 40

result = binary_search_recursive(numbers, target, 0, len(numbers))
print(f"Elemento encontrado na posição: {result}")
