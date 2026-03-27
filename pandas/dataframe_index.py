# ============================================================
# Chapter: Pandas – DataFrame Sub-chapters
# Topic:   4. Working with the Index
# ============================================================
#
# DESCRIPTION:
#   Every pandas DataFrame has an *index* – a set of row labels
#   used for alignment, look-up, and merging.  By default this
#   is a RangeIndex (0, 1, 2, …), but it can be any sequence of
#   unique labels: strings, dates, integers, or a MultiIndex.
#
# LEARNING GOALS:
#   - Understand and inspect the default RangeIndex
#   - Assign a custom list as the index
#   - Set a column as the index with set_index()
#   - Reset the index back to RangeIndex with reset_index()
#   - Name and rename the index
#   - Sort rows by the index with sort_index()
#   - Use the index to look up rows with .loc[]
#   - Avoid common pitfalls (duplicate index values, index drift)
#
# REQUIRES:  pip install pandas
# ============================================================

import pandas as pd

# ============================================================
# EXAMPLES
# ============================================================

data = {
    "name":  ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "age":   [25, 30, 35, 28, 22],
    "score": [88.5, 92.0, 79.5, 95.0, 85.0],
    "city":  ["London", "Paris", "London", "Berlin", "Paris"],
}
df = pd.DataFrame(data)

# ------------------------------------------------------------------
# 1. Inspecting the default RangeIndex
# ------------------------------------------------------------------

print("--- Default index ---")
print(df.index)              # RangeIndex(start=0, stop=5, step=1)
print()

print("--- Index as a list ---")
print(df.index.tolist())     # [0, 1, 2, 3, 4]
print()

# ------------------------------------------------------------------
# 2. Assigning a custom index
# ------------------------------------------------------------------
# Replace the index by assigning any list of the same length.

df_custom = df.copy()
df_custom.index = [101, 102, 103, 104, 105]
print("--- Custom integer index ---")
print(df_custom)
print()

# String labels work just as well
df_str_idx = df.copy()
df_str_idx.index = ["a", "b", "c", "d", "e"]
print("--- Custom string index ---")
print(df_str_idx)
print()

# ------------------------------------------------------------------
# 3. Setting a column as the index  (set_index)
# ------------------------------------------------------------------
# The chosen column is removed from the columns and becomes the index.

df_name_idx = df.set_index("name")
print("--- 'name' as index ---")
print(df_name_idx)
print()

# Look up a row by the new index label
print("--- Look up 'Alice' with .loc[] ---")
print(df_name_idx.loc["Alice"])
print()

# Keep the column in place by passing drop=False
df_keep = df.set_index("name", drop=False)
print("--- set_index with drop=False (column kept) ---")
print(df_keep.columns.tolist())
print()

# ------------------------------------------------------------------
# 4. Resetting the index  (reset_index)
# ------------------------------------------------------------------
# Moves the current index back into a regular column and restores
# the default RangeIndex.

df_reset = df_name_idx.reset_index()
print("--- After reset_index() ---")
print(df_reset)
print()

# Discard the old index entirely instead of turning it into a column
df_drop_idx = df_name_idx.reset_index(drop=True)
print("--- reset_index(drop=True) – old index discarded ---")
print(df_drop_idx)
print()

# ------------------------------------------------------------------
# 5. Naming and renaming the index
# ------------------------------------------------------------------

df_named = df.copy()
df_named.index.name = "row_id"
print("--- Index with name 'row_id' ---")
print(df_named)
print()

# Rename after set_index using rename_axis
df_axis = df.set_index("name").rename_axis("student")
print("--- rename_axis: index named 'student' ---")
print(df_axis.index.name)
print()

# ------------------------------------------------------------------
# 6. Sorting rows by the index  (sort_index)
# ------------------------------------------------------------------

df_unsorted = df.copy()
df_unsorted.index = [3, 1, 4, 0, 2]          # deliberately out of order
print("--- Before sort_index ---")
print(df_unsorted.index.tolist())

df_sorted = df_unsorted.sort_index()
print("--- After sort_index (ascending) ---")
print(df_sorted)
print()

df_sorted_desc = df_unsorted.sort_index(ascending=False)
print("--- sort_index(ascending=False) ---")
print(df_sorted_desc.index.tolist())
print()

# ------------------------------------------------------------------
# 7. Checking for and handling duplicate index values
# ------------------------------------------------------------------

df_dup = pd.DataFrame(
    {"val": [10, 20, 30]},
    index=[1, 1, 2],          # duplicate label 1
)
print("--- DataFrame with duplicate index ---")
print(df_dup)
print(f"    is_unique: {df_dup.index.is_unique}")
print()

# Reset to a clean RangeIndex to remove duplicates
df_dup_fixed = df_dup.reset_index(drop=True)
print("--- Duplicate index removed with reset_index ---")
print(df_dup_fixed)
print()

# ------------------------------------------------------------------
# 8. Using the index for row selection with .loc[]
# ------------------------------------------------------------------

df_sel = df.set_index("name")

# Single label
print("--- .loc['Bob'] ---")
print(df_sel.loc["Bob"])
print()

# Slice of labels (inclusive on both ends)
print("--- .loc['Bob':'Diana'] ---")
print(df_sel.loc["Bob":"Diana"])
print()


# ============================================================
# TASKS
# ============================================================
#
# Use the following DataFrame for all tasks:
#
#   df_emp = pd.DataFrame({
#       "name":       ["Ana", "Ben", "Cara", "Dan", "Eli"],
#       "salary":     [45000, 62000, 55000, 38000, 71000],
#       "department": ["HR", "Eng", "Eng", "HR", "Eng"],
#   })
#
# Task 1:
#   Assign the index [201, 202, 203, 204, 205] to the DataFrame.
#   Print the index and confirm it is no longer a RangeIndex.
#
# Task 2:
#   Set the "name" column as the index.
#   Use .loc[] to retrieve the row for "Cara".
#
# Task 3:
#   Reset the index so that "name" becomes a regular column again
#   and the index is a default RangeIndex.
#
# Task 4:
#   Give the index the name "emp_id".
#   Print the first two rows to verify the name appears.
#
# Task 5:
#   Shuffle the index so it reads [4, 2, 0, 3, 1].
#   Then sort the DataFrame back into index order using
#   sort_index() and print the result.
#
# Task 6 (challenge):
#   Create a DataFrame with intentional duplicate index labels.
#   Show that .loc[] returns multiple rows for a duplicated label.
#   Then reset the index to eliminate duplicates.
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
# df_emp = pd.DataFrame({
#     "name":       ["Ana", "Ben", "Cara", "Dan", "Eli"],
#     "salary":     [45000, 62000, 55000, 38000, 71000],
#     "department": ["HR", "Eng", "Eng", "HR", "Eng"],
# })

# Task 1:
# df_emp.index = [201, 202, 203, 204, 205]
# print(df_emp.index)
# print(type(df_emp.index))   # Index, not RangeIndex

# Task 2:
# df_emp = df_emp.set_index("name")
# print(df_emp.loc["Cara"])

# Task 3:
# df_emp = df_emp.reset_index()
# print(df_emp.index)

# Task 4:
# df_emp.index.name = "emp_id"
# print(df_emp.head(2))

# Task 5:
# df_emp.index = [4, 2, 0, 3, 1]
# df_emp = df_emp.sort_index()
# print(df_emp)

# Task 6:
# df_dup = pd.DataFrame(
#     {"name": ["X", "Y", "Z"], "val": [1, 2, 3]},
#     index=[10, 10, 20],
# )
# print(df_dup.loc[10])          # returns both rows with label 10
# df_dup = df_dup.reset_index(drop=True)
# print(df_dup)
