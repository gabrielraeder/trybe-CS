listaA = [1, 2, 3, 4, 5, 6]
listaB = [4, 5, 6, 7, 8, 9]


def intersection(listaA, listaB):
    intersect = []
    for item in listaA:
        if item in listaB:
            intersect.append(item)
    return intersect


print(intersection(listaA, listaB))
