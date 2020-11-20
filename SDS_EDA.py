#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


df = pd.read_csv('./SDS-Project-Bike-rentals.csv')


# In[4]:


type(df)


# In[5]:


df.shape


# In[6]:


df.info()


# In[7]:


df.head(50)


# In[8]:


df.head()


# In[9]:


df


# In[10]:


np.unique(df['weekday'])


# In[11]:


np.unique(df['season'])


# In[12]:


df.isnull().sum()


# In[13]:


pd.__version__


# In[14]:


df['season'].replace([1,2,3,4],['winter','spring','summer','fall'],inplace=True)


# In[15]:


df.head(50)


# In[16]:


df['weekday'].replace([0,1,2,3,4,5,6],['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'],inplace=True)


# In[17]:


df['mnth'].replace([1,2,3,4,5,6,7,8,9,10,11,12],['January','February','March','April','May','June','July','August','September','October','November','December'],inplace=True)


# In[18]:


df.isnull().sum()


# In[19]:


df[df['temp'].isnull()]


# In[20]:


temp_mean = df["temp"].mean()


# In[21]:


atemp_mean = df["atemp"].mean()


# In[22]:


hum_mean = df["hum"].mean()


# In[23]:


df['temp'] = df['temp'].replace(np.nan , temp_mean)


# In[24]:


df


# In[25]:


df['atemp'] = df['atemp'].replace(np.nan , atemp_mean)


# In[26]:


df['hum'] = df['hum'].replace(np.nan , hum_mean)


# In[27]:


df


# In[28]:


df.isnull().sum()

# In[29]:


pd.set_option('precision', 4)


# In[30]:


df.to_csv(r'./Data_Handling.csv', index = False, header = True)






