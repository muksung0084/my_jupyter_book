#!/usr/bin/env python
# coding: utf-8

# ## Data merge

# ### sql 쿼리문 활용 <- 시간 term base로 묶기

# In[1]:


import pandasql as ps 

query = """SELECT a.*
from tableb b inner join tablea a on ((a.test1 between b.cast1 and b.cast2) & ( a.batch=b.BATCH)); """


# ### concat 활용하여 행,열 base로 붙이기

# In[ ]:


test_df = pd.DataFrame()
for i in range(5) : 
    a = pd.DataFrame(data = datetime.now().strftime('%Y-%m-%d %H:%M:%S') , index = [datetime.now().strftime('%Y-%m-%d %H:%M:%S')] , columns = ['time'])
    test_df = pd.concat([a,test_df],axis=0,ignore_index=True)
    #pd.merge([test_df,a])
    print(test_df)
    time.sleep(1)

