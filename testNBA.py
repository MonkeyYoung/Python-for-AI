#!/usr/bin/env python
# coding: utf-8

# In[56]:


import matplotlib.pyplot as plt
import matplotlib
import numpy as np
#以下为解决中文乱码问题
matplotlib.use('qt4agg')
#指定默认字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family']='sans-serif'
#解决负号'-'显示为方块的问题
matplotlib.rcParams['axes.unicode_minus'] = False

#x为总胜场
x=np.array([498,354,224,97,798,462,352,75,528,216,311,245,249,359,141,278,95,85,501,432])
#y为总得分
y=np.array([18627,11983,8745,3833,32543,16315,8250,5820,22940,11059,12909,12009,9684,13200,7187,11294,3445,4710,18859,11995])
#n为球员姓名
n=np.array(['詹姆斯-哈登','保罗-乔治','扬尼斯-阿德托昆博','乔尔-恩比德','勒布朗-詹姆斯','斯蒂芬-库里','科怀-伦纳德','德文-布克',
           '凯文-杜兰特','安东尼-戴维斯','达米安-利拉德','肯巴-沃克','布拉德利-比尔','布雷克-格里芬','卡尔-安东尼-唐斯','凯里-欧文',
           '多诺万-米切尔','扎克-拉文','拉塞尔-威斯布鲁克','克莱-汤普森'])
data={'a':x,'b':y}
plt.figure(figsize=(16,8))
plt.scatter('a','b',data=data)
for i in range(n.size):
    plt.text(x[i]+5,y[i],r''+n[i])
plt.ylabel('总得分')
plt.xlabel('总胜场')
plt.show()










