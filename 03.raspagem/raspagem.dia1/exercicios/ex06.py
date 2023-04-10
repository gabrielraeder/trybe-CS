from pymongo import MongoClient


def find_by_category(category: str):
    with MongoClient() as client:
        db = client.library
        found = db.books.find({"categories": category}, projection=["title"])
        for book in found:
            print(book["title"])


find_by_category("Internet")
