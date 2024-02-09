from sklearn.feature_extraction.text import TfidfVectorizer

def preprocess_texts(articles):
    summaries = [article['summary'] for article in articles]
    vectorizer = TfidfVectorizer(stop_words='english', max_features=10000)
    X = vectorizer.fit_transform(summaries)
    return X, vectorizer
    
