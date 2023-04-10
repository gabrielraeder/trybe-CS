from pymongo import MongoClient

with MongoClient() as client:
    # o banco de dados catalogue será criado se não existir
    db = client.catalogue
    # book representa um dado obtido na raspagem
    # book = {
    #     "title": "A Light in the Attic",
    # }
    # document_id = db.books.insert_one(book).inserted_id
    # print(document_id)

    # documents = [
    #     {
    #         "title": "Tipping the Velvet",
    #     },
    #     {
    #         "title": "Soumission",
    #     },
    # ]
    # db.books.insert_many(documents)

    # busca um documento da coleção, sem filtros
    print(db.books.find_one())
    # busca utilizando filtros
    for book in db.books.find({"title": {"$regex": "t"}}):
        print(book["title"])
