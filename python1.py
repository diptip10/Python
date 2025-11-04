'''
Python basics 


Python is a general-purpose programming language created by Guido van Rossum in 1991. 
It emphasizes readability and simplicity, 
making it easy for beginners to learn and powerful enough for experts to build complex systems.

Key Features :
1. Easy to Read and Write - Python's syntax is simple and close to English.

2. Interpreted Language - You don't need to compile your code; Python runs it directly.

3. Dynamically Typed - You don't need to declare variable types explicitly.

4. Extensive Libraries - Python has huge libraries for almost everything:

            Data analysis: pandas, numpy

            Machine learning: scikit-learn, tensorflow

            Web development: Django, Flask

            Automation: os, selenium

5. Cross-Platform - Works on Windows, macOS, and Linux.

6. Object-Oriented - Supports OOP concepts like classes and inheritance.

7. Open Source - Free to use and has a large community for support.


'''

# # Python identifier
# -----------------------
#  python identifier are names you assign to a variable, class and function following the spaecific rule 
# regarding the character usage, starting letters and avoiding reserved key

name = 'seeya'  #variable identifier

def greet():          # function identifier
    print("Hello")

greet()

class Student:        # class identifier
    pass

# Rules for Writing Identifiers in Python
# ------------------------------------------
# 1. Must start with a letter (A–Z, a–z) or an underscore (_)
# 2. Can contain letters, digits, and underscores
# 3. Cannot start with a digit
# 4. No special characters like @, $, %
# 5. Cannot be a keyword (e.g., if, class, for)
# 6. Case-sensitive (name ≠ Name)

# Python Statements
# -----------------
# A Python statement is an instruction that the Python interpreter can execute.

# Example 1: Assignment statement
x = 10   # assigns value 10 to variable x

# Example 2: Print statement
print("Hello, Python!")   # prints text to the console

# Example 3: Conditional statement
if x > 5:
    print("x is greater than 5")

# Example 4: Loop statement
for i in range(3):
    print("Loop count:", i)

# Example 5: Function definition statement
def greet():
    print("Welcome to Python!")

greet()
