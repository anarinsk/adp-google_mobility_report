# This module is to load data from csv file  
# https://www.google.com/covid19/mobility/

#%% 
import pandas as pd 
import numpy as np 

#%%
url_data = 'https://www.gstatic.com/covid19/mobility/Global_Mobility_Report.csv?cachebust=9cfdda8c20841ad1'
df = pd.read_csv(url_data)

# %%
df
# %%
