import pandas as pd
from sqlalchemy import create_engine

# import pymysql

database_url = "mysql+pymysql://root:root@127.0.0.1:3306/estudantes"

engine = create_engine(database_url)

db_conn = engine.connect()

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


try:
    df.to_sql("estudantes", db_conn, if_exists="replace")

except Exception as error:
    print("Um erro ocorreu", error)

else:
    print("SUCESSO!")
finally:
    db_conn.close()
