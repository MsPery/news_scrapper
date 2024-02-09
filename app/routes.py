from flask import render_template
from app import app
from app.utils.scrapper import scrape_news_articles
from app.utils.text_processor import preprocess_texts
from app.utils.clusterer import cluster_texts, assign_theme_to_clusters

@app.route('/')
def index():
    feed_url = "https://www.nytimes.com/section/world"  
    articles = scrape_news_articles(feed_url)
    X, vectorizer = preprocess_texts(articles)
    labels = cluster_texts(X)
    themed_labels = assign_theme_to_clusters(labels)
    
    # Organize articles by themed cluster for display
    clusters = {theme: [] for theme in set(themed_labels)}
    for article, theme in zip(articles, themed_labels):
        clusters[theme].append(article)
    
    return render_template('index.html', clusters=clusters)