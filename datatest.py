#!/usr/bin/env python
# coding: utf-8

# In[42]:


#利用python实现栈，后进先出。
class Stack:
    #isEmpty 是否为空 push 放入 pop取出 peek 栈顶
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
s=Stack()


# In[43]:


s.push(1)


# In[44]:


s.push(2)


# In[45]:


s.push(3)


# In[46]:


s.push('xixi')


# In[47]:


s.isEmpty()


# In[50]:


s.peek()


# In[51]:


s.pop()


# In[52]:


s.size()


# In[ ]:




