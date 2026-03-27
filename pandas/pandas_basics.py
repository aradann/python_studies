# ============================================================
# Chapter: Pandas Basics
# Topic: Indexing, Fill NA, Apply
# ============================================================
#
# DESCRIPTION:
#   pandas is the go-to library for working with tabular data in
#   Python.  This file covers the three operations you will reach
#   for every day: selecting rows and columns, handling missing
#   values, and transforming data with apply().
#
# LEARNING GOALS:
#   - Create DataFrames and Series
#   - Select data with .loc[] (label-based) and .iloc[] (position-based)
#   - Filter rows with boolean indexing
#   - Fill missing values with fillna() and remove them with dropna()
#   - Apply a function to a column or row with apply()
#
# REQUIRES:  pip install pandas
# ============================================================

import pandas as pd

# ============================================================
# EXAMPLES
# ============================================================

# ------------------------------------------------------------------
# 1. Creating a DataFrame
# ------------------------------------------------------------------

data = {
    "name":   ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "age":    [25, 30, 35, 28, 22],
    "score":  [88.5, 92.0, 79.5, 95.0, 85.0],
    "city":   ["London", "Paris", "London", "Berlin", "Paris"],
}
df = pd.DataFrame(data)
print("--- DataFrame ---")
print(df)
print()

# ------------------------------------------------------------------
# 2. Label-based indexing with .loc[]
# ------------------------------------------------------------------

# Select a single row by index label
print("--- loc: row with label 2 ---")
print(df.loc[2])
print()

# Select specific rows and columns
print("--- loc: rows 1-3, name & score columns ---")
print(df.loc[1:3, ["name", "score"]])
print()

# ------------------------------------------------------------------
# 3. Position-based indexing with .iloc[]
# ------------------------------------------------------------------

# Select the first two rows and first three columns
print("--- iloc: first 2 rows, first 3 columns ---")
print(df.iloc[:2, :3])
print()

# Select a single cell: row 4, column 1
print("--- iloc: single cell [4, 1] ---")
print(df.iloc[4, 1])
print()

# ------------------------------------------------------------------
# 4. Boolean (conditional) indexing
# ------------------------------------------------------------------

# Rows where age is greater than 27
print("--- boolean: age > 27 ---")
print(df[df["age"] > 27])
print()

# Multiple conditions (use & for AND, | for OR)
print("--- boolean: age > 27 AND city == London ---")
print(df[(df["age"] > 27) & (df["city"] == "London")])
print()

# ------------------------------------------------------------------
# 5. Handling missing values
# ------------------------------------------------------------------

df_missing = pd.DataFrame({
    "name":   ["Alice", "Bob", "Charlie", "Diana"],
    "age":    [25, None, 35, 28],
    "score":  [88.5, 92.0, None, 95.0],
})
print("--- DataFrame with missing values ---")
print(df_missing)
print()

# fillna: replace NaN with a fixed value
print("--- fillna: replace NaN with 0 ---")
print(df_missing.fillna(0))
print()

# fillna: replace per-column (different values per column)
print("--- fillna: per-column defaults ---")
print(df_missing.fillna({"age": df_missing["age"].mean(), "score": 0}))
print()

# forward-fill (propagate last valid value forward)
print("--- ffill: forward-fill ---")
print(df_missing.ffill())
print()

# dropna: remove any row that contains at least one NaN
print("--- dropna ---")
print(df_missing.dropna())
print()

# ------------------------------------------------------------------
# 6. Transforming data with apply()
# ------------------------------------------------------------------

# apply() on a column (Series): double every score
print("--- apply on column: double score ---")
df["score_doubled"] = df["score"].apply(lambda x: x * 2)
print(df[["name", "score", "score_doubled"]])
print()

# apply() on a column: categorise age into brackets
def age_bracket(age):
    if age < 25:
        return "young"
    elif age < 32:
        return "mid"
    else:
        return "senior"

df["age_group"] = df["age"].apply(age_bracket)
print("--- apply on column: age bracket ---")
print(df[["name", "age", "age_group"]])
print()

# apply() on a row (axis=1): combine name and city into one string
df["label"] = df.apply(lambda row: f"{row['name']} ({row['city']})", axis=1)
print("--- apply on rows (axis=1): label ---")
print(df[["name", "city", "label"]])
print()


# ============================================================
# TASKS
# ============================================================
#
# Task 1:
#   Create a DataFrame with at least four columns and five rows
#   of your own data (e.g. a mini product catalogue with columns
#   "product", "category", "price", "in_stock").
#   Print the first three rows using iloc.
#
# Task 2:
#   Using the DataFrame from Task 1, use .loc[] to select only the
#   "product" and "price" columns for all rows.
#
# Task 3:
#   Filter the DataFrame from Task 1 to show only rows where
#   "in_stock" is True (or where "price" is above a threshold of
#   your choice).
#
# Task 4:
#   Add a column "discounted_price" to the Task 1 DataFrame by
#   applying a 10 % discount to the "price" column using apply().
#
# Task 5:
#   Create a DataFrame that has at least two columns with some
#   missing values (use None or float('nan')).
#   Fill the missing values in one column with the column mean
#   and drop any remaining rows that still have NaN values.
#
# Task 6 (challenge):
#   Use apply() with axis=1 to create a new column "summary" that
#   combines values from two or more columns into a single
#   descriptive string (e.g. "ProductA – $9.99").
#
# ============================================================
# WRITE YOUR SOLUTIONS BELOW THIS LINE
# ============================================================

# Task 1 solution:

# Task 2 solution:

# Task 3 solution:

# Task 4 solution:

# Task 5 solution:

# Task 6 solution:


# ============================================================
# ----------------------- SOLUTIONS --------------------------
# ============================================================

# Task 1:
# products = pd.DataFrame({
#     "product":   ["Apple", "Banana", "Cherry", "Date", "Elderberry"],
#     "category":  ["fruit", "fruit", "fruit", "fruit", "fruit"],
#     "price":     [1.20, 0.50, 3.00, 4.50, 6.00],
#     "in_stock":  [True, True, False, True, False],
# })
# print(products.iloc[:3])

# Task 2:
# print(products.loc[:, ["product", "price"]])

# Task 3:
# print(products[products["in_stock"] == True])
# # or: print(products[products["price"] > 2.00])

# Task 4:
# products["discounted_price"] = products["price"].apply(lambda p: round(p * 0.90, 2))
# print(products[["product", "price", "discounted_price"]])

# Task 5:
# df_na = pd.DataFrame({
#     "a": [1.0, None, 3.0, None, 5.0],
#     "b": [10.0, 20.0, None, 40.0, 50.0],
# })
# df_na["a"] = df_na["a"].fillna(df_na["a"].mean())
# df_na = df_na.dropna()
# print(df_na)

# Task 6:
# products["summary"] = products.apply(
#     lambda row: f"{row['product']} – ${row['price']:.2f}", axis=1
# )
# print(products[["product", "price", "summary"]])
