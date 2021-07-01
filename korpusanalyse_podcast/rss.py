import feedparser

d = feedparser.parse('https://www.tagesschau.de/xml/atom/')

print(len(d))