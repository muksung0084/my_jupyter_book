#!/usr/bin/env python
# coding: utf-8

# ## Data visualization

# In[ ]:




[공식 도큐먼트] https://seaborn.pydata.org/api.html

[세부 도큐먼트 확인하기]
https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
# #### Matplotlib 
line: 선그래프

bar: 바 그래프
barh: 수평 바 그래프

hist: 히스토그램

kde: 커널 밀도 그래프

hexbin: 고밀도 산점도 그래프

box: 박스 플롯

area: 면적 그래프

pie: 파이 그래프

scatter: 산점도 그래프
# 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv('https://bit.ly/ds-house-price-clean')


# 

# In[3]:


a=['X','Y','Z']
b=[1,2,4]
c=[6,7,8]
plt.plot(a,b,marker='o',markersize=5,linestyle='--',color='r',alpha=0.5)
plt.plot(a,c,marker='o',markersize=5,linestyle='--',color='b',alpha=0.5)

plt.title('Title',fontsize=10)
plt.xlabel('x축',fontsize=10)
plt.ylabel('y축',fontsize=10)
plt.xticks(rotation=90)
plt.yticks(rotation=30)
plt.legend(['빨','파'],fontsize=10)

plt.ylim(1,10)
plt.grid()
plt.show()


# In[ ]:





# In[4]:


# hist --> histogram 도수분포표 
plt.hist(df['지역'])
plt.figure()

df_count.plot(kind='kde')
plt.show


# In[ ]:





# In[ ]:


#line 
#--> index가 숫자로 되어있는데 만약 index를 연도로 표현 한다면!?
df_seoul=df.loc[df['지역']=='서울']
df_seoul_year=df_seoul.groupby('연도').mean()
df_seoul_year.plot(kind='line')


# In[ ]:





# In[ ]:


plt.rcParams["figure.figsize"] = (10, 3)
a=df.groupby('지역')['분양가'].mean().reset_index()#a라는 공통된 데이터프레임 --> 공통된 index를 가지고 있다. 
b=df.groupby('지역')['분양가'].max().reset_index()
c=df.groupby('지역')['분양가'].min().reset_index()

plt.plot(a['지역'],a['분양가'],label='mean',color='red',alpha=0.7,marker='*')
plt.plot(b['지역'],b['분양가'],label='max',color='orange',alpha=0.7,linestyle='--')
plt.plot(c['지역'],c['분양가'],label='min',color='black',alpha=1,linestyle=':')
plt.legend()  # 내가 설정한 범례(label)을 출력하겠다.

plt.title('line 그래프',fontsize=10)
plt.xlabel('지역',fontsize=10)
plt.ylabel('분양가',fontsize=10)
plt.grid()
plt.show()

#x에 대한 y값이 붙을때 기준은 index이다... 
#x와 y에 대한 값이 list 혹은 array 타입은 순서대로 쭉 열거되어 있다면, 그 순서대로 값이 박힘.
#data frame 형태에서 index가 부여된 상태에서는 그 값은 index값 별로 매칭된다 
# 즉 df과 list,array 타입을 가지고 plot을 만드려고 하면 그 값들은 매칭이 안됨. 지역값 분양가 값이 다 있어도 얘는 index 매칭이 안되기 때문에 


# In[ ]:





# In[ ]:


#잘못된 예시 
# x는 array 타입으로 그냥 글자 순서대로 박혀있음 
# y는 지역이 index로 잡혀있는 시리즈 타입 
# 둘의 갯수는 같으니까 그냥 그 순서대로 그래프에 값이 찍힘 
# 때문에 지역명에 따른 y값의 수치가 다름 정확하지 않음
# y도 x의 지역명 순서에 맞게 열거를 시켜주거나 
# 둘사이의 공통 index가 존재해야 정확한 그래프를 나타낼 수 있음 
# 또한 기본적으로 demension이 같아야 하지만, 그래프는 하나하나의 값들을 가져오는 거니까 기본적으로 1차원 값이어야 함. 
print(type(df['지역'].unique()))
a=df.groupby('지역')['분양가'].mean()
print(type(a))


# In[ ]:





# In[ ]:


# area
df.groupby('연도')['분양가'].mean().plot(kind='area')


# In[ ]:





# In[ ]:


# scatter 
df.plot(kind='scatter',x='월',y='분양가')


# In[ ]:





# In[ ]:


x=np.arange(1,10,0.1)
print(x)
y=np.sin(x)
y2=np.cos(x)

plt.fill_between(x,y,alpha=0.4,color='red',label='sin')
plt.fill_between(x,y2,alpha=0.5,color='blue',label='cos')
plt.xticks(rotation=45)
plt.plot(x,y) # 첫번째 area 그래프에 line을 한번 더 그려주면서 라인을 조금더 굵게 부각 시켜줌 
plt.plot(x,y2)
plt.legend()

plt.ylim(-1,1) ## 부분 확대시키기. 
plt.xlim(1,10)
plt.show()


# In[ ]:





# In[ ]:


#bar      //  .plot(kind='bar')
plt.bar(df['지역'],df['분양가'],label='mean',color='orange')
plt.xlabel('지역')
plt.ylabel('분양가')
plt.legend()
plt.figure()

plt.barh(df['지역'],df['분양가'])
plt.figure()

plt.bar(df['지역'],df['분양가'],label='max')
plt.xlabel('지역')
plt.ylabel('분양가')
plt.legend()
plt.show()


# In[ ]:





# In[ ]:


a = df.groupby('지역')['분양가'].mean().reset_index()
b = df.groupby('지역')['분양가'].max().reset_index()

plt.rcParams["figure.figsize"] = (8, 5)
x=np.arange(len(a['지역'])) 

fig, axes = plt.subplots()
axes.bar(x - 0.35/2,a['분양가'],0.35,align ='center',alpha=0.8,color='blue',label='mean')  # --> center는 x값기준 중앙정렬 위치 , edge는 오른정렬 
axes.bar(x + 0.35/2,b['분양가'],0.35,align ='edge',alpha=0.8,color = 'red',label='max')
plt.title('제목',color='grey',fontsize=20)
plt.legend()
plt.xticks(x,rotation=90)
axes.set_xticklabels(a['지역'])

#plt.grid()
plt.show()


# In[ ]:





# In[ ]:


z=df.loc[df['지역'].isin(['서울','경기','대전','세종'])]
z1=z.groupby('지역')['분양가'].mean()

plt.rcParams["figure.figsize"] = (8, 5)
# 기본형 --> df.groupby('지역')['분양가'].mean().plot(kind='pie')
# texts, autotexts 인자를 활용하여 텍스트 스타일링을 적용합니다
#fig,axes = plt.subplots(2,2)
patches, texts, autotexts = plt.pie( z1,
                                    labels=z1.index,
                                    explode=(0,0,0.3,0),
                                    autopct='%1.1f%%',
                                    shadow=True, 
                                    startangle=90)
plt.title('pie data',fontsize=20)
# label 텍스트에 대한 스타일 적용
for t in texts:
    t.set_fontsize(10)
    t.set_color('gray')
    
# pie 위의 텍스트에 대한 스타일 적용
for t in autotexts:
    t.set_color("white")
    t.set_fontsize(18)


# In[ ]:





# In[ ]:


## **5-2 seaborn으로 시각화** 

sns.set(style='darkgrid')
## data sample 가져오기 
tips = sns.load_dataset('tips')
titanic = sns.load_dataset('titanic')


# In[ ]:





# In[ ]:


df_count.plot(kind='kde')
plt.show()


# In[ ]:


### **Box plot**
**제일 많이쓰이고 중요한 box plot**

박스 안의 횡선 --> 중간값 (median) 

박스의 윗변 --> 3/4 상위 75%값

박스의 아랫변 --> 1/4 하위 25%값

맨 위의 선 --> 이 box plot mechanism에서 구하는 추정 max값

맨 아래의 선 --> 이 box plot mechanism에서 구하는 추정 min값

위 아래에 생기는 동그라미 점 --> outlier로 헌팅값  --> data상에 값이 있지만 25%~75% 사이의 값을 기준으로 볼때 이 data의 max,min은 이정도에 있어야 하는데 그값을 벗어나는 값을 outlier로 처리함 --> outlier가 많다면 data상의 기록되는 값에 이상이 있을 수 도 있다는 의심을 해볼 필요있음.

###   max 값 산정 방식 :
###   IPQ=inter quantile range (내부 퀀타일 범위 측정값 ) ==> (75%value - 25%value)*1.5

> ### max = 75%value(3632)+IQR 

> ### min = 25%value(2478)-IQR


# In[ ]:





# In[ ]:


seoul=df.loc[df['지역']=='서울','분양가']
daejeon=df.loc[df['지역']=='대전','분양가']
plt.boxplot([seoul,daejeon])
plt.figure()

data=[seoul,daejeon]
outlier_marker = dict(markerfacecolor='r', marker='D') # 아웃라이어 설정 

plt.boxplot(data, flierprops=outlier_marker, vert=False) # 뉘어 보고 싶을땐  vert = False 옵션 넣어준다. 
plt.yticks([1,2],['서울','대전'])
plt.show()


# In[ ]:





# In[ ]:


v=df.loc[df['지역'].isin(['서울']),['분양가','지역']]
sns.boxplot(x='지역',y='분양가',data=v, orient='v',width=0.3)    # 단일로 할땐, width & orient = vertical의 'v' 


# In[ ]:





# In[ ]:


sns.boxplot(df['지역'],df['분양가'],orient='v',width=0.3, flierprops=outlier_marker)
#(x= , y= ,data= ) 해도 되고 그냥 data[] a컬럼 해도 됨, 


# In[ ]:





# In[ ]:


#violinplot : max값과 min값 그리고 각 값의 분포도를 바이올린 형태의 모양으로 보여준다.  x와 y에 대한 값이 필요 
sns.violinplot(y=tips['tip'],color='red',height=5)
plt.figure()
sns.violinplot(x=tips['day'],y=tips['tip'],hue=tips['time'],palette='rainbow')   #hue옵션 빼면 그냥 하나씩 단일그림으로나옴/ hue옵션 적용 : 사이즈별 - 타임때별 tip의 트랜드 --> 하지만 size에 묶여 두개씩 표현 --> 비교하기가 조금 애매함 이럴때 split을 써준다 
plt.figure()
sns.violinplot(x=tips['day'],y=tips['tip'],hue=tips['time'],split=True,palette='rainbow') 


# In[ ]:





# In[ ]:


#SNS scatter plot
x = np.random.rand(50)    #x축 값
y = np.random.rand(50)    #y축 값
colors = np.arange(50)    # 해당 (x,y)의 점의 색깔  --> 숫자별로 color가 다른 값을 가지고 있음
area = x * y * 1000       # 해당 (x,y)의 점의 크기 

sns.scatterplot(x,y,color='red',alpha=0.3)
plt.show()


# In[ ]:





# In[ ]:


#countplot : 항목별 개수를 세어주는 plot
sns.countplot(data=titanic,x='class',hue='who')
plt.show()


# In[ ]:


sns.distplot(tips['tip'],color='red',rug=True)   # 히스토를 없애고 싶다면 : hist=False추가 , 가로로 보고싶다면 vertical=True 추가 
#distplot 중 rug기능 --> 작은 눈금으로 data의 값들이 어느 값에서 주로 분포하는지 실제를 파악할 수 있음


# In[ ]:


sns.jointplot(x="total_bill", y="tip", height=5, data=tips)
plt.show()


# In[ ]:


#밀도를 보고싶으면 kind =hex 추가   --> kind가 가운데 그래프에 더 많은 영향을 준다  --> side에 표시되는 그래프는 대부분 hist 
sns.jointplot(x="total_bill", y="tip", height=5, data=tips,kind='hex',color='red')


# In[ ]:


#★heatmap  :  상관관계 파악시 많이 사용 !!   --> 내가 보고싶은 특정 column과 column간의 value 관계를 알 수 있음 
# 따라서 보고픈 컬럼과 컬럼을 가지고 pivort를 만들어 줘야함.    x와 y 값이 있어야함. 즉 index와 columns 이 독립되어 있어야함. 그리고 이를 기준으로 존재하는 값value가 있어야함

a=tips.pivot_table(index='day',columns='size',values='tip')
sns.heatmap(a,annot=True,cmap='Blues')  # annot은 칸 안에 value값을 표현해줌 


# In[ ]:





# In[ ]:


#★correlation : column과 column간의 상관계수 파악 가능 
tips.corr()
# 표로 보면 수치값이라 파악이 힘듬 --> 이를 heatmap으로 연동 
sns.heatmap(tips.corr(),annot=True)


# In[ ]:





# In[ ]:


#★★pairplot : 기본적으로 컬럼과 컬럼들 간의 분포도를 나타냄 기본적으로 scatter 형식 컬럼 겹치면 hist  & subplots를 적용한듯 볼 수 있다. 
sns.pairplot(tips, hue='time',palette="rainbow",height=3)


# In[ ]:





# In[ ]:


sns.lmplot(x='total_bill',y='tip',data=tips)   # only numerical value


# In[ ]:





# In[ ]:


#추가적인 옵션 col --> 컬럼을 추가하는 것 
sns.lmplot(x='total_bill',y='tip',hue='time',col='size',data=tips,palette='CMRmap_r') 


# In[ ]:





# In[ ]:


#relplot : lmplot과 유사함  하지만. 선형은 표시해 주지 않음 
sns.relplot(x='total_bill',y='tip',data=tips,hue='time',col='size',palette='CMRmap_r')


# In[ ]:


#col에 추가하여 row를 적용할 수 있음  --> 즉, x를에 대한 data값을 추가로 나누어 주면서 더욱 세분화 가능
sns.relplot(x='total_bill',y='tip',data=tips,hue='time',col='size',row='sex',palette='CMRmap_r')
#totalbill (x) 중time별 (hue) 남성고객이 (row) 낸 tip값(y) 에서 y를 size별로 나누어 나타낸 값 분포.  역시 col_wrap으로 세분화 가능. 


# In[ ]:





# In[ ]:


# **++subplots**

## plotlib x_limtit. y_limit 
## scale 조절 

### fig,axes=plt.subplots(x,y)

### axes[x1,y1].plot(data)


# In[ ]:





# In[ ]:


# subplots()
# subplot보다 보다 직관적으로 해당 data들을 위치시키고 싶은 경우 
# 먼저 프레임을 만들어 놓고 그안에 (x,y)로 지정 

fig, axes = plt.subplots(2,2)

axes[0,0].plot(df.groupby('지역').count())
axes[0,1].set_xlim(0,10)
axes[0,1].set_ylim(0,10)

axes[1,1].plot(df.groupby('지역').count()) 
plt.tight_layout() # subplots의 배치를 조금더 깔끔하고 이쁘게 정리해 주는 기능.
plt.show()


# In[ ]:





# In[ ]:


# **twinx**


# In[ ]:


fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(tips.index,tips['total_bill'] , color = 'blue' , label = 'total_bill')
ax1.legend(loc = 'upper left')
ax1.set_ylabel('ax1 제목', color='b',size =12,weight='bold')
ax1.set_ylim(0,50)
 
ax1.tick_params(axis='x', direction='in', length=3, pad=6, labelsize=20, labelcolor='blue', top=True)
ax1.tick_params(axis='y', direction='in', length=3, pad=6, labelsize=20, labelcolor='black', top=True) 

ax2.plot(tips.index,tips['tip'] , color = 'red' , label = 'tip')
ax2.legend(loc = 'upper right')
ax2.set_ylabel('ax2 제목', color='r',size =12,weight='bold')
ax2.set_ylim(0,100)
ax2.tick_params(axis='y', direction='in', length=13, pad=6, labelsize=14, labelcolor='red', top=True)

plt.show()

# plt.tick_params(axis='x', direction='in', length=3, pad=6, labelsize=14, labelcolor='black', top=True)
# plt.tick_params(axis='y', direction='in', length=3, pad=6, labelsize=14, labelcolor='black', top=True)

