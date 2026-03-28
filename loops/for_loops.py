# ============================================================
# Chapter: Loops
# Topic: For Loops
# ============================================================
#
# DESCRIPTION:
#   A `for` loop lets you iterate over any sequence — a range
#   of numbers, a list, a string, or any other iterable.
#   Python sequences are zero-indexed, so the first element is
#   always at index 0.
#
# LEARNING GOALS:
#   - Write basic `for` loops with `range()`
#   - Understand that indexing starts at 0
#   - Iterate over lists, strings, and other iterables
#   - Use `range(start, stop, step)` to control iteration
#   - Access elements by index inside a loop
#   - Use `enumerate()` to get index and value at the same time
#   - Use `break` and `continue` to control loop flow
#
# ============================================================
# EXAMPLES
# ============================================================

# --- Basic for loop with range() ---

# Example 1: Loop from 0 to 4 (range stops BEFORE the end value)
for i in range(5):
    print(i)   # prints 0, 1, 2, 3, 4

# Example 2: range(start, stop) — start is inclusive, stop is exclusive
for i in range(1, 6):
    print(i)   # prints 1, 2, 3, 4, 5

# Example 3: range(start, stop, step)
for i in range(0, 10, 2):
    print(i)   # prints 0, 2, 4, 6, 8

# --- Indexing from 0 ---

# Example 4: Accessing list elements by index starting at 0
colors = ["red", "green", "blue", "yellow"]
for i in range(len(colors)):
    print(f"Index {i}: {colors[i]}")
# Index 0: red
# Index 1: green
# Index 2: blue
# Index 3: yellow

# Example 5: Iterating directly over a list (no explicit index needed)
for color in colors:
    print(color)

# Example 6: Using enumerate() — the Pythonic way to get index + value
for index, color in enumerate(colors):
    print(f"{index}: {color}")
# 0: red
# 1: green
# 2: blue
# 3: yellow

# Example 7: enumerate() with a custom start value
for index, color in enumerate(colors, start=1):
    print(f"{index}: {color}")
# 1: red  ...

# --- Iterating over strings ---

# Example 8: Each character of a string, starting at position 0
word = "Python"
for i in range(len(word)):
    print(f"word[{i}] = {word[i]}")

# Example 9: Simpler string iteration
for char in "loop":
    print(char)

# --- Nested for loops ---

# Example 10: Multiplication table (3x3)
for row in range(1, 4):
    for col in range(1, 4):
        print(f"{row} x {col} = {row * col}")

# --- break and continue ---

# Example 11: break — exit the loop early
for i in range(10):
    if i == 5:
        break
    print(i)   # prints 0 1 2 3 4

# Example 12: continue — skip the current iteration
for i in range(6):
    if i % 2 == 0:
        continue
    print(i)   # prints 1 3 5  (odd numbers only)


# ============================================================
# TASKS
# ============================================================
#
# Task 1:
#   Use a for loop with range() to print every number from
#   0 to 9 (inclusive).  Notice that the sequence starts at 0.
#
# Task 2:
#   Given the list planets = ["Mercury", "Venus", "Earth",
#   "Mars", "Jupiter"], use a for loop and range(len(...)) to
#   print each planet with its index:
#       0: Mercury
#       1: Venus
#       ...
#
# Task 3:
#   Repeat Task 2 using enumerate() instead of range(len(...)).
#
# Task 4:
#   Use a for loop to calculate the sum of all numbers from
#   1 to 100 (inclusive) and print the result.
#
# Task 5:
#   Use a for loop to print only the even numbers between
#   1 and 20 (inclusive).
#
# Task 6:
#   Use a nested for loop to print a 4x4 grid of asterisks (*):
#       * * * *
#       * * * *
#       * * * *
#       * * * *
#
# Task 7:
#   Use a for loop with break to find the first number in
#   range(1, 50) that is divisible by both 6 and 7.
#   Print that number.
#
# Task 8 (challenge):
#   Given the list scores = [45, 78, 92, 55, 88, 34, 67],
#   use a for loop to find and print the index and value of
#   the highest score without using the max() function.
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
# for i in range(10):
#     print(i)

# Task 2:
# planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter"]
# for i in range(len(planets)):
#     print(f"{i}: {planets[i]}")

# Task 3:
# for i, planet in enumerate(planets):
#     print(f"{i}: {planet}")

# Task 4:
# total = 0
# for n in range(1, 101):
#     total += n
# print(total)  # 5050

# Task 5:
# for n in range(2, 21, 2):
#     print(n)

# Task 6:
# for row in range(4):
#     print("* " * 4)

# Task 7:
# for n in range(1, 50):
#     if n % 6 == 0 and n % 7 == 0:
#         print(n)  # 42
#         break

# Task 8:
# scores = [45, 78, 92, 55, 88, 34, 67]
# best_index = 0
# for i in range(1, len(scores)):
#     if scores[i] > scores[best_index]:
#         best_index = i
# print(f"Highest score: {scores[best_index]} at index {best_index}")
