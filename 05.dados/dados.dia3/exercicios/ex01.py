# Em um software monitor, o qual verifica a resiliência de outro software,
# precisamos saber o tempo máximo que um software permaneceu sem
# instabilidades. Para isto, a cada hora é feito uma requisição ao sistema
# para verificamos se está tudo bem.
# Supondo um array que contenha os estados coletados por nosso software,
#  calcule quanto tempo máximo que o servidor permaneceu sem instabilidades.

# 1 - OK
# 0 - Instabilidades


def stability_check(arr: list):
    first_stability = arr.index(1)
    count = 1
    for i in range(first_stability, len(arr)):
        if arr[i] == arr[i + 1]:
            count += 1
        elif arr[i] != arr[i + 1]:
            break
    return count


valores_coletados = [0, 1, 1, 1, 0, 0, 1, 1]
print(stability_check(valores_coletados))

valores_coletados = [1, 1, 1, 1, 0, 0, 1, 1]
print(stability_check(valores_coletados))

# O(n)
