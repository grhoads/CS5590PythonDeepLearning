import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")
sns.set(style="white", color_codes=False)

dataset = pd.read_csv('train.csv')

for i in dataset:
    if i == "GarageArea" or i == "SalePrice":
        continue
    else:
        dataset.drop(labels=i,axis=1,inplace=True)


sns.FacetGrid(dataset, hue=None, size=5).map(plt.scatter, "GarageArea","SalePrice")
plt.show()
count = 0
for i in dataset["GarageArea"]:
    if i > 1200:
        dataset.drop([count],inplace=True)
    count+=1

print(dataset["GarageArea"].value_counts())
print(dataset)
sns.FacetGrid(dataset, hue=None, size=5).map(plt.scatter, "GarageArea","SalePrice")
plt.show()

