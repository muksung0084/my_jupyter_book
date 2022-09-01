#!/usr/bin/env python
# coding: utf-8

# ## Descriptive analysis _ tips 

# In[1]:


import pandas as pd 
import numpy as np 


# ### 통계치 세분화 _ describe 

# In[2]:


target_data['cycle[min]'].describe(percentiles= [0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9])
cycle_org[cycle_org['gas_consum']>0]['gas_consum'].describe(percentiles= [0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9])


# ### quantile --> 분위수 찾기 

# In[ ]:


batch_skim_time4.groupby(['year','month','day','WIDTH'])['skim_time'].quantile(0.9).plot(figsize=(20,5), ylim=(120,400))


# ### 누적합 구하기 

# In[ ]:


sample['b'] = sample['a'].cumsum()
sample


# ###  groupby _ agg 펑션

# In[ ]:


data_rv2.groupby(['regen','group1']).agg({'group1':'count', 'skimm':'sum'})


# ### shift 함수  --> 해당 컬럼 몇번째 

# In[ ]:


sample['a'].shift(-2)
sample['shift'] = sample['a'].shift(-2)
sample


# ### group by후 몇번째 nth 

# In[ ]:


raise_temp_l=data_rv2[(data_rv2['group1']!=0) & (data['Actual TPH']_rv2['skimm']==0)].groupby(['regen','group1'])[['date','rf1_air_temp','rf1_gas_flow_pv','gas_cumsum']].nth(5)


# ### q cut 범위별 range 자르기 

# In[ ]:


# q cut 범위별 range 자르기 
ball_vari['rank'] = pd.qcut(ball_vari['vari'], q = 5 )  --> [1.*** ~ 3.****] 지저분하게 나옴.  

# 소수점 없애기 precision 
corr_data1['temp_mean_section'] = pd.qcut(corr_data1['inner_temp_pv/mean'],q=4,precision=0)

# range를 범주화 시키기 
target_comp_gss_20['rank2'] = pd.qcut(target_comp_gss_20['target_func'], q=5,labels=range(5))

# duplicates drop 추가 
gss_raw['raw_rank2'] = pd.qcut(gss_raw['RAS'],q=4,duplicates='drop')

