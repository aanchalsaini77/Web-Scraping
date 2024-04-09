#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup


# In[2]:


import requests


# In[3]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


# In[4]:


print(soup)


# In[5]:


soup.find_all('table')[0]


# In[6]:


soup.find('table',class_='wikitable sortable sticky-header-multi sort-under')


# In[7]:


table = soup.find_all('table')[0]


# In[8]:


print(table)


# In[9]:


titles_h= table.find_all('th')[1:10]


# In[10]:


print(titles_h)


# In[11]:


titles_table_h = [title.text.strip() for title in titles_h]


# In[12]:


print(titles_table_h)


# In[13]:


import pandas as pd


# In[14]:


df = pd.DataFrame(columns = titles_table_h )


# In[15]:


df


# In[16]:


column_data = table.find_all('tr')
print(column_data)


# In[17]:


for row in column_data[2:]:
    row_data = row.find_all('td')
    each_row_data =  [data.text.strip() for data in row_data]


    length = len(df)
    df.loc[length] = each_row_data


# In[18]:


df


# To turn the file into "csv" file
# 
# **df.to_csv = (r'path)
# 

# In[ ]:




