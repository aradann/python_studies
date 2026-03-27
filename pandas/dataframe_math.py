# ============================================================
# Chapter: Pandas – DataFrame Sub-chapters
# Topic:   4. Math Functions – min, max, mean (avg)
# ============================================================
#
# DESCRIPTION:
#   pandas exposes Python's familiar min / max / mean (average)
#   operations as both Series methods and DataFrame aggregations.
#   This file shows how to apply them to individual columns,
#   to multiple columns at once, and across rows.
#
# LEARNING GOALS:
#   - Compute min, max, and mean on a Series
#   - Apply the same functions to a whole DataFrame (column-wise
#     and row-wise with axis parameter)
#   - Find the *index label* of the min/max value (idxmin/idxmax)
#   - Use .agg() to apply several functions in one call
#   - Understand how missing values are handled
#
# REQUIRES:  pip install pandas
# ============================================================

import pandas as pd

# ============================================================
# EXAMPLES
# ============================================================

data = {
    "name":    ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "maths":   [88, 72, 95, 60, 83],
    "english": [76, 85, 70, 92, 78],
    "science": [91, 68, 88, 75, 80],
}
df = pd.DataFrame(data).set_index("name")

# ------------------------------------------------------------------
# 1. min, max, mean on a single Series (column)
# ------------------------------------------------------------------

print("--- maths column statistics ---")
print("min  :", df["maths"].min())
print("max  :", df["maths"].max())
print("mean :", df["maths"].mean())
print()

# ------------------------------------------------------------------
# 2. Finding the row label of the minimum / maximum value
# ------------------------------------------------------------------

print("--- who scored lowest / highest in maths? ---")
print("Lowest  :", df["maths"].idxmin())   # returns index label
print("Highest :", df["maths"].idxmax())
print()

# ------------------------------------------------------------------
# 3. Column-wise aggregation across the whole DataFrame
#    (default: axis=0 → aggregate down each column)
# ------------------------------------------------------------------

print("--- min per column (axis=0) ---")
print(df.min())
print()

print("--- max per column ---")
print(df.max())
print()

print("--- mean per column ---")
print(df.mean(numeric_only=True))
print()

# ------------------------------------------------------------------
# 4. Row-wise aggregation  (axis=1 → aggregate across each row)
# ------------------------------------------------------------------

df["row_min"]  = df.min(axis=1)
df["row_max"]  = df.max(axis=1)
df["row_mean"] = df.mean(axis=1)

print("--- per-student min / max / mean across all subjects ---")
print(df[["maths", "english", "science", "row_min", "row_max", "row_mean"]])
print()

# ------------------------------------------------------------------
# 5. .agg() – several functions in one call
# ------------------------------------------------------------------

print("--- agg: min, max, mean for each subject ---")
print(df[["maths", "english", "science"]].agg(["min", "max", "mean"]))
print()

# ------------------------------------------------------------------
# 6. Handling missing values
# ------------------------------------------------------------------

df_missing = pd.DataFrame({
    "a": [10.0, None, 30.0, 40.0],
    "b": [None, 20.0, None, 80.0],
})

# By default, NaN values are skipped (skipna=True)
print("--- min / max / mean with NaN (skipna=True) ---")
print("min :", df_missing.min())
print("max :", df_missing.max())
print("mean:", df_missing.mean())
print()

# Set skipna=False to propagate NaN to the result
print("--- mean with skipna=False ---")
print(df_missing.mean(skipna=False))
print()


# ============================================================
# TASKS
# ============================================================
#
# Use the following DataFrame for all tasks:
#
#   df_sales = pd.DataFrame({
#       "rep":     ["Ana", "Ben", "Cara", "Dan", "Eli"],
#       "jan":     [5200, 4800, 6100, 3900, 5500],
#       "feb":     [4700, 5300, 5800, 4200, 6000],
#       "mar":     [5800, 4900, None, 4600, 5700],
#   }).set_index("rep")
#
# Task 1:
#   Print the minimum, maximum, and mean sales for the "jan"
#   column.
#
# Task 2:
#   Which sales representative had the highest "feb" sales?
#   Use .idxmax() to find out.
#
# Task 3:
#   Compute the column-wise min and max for all three months
#   in a single .agg() call.
#
# Task 4:
#   Add a column "avg_sales" that contains each rep's average
#   monthly sales (use axis=1).  Note: decide how you want to
#   handle the missing value in "mar" for Cara.
#
# Task 5:
#   Find the overall highest single sales figure across the
#   entire DataFrame (all reps, all months).
#   Hint: chain .max() twice.
#
# Task 6 (challenge):
#   Compute the month with the highest mean sales.
#   Hint: calculate the column-wise mean, then call .idxmax()
#   on the resulting Series.
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
# df_sales = pd.DataFrame({
#     "rep":  ["Ana", "Ben", "Cara", "Dan", "Eli"],
#     "jan":  [5200, 4800, 6100, 3900, 5500],
#     "feb":  [4700, 5300, 5800, 4200, 6000],
#     "mar":  [5800, 4900, None, 4600, 5700],
# }).set_index("rep")

# Task 1:
# print("min:", df_sales["jan"].min())
# print("max:", df_sales["jan"].max())
# print("mean:", df_sales["jan"].mean())

# Task 2:
# print(df_sales["feb"].idxmax())

# Task 3:
# print(df_sales.agg(["min", "max"]))

# Task 4:
# df_sales["avg_sales"] = df_sales.mean(axis=1)   # NaN in mar is skipped
# print(df_sales)

# Task 5:
# print(df_sales.max().max())

# Task 6:
# print(df_sales.mean().idxmax())
