#!/usr/bin/env python
# coding: utf-8

# ## Useful Function

# In[1]:


import pandas as pd
import numpy as np


# 

# #### lambda 매개변수 : 표현식
# 
# ##### 간단한 함수식을 def로 정의하지 않고, lambda를 이용하여 연산할 수 있음. 

# In[2]:


# sample 만들기 
lambda_sample = pd.DataFrame( [np.random.randint(-10,20,size=2)for i in range(5)], columns= ['test','test2'] )
display(lambda_sample)


# In[3]:


lambda_sample['PLUS'] = (lambda x,y :x+y)(lambda_sample['test'],lambda_sample['test2'])
lambda_sample


# In[4]:


lambda_sample['test'][lambda_sample['test'].apply(lambda x : x-2) >= 3]


# In[5]:


# 공정데이터 적용 예시.
observable1 = mf3_cleaned.groupby('BATCHNO')['Time'].apply(lambda x: x.max() - x.min()) >=  pd.Timedelta(minutes=100) 
observable2 = mf3_cleaned.groupby('BATCHNO')['Time'].apply(lambda x: x.max() - x.min()) <=  pd.Timedelta(minutes=150) 
observable3 = mf4_cleaned.groupby('BATCHNO')['Time'].apply(lambda x: x.max() - x.min()) >=  pd.Timedelta(minutes=100) 
observable4 = mf4_cleaned.groupby('BATCHNO')['Time'].apply(lambda x: x.max() - x.min()) <=  pd.Timedelta(minutes=150)


# 

# #### .reduce (함수 : 시퀀스)  
# ###### 시퀀스(문자열, 리스트, 튜플)의 원소들을 누적적으로 함수에 적용.

# In[ ]:


from function import reduce
reduce(lambda x,y: x+y,[1,2,3,4,5])


# 

# #### map함수 
# ###### object 객체를 categorical 객체로 변환하고 싶은경우 --> 메모리사용이 효율적임.

# In[6]:


mapping_sample = pd.DataFrame(np.random.randint(0,9,30), columns = ['point'])


# In[8]:


mapping = {0:'good', 1:'good', 2:'bad', 3:'bad', 4:'bad',5:'worse',6:'worse',7:'worse',8:'worse',9:'worse'}
mapping_sample['rating'] =mapping_sample['point'].map(mapping)

mapping_sample.info() # 메모리 사용량 


# In[9]:


mapping_sample['rating'] = mapping_sample.rating.astype('category')


# In[11]:


mapping_sample.head(3)


# 

# ##### .applymap (함수 ) : dataframe 전체에 해당 function을 적용 
# 
# ##### .apply(함수) : series type 즉, 특정 컬럼에 대해서 선택적으로 function  적용 가능 

# In[12]:


function = lambda x : str(x)+'점'


# In[13]:


mapping_sample.applymap(function).head(3)


# In[14]:


mapping_sample['point_점_apply'] = mapping_sample['point'].apply(function)


# In[15]:


mapping_sample.head(3)


# 
