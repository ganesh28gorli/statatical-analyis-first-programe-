#!/usr/bin/env python
# coding: utf-8

# # First programe

# In[3]:


# # calculate mean,standard deviation , variance,median and mode with using libraries for first column


# In[4]:


import pandas as pd
import numpy as np


# In[5]:


data=pd.read_excel('C:/Users/Ganesh/Downloads/stats.xlsx')


# In[6]:


print(data)


# In[7]:


yoe=np.array(data['YearsOfExp'])


# In[8]:


print(yoe)


# In[9]:


print('Mean:',+np.mean(yoe))
print('Standard Deviation:',+np.std(yoe))
print('Variance:',+np.var(yoe))
print('Median:',+np.median(yoe))
from scipy import stats
print(stats.mode(yoe))


# #calculate mean,standard deviation , variance,median and mode without using libraries for first column(YearOfExp)

# In[10]:


#Mean of the first coloumn without using the built in libraries


# In[11]:



n=len(yoe)
s=sum(yoe)
mean=s/n
print(mean)


# In[12]:


#standard deviation


# In[13]:


std_dev =np.sqrt(np.mean((yoe - np.mean(yoe)) ** 2 ))
print(std_dev)


# In[14]:


#calculate variance


# In[15]:


var = np.mean((yoe - np.mean(yoe)) ** 2)
print(var)


# In[16]:


#calculate median


# In[17]:


n = len(yoe) 
yoe.sort()
if n % 2 == 0: 
    median1 = yoe[n//2]
    print(median1)
    median2 = yoe[n//2 - 1] 
    print(median2)
    median = (median1 + median2)/2
else: 
    median = yoe[n//2] 
print("Median is: " + str(median)) 


# In[18]:


#calculate mode


# In[20]:


from collections import Counter 
# list of elements to calculate mode 
n = len(yoe) 
dat = Counter(yoe) 
print(dat)
get_mode = dict(dat) 
print(get_mode)
mode = [k for k, v in get_mode.items() if v == max(list(dat.values()))] 
  
if len(mode) == n: 
    get_mode = "No mode found"
else: 
    get_mode = "Mode is / are: " + ', '.join(map(str, mode)) 
      
print(get_mode) 

