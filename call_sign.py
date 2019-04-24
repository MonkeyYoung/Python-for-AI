#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import pandas as pd


# In[3]:


#读取数据
data=pd.read_excel('call_sign.xls')
#截取部门、姓名、通话量、签单量的列
depts=data.iloc[:,0]
names=data.iloc[:,1]
calls=data.iloc[:,2]
signs=data.iloc[:,3]
#获取数据
dept=depts.values
name=names.values
call=calls.values
sign=signs.values

data={'call':call,'sign':sign}
plt.figure(figsize=(16,8))
#设置xy最大最小值
plt.axis([0,300000,0,70])
plt.scatter('call','sign',data=data)
#标注
for i in range(len(name)):
    plt.text(call[i],sign[i],r''+dept[i]+name[i])
    
plt.title('1~3月 1中心签单量与通话量分析')
plt.ylabel('签单量')
plt.xlabel('通话时长(秒)')
plt.grid(True)
plt.show()


# In[ ]:




