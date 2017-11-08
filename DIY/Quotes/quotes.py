import urllib
import re

url ="http://quotes.toscrape.com/page/1/"

htmlfile=urllib.urlopen(url)
htmltext=htmlfile.read()
# print htmltext
regex='<span class="text" itemprop="text">(.+?)</span>'
pattern = re.compile(regex)
quote= re.findall(pattern,htmltext)
# print quote
# print(type(quote))
for item in quote:
        print str(item)
        
