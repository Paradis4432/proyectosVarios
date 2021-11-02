
#%%
import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

#region Practice
#%%
df_trigo= pd.read_csv('dataClase20/seeds_dataset.csv')
print("shape: ", df_trigo.shape)
df_trigo.sample(5)

#%%
df_trigo.type_wheat.unique()
#%%
df_trigo.describe()
#%%
model = GaussianNB()
#%%
X = df_trigo.drop(['type_wheat'], axis=1)
y = df_trigo['type_wheat']

Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=2)

model.fit(Xtrain, ytrain)

GaussianNB()
# %%
ypred = model.predict(Xtest)
ypred

#%%
round(accuracy_score(ytest, ypred), 2)

#%%
dfSalary = pd.read_csv('dataClase20/Salary_Data.csv')
dfSalary.head()
#%%
sns.set_style('whitegrid')
fig = plt.figure(figsize=(6,3.5))
sns.scatterplot(data=dfSalary, x='YearsExperience', y='Salary')
plt.show()

#%%
kmeans = KMeans(n_clusters=4)
scaler = StandardScaler()
x = dfSalary
X_scaled = scaler.fit_transform(x)

kmeans.fit(X_scaled)
#%%
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

#%%
plt.figure(figsize=(8,5))
sns.scatterplot(x=X_scaled[:,0], y=X_scaled[:,1], hue=labels, legend='full')
plt.xlabel('YearsExperience'), plt.ylabel('Salary')
plt.scatter(centroids[:,0], centroids[:,1], marker='x', s=50, color="r")

#endregion Practice
#%%
#ej 1 
tips = sns.load_dataset('tips')
tips.head()
#%%
dfTips = tips.drop(['sex', 'day', 'time', 'size'], axis=1)
dfTips.shape
#%%
dfTips.describe().T

#%%
sns.set(style="darkgrid")
sns.scatterplot(x="total_bill", y = "tip", hue=dfTips.smoker.tolist(), data = dfTips)
plt.show()

#%%
dfTips
#%%
X = dfTips.drop(['smoker'], axis=1) 
y = dfTips['smoker']
#%%
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=2)

model.fit(Xtrain, ytrain)

#%%
ypred = model.predict(Xtest)
ypred

#%%
round(accuracy_score(ytest, ypred), 2)
#%%
#make a list of 10 random numbers
listNumbers = np.random.randint(0, 100, 10)
listNumbers