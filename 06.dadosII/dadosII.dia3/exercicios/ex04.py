# O departamento comercial de sua empresa quer fazer um trabalho
# especial nos países que fazem parte da confederação
# CONMEBOL, portanto mostre na tela quais são eles.
from ex01 import df


conmebol = df.loc[df["confederation"] == "CONMEBOL"]

print(conmebol)
