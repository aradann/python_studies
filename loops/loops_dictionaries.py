# ============================================================
# Chapter: Loops
# Topic: Looping over Dictionaries — Keys, Values, Items
# ============================================================
#
# DESCRIPTION:
#   Dictionaries store data as key-value pairs.  Python
#   provides three dedicated views for iterating over them:
#     - .keys()   — iterate over every key
#     - .values() — iterate over every value
#     - .items()  — iterate over (key, value) pairs at once
#   Understanding these views is essential for processing,
#   filtering, and transforming dictionary data with loops.
#
# LEARNING GOALS:
#   - Iterate over dictionary keys with .keys() (and bare for)
#   - Iterate over dictionary values with .values()
#   - Iterate over key-value pairs with .items()
#   - Modify or build dictionaries inside a loop
#   - Use dictionary comprehensions as a concise alternative
#   - Handle nested dictionaries with loops
#
# ============================================================
# EXAMPLES
# ============================================================

scores = {"Alice": 92, "Bob": 78, "Carol": 85, "Dave": 61}

# -------------------------------------------------------
# Iterating over KEYS
# -------------------------------------------------------

# Example 1: Default iteration — yields keys (same as .keys())
for name in scores:
    print(name)   # Alice  Bob  Carol  Dave

# Example 2: Explicit .keys() — more readable when intent matters
for name in scores.keys():
    print(name)

# Example 3: Check membership using the key view
if "Alice" in scores.keys():
    print("Alice is in the dictionary")

# Example 4: Sorted keys
for name in sorted(scores.keys()):
    print(name)   # alphabetical order

# -------------------------------------------------------
# Iterating over VALUES
# -------------------------------------------------------

# Example 5: Print every value
for score in scores.values():
    print(score)   # 92  78  85  61

# Example 6: Calculate the average using .values()
total = 0
for score in scores.values():
    total += score
average = total / len(scores)
print(f"Average score: {average}")   # 79.0

# Example 7: Filter values (find passing scores ≥ 70)
passing = [s for s in scores.values() if s >= 70]
print("Passing scores:", passing)   # [92, 78, 85]

# -------------------------------------------------------
# Iterating over ITEMS (key-value pairs)
# -------------------------------------------------------

# Example 8: .items() unpacks each pair into (key, value)
for name, score in scores.items():
    print(f"{name}: {score}")
# Alice: 92
# Bob:   78
# ...

# Example 9: Conditional logic inside an items loop
for name, score in scores.items():
    grade = "Pass" if score >= 70 else "Fail"
    print(f"{name}: {score} → {grade}")

# Example 10: Build a new dictionary from an items loop
scaled = {}
for name, score in scores.items():
    scaled[name] = round(score * 1.05, 1)   # 5 % bonus
print(scaled)

# Example 11: Same result with a dictionary comprehension
scaled = {name: round(score * 1.05, 1) for name, score in scores.items()}
print(scaled)

# -------------------------------------------------------
# Nested dictionaries
# -------------------------------------------------------

# Example 12: Loop over a nested dictionary
students = {
    "Alice": {"grade": "A", "age": 20},
    "Bob":   {"grade": "B", "age": 22},
    "Carol": {"grade": "A", "age": 21},
}

for name, info in students.items():
    print(f"{name} — grade: {info['grade']}, age: {info['age']}")

# Example 13: Collect all students with grade "A"
top_students = [name for name, info in students.items() if info["grade"] == "A"]
print("Top students:", top_students)   # ['Alice', 'Carol']


# ============================================================
# TASKS
# ============================================================
#
# Task 1 — keys:
#   Given the dictionary:
#       inventory = {"apples": 30, "bananas": 12, "cherries": 45}
#   Use a for loop over .keys() to print each item name.
#
# Task 2 — keys:
#   Using the same inventory dictionary, print the keys in
#   reverse alphabetical order.
#
# Task 3 — values:
#   Using inventory, use a for loop over .values() to
#   calculate and print the total number of items in stock.
#
# Task 4 — values:
#   Using inventory, find and print the name of the item
#   with the highest stock level.  (Hint: iterate over
#   .items() and track the maximum as you go.)
#
# Task 5 — items:
#   Given:
#       prices = {"apple": 0.5, "banana": 0.3, "cherry": 1.2}
#   Use a for loop over .items() to print a formatted receipt:
#       apple   : $0.50
#       banana  : $0.30
#       cherry  : $1.20
#
# Task 6 — items:
#   Using prices from Task 5, create a new dictionary called
#   discounted where every price is reduced by 10 %.
#   Use a dictionary comprehension.
#
# Task 7 — nested dict:
#   Given:
#       catalog = {
#           "laptop":  {"price": 999, "stock": 5},
#           "monitor": {"price": 299, "stock": 12},
#           "keyboard":{"price":  49, "stock": 30},
#       }
#   Use a for loop over .items() to print each product name
#   together with its price and stock level.
#
# Task 8 (challenge):
#   Using catalog from Task 7, create a new dictionary called
#   restock that contains only the products where stock < 10,
#   with the value set to (20 - current_stock) to indicate
#   how many units to order.
#   Expected: {"laptop": 15}
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

# Task 8 solution:


# ============================================================
# ----------------------- SOLUTIONS --------------------------
# ============================================================

# Task 1:
# inventory = {"apples": 30, "bananas": 12, "cherries": 45}
# for item in inventory.keys():
#     print(item)

# Task 2:
# for item in sorted(inventory.keys(), reverse=True):
#     print(item)

# Task 3:
# total = 0
# for qty in inventory.values():
#     total += qty
# print("Total items:", total)   # 87

# Task 4:
# max_item = None
# max_qty = -1
# for item, qty in inventory.items():
#     if qty > max_qty:
#         max_qty = qty
#         max_item = item
# print(f"Highest stock: {max_item} ({max_qty})")   # cherries (45)

# Task 5:
# prices = {"apple": 0.5, "banana": 0.3, "cherry": 1.2}
# for item, price in prices.items():
#     print(f"{item:<8}: ${price:.2f}")

# Task 6:
# discounted = {item: round(price * 0.9, 2) for item, price in prices.items()}
# print(discounted)

# Task 7:
# catalog = {
#     "laptop":   {"price": 999, "stock": 5},
#     "monitor":  {"price": 299, "stock": 12},
#     "keyboard": {"price":  49, "stock": 30},
# }
# for product, details in catalog.items():
#     print(f"{product}: ${details['price']}, stock: {details['stock']}")

# Task 8:
# restock = {
#     product: 20 - details["stock"]
#     for product, details in catalog.items()
#     if details["stock"] < 10
# }
# print(restock)   # {'laptop': 15}
