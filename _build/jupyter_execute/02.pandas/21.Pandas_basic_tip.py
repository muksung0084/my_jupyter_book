#!/usr/bin/env python
# coding: utf-8

# ## Pandas basic _ tips 

# In[4]:


import pandas as pd 

<img src="0.dataframe_series_image.png" alt="drawing" width="500" /> from IPython.display import Image
Image("0.dataframe_series_image.png" , height=300 , width=500) # code안에서 나오게  

![title](dataframe_series_image.png) # markdown안에서 나오게 할 때.   
<img src="dataframe_series_image.png" alt="drawing" width="500" />  # markdown에서 사이즈 조절까지
                                                                                                                                                                       # https://lucycle.tistory.com/282
# 

# #### Series, DataFrame sample 만들기

# In[14]:


my_series = pd.Series({"United Kingdom":"London", "India":"New Delhi", "United States":"Washington", "Belgium":"Brussels"})
display(pd.DataFrame(my_series,columns = ['name']))


# In[23]:


comp_mf34 = pd.DataFrame(
    columns=['5182','3104','6***','5***'],
    data=0,
    index=['mf3_batches','mf3_press_pv(std)','mf3_temp_pv(std)','mf4_batches','mf3_target_func','mf4_press_pv(std)','mf4_temp_pv(std)','mf4_target_func'])

comp_mf34.index.name = 'factors'
comp_mf34.columns.name = 'alloy'

display(comp_mf34)


# In[15]:


df2 = pd.DataFrame( { 
    'A' : 1 , 
    'B' : pd.Timestamp('20220913') , 
    'C' : pd.Series(1, index = list(range(4)), dtype = 'float32'),
    'D': np.array([3]*4 ,dtype ='int32') , 
    'E': pd.Categorical(['text','train','text','train']), 
    'F' : 'foo' })


# #### dataframe관련 조회 method및 속성 

# In[25]:


print("datatype  조회 : \n",  df2.dtypes)  # type을 출력해 주는 함수 
print("\n")
print('index내용 조회 : \n',  df2.index)    # 메서드(함수)는  () 가 필요 , 속성은 () 필요 x 
print("\n")
print("column명  조회 : \n",  df2.columns)
print("\n")
print("value     조회 : \n",  df2.values)  # 데이터프레임의 값들 확인 


# #### dataframe 정렬  

# In[26]:


df2.sort_index(axis=1 , ascending= False)  
                        # axis = 0 index 기준 //  axis =1 column 기준 
                        # ascending = True -> 오름차순 
                        # ascending = False -> 내림차순
            
#print(dir(df2))  #오브젝트가 가지고 있는 속성 및 메소드 확인


# In[22]:


df2.sort_values(by='C',ascending = False)


# In[28]:


import warnings
warnings.filterwarnings('ignore')

print(df2.mean(0))  
print(df2.mean())   # default 값 0 , column별  
print(df2.mean(1))  # index 별 


# In[ ]:




