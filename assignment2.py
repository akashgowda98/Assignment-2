#!/usr/bin/env python
# coding: utf-8

# In[8]:


def last(n):
    return n[-1]  
   
def sort(tuples):
    return sorted(tuples, key=last)
   
print(sort([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


# In[16]:


alphabets = {}
for i in range(97,123):
    alphabets[chr(i)]=i
print(alphabets)


# In[ ]:




