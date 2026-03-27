# ============================================================
# Chapter: Pandas – DataFrame Sub-chapters
# Topic:   2. DataFrame Initialisation Styles
# ============================================================
#
# DESCRIPTION:
#   A DataFrame can be constructed in many different ways
#   depending on where your data comes from.  Knowing the most
#   common patterns lets you get data into a usable shape
#   quickly, whether you are starting from scratch, reading in
#   data, or building a DataFrame incrementally.
#
# LEARNING GOALS:
#   - Build a DataFrame via the constructor (dict, list-of-dicts,
#     list-of-lists, NumPy array)
#   - Grow a DataFrame by adding rows with pd.concat()
#   - Grow a DataFrame by adding columns
#
# REQUIRES:  pip install pandas numpy
# ============================================================

import pandas as pd
import numpy as np

# ============================================================
# EXAMPLES
# ============================================================

# ------------------------------------------------------------------
# 1. Constructor – from a dictionary of lists  (most common)
# ------------------------------------------------------------------
# Each key becomes a column name; each list becomes the column data.

data_dict = {
    "name":  ["Alice", "Bob", "Charlie"],
    "age":   [25, 30, 35],
    "score": [88.5, 92.0, 79.5],
}
df_dict = pd.DataFrame(data_dict)
print("--- From dict of lists ---")
print(df_dict)
print()

# ------------------------------------------------------------------
# 2. Constructor – from a list of dicts
# ------------------------------------------------------------------
# Each dict is one row; missing keys become NaN.

data_rows = [
    {"name": "Alice",   "age": 25, "score": 88.5},
    {"name": "Bob",     "age": 30, "score": 92.0},
    {"name": "Charlie", "age": 35},          # score missing → NaN
]
df_rows = pd.DataFrame(data_rows)
print("--- From list of dicts ---")
print(df_rows)
print()

# ------------------------------------------------------------------
# 3. Constructor – from a list of lists  (with explicit columns)
# ------------------------------------------------------------------
# Useful when column names are separate from the data.

data_lists = [
    ["Alice",   25, 88.5],
    ["Bob",     30, 92.0],
    ["Charlie", 35, 79.5],
]
df_lists = pd.DataFrame(data_lists, columns=["name", "age", "score"])
print("--- From list of lists ---")
print(df_lists)
print()

# ------------------------------------------------------------------
# 4. Constructor – from a NumPy array
# ------------------------------------------------------------------
# Efficient for numeric data; column names must be supplied.

arr = np.array([[1, 10, 100],
                [2, 20, 200],
                [3, 30, 300]])
df_np = pd.DataFrame(arr, columns=["x", "y", "z"])
print("--- From NumPy array ---")
print(df_np)
print()

# ------------------------------------------------------------------
# 5. Constructor – empty DataFrame with predefined columns
# ------------------------------------------------------------------
# Handy when you want to define structure before populating it.

df_empty = pd.DataFrame(columns=["product", "price", "qty"])
print("--- Empty DataFrame with columns ---")
print(df_empty)
print(f"    shape: {df_empty.shape}")
print()

# ------------------------------------------------------------------
# 6. Building a DataFrame by adding rows  (pd.concat)
# ------------------------------------------------------------------
# The recommended approach (pandas ≥ 2.0) is pd.concat; avoid
# repeated df.append() which was removed in pandas 2.0.

base = pd.DataFrame(columns=["name", "age", "score"])

new_rows = [
    {"name": "Diana", "age": 28, "score": 95.0},
    {"name": "Eve",   "age": 22, "score": 85.0},
]

for row in new_rows:
    base = pd.concat([base, pd.DataFrame([row])], ignore_index=True)

print("--- Built by adding rows with pd.concat ---")
print(base)
print()

# Concatenating two existing DataFrames vertically
df_a = pd.DataFrame({"name": ["Alice", "Bob"],   "score": [88.5, 92.0]})
df_b = pd.DataFrame({"name": ["Charlie", "Diana"], "score": [79.5, 95.0]})
df_combined = pd.concat([df_a, df_b], ignore_index=True)
print("--- Vertical concat of two DataFrames ---")
print(df_combined)
print()

# ------------------------------------------------------------------
# 7. Building a DataFrame by adding columns
# ------------------------------------------------------------------
# Columns can be added one at a time or via pd.concat (axis=1).

df_cols = pd.DataFrame({"name": ["Alice", "Bob", "Charlie"]})

# Add a single column directly
df_cols["age"] = [25, 30, 35]

# Add a column derived from another column
df_cols["score"] = [88.5, 92.0, 79.5]
df_cols["passed"] = df_cols["score"] >= 85

print("--- Built by adding columns ---")
print(df_cols)
print()

# Horizontal concat of two DataFrames (axis=1)
df_names  = pd.DataFrame({"name": ["Alice", "Bob", "Charlie"]})
df_scores = pd.DataFrame({"maths": [88, 72, 95], "english": [76, 85, 70]})
df_h = pd.concat([df_names, df_scores], axis=1)
print("--- Horizontal concat of two DataFrames ---")
print(df_h)
print()


# ============================================================
# TASKS
# ============================================================
#
# Task 1:
#   Create a DataFrame using a dictionary of lists with columns
#   "city", "country", "population" for at least four cities.
#   Print the result.
#
# Task 2:
#   Create the same DataFrame using a list of dicts instead.
#   Verify that the output is identical.
#
# Task 3:
#   Create a DataFrame using a list of lists and explicit column
#   names: "month", "revenue", "expenses".  Use at least six rows.
#   Print the first three rows with iloc.
#
# Task 4:
#   Start with an empty DataFrame that has the columns
#   "student", "grade".  Add three rows one at a time using
#   pd.concat().  Print the final DataFrame.
#
# Task 5:
#   Create two separate DataFrames with the same columns
#   "item" and "price", then combine them vertically using
#   pd.concat() and reset the index.
#
# Task 6 (challenge):
#   Build a DataFrame column-by-column: start with just a
#   "name" column, then add "salary", then add "tax" (10 % of
#   salary), and finally add a "department" column.
#   Use horizontal pd.concat() for the last step.
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
# cities = pd.DataFrame({
#     "city":       ["London", "Paris", "Berlin", "Tokyo"],
#     "country":    ["UK", "France", "Germany", "Japan"],
#     "population": [9_000_000, 2_100_000, 3_700_000, 13_900_000],
# })
# print(cities)

# Task 2:
# cities2 = pd.DataFrame([
#     {"city": "London", "country": "UK",      "population": 9_000_000},
#     {"city": "Paris",  "country": "France",  "population": 2_100_000},
#     {"city": "Berlin", "country": "Germany", "population": 3_700_000},
#     {"city": "Tokyo",  "country": "Japan",   "population": 13_900_000},
# ])
# print(cities2)

# Task 3:
# finances = pd.DataFrame(
#     [
#         ["Jan", 12000, 8000],
#         ["Feb", 15000, 9500],
#         ["Mar", 11000, 7800],
#         ["Apr", 17000, 10200],
#         ["May", 19000, 11000],
#         ["Jun", 21000, 12500],
#     ],
#     columns=["month", "revenue", "expenses"],
# )
# print(finances.iloc[:3])

# Task 4:
# grades = pd.DataFrame(columns=["student", "grade"])
# for student, grade in [("Alice", "A"), ("Bob", "B"), ("Charlie", "C")]:
#     grades = pd.concat(
#         [grades, pd.DataFrame([{"student": student, "grade": grade}])],
#         ignore_index=True,
#     )
# print(grades)

# Task 5:
# shop_a = pd.DataFrame({"item": ["Apple", "Banana"], "price": [1.20, 0.50]})
# shop_b = pd.DataFrame({"item": ["Cherry", "Date"],  "price": [3.00, 4.50]})
# all_items = pd.concat([shop_a, shop_b], ignore_index=True)
# print(all_items)

# Task 6:
# df_build = pd.DataFrame({"name": ["Ana", "Ben", "Cara"]})
# df_build["salary"] = [45000, 62000, 55000]
# df_build["tax"] = df_build["salary"] * 0.10
# df_dept = pd.DataFrame({"department": ["HR", "Eng", "Eng"]})
# df_build = pd.concat([df_build, df_dept], axis=1)
# print(df_build)
