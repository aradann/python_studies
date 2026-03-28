# Python Studies

A structured set of Python exercises organised by topic.  Each `.py` file
contains **examples**, **tasks** (problems without solutions), and a
**solutions section** separated by a clearly commented line so you can
practise before peeking at the answers.

---

## Project Structure

```
python_studies/
├── README.md                          ← you are here
│
├── intro/                             ← Chapter 1: Introduction to Python
│   ├── README.md                      ← chapter overview & file index
│   ├── hello_world.py                 ← Printing output, the print() function
│   ├── basic_types.py                 ← Integers, floats, arithmetic, type conversion
│   └── strings.py                     ← String creation, indexing, methods, formatting
│
├── complex_types/                     ← Chapter 2: Complex Types
│   ├── README.md                      ← chapter overview & sub-chapter index
│   ├── lists/                         ← Chapter 2.1: Lists
│   │   ├── README.md                  ← sub-chapter overview & file index
│   │   └── lists.py                   ← Creating, modifying, iterating, comprehensions
│   └── dictionaries/                  ← Chapter 2.2: Dictionaries
│       ├── README.md                  ← sub-chapter overview & file index
│       └── dictionaries.py            ← Creating, accessing, iterating, comprehensions
│
├── arithmetic/                        ← Chapter 3: Basic Arithmetic Operations
│   ├── README.md                      ← chapter overview & file index
│   └── arithmetic.py                  ← Operators, precedence, math module, real-world tasks
│
├── pandas/                            ← Chapter 4: Pandas Basics
│   ├── README.md                      ← chapter overview & file index
│   ├── pandas_basics.py               ← Indexing (loc/iloc), fillna, apply
│   ├── dataframe_overview.py          ← Columns, index, set_index, reset_index
│   ├── dataframe_stats.py             ← describe, mean, std, corr, value_counts
│   ├── dataframe_visualisations.py    ← df.plot(): line, bar, hist, box, scatter, pie
│   ├── dataframe_math.py              ← min, max, mean; idxmin/idxmax; axis=0/1
│   └── dataframe_apply.py             ← apply axis, lambda vs named function
│
├── seaborn/                           ← Chapter 5: Seaborn Basics
│   ├── README.md                      ← chapter overview & file index
│   └── seaborn_basics.py              ← Scatter, linear regression, heatmap, plot grid
│
└── loops/                             ← Chapter 6: Loops
    ├── README.md                      ← chapter overview & file index
    ├── for_loops.py                   ← for loop, range(), zero-based indexing, enumerate(), break/continue
    └── while_loops.py                 ← while condition, while not, while True, break/continue
```

---

## How Each File Is Organised

1. **Header** – chapter, topic, description, and learning goals.
2. **Examples** – short, runnable snippets that demonstrate each concept.
3. **Tasks** – problems for you to solve; no solution is provided in this section.
4. **`# WRITE YOUR SOLUTIONS BELOW THIS LINE`** – your personal workspace.
5. **`# ----------------------- SOLUTIONS --------------------------`** –
   reference solutions, commented out so they don't run automatically.

---

## Chapters

### Chapter 1 · Intro (`intro/`)

> 📄 See [`intro/README.md`](intro/README.md) for the full file index.

| File | Topics covered |
|------|---------------|
| `hello_world.py` | `print()`, separators, end parameter, expressions in print |
| `basic_types.py` | `int`, `float`, arithmetic operators (`+` `-` `*` `/` `//` `%` `**`), `type()`, `isinstance()`, type conversion |
| `strings.py` | String literals, escape characters, indexing, slicing, `.upper()` `.lower()` `.strip()` `.split()` `.join()` `.replace()` `.find()`, f-strings, membership testing |

### Chapter 2 · Complex Types (`complex_types/`)

> 📄 See [`complex_types/README.md`](complex_types/README.md) for the full sub-chapter index.

#### Chapter 2.1 · Lists (`complex_types/lists/`)

> 📄 See [`complex_types/lists/README.md`](complex_types/lists/README.md) for the full file index.

| File | Topics covered |
|------|---------------|
| `lists.py` | List creation, indexing, slicing, `.append()` `.insert()` `.remove()` `.pop()` `.sort()` `.reverse()`, `len()` `min()` `max()` `sum()` `sorted()`, `for` loops with `enumerate()`, list comprehensions, nested lists |

#### Chapter 2.2 · Dictionaries (`complex_types/dictionaries/`)

> 📄 See [`complex_types/dictionaries/README.md`](complex_types/dictionaries/README.md) for the full file index.

| File | Topics covered |
|------|---------------|
| `dictionaries.py` | Dictionary creation, key access, `.get()`, `.keys()` `.values()` `.items()`, adding/updating/deleting entries, `in` operator, `for` loops, dictionary comprehensions, nested dictionaries, `.setdefault()`, merging dicts |

### Chapter 3 · Basic Arithmetic Operations (`arithmetic/`)

> 📄 See [`arithmetic/README.md`](arithmetic/README.md) for the full file index.

| File | Topics covered |
|------|---------------|
| `arithmetic.py` | All arithmetic operators, operator precedence (PEMDAS), augmented assignment, `abs()` `round()` `divmod()` `pow()`, `math` module (`sqrt`, `ceil`, `floor`, `log`, `log2`, `pi`, `e`), real-world problems |

### Chapter 4 · Pandas Basics (`pandas/`)

> 📄 See [`pandas/README.md`](pandas/README.md) for the full file index.

| File | Topics covered |
|------|---------------|
| `pandas_basics.py` | DataFrame & Series creation, label-based indexing (`loc`), position-based indexing (`iloc`), boolean indexing, `fillna()`, `dropna()`, column-wise `apply()`, row-wise `apply()` |
| `dataframe_overview.py` | Columns & index inspection, adding / dropping / renaming columns, `set_index()`, `reset_index()` |
| `dataframe_stats.py` | `describe()`, `mean()`, `median()`, `std()`, `var()`, `min()`, `max()`, `quantile()`, `agg()`, `value_counts()`, `corr()` |
| `dataframe_visualisations.py` | Built-in `df.plot()`: line, bar, barh, histogram, box, scatter, pie |
| `dataframe_math.py` | `min()`, `max()`, `mean()` on Series and DataFrame; `idxmin()` / `idxmax()`; `axis=0` vs `axis=1` |
| `dataframe_apply.py` | `apply()` axis usage; lambda vs named function; extra args; returning a `Series` |

### Chapter 5 · Seaborn Basics (`seaborn/`)

> 📄 See [`seaborn/README.md`](seaborn/README.md) for the full file index.

| File | Topics covered |
|------|---------------|
| `seaborn_basics.py` | `scatterplot()`, `regplot()` / `lmplot()`, `heatmap()`, `pairplot()`, `FacetGrid` |

### Chapter 6 · Loops (`loops/`)

> 📄 See [`loops/README.md`](loops/README.md) for the full file index.

| File | Topics covered |
|------|---------------|
| `for_loops.py` | `for` with `range()`, zero-based indexing, iterating over lists and strings, `range(start, stop, step)`, `enumerate()`, nested loops, `break`, `continue` |
| `while_loops.py` | `while <condition>`, `while not <condition>`, `while True` with `break`, `continue`, Collatz sequence (challenge) |

---

## Useful References

- GeekForGeeks Python types: <https://www.geeksforgeeks.org/python/python-data-types/>
- GeekForGeeks type() function: <https://www.geeksforgeeks.org/python/python-type-function/>
- Pandas (Kaggle intro): <https://www.kaggle.com/learn/pandas>
- Seaborn data visualisation: <https://seaborn.pydata.org/>
