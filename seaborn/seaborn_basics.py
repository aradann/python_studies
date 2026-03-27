# ============================================================
# Chapter: Seaborn Basics
# Topic: Scatter, Linear Regression, Heat Map, Plot Grid
# ============================================================
#
# DESCRIPTION:
#   seaborn is a high-level data-visualisation library built on
#   top of matplotlib.  It makes it easy to create attractive,
#   informative statistical graphics with minimal code.
#
# LEARNING GOALS:
#   - Create scatter plots with scatterplot()
#   - Overlay a linear-regression line with regplot() / lmplot()
#   - Visualise correlations with heatmap()
#   - Explore multi-variable relationships with pairplot() and
#     FacetGrid
#
# REQUIRES:  pip install seaborn matplotlib pandas
#
# NOTE:
#   Each example saves a .png file next to this script so you can
#   inspect the output without a GUI.  Remove the savefig() calls
#   and replace plt.close() with plt.show() if you prefer an
#   interactive window.
# ============================================================

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

# Use a consistent, clean theme for all plots
sns.set_theme(style="whitegrid")

# Save output images next to this script
_HERE = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# EXAMPLES
# ============================================================

# ------------------------------------------------------------------
# 1. Scatter plot
# ------------------------------------------------------------------
# A scatter plot reveals the relationship between two numeric variables.
# We use the built-in "tips" dataset (restaurant tip data).

tips = sns.load_dataset("tips")

fig, ax = plt.subplots()
sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="sex",        # colour points by gender
    style="smoker",   # marker shape by smoker status
    ax=ax,
)
ax.set_title("Tips vs Total Bill")
fig.savefig(os.path.join(_HERE, "scatter_plot.png"), dpi=100)
plt.close(fig)
print("Saved: scatter_plot.png")

# ------------------------------------------------------------------
# 2. Linear regression plot
# ------------------------------------------------------------------
# regplot() draws a scatter plot AND fits a linear-regression line with
# a confidence interval shaded around it.

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# regplot – single axes object (no hue support)
sns.regplot(
    data=tips,
    x="total_bill",
    y="tip",
    scatter_kws={"alpha": 0.4},
    line_kws={"color": "red"},
    ax=axes[0],
)
axes[0].set_title("regplot: total_bill vs tip")

# lmplot – figure-level function that supports hue/col/row faceting
# It creates its own figure, so we save it separately.
plt.close(fig)

lm_grid = sns.lmplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="sex",       # separate regression line per group
    height=5,
    aspect=1.2,
)
lm_grid.set_axis_labels("Total Bill ($)", "Tip ($)")
lm_grid.figure.suptitle("lmplot: regression by gender", y=1.02)
lm_grid.savefig(os.path.join(_HERE, "regression_plot.png"), dpi=100)
plt.close(lm_grid.figure)
print("Saved: regression_plot.png")

# ------------------------------------------------------------------
# 3. Heat map
# ------------------------------------------------------------------
# heatmap() is ideal for displaying a correlation matrix or any 2-D
# numeric table.

# Build a correlation matrix from the numeric columns of tips
corr = tips[["total_bill", "tip", "size"]].corr()

fig, ax = plt.subplots(figsize=(6, 5))
sns.heatmap(
    corr,
    annot=True,       # write the correlation value inside each cell
    fmt=".2f",        # format to 2 decimal places
    cmap="coolwarm",  # diverging colour map (blue=negative, red=positive)
    vmin=-1, vmax=1,
    ax=ax,
)
ax.set_title("Correlation Matrix – Tips Dataset")
fig.tight_layout()
fig.savefig(os.path.join(_HERE, "heatmap.png"), dpi=100)
plt.close(fig)
print("Saved: heatmap.png")

# ------------------------------------------------------------------
# 4. Plot grid
# ------------------------------------------------------------------
# (a) pairplot – the quickest way to visualise pairwise relationships
#     across all numeric columns at once.

pair_grid = sns.pairplot(
    tips,
    hue="sex",         # colour by gender
    diag_kind="kde",   # kernel-density estimate on the diagonal
    plot_kws={"alpha": 0.5},
)
pair_grid.figure.suptitle("Pairplot – Tips Dataset", y=1.02)
pair_grid.savefig(os.path.join(_HERE, "pairplot.png"), dpi=100)
plt.close(pair_grid.figure)
print("Saved: pairplot.png")

# (b) FacetGrid – a flexible grid for plotting the same chart for
#     different subsets of the data.
#     Here we draw a histogram of total_bill for each day.

fg = sns.FacetGrid(tips, col="day", col_wrap=2, height=3.5)
fg.map(sns.histplot, "total_bill", kde=True)
fg.set_axis_labels("Total Bill ($)", "Count")
fg.set_titles(col_template="{col_name}")
fg.figure.suptitle("FacetGrid: Total Bill by Day", y=1.03)
fg.tight_layout()
fg.savefig(os.path.join(_HERE, "facet_grid.png"), dpi=100)
plt.close(fg.figure)
print("Saved: facet_grid.png")


# ============================================================
# TASKS
# ============================================================
#
# Use any seaborn built-in dataset you like – run
#   sns.get_dataset_names()
# to see what is available.  The "iris", "penguins", "titanic",
# "flights", and "tips" datasets are good starting points.
#
# Task 1: Scatter plot
#   Load the "iris" dataset.
#   Create a scatter plot with "sepal_length" on the x-axis,
#   "petal_length" on the y-axis, and colour the points by
#   "species".  Give the plot an informative title.
#
# Task 2: Linear regression
#   Using the "tips" dataset, create a regplot() that shows
#   the relationship between "size" (number of diners) and
#   "total_bill".  Customise the colour of the regression line.
#
# Task 3: Heat map
#   Load the "flights" dataset (monthly passenger counts 1949-1960).
#   Pivot it into a month × year matrix and plot it as a heatmap
#   with annotations.  Hint: use df.pivot().
#
# Task 4: Pairplot
#   Load the "penguins" dataset.
#   Create a pairplot coloured by "species" and use "hist" as the
#   diagonal kind.  Save or display the result.
#
# Task 5: FacetGrid (challenge)
#   Using the "titanic" dataset, build a FacetGrid with one column
#   per passenger class ("pclass").  In each facet draw a KDE plot
#   of "age".  Add a title to the whole figure.
#
# ============================================================
# WRITE YOUR SOLUTIONS BELOW THIS LINE
# ============================================================

# Task 1 solution:

# Task 2 solution:

# Task 3 solution:

# Task 4 solution:

# Task 5 solution:


# ============================================================
# ----------------------- SOLUTIONS --------------------------
# ============================================================

# Task 1:
# iris = sns.load_dataset("iris")
# fig, ax = plt.subplots()
# sns.scatterplot(data=iris, x="sepal_length", y="petal_length",
#                 hue="species", ax=ax)
# ax.set_title("Iris: Sepal Length vs Petal Length by Species")
# plt.show()

# Task 2:
# fig, ax = plt.subplots()
# sns.regplot(data=tips, x="size", y="total_bill",
#             line_kws={"color": "green"}, ax=ax)
# ax.set_title("Party Size vs Total Bill")
# plt.show()

# Task 3:
# flights = sns.load_dataset("flights")
# pivot = flights.pivot(index="month", columns="year", values="passengers")
# fig, ax = plt.subplots(figsize=(12, 6))
# sns.heatmap(pivot, annot=True, fmt="d", cmap="YlOrRd", ax=ax)
# ax.set_title("Monthly Airline Passengers (1949-1960)")
# plt.tight_layout()
# plt.show()

# Task 4:
# penguins = sns.load_dataset("penguins").dropna()
# g = sns.pairplot(penguins, hue="species", diag_kind="hist")
# g.figure.suptitle("Penguins Pairplot", y=1.02)
# plt.show()

# Task 5:
# titanic = sns.load_dataset("titanic").dropna(subset=["age"])
# g = sns.FacetGrid(titanic, col="pclass", height=4)
# g.map(sns.kdeplot, "age", fill=True)
# g.set_axis_labels("Age", "Density")
# g.set_titles("Class {col_name}")
# g.figure.suptitle("Age Distribution by Passenger Class", y=1.05)
# plt.show()
