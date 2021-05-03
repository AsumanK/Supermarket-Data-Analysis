# Supermarket-Data-Analysis

Contents
1. Problem statement 
2. Hypothesis generation
3. Getting the system ready and loading the data
4. Understanding the data
5. Exploratory data analysis (EDA)
-	Univariate analysis
-	Bivariate analysis
6. Missing value and outlier treatment
Evaluation metrics for classification problems
Model building: Part I
Logistic regression using stratified k-folds cross validation
Feature engineering 
Model building: Part II
-	Logistic regression
-	Decision tree
-	Random forest 
-	XGBoost


Problem statement

The growth of supermarkets in most populated cities are increasing and market competitions are also high. The dataset is one of the historical sales of supermarket company which has recorded in 3 different branches for 3 months data. We want to analyse the performance of the supermarket using the data provided.

Attribute information

Invoice id: Computer generated sales slip invoice identification number

Branch: Branch of supercentre (3 branches are available identified by A, B and C).

City: Location of supercentres

Customer type: Type of customers, recorded by Members for customers using member card and Normal for without member card.

Gender: Gender type of customer

Product line: General item categorization groups - Electronic accessories, Fashion accessories, Food and beverages, Health and beauty, Home and lifestyle, Sports and travel

Unit price: Price of each product in $

Quantity: Number of products purchased by customer

Tax: 5% tax fee for customer buying

Total: Total price including tax

Date: Date of purchase (Record available from January 2019 to March 2019)

Time: Purchase time (10am to 9pm)

Payment: Payment used by customer for purchase (3 methods are available – Cash, Credit card and Ewallet)

COGS: Cost of goods sold

Gross margin percentage: Gross margin percentage

Gross income: Gross income

Rating: Customer stratification rating on their overall shopping experience (On a scale of 1 to 10)


1. What gender had most sales?
2. What was the average income in both genders?
3. What customer type had most sales?
4. Which product line had most sales?
5. Which city experienced most sales?
6. What was the most popular payment method?
7. Which branch had most sales?
8. What is the distribution of gross income?
9. What does the customer rating look like?
10. What was the total aggregate sales in each branch?
11. What was the total aggregate sales in each city?
12. What was the average rating in each branch?
13. What was the number of sales in each product line?
14. What was the total income and count in each product line among males and females?
15. Which month generated the most income?
16. What day of the week generated the highest income?
17. What time of the day was the busiest?
18. Which product line had the highest quantity of sales?
19. What was the average unit price in each product line?


Getting the system ready and loading the data

We will be using python for this project along with the below listed libraries.
-Python
-Pandas
- Numpy
-Plotly

Data 

Data for this project will be downloaded from the link below.
https://www.kaggle.com/aungpyaeap/supermarket-sales
