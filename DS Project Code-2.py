#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd


# In[34]:


years = []
for i in range(2000, 2023):
    years.append(str(i))


# In[29]:


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
    


# In[17]:


payroll_list = pd.read_html("http://www.stevetheump.com/Payrolls.htm")

years = []
for i in range(2000, 2023):
    years.append(str(i))

years.reverse()


# In[39]:


payroll_dict = {}

for i in range(len(years)):
    payroll_dict[years[i]] = payroll_list[i+1]

