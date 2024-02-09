from sklearn.cluster import KMeans

def cluster_texts(X, n_clusters=5):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(X)
    return labels

def assign_theme_to_clusters(labels):
    theme_mapping = {0: "Africa", 1: "Asia", 2: "Europe", 3: "Middle East", 4: "US & Canada"}
    themed_labels = [theme_mapping[label] for label in labels]
    return themed_labels