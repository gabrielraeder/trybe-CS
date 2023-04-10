import requests


url = "https://scrapethissite.com/pages/advanced/?gotcha=headers"

response = requests.get(url)
assert "bot detected" not in response.text
