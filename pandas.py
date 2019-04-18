#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


pd.Series(['A','B','C'],['1','2','3'])


# In[9]:


s=pd.Series({'name':'james','age':'26'})#插入字典，自动识别key为index


# In[16]:


#方法一：通过series生成
pd.DataFrame(s,columns=list('1'))


# In[21]:


#方法二：通过np数组
array=np.random.randint(10,size=(4,4))
array


# In[27]:


df=pd.DataFrame(array,index=list('1234'),columns=list('ABCD'))
df


# In[26]:


#方法三：excel导入 待续。。。


# In[29]:


#修改列名
df.rename(columns={'A':'a'})


# In[31]:


#修改index
df.rename(index={'1':'one'})


# In[32]:


#切片
df.iloc[1:]


# In[34]:


#数据统计
#筛选B列大于8，C列大于3的数据
df[(df['B']>8) & (df['C']>3)]


# In[35]:





# In[ ]:




