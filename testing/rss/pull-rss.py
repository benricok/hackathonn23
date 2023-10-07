import feedparser
import pandas as pd
from datetime import datetime

DATA_PATH='/home/bkadmin/datasets/spatialedge-hackathon-H1/v1/' 
FROM_DATE='20200101'
TO_DATE='20221231'
SYMBOL = 'EURUSD'
TIMEFRAME = 'H1'

## Google News for rss

# https://news.google.com/search?q=central+bank+US+EU+site%3Abloomberg.com+when%3A1d&hl=en-ZA&gl=ZA&ceid=ZA%3Aen
#                                               ^
#                                               Could possibly swop with SYMBOL tags 

feed = feedparser.parse("https://news.google.com/rss/search?q=central+bank+US+EU+site%3Abloomberg.com+when%3A1d&hl=en-ZA&gl=ZA&ceid=ZA%3Aen")

print('Number of RSS posts :', len(feed.entries))

if len(feed.entries) == 0:
    exit()

titles = []
dates = []

for post in feed.entries:
    title = post.title
    date = post.published
    titles.append(title.replace(' - Bloomberg', ''))
    dates.append(datetime.strptime(date, '%a, %d %b %Y %X %Z').date())

if SYMBOL == 'EURUSD':
    search = ['US', 'EU']
else:
    search = []

tags_in_title = []
for title in titles:
    tags = []
    for tag in search:
        if tag in title: tags+=[tag]
    tags_in_title += [tags]

# tags = [ (True if tag in title else False) for tag in search]

print(tags)

df = pd.DataFrame({'Title': titles,'Tags': tags_in_title,'Date': pd.to_datetime(dates)})

df.info()
print(df)