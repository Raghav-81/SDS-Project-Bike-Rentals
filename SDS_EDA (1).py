#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


from pandas import Series,DataFrame


# In[4]:


df = pd.read_csv('./SDS-Project-Bike-rentals.csv')


# In[5]:


type(df)


# In[6]:


df.shape


# In[7]:


df.info()


# In[8]:


df.head(50)


# In[9]:


df.head()


# In[10]:


df


# In[11]:


np.unique(df['weekday'])


# In[12]:


np.unique(df['season'])


# In[13]:


df.isnull().sum()


# In[14]:


pd.__version__


# In[15]:


df['season'].replace([1,2,3,4],['winter','spring','summer','fall'],inplace=True)


# In[16]:


df.head(50)


# In[17]:


df['weekday'].replace([0,1,2,3,4,5,6],['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'],inplace=True)


# In[18]:


df['mnth'].replace([1,2,3,4,5,6,7,8,9,10,11,12],['January','February','March','April','May','June','July','August','September','October','November','December'],inplace=True)


# In[19]:


df.isnull().sum()


# In[20]:


df[df['temp'].isnull()]


# In[21]:


temp_mean = df["temp"].mean()


# In[22]:


atemp_mean = df["atemp"].mean()


# In[23]:


hum_mean = df["hum"].mean()


# In[24]:


df['temp'] = df['temp'].replace(np.nan , temp_mean)


# In[25]:


df


# In[26]:


df['atemp'] = df['temp'].replace(np.nan , atemp_mean)


# In[27]:


df['hum'] = df['hum'].replace(np.nan , hum_mean)


# In[28]:


df


# In[29]:


df.isnull().sum()


# In[31]:


df.to_csv(r'./Data_Handling.csv', index = False, header = True)


# In[ ]:




