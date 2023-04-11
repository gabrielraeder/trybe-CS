import requests
from bs4 import BeautifulSoup

BASE_URL = "https://pt.wikipedia.org"
URL = f"{BASE_URL}/wiki/Rock_in_Rio%22"


def get_html_soup(url):
    page = requests.get(url)
    html_page = page.text

    soup = BeautifulSoup(html_page, "html.parser")
    soup.prettify()
    return soup


def transform_wiki_links(link: str) -> str:
    return link if link[:4] == "http" else f"{BASE_URL}{link}"


def get_page_links(url):
    soup = get_html_soup(url)
    links = soup.find_all("a")
    for link in links:
        print(transform_wiki_links(link["href"]))


get_page_links(URL)
