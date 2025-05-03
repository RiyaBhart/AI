import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv('/content/Mall_Customer.csv.txt')

df_clustering = df.drop(columns=['CustomerID'])

df_clustering = pd.get_dummies(df_clustering, columns=['Gender'], drop_first=True)

X = df_clustering.values  # Using all features without scaling
wcss_list = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(x)
    wcss_list.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss_list)
plt.title('The Elbow Method Graph')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('WCSS')
plt.show()

kmeans_no_scaling = KMeans(n_clusters=2, init='k-means++', random_state=42)
y_predict_no_scaling = kmeans_no_scaling.fit_predict(X)



plt.figure(figsize=(8, 6))
plt.scatter(X[y_predict_no_scaling == 0, 0], X[y_predict_no_scaling == 0, 1], s=100, c='blue', label='Cluster 1')
plt.scatter(X[y_predict_no_scaling == 1, 0], X[y_predict_no_scaling == 1, 1], s=100, c='green', label='Cluster 2')
plt.scatter(X[y_predict_no_scaling == 2, 0], X[y_predict_no_scaling == 2, 1], s=100, c='red', label='Cluster 3')
plt.scatter(X[y_predict_no_scaling == 3, 0], X[y_predict_no_scaling == 3, 1], s=100, c='black', label='Cluster 4')
plt.scatter(X[y_predict_no_scaling == 4, 0], X[y_predict_no_scaling == 4, 1], s=100, c='purple', label='Cluster 5')


plt.scatter(kmeans_no_scaling.cluster_centers_[:, 0], kmeans_no_scaling.cluster_centers_[:, 1], s=300, c='yellow', label='Centroids')
plt.title('K-Means Clustering (Without Scaling)')
plt.xlabel('Annual Income (k$) / Spending Score')
plt.ylabel('Annual Income (k$) / Spending Score')
plt.legend()
plt.show()
