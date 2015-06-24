
#!/usr/bin/python

import feedparser
import codecs
import datetime

f = codecs.open('bzusnews.tsv', 'a', 'utf-8')
f.write("column" + "\n")

feeds = feedparser.parse('http://www.buzzfeed.com/usnews.xml')

for feed in feeds.entries:
    f.write("\t".join((feed.title, feed.author, feed.published, feed.link)) + "\n")

f.close()