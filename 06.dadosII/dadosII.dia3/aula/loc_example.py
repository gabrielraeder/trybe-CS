import pandas as pd


data = {
    "comida": [
        "abacate",
        "requeijão",
        "margarina",
        "doce de leite",
        "abacaxi",
    ],
    "tipo": [None, "salgado", "salgado", "doce", "doce"],
}

df = pd.DataFrame(data)

# Aqui fazemos a filtragem pelo tipo "doce" passando a condição
#  df["tipo"] == "doce" como índice do loc.
comidas_doces = df.loc[df["tipo"] == "doce"]

# print(comidas_doces)
# print(df.iloc[0])
# print(df.iloc[:2])
print(df.isnull())
print(df.isnull().sum())

print(df.groupby(by="tipo"))
