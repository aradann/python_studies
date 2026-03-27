# Python Studies

A structured set of Python exercises organised by topic.  Each `.py` file
contains **examples**, **tasks** (problems without solutions), and a
**solutions section** separated by a clearly commented line so you can
practise before peeking at the answers.

---

## Project Structure

```
python_studies/
├── README.md                    ← you are here
│
├── intro/                       ← Chapter 1: Introduction to Python
│   ├── README.md                ← chapter overview & file index
│   ├── hello_world.py           ← Printing output, the print() function
│   ├── basic_types.py           ← Integers, floats, arithmetic, type conversion
│   └── strings.py               ← String creation, indexing, methods, formatting
│
├── lists/                       ← Chapter 2: Lists
│   ├── README.md                ← chapter overview & file index
│   └── lists.py                 ← Creating, modifying, iterating, comprehensions
│
└── arithmetic/                  ← Chapter 3: Basic Arithmetic Operations
    ├── README.md                ← chapter overview & file index
    └── arithmetic.py            ← Operators, precedence, math module, real-world tasks
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

### Chapter 2 · Lists (`lists/`)

> 📄 See [`lists/README.md`](lists/README.md) for the full file index.

| File | Topics covered |
|------|---------------|
| `lists.py` | List creation, indexing, slicing, `.append()` `.insert()` `.remove()` `.pop()` `.sort()` `.reverse()`, `len()` `min()` `max()` `sum()` `sorted()`, `for` loops with `enumerate()`, list comprehensions, nested lists |

### Chapter 3 · Basic Arithmetic Operations (`arithmetic/`)

> 📄 See [`arithmetic/README.md`](arithmetic/README.md) for the full file index.

| File | Topics covered |
|------|---------------|
| `arithmetic.py` | All arithmetic operators, operator precedence (PEMDAS), augmented assignment, `abs()` `round()` `divmod()` `pow()`, `math` module (`sqrt`, `ceil`, `floor`, `log`, `log2`, `pi`, `e`), real-world problems |

---

## Useful References

- GeekForGeeks Python types: <https://www.geeksforgeeks.org/python/python-data-types/>
- GeekForGeeks type() function: <https://www.geeksforgeeks.org/python/python-type-function/>
- Pandas (Kaggle intro): <https://www.kaggle.com/learn/pandas>
- Seaborn data visualisation: <https://seaborn.pydata.org/>
