from Ventilador import Ventilador


class Pessoa:
    def __init__(self, nome, saldo_na_conta):
        self.nome = nome
        self.saldo_na_conta = saldo_na_conta
        self.liquidificador = None
        self.ventilador = None

    def comprar_liquidificador(self, liquidificador):
        if liquidificador.preco <= self.saldo_na_conta:
            self.saldo_na_conta -= liquidificador.preco
            self.liquidificador = liquidificador

    def comprar_ventilador(self, ventilador):
        if ventilador.preco <= self.saldo_na_conta:
            self.saldo_na_conta -= ventilador.preco
            self.ventilador = ventilador

    def __str__(self) -> str:
        return f"""Nome: {self.nome}
Saldo: {self.saldo_na_conta}
Possui Ventilador? {type(self.ventilador) == Ventilador }
"""


ventilador = Ventilador("Preto", "110", "127", "200")

pessoa = Pessoa("Gabriel", 1000)
pessoa.comprar_ventilador(ventilador)
print(pessoa)
