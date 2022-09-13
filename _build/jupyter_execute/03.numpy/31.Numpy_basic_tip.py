#!/usr/bin/env python
# coding: utf-8

# ## Numpy basic _ tips

# 

# In[2]:


import numpy as np
import pandas as pd

다차원 배열을 쉽게 처리하고 효율적으로 사용할 수 있도록지원하는 파이썬의 패키지로 

데이터 구조 외에도 수치 계산을 위해 효율적으로 구현된 기능을 제공

                                                                                                                < https://brownbears.tistory.com/480 >
                                                                                                                

파이썬의 리스트는 데이터 주소값을 저장합니다. 그리고 데이터를 가져 올때는 해당 주소에 가서 데이터를 가져옴.

하지만 Numpy Array는 C 배열과 유사하여 연속된 주소를 가지고 있음 --> 배열에 담긴 데이터를 가져온다면 순서대로 가져오면 되기 때문에 메모리를 효율적으로 사용.

                                                                                                                < https://firework-ham.tistory.com/31 > <img src="0.numpy_array_concept.JPG" alt="drawing" width="500" />
# #### numpy 무작위 추출 _ choice 

# * 숫자가 존재하는 list에서 몇개씩(크기)무작위 추출
# 
# np.random.choice(리스트명,크기)
# 
# * 리스트1에서 무작위로 3개의 sample을 뽑을것인데, 각각이 뽑힐 확률을 prob를 따르겠다.
# 
# np.random.choice(리스트명,크기,p=??)  # p값에 확률을 지정할 수 있음 

# In[3]:


list1=[1,2,3,4,5,6]
prob = [1/6,1/6,1/6,1/6,1/6,1/6] 
np.random.choice(list1,3,p=prob, replace=False)  ## 보통 replace를 건드리지 않지만, default는 True로 복원 추출, False의 경우는 비복원 추출로 한번 시행할때, 뽑힌것은 일단 배제하고 다음 것을 뽑는다.


# #### numpy 난수로 array 형성 

# In[4]:


# 0에서 1사이의 값 중에서 난수 생성. 
# 0~1 사이의 숫자로 3 by 3 array 생성 
np.random.rand(3,3)    


# #### numpy _ 정규분포

# In[5]:


# 표준 정규분포에서 무작위 숫자 추출  // [0, 1) 범위에서 균일한 분포
np.random.randn(3,2)   # 3 by 2 matrix


# In[6]:


# 표준정규분포 N(1, 0)이 아닌, 평균 μ, 표준편차 σ 를 갖는 정규분포 N(μ, σ2)의 난수를 생성
#σ * np.random.randn(…) + μ 와 같은 형태로 사용할 수 있습니다.
sigma, mu = 1.5, 2.0
c = sigma * np.random.randn(5) + mu
print(c)


# In[ ]:





# #### numpy _ random randint, normal

# In[7]:


# random.randint() 함수는 [최소값, 최대값)의 범위에서 임의의 정수
np.random.randint(2, size=5) # 는 [0, 2) 범위에서 다섯개의 임의의 정수를 생성.
np.random.randint(2, 4, size=5) # 는 [2, 4) 범위에서 다섯개의 임의의 정수를 생성합.
np.random.randint(1, 5, size=(2, 3)) # 는 [1, 5) 범위에서 (2, 3) 형태의 어레이를 생성합.

# random.normal() 함수는 정규 분포 (Normal distribution)로부터 샘플링된 난수를 반환
a = np.random.normal(0, 1, 2) # 어레이 a는 정규 분포 N(0,1)로부터 얻은 임의의 숫자 2개,
b = np.random.normal(1.5, 1.5, 4) # 어레이 b는 정규 분포 N(1.5,1.52)로부터 얻은 임의의 숫자 4개,
c = np.random.normal(3.0, 2.0, (2, 3)) # 어레이 c는 정규 분포 N(3.0,2.02)로부터 얻은 (2, 3) 형태의 임의의 숫자 어레이.           


# In[24]:


print(a)
print(b)
print(c)


# In[9]:


s = pd.Series(np.random.randint(0,7 , size =3))  # 0~7사이의 정수 생성, index는 10개
print(s)


# #### numpy random과 array 매서드로 dataframe

# In[17]:


pd.DataFrame( np.random.randn(10,20), columns = ('col %d' % i for i in range(20)) )

sample = pd.DataFrame(np.random.randint(1,20,2) for i in range(10))

my_2darray = np.array([[1, 2, 3], [4, 5, 6]])
display(pd.DataFrame(my_2darray))


sample = pd.DataFrame({'type' : ['k','y','k'],
                       'a' : [1,2,np.nan]},index=[1,2,3])
display(pd.DataFrame(sample))


# In[16]:


# np.random.randn -> 평균 0 , 표준편차 1인 표준정규분포 난수를 matrix array(n,m)으로 생성 
df = pd.DataFrame(np.random.randn(6,4), index = [i for i in range(6)] , columns = list('ABCD'))
display(df)


# #### np.where을 통한 조건부 정리

# In[ ]:


#np.where 
skimming_data2['group'] = np.where(skimming_data2['skimm'].between(4,6),'4~6',
                                  np.where(skimming_data2['skimm'].between(6,10),'7~10', '10~'))
# inull로 np where 
total_data['edge_crack'] = np.where(total_data['HFI 비고'].isnull(),0,1)


# 

# https://codetorial.net/numpy/random.html
