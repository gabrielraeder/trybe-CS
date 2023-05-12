class Conjunto:
    def __init__(self) -> None:
        self._set = [False for i in range(11)]

    def __str__(self):
        string = "{ "
        for i in range(len(self._set)):
            if i == len(self._set) - 1:
                string += f"{self._set[i]} "
            else:
                string += f"{self._set[i]}, "
        string += "}"
        return string

    def __contains__(self, item):
        return self._set[item]

    def add(self, item):
        self._set[item] = True

    def union(self, conjunto_b):
        new_conjunto = Conjunto()
        for i in range(len(self._set)):
            if self._set[i] is True or conjunto_b._set[i] is True:
                new_conjunto.add(i)
        return new_conjunto

    def intersection(self, conjunto_b):
        new_conjunto = Conjunto()
        for i in range(len(self._set)):
            if self._set[i] is True and conjunto_b._set[i] is True:
                new_conjunto.add(i)

        return new_conjunto

    def difference(self, conjunto_b):
        new_conjunto = Conjunto()
        for index in range(len(self._set)):
            if self._set[index] and not conjunto_b._set[index]:
                new_conjunto.add(index)

        return new_conjunto

    def issubset(self, conjunto_b):
        for i in range(len(self._set)):
            if self._set[i] is True and conjunto_b._set[i] is False:
                return False
        return True

    def issuperset(self, conjunto_b):
        for i in range(len(conjunto_b._set)):
            if conjunto_b._set[i] is True and self._set[i] is False:
                return False
        return True


if __name__ == "__main__":
    # conjunto = Conjunto()
    # conjunto.add(0)
    # conjunto.add(10)
    # conjunto.add(100)
    # conjunto.add(1000)

    # UNION
    # conjuntoA = Conjunto()
    # for i in range(10):
    #     conjuntoA.add(i)
    # conjuntoB = Conjunto()
    # for i in range(10, 20):
    #     conjuntoB.add(i)

    # union = conjuntoA.union(conjuntoB)
    # print(union)

    # INTERSECTION
    # conj1 = Conjunto()
    # for i in [1, 2, 3]:
    #     conj1.add(i)

    # conj2 = Conjunto()
    # for i in [7, 2, 10]:
    #     conj2.add(i)

    # conj3 = conj1.intersection(conj2)
    # print(conj3)

    # DIFFERENCE
    # conj4 = conj1.difference(conj2)
    # print(conj4)

    # SUBSET
    # conj1 = Conjunto()
    # for i in [1, 2, 3, 4]:
    #     conj1.add(i)

    # conj2 = Conjunto()
    # for i in [1, 2, 3, 7, 9, 10]:
    #     conj2.add(i)

    # print(conj1.issubset(conj2))

    # Exercício 7
    estudantes = Conjunto()
    for i in [1, 2, 3, 4, 5, 6, 7]:
        estudantes.add(i)

    lista1_entregues = Conjunto()
    for i in [1, 4, 7, 3]:
        lista1_entregues.add(i)

    lista2_entregues = Conjunto()
    for i in [3, 1, 6]:
        lista2_entregues.add(i)

    print(" 1 - Quem ainda não entregou a lista1?")
    print(estudantes.difference(lista1_entregues))
    print("=" * 80)

    print(" 2 - Quem já entregou as duas listas?")
    print(lista1_entregues.intersection(lista2_entregues))
    print("=" * 80)

    print(" 3 - Quem já entregou qualquer uma das duas listas?")
    print(lista1_entregues.union(lista2_entregues))
    print("=" * 80)

    print(" 4 - Quem ainda não entregou nenhuma das listas?")
    entregou_algo = lista1_entregues.union(lista2_entregues)
    print(estudantes.difference(entregou_algo))
    print("=" * 80)
