import feedparser

python_wiki_rss_url = "https://classicsandiego.com/feed/"
d = feedparser.parse( python_wiki_rss_url )
print(d)
# print(feed['feed']['title'])
#for item in d.entries:
  # print(item)
  #print(item.content)