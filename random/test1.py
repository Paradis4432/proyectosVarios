# %%

import seaborn as sns
import pandas as pd
import numpy as np

# %%
a = np.arange(15)
# %%
#mask = (a >= 5) & (a <= 10)
mask = np.logical_or(a >= 5, a <= 10)
# %%
a[mask]
# %%

# create two lists of random values between 0 and 100
x = np.random.randint(0, 100, 10)
y = np.random.randint(0, 100, 10)

# make a heatmap correlation of x and y
sns.heatmap(pd.DataFrame(np.c_[x, y]))

# %%
# import a random dataset
df = pd.read_csv(
    'https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv')
df.head()

# %%
sample = df.sample(n=100)
sample.head()

# %%
sns.heatmap(sample.corr())

# %%
# take two random columns from sample
cols = list(sample.columns)
x = cols[0]
y = cols[1]
# make a heatmap correlation of x and y
sns.heatmap(sample[[x, y]].corr())
# %%
data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
# %%
data.loc[["a", "d"]]
# %%
mask = np.logical_or(data.index == 'a', data.index == 'd')
data.loc[mask]
# %%
mask = [x in ['a', 'd'] for x in data.index]
data.loc[mask]
# %%

data[['a', 'd']]
# %%

data['a', 'd']
# %%
# create a df with 3 cols
# col1
# col2
# col3
df = pd.DataFrame(np.random.randn(4, 3), columns=['col1', 'col2', 'col3'])
# define the values in df as columns for col1: 1 3 5 8
df['col1'] = [1, 3, 5, 8]
# col2: 10 12 18 21
df['col2'] = [10, 12, 18, 21]
# col3: 9 4 0 78
df['col3'] = [9, 4, 0, 78]

# %%
mask1 = (df % 2 == 0)
mask2 = (df < 50)
mask = np.logical_or(mask1, mask2)
df[mask]

#%%
mask1 = (df % 2 == 0)
data_pares = df[mask1]
mask2 = (df < 50)
data_pares[mask2]
#%%

mask1 = (df % 2 == 0)
mask2 = (df < 50)
mask = np.logical_and(mask1, mask2)
df.loc[mask]
#%%

mask1 = (df % 2 == 0)
mask2 = (df < 50)
mask = np.logical_and(mask1, mask2)
df[mask]