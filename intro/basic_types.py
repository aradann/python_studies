# ============================================================
# Chapter: Intro
# Topic: Basic Types — int and float
# ============================================================
#
# DESCRIPTION:
#   Python has built-in numeric types for whole numbers (int)
#   and decimal/floating-point numbers (float).  Understanding
#   how to create, inspect, and manipulate them is fundamental
#   to almost every Python program.
#
# LEARNING GOALS:
#   - Declare int and float variables
#   - Perform arithmetic operations (+, -, *, /, //, %, **)
#   - Understand integer vs. float division
#   - Use type() and isinstance() to inspect types
#   - Convert between int and float
#
# ============================================================
# EXAMPLES
# ============================================================

# --- int ---

# Example 1: Declaring integers
age = 25
year = 2024
negative = -7
print(age, year, negative)

# Example 2: Basic arithmetic with integers
a = 10
b = 3
print("Addition:       ", a + b)   # 13
print("Subtraction:    ", a - b)   # 7
print("Multiplication: ", a * b)   # 30
print("Floor division: ", a // b)  # 3  (integer division)
print("Modulus:        ", a % b)   # 1  (remainder)
print("Exponentiation:", a ** b)   # 1000

# Example 3: Checking the type
print(type(age))          # <class 'int'>
print(isinstance(age, int))  # True

# --- float ---

# Example 4: Declaring floats
pi = 3.14159
temperature = -0.5
scientific = 1.5e3   # 1500.0
print(pi, temperature, scientific)

# Example 5: Arithmetic with floats
x = 7.5
y = 2.0
print("True division:", x / y)   # 3.75
print("Floor division:", x // y) # 3.0

# Example 6: Checking the type
print(type(pi))               # <class 'float'>
print(isinstance(pi, float))  # True

# --- Conversions ---

# Example 7: int to float and float to int
print(float(10))    # 10.0
print(int(3.99))    # 3  (truncates, does NOT round)
print(round(3.99))  # 4  (rounds)


# ============================================================
# TASKS
# ============================================================
#
# Task 1:
#   Create two integer variables, x and y, with values 15 and 4.
#   Print their sum, difference, product, and floor-division result.
#
# Task 2:
#   What is the remainder when 29 is divided by 6?
#   Calculate it using the modulus operator and print it.
#
# Task 3:
#   Calculate 2 to the power of 10 using the exponentiation
#   operator and print the result.
#
# Task 4:
#   Create a float variable called price set to 9.99.
#   Multiply it by an integer quantity of 3 and print the total.
#   What type is the result?  Print the type as well.
#
# Task 5:
#   Convert the float 7.8 to an integer and print the result.
#   Then convert the integer 5 to a float and print the result.
#   Explain in a comment why int(7.8) does NOT equal 8.
#
# Task 6 (challenge):
#   Write a small snippet that calculates the area of a circle
#   with radius 5.  Use 3.14159 as the value of pi.
#   Formula: area = pi * r ** 2
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

# Task 1:
# x = 15
# y = 4
# print(x + y)   # 19
# print(x - y)   # 11
# print(x * y)   # 60
# print(x // y)  # 3

# Task 2:
# print(29 % 6)  # 5

# Task 3:
# print(2 ** 10)  # 1024

# Task 4:
# price = 9.99
# quantity = 3
# total = price * quantity
# print(total)        # 29.97
# print(type(total))  # <class 'float'>

# Task 5:
# print(int(7.8))    # 7
# print(float(5))    # 5.0
# int() truncates toward zero — it drops the decimal part without rounding.

# Task 6:
# pi = 3.14159
# r = 5
# area = pi * r ** 2
# print(area)  # 78.53975
