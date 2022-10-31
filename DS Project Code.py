#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[ ]:


years = []
for i in range(2000, 2023):
    years.append(str(i))


# In[8]:


fangraphs_dict = {}

string = "FanGraphs Leaderboard - "

for year in years:
    curr_str = string + year + ".csv"
    curr_df = pd.read_csv(curr_str)
    fangraphs_dict[year] = curr_df


# In[ ]:


salary_dict = {}

string = "MLB-Salaries 2000-22 -"
for year in years:
    curr_str = string + year + ".xls.csv"
    curr_df = pd.read_csv(curr_str)
    salary_dict[year] = curr_df

