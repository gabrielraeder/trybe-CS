from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from browser import browser


URL = "https://www.wikimetal.com.br/moonspell-porto-alegre-2023/"


def scrape(url):
    browser.get(url)
    try:
        elements = browser.find_element(
            By.CLASS_NAME, "entry-content"
        ).find_elements(By.TAG_NAME, "p")
        for p in elements:
            print(p.text)
    except NoSuchElementException:
        return ""


scrape(URL)
