from sklearn import preprocessing
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="white", color_codes=True)
import warnings
warnings.filterwarnings("ignore")

dataset = pd.read_csv('College.csv')
x = dataset.iloc[:,3:]
y = dataset.iloc[:-1]

print(dataset["Private"].value_counts())

sns.FacetGrid(dataset, hue="Private", size=5).map(plt.scatter, "Outstate", "Accept")

plt.show()

scaler = preprocessing.StandardScaler()
scaler.fit(x)

X_scaled_array = scaler.transform(x)
X_scaled = pd.DataFrame(X_scaled_array, columns = x.columns)

nclusters = 3
seed = 0

km = KMeans(n_clusters=nclusters, random_state=seed)
km.fit(X_scaled)
y_cluster_kmeans = km.predict(X_scaled)

wcss = []

# dataset.drop("Name",axis=1,inplace=True)
# dataset.drop("Private",axis=1,inplace=True)

for i in range(1,11):
    kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

plt.plot(range(1,11),wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()

from sklearn.metrics import silhouette_score

print("Silhouette Score:", silhouette_score(x, y_cluster_kmeans,metric='euclidean'))