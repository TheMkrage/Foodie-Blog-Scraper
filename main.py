import feedparser
import html2text
import pprint
from textblob import TextBlob
import csv

htmlToTextTranslator = html2text.HTML2Text()
htmlToTextTranslator.ignore_links = True
htmlToTextTranslator.ignore_images = True
pp = pprint.PrettyPrinter(indent=4)

def getParsedItemFunction(blog_title):
  def getItem(item):
    parsed_description = htmlToTextTranslator.handle(item.description)
    item['description'] = parsed_description
    item['blog'] = blog_title
    return item
  return getItem


field_names = ['id', 'title', 'blog', 'link', 'description', 'author', 'published']
def writeHeaderToCSV():
  with open('output.csv', 'w') as csvfile: 
    writer = csv.DictWriter(csvfile, fieldnames = field_names, extrasaction='ignore') 
    writer.writeheader() 


def writeToCSV(entries):
  with open('output.csv', 'a') as csvfile: 
    writer = csv.DictWriter(csvfile, fieldnames = field_names, extrasaction='ignore') 
    writer.writerows(entries) 

def scrape_rss_feeds():
  writeHeaderToCSV()
  rss_urls = ["https://www.oh-soyummy.com/rss.xml", "https://mmm-yoso.typepad.com/mmmyoso/atom.xml", "https://classicsandiego.com/feed/", "https://sandiegofoodfinds.com/category/restaurant-reviews/feed/", "http://bitesandiego.com/feed/", "http://www.sandiegofoodstuff.com/feeds/posts/default?alt=rss"] 
  for rss_url in rss_urls:
    d = feedparser.parse( rss_url )
    entries = map(getParsedItemFunction(d.feed.title), d.entries)
    writeToCSV(entries)


# for item in d.entries:
#   print(item.id)
#   # pp.pprint(item)
#   print(item.title)
#   print(item.link)
#   print(item.author)
#   parsed_description = htmlToTextTranslator.handle(item.description)
#   print(parsed_description)

#   # blob = TextBlob(parsed_description)
#   # print(blob.tags)
#   # print(blob.noun_phrases)
#   # pp.pprint(blob.np_counts)