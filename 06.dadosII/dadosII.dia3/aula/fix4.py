import pandas as pd

df = pd.read_csv("pesquisa_pao_na_chapa.csv")
# print(df)
print("=" * 30)
# 1 - Qual o dia da semana em que o queijo muçarela está com o menor preço?
menor_valor = df["preco_reais"].loc[df["produto"] == "queijo muçarela"].min()

dia = df["dia_da_semana"].loc[
    (df["preco_reais"] == menor_valor) & (df["produto"] == "queijo muçarela")
]
print(dia)
print("=" * 30)

# 2 - Qual o nome do fornecedor onde o tomate esteve
# com o maior preço histórico?
maior_valor = df["preco_reais"].loc[df["produto"] == "tomate"].min()

fornecedor = df["nome_do_fornecedor"].loc[
    (df["preco_reais"] == maior_valor) & (df["produto"] == "tomate")
]

print(fornecedor)
print("=" * 30)

# 3 - Em qual/quais dia/dias da semana o fornecedor soma pão
#  aparentemente não abriu as portas?

not_found = df["dia_da_semana"].loc[
    df["preco_reais"].isnull() & (df["nome_do_fornecedor"] == "soma pão")
]
print(not_found)
print("=" * 30)
# 4 - Crie um novo DataFrame com o preço médio de cada produto pesquisado.
new_df = (
    df.groupby(by="produto")
    .mean(numeric_only=True)
    .rename(columns={"preco_reais": "preco_medio"})
)

print(new_df)
