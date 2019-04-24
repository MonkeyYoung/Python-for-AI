#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib


# In[37]:


#解决中文乱码问题
matplotlib.use('qt4agg')
#指定默认字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family']='sans-serif'
#解决负号'-'显示为方块的问题
matplotlib.rcParams['axes.unicode_minus'] = False

#读取excel中的数据
data=pd.read_excel('2018-2019.xls',usecols=[1,24,25])
#获取姓名、得分、胜场列
names=data.iloc[:,0]
scores=data.iloc[:,1]
wins=data.iloc[:,2]
#获取列值
name=names.values
score=scores.values
win=wins.values

data={'score':score,'win':win}
plt.figure(figsize=(18,9))
plt.scatter('win','score',data=data)
for i in range(len(name)):
    plt.text(win[i],score[i],r''+name[i])
plt.ylabel('得分')
plt.xlabel('胜场')
plt.show()


# In[35]:

#获取配置文件
matplotlib.matplotlib_fname()


# In[ ]:




