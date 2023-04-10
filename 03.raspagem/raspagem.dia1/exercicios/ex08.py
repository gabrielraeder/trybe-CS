import requests
from parsel import Selector


url = "https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags"


response = requests.get(url)
selector = Selector(text=response.text)

images = selector.css(".gallerybox .image img::attr(src)").getall()

for image in images:
    filename = image.split("/")[-1]
    image_content = requests.get("https:" + image).content
    with open("./country_flags/" + filename, "wb") as file:
        file.write(image_content)
