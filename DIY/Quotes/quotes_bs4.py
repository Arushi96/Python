import urllib2
from bs4 import BeautifulSoup
url = 'http://quotes.toscrape.com/'

conn = urllib2.urlopen(url)
html = conn.read()

soup = BeautifulSoup(html)
links = soup.find_all('a')
spans = soup.find_all('span')

# for tag in links:
#     link = tag.get('href',None)
#     if link is not None:
#         print link
        
for text in spans:
    spans = text.get('itemprop="text">',None)
    if spans is not None:
        print spans