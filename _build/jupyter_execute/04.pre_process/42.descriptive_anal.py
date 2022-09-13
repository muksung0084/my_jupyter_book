#!/usr/bin/env python
# coding: utf-8

# ## Descriptive analysis _ tips 

# 

# In[1]:


import pandas as pd 
import numpy as np 


# In[3]:


np.random.randint(1, 20, size=(10, 3))


# In[32]:


np.random.seed(10)
[np.random.randint(1,20,9) for i in range(10)]


# In[45]:


np.random.seed(10)
sample = pd.DataFrame([np.random.randint(1,20,9) for i in range(10)], columns =['a','b','c','d','e','f','g','h','i'])
sample['goup'] =['f','f','a','a','a','b','c','d','c','d']


# In[46]:


sample


# #### 통계치 세분화 _ describe 

# In[39]:


display(sample['a'].describe(percentiles= [0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]))


# In[40]:


display(sample[sample['a']>5]['b'].describe(percentiles= [0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]))


# #### quantile --> 분위수 찾기 

# In[42]:


sample['a'].quantile(0.9)


# #### 누적합 구하기 

# In[47]:


sample['consum_a'] = sample['a'].cumsum()
sample


# 

# ####  groupby _ agg 펑션

# In[51]:


sample.groupby('goup').agg({'a':'count', 'b':'sum'})


# 

# #### shift 함수  --> 해당 컬럼 몇번째 

# In[52]:


sample['a_shift'] = sample['a'].shift(-2)    # 아래에서 2번째 
sample


# 

# #### group by후 몇번째 nth 

# In[ ]:


raise_temp_l=data_rv2[(data_rv2['group1']!=0) & (data['Actual TPH']_rv2['skimm']==0)].groupby(['regen','group1'])[['date','rf1_air_temp','rf1_gas_flow_pv','gas_cumsum']].nth(5)


# In[59]:


sample.groupby('goup')[['a','d','f']].nth(1)   # goup의 a,d,f에서 두번째 항목 cf> 0이 첫번째


# 

# #### q cut 범위별 range 자르기 

# In[68]:


# q cut 범위별 range 자르기 
sample['range'] = pd.qcut(sample['a'],q=5)

# 소수점 없애기 precision 
sample['range_2'] = pd.qcut(sample['a'],q=5,precision=0)

# range를 범주화 시키기 
sample['range_labels'] = pd.qcut(sample['a'],q=5,labels=range(5))

# duplicates drop 추가
sample['range_labels_2'] = pd.qcut(sample['a'],q=5,duplicates='drop')


# In[69]:


sample


# * q cut 범위별 range 자르기 
# 
# ball_vari['rank'] = pd.qcut(ball_vari['vari'], q = 5 )  --> [1.*** ~ 3.****] 지저분하게 나옴.  
# 
# * 소수점 없애기 precision 
# 
# corr_data1['temp_mean_section'] = pd.qcut(corr_data1['inner_temp_pv/mean'],q=4,precision=0)
# 
# * range를 범주화 시키기 
# 
# target_comp_gss_20['rank2'] = pd.qcut(target_comp_gss_20['target_func'], q=5,labels=range(5))
# 
# * duplicates drop 추가 
# 
# gss_raw['raw_rank2'] = pd.qcut(gss_raw['RAS'],q=4,duplicates='drop')

# 
