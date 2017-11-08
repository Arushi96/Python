import requests
from bs4 import BeautifulSoup

http = requests.get("http://quotes.toscrape.com/page/1/")
http_doc = http.text
f=open("D:\\Arushi\\Quotes.txt" ,"a")
f.write(http.text.encode("utf-8"))

http_doc = open("D:\\Arushi\\Quotes.txt", "r").read()
soup = BeautifulSoup(http_doc, "html.parser")
