import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('/content/Mall_Customer.csv.txt')

df_clustering = df.drop(columns=['CustomerID'])


df_clustering = pd.get_dummies(df_clustering, columns=['Gender'], drop_first=True)

features_to_scale = df_clustering.drop(columns=['Age']).values  # Exclude 'Age' from scaling

scaler = StandardScaler()
X_scaled = scaler.fit_transform(features_to_scale)

kmeans_scaled = KMeans(n_clusters=2, init='k-means++', random_state=42)
y_predict_scaled = kmeans_scaled.fit_predict(X_scaled)

plt.figure(figsize=(8, 6))
plt.scatter(X_scaled[y_predict_scaled == 0, 0], X_scaled[y_predict_scaled == 0, 1], s=100, c='blue', label='Cluster 1')
plt.scatter(X_scaled[y_predict_scaled == 1, 0], X_scaled[y_predict_scaled == 1, 1], s=100, c='green', label='Cluster 2')
plt.scatter(X_scaled[y_predict_scaled == 2, 0], X_scaled[y_predict_scaled == 2, 1], s=100, c='red', label='Cluster 3')
plt.scatter(X_scaled[y_predict_scaled == 3, 0], X_scaled[y_predict_scaled == 3, 1], s=100, c='black', label='Cluster 4')
plt.scatter(X_scaled[y_predict_scaled == 4, 0], X_scaled[y_predict_scaled == 4, 1], s=100, c='purple', label='Cluster 5')

plt.scatter(kmeans_scaled.cluster_centers_[:, 0], kmeans_scaled.cluster_centers_[:, 1], s=300, c='yellow', label='Centroids')
plt.title('K-Means Clustering (With Scaling)')
plt.xlabel('Annual Income (k$) / Spending Score')
plt.ylabel('Annual Income (k$) / Spending Score')
plt.legend()
plt.show()
