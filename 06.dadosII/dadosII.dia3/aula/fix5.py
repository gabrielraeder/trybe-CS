import pandas as pd
from sqlalchemy import create_engine

# import pymysql

df = pd.read_csv("./data/Pokemon.csv")

database_url = "mysql+pymysql://root:root@127.0.0.1:3306/pokemon"

engine = create_engine(database_url)
db_conn = engine.connect()

try:
    df.to_sql("pokemon", db_conn, if_exists="replace")

except Exception as error:
    print("Um erro ocorreu", error)

else:
    print("SUCESSO!")
    from_sql = pd.read_sql("pokemon", db_conn)
finally:
    db_conn.close()


print(from_sql)
