from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from browser import browser

URL = "https://quotes.toscrape.com/"


def scrape(url):
    browser.get(url)
    try:
        element = browser.find_element(By.CLASS_NAME, "quote")
        text = element.find_element(By.CLASS_NAME, "text").get_attribute(
            "innerHTML"
        )
    except NoSuchElementException:
        return ""
    return text


print(scrape(URL))
