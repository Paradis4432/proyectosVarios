#%%
from enum import unique
import pandas as pd
import numpy as np

#%%
pd.set_option('display.max_colwidth', -1)

#import the csv file
data = pd.read_csv('jeopardy.csv')

df = pd.DataFrame(data)

#%%

df.columns = ['show_number', 'Time', "round", 'Category', 'Value', 'Question', 'answer']


# %%
# Write a function that returns the count of the unique answers to 
# all of the questions in a dataset.
