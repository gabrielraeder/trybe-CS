from Eletrodomestico import Eletrodomestico


class Liquidificador(Eletrodomestico):
    def esta_ligado(self):
        return "Sim" if super().esta_ligado() else "Não"


liquidificador = Liquidificador("Preto", 110, 127, 50)
liquidificador.ligar(2)
print(liquidificador.esta_ligado())
