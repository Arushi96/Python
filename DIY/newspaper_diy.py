import newspaper
from newspaper import Source
import datetime

news_dict = {}
url_list=[u"https://www.nytimes.com/",u"http://cnn.com", u"https://timesofindia.indiatimes.com/", u"https://www.washingtonpost.com/", u"https://www.theguardian.com/international", u"https://www.thesun.co.uk/", u"http://www.dailymail.co.uk/ushome/index.html", u"http://www.thehindu.com/", u"http://en.people.cn/", u"https://www.bhaskar.com/"]
for url in url_list:
    ppr= newspaper.build(url,memoize_articles=False)
    ppr.download()
    ppr.parse()
    print(ppr.size())
    #print(ppr.articles)
    for category in ppr.category_urls():
        print(ppr.brand, ppr.description, category)
        for article in ppr.articles:
            article.download()
            article.parse()
#             print(article.text)
            print(article.authors, article.publish_date)
#         print(article.summary.encode('utf-8'))
#         print(url.encode('utf-8') + ":" + article.authors() + ":" + article.title.encode('utf-8') + ":" + article.text.encode('utf-8'))
#         print(url,article.title.encode('utf-8'))