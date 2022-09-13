#!/usr/bin/env python
# coding: utf-8

# ## Data merge

# In[3]:


import pandas as pd 


# #### concat 활용하여 행,열 base로 붙이기

# In[9]:


from datetime import datetime 
import time 

test_df = pd.DataFrame()
for i in range(5) : 
    a = pd.DataFrame(data = datetime.now().strftime('%Y-%m-%d %H:%M:%S') , index = [datetime.now().strftime('%Y-%m-%d %H:%M:%S')] , columns = ['time'])
    test_df = pd.concat([a,test_df],axis=0,ignore_index=True)
    #pd.merge([test_df,a])
    time.sleep(1)
print(test_df)


# 
pip install pandasql
# #### sql 쿼리문 활용 <- 시간 term base로 묶기

# In[ ]:


import pandasql as ps 

query = """SELECT a.*
           from tableb b inner join tablea a on ((a.test1 between b.cast1 and b.cast2) & ( a.batch=b.BATCH)); """

