from FiguraGeometrica import FiguraGeometrica


class Quadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

    def perimetro(self):
        return self.lado * 4


class QuadradoStatic(FiguraGeometrica):
    @staticmethod
    def area(lado):
        return lado * lado

    @staticmethod
    def perimetro(lado):
        return lado * 4
