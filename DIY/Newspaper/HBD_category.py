# import newspaper
from newspaper import Source
from datetime import datetime
import os
import datetime
import newspaper

ppr = newspaper.build('http://cnn.com')

for category in ppr.category_urls():
#         print(ppr.brand, ppr.description, category)
        for article in ppr.articles:
            article.download()
            article.parse()
#             print(article.text)
#             print(article.authors, article.publish_date)
            print(article.summary.encode('utf-8'))
#         print(url.encode('utf-8') + ":" + article.authors() + ":" + article.title.encode('utf-8') + ":" + article.text.encode('utf-8'))
#         print(url,article.title.encode('utf-8'))