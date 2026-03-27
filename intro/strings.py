# ============================================================
# Chapter: Intro
# Topic: Strings
# ============================================================
#
# DESCRIPTION:
#   Strings are sequences of characters and one of the most
#   commonly used types in Python.  This file covers creation,
#   indexing, slicing, common methods, and formatting.
#
# LEARNING GOALS:
#   - Create strings with single and double quotes
#   - Use escape characters
#   - Index and slice strings
#   - Use common string methods (upper, lower, strip, split, join, …)
#   - Format strings using f-strings and .format()
#   - Check membership and iterate over a string
#
# ============================================================
# EXAMPLES
# ============================================================

# --- Creating strings ---

# Example 1: Single and double quotes
greeting = "Hello, World!"
name = 'Python'
print(greeting, name)

# Example 2: Multi-line string
poem = """Roses are red,
Violets are blue,
Python is great,
And so are you!"""
print(poem)

# Example 3: Escape characters
print("She said: \"Hello!\"")   # double-quote inside double-quoted string
print("Line one\nLine two")      # newline
print("Column1\tColumn2")        # tab

# --- Indexing and slicing ---

word = "Python"

# Example 4: Positive and negative indexing
print(word[0])   # P   (first character)
print(word[-1])  # n   (last character)

# Example 5: Slicing  [start:stop:step]
print(word[0:3])   # Pyt
print(word[2:])    # thon
print(word[:4])    # Pyth
print(word[::-1])  # nohtyP  (reversed)

# --- String methods ---

s = "  Hello, Python World!  "

# Example 6: Case methods
print(s.upper())
print(s.lower())
print("hello world".title())

# Example 7: Stripping whitespace
print(s.strip())    # removes leading and trailing spaces
print(s.lstrip())   # left only
print(s.rstrip())   # right only

# Example 8: Finding and replacing
sentence = "I love Python"
print(sentence.find("Python"))     # 7  (start index)
print(sentence.replace("Python", "coding"))  # I love coding

# Example 9: Splitting and joining
csv_line = "apple,banana,cherry"
fruits = csv_line.split(",")       # ['apple', 'banana', 'cherry']
print(fruits)
print(" | ".join(fruits))          # apple | banana | cherry

# Example 10: Membership test
print("Python" in sentence)   # True
print("Java" in sentence)     # False

# --- String formatting ---

# Example 11: f-strings (recommended, Python 3.6+)
language = "Python"
version = 3
print(f"I am learning {language} {version}!")

# Example 12: .format()
print("I am learning {} {}!".format(language, version))

# Example 13: String length
print(len("Hello"))  # 5


# ============================================================
# TASKS
# ============================================================
#
# Task 1:
#   Create a variable called full_name that contains your first
#   and last name separated by a space.  Print it.
#
# Task 2:
#   Given the string "Hello, World!", print only the word "World"
#   using slicing.
#
# Task 3:
#   Take the string "  python programming  " and print it with:
#     a) All whitespace removed from both ends
#     b) All characters in uppercase
#     c) The word "programming" replaced with "is fun"
#
# Task 4:
#   Split the sentence "the cat sat on the mat" into a list of
#   words and print the list.  Then join them back with hyphens
#   and print the result.
#
# Task 5:
#   Use an f-string to print: "My name is <name> and I am <age> years old."
#   Use variables for name and age.
#
# Task 6:
#   Check whether the letter 'z' is in the string "Python" and print
#   the result.  Also print the number of characters in "Python".
#
# Task 7 (challenge):
#   Reverse the string "abcde" using slicing, without using any
#   built-in reverse function, and print the result.
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
# full_name = "Jane Doe"
# print(full_name)

# Task 2:
# s = "Hello, World!"
# print(s[7:12])  # World

# Task 3:
# s = "  python programming  "
# print(s.strip())                          # a)
# print(s.strip().upper())                  # b)
# print(s.strip().replace("programming", "is fun"))  # c)

# Task 4:
# words = "the cat sat on the mat".split()
# print(words)
# print("-".join(words))

# Task 5:
# name = "Alice"
# age = 30
# print(f"My name is {name} and I am {age} years old.")

# Task 6:
# print('z' in "Python")   # False
# print(len("Python"))     # 6

# Task 7:
# print("abcde"[::-1])  # edcba
