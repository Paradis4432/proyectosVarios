#%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sklearn as skplt

from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
#%%
(X,y) = skplt.datasets.load_wine(return_X_y=True, as_frame=True)
print("sape X: ",X.shape)
X.head(3)

#%%
print("shape y: ", y.shape)
#print total of labels in y
print("total of labels in y: ", y.groupby(y).count())
#%%
tree_instance = DecisionTreeClassifier(max_depth=2)

#%%
X.sample(2)
#%%
y.sample(3)
#%%
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=1)

tree_instance.fit(Xtrain, ytrain)

#%%
tree_instance.tree_.node_count

#%%
plot_tree(tree_instance, feature_names=Xtrain.columns, filled=True,
class_names=True,label= None, impurity=False)

plt.show()
# %%
ypred = tree_instance.predict(Xtest)
ypred
#%%
print(Xtest)
print(Xtest.iloc[0:2,[6,9]])
#print('etiquetas: ' , ypred[0:2])

#%%
plot_tree(tree_instance, feature_names=Xtrain.columns, filled=True, class_names=True, label=None, impurity=False) 
plt.show()
# %%
accuracy_score(ytest, ypred)