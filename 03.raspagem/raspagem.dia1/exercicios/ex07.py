from pymongo import MongoClient


def filter_published_by_category():
    with MongoClient() as client:
        db = client.library
        found = db.books.aggregate(
            [
                {"$match": {"status": "PUBLISH"}},
                {"$unwind": "$categories"},
                {"$group": {"_id": "$categories", "count": {"$sum": 1}}},
                {"$sort": {"count": -1}},
            ]
        )
        for category in found:
            print(category["_id"], category["count"], sep=": ")


filter_published_by_category()
