Task 2 — Data Cleaning & Missing Value Handling
AI & ML Internship

Report by: Pranav S P


## 1. Objective

The aim of this task was to clean the dataset by identifying missing values, visualizing missing patterns, applying correct imputation strategies, and ensuring the dataset is ready for Machine Learning.


## 2. Dataset Used

House Prices Dataset:Contains features such as:

Location (longitude, latitude)
House characteristics (age, rooms, bedrooms)
Socio-economic factors (population, households, income)
Target variable (median house value)

Total rows: 20,640
Total columns: 10


## 3. Missing Value Analysis

The first step was to analyze missing values using: missing_summary(df)

Findings:

Only 1 column had missing data
total_bedrooms had 207 missing values (1%)
All other columns had 0% missing values

A bar chart was plotted to visually check missing patterns.


## 4. Cleaning Steps Performed

a) Dropped High-Missing Columns

Columns with more than 60% missing would normally be removed.
No columns crossed this threshold
No columns were dropped

b) Numerical Imputation (Median)

Numerical columns were checked for missing values.
Only one numerical column had missing values
total_bedrooms had 207 missing values (1%)
Imputed using median, since median is robust to skewness

Affected Column: total_bedrooms

c) Categorical Imputation (Mode)

Categorical columns were checked for missing values.
ocean_proximity had 0 missing values
No categorical imputation was required

Affected Columns: None


## 5. Cleaning Report (Before vs After)
Metric	          Before Cleaning	    After Cleaning
Rows	           20,640	              20,640
Columns	           10	                  10
Missing Values	   207	                  0
Dropped  Columns   None                	  —

All missing values were successfully handled.


## 6. Output

Cleaned dataset saved as:

data/house_prices_cleaned.csv


## 7. Final Summary

This task helped me understand:

How to detect missing data
How to visualize missing patterns
When to drop columns
When to apply mean/median/mode imputation
How to maintain a modular cleaning workflow using a custom Python module