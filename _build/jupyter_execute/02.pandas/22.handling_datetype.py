#!/usr/bin/env python
# coding: utf-8

# ## Datetype handling

# In[63]:


import pandas as pd


# #### datetime 표현 관련

# In[64]:


df = pd.DataFrame({'Birth':['1993-01-28 01:10:00',
                            '1993-08-28 06:20:30']})
df['Birth'] = pd.to_datetime(df['Birth'], format='%Y-%m-%d %H:%M:%S', errors='raise')


# In[65]:


df['Birth_date']       = df['Birth'].dt.date         # YYYY-MM-DD(문자)
df['Birth_year']       = df['Birth'].dt.year         # 연(4자리숫자)
df['Birth_month']      = df['Birth'].dt.month        # 월(숫자)
df['Birth_month_name'] = df['Birth'].dt.month_name() # 월(문자)

df['Birth_day']        = df['Birth'].dt.day          # 일(숫자)
df['Birth_time']       = df['Birth'].dt.time         # HH:MM:SS(문자)
df['Birth_hour']       = df['Birth'].dt.hour         # 시(숫자)
df['Birth_minute']     = df['Birth'].dt.minute       # 분(숫자)
df['Birth_second']     = df['Birth'].dt.second       # 초(숫자)
df['Birth_quarter']    = df['Birth'].dt.quarter      # 분기(숫자)


# In[66]:


df


# #### datetime, time sleep 사용 

# In[67]:


from datetime import datetime
import time

time_data_sample = []
for i in range(3) :
    time_data_sample.append(datetime.now())  # .now --> 현재 시간 생성
    time.sleep(0.1)
    
df_time = pd.DataFrame(time_data_sample , columns=['time_now'])
df_time


# #### datetime 연산

# In[68]:


from datetime import timedelta
now = datetime.now()
print('now       : ' , now )
print('days 연산 : ', now + timedelta(days=2) )
print('time 연산 : ' , now + timedelta(hours=23))
print('mixed 연산 : ' , now + timedelta(days = 1 , hours=1, minutes=20, seconds=30))


# #### datetime 연산 [ hour, mins , sec 환산 ] 

# In[69]:


now = datetime.now()
print('days 환산 : ', (now - df_time['time_now'][0]).days)
print('seconds 환산 : ', (now - df_time['time_now'][0]).seconds)
print('mins 환산 : ', (now - df_time['time_now'][0]).seconds/60)
print('time 환산 : ', (now - df_time['time_now'][0]).seconds/3600)


# 

# #### date time <-> str 변환 

# 날짜와 시간(datetime)  --> 문자열 : strftime    
# 
# date = now.strftime(%Y-%m-%d)  // series가 아닌 단순히 하나의 문자열 data인 경우 // 
# 
# series type에 적용을 원하면 df['a'].dt.strftime(~~)

# In[77]:


df_time['date_to_str'] = df_time['time_now'].dt.strftime('%Y - %m - %d %H:%M:%S')


# 문자열 --> datetime type으로 변환 : strptime     
# 
# datetime.strptime(원하는 문자열 , 원하는 형태 '%Y - %m - %d %H:%M:%S' )    
# 
# series type에 적용르 원하면, [ list comprehension 리스트컴프리핸션을 이용 ]

# In[78]:


df_time['str_to_date'] = [ datetime.strptime(i,'%Y - %m - %d %H:%M:%S') for i in df_time['date_to_str']]


# In[79]:


df_time


# In[80]:


df_time.dtypes


# #### date생성 관련 method data_range 

# In[82]:


dates  = pd.date_range('20220101',periods = 6)  # 20220101 부터 6개의 기간
print(dates)

