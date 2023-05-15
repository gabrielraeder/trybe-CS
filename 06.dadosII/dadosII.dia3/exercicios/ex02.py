# Com a finalidade de ter a visibilidade dos países com maior
# participação no compartilhamento global de transmissões,
# mostre na tela apenas os países com porcentagem de
# compartilhamento global (population_share) maior que 2.
from ex01 import df

population_share_2plus = df.loc[df["population_share"] >= 2]

print(population_share_2plus)
