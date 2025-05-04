import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\Me\Desktop\lab10\student.csv')
print(df.isnull().sum())


df = df.drop(columns=['student_id'])
for cols in ['GPA','study_hours','attendance_rate']:
    df[cols] = df[cols].fillna(df[cols].mean())

x = df.values

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

wcss=[]


for i in range(1,11):
    kmeans = KMeans(n_clusters=i,init='k-means++',random_state=42)
    kmeans.fit(x_scaled)
    wcss.append(kmeans.inertia_)
    
plt.plot(range(1,11),wcss)
plt.title('The Elbow Method Graph')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('WCSS')
plt.show()
    
    
kmeans = KMeans(n_clusters=3,init='k-means++',random_state=42)
ypred = kmeans.fit_predict(x_scaled)

plt.figure(figsize=(8, 6))
for cluster in np.unique(ypred):
    plt.scatter(
        x[ypred == cluster, 0],
        x[ypred == cluster, 1],
        s=100,
        label=f'Cluster {cluster + 1}'
    )

plt.xlabel('GPA')
plt.ylabel('Study Hours')
plt.title('K-Means Clustering (Scaling)')
plt.legend()
plt.show()
