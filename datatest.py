#!/usr/bin/env python
# coding: utf-8

# In[1]:


#利用python实现栈，后进先出。
class Stack:
    #isEmpty 是否为空 push 放入 pop取出 peek 栈顶 size大小
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)


# In[23]:


#利用python实现队列，先进先出。
class Queue:
    #isEmpty 是否为空 push 放入 pop 取出 peek 队列顶 size 大小
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop(0)
    def peek(self):
        return self.items[0]
    def size(self):
        return len(self.items)


# In[24]:


q=Queue()


# In[25]:


q.isEmpty()


# In[26]:


q.push(3)


# In[27]:


q.push(5)


# In[28]:


q.push(7)


# In[29]:


q.peek()


# In[31]:


q.peek()


# In[33]:


q.pop()


# In[34]:


q.peek()


# In[ ]:




