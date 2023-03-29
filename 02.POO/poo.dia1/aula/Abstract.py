from abc import ABC, abstractmethod

# Para criar uma classe abstrata em Python,
# basta criar uma classe que herda de abc.ABC:


class Database(ABC):
    @abstractmethod
    def execute(self, query):
        ...


class MongoDatabase(Database):
    def execute(self, query):
        print(f"executando query '{query}' no mongo")


class MySQLDatabase(Database):
    def execute(self, query):
        print(f"executando query '{query}' no mysql")


def minha_func(database):  # repare que o d é minúsculo
    if isinstance(database, Database):
        database.execute("query qualquer")
    else:
        print(f"{database} não é um Database válido")


db1 = MongoDatabase()
db2 = MySQLDatabase()

# minha_func(db1)
# minha_func(db2)
# minha_func("db_inválido")


# repare que coloco o tipo do parâmetro, ou seja, `database` é do tipo
# `Database`
def minha_func2(database: Database):
    database.execute("query qualquer")


minha_func2(db1)
minha_func2(db2)
minha_func2("db_inválido")
