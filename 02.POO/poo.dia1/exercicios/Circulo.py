from math import pi as PI
from FiguraGeometrica import FiguraGeometrica


class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return PI * self.raio**2

    def perimetro(self):
        return 2 * PI * self.raio


class CirculoStatic(FiguraGeometrica):
    @staticmethod
    def area(raio):
        return PI * raio**2

    @staticmethod
    def perimetro(raio):
        return 2 * PI * raio


print(CirculoStatic.area(5))
