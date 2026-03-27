# Chapter 4 · Pandas Basics

An introduction to the most common day-to-day operations with **pandas**:
selecting data by label and position, dealing with missing values, and
transforming columns with `apply`.

---

## Files in this folder

| File | Topics covered |
|------|----------------|
| `pandas_basics.py` | DataFrame & Series creation, label-based indexing (`loc`), position-based indexing (`iloc`), boolean indexing, `fillna()`, `dropna()`, column-wise `apply()`, row-wise `apply()` |
| `dataframe_overview.py` | Columns & index inspection (`.columns`, `.dtypes`, `.shape`), adding / dropping / renaming columns, `set_index()`, `reset_index()` |
| `dataframe_stats.py` | `describe()`, `mean()`, `median()`, `std()`, `var()`, `min()`, `max()`, `sum()`, `count()`, `quantile()`, `agg()`, `value_counts()`, `nunique()`, `corr()` |
| `dataframe_visualisations.py` | Built-in `df.plot()`: line, bar, barh, histogram, box, scatter, pie |
| `dataframe_math.py` | `min()`, `max()`, `mean()` on Series and DataFrame; `idxmin()` / `idxmax()`; column-wise vs row-wise (`axis=0` / `axis=1`) |
| `dataframe_apply.py` | `apply()` on a Series; `axis=0` vs `axis=1`; lambda vs named function; extra arguments; returning a `Series` from `apply()` |

---

## How each file is organised

1. **Header** – chapter, topic, description, and learning goals.
2. **Examples** – short, runnable snippets that demonstrate each concept.
3. **Tasks** – problems for you to solve; no solution is given here.
4. **`# WRITE YOUR SOLUTIONS BELOW THIS LINE`** – your personal workspace.
5. **`# ---- SOLUTIONS ----`** – reference answers, commented out.
