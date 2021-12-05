#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install plotly


# In[6]:


pip install cufflinks


# In[8]:


pip install chart_studio


# In[12]:


import chart_studio.plotly as py
import cufflinks as cf
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode (connected = True)


# In[14]:


cf.go_offline()


# In[16]:


import pandas as pd
import numpy as np
import datetime
get_ipython().run_line_magic('matplotlib', 'inline')


# In[28]:


banking = pd.read_pickle('all_banks')


# In[26]:


start = datetime.datetime (2006,1,1)
end = datetime.datetime (2016,1,1)


# In[30]:


banking.head()


# In[32]:


banking.describe()


# In[34]:


banking.info()


# In[37]:


banking['BAC']['Close']


# In[39]:


tickers = ['BAC','C','GS','JPM','MS','WFC']


# In[42]:


for tick in tickers:
  print (tick, banking[tick]['Close'].max())


# In[44]:


banking.xs (key = 'Close', axis = 1, level = 'Stock Info')


# In[47]:


returns = pd.DataFrame()


# In[49]:


for tick in tickers:
  returns [tick+'Return'] = banking[tick]['Close'].pct_change()


# In[54]:


returns.head()


# In[61]:


import seaborn as sns


# In[65]:


sns.pairplot(returns[1:])


# In[67]:


returns.min()


# In[69]:


returns['BACReturn'].argmin()


# In[71]:


returns.idxmin()


# In[73]:


returns.idxmax()


# In[75]:


returns.std()


# In[77]:


returns.loc['2015-01-01':'2015-12-31'].std()


# In[81]:


sns.displot(returns.loc['2015-01-01':'2015-12-31']['MSReturn'], color = 'green', bins = 50)


# In[83]:


sns.displot(returns.loc['2008-01-01':'2008-12-31']['CReturn'],color = 'blue', bins = 50)


# In[85]:


for tick in tickers:
  banking[tick]['Close'].plot(label=tick, figsize = (12,4))


# In[87]:


banking.xs(key='Close',axis = 1, level = 'Stock Info').plot()


# In[89]:


banking.xs (key = 'Close', axis = 1, level = 'Stock Info')


# In[91]:


df = banking.xs (key = 'Close', axis = 1, level = 'Stock Info')


# In[92]:


banking.xs (key = 'Close', axis = 1, level = 'Stock Info').iplot()


# In[ ]:





# In[ ]:





# In[93]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().run_line_magic('matplotlib', 'inline')

# Optional Plotly Method Imports
import plotly
import cufflinks as cf
cf.go_offline()


# ** Create a line plot showing Close price for each bank for the entire index of time. (Hint: Try using a for loop, or use [.xs](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.xs.html) to get a cross section of the data.)**

# In[95]:


for tick in tickers:
    banking[tick]['Close'].plot(figsize=(12,4),label=tick)
plt.legend()


# In[97]:


banking.xs(key='Close',axis=1,level='Stock Info').plot()


# In[100]:


# plotly
banking.xs(key='Close',axis=1,level='Stock Info').iplot()


# In[102]:


BAC = banking['BAC']


# In[105]:


BAC['Close'].loc['2008-01-01':'2009-01-01'].rolling (window = 30).mean().plot(label = '30 day Mov Avg')
BAC['Close'].loc['2008-01-01':'2009-01-01'].plot(label = 'BAC Close')
plt.legend ()


# In[108]:


banking.xs(key='Close',axis = 1, level = 'Stock Info').corr ()


# In[110]:


sns.heatmap(banking.xs(key='Close',axis = 1, level = 'Stock Info').corr (),annot = True)


# In[112]:


sns.clustermap(banking.xs(key='Close',axis = 1, level = 'Stock Info').corr (),annot = True)


# In[116]:


close_corr = banking.xs(key='Close',axis = 1, level = 'Stock Info').corr()


# In[118]:


close_corr.iplot(kind = 'heatmap')


# In[121]:


BAC15 = BAC[['Open','High','Low','Close']].loc['2015-01-01':'2016-01-01']
BAC15.iplot(kind = 'candle')


# In[126]:


MS = banking['MS']


# In[131]:


MS['Close'].loc['2015-01-01':'2016-01-01'].ta_plot(study='sma',period = [13,21,55])


# In[132]:


BAC['Close'].loc['2015-01-01':'2016-01-01'].ta_plot(study='boll')

