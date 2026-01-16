AI & ML Internship — Task 2
Data Cleaning & Missing Value Handling
By: Pranav S P

Project Overview

This task focuses on cleaning the House Prices Dataset by identifying missing values, visualizing missing patterns, applying appropriate imputation techniques, and generating a clean dataset ready for machine learning.
To ensure modularity, I created a custom data cleaning module (data_cleaner.py), similar to real-world ML pipelines.


Project Structure
AI_ML_Task2/
│
├── data/
│   ├── house_prices.csv               # Original dataset
│   └── house_prices_cleaned.csv       # Cleaned dataset
│
├── src/
│   └── data_cleaner.py                # Custom cleaning module
│
├── notebooks/
│   └── cleaning.ipynb                 # Main data cleaning notebook
│
├── reports/
│   └── task2_report.md                # One-page professional cleaning report
│
└── outputs/
    └── screenshots/                   # Screenshots of notebook outputs


Cleaning Workflow Summary 
  1.Loaded the House Prices dataset using Pandas.
  2.Generated missing value summary using a custom missing_summary() function.
  3.Visualized missing data patterns using a bar chart (matplotlib).
  4.Identified high-missing columns (>60%) and checked if they needed removal.
  5.Performed numerical imputation using median for stability against outliers.
  6.Checked categorical columns and applied mode imputation when required.
  7.Generated a before-vs-after cleaning report using cleaning_report().
  8.Verified dataset completeness and ensured all missing values were resolved.
  9.Exported the cleaned dataset as house_prices_cleaned.csv for ML readiness.


Tech Stack Used 

Languages & Libraries:
  Python 3.11
  Pandas — data handling & analysis
  NumPy — numerical operations
  Matplotlib — visualizations
  Jupyter Notebook / VS Code — notebook execution environment

Tools:
  Git & GitHub — version control
  VS Code — development environment


Key Learnings from Task 2

How to analyze missing values
When to drop vs. when to impute
Mean vs median vs mode imputation
Why missing data affects ML performance
How to avoid data leakage
How to write reusable data cleaning functions
How to create a professional cleaning report

