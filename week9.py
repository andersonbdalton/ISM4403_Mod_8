#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# this is are first assignment in python exciting


# In[1]:


a = 3
b = 5


# In[7]:


3+5


# In[8]:


addTwoItems = a + b


# In[9]:


print(addTwoItems)


# In[10]:


c = addTwoItems


# In[11]:


print(c)


# In[12]:


createSomeString = c


# In[13]:


print(createSomeString)


# In[29]:


thirdNumber = createSomeString


# In[30]:


print(thirdNumber)


# In[26]:


i = range(1, 101)


# In[39]:


num = 0
while num <= 100:
    num +=1
    if num % 10 ==0:
        print(str(num) + " , ", end = " ")
        


# In[38]:


num = 0
while num <= 100:
    num +=1
    if num % 10 == 0 and num <= 79:
        print(str(num) + " , ", end = " ")


# In[43]:


if c <= 5:
    print("Hello World")
elif c >= 5:
    print("Goodnight World")

