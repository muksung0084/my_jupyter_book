#!/usr/bin/env python
# coding: utf-8

# ## Datetype handling
datetime 표현 관련. 

df['Birth_date']       = df['Birth'].dt.date         # YYYY-MM-DD(문자)
df['Birth_year']       = df['Birth'].dt.year         # 연(4자리숫자)
df['Birth_month']      = df['Birth'].dt.month        # 월(숫자)
df['Birth_month_name'] = df['Birth'].dt.month_name() # 월(문자)

df['Birth_day']        = df['Birth'].dt.day          # 일(숫자)
df['Birth_time']       = df['Birth'].dt.time         # HH:MM:SS(문자)
df['Birth_hour']       = df['Birth'].dt.hour         # 시(숫자)
df['Birth_minute']     = df['Birth'].dt.minute       # 분(숫자)
df['Birth_second']     = df['Birth'].dt.second       # 초(숫자)

df['Birth_quarter']       = df['Birth'].dt.quarter       # 분기(숫자)
df['Birth_weekday_name']  = df['Birth'].dt.weekday_name  # 요일이름(문자) (=day_name())
df['Birth_weekday']       = df['Birth'].dt.weekday       # 요일숫자(0-월, 1-화) (=dayofweek)
df['Birth_weekofyear']    = df['Birth'].dt.weekofyear    # 연 기준 몇주째(숫자) (=week)
df['Birth_dayofyear']     = df['Birth'].dt.dayofyear     # 연 기준 몇일째(숫자)
df['Birth_days_in_month'] = df['Birth'].dt.days_in_month # 월 일수(숫자) (=daysinmonth)
# ### datetime 연산
# 

# In[1]:


import pandas as pd 
from datetime import datetime
import time

time_data_sample = []
for i in range(10) :
    time_data_sample.append(datetime.now())
    time.sleep(1)
    
df_time = pd.DataFrame(time_data_sample , columns=['time_now'])


# In[2]:


print('days 환산 : ', (now - df_time['time_datetime'][0]).days)
print('seconds 환산 : ', (now - df_time['time_datetime'][0]).seconds)
print('mins 환산 : ', (now - df_time['time_datetime'][0]).seconds/60)
print('time 환산 : ', (now - df_time['time_datetime'][0]).seconds/3600)


# In[ ]:


print('now       : ' , now )
print('days 연산 : ', now + timedelta(days=2) )
print('time 연산 : ' , now + timedelta(hours=23))
print('mixed 연산 : ' , now + timedelta(days = 1 , hours=1, minutes=20, seconds=30))


# ### date time <-> str 변환 
날짜와 시간(datetime)  --> 문자열 : strftime    
date = now.strftime(%Y-%m-%d)  // series가 아닌 단순히 하나의 문자열 data인 경우 // 

series type에 적용을 원하면 df['a'].dt.strftime(~~)
# In[ ]:


df_time['time_str'] = df_time['time_datetime'].dt.strftime('%Y - %m - %d %H:%M:%S')

문자열 --> datetime type으로 변환 : strptime     
datetime.strptime(원하는 문자열 , 원하는 형태 '%Y - %m - %d %H:%M:%S' )    
series type에 적용르 원하면, [ list comprehension 리스트컴프리핸션을 이용 ]
# In[ ]:


df_time['str-datetime'] = [ datetime.strptime(i,'%Y - %m - %d %H:%M:%S') for i in df_time['time_str']]

