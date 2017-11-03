# import newspaper
from newspaper import Source
from datetime import datetime
import os
import datetime
import newspaper

# url=u"http://www.dailymail.co.uk/ushome/index.html"
url_list=[u"https://www.nytimes.com/",u"http://cnn.com", u"https://timesofindia.indiatimes.com/", u"https://www.washingtonpost.com/", u"https://www.theguardian.com/international", u"https://www.thesun.co.uk/", u"http://www.dailymail.co.uk/ushome/index.html", u"http://www.thehindu.com/", u"http://en.people.cn/", u"https://www.bhaskar.com/", u"http://www.hindustantimes.com/"]
for url in url_list:
    ppr = newspaper.build(url,memoize_articles=False,is_memo=False) #is_memo=False is to remove duplicacy
    ppr.download()
    ppr.parse()
      
    print(datetime.datetime.now())
#     print(ppr.logo_url.encode("utf-8"))
    print(ppr.brand,ppr.description,ppr.size())
    saved_file = open("D:\\Arushi\\Arushi.txt" ,"a") #Change location
    saved_file.write("Current Date Time: \n")
    saved_file.write(str(datetime.datetime.now()))
    saved_file.write("\n")
    saved_file.write("Newspaper Brand Name: \n")
    saved_file.write(ppr.brand.encode("utf-8"))
    saved_file.write("\n")
    saved_file.write("Newspaper Description: \n")
    saved_file.write(ppr.description.encode("utf-8"))
    saved_file.write("\n")
    saved_file.write("Total Articles: \n")
    saved_file.write(str(ppr.size()))
    saved_file.write("\n")        
    for article in ppr.articles:
        article.download()
        article.parse()
        for author in article.authors:
            print(article.authors, article.publish_date, article.text.encode('utf-8'))
            saved_file.write("Author(s) of article: \n")
            saved_file.write(str(article.authors))
            saved_file.write("\n")
            saved_file.write("Article publish date: \n")
            saved_file.write(str(article.publish_date))
            saved_file.write("\n")
            saved_file.write("Title of the article: \n")
            saved_file.write(article.title.encode('utf-8'))
            saved_file.write("\n")
            saved_file.write("Text, image & videos in the article: \n")
            saved_file.write(article.text.encode('utf-8'))
            saved_file.write("\n")
            saved_file.write(str(article.images))
            saved_file.write("\n")
            saved_file.write(str(article.movies))
            saved_file.write("\n")
            saved_file.write("Summary of the article: \n")
            saved_file.write(article.summary.text.encode('utf-8'))
            saved_file.write("\n")
            saved_file.write("=======================================END OF ARTICLE===================================================")
            saved_file.write("\n")
#        