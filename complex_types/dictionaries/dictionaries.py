# ============================================================
# Chapter: Complex Types
# Topic: Python Dictionaries
# ============================================================
#
# DESCRIPTION:
#   A dictionary is an unordered, mutable collection of
#   key-value pairs.  Keys must be unique and hashable;
#   values can be any Python object.  Dictionaries are
#   ideal for fast lookups by a meaningful label rather
#   than a numeric index.
#
# LEARNING GOALS:
#   - Create and inspect dictionaries
#   - Access values by key ([] and .get())
#   - Add, update, and delete entries
#   - Iterate over keys, values, and items
#   - Use common dictionary methods
#   - Use dictionary comprehensions
#   - Understand nested dictionaries
#
# ============================================================
# EXAMPLES
# ============================================================

# --- Creating dictionaries ---

# Example 1: Basic dictionary
person = {"name": "Alice", "age": 30, "city": "London"}
empty = {}
print(person)
print(empty)

# Example 2: dict() constructor
settings = dict(theme="dark", font_size=14, show_grid=True)
print(settings)

# --- Accessing values ---

# Example 3: Square-bracket access
print(person["name"])   # Alice
print(person["age"])    # 30

# Example 4: .get() – returns None (or a default) if key is missing
print(person.get("city"))           # London
print(person.get("country"))        # None
print(person.get("country", "N/A")) # N/A

# --- Modifying dictionaries ---

# Example 5: Adding and updating entries
person["email"] = "alice@example.com"  # add new key
person["age"] = 31                     # update existing key
print(person)

# Example 6: Deleting entries
del person["email"]
removed = person.pop("city")   # remove and return the value
print(person)
print("Removed city:", removed)

# --- Checking membership ---

# Example 7: in operator checks keys
print("name" in person)    # True
print("city" in person)    # False

# --- Keys, values, and items ---

# Example 8: .keys(), .values(), .items()
scores = {"Alice": 95, "Bob": 82, "Carol": 88}
print(list(scores.keys()))    # ['Alice', 'Bob', 'Carol']
print(list(scores.values()))  # [95, 82, 88]
print(list(scores.items()))   # [('Alice', 95), ('Bob', 82), ('Carol', 88)]

# --- Iterating over a dictionary ---

# Example 9: Iterating over keys
for name in scores:
    print(name)

# Example 10: Iterating over key-value pairs with .items()
for name, score in scores.items():
    print(f"{name}: {score}")

# --- Useful methods ---

# Example 11: .setdefault() – insert a key with default if missing
inventory = {"apples": 5, "bananas": 3}
inventory.setdefault("oranges", 0)   # key didn't exist → added with 0
inventory.setdefault("apples", 0)    # key exists → unchanged
print(inventory)

# Example 12: Merging dictionaries (Python 3.9+ uses |; earlier uses .update())
defaults = {"color": "blue", "size": "medium"}
overrides = {"color": "red", "weight": "light"}
merged = {**defaults, **overrides}   # unpacking – works in all Python 3 versions
print(merged)

# --- Dictionary comprehensions ---

# Example 13: Build a dict from a range
squares = {x: x ** 2 for x in range(1, 6)}
print(squares)   # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Example 14: Filter a dict with a comprehension
high_scores = {name: score for name, score in scores.items() if score >= 88}
print(high_scores)   # {'Alice': 95, 'Carol': 88}

# --- Nested dictionaries ---

# Example 15: A dict whose values are dicts
students = {
    "Alice": {"age": 20, "grade": "A"},
    "Bob":   {"age": 22, "grade": "B"},
}
print(students["Alice"]["grade"])   # A
students["Carol"] = {"age": 21, "grade": "A+"}
print(students)


# ============================================================
# TASKS
# ============================================================
#
# Task 1:
#   Create a dictionary called `book` with the keys "title",
#   "author", and "year".  Print each value using its key.
#
# Task 2:
#   Add a "genre" key to your `book` dictionary, then update
#   the "year" to the current year.  Print the updated dict.
#
# Task 3:
#   Given the dictionary {"a": 1, "b": 2, "c": 3}, remove
#   the key "b" using pop() and print both the removed value
#   and the remaining dictionary.
#
# Task 4:
#   Write a for loop that prints every key-value pair from
#   {"sun": "star", "earth": "planet", "moon": "satellite"}
#   in the format:  "sun -> star"
#
# Task 5:
#   Use a dictionary comprehension to create a dictionary
#   that maps each word in
#       ["apple", "banana", "cherry"]
#   to its length.  Expected: {"apple": 5, "banana": 6, "cherry": 6}
#
# Task 6:
#   Given the scores dict {"Alice": 70, "Bob": 55, "Carol": 90, "Dave": 45},
#   use a dict comprehension to create a new dict containing only
#   students who scored 60 or above.
#
# Task 7 (challenge):
#   You have a nested dictionary:
#       catalog = {
#           "laptop": {"price": 999, "stock": 5},
#           "mouse":  {"price": 25,  "stock": 50},
#           "monitor":{"price": 300, "stock": 8},
#       }
#   Print the total value of all stock (price * stock) for each
#   item and the grand total.
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

# Task 7 solution:


# ============================================================
# ----------------------- SOLUTIONS --------------------------
# ============================================================

# Task 1:
# book = {"title": "1984", "author": "George Orwell", "year": 1949}
# print(book["title"])    # 1984
# print(book["author"])   # George Orwell
# print(book["year"])     # 1949

# Task 2:
# book["genre"] = "dystopian fiction"
# book["year"] = 2024
# print(book)

# Task 3:
# d = {"a": 1, "b": 2, "c": 3}
# removed = d.pop("b")
# print("Removed:", removed)   # 2
# print("Remaining:", d)       # {"a": 1, "c": 3}

# Task 4:
# celestial = {"sun": "star", "earth": "planet", "moon": "satellite"}
# for body, kind in celestial.items():
#     print(f"{body} -> {kind}")

# Task 5:
# words = ["apple", "banana", "cherry"]
# word_lengths = {word: len(word) for word in words}
# print(word_lengths)   # {"apple": 5, "banana": 6, "cherry": 6}

# Task 6:
# scores = {"Alice": 70, "Bob": 55, "Carol": 90, "Dave": 45}
# passing = {name: score for name, score in scores.items() if score >= 60}
# print(passing)   # {"Alice": 70, "Carol": 90}

# Task 7:
# catalog = {
#     "laptop":  {"price": 999, "stock": 5},
#     "mouse":   {"price": 25,  "stock": 50},
#     "monitor": {"price": 300, "stock": 8},
# }
# grand_total = 0
# for item, info in catalog.items():
#     value = info["price"] * info["stock"]
#     grand_total += value
#     print(f"{item}: ${value}")
# print(f"Grand total: ${grand_total}")
