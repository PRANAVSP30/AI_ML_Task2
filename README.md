AI & ML Internship – Task 2
Data Cleaning & Missing Value Handling
Submitted by: Pranav S P
📝 Project Overview

This task focuses on cleaning the House Prices Dataset by identifying missing values, visualizing missing patterns, applying appropriate imputation techniques, and preparing a cleaned dataset ready for machine learning.

To follow a professional workflow, I built a custom data cleaning module (data_cleaner.py) and used a modular notebook structure similar to real ML pipelines.

📁 Dataset Used

House Prices Dataset
Contains features such as location, median income, room count, bedroom count, population, households, and median house value.

🛠 Tools Used

Python

Pandas

NumPy

Matplotlib

VS Code / Jupyter Notebook

Git & GitHub (Version control)

📂 Project Structure
AI_ML_Task2/
│
├── data/
│   ├── house_prices.csv
│   └── house_prices_cleaned.csv
│
├── src/
│   └── data_cleaner.py
│
├── notebooks/
│   └── cleaning.ipynb
│
├── reports/
│   └── task2_report.md
│
└── outputs/
    └── screenshots/

🚀 Cleaning Workflow Summary

Loaded the dataset using Pandas.

Generated missing value summary using a custom missing_summary() function.

Visualized missing data using a bar chart (matplotlib).

Checked for high-missing columns (>60%) and removed if necessary.

Applied median imputation for numerical columns (robust to outliers).

Applied mode imputation for categorical columns when required.

Generated a before-vs-after cleaning report using cleaning_report().

Verified dataset completeness and confirmed all missing values were resolved.

Exported cleaned dataset as house_prices_cleaned.csv.

📊 Before vs After Cleaning
Metric	Before	After
Rows	20,640	20,640
Columns	10	10
Missing Values	207	0
Dropped Columns	None	—
📘 What I Learned from This Task

How to detect and analyze missing values

When to drop vs. when to impute

Mean vs Median vs Mode imputation

Avoiding data leakage during cleaning

Writing reusable cleaning code using Python modules

Creating professional reports and workflow documentation
