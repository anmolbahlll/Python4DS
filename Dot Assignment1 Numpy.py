#!/usr/bin/env python
# coding: utf-8

# # Assignment

# Import numpy as np

# In[1]:


import numpy as np


# Make a python list => \[1,2,3,4,5\]
# 
# Convert it into numpy array and print it
# 

# In[15]:


list1 = [1,2,3,4,5]
array1 = np.array(list1)
array1


# Make a python matrix (3 x 3) => \[[1,2,3],[4,5,6],[7,8,9]\]
# 
# Convert it into numpy array and print it

# In[16]:


mat1= [[1,2,3],[4,5,6],[7,8,9]]
np.array(mat1)


# Make a matrix (3 x 3) using built-in methods (like arange(), reshape() etc.):
# 
# \[ [1,3,5],
# 
#  [7,9,11],
#  
#  [13,15,17] \]

# In[29]:


ar=np.arange(1,19,2)
ar.reshape(3,3)


# In[30]:


ar.shape


# Create a numpy array with 10 random numbers from 0 to 10 (there should be few numbers greater than 1)

# In[56]:


from numpy import random
r=np.random.randint(0,3,10)
r


# Create numpy array => \[1,2,3,4,5\] and convert it to 2D array with 5 rows

# In[37]:


ar1=np.arange(1,6)
ar1.reshape(5,1)


# Print the shape of the above created array

# In[38]:


ar1.shape


# Create a numpy array with 10 elements in it. Access and print its 3rd, 4th and 9th element.

# In[44]:


ar1=np.arange(0,10)
ar1[2],ar1[3],ar1[8]


# Print alternate elements of that array

# In[46]:


ar1[0:10:2]


# In[47]:


ar1[1:10:2]


# Change last 3 elements into 100 using broadcasting and print

# In[48]:


ar1[-3:]=100
ar1


# Create a 5 x 5 matrix (fill it with any element you like), print it.
# 
# Then print the middle (3 x 3) matrix.

# In[84]:


p=np.arange(0,25)
p=p.reshape(5,5)
q=5
r=5
print(q)


# In[87]:


for i in range(q):
    for j in range(r):
        if ((i!=0)&(j!=0)&(i!=4)&(j!=4)):
            print(p[i][j], end = " ,") 
    print() 


# In[88]:


p[1:4,1:4]


# In[ ]:




