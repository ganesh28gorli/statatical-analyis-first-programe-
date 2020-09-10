#!/usr/bin/env python
# coding: utf-8

# # second programe

# In[20]:


# # calculate mean,standard deviation , variance,median and mode with using libraries for second column(Salary in Rs.)


# In[38]:


import pandas as pd
import numpy as np


# In[39]:


data=pd.read_excel('C:/Users/Ganesh/Downloads/stats.xlsx')


# In[40]:


print(data)


# In[41]:


sir=np.array(data['Salary in Rs.'])


# In[42]:


print(sir)


# In[43]:


print('Mean:',+np.mean(sir))
print('Standard Deviation:',+np.std(sir))
print('Variance:',+np.var(sir))
print('Median:',+np.median(sir))
from scipy import stats
print(stats.mode(sir))


# In[44]:


#calculate mean,standard deviation , variance,median and mode without using libraries for first column(Salary in Rs.)


# In[45]:


#Mean of the second coloumn without using the built in libraries


# In[46]:



n=len(sir)
s=sum(sir)
mean=s/n
print(mean)


# In[47]:


#standard deviation


# In[48]:


std_dev =np.sqrt(np.mean((sir - np.mean(sir)) ** 2 ))
print(std_dev)


# In[49]:


#calculate variance


# In[50]:


var = np.mean((sir - np.mean(sir)) ** 2)
print(var)


# In[51]:


#calculate median


# In[52]:


n = len(sir) 
sir.sort()
if n % 2 == 0: 
    median1 = sir[n//2]
    print(median1)
    median2 = sir[n//2 - 1] 
    print(median2)
    median = (median1 + median2)/2
else: 
    median = sir[n//2] 
print("Median is: " + str(median)) 


# In[53]:


#calculate mode


# In[54]:


from collections import Counter 
# list of elements to calculate mode 
n = len(sir) 
dat = Counter(sir) 
print(dat)
get_mode = dict(dat) 
print(get_mode)
mode = [k for k, v in get_mode.items() if v == max(list(dat.values()))] 
  
if len(mode) == n: 
    get_mode = "No mode found"
else: 
    get_mode = "Mode is / are: " + ', '.join(map(str, mode)) 
      
print(get_mode) 


# In[ ]:




