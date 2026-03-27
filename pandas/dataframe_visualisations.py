# ============================================================
# Chapter: Pandas – DataFrame Sub-chapters
# Topic:   3. Built-in Visualisations (df.plot)
# ============================================================
#
# DESCRIPTION:
#   pandas wraps matplotlib to give every DataFrame and Series
#   a .plot accessor.  With a single method call you can
#   produce line charts, bar charts, histograms, box plots,
#   scatter plots, and pie charts – no seaborn required.
#
# LEARNING GOALS:
#   - Use df.plot() to create line charts
#   - Create bar and horizontal-bar charts with kind="bar" / "barh"
#   - Plot frequency distributions with kind="hist"
#   - Visualise spread and outliers with kind="box"
#   - Create scatter plots with kind="scatter"
#   - Create pie charts with kind="pie"
#
# REQUIRES:  pip install pandas matplotlib
#
# NOTE:
#   Each example saves a .png file next to this script.
#   Replace fig.savefig(...) + plt.close(fig) with plt.show()
#   if you prefer an interactive window.
# ============================================================

import os
import pandas as pd
import matplotlib.pyplot as plt

_HERE = os.path.dirname(os.path.abspath(__file__))

# Shared sample data
monthly = pd.DataFrame({
    "month":   ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "sales":   [200, 240, 180, 310, 275, 330],
    "returns": [20,  35,  15,  40,  30,  25],
})
monthly = monthly.set_index("month")

students = pd.DataFrame({
    "name":  ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "maths": [88, 72, 95, 60, 83],
    "english": [76, 85, 70, 92, 78],
    "science": [91, 68, 88, 75, 80],
})
students = students.set_index("name")

# ============================================================
# EXAMPLES
# ============================================================

# ------------------------------------------------------------------
# 1. Line chart  (default kind)
# ------------------------------------------------------------------
# Perfect for time-series or ordered data.

ax = monthly.plot(title="Monthly Sales & Returns", figsize=(8, 4))
ax.set_ylabel("Units")
ax.set_xlabel("Month")
fig = ax.get_figure()
fig.tight_layout()
fig.savefig(os.path.join(_HERE, "plot_line.png"), dpi=100)
plt.close(fig)
print("Saved: plot_line.png")

# ------------------------------------------------------------------
# 2. Bar chart
# ------------------------------------------------------------------
# Useful for comparing discrete categories.

ax = students.plot(kind="bar", figsize=(8, 4),
                   title="Student Scores by Subject")
ax.set_ylabel("Score")
ax.set_xlabel("Student")
ax.legend(loc="lower right")
fig = ax.get_figure()
fig.tight_layout()
fig.savefig(os.path.join(_HERE, "plot_bar.png"), dpi=100)
plt.close(fig)
print("Saved: plot_bar.png")

# Horizontal bar chart – easier to read with long category names
ax = students.plot(kind="barh", figsize=(8, 4),
                   title="Student Scores – Horizontal")
ax.set_xlabel("Score")
fig = ax.get_figure()
fig.tight_layout()
fig.savefig(os.path.join(_HERE, "plot_barh.png"), dpi=100)
plt.close(fig)
print("Saved: plot_barh.png")

# ------------------------------------------------------------------
# 3. Histogram
# ------------------------------------------------------------------
# Shows the frequency distribution of a numeric column.

ax = students["maths"].plot(kind="hist", bins=5,
                             title="Maths Score Distribution",
                             figsize=(6, 4), edgecolor="black")
ax.set_xlabel("Score")
ax.set_ylabel("Frequency")
fig = ax.get_figure()
fig.tight_layout()
fig.savefig(os.path.join(_HERE, "plot_hist.png"), dpi=100)
plt.close(fig)
print("Saved: plot_hist.png")

# ------------------------------------------------------------------
# 4. Box plot
# ------------------------------------------------------------------
# Shows median, quartiles, and outliers for each numeric column.

ax = students.plot(kind="box", figsize=(6, 5),
                   title="Score Distribution per Subject")
ax.set_ylabel("Score")
fig = ax.get_figure()
fig.tight_layout()
fig.savefig(os.path.join(_HERE, "plot_box.png"), dpi=100)
plt.close(fig)
print("Saved: plot_box.png")

# ------------------------------------------------------------------
# 5. Scatter plot
# ------------------------------------------------------------------
# Visualises the relationship between two numeric columns.

ax = students.plot(kind="scatter", x="maths", y="english",
                   title="Maths vs English", figsize=(6, 5))
ax.set_xlabel("Maths Score")
ax.set_ylabel("English Score")
fig = ax.get_figure()
fig.tight_layout()
fig.savefig(os.path.join(_HERE, "plot_scatter.png"), dpi=100)
plt.close(fig)
print("Saved: plot_scatter.png")

# ------------------------------------------------------------------
# 6. Pie chart
# ------------------------------------------------------------------
# Shows proportional breakdown of a single series.

city_counts = pd.Series(
    {"London": 12, "Paris": 8, "Berlin": 5, "Rome": 3},
    name="Employees"
)
ax = city_counts.plot(kind="pie", autopct="%1.0f%%", figsize=(6, 6),
                      title="Employees by City")
ax.set_ylabel("")          # remove default "Employees" ylabel
fig = ax.get_figure()
fig.tight_layout()
fig.savefig(os.path.join(_HERE, "plot_pie.png"), dpi=100)
plt.close(fig)
print("Saved: plot_pie.png")


# ============================================================
# TASKS
# ============================================================
#
# Use the following DataFrame for all tasks:
#
#   df_q = pd.DataFrame({
#       "quarter":  ["Q1", "Q2", "Q3", "Q4"],
#       "revenue":  [150, 200, 175, 225],
#       "expenses": [120, 140, 160, 130],
#   }).set_index("quarter")
#
# Task 1:
#   Create a line chart showing both "revenue" and "expenses"
#   across the four quarters.  Add a title and axis labels.
#   Save or display the plot.
#
# Task 2:
#   Create a grouped bar chart comparing "revenue" and
#   "expenses" per quarter.  Rotate the x-axis tick labels
#   so they are readable.
#
# Task 3:
#   Add a "profit" column (revenue – expenses) to df_q.
#   Plot a horizontal bar chart showing only the "profit"
#   column.
#
# Task 4:
#   Using any numeric column from the tasks above, create a
#   histogram with 4 bins to show the frequency distribution.
#
# Task 5:
#   Create a scatter plot of "revenue" (x-axis) vs "expenses"
#   (y-axis).  Add a descriptive title.
#
# Task 6 (challenge):
#   Plot a pie chart showing the proportion of total revenue
#   contributed by each quarter.  Format the percentage labels
#   to one decimal place.
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
# df_q = pd.DataFrame({
#     "quarter":  ["Q1", "Q2", "Q3", "Q4"],
#     "revenue":  [150, 200, 175, 225],
#     "expenses": [120, 140, 160, 130],
# }).set_index("quarter")

# Task 1:
# ax = df_q.plot(title="Revenue vs Expenses by Quarter", figsize=(7, 4))
# ax.set_xlabel("Quarter")
# ax.set_ylabel("Amount ($k)")
# plt.tight_layout()
# plt.show()

# Task 2:
# ax = df_q.plot(kind="bar", title="Quarterly Revenue vs Expenses",
#                figsize=(7, 4))
# ax.set_xticklabels(df_q.index, rotation=0)
# ax.set_ylabel("Amount ($k)")
# plt.tight_layout()
# plt.show()

# Task 3:
# df_q["profit"] = df_q["revenue"] - df_q["expenses"]
# ax = df_q["profit"].plot(kind="barh", title="Quarterly Profit",
#                           figsize=(6, 4))
# ax.set_xlabel("Profit ($k)")
# plt.tight_layout()
# plt.show()

# Task 4:
# ax = df_q["revenue"].plot(kind="hist", bins=4,
#                            title="Revenue Distribution",
#                            edgecolor="black", figsize=(6, 4))
# ax.set_xlabel("Revenue ($k)")
# plt.tight_layout()
# plt.show()

# Task 5:
# ax = df_q.plot(kind="scatter", x="revenue", y="expenses",
#                title="Revenue vs Expenses (scatter)", figsize=(6, 5))
# ax.set_xlabel("Revenue ($k)")
# ax.set_ylabel("Expenses ($k)")
# plt.tight_layout()
# plt.show()

# Task 6:
# ax = df_q["revenue"].plot(kind="pie", autopct="%.1f%%",
#                            title="Revenue Share by Quarter",
#                            figsize=(6, 6))
# ax.set_ylabel("")
# plt.tight_layout()
# plt.show()
