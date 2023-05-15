# Uma pessoa da equipe ficou curiosa sobre a quantidade
# de países em cada confederação, portanto mostre a ela essa informação.

from ex01 import df

confederations = (
    df.groupby(by="confederation")["country"].count().reset_index(name="count")
)

print(confederations)
