import feedparser
import pandas as pd
from datetime import datetime

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
    #dates.append(datetime.strptime(date, '%c %Z').date())

print(dates)

df = pd.DataFrame({'Title': titles,'Date': pd.to_datetime(dates)})

df.info()
print(df)