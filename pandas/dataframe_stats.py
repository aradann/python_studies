# ============================================================
# Chapter: Pandas – DataFrame Sub-chapters
# Topic:   2. DataFrame-related Statistics
# ============================================================
#
# DESCRIPTION:
#   pandas provides a rich set of descriptive statistics that
#   can be computed directly on a DataFrame or Series.  This
#   file surveys the most useful methods: summary statistics,
#   aggregations, and value frequency counts.
#
# LEARNING GOALS:
#   - Summarise a DataFrame with .describe()
#   - Compute individual statistics: mean, median, std, var,
#     count, sum, min, max, quantile
#   - Count distinct values with .nunique() and .value_counts()
#   - Compute pairwise correlations with .corr()
#   - Handle missing data in statistical computations
#
# REQUIRES:  pip install pandas
# ============================================================

import pandas as pd

# ============================================================
# EXAMPLES
# ============================================================

data = {
    "name":   ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"],
    "age":    [25, 30, 35, 28, 22, 40],
    "score":  [88.5, 92.0, 79.5, 95.0, 85.0, 70.0],
    "city":   ["London", "Paris", "London", "Berlin", "Paris", "Berlin"],
    "passed": [True, True, False, True, True, False],
}
df = pd.DataFrame(data)

# ------------------------------------------------------------------
# 1. describe() – summary statistics at a glance
# ------------------------------------------------------------------

# By default, describe() operates on numeric columns only.
print("--- describe() – numeric columns ---")
print(df.describe())
print()

# Pass include="all" to include non-numeric columns too.
print("--- describe(include='all') ---")
print(df.describe(include="all"))
print()

# ------------------------------------------------------------------
# 2. Individual aggregation methods on a Series
# ------------------------------------------------------------------

print("--- score statistics ---")
print("mean   :", df["score"].mean())
print("median :", df["score"].median())
print("std    :", df["score"].std())
print("var    :", df["score"].var())
print("min    :", df["score"].min())
print("max    :", df["score"].max())
print("sum    :", df["score"].sum())
print("count  :", df["score"].count())   # non-NaN values
print()

# ------------------------------------------------------------------
# 3. Quantiles and percentiles
# ------------------------------------------------------------------

print("--- quantiles for 'score' ---")
print("25th percentile :", df["score"].quantile(0.25))
print("75th percentile :", df["score"].quantile(0.75))
print("IQR             :", df["score"].quantile(0.75) - df["score"].quantile(0.25))
print()

# ------------------------------------------------------------------
# 4. Aggregating multiple columns at once
# ------------------------------------------------------------------

print("--- mean of all numeric columns ---")
print(df[["age", "score"]].mean())
print()

# .agg() lets you apply multiple functions in one call
print("--- agg: min, max, mean for age and score ---")
print(df[["age", "score"]].agg(["min", "max", "mean"]))
print()

# ------------------------------------------------------------------
# 5. Counting values
# ------------------------------------------------------------------

print("--- nunique: distinct values per column ---")
print(df.nunique())
print()

print("--- value_counts for 'city' ---")
print(df["city"].value_counts())
print()

# Normalise to get relative frequencies
print("--- value_counts (normalised) for 'city' ---")
print(df["city"].value_counts(normalize=True).round(2))
print()

# ------------------------------------------------------------------
# 6. Correlation matrix
# ------------------------------------------------------------------

print("--- correlation matrix (numeric columns) ---")
print(df[["age", "score"]].corr())
print()

# ------------------------------------------------------------------
# 7. Statistics with missing values
# ------------------------------------------------------------------

df_missing = pd.DataFrame({
    "a": [1.0, None, 3.0, None, 5.0],
    "b": [10.0, 20.0, None, 40.0, 50.0],
})

print("--- mean ignores NaN by default ---")
print(df_missing.mean())                 # skipna=True is the default
print()

print("--- mean with skipna=False ---")
print(df_missing.mean(skipna=False))     # NaN propagates
print()

print("--- count (non-NaN) vs size (all rows) ---")
print("count:", df_missing["a"].count(), "  size:", df_missing["a"].size)
print()


# ============================================================
# TASKS
# ============================================================
#
# Use the following DataFrame for all tasks:
#
#   df_students = pd.DataFrame({
#       "name":   ["Ana", "Ben", "Cara", "Dan", "Eli", "Fay"],
#       "maths":  [78, 85, None, 92, 55, 88],
#       "english":[82, 79, 91, None, 67, 74],
#       "grade":  ["B", "B", "A", "A", "C", "B"],
#   })
#
# Task 1:
#   Call .describe() on df_students.  Which column has the
#   highest mean?  Print just the mean row of the result.
#
# Task 2:
#   Compute and print the median, standard deviation, and
#   variance for both "maths" and "english" in a single
#   .agg() call.
#
# Task 3:
#   Use .value_counts() to count how many students are in
#   each grade.  Then normalise the counts so they sum to 1.
#
# Task 4:
#   Calculate the correlation between "maths" and "english".
#   Print the correlation coefficient (a single number).
#
# Task 5:
#   How many non-NaN values exist in each column?  Use the
#   .count() method on the whole DataFrame.
#
# Task 6 (challenge):
#   For each grade (A, B, C), compute the average "maths"
#   score.  Hint: use .groupby() combined with .mean().
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
# df_students = pd.DataFrame({
#     "name":    ["Ana", "Ben", "Cara", "Dan", "Eli", "Fay"],
#     "maths":   [78, 85, None, 92, 55, 88],
#     "english": [82, 79, 91, None, 67, 74],
#     "grade":   ["B", "B", "A", "A", "C", "B"],
# })

# Task 1:
# stats = df_students.describe()
# print(stats.loc["mean"])

# Task 2:
# print(df_students[["maths", "english"]].agg(["median", "std", "var"]))

# Task 3:
# counts = df_students["grade"].value_counts()
# print(counts)
# print(counts / counts.sum())   # or: value_counts(normalize=True)

# Task 4:
# corr_matrix = df_students[["maths", "english"]].corr()
# print(corr_matrix.loc["maths", "english"])

# Task 5:
# print(df_students.count())

# Task 6:
# print(df_students.groupby("grade")["maths"].mean())
