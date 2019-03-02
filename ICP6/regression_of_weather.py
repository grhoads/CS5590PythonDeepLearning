import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use(style="ggplot")
plt.rcParams['figure.figsize'] = [10,6]

data = pd.read_csv('weatherHistory.csv')
data = data.dropna()

from sklearn.preprocessing import LabelEncoder
data=data.apply(LabelEncoder().fit_transform)

y = data['Temperature']
X = data.drop(['Temperature','Summary','Precip Type','Daily Summary'], axis=1)
from sklearn.model_selection import train_test_split
X_data, X_test, y_data, y_test = train_test_split(
                                    X, y, random_state=42, test_size=.33)
from sklearn import linear_model
lr = linear_model.LinearRegression()
model = lr.fit(X_data, y_data)

print ("R^2 is: \n", model.score(X_test, y_test))
predictions = model.predict(X_test)
from sklearn.metrics import mean_squared_error
print ('RMSE is: \n', mean_squared_error(y_test, predictions))

