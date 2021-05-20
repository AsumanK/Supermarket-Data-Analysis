#!/usr/bin/env python
# coding: utf-8

# # SUPERMARKET SALES DATA ANALYSIS

# # Contents
# 1. Problem statement
# 2. Questions to answer
# 3. Getting the system ready and loading the data
# 4. Exploratory data analysis (EDA) using Pandas Profiling
# 5. Answers to questions

# # 1. Problem Statement
# The growth of supermarkets in most populated cities are increasing and market competitions are also high. The 
# dataset is one of the historical sales of supermarket company which has recorded in 3 different branches for 3 
# months data. We want to analyse the performance of the supermarket using the data provided.

# # 2. Questions
# 
# 1. The sales volume by different payments methods
# 2. The best-selling product lines
# 3. What is the prefered payment type of each branch
# 4. In relation to questions 1 and 2, according to the product line, does any payment method stand out?
# 5. Type of customer according to gender and city
# 6. What's the best time to offer online discounts
# 7. Type of Customer by Gender
# 8. Type of Customer by City
# 9. What's the best time to offer online discounts
# 10. What day of the week saw most sales?
# 11. What month generated the most income?
# 12. What was the average rating in each branch?

# # 3. Getting the system ready and loading the data
# 
# We will be using python for this project along with the below listed libraries.
# 
# - Python
# - Pandas
# - numpy
# - pandas profiling
# - Plotly express

# Loading packages

# In[1]:


import pandas as pd
import numpy as np              # for mathematical calculations
from pandas_profiling import ProfileReport
import plotly.express as px     # for plotting graphs
import plotly.graph_objects as go #for plotting grapphs
import warnings                 # to ignore any warnings
warnings.filterwarnings("ignore")


# # Data
# 
# - Data for this project will be downloaded from the link below.
# - https://www.kaggle.com/aungpyaeap/supermarket-sales

# Reading data

# In[2]:


df = pd.read_excel("/Users/asumankabugo/Desktop/supermarket_sales - Sheet1.xlsx")


# In[3]:


#copy of dataset
df_original = df.copy()


# # 4. Exploratory data analysis (EDA) using Pandas Profiling

# In[4]:


profile = ProfileReport(df, title="Pandas Profiling Report")
profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)
profile.to_widgets()


# In[5]:


profile.to_notebook_iframe()


# # 5. Answers to questions

# # 1. Sales volume by different payments methods

# In[6]:


payments = df.groupby(['Payment'])[['Total','Quantity']].apply(sum).reset_index().sort_values(by=['Total'], 
                                                                                              ascending = False)
payments.head()


# In[9]:


fig = px.bar(payments, x='Payment', y='Total', color= 'Payment',width=800,height=400)

fig.show()


# As you can see, there is no preferred payment method, but customers choose cash payments slightly more.

# # 2. The best-selling product lines

# In[10]:


products = df.groupby(['Product_line'])[['Total','Quantity']].apply(sum).reset_index().sort_values(by=['Total'], 
                                                                                                   ascending = False)
products.head()


# In[11]:


fig = px.bar(products, x='Product_line', y='Total', color= 'Product_line',width=800,height=500)

fig.show()


# Again, there is no product line that makes a real difference.

# # 3. What is the prefered payment type of each branch

# In[12]:


branch_payment= pd.DataFrame(df.groupby(by=['Branch','Payment'])['Total'].count()).reset_index().sort_values(by=['Total'], ascending = False)
branch_payment


# In[13]:


fig = px.bar(branch_payment, x='Branch', y='Total', color='Payment',text='Total',width=700,height=500)

fig.show()


# The preffered payment method is Ewallet in branch A followed by branch B and Cash in branch C.

# # 4. In relation to questions 1 and 2, according to the product line, does any payment method stand out?

# In[14]:


product_payment= pd.DataFrame(df.groupby(by=['Payment','Product_line'])['Total'].count()).reset_index().sort_values(by=['Total'], ascending = False)
product_payment


# In[15]:


fig = px.bar(product_payment, x='Payment', y='Total', color='Product_line',text='Total',width=700,height=500)

fig.show()


# Ewallet slightly stands out. 

# # 5. Type of customer according to gender and city

# In[16]:


customer_gen= pd.DataFrame(df.groupby(by=['Customer_type','Gender','City'])['Total'].count()).reset_index().sort_values(by=['Total'], ascending = False)
customer_gen


# In[32]:


fig = px.bar(customer_gen, x='Customer_type', y='Total', color='City',barmode='group',text='Gender',width=700,height=500)

fig.show()


# - Naypyitaw has slightly more Members(Customer type) with more females than men 
# - Yangon has more normal customers(customer type) with more males than females.

# # 7. Type of Customer by Gender

# In[18]:


cust_gen= pd.DataFrame(df.groupby(by=['Customer_type','Gender'])['Total'].count()).reset_index().sort_values(by=['Total'], ascending = False)
cust_gen


# In[19]:


fig = px.bar(cust_gen, x='Customer_type', y='Total', color='Gender',text='Total',barmode='group',width=700,height=500)

fig.show()


# More Females belong to Member customer type than men while Male are more than females in Normal customer type.

# In this case, the female gender is mostly committed to the brand.

# # 8. Type of Customer by City

# In[20]:


cust_city= pd.DataFrame(df.groupby(by=['Customer_type','City'])['Total'].count()).reset_index().sort_values(by=['Total'], ascending = False)
cust_city


# In[21]:


fig = px.bar(cust_city, x='Customer_type', y='Total', color='City',text='Total',barmode='group',width=700,height=500)

fig.show()


# Yangon has more Normal customer type followed by Mandalay then Naypyitaw while in Memeber customer type, Naypyitaw is slightly more than Yanon and Mandalay

# In relation to the second graph, in the city of Yangon, most of the customers are normal, which allows us to think
# about advertising campaigns to achieve greater loyalty.
# 

# # 9. What's the best time to offer online discounts

# Date transformations
# 
# - transform date into months
# - transform date into weekday
# - Extract hour from time

# In[22]:


# date transformation
df['Date'] = pd.to_datetime(df['Date'])

# transform into weekday
df['weekday'] = df['Date'].dt.day_name()

# transform into month
df['month'] = df['Date'].dt.month_name()

# We need to extract the hour from the ‘Date’ variable to do this analysis.
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S')

df['hour'] = df['Time'].dt.hour


# In[23]:


time= pd.DataFrame(df.groupby(by=['hour'])['Quantity'].sum()).reset_index().sort_values(by=['Quantity'], ascending = False)
time


# In[24]:


fig = px.bar(time, x='hour', y='Quantity', color='Quantity',width=700,height=400)

fig.show()


# The best time is 7 pm in the evening and 1 pm in the afternoon.

# # 10. What day of the week saw most sales?

# In[25]:


week= pd.DataFrame(df.groupby(by=['weekday'])['Quantity'].sum()).reset_index().sort_values(by=['Quantity'], ascending = False)
week


# In[26]:


fig = px.bar(week, x='weekday', y='Quantity', color='Quantity',width=700,height=400)

fig.show()


# Tuesday saw the most sales.

# # 11. What month generated the most income?

# In[27]:


month= pd.DataFrame(df.groupby(by=['month'])['Quantity'].sum()).reset_index().sort_values(by=['Quantity'], ascending = False)
month


# In[28]:


fig = px.bar(month, x='month', y='Quantity', color='Quantity',width=800,height=400)

fig.show()


# January generated the most sales

# # 12. Which branch has the highest rating? 

# In[29]:


branch_rating = pd.DataFrame(df.groupby(by=['Branch'])['Rating'].mean()).reset_index().sort_values(by=['Rating'], ascending = False)
branch_rating


# In[30]:


fig = px.bar(branch_rating, x='Branch', y='Rating', color='Rating',width=500,height=400)
fig.show()


# Branch C has the highest rating which is slightly higher than branch A.

# In[ ]:




