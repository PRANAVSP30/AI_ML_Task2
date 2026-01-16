# AI & ML Internship – Task 2
# Data Cleaning & Missing Value Handling
# Submitted by: Pranav S P 

## 1.Project Overview

This task focuses on cleaning the House Prices Dataset by identifying missing values, visualizing missing patterns, applying appropriate imputation techniques, and preparing a cleaned dataset ready for machine learning.

To follow a professional workflow, I built a custom data cleaning module (data_cleaner.py) and used a modular notebook structure similar to real ML pipelines.


## 2.Dataset Used

### House Prices Dataset : Contains features such as location, median income, room count, bedroom count, population, households, and median house value.


## 3.TechStack & Tools Used

    1.Python

    2.Pandas

    3.NumPy

    4.Matplotlib

    5.VS Code / Jupyter Notebook

    6.Git & GitHub (Version control)


## 4.Cleaning Workflow Summary

    1.Loaded the dataset using Pandas.

    2.Generated missing value summary using custom missing_summary().

    3.Visualized missing patterns using bar chart (Matplotlib).

    4.Checked for high-missing columns (>60%).

    5.Imputed numerical columns using median.

    6.Imputed categorical columns using mode (if needed).

    7.Generated detailed before–after cleaning report.

    8.Verified all missing values were handled correctly.

    9.Exported cleaned dataset as house_prices_cleaned.csv.


## 5.What i learnt from this project

    -> How to detect and understand missing values.
    -> When to impute vs drop rows.
    -> Mean vs Median vs Mode imputation.
    -> Why missing data affects ML accuracy.
    -> How to avoid data leakage.
    -> Building reusable Python modules
