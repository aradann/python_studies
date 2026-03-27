# ============================================================
# Chapter: Basic Arithmetic Operations
# Topic: Arithmetic Operators, Order of Operations, Math Module
# ============================================================
#
# DESCRIPTION:
#   Python provides a rich set of arithmetic operators for
#   working with numbers.  This chapter covers all core
#   operators, operator precedence (order of operations),
#   augmented assignment, and the built-in math module for
#   more advanced calculations.
#
# LEARNING GOALS:
#   - Use all arithmetic operators: +, -, *, /, //, %, **
#   - Understand operator precedence (PEMDAS / BODMAS)
#   - Use augmented assignment operators (+=, -=, *=, /=, …)
#   - Apply built-in functions: abs(), round(), divmod(), pow()
#   - Use the math module: sqrt, ceil, floor, log, pi, e
#   - Solve real-world arithmetic problems in Python
#
# ============================================================
# EXAMPLES
# ============================================================

# --- Core arithmetic operators ---

# Example 1: The seven arithmetic operators
a = 17
b = 5
print("Addition:        ", a + b)   # 22
print("Subtraction:     ", a - b)   # 12
print("Multiplication:  ", a * b)   # 85
print("True division:   ", a / b)   # 3.4   (always float)
print("Floor division:  ", a // b)  # 3     (integer quotient)
print("Modulus:         ", a % b)   # 2     (remainder)
print("Exponentiation:  ", a ** b)  # 1419857

# --- Operator precedence ---

# Example 2: PEMDAS – Parentheses, Exponents, Mul/Div, Add/Sub
result = 2 + 3 * 4        # multiplication before addition
print(result)             # 14

result_parens = (2 + 3) * 4   # parentheses first
print(result_parens)          # 20

# Example 3: Mixed precedence
print(10 - 2 ** 3)        # 10 - 8  = 2   (** before -)
print(10 / 2 + 3 * 4)     # 5.0 + 12 = 17.0

# --- Augmented assignment ---

# Example 4: Shortcuts that modify a variable in place
x = 10
x += 5    # x = x + 5  → 15
print(x)
x -= 3    # x = x - 3  → 12
print(x)
x *= 2    # x = x * 2  → 24
print(x)
x //= 7   # x = x // 7 → 3
print(x)
x **= 4   # x = x ** 4 → 81
print(x)

# --- Built-in arithmetic functions ---

# Example 5: abs() – absolute value
print(abs(-42))    # 42
print(abs(3.7))    # 3.7

# Example 6: round() – round to n decimal places
print(round(3.14159, 2))   # 3.14
print(round(2.5))          # 2  (banker's rounding)
print(round(3.5))          # 4

# Example 7: divmod() – quotient and remainder together
quotient, remainder = divmod(17, 5)
print(quotient, remainder)   # 3 2

# Example 8: pow() – exponentiation (same as **)
print(pow(2, 10))          # 1024
print(pow(2, 10, 1000))    # 24  (modular exponentiation: 2**10 % 1000)

# --- math module ---

import math

# Example 9: Square root and power
print(math.sqrt(144))      # 12.0
print(math.pow(3, 4))      # 81.0  (always float)

# Example 10: Ceiling and floor
print(math.ceil(4.1))      # 5
print(math.floor(4.9))     # 4

# Example 11: Logarithms
print(math.log(math.e))    # 1.0  (natural log)
print(math.log(100, 10))   # 2.0  (log base 10)
print(math.log2(8))        # 3.0

# Example 12: Constants
print(math.pi)    # 3.141592653589793
print(math.e)     # 2.718281828459045

# Example 13: Practical – distance between two points
x1, y1 = 0, 0
x2, y2 = 3, 4
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("Distance:", distance)   # 5.0

# Example 14: Practical – compound interest
principal = 1000
rate = 0.05        # 5%
years = 10
amount = principal * (1 + rate) ** years
print(f"After {years} years: ${amount:.2f}")   # $1628.89


# ============================================================
# TASKS
# ============================================================
#
# Task 1:
#   Create two variables, a = 36 and b = 7.
#   Print all seven arithmetic results:
#   a + b, a - b, a * b, a / b, a // b, a % b, a ** b.
#
# Task 2:
#   Without running the code first, predict the result of:
#       3 + 4 * 2 - 10 / 5
#   Then verify your prediction by printing it.
#
# Task 3:
#   Start with a variable score = 50.
#   Use augmented assignment operators to:
#     • add 20
#     • multiply by 3
#     • subtract 10
#     • floor-divide by 4
#   Print score after each step.
#
# Task 4:
#   Use divmod() to find how many full weeks and remaining days
#   are in 100 days.  Print a message like:
#       "100 days = 14 weeks and 2 days"
#
# Task 5:
#   Use the math module to calculate:
#     a) The hypotenuse of a right triangle with legs 8 and 15.
#     b) The ceiling and floor of 7.3.
#     c) log₂(256).
#
# Task 6:
#   The formula for converting Celsius to Fahrenheit is:
#       F = C * 9/5 + 32
#   Write a snippet that converts 0 °C, 100 °C, and -40 °C
#   to Fahrenheit and prints each result.
#
# Task 7:
#   A rectangle has width 8.5 and height 4.2.
#   Calculate and print:
#     • its area (width * height)
#     • its perimeter (2 * (width + height))
#     • the length of its diagonal (use math.sqrt)
#   Round every result to 2 decimal places.
#
# Task 8 (challenge):
#   The formula for the nth term of a geometric sequence is:
#       a_n = a_1 * r ** (n - 1)
#   where a_1 is the first term and r is the common ratio.
#   Given a_1 = 3 and r = 2, print the first 8 terms.
#   Then print their sum.
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
# a = 36
# b = 7
# print(a + b)    # 43
# print(a - b)    # 29
# print(a * b)    # 252
# print(a / b)    # 5.142857142857143
# print(a // b)   # 5
# print(a % b)    # 1
# print(a ** b)   # 78364164096

# Task 2:
# 3 + 4 * 2 - 10 / 5
# = 3 + 8 - 2.0
# = 9.0
# print(3 + 4 * 2 - 10 / 5)   # 9.0

# Task 3:
# score = 50
# score += 20
# print(score)    # 70
# score *= 3
# print(score)    # 210
# score -= 10
# print(score)    # 200
# score //= 4
# print(score)    # 50

# Task 4:
# weeks, days = divmod(100, 7)
# print(f"100 days = {weeks} weeks and {days} days")   # 14 weeks and 2 days

# Task 5:
# import math
# a) hypotenuse
# hyp = math.sqrt(8 ** 2 + 15 ** 2)
# print(hyp)    # 17.0
# b) ceiling and floor
# print(math.ceil(7.3))    # 8
# print(math.floor(7.3))   # 7
# c) log base 2
# print(math.log2(256))    # 8.0

# Task 6:
# for c in [0, 100, -40]:
#     f = c * 9 / 5 + 32
#     print(f"{c} °C = {f} °F")
# 0 °C = 32.0 °F
# 100 °C = 212.0 °F
# -40 °C = -40.0 °F

# Task 7:
# import math
# width, height = 8.5, 4.2
# area = round(width * height, 2)
# perimeter = round(2 * (width + height), 2)
# diagonal = round(math.sqrt(width ** 2 + height ** 2), 2)
# print("Area:     ", area)       # 35.7
# print("Perimeter:", perimeter)  # 25.4
# print("Diagonal: ", diagonal)   # 9.49

# Task 8:
# a1, r = 3, 2
# terms = [a1 * r ** (n - 1) for n in range(1, 9)]
# for n, term in enumerate(terms, start=1):
#     print(f"a_{n} = {term}")
# print("Sum:", sum(terms))   # 765
