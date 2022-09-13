#!/usr/bin/env python
# coding: utf-8

# ## Str type handling

# In[4]:


import pandas as pd 
import numpy as np


# In[13]:


s = pd.Series(['A','B','A-B C','B CD',np.nan,'dog ','c-a-t',' 1 '])
df = pd.DataFrame(s,columns = ['data'])


# In[ ]:





# 1. split --> 해당 obstacle을 기준으로 문자열을 나눈다.

# In[16]:


df['data'].str.split('-')


# 2. replace --> 해당 obstacle을 다른 것으로 대체한다. 

# In[17]:


df['data'].str.replace('-','')


# 3. strip --> 값에 공백만 존재하는 경우, 문자열 값의 앞뒤로 공백이 존재하는 경우 이를 없애고 싶을때

# In[19]:


df['data'].str.strip()


# 4. str  -->원하는 부분의 문자열만 끈고 싶을때

# In[22]:


df['data'].str[:2]


# 5. str  --> 소문자, 대문자

# In[23]:


df['data'].str.lower()


# In[24]:


df['data'].str.upper()


# In[ ]:




