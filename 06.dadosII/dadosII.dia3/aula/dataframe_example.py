import pandas as pd


dicionario_de_notas = {
    "nome": ["Maria", "João", "Fernanda", "Túlio"],
    "primeira_nota": [9, 8, 7, 8],
    "segunda_nota": [8, 7, 9, 3],
    "terceira_nota": [5, 10, 7, 1],
}


def calcula_situacao(media):
    return media >= 7


df = pd.DataFrame(dicionario_de_notas)

df["media"] = round(
    (df["primeira_nota"] + df["segunda_nota"] + df["terceira_nota"]) / 3, 2
)

df["aprovado"] = df["media"].apply(calcula_situacao)

print("=" * 40)
# print(df)
# print("=" * 40)
# print(df["nome"])
# print("=" * 40)
# print(df["primeira_nota"])
# print("=" * 40)
# print(df["media"])
# print("=" * 40)
# print(df["aprovado?"])

# print(df.tail(2))
print(df.groupby(by="aprovado"))
