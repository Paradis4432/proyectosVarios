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
# %%
x_is = ad.Newspaper
y_is =  ad.Sales

x_bar = np.mean(x_is)

y_bar = np.mean(y_is)
x_is_minus_x_bar = x_is - x_bar

y_is_minus_y_bar = y_is - x_bar
y_is_minus_y_bar

denom_1 = x_is_minus_x_bar ** 2
denom = np.sum(denom_1)

num_1 = x_is_minus_x_bar * y_is_minus_y_bar
num = np.sum(num_1)

beta_1_hat = num / denom
beta_1_hat

#%%
beta_0_hat = y_bar - beta_1_hat *  x_bar
beta_0_hat

#%%
y_is_hat = beta_0_hat + beta_1_hat * x_is
rss = np.sum((y_is - y_is_hat) ** 2)
rss
#%%
n = ad.shape[0]
sigma_sq_hat = rss / (n - 2)
#%%
se_beta_1_hat = np.sqrt(sigma_sq_hat / denom)
se_beta_1_hat

#%%
min_ci = beta_1_hat - 2 * se_beta_1_hat
max_ci = beta_1_hat + 2 * se_beta_1_hat

round(min_ci, 3), round(max_ci, 3)

#%%
num = sigma_sq_hat * np.sum(x_is ** 2)

denom = n * np.sum(x_is ** 2) - np.sum(x_is)**2

se_beta_0_hat = np.sqrt(num / denom)

se_beta_0_hat

#%%
min_ci = beta_0_hat - 2 * se_beta_0_hat
max_ci = beta_0_hat + 2 * se_beta_0_hat

round(min_ci, 3), round(max_ci, 3)

#%%
X_t = np.array(ad.Newspaper, ndmin=2)
X = np.transpose(X_t)
y = ad.Sales

# Tenemos que agregar explícitamente a una constante:
X = sm.add_constant(X)

model = sm.OLS(y, X).fit()
print(model.summary())