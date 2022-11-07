#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


births=pd.read_csv('C:/Users/Rakesh/Datasets/births.csv')


# In[3]:


births.head()


# In[4]:


births['decade'] = 10 * (births['year'] // 10)


# In[5]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


sns.set()
birth_decade=births.pivot_table('births', index='decade', columns='gender', aggfunc='sum')
birth_decade.plot()
plt.ylabel('Total births per year')
plt.show()


# In[7]:


import numpy as np
quartiles = np.percentile(births['births'], [25,50,75])
mu = quartiles[1]
sig = 0.74 * (quartiles[2] - quartiles[0])


# In[8]:


births = births.query('(births > @mu - 5 * @sig) & (births < @mu + 5 * @sig)')
births['day'] = births['day'].astype(int)
births.index = pd.to_datetime(10000*births.year + 100*births.month + births.day, format='%Y%m%d')

births['dayofweek'] = births.index.dayofweek


# In[9]:


births.pivot_table('births', index='dayofweek', columns='decade', aggfunc='mean').plot()
plt.gca().set_xticklabels(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'])
plt.ylabel('mea births by day');
plt.show()


# In[12]:


births_month =births.pivot_table('births', [births.index.month, births.index.day])
print(births_month.head())

births_month.index = [pd.datetime(2012, month, day)
                     for (month, day) in births_month.index]
print(births_month.head())


# In[13]:


fig, ax = plt.subplots(figsize=(12,4))
births_month.plot(ax=ax)
plt.show()

