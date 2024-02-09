import feedparser

def scrape_news_articles(feed_url):
    feed = feedparser.parse(feed_url)
    articles = []
    for entry in feed.entries:
        content = entry.get('summary', entry.get('description', 'No content available.'))
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'summary': content if content.strip() else 'No content available.'
        })
    return articles
