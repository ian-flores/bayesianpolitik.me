import numpy as np
import matplotlib.pyplot as plt


from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

n_samples = 21000
centers = 7
random_state = 2019

X, y = make_blobs(n_samples=n_samples, random_state=random_state, centers = centers, cluster_std = 2.5)
y_pred = KMeans(n_clusters=centers, random_state=random_state).fit_predict(X)

from matplotlib import cm

plt.figure(figsize = (24, 15))
plt.scatter(X[:, 0], X[:, 1], c=y_pred, alpha = 0.15, cmap = cm.Dark2)

plt.axis('off')
plt.savefig('k_means.png', bbox_inches='tight')
