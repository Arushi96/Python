import urllib
import re

#to print all from a file
# symbolfile = open("D:\\Arushi\\symbols.txt")
# symbollist=symbolfile.read()
# print symbollist.split("\n")

symbollist=["aapl", "spy", "goog", "nflx", "fb"]
i=0
  
while i<len(symbollist):
    url="http://www.nasdaq.com/symbol/"+symbollist[i] #for nasdaq
#     url="https://finance.google.com/finance?q="+symbollist[i] #for google
    htmlfile=urllib.urlopen(url)
    htmltext=htmlfile.read()
    regex= '<div id="qwidget_lastsale" class="qwidget-dollar">(.+?)</div>' #for nasdaq
#     regex= '<span class="unchanged">(.+?)</span>' #for google
    regex= '<span id="ref_[^.]*">(.+?)</span>'
    pattern = re.compile(regex)
    price= re.findall(pattern,htmltext)
    print "Stock price of " + symbollist[i] + " is" , price
    i+=1


