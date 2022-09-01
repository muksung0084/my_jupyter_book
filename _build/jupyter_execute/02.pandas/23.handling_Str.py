#!/usr/bin/env python
# coding: utf-8

# ## Str type handling

# 

# In[1]:


# 문자열 처리 관련 함수. 
>> 1. split --> 해당 obstacle을 기준으로 문자열을 나눈다.
>>> df[].str.split('-')

>> 2. replace --> 해당 obstacle을 다른 것으로 대체한다. 
>>> df[].str.replace('-','') -를 공백없는 칸으로 매운다.

>> 3. strip --> 값에 공백만 존재하는 경우, 문자열 값의 앞뒤로 공백이 존재하는 경우 이를 없애고 싶을때 
>>> df[].str.strip()  

>> 4. str  -->원하는 부분의 문자열만 끈고 싶을때
>>> dataframe['series'].str[:] 


# 
