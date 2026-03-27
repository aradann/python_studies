# ============================================================
# Chapter: Lists
# Topic: Python Lists
# ============================================================
#
# DESCRIPTION:
#   A list is an ordered, mutable collection that can hold items
#   of any type.  Lists are one of the most versatile and widely
#   used data structures in Python.
#
# LEARNING GOALS:
#   - Create and inspect lists
#   - Access elements by index and slice
#   - Modify lists (append, insert, remove, pop, sort, reverse)
#   - Iterate over lists with for loops
#   - Use common list functions (len, min, max, sum, sorted)
#   - Use list comprehensions
#   - Understand nested lists
#
# ============================================================
# EXAMPLES
# ============================================================

# --- Creating lists ---

# Example 1: Basic list
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [42, "hello", 3.14, True]
empty = []
print(fruits)
print(numbers)
print(mixed)

# --- Indexing and slicing ---

# Example 2: Positive and negative indexing
print(fruits[0])    # apple
print(fruits[-1])   # cherry

# Example 3: Slicing
print(numbers[1:4])   # [2, 3, 4]
print(numbers[:3])    # [1, 2, 3]
print(numbers[::2])   # [1, 3, 5]  (every other element)

# --- Modifying lists ---

# Example 4: Appending and inserting
fruits.append("date")          # add to end
fruits.insert(1, "avocado")    # insert at index 1
print(fruits)

# Example 5: Removing elements
fruits.remove("banana")        # remove first occurrence by value
popped = fruits.pop()          # remove and return last element
popped_index = fruits.pop(0)   # remove and return element at index
print(fruits, "| popped:", popped, "| popped[0]:", popped_index)

# Example 6: Sorting and reversing
nums = [3, 1, 4, 1, 5, 9, 2, 6]
nums.sort()               # sort in place (ascending)
print(nums)
nums.sort(reverse=True)   # sort descending
print(nums)
nums.reverse()            # reverse in place
print(nums)

# --- Useful functions ---

# Example 7: len, min, max, sum
data = [10, 20, 30, 40, 50]
print(len(data))   # 5
print(min(data))   # 10
print(max(data))   # 50
print(sum(data))   # 150

# Example 8: sorted() returns a new list (original unchanged)
original = [5, 2, 8, 1]
new_sorted = sorted(original)
print(original)    # [5, 2, 8, 1]  unchanged
print(new_sorted)  # [1, 2, 5, 8]

# --- Iterating over a list ---

# Example 9: Simple for loop
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)

# Example 10: for loop with index using enumerate()
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"{index}: {color}")

# --- List comprehensions ---

# Example 11: Create a new list from an existing one
squares = [x ** 2 for x in range(1, 6)]
print(squares)   # [1, 4, 9, 16, 25]

# Example 12: Filtering with a condition
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)     # [2, 4, 6, 8, 10]

# --- Nested lists ---

# Example 13: A 2D grid (list of lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(matrix[1][2])   # 6  (row 1, column 2)

# --- Other useful methods ---

# Example 14: count and index
letters = ["a", "b", "a", "c", "a"]
print(letters.count("a"))    # 3
print(letters.index("b"))    # 1

# Example 15: Concatenation and repetition
list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(list_a + list_b)    # [1, 2, 3, 4, 5, 6]
print(list_a * 3)          # [1, 2, 3, 1, 2, 3, 1, 2, 3]


# ============================================================
# TASKS
# ============================================================
#
# Task 1:
#   Create a list called vegetables with at least 5 items.
#   Print the first and last item using indexing.
#
# Task 2:
#   Add "spinach" to the end of your vegetables list and insert
#   "kale" at position 2.  Print the updated list.
#
# Task 3:
#   Remove the third element from the list [10, 20, 30, 40, 50]
#   using pop() and print both the removed element and the
#   remaining list.
#
# Task 4:
#   Given the list [5, 3, 8, 1, 9, 2, 7], sort it in ascending
#   order without modifying the original list.  Print both.
#
# Task 5:
#   Use a for loop to print every item in
#   ["cat", "dog", "fish", "bird"] along with its index number.
#   Example output:
#       0: cat
#       1: dog
#       ...
#
# Task 6:
#   Use a list comprehension to create a list of the cubes of
#   numbers from 1 to 8 (i.e., [1, 8, 27, ..., 512]) and print it.
#
# Task 7:
#   Use a list comprehension to filter the list
#   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and keep only numbers
#   that are divisible by 3.  Print the result.
#
# Task 8 (challenge):
#   Given a 3x3 matrix (list of lists):
#       matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#   Use a nested list comprehension or nested loops to print
#   the transpose of the matrix (rows become columns).
#   Expected output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
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
# vegetables = ["carrot", "broccoli", "potato", "onion", "tomato"]
# print(vegetables[0])    # carrot
# print(vegetables[-1])   # tomato

# Task 2:
# vegetables.append("spinach")
# vegetables.insert(2, "kale")
# print(vegetables)

# Task 3:
# lst = [10, 20, 30, 40, 50]
# removed = lst.pop(2)
# print("Removed:", removed)   # 30
# print("Remaining:", lst)     # [10, 20, 40, 50]

# Task 4:
# original = [5, 3, 8, 1, 9, 2, 7]
# new_sorted = sorted(original)
# print("Original:", original)     # unchanged
# print("Sorted:  ", new_sorted)

# Task 5:
# animals = ["cat", "dog", "fish", "bird"]
# for i, animal in enumerate(animals):
#     print(f"{i}: {animal}")

# Task 6:
# cubes = [x ** 3 for x in range(1, 9)]
# print(cubes)

# Task 7:
# divisible_by_3 = [x for x in range(1, 11) if x % 3 == 0]
# print(divisible_by_3)  # [3, 6, 9]

# Task 8:
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# transpose = [[matrix[row][col] for row in range(3)] for col in range(3)]
# print(transpose)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
