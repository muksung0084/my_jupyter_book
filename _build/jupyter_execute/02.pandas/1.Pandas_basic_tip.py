#!/usr/bin/env python
# coding: utf-8

# # Pandas basic _ tips 

# In[1]:


import pandas as pd 

<img src="0.dataframe_series_image.png" alt="drawing" width="500" /> from IPython.display import Image
Image("0.dataframe_series_image.png" , height=300 , width=500) # code안에서 나오게  

![title](dataframe_series_image.png) # markdown안에서 나오게 할 때.   
<img src="dataframe_series_image.png" alt="drawing" width="500" />  # markdown에서 사이즈 조절까지
                                                                                                                                                                            # https://lucycle.tistory.com/282
# ## Series, DataFrame sample 만들기

# In[2]:


my_series = pd.Series({"United Kingdom":"London", "India":"New Delhi", "United States":"Washington", "Belgium":"Brussels"})
display(pd.DataFrame(my_series))

my_dict = {"a": ['1', '3'], "b": ['1', '2'], "c": ['2', '4']}
display(pd.DataFrame(my_dict))

sample = pd.DataFrame({'type' : ['k','k','k','y','y','y','y','k'],
                       'a' : [1,2,3,4,5,6,7,np.NaN]},index=[1,2,3,4,5,6,7,8])

my_df = pd.DataFrame(data=[4,5,6,7], index=range(0,4), columns=['A'])
display(pd.DataFrame(my_df))

comp_mf34 = pd.DataFrame(
    columns=['5182','3104','6***','5***'],
    data=0,
    index=['mf3_batches','mf3_press_pv(std)','mf3_temp_pv(std)','mf4_batches','mf3_target_func','mf4_press_pv(std)','mf4_temp_pv(std)','mf4_target_func'])

comp_mf34.index.name = 'factors'
comp_mf34.columns.name = 'alloy'

display(comp_mf34)

