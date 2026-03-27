# ============================================================
# Chapter: Pandas – DataFrame Sub-chapters
# Topic:   1. Columns, Index – Overview and Working with Them
# ============================================================
#
# DESCRIPTION:
#   A DataFrame has two key structural elements: its *columns*
#   (named series of data) and its *index* (row labels).
#   Understanding how to inspect and manipulate both is
#   fundamental to every pandas workflow.
#
# LEARNING GOALS:
#   - Inspect column names and dtypes with .columns and .dtypes
#   - Add, rename, and drop columns
#   - Understand the default RangeIndex
#   - Set, reset, and rename the index
#   - Use the index to align and look up data
#
# REQUIRES:  pip install pandas
# ============================================================

import pandas as pd

# ============================================================
# EXAMPLES
# ============================================================

data = {
    "name":    ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "age":     [25, 30, 35, 28, 22],
    "score":   [88.5, 92.0, 79.5, 95.0, 85.0],
    "city":    ["London", "Paris", "London", "Berlin", "Paris"],
}
df = pd.DataFrame(data)

# ------------------------------------------------------------------
# 1. Inspecting columns
# ------------------------------------------------------------------

print("--- Column names (.columns) ---")
print(df.columns.tolist())        # ['name', 'age', 'score', 'city']
print()

print("--- Column dtypes (.dtypes) ---")
print(df.dtypes)
print()

print("--- Shape: (rows, columns) ---")
print(df.shape)                   # (5, 4)
print()

# Select a single column → returns a Series
print("--- Single column (Series) ---")
print(df["name"])
print()

# Select multiple columns → returns a DataFrame
print("--- Multiple columns (DataFrame) ---")
print(df[["name", "score"]])
print()

# ------------------------------------------------------------------
# 2. Adding and dropping columns
# ------------------------------------------------------------------

# Add a new column
df["passed"] = df["score"] >= 85
print("--- After adding 'passed' column ---")
print(df)
print()

# Drop a column (axis=1 means columns; inplace=False returns a new df)
df_no_city = df.drop(columns=["city"])
print("--- After dropping 'city' ---")
print(df_no_city)
print()

# ------------------------------------------------------------------
# 3. Renaming columns
# ------------------------------------------------------------------

df_renamed = df.rename(columns={"name": "full_name", "score": "test_score"})
print("--- After renaming columns ---")
print(df_renamed.columns.tolist())
print()

# ------------------------------------------------------------------
# 4. The default RangeIndex
# ------------------------------------------------------------------

print("--- Default index ---")
print(df.index)        # RangeIndex(start=0, stop=5, step=1)
print()

# ------------------------------------------------------------------
# 5. Setting a custom index
# ------------------------------------------------------------------

df_idx = df.set_index("name")
print("--- DataFrame with 'name' as index ---")
print(df_idx)
print()

# Look up a row by the new index label
print("--- Look up 'Alice' by index ---")
print(df_idx.loc["Alice"])
print()

# ------------------------------------------------------------------
# 6. Resetting the index
# ------------------------------------------------------------------

df_reset = df_idx.reset_index()
print("--- After reset_index() ---")
print(df_reset)
print()

# ------------------------------------------------------------------
# 7. Renaming the index
# ------------------------------------------------------------------

df_named_idx = df.copy()
df_named_idx.index.name = "row_id"
print("--- Index with a custom name ---")
print(df_named_idx)
print()


# ============================================================
# TASKS
# ============================================================
#
# Task 1:
#   Create a DataFrame with columns "product", "price", "qty",
#   and "in_stock" for at least five products.
#   Print the list of column names and the dtype of each column.
#
# Task 2:
#   Add a column "total_value" = price * qty to the DataFrame.
#   Then drop the "qty" column and print the result.
#
# Task 3:
#   Rename the "price" column to "unit_price" and print the
#   updated column list.
#
# Task 4:
#   Set the "product" column as the index.
#   Use .loc[] to retrieve the row for one specific product.
#
# Task 5:
#   Reset the index back to the default RangeIndex and print
#   the first three rows.
#
# Task 6 (challenge):
#   Starting from the original DataFrame, rename the index so
#   that it is called "item_id".  Then reassign the index to
#   be [101, 102, 103, 104, 105] and print the result.
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
#     "product":  ["Apple", "Banana", "Cherry", "Date", "Elderberry"],
#     "price":    [1.20, 0.50, 3.00, 4.50, 6.00],
#     "qty":      [50, 120, 30, 20, 10],
#     "in_stock": [True, True, False, True, False],
# })
# print(products.columns.tolist())
# print(products.dtypes)

# Task 2:
# products["total_value"] = products["price"] * products["qty"]
# products = products.drop(columns=["qty"])
# print(products)

# Task 3:
# products = products.rename(columns={"price": "unit_price"})
# print(products.columns.tolist())

# Task 4:
# products = products.set_index("product")
# print(products.loc["Apple"])

# Task 5:
# products = products.reset_index()
# print(products.head(3))

# Task 6:
# products.index.name = "item_id"
# products.index = [101, 102, 103, 104, 105]
# print(products)
