import urllib
import re
 
url="http://quotes.toscrape.com/page/"
url_list=[]
for index in range (1,50):
    final_url=url+str(index)
#     print (final_url)
    url_list.append(final_url)
# print[l]
   
for url in url_list:  
    htmlfile=urllib.urlopen(url)
    htmltext=htmlfile.read()
# print htmltext
    regex='<span class="text" itemprop="text">(.+?)</span>' 
    pattern = re.compile(regex)
    quote= re.findall(pattern,htmltext)
    for item in quote:
        print str(item)
