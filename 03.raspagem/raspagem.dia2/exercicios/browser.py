from selenium import webdriver
import os.path
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


# Setup chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")

homedir = os.path.expanduser("~")
webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")

browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)
