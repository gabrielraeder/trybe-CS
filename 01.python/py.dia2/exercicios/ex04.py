import json
import csv


def read_file():
    with open("books.json") as file:
        books = json.load(file)
    return books


def categories():
    books = read_file()
    categories = {}
    for book in books:
        for cat in book["categories"]:
            if cat not in categories:
                categories[cat] = 0
            categories[cat] += 1
    return categories, len(books)


def calculate_percentages():
    dict_cat, book_count = categories()
    percentages = {}
    for key in dict_cat:
        percentages[key] = dict_cat[key] * 100 / book_count
    return percentages


def write_csv():
    percentages = calculate_percentages()
    with open("categories_percentage.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)

        headers = [
            "categoria",
            "porcentagem",
        ]
        writer.writerow(headers)

        for key, value in percentages.items():
            if key == "":
                key = "No Categories"
            row = [
                key,
                value,
            ]
            writer.writerow(row)


write_csv()
