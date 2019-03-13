import pandas as pd
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import preprocessing


iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris['feature_names'])
###########INFORMATION ON DATAFRAME
###########HAS NO NULL VALUES
X.info()
###############STANDARDIZATION PERFORMED
scaler =preprocessing.StandardScaler()
scaler.fit(X)
X_scaled_array=scaler.transform(X)
X_scaled=pd.DataFrame(X_scaled_array, columns =X.columns)
#############STANDARDIZATION PERFORMED


data = X[['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)']]
data_scaled= X[['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)']]

sse = {}
sse_scaled={}
for k in range(1, 10):
    kmeans = KMeans(n_clusters=k, max_iter=1000).fit(data)
    kmeans_scaled = KMeans(n_clusters=k, max_iter=1000).fit(data_scaled)
    data["clusters"] = kmeans.labels_
    data_scaled["clusters"]=kmeans_scaled.labels_
    #print(data["clusters"])
    sse_scaled[k]=kmeans_scaled.inertia_
    sse[k] = kmeans.inertia_ # Inertia: Sum of distances of samples to their closest cluster center

plt.figure(1)
plt.plot(list(sse.keys()), list(sse.values()))
plt.title('ELBOW METHOD LAB 2')
plt.xlabel("Number of cluster")
plt.ylabel("SSE")
plt.show()

plt.figure(2)
plt.plot(list(sse_scaled.keys()), list(sse_scaled.values()))

plt.show()


############FOR SILHOUETT SCORE

from sklearn.metrics import silhouette_score
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

X = load_iris().data
y = load_iris().target

for n_cluster in range(2, 11):
    kmeans = KMeans(n_clusters=n_cluster).fit(X)
    label = kmeans.labels_
    sil_coeff = silhouette_score(X, label, metric='euclidean')
    print("For n_clusters={}, The Silhouette Coefficient is {}".format(n_cluster, sil_coeff))