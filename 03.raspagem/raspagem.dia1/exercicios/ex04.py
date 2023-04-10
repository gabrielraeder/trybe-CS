import requests
from parsel import Selector


url = "http://books.toscrape.com/catalogue/the-grand-design_405/index.html"

response = requests.get(url)
selector = Selector(text=response.text)

description: str = (
    selector.css("#product_description ~ p::text").get().rstrip("...more")
)
title: str = selector.css(".product_main h1::text").get()

price: str = selector.css(".price_color::text").re_first(r"\d+\.\d{2}")

cover: str = (
    "http://books.toscrape.com/catalogue/"
    + selector.css(".active img").xpath("@src").get()
)
print(title)
print(price)
print(description)
print(cover)
