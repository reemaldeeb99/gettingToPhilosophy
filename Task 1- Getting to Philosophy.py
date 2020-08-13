#!/usr/bin/env python
# coding: utf-8

# # Task 1 - Getting to Philosophy

# ## BeautifulSoup and Resquests libraries are used 

# In[50]:


from bs4 import BeautifulSoup
import requests


# In[53]:


url = "https://en.wikipedia.org/wiki/Special:Random"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
print(soup.prettify())

#get all the html tags in the site


# In[62]:


soup.find_all("a")
#get only the ahref (links) tags from the site


# In[63]:


# next step is to select only the "Normal ahref Links" and perform a loopliteration 
# by clicking the links programatically until the getting to philosophy page is reached 
# unfortunately that is all i could reach in this task as I'm not experienced with pythin programming yet
# so I'm not fully aware of all the libraries, syntax and whatnot.
    


# In[ ]:




