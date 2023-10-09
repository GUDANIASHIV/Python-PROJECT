#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import seaborn as sns


# In[5]:


cs=pd.read_csv("D:\Diwali Sales Data.csv" , encoding='unicode_escape')
cs


# In[6]:


cs.shape


# In[6]:


cs.head(5)


# In[7]:


cs.info()


# In[8]:


pd.isnull(cs).sum()


# In[25]:


cs.dropna(inplace=True)


# In[26]:


pd.isnull(cs).sum()


# In[29]:


cs['Amount']=cs['Amount'].astype('int')


# In[31]:


cs['Amount'].dtype


# In[32]:


cs.columns


# In[33]:


cs.describe()


# # EXPLORATORY DATA ANALYSIS

# GENDER

# In[51]:


ax=sns.countplot(x='Gender',data=cs)
for bars in ax.containers:
    ax.bar_label(bars)
        



# In[62]:


sales_gen=cs.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sales_gen


# In[63]:


sns.barplot(x='Gender',y='Amount',data=sales_gen)


# From the above graphs we can conclude that most of the buyers are females and even their purchasing power is more than that 
# of males 

# # AGE

# In[69]:


sns.countplot(x='Age Group',data=cs,hue='Gender')


# In[71]:


ax=sns.countplot(x='Age Group',data=cs,hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)


# In[72]:


#total  amount v/s age group
sales_age=cs.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sales_age


# In[76]:


sns.barplot(x='Age Group',y='Amount',data=sales_age)


# From the above graphs we can see that most of the buyers lies in the 26-35 age group Females

# # State

# In[80]:


cs.columns


# In[101]:


sales_state=cs.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False)
sales_state.head(10)


# In[104]:


sns.set(rc={'figure.figsize' :(15,5)})
sns.barplot(x='State',y='Orders',data=sales_state.head(10))


# In[105]:


sales_state=cs.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sales_state.head(10)


# In[110]:


sns.set(rc={'figure.figsize' :(20,5)})
sns.barplot(x='State',y='Amount',data=sales_state.head(10))


# From the above graph we can see most of the orders and total sales/amount are from UP ,Maharashtra,Karnataka,Delhi respectively

# # Marital Status

# In[116]:


ax=sns.countplot(x='Marital_Status',data=cs)
sns.set(rc={'figure.figsize' :(6,5)})

for bars in ax.containers:
    ax.bar_label(bars)


# In[124]:


sales_marital=cs.groupby(['Marital_Status','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sales_marital


# In[125]:


sns.barplot(x='Marital_Status',y='Amount',data=sales_marital,hue='Gender')


# From the above graphs we can see that most of the buyers are married(women) and they have high purchasing power 

# # Occupation

# In[10]:


ax=sns.countplot(x='Occupation',data=cs)
sns.set(rc={'figure.figsize' :(10,5)})

for bars in ax.containers:
    ax.bar_label(bars)


# In[18]:


sales_oc=cs.groupby(['Occupation'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x='Occupation',y='Amount',data=sales_oc)
sns.set(rc={'figure.figsize' :(10,5)})


# From the above graphs we can see that most of the buyers are from IT ,Healthcare and Aviation sector

# # Product Category

# In[36]:


sns.set(rc={'figure.figsize' :(25,5)})
sns.countplot(x='Product_Category',data=cs)

for bars in ax.containers:
    ax.bar_label(bars)


# In[53]:


sales_pc=cs.groupby(['Product_Category'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(x='Product_Category',y='Amount',data=sales_pc)
sns.set(rc={'figure.figsize' :(20,5)})


# From the above graphs we can see most sold product_category are Food,Clothing and Electronics Gadgets

# In[ ]:


sales_pID=cs.groupby(['Product_ID'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False.head(10))
sns.barplot(x='Product_ID',y='Orders',data=sales_pID)
sns.set(rc={'figure.figsize' :(20,5)})


# # Conclusion:

# Married Women age group 26-35 yrs from UP,Maharashtra and Karnataka working in IT ,Healthcare and Aviation are more likely to buy products from food,clothing and electronics category

# In[ ]:




