#basic tests nothing important
# region
data = [['A1', 28], ['A2', 32], ['A3', 1], ['A4', 0],
        ['A5', 10], ['A6', 22], ['A7', 30], ['A8', 19],
		['B1', 145], ['B2', 27], ['B3', 36], ['B4', 25],
		['B5', 9], ['B6', 38], ['B7', 21], ['B8', 12],
		['C1', 122], ['C2', 87], ['C3', 36], ['C4', 3],
		['D1', 0], ['D2', 5], ['D3', 55], ['D4', 62],
		['D5', 98], ['D6', 32]]

# %%
#ej 1
totalSites = 0
for i in data:
    totalSites += 1
print(totalSites)
# %%
print(data[6][1])
# %%
print(data[-1][1])
# %%
totalBirds = 0
for i in data:
    print(i[1])
    totalBirds += i[1]

print(totalBirds)
# %%
totalBirds = 0
for i in data:
    if i[0].startswith('C'):
        print(i[1])
        totalBirds += i[1]

print(totalBirds)
# endregion

# basic data science tests
# region
#%%

import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
df = pd.read_csv('data/2015.csv')

#%%
happScore = df['Happiness Score']
country = df['Country']

print(happScore)
print(country)
# %%

fig = go.Figure(
    data=[go.Bar(y = happScore, x = country)],
    layout_title_text="Basic Bar Chart"
)
fig.show()
# %%
fig = px.scatter(df, x="Happiness Score", y="Country", color="Region")
fig.show()

# %%
df = px.data.tips()
fig = px.bar(df, x="sex",y="total_bill",color="smoker", barmode="group")
fig.show()

# %%
df = px.data.iris()
fig = px.parallel_coordinates(df, color="species_id", labels={"species_id": "Species",
                  "sepal_width": "Sepal Width", "sepal_length": "Sepal Length",
                  "petal_width": "Petal Width", "petal_length": "Petal Length", },
                    color_continuous_scale=px.colors.diverging.Tealrose, color_continuous_midpoint=2)
fig.show()

# %%
df = px.data.tips()
fig = px.parallel_categories(df, color="size", color_continuous_scale=px.colors.sequential.Inferno)
fig.show()

#%%
data = dict(
    number=[39, 27.4, 20.6, 11, 2],
    stage=["Website visit", "Downloads", "Potential customers", "Requested price", "Invoice sent"])
fig = px.funnel(data, x='number', y='stage')
fig.show()

# endregion