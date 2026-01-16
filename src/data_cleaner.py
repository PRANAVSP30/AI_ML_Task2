"""
data_cleaner.py
----------------
A custom module designed to perform structured data cleaning for datasets.

This module:
- Detects missing values and their percentages
- Visualizes missing data
- Applies numerical and categorical imputations
- Drops columns with too many missing values
- Compares before vs after cleaning
- Saves cleaned dataset

Written by: Pranav S P
AI & ML Internship – Task 2
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# -------------------------------------------------------
# 1. Detect Missing Values (Count + Percentage)
# -------------------------------------------------------
def missing_summary(df):
    """
    Returns a DataFrame containing:
    - Missing value count
    - Missing value percentage
    """
    missing_count = df.isnull().sum()
    missing_percent = (missing_count / len(df)) * 100

    summary = pd.DataFrame({
        "Missing Count": missing_count,
        "Missing %": missing_percent.round(2)
    })

    return summary.sort_values("Missing %", ascending=False)



# -------------------------------------------------------
# 2. Visualize Missing Value Percentage
# -------------------------------------------------------
def plot_missing_values(df):
    """
    Creates a bar chart showing missing percentage of each column.
    """
    summary = missing_summary(df)

    plt.figure(figsize=(10, 6))
    summary["Missing %"].plot(kind="bar", color="skyblue")
    plt.title("Missing Value Percentage by Column")
    plt.xlabel("Columns")
    plt.ylabel("Missing %")
    plt.tight_layout()
    plt.show()



# -------------------------------------------------------
# 3. Drop Columns with Extremely High Missing Values
# -------------------------------------------------------
def drop_high_missing(df, threshold=60):
    """
    Drops columns where missing percentage > threshold.
    Default threshold = 60%.
    """
    summary = missing_summary(df)
    cols_to_drop = summary[summary["Missing %"] > threshold].index.tolist()
    return df.drop(columns=cols_to_drop), cols_to_drop



# -------------------------------------------------------
# 4. Impute Numerical Columns (Mean or Median)
# -------------------------------------------------------
def impute_numerical(df, method="median"):
    """
    Imputes numerical columns using mean or median.
    Default = median
    """
    num_cols = df.select_dtypes(include=["int64", "float64"]).columns

    for col in num_cols:
        if df[col].isnull().sum() > 0:
            if method == "mean":
                df[col].fillna(df[col].mean(), inplace=True)
            else:
                df[col].fillna(df[col].median(), inplace=True)

    return df, list(num_cols)



# -------------------------------------------------------
# 5. Impute Categorical Columns (Mode)
# -------------------------------------------------------
def impute_categorical(df):
    """
    Imputes categorical columns using mode (most frequent value).
    """
    cat_cols = df.select_dtypes(include=["object"]).columns

    for col in cat_cols:
        if df[col].isnull().sum() > 0:
            df[col].fillna(df[col].mode()[0], inplace=True)

    return df, list(cat_cols)



# -------------------------------------------------------
# 6. Compare Before vs After Cleaning
# -------------------------------------------------------
def cleaning_report(before_df, after_df, dropped_cols):
    """
    Generates a summary dictionary comparing before vs after cleaning.
    """
    report = {
        "Rows Before": len(before_df),
        "Rows After": len(after_df),
        "Columns Before": before_df.shape[1],
        "Columns After": after_df.shape[1],
        "Missing Before": before_df.isnull().sum().sum(),
        "Missing After": after_df.isnull().sum().sum(),
        "Dropped Columns": dropped_cols
    }

    return report



# -------------------------------------------------------
# 7. Save Cleaned Dataset
# -------------------------------------------------------
def save_cleaned_data(df, path):
    df.to_csv(path, index=False)
