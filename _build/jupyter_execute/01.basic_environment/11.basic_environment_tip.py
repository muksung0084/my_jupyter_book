#!/usr/bin/env python
# coding: utf-8

# ## code for basic environment setting

# #### 불필요한 error 제거 

# In[1]:


import warnings
warnings.filterwarnings('ignore')


# #### 한글 폰트 사용시 폰트 깨짐 해결

# In[4]:


import platform 
import matplotlib.pyplot as plt

if platform.system() == 'Darwin': #맥
        plt.rc('font', family='AppleGothic')
elif platform.system() == 'Windows': #윈도우
        plt.rc('font', family='Malgun Gothic')
elif platform.system() == 'Linux': #리눅스 (구글 콜랩)
        plt.rc('font', family='Malgun Gothic')

#한글 폰트 사용시 마이너스 폰트 깨짐 해결
plt.rcParams['axes.unicode_minus'] = False


# #### 경로확인 및 변경 

# In[6]:


import os 

## 경로 확인 
#   print(os.getcwd()) 

## 변경원하는 경로
#   path = 'C:\\Users\\limsun\\OneDrive - Novelis Inc\\Desktop\\Data Science\\0.personal_practice\\' 

## 경로 변경
#   os.chdir(path) 

## 다른 경로에 있는 파일 불러올때
#   path = 'C:\\Users\\limsun\\OneDrive - Novelis Inc\\Desktop\\Data Science\\0.통계관련 self study\\'
#   pd.read_csv(path+'copy_of_the_training_data.csv') # ,sheet_name='excel' 


# #### 엑셀파일 sheet 여러개에 나누어 저장하고 싶을때.

# In[ ]:


import pandas as pd 
#  with pd.ExcelWriter('request_result_rmu.xlsx') as writer:  # doctest: +SKIP
#     dc1_result.to_excel(writer, sheet_name='dc1_1')
#     dc2_result.to_excel(writer, sheet_name='dc2_2')


# #### DataFrame의 출력을 소수점 자리수 제한

# In[9]:


import pandas as pd 

# 전체적인 출력 소수점 제한
pd.options.display.float_format = '{:,.2f}'.format


# #### DF 조회시 짤리는 컬럼,로우없이 확인 

# In[10]:


pd.set_option('display.width',120)
pd.set_option('display.max_row', 500)
pd.set_option('display.max_columns', 100)

# 컬럼 셀 너비 관련 _ 정보 url 
#    https://rfriend.tistory.com/487


# In[ ]:




