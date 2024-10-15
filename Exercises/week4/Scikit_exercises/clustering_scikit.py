# Importera nödvändiga bibliotek
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Syntetisk data med 3 kluster
X, y = make_blobs(n_samples=300, centers=3, cluster_std=0.60, random_state=0)


# Funktion för att visualisera resultaten
def plot_clusters(ax, X, y_pred, centers=None, title=""):
    ax.scatter(X[:, 0], X[:, 1], c=y_pred, cmap='viridis')

    if centers is not None:
        ax.scatter(centers[:, 0], centers[:, 1], c='red', marker='x', s=200, linewidths=3)

    ax.set_title(title)
    ax.set_xlabel("Feature 1")
    ax.set_ylabel("Feature 2")

# Skapa en figur med subplots
fig, axs = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle('K-means Klustring med Olika Antal Kluster', fontsize=16)


# Plotta den genererade datan
plot_clusters(axs[0, 0], X, y, title='Genererad data med 3 kluster')

# Implementera och plotta K-means-klustring med 3 kluster
kmeans = KMeans(n_clusters=3, random_state=0)
y_pred = kmeans.fit_predict(X)
plot_clusters(axs[0, 1], X, y_pred, kmeans.cluster_centers_, title='K-means klustring resultat (3 kluster)')


# Experimentera med olika antal kluster
for i, n_clusters in enumerate([2, 4, 5]):
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    y_pred = kmeans.fit_predict(X)
    plot_clusters(axs[1, i], X, y_pred, kmeans.cluster_centers_, title=f'K-means klustring resultat ({n_clusters} kluster)')


# Ta bort den tomma subplotten
fig.delaxes(axs[0, 2])

# Justera layouten och visa plotten
plt.tight_layout()
plt.show()
