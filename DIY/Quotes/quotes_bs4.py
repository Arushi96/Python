from bs4 import BeautifulSoup
import requests

http = requests.get("http://quotes.toscrape.com/")
http_doc = http.text
soup = BeautifulSoup(http_doc, "html.parser")
spans= soup.findall{attrs={"class":"next"}}
print spans


# <a href="/page/2/">Next <span aria-hidden="true">→</span></a>