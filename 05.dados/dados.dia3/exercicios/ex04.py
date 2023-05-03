# Você têm dois arrays de números inteiros que representam:

# I - instantes de entrada e saídas em uma biblioteca
# II - um número que represente um instante a ser buscado.

# Retorne quantas pessoas estudantes estão na biblioteca naquele instante.
# Considere que todo estudante entrou e saiu da biblioteca.


# def students_in_instant(arrivals: list, departures: list, time_instant: int):
#     return len(
#         [
#             True
#             for i in range(len(arrivals))
#             if arrivals[i] <= time_instant <= departures[i]
#         ]
#     )


def students_in_instant(arrivals, departures, time_instant):
    return sum(
        arrival <= time_instant <= departure
        for arrival, departure in zip(arrivals, departures)
    )


entradas = [1, 2, 3]
saidas = [3, 2, 7]
instante_buscado = 4

print(students_in_instant(entradas, saidas, instante_buscado))
