#!/usr/bin/env python
# coding: utf-8

# In[10]:


import matplotlib.pyplot as plt
import numpy as np


# In[21]:


#第一个可视化内容，只提供一个列表的话默认是Y值，X值与Y值相同，但是X从0开始。
plt.plot([1,2,3,4,5])
plt.ylabel('some numbers')#y标签名
plt.show()


# In[4]:


#提供两个列表，第一个为x，第二个为y
plt.plot([1,2,3,4],[1,4,9,16])
plt.show()


# In[9]:


#plot 加入第三个参数，决定绘图的样式，参数来自命名：MATLAB
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.axis([0,8,0,24])#[xmin, xmax, ymin, ymax]设置x和y轴最大值和最小值
plt.show()


# In[20]:


#使用numpy数组生成图像，plot方法可加入多个x、y轴
t=np.arange(0,5,0.2)
plt.plot(t,t,'r--',t,t**2,'r--',t,t**3)
plt.show()


# In[8]:


#散点图
data={'a':np.arange(50),'c':np.random.randint(0,50,50),'d':np.random.randn(50)}
data['b']=data['a']+10*np.random.randn(50)
#np.abs 取绝对值
data['d']=np.abs(data['d'])*100
#plt.scatter(x,y,c,s,data) xy表xy轴，c表颜色，s表标量，data表。。。。
plt.scatter('a','b',c='c',s='d',data=data)
plt.xlabel('label a')
plt.ylabel('label b')
plt.show()
#plt.scatter参数详解


# In[54]:


#分类变量 多个绘图
names=['Harden','Curry','James','Durant','Antetokounmpo']
values=[36.1,27.3,27.4,28.8,26.3]
#设置整体绘图的宽高
plt.figure(figsize=(19,6))
#subplot(131) 1,3,1分别代表：总行数，总列数，第几个图
plt.subplot(131)
plt.bar(names,values)#直方图
plt.ylabel('score')

plt.subplot(132)
plt.scatter(names,values)#散点图
plt.ylabel('score')

plt.subplot(133)
plt.plot(names,values,linewidth=2.0)#折线图
plt.ylabel('score')

#标题
plt.suptitle('Rank')
plt.show()


# In[58]:


#使用多个图形和轴
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)
t1=np.arange(0,5.0,0.1)
t2=np.arange(0,5.0,0.02)

plt.figure(1)

plt.subplot(211)
plt.plot(t1,f(t1),'bo',t2,f(t2),'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()


# In[23]:


mu,sigma=100,15
x=mu+sigma*np.random.randn(10000)
#x为x轴，50代表有多少个直方图，alpha表示透明度
n,bins,patches=plt.hist(x,50,density=1,facecolor='g',alpha=0.75)
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')#标题
plt.text(60,.025,r'$\mu=100,\ \sigma=15$')#在指定位置标注
plt.axis([40,160,0,0.03])
plt.grid(True)#显示网格
plt.show()


# In[40]:


#ax=plt.subplot(111)
#注释
t=np.arange(0.0,5.0,0.01)
s=np.cos(2*np.pi*t)
line,=plt.plot(t,s,lw=2)#lw为linewidth
#xy 为注释的地方，xytext为注释文本的地方，arrowprops为箭头
plt.annotate('local max',xy=(2,1),xytext=(3,1.5),arrowprops=dict(facecolor='black',shrink=0.05),
            )
plt.ylim(-2,2)
plt.show()


# In[ ]:





# In[ ]:




