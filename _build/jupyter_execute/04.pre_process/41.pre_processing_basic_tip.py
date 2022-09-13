#!/usr/bin/env python
# coding: utf-8

# ## Data Pre-processing _ tips

# In[5]:


import pandas as pd 
import numpy as np


# In[52]:


sample = pd.DataFrame({'type' : ['k','y','k','y',np.nan],
                       'a' : [1,2,'1 ',3,np.nan]},index=[1,2,3,4,5])
display(pd.DataFrame(sample))


# #### null 값 check 

# In[8]:


for i in sample.columns : 
    print(i+" _null : ")
    print(sample[i].isnull().sum())
    print(sample[i].notnull().sum())


# In[9]:


sample.isnull().sum(1) # row 마다 결측값 개수 
sample.isnull().sum()  # column마다 결측값 개수 


# In[14]:


sample


# In[19]:


df_=sample.copy()


# #### null값 처리 

# In[53]:


# 어느 칼럼에 하나라도 nan값이 박혀있다면 그 행을 모두 지울것이다.  => 열, 즉 칼럼을 지우고 싶으면 axis=1 
df_=sample.copy()
display(df_.dropna(axis=0,how='any'))
display(df_.dropna(axis=0,how='all'))


# In[54]:


# 결측치 무시하고 숫자 DATA로 바꾸기  // 컬럼에 들어와야할 데이터가 분명 숫자 데이터인데 다른 타입의 에러데이터가 낄 경우 
df_['a'] = pd.to_numeric(df_['a'], errors='coerce')
display(df_)

# 이후 결측치 파악 
print("\n결측치")
print(df_['a'].isnull().sum())

# 해당 결측치 DATA DROP 
df_.dropna(subset = ['a'])
#df_ = df_.dropna(subset = ['a'])


# 

# #### 중복값 처리

# In[55]:


# 중복값 제거 
display(df_.drop_duplicates(['type'],keep='first'))
# 컬럼이 두개 이상일 경우 --> 두개의 컬럼 조건이 모두 같아야 삭제된다. 
display(df_.drop_duplicates(['type','a'],keep='first'))


# In[61]:


sample[sample['a']==1]


# #### 원하는 조건부 drop _ (feat. loc,iloc)

# In[65]:


# 해당 index drop하기
display(sample)
display(sample.drop(sample[sample['a']==1].index))  # 3번열의 1번은 문자 타입이라서 삭제가 안되는 것임.


# #### loc , iloc 활용 

# In[ ]:


.loc[indexing, colums선택(컬럼명) ] 

.iloc[indexing, colums선택 (숫자로 몇번째)] 

### > 해당 색인 추출에서 중요한것은 []안에 ,기준 첫번째는 행에대한 조건을 기입 - 두번째는 열에대한 조건을 기입하는 것이다.


# In[ ]:


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


# #### 컬럼명 바꾸기

# In[70]:


df_.rename(columns = {'type' : 'TYPE','a': 'A'},inplace=True)


# In[71]:


df_

