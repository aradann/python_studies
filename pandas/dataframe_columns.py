# ============================================================
# Chapter: Pandas – DataFrame Sub-chapters
# Topic:   3. Working with Columns
# ============================================================
#
# DESCRIPTION:
#   Columns are the primary way data is organised in a
#   DataFrame.  This file covers everything you need to
#   confidently add, remove, rename, reorder, inspect, and
#   transform columns in your day-to-day workflow.
#
# LEARNING GOALS:
#   - Add an empty (NaN) column and a column with a default value
#   - Drop one or more columns
#   - Rename columns individually or all at once
#   - Reorder columns
#   - Insert a column at a specific position with insert()
#   - Check whether a column exists
#   - Inspect and convert column data types (dtypes / astype)
#
# REQUIRES:  pip install pandas
# ============================================================

import pandas as pd

# ============================================================
# EXAMPLES
# ============================================================

data = {
    "name":   ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "age":    [25, 30, 35, 28, 22],
    "score":  [88.5, 92.0, 79.5, 95.0, 85.0],
    "city":   ["London", "Paris", "London", "Berlin", "Paris"],
}
df = pd.DataFrame(data)

# ------------------------------------------------------------------
# 1. Adding an empty column (filled with NaN)
# ------------------------------------------------------------------
# Assign float('nan') or pd.NA to every row at once.

df["notes"] = float("nan")
print("--- After adding empty 'notes' column ---")
print(df)
print()

# ------------------------------------------------------------------
# 2. Adding a column with a constant default value
# ------------------------------------------------------------------

df["active"] = True
print("--- After adding 'active' column (default True) ---")
print(df)
print()

# ------------------------------------------------------------------
# 3. Adding a column derived from existing data
# ------------------------------------------------------------------

df["score_pct"] = (df["score"] / 100).round(4)
print("--- After adding derived 'score_pct' column ---")
print(df[["name", "score", "score_pct"]])
print()

# ------------------------------------------------------------------
# 4. Inserting a column at a specific position
# ------------------------------------------------------------------
# insert(loc, column, value)  –  loc is the integer position (0-based)

df.insert(1, "id", range(1, len(df) + 1))
print("--- After inserting 'id' at position 1 ---")
print(df.columns.tolist())
print()

# ------------------------------------------------------------------
# 5. Dropping (removing) columns
# ------------------------------------------------------------------

# Drop a single column; inplace=True modifies df directly
df.drop(columns=["notes"], inplace=True)
print("--- After dropping 'notes' ---")
print(df.columns.tolist())
print()

# Drop multiple columns at once
df_trimmed = df.drop(columns=["active", "score_pct"])
print("--- After dropping 'active' and 'score_pct' ---")
print(df_trimmed.columns.tolist())
print()

# ------------------------------------------------------------------
# 6. Renaming columns
# ------------------------------------------------------------------

# Rename specific columns with a mapping dict
df_renamed = df.rename(columns={"name": "full_name", "score": "test_score"})
print("--- After renaming 'name' → 'full_name', 'score' → 'test_score' ---")
print(df_renamed.columns.tolist())
print()

# Rename ALL columns by assigning a new list
df_all_renamed = df.copy()
df_all_renamed.columns = ["id", "full_name", "years", "points", "location",
                           "points_pct", "is_active"]
print("--- After renaming all columns ---")
print(df_all_renamed.columns.tolist())
print()

# Remove the column name entirely (set to None / empty string)
df_no_name = df.copy()
df_no_name.columns.name = None      # clears the Index name, not the column labels
print("--- Columns index name cleared ---")
print(df_no_name.columns)
print()

# ------------------------------------------------------------------
# 7. Reordering columns
# ------------------------------------------------------------------

desired_order = ["id", "name", "city", "age", "score", "score_pct", "active"]
df_reordered = df[desired_order]
print("--- After reordering columns ---")
print(df_reordered.columns.tolist())
print()

# ------------------------------------------------------------------
# 8. Checking whether a column exists
# ------------------------------------------------------------------

print("--- Check if column exists ---")
print("'score' in df:", "score" in df.columns)
print("'salary' in df:", "salary" in df.columns)
print()

# ------------------------------------------------------------------
# 9. Inspecting and converting column data types
# ------------------------------------------------------------------

print("--- Column dtypes ---")
print(df.dtypes)
print()

# Convert a column to a different dtype
df["age"] = df["age"].astype(float)
print("--- 'age' after astype(float) ---")
print(df["age"].dtype)
print()

# Convert a column to a categorical type (memory-efficient for repeated strings)
df["city"] = df["city"].astype("category")
print("--- 'city' after astype('category') ---")
print(df["city"].dtype)
print()

# ------------------------------------------------------------------
# 10. Selecting columns
# ------------------------------------------------------------------

# Single column → Series
city_series = df["city"]
print("--- Single column (Series) ---")
print(type(city_series))
print()

# Multiple columns → DataFrame
subset = df[["name", "score"]]
print("--- Multiple columns (DataFrame) ---")
print(subset)
print()


# ============================================================
# TASKS
# ============================================================
#
# Use the following DataFrame for all tasks:
#
#   df_products = pd.DataFrame({
#       "product":  ["Apple", "Banana", "Cherry", "Date", "Elderberry"],
#       "price":    [1.20, 0.50, 3.00, 4.50, 6.00],
#       "qty":      [50, 120, 30, 20, 10],
#       "in_stock": [True, True, False, True, False],
#   })
#
# Task 1:
#   Add an empty column "supplier" (filled with NaN) and a
#   column "currency" with the constant value "GBP".
#   Print the updated column list.
#
# Task 2:
#   Add a "total_value" column calculated as price * qty.
#   Then drop the "qty" column in place.
#   Print the result.
#
# Task 3:
#   Rename "price" → "unit_price" and "in_stock" → "available".
#   Print the updated column names.
#
# Task 4:
#   Reorder the columns so that "product" comes first, then
#   "currency", then the remaining columns in any order.
#
# Task 5:
#   Check if the columns "product", "weight", and "total_value"
#   exist in the DataFrame.  Print True or False for each.
#
# Task 6 (challenge):
#   Convert the "unit_price" column to float32 to save memory.
#   Convert the "product" column to a categorical dtype.
#   Print the dtypes of both columns after conversion.
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

# Setup:
# df_products = pd.DataFrame({
#     "product":  ["Apple", "Banana", "Cherry", "Date", "Elderberry"],
#     "price":    [1.20, 0.50, 3.00, 4.50, 6.00],
#     "qty":      [50, 120, 30, 20, 10],
#     "in_stock": [True, True, False, True, False],
# })

# Task 1:
# df_products["supplier"] = float("nan")
# df_products["currency"] = "GBP"
# print(df_products.columns.tolist())

# Task 2:
# df_products["total_value"] = df_products["price"] * df_products["qty"]
# df_products.drop(columns=["qty"], inplace=True)
# print(df_products)

# Task 3:
# df_products = df_products.rename(columns={"price": "unit_price",
#                                            "in_stock": "available"})
# print(df_products.columns.tolist())

# Task 4:
# remaining = [c for c in df_products.columns
#              if c not in ("product", "currency")]
# df_products = df_products[["product", "currency"] + remaining]
# print(df_products.columns.tolist())

# Task 5:
# for col in ["product", "weight", "total_value"]:
#     print(f"'{col}' exists:", col in df_products.columns)

# Task 6:
# df_products["unit_price"] = df_products["unit_price"].astype("float32")
# df_products["product"]    = df_products["product"].astype("category")
# print(df_products[["unit_price", "product"]].dtypes)
