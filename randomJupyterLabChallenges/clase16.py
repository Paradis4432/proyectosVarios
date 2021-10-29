#%%
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#%%
#make a list with 80 82.5 85 87.5 90 92.5 95 97.5 100
#make a list with 5 24 72 181 281 272 136 27 2
satisCustomers = [80, 82.5, 85, 87.5, 90, 92.5, 95, 97.5, 100]
freq = [5, 24, 72, 181, 281, 272, 136, 27, 2]

#%%
#create a bar chart with the data

data = pd.Series(freq,satisCustomers)
sns.barplot(x = data.index, y = data.values, color='#008080')

#%%
#segun las simulaciones cual es la probabilidad de obtener una muestra
#con 80% de clientes satisfechos o menos


#print the sum of all values in freq
print(sum(freq))