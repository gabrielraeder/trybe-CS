from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from browser import browser


URL = "https://diolinux.com.br/"


def scrape(url):
    browser.get(url)
    try:
        elements = browser.find_elements(By.CLASS_NAME, "col-md-4 ")
        for element in elements:
            title = element.find_element(By.CLASS_NAME, "post-title")
            link = title.find_element(By.TAG_NAME, "a").get_attribute("href")
            print(title.text, link)
    except NoSuchElementException:
        return ""


scrape(URL)
