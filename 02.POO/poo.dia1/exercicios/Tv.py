class Tv:
    def __init__(self, tamanho) -> None:
        self.tamanho = tamanho
        self.volume = 1
        self.canal = 1
        self.ligada = False

    def aumentar_volume(self):
        if self.volume == 99:
            print("volume maximo atingido")
        else:
            self.volume += 1

    def diminuir_volume(self):
        if self.volume == 1:
            print("volume minimo atingido")
        else:
            self.volume -= 1

    def modificar_canal(self, canal: int):
        if canal < 0 or canal > 99:
            raise ValueError
        else:
            self.canal = canal

    def ligar_desligar(self):
        self.ligada = not self.ligada


tv = Tv(50)
