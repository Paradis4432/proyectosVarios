#%%
from numpy.core.fromnumeric import ndim
import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.api as sm

#%%
ad = pd.read_csv("./dataClase21/advertising.csv")
ad.head()

#https://seaborn.pydata.org/generated/seaborn.regplot.html

advertising_grid = pd.melt(ad, id_vars="Sales", value_vars = ["TV", "Radio", "Newspaper"])
g = sns.FacetGrid(advertising_grid, col="variable")
g.map(sns.regplot, "value", "Sales",  
      ci = 95,
      scatter_kws = {"color": "blue", 's': 10}, 
      line_kws = {"color": "red"})

#%%
sns.regplot(data = ad, x = "TV", y = "Sales", 
            ci = 95,
            scatter_kws = {"color": "blue", 's': 10},
            line_kws = {"color": "red"});   

#%%
sns.regplot(data = ad, x = "Radio", y = "Sales", 
            ci = 95,
            scatter_kws = {"color": "blue", 's': 10},
            line_kws = {"color": "red"});     

#%%
sns.regplot(data = ad, x = "Newspaper", y = "Sales", 
            ci = 95,
            scatter_kws = {"color": "blue", 's': 10},
            line_kws = {"color": "red"})

#%%
beta_0 = 6.975
beta_1 = 0.055

mean_y = ad.Sales.mean()
mean_y

tss_i = ad.Sales.apply(lambda yi: (yi - mean_y) ** 2)
tss = tss_i.sum()
tss

y_hat_i = beta_0 + beta_1 * ad.TV
y_hat_i

i_count = ad.shape[0]
rss_i = [(ad.Sales[i] - y_hat_i[i]) ** 2 for i in range(i_count)]
    
rss = sum(rss_i)
rss

r2 = (tss - rss) / tss
print("R2: ", np.round(r2, 3))
#%%
X_t = np.array(ad.TV, ndmin=2)
X = np.transpose(X_t)
y = ad.Sales

X = sm.add_constant(X)

model = sm.OLS(y,X).fit()
print(model.summary())