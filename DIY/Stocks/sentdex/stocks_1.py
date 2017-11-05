import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2000,1,1)
end = dt.datetime(2016,12,31)
df= web.DataReader('TSLA','yahoo', start, end)
print(df.head)#will print first 5 rows
# print(df.tail(6))#will print last 6 rows
df.to_csv('tsla.csv')
