# ============================================================
# Chapter: Loops
# Topic: While Loops
# ============================================================
#
# DESCRIPTION:
#   A `while` loop repeats a block of code for as long as a
#   given condition is True.  Three common patterns are:
#     1. `while <condition>`   — loop until the condition becomes False
#     2. `while not <condition>` — loop until the condition becomes True
#     3. `while True`          — loop forever; exit explicitly with break
#
# LEARNING GOALS:
#   - Write basic while loops with a condition
#   - Use `while not` to loop until something becomes true
#   - Write infinite loops with `while True` and exit with `break`
#   - Use `continue` to skip iterations
#   - Avoid infinite loops by updating the loop variable
#   - Simulate do-while behaviour with `while True` + `break`
#
# ============================================================
# EXAMPLES
# ============================================================

# -------------------------------------------------------
# Pattern 1 — while <condition>
# -------------------------------------------------------

# Example 1: Count up while the counter is less than 5
count = 0
while count < 5:
    print(count)   # 0 1 2 3 4
    count += 1     # IMPORTANT: update the variable to avoid an infinite loop

# Example 2: Count down to zero
n = 5
while n > 0:
    print(n)   # 5 4 3 2 1
    n -= 1

# Example 3: Sum numbers until the total exceeds 20
total = 0
number = 1
while total <= 20:
    total += number
    number += 1
print(f"First total that exceeds 20: {total}")  # 21

# -------------------------------------------------------
# Pattern 2 — while not <condition>
# -------------------------------------------------------

# Example 4: Loop until a target value is found
items = [3, 7, 1, 9, 4, 6]
index = 0
target = 9
while not items[index] == target:
    index += 1
print(f"Found {target} at index {index}")   # Found 9 at index 3

# Example 5: Read-style loop — keep going until a flag is set
found = False
value = 0
while not found:
    value += 1
    if value == 7:
        found = True
print(f"Stopped at value: {value}")   # 7

# -------------------------------------------------------
# Pattern 3 — while True (infinite loop + explicit break)
# -------------------------------------------------------

# Example 6: Basic while True with break
counter = 0
while True:
    print(counter)      # 0 1 2 3 4
    counter += 1
    if counter == 5:
        break           # exit the loop

# Example 7: Simulate a menu loop (no real input — just one pass)
attempts = 0
while True:
    attempts += 1
    choice = "quit" if attempts == 3 else "continue"   # simulated input
    if choice == "quit":
        print("Exiting menu.")
        break
    print(f"Attempt {attempts}: still running.")

# Example 8: Retry pattern — keep trying until success
import random
random.seed(42)          # fixed seed so output is reproducible
while True:
    roll = random.randint(1, 6)
    print(f"Rolled: {roll}")
    if roll == 6:
        print("Got a 6! Stopping.")
        break

# --- break and continue inside while ---

# Example 9: continue — skip even numbers
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue        # skip the rest of the loop body for even i
    print(i)            # prints 1 3 5 7 9


# ============================================================
# TASKS
# ============================================================
#
# Task 1 — while <condition>:
#   Use a while loop to print the numbers 1 to 10 (inclusive).
#
# Task 2 — while <condition>:
#   Write a while loop that starts at 100 and halves the value
#   (using integer division) on each iteration.  Stop when the
#   value drops below 1.  Print the value on each step.
#
# Task 3 — while <condition>:
#   Given the list words = ["apple", "banana", "cherry", "date"],
#   use a while loop to print each word one by one using an index
#   variable that starts at 0.
#
# Task 4 — while not:
#   Use `while not` to keep adding 3 to a variable that starts at
#   0, until it reaches or exceeds 30.  Print the final value.
#
# Task 5 — while not:
#   Given the list data = [2, 5, 11, 3, 17, 8], use `while not`
#   to iterate through the list from the start until you find
#   a value greater than 10.  Print the index and value where
#   you stopped.
#
# Task 6 — while True:
#   Use a `while True` loop to print the squares of 1, 2, 3, …
#   Stop (break) when the square exceeds 50.
#
# Task 7 — while True (do-while pattern):
#   Simulate a password prompt.  Use a list of attempts:
#       attempts = ["wrong", "wrong", "secret"]
#   Use a while True loop that pops the first item from the list
#   each iteration.  If the item equals "secret", print
#   "Access granted" and break; otherwise print "Wrong password".
#
# Task 8 (challenge):
#   Use a while loop to implement the Collatz sequence starting
#   from n = 27:
#     - If n is even, divide it by 2.
#     - If n is odd, multiply it by 3 and add 1.
#   Count and print the number of steps it takes to reach 1.
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
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# Task 2:
# value = 100
# while value >= 1:
#     print(value)
#     value //= 2

# Task 3:
# words = ["apple", "banana", "cherry", "date"]
# i = 0
# while i < len(words):
#     print(words[i])
#     i += 1

# Task 4:
# value = 0
# while not value >= 30:
#     value += 3
# print(value)  # 30

# Task 5:
# data = [2, 5, 11, 3, 17, 8]
# i = 0
# while not data[i] > 10:
#     i += 1
# print(f"Index {i}: {data[i]}")  # Index 2: 11

# Task 6:
# n = 1
# while True:
#     square = n ** 2
#     if square > 50:
#         break
#     print(square)
#     n += 1

# Task 7:
# attempts = ["wrong", "wrong", "secret"]
# while True:
#     attempt = attempts.pop(0)
#     if attempt == "secret":
#         print("Access granted")
#         break
#     print("Wrong password")

# Task 8:
# n = 27
# steps = 0
# while n != 1:
#     if n % 2 == 0:
#         n //= 2
#     else:
#         n = n * 3 + 1
#     steps += 1
# print(f"Reached 1 in {steps} steps")  # 111
