import newspaper

newsDict = {}
sourceurl="https://www.bhaskar.com/"
for name,  source in newsSources.iteritems():
    newscount = 0
    newsbuild = newspaper.build(source["sourceurl"])
    newsbuild.download()
    for article in newsbuild.articles:
        article.download()
        article.parse()
        print(source['sourceName'],article.publish_date, article.title.encode('utf-8'))
        if source['sourceName'] in newsDict.keys():
            newsDict[source['sourceName']] = newsDict[source['sourceName']] + 1
        else:
            newsDict[source['sourceName']] = 1

        del article
        #newscount +=1
        

    del newsbuild
print(newsDict)