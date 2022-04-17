#!/usr/bin/env python
# coding: utf-8

# In[1]:


def majorizing(a,b):
    for k in range(1,len(a)+1):
        if sum(a[0:k])<sum(b[0:k]):
            return(False)
            break
    return(True)


# In[2]:


L=[]
for g in graphs(7,size=6):
    k=g.degree_sequence()
    add='y'
    for l in L:
        if majorizing(l,k):
            add='n'
    if add=='y':
        L.append(k)
print(L)


# In[3]:


L=[]
for g in graphs(6,size=5):
    k=g.degree_sequence()
    add='y'
    for l in L:
        if majorizing(l,k):
            add='n'
    if add=='y':
        L.append(k)
print(L)


# In[4]:


L=[]
for g in graphs(5,size=4):
    k=g.degree_sequence()
    add='y'
    for l in L:
        if majorizing(l,k):
            add='n'
    if add=='y':
        L.append(k)
print(L)


# In[ ]:




