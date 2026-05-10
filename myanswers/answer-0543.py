from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def mejor_k_clustering(X):
    resultados = {}

    for k in [2, 3, 4]:
        modelo = KMeans(n_clusters=k, n_init=10)
        labels = modelo.fit_predict(X)
        score = silhouette_score(X, labels)
        resultados[k] = score

    mejor_k = max(resultados, key=resultados.get)

    return int(mejor_k)
