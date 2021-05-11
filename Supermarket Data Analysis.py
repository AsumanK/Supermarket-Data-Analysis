#!/usr/bin/env python
# coding: utf-8

# # SUPERMARKET SALES DATA ANALYSIS 

# # Contents
# 
# 1. Problem statement 
# 2. Questions to answer
# 3. Getting the system ready and loading the data
# 4. Understanding the data
# 5. Exploratory data analysis (EDA)
# -	Univariate analysis
# -	Bivariate analysis
# 6. Missing value and outlier treatment
# 

# # 1. Problem Statement
# 
# - The growth of supermarkets in most populated cities are increasing and market competitions are also high. 
# The dataset is one of the historical sales of supermarket company which has recorded in 3 different branches for 
# 3 months data. We want to analyse the performance of the supermarket using the data provided.

# # 2. Questions 
# 
# 1. What gender had most sales?
# 2. What was the average income in both genders?
# 3. What customer type had most sales?
# 
# 4. Which product line had most sales?
# 5. Which city experienced most sales?
# 6. What was the most popular payment method?
# 7. Which branch had most sales?
# 8. What is the distribution of gross income?
# 9. What does the customer rating look like?
# 10. What was the total aggregate sales in each branch?
# 11. What was the total aggregate sales in each city?
# 12. What was the average rating in each branch?
# 13. What was the number of sales in each product line?
# 14. What was the total income and count in each product line among males and females?
# 15. Which month generated the most income?
# 16. What day of the week generated the highest income?
# 17. What time of the day was the busiest?
# 18. Which product line had the highest quantity of sales?
# 19. What was the average unit price in each product line?
# 

# # 3. Getting the system ready and loading the data
# 
# We will be using python for this project along with the below listed libraries.
# - Python
# - Pandas
# - numpy
# - Plotly express
# 
# Loading packages
# 

# In[1]:


import pandas as pd
import numpy as np              # for mathematical calculations
import plotly.express as px     # for plotting graphs
import plotly.graph_objects as go #for plotting grapphs
import warnings                 # to ignore any warnings
warnings.filterwarnings("ignore")


# Data 
# 
# - Data for this project will be downloaded from the link below.
# - https://www.kaggle.com/aungpyaeap/supermarket-sales
# 
# Reading data

# In[2]:


df = pd.read_excel("/Users/asumankabugo/Desktop/supermarket_sales - Sheet1.xlsx")


# In[3]:


#copy of dataset
df_original = df.copy()


# # 4. Understanding the Data
# 
# - In this section, we will look at the structure of the dataset. Firstly, we will check the features present in 
# our data and then then we will look at their data types.
# 

# In[4]:


df.columns


# # Description of each variable in the dataset
# 
# - Invoice id: Computer generated sales slip invoice identification number
# 
# - Branch: Branch of supercentre (3 branches are available identified by A, B and C).
# 
# - City: Location of supercentres
# 
# - Customer type: Type of customers, recorded by Members for customers using member card and Normal for without member card.
# 
# - Gender: Gender type of customer
# 
# - Product line: General item categorization groups - Electronic accessories, Fashion accessories, Food and beverages, Health and beauty, Home and lifestyle, Sports and travel
# 
# - Unit price: Price of each product in $
# 
# - Quantity: Number of products purchased by customer
# 
# - Tax: 5% tax fee for customer buying
# 
# - Total: Total price including tax
# 
# - Date: Date of purchase (Record available from January 2019 to March 2019)
# 
# - Time: Purchase time (10am to 9pm)
# 
# - Payment: Payment used by customer for purchase (3 methods are available – Cash, Credit card and Ewallet)
# 
# - COGS: Cost of goods sold
# 
# - Gross margin percentage: Gross margin percentage
# 
# - Gross income: Gross income
# 
# - Rating: Customer stratification rating on their overall shopping experience (On a scale of 1 to 10)
# 

# In[5]:


# print data types for each varibale
df.info()


# We can see there are three formats of data types
# - Object: object format means variables are categorical. Categorical variables in our dataset are:
# - Int64: It represents the integer variables. 
# - Float64: It represents the variable which have some decimal values involved. They are also numerical variables.  
# 
# The dataset doesn't contain any missing values

# In[6]:


# lets look at the shape of the dataset
df.shape


# We have 1000 rows and 17 columns

# Summary Statistics

# In[7]:


# summary statistics
df.describe()


# Date transformations
# 
# - transform date into months
# - transform date into weekday
# - Extract hour from time

# In[8]:


# date transformation
df['Date'] = pd.to_datetime(df['Date'])

# transform into weekday
df['weekday'] = df['Date'].dt.day_name()

# transform into month
df['month'] = df['Date'].dt.month_name()

# We need to extract the hour from the ‘Date’ variable to do this analysis.
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S')

df['hour'] = df['Time'].dt.hour


# In[9]:


df.head()


# # 5. Exploratory Data Analysis (EDA)

# Univariate Analysis
# 
# - In this section, we will do univariate analysis. It is the simplest form of analysing data where we examine each 
# variable individually. This will answer most questions. For categorical features, we can use frequency table or 
# bar plots which will calculate the number of each category in a particular variable. For numerical features, 
# probability density plots can be used to look at the distribution of the variable.
# 
# Now lets visualise each variable separately. Different types of variable are categorical, ordinal and numerical.
# - Categorical features: These features have categories (Customer type, gender, and payment)
# - Ordinal features: Variables in categorical features having some order involved (Branch, City, Product line)
# - Numerical features: These features have numerical values (
# 

# Let’s visualise categorical features
# 
# Independent variable (Categorical)
# 

# # Query 1: What gender had most sales?

# In[10]:


df["Gender"].value_counts()


# In[11]:


fig = px.bar(df, x='Gender', color='Gender', title='Gender Count')
fig.show()


# # Query 2: What was the average income in both genders?

# In[12]:


df.groupby(by='Gender')['gross_income'].mean()


# In[13]:


df.query("Gender=='Male'")['gross_income'].sum()


# # Query 3: What customer type had most sales?

# In[14]:


df["Customer_type"].value_counts()


# In[15]:


fig = px.bar(df, x='Customer_type', color='Customer_type', title='Customer type Count')
fig.show()


# # Independent(ordianl)

# # Query 4: Which product line had most sales?

# In[16]:


df['Product_line'].value_counts()


# In[17]:


fig = px.bar(df, x='Product_line', color='Product_line', title='Product line Count')
fig.show()


# # Query 5: Which city experienced most sales?

# In[18]:


df['City'].value_counts()


# In[19]:


fig = px.bar(df, x='City', color='City', title='City count')
fig.show()


# # Query 6: What was the most popular payment method?

# In[20]:


df['Payment'].value_counts()


# In[21]:


fig = px.bar(df, x='Payment', color='Payment', title='Payment count')
fig.show()


# # Query 7: Which branch had most sales?

# In[22]:


df['Branch'].value_counts()


# In[23]:


fig = px.bar(df, x='Branch', color='Branch', title='Branch count')
fig.show()


# # Independent Variable (Numerical)
# 
# Let’s visualise the numerical variables, gross income and ratings
# 

# # Query 8: What is the distribution of Gross income?

# In[24]:


fig = px.histogram(df, x="gross_income")

fig.show()

fig = px.box(df, y="gross_income")
fig.show()


# It can be inferred that most gross income data is leaning on the left.
# 
# The box plot confirms the presence of outliers. This can be atttributed to the amount of goods bought. 

# # Query 9: What does the customer rating look like?

# In[25]:


fig = px.histogram(df, x="Rating")

fig.show()

fig = px.box(df, y="Rating")
fig.show()


# It can be observed that the rating data is evenly distributed.
# 
# The box plot confirms 7 as median, 10 as maximum and 4 as minimum.

# # Query 10: What was the total aggregate sales in each branch?

# In[26]:


df.groupby(by='Branch')['gross_income'].sum()


# In[27]:


df1 = pd.DataFrame(df.groupby(by=['Branch'])['gross_income'].sum())

df1.reset_index(inplace=True)

fig = px.bar(df1, x='Branch', y='gross_income', color='Branch', barmode='group', text='gross_income')

fig.show()


# # Query 11: What was the total aggragate sales in each city?

# In[28]:



df2 = pd.DataFrame(df.groupby(by=['City'])['gross_income'].sum())
df2.reset_index(inplace=True)
fig = px.bar(df2, x='City', y='gross_income', color='City', barmode='group', text='gross_income')

fig.show()


# # Query 12: What was the average rating in each branch?

# In[29]:


df4 = pd.DataFrame(df.groupby(by=['Branch'])['Rating'].mean())
df4.reset_index(inplace=True)
fig = px.bar(df4, x='Branch', y='Rating', color='Branch', barmode='group', text='Rating')

fig.show()


# # Query 13:What was the number of sales in each product line?

# In[30]:


df5 = pd.DataFrame(df.groupby(by=['Product_line'])['gross_income'].count())
df5.reset_index(inplace=True)
fig = px.bar(df5, x='Product_line', y='gross_income', barmode='group', text='gross_income')

fig.show()


# # Query 14: What was the total income and count in each product line among males and females? 

# In[31]:


df6 = pd.DataFrame(df.groupby(by=['Product_line', 'Gender'])['gross_income'].sum())

df6.reset_index(inplace=True)

fig = px.bar(df6, x='Product_line', y='gross_income', color='Gender', barmode='group', text='gross_income')

fig.show()


# In[32]:


df.groupby(by=['Product_line'])['Gender'].value_counts()


# # Query 15: Which month generated the most income?

# In[33]:


df7 = pd.DataFrame(df.groupby(by=['month'])['gross_income'].sum())
df7.reset_index(inplace=True)
fig = px.bar(df7, x='month', y='gross_income', barmode='group', text='gross_income')
fig.show()


# # Query 16: What day of the week generated the highest income?

# In[34]:


df8 = pd.DataFrame(df.groupby(by=['weekday'])['gross_income'].sum())
df8.reset_index(inplace=True)
fig = px.bar(df8, x='weekday', y='gross_income', barmode='group', text='gross_income')

fig.show()


# # Query 17: What time of the day was the busiest?

# In[35]:


df9 = pd.DataFrame(df.groupby(by=['hour'])['Quantity'].count())
df9.reset_index(inplace=True)
fig = px.line(df9, x='hour', y='Quantity')

fig.show()


# # Query 18: Which product line had the highest quantity of sales?

# In[36]:


dfx = pd.DataFrame(df.groupby(by=['Product_line'])['Quantity'].sum())
dfx.reset_index(inplace=True)
fig = px.bar(dfx, x='Product_line', y='Quantity', barmode='group', text='Quantity')

fig.show()


# # Query 19: What was the average unit price in each product line?

# In[37]:


prices = df.groupby('Product_line').mean()['Unit_price']
print(prices)


# In[38]:


dfx3 = pd.DataFrame(df.groupby(by=['Product_line'])['Unit_price'].mean())

dfx3.reset_index(inplace=True)

fig = px.bar(dfx3, x='Product_line', y='Unit_price', barmode='group', text='Unit_price')

fig.show()


# In[ ]:




