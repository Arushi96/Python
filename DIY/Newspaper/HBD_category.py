# import newspaper
from newspaper import Source
from datetime import datetime
import os
import datetime
import newspaper

cnn_paper = newspaper.build('http://cnn.com')

for category in cnn_paper.category_urls():
    cat_paper = newspaper.build(category)
    cat_paper.download()
    cat_paper.parse()
    print(category)
    for art in cat_paper.articles:
        cat_paper.articles.download()
        cat_paper.articles.parse()
        print(art.authors)
#         print cat_paper.articles #Gives all articles of category
#     for article in cat_paper.articles:
#         print article.title.encode('utf-8')
#         
        
        
#     print cat_paper.articles #Gives all articles of category
#     for article in cat_paper.articles:
#         print article.url() 