from collections.abc import Iterable, Iterator
from abc import ABC, abstractmethod


class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __repr__(self):
        return "<%s de %s>" % (self.valor, self.naipe)


class Baralho(Iterable):
    naipes = "copas ouros espadas paus".split()
    valores = "A 2 3 4 5 6 7 8 9 10 J Q K".split()

    def __init__(self, estrategia):
        self._cartas = [
            Carta(valor, naipe)
            for naipe in self.naipes
            for valor in self.valores
        ]
        self.estrategia = estrategia

    def __len__(self):
        return len(self._cartas)

    def __iter__(self):
        return BaralhoIterator(self._cartas, self.estrategia)

    def __str__(self) -> str:
        return f"{[carta for carta in self]}"


class BaralhoInverso(Baralho):
    def __iter__(self):
        self._cartas.reverse()
        return BaralhoIterator(self._cartas)


class BaralhoIterator(Iterator):
    def __init__(self, baralho, estrategia):

        self.baralho = baralho
        self._estrategia = estrategia
        self._pos = 0

    def __next__(self):
        try:
            carta = self.baralho[self._pos]
        except IndexError:
            raise StopIteration()
        else:
            self._pos = self._estrategia.proxima_carta(self._pos)
            return carta


class EstrategiaIteracao(ABC):
    posicao_inicial = 0

    @abstractmethod
    def proxima_carta(cls, index):
        raise NotImplementedError


class EstrategiaRegular(EstrategiaIteracao):
    posicao_inicial = 1

    @classmethod
    def proxima_carta(cls, index):
        return index + 1


class EstrategiaReversa(EstrategiaIteracao):
    posicao_inicial = -1

    @classmethod
    def proxima_carta(cls, index):
        return index - 1


iterator = Baralho(EstrategiaRegular())

for page in iterator:
    print(page)
