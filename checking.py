from app.utils.scrapper import scrape_news_articles

url = "http://feeds.bbci.co.uk/news/rss.xml"
articles = scrape_news_articles(url)

for article in articles:
    print("Title:", article['title'])
    print("Link:", article['link'])
    print("Description:", article['description'])
    print("\n")