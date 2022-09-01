#!/usr/bin/env python
# coding: utf-8

# ## Data Pre-processing _ tips

# 

# In[1]:


import pandas as pd 
import numpy as np


# #### null 값 check 

# In[2]:


for i in temp_anal.columns : 
    print(i+" _null : ")
    print(temp_anal[i].isnull().sum())
    print(temp_anal[i].notnull().sum())


# In[ ]:


temp_anal.isnull().sum(1) # row 마다 결측값 개수 
temp_anal.isnull().sum()  # column마다 결측값 개수 


# 

# #### null값 처리 

# In[ ]:


# 어느 칼럼에 하나라도 nan값이 박혀있다면 그 행을 모두 지울것이다.  => 열, 즉 칼럼을 지우고 싶으면 axis=1 
df_=df.copy()
df_=df_.dropna(axis=0,how='any')
df_

# 아니다 해당 행이 모든 칼럼값에 다 nan값이 박혀있다면 그때, 그 행을 모두 지울것이다.
df_.dropna(axis=0,how='all')


# In[ ]:


# 결측치 무시하고 숫자 DATA로 바꾸기 
data_1['RF1_GAS_DAY_TOTAL'] = pd.to_numeric(data_1['RF1_GAS_DAY_TOTAL'], errors='coerce')

# 이후 결측치 파악 
print(data_1['RF1_GAS_DAY_TOTAL'].isnull().sum())

# 해당 결측치 DATA DROP 
data_1 = data_1.dropna(subset = ['RF1_GAS_DAY_TOTAL'])


# 

# #### 중복값 처리

# In[ ]:


# 중복값 제거 
df_['키']=df_['키'].drop_duplicates(keep='first')

# 컬럼이 두개 이상일 경우 --> 두개의 컬럼 조건이 모두 같아야 삭제된다. 
df_.drop_duplicates(['키','그룹'],keep='first')


# 

# ### 원하는 조건부 drop _ (feat. loc,iloc)

# In[ ]:


# 해당 index drop하기
print(sample.drop(sample.iloc[1:4]).shape)


# #### - loc , iloc 활용 

# In[ ]:


.loc[indexing, colums선택(컬럼명) ] 

.iloc[indexing, colums선택 (숫자로 몇번째)] 

### > 해당 색인 추출에서 중요한것은 []안에 ,기준 첫번째는 행에대한 조건을 기입 - 두번째는 열에대한 조건을 기입하는 것이다.


# In[5]:


data1 = ['a','b','c','d','e','f','g','h','i','j']
data2 = [10,20,30,40,50,60,70,80,90,100]
index = [1,2,3,4,5,6,7,8,9,10] 
index_sample = pd.DataFrame( { 'alpha' : data1,
                              'num' : data2 }, index = index) 


# In[ ]:


# index 정보로 선택적으로 data 컬럼별 정보 보기 
display(index_sample.loc[[3,4,6],])
display(pd.DataFrame(index_sample.loc[[3,4,6],'alpha']))
display(pd.DataFrame(index_sample.loc[[3,4,6],'num']))
display(index_sample.loc[:,'alpha'][:5])


# In[ ]:


display(pd.DataFrame(index_sample.iloc[[3,4,6],0]))
display(pd.DataFrame(index_sample.iloc[[3,4,6],[0,1]]))
display(index_sample.iloc[:,0][:5])


# 

# ### 컬럼명 바꾸기

# In[ ]:


data.rename(columns = {'RF1_N2_BNR_OFF_TIME' : 'regen_2_off_time','RF1_FIC01_SP': 'rf1_gas_flow_sp'},inplace=True)


# 
