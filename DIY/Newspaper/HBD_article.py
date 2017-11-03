from newspaper import Source
from datetime import datetime
import os
import datetime
import newspaper

# cnn_paper = newspaper.build('http://cnn.com')
url_list=[u"https://www.nytimes.com/",u"http://cnn.com", u"https://timesofindia.indiatimes.com/", u"https://www.washingtonpost.com/", u"https://www.theguardian.com/international", u"https://www.thesun.co.uk/", u"http://www.dailymail.co.uk/ushome/index.html", u"http://www.thehindu.com/", u"http://en.people.cn/", u"https://www.bhaskar.com/", u"http://www.hindustantimes.com/"]
for url in url_list:
    ppr = newspaper.build(url,memoize_articles=False,is_memo=False)
    ppr.download()
    ppr.parse()
    for category in ppr.category_urls():
        cat_paper = newspaper.build(category)
        cat_paper.download()
        cat_paper.parse()
        print cat_paper.articles