#%%
import numpy as np
#%%生成随机一维数组
array1 = np.random.randint(10, size=4)
array1
#%%生成随机二维数组
array2 = np.random.randint(10, size=(4, 3))
array2
#%%生成随机三维数组
array3=np.random.randint(10,size=(2,3,4))
array3
#%%获取形状
array2.shape
#%%获取维度
array3.ndim
#%%获取字节数
array3.nbytes
#%%变形为3行4列的数组
rearray=array2.reshape(3,4)
rearray
#%%创建指定数组
a=np.array([1,2,3])
a
#%%横向拼接数组
b=np.array([4,5,6])
np.concatenate([a,b])
#%%纵向拼接数组
np.vstack([a,b])
#%%格式化数组
np.zeros((2,3),int)
#%%利用格式化
