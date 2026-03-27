# ============================================================
# Chapter: Pandas – DataFrame Sub-chapters
# Topic:   5. apply() – Axis Usage; Lambda vs Named Function
# ============================================================
#
# DESCRIPTION:
#   apply() is one of the most flexible pandas tools.  It lets
#   you pass any callable – a built-in, a lambda, or a named
#   function – and run it over every element of a Series or
#   over every row / column of a DataFrame.
#
# LEARNING GOALS:
#   - Apply a function to a Series (column or row)
#   - Understand the axis parameter:
#       axis=0 → function called once per *column* (default)
#       axis=1 → function called once per *row*
#   - Know when to use a lambda vs a named function
#   - Return a scalar, a Series, or a DataFrame from apply()
#   - Use apply() with extra arguments via args / kwargs
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
df = pd.DataFrame(data)

# ------------------------------------------------------------------
# 1. apply() on a Series – transform every element
# ------------------------------------------------------------------

# Lambda: concise, ideal for short one-liners
df["maths_grade"] = df["maths"].apply(lambda x: "pass" if x >= 70 else "fail")
print("--- lambda on Series: pass/fail maths ---")
print(df[["name", "maths", "maths_grade"]])
print()

# Named function: clearer for complex or reusable logic
def letter_grade(score):
    """Convert a numeric score to a letter grade."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "D"

df["english_letter"] = df["english"].apply(letter_grade)
print("--- named function on Series: letter grade ---")
print(df[["name", "english", "english_letter"]])
print()

# ------------------------------------------------------------------
# 2. apply() with axis=0 – called once per *column* (default)
# ------------------------------------------------------------------
# The function receives a Series containing all values in that column.

print("--- axis=0 (default): range of each numeric column ---")
numeric_cols = df[["maths", "english", "science"]]
col_ranges = numeric_cols.apply(lambda col: col.max() - col.min())
print(col_ranges)
print()

# Named function equivalent
def col_range(series):
    """Return max − min for a Series."""
    return series.max() - series.min()

print("--- axis=0 with named function ---")
print(numeric_cols.apply(col_range))
print()

# ------------------------------------------------------------------
# 3. apply() with axis=1 – called once per *row*
# ------------------------------------------------------------------
# The function receives a Series containing all values in that row.

# Lambda: compute total score per student
df["total"] = df[["maths", "english", "science"]].apply(
    lambda row: row.sum(), axis=1
)
print("--- axis=1 (lambda): total score per student ---")
print(df[["name", "maths", "english", "science", "total"]])
print()

# Named function: classify a student based on their average score
def overall_grade(row):
    """Classify a student by their mean score across all subjects."""
    avg = row[["maths", "english", "science"]].mean()
    if avg >= 85:
        return "Distinction"
    elif avg >= 70:
        return "Merit"
    else:
        return "Pass"

df["award"] = df.apply(overall_grade, axis=1)
print("--- axis=1 (named function): overall award ---")
print(df[["name", "maths", "english", "science", "award"]])
print()

# ------------------------------------------------------------------
# 4. Passing extra arguments with args / kwargs
# ------------------------------------------------------------------

def threshold_check(value, threshold, label="above"):
    """Return a label if value is above threshold, else 'below'."""
    return label if value >= threshold else "below"

df["science_check"] = df["science"].apply(
    threshold_check, args=(80,), label="top"
)
print("--- apply with extra args ---")
print(df[["name", "science", "science_check"]])
print()

# ------------------------------------------------------------------
# 5. Returning a Series from apply() – expands to new columns
# ------------------------------------------------------------------

def subject_stats(row):
    """Return min and max across the three subjects for one student."""
    scores = row[["maths", "english", "science"]]
    return pd.Series({"best": scores.max(), "worst": scores.min()})

stats_df = df.apply(subject_stats, axis=1)
print("--- apply returning a Series: best and worst per student ---")
print(pd.concat([df["name"], stats_df], axis=1))
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
#       "years":      [3, 8, 5, 1, 10],
#       "department": ["HR", "Eng", "Eng", "HR", "Eng"],
#   })
#
# Task 1:
#   Use apply() with a lambda to add a column "tax" that is
#   20 % of each employee's salary.
#
# Task 2:
#   Write a named function seniority(years) that returns
#   "junior" (< 3 yrs), "mid" (3–7 yrs), or "senior" (> 7 yrs).
#   Apply it to the "years" column to create a "level" column.
#
# Task 3:
#   Use apply() with axis=0 to compute the standard deviation
#   of both "salary" and "years" in one call.
#
# Task 4:
#   Use apply() with axis=1 (lambda) to create a "summary"
#   column that reads e.g. "Ana – HR – $45,000".
#
# Task 5:
#   Write a named function raise_salary(row, pct) that returns
#   the salary multiplied by (1 + pct/100).  Use apply() with
#   axis=1 and pass pct=10 as an extra argument via kwargs.
#   Store the result in a new column "new_salary".
#
# Task 6 (challenge):
#   Use apply() with axis=1 to return a Series with two fields:
#   "net_salary" (salary * 0.8 after tax) and "bonus"
#   (salary * 0.05 for Eng, salary * 0.03 for HR).
#   Assign the result back to the DataFrame as two new columns.
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
#     "years":      [3, 8, 5, 1, 10],
#     "department": ["HR", "Eng", "Eng", "HR", "Eng"],
# })

# Task 1:
# df_emp["tax"] = df_emp["salary"].apply(lambda s: s * 0.20)
# print(df_emp[["name", "salary", "tax"]])

# Task 2:
# def seniority(years):
#     if years < 3:
#         return "junior"
#     elif years <= 7:
#         return "mid"
#     else:
#         return "senior"
# df_emp["level"] = df_emp["years"].apply(seniority)
# print(df_emp[["name", "years", "level"]])

# Task 3:
# print(df_emp[["salary", "years"]].apply(lambda col: col.std()))

# Task 4:
# df_emp["summary"] = df_emp.apply(
#     lambda row: f"{row['name']} – {row['department']} – ${row['salary']:,}",
#     axis=1
# )
# print(df_emp["summary"])

# Task 5:
# def raise_salary(row, pct):
#     return row["salary"] * (1 + pct / 100)
# df_emp["new_salary"] = df_emp.apply(raise_salary, axis=1, pct=10)
# print(df_emp[["name", "salary", "new_salary"]])

# Task 6:
# def comp_details(row):
#     bonus_rate = 0.05 if row["department"] == "Eng" else 0.03
#     return pd.Series({
#         "net_salary": row["salary"] * 0.80,
#         "bonus":      row["salary"] * bonus_rate,
#     })
# df_emp[["net_salary", "bonus"]] = df_emp.apply(comp_details, axis=1)
# print(df_emp[["name", "salary", "net_salary", "bonus"]])
