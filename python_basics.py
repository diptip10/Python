"""
Python- developed by Guido van Rossum in 1991.

# Key points about Python (easy to remember)

1. High-level and beginner-friendly

2. Object-oriented and interpreted language

3. Portable and open-source

4. Huge ecosystem of libraries (pandas, NumPy, PySpark, requests, Flask, etc.)

5. Commonly used for data engineering, automation, AI/ML, backend APIs, and scripting


# Comments in Python are non-executable lines used to explain the code, improve readability, 
and help other developers understand the logic.

1. single line- Starts with #
2. multi line- Written using triple quotes ("""   """ ) or ('''  ''')

"""

# keywords
import keyword
print(keyword.kwlist)

# Datatypes in python (general)- Python is dynamically typed language

# 1. Number - integer(int) 10,20
#             float 10.4, 20.5
#             complex (10+j)
# 2. String- str- 'Python', 'data'
# Boolean- bool - True(1), False (0)

eid = 1    # int
ename ='Riya'  # str
esal = 10000.45   # float

# To check the type of variable we have type() function
print(type(eid))
print(type(ename))
print(type(esal))

# concat- possible to concat only similar type of data

# single line of code
a,b,c= 10,20,30
print(a+b+c)

print(10+20)
print("python"+ "python")
print(10.4+20.6)
print(True+False)

#Whenever you are trying to combine two different types of data you will get the type error
print('python' + 10)  # type error as these are two diff values 'str' and 'int'

print(True+10)   # True is nothing but 1
print(False+10.5)

print(10+10.5)   # 10 and 10.5 are both number type

# We can reassign the same variable multiple times
# Reassigning
a= 100
print(a)
a=10  # reassign the same variable 'a'
print(a)

# Swapping data
a,b =10, 20
print(a)
print(b)
a,b = b,a  # swapping of 'a' to 'b' and 'b' to 'a'
print(a)
print(b)

# delete variable
a= 10
print(a)
del a  # here memory is deleted
print(a)  # name error  as we already deleted variable 'a'

# name error-  We will get the name error when corresponding data/ variable/ function is not available


# printing data in different ways
eid, ename, esal = 111, 'siya' , 10000.45
#1 
print(eid)
print(ename)
print(esal)

#2
print("eid", eid)
print("ename", ename)
print("esal", esal)

#3
print(eid, ename, esal)

#4
print("eid=",eid, "ename=",ename,"esal=",esal)

#The input() function is used to take input from the end user.
# It always returns the input as a string, regardless of what the user types.

number1= input('enter first value:')   # value is taken in "str" format
number2= input('enter second value:')
add = number1 + number2
print("addition:", add)

# Formating data
#1. %  -  %d (int) , %g %f (float) , %s (string)
#2. {} -

# to print the data using % option
eid, ename, esal = 111, 'siya' , 10000.45
print("eid= %d ename = %s esal = %g"%(eid,ename,esal))

# print using {}
print("eid= {} ename={} esal={}".format(eid,ename,esal))

print("eid={0} ename={1} esal={2}".format(eid,ename,esal))
# Indexing allows you to choose which value goes into which placeholder {} in a formatted string.
print("eid={0} ename={2} esal={1}".format(eid,ename,esal))

# FLOW CONTROL STATEMENTS
# 1) conditional - 1. if   2.if-else  3. elif
# 2) Interation - 1. for  2. while
# 3) transfer - 1. break  2. continue

## CONDITIONAL STATEMENT

# case 1 :   if-else condition
a=10
if a>20:                         # basic condition
    print('true condition')
else:
    print('false condition')

# case 2 
if True:                            # Boolian constant
    print("true condition")
else:
    print("false condition")

# case 3
if 0:
    print("true condition")
else:
    print("false condition")

# case 4
if True:                    # normal code
    print("python")
    print("python coding")
print("Normal code")

# case 5 
print("if body") if True else print("else body")  # single line code

# case 6 - You should take multiple statements in braces {}
{print("python"),print("code")} if 10<20 else {print("else body"), print("else code")}


# elif condition -- (It is nothing but else if) --else is optional here
a=10
if a==10:
    print("hello")
elif a==20:
    print("good day")
elif a==30:
    print("hii")
else:
    print("nice day")


## ITERATION STATEMENTS

# range function
print(list(range(10)))
print(list(range(4,10)))
print(list(range(4,10,3)))
print(list(range(10,4,-3)))
print(list(range(-10,-5)))
print(list(range(-10,-5,2)))
print(list(range(-5,-10,-2)))

# FOR LOOP: A for loop is used when you want to repeat a block of code for each item in a 
# sequence such as: range(), list, tuple, string, dictionary, set, file

#   CASE 1 
for x in range(10):
    print("python",x)

for x in range(4,10):
    print("python",x)

for x in range(4,10,3):
    print("python",x)

for x in range(10,4,-3):
    print("python",x)

for x in range(-10,-4):
    print("python",x)

for x in range(-10,-4,3):
    print("python",x)

for x in range(-4,-10,-3):
    print("python",x)

L=[10,20,30]
for x in L:
    print(x)

t=(10,20,30)
for x in t:
    print(x)

# CASE 2
for x in range(10):
    print("hello",x)
else:
    print("normal execution of for loop")

# in 3 cases else block is not executed
#case1 - Whenever in the for loop there is break statement, else block will not execute
#ex.
for x in range(10):
    if x == 3:
        break
    print("hello",x)
else:
    print("normal execution of for loop")

#case2 - Whenever you get exceptions in for loop
for x in range(10):
    print("hello",x)
    print(10/0)            # zero division error
else:
    print("normal execution of for loop")

#case3 - when virtual machine/ programme is shut down
import os
for x in range(10):
    print("hii",x)
    os._exit(0)
else:
    ("normal execution of for loop")


# WHILE LOOP - A while loop is used when you want to repeat a block of code as long as a condition is true.
# while (condition):
#     body

a=0
while a<5:
    print("hi")
    a=a+1
    print("normal code")

a=0
while a<10:
    print("python")
    a=a+1
else:
    print("normal execution of while")

# in 3 cases else block not executed
# case1 - Break statement
a=0
while a<10:
    print("hi")
    a=a+1
    if a == 5:
        break
else:
    print("normal execution of while")

# case2 - exception in while
a=0
while a<10:
    print("hello")
    a=a+1
    print(10/0)
else:
    print("normal execution of while")

# case3 - exit(0)
import os
a=0
while a<10:
    print("hi")
    a=a+1
    os._exit(0)
else:
    print("normal execution of while")

# TRANSFER STATEMENT - 1.BREAK  2.CONTINUE  
#1.BREAK - Immediately terminates the loop (for/while) and Control goes outside the loop
#2.CONTINUE - Skips the current iteration and Control goes to the next loop iteration
#case1
for x in range(10):
    if x == 4:
        break
    print(x)

#case2
# if True:
#     print("world")
#     break           # syntax error : 'break' outside loop 
#     print("hello")

#case3
# if True:
#     print("dipti")
#     continue       # syntax error: 'continue' outside loop
#     print("pawar")

#case4
for x in range(10):
    if x==4:    
        continue  # When x == 4 the continue statement skips that iteration That means 4 will not be printed
    print(x)

# break and continue are NOT allowed inside normal conditional statements alone.
# They must be used inside loops (for or while).
# Even if they are written inside an if-statement, that if-statement must itself be inside a loop.

# PYTHON VARIABLES -- A variable is a name that stores a value.
# types --  1. local variable     2. global variable
# local variable -- variable which are declare inside the function, function argument are also local var
#case1
def disp1():            # function use to write the logics of the operation
    print("hello world")
def disp2(name):        # function argument is the local variable
    print("good evening", name)
disp1()
disp2("dipti")

#case2
def disp1(name):         
    print("good morning", name)
def disp2():
    name = "xyz"  # if we declare the variable inside the function then it is local variable
    print("good evening", name)
disp1("abc")
disp2()

#case3 -- scope of local variable is only within the functions
def disp():
    name = "xyz"
    print("good evening",name)
disp()
print(name) # here we are trying to print local variable outside the function  -- name error


#GLOBAL VARIABLES -- variables which are declare outside of the function is call global variable
# scope- all the functions can access the global variable

#case1
name= "xyz"  # global variable
def disp1():
    print("good morning", name)
def disp2():
    print("good evening", name)
disp1()
disp2()

#case2  -- local and global (combination) different names
a,b=10,20        #global variables
def add(x,y):     # x and y are local variables (function arguments)
    print(x+y)   # uses local variables
    print(a+b)   # uses global variables
def multi(x,y):   # x and y are local variables (function arguments)
    print(x*y)    # uses local variables
    print(a*b)    # uses global variables
add(3,3)
multi(4,4)


# Case 3 — Local & Global Variables (Same Names)
a, b = 10, 20 # Global variables

def add(a, b):        # local variables (same name as globals)
    print(a + b)      # uses LOCAL a, b
    print(globals()['a'] + globals()['b'])   # uses GLOBAL a, b

def mul(a, b):        # local variables (same name as globals)
    print(a * b)      # uses LOCAL a, b
    print(globals()['a'] * globals()['b'])   # uses GLOBAL a, b

add(3, 3)
mul(4, 4)
# Whenever local and global variables have the same name, the priority 
# always goes to the local variable. To access the global variable, 
# we must use globals() inside the function.


#case4
name = "dipti"  # global variable
def disp1():
    print(name)   # printing global variable inside the function
disp1()
print(name)     # printing global variable outside the function
# scope of global var - all functions can access global variable

# OBSERVATIONS
#case1
name = "xyz"  # global variable
def disp():
    name = "abc"  # local variable
    print(name)   # printing local variable

disp()  # calling function
print(name)  # printing global variable


#case2 -- When we try to use and modify a global variable inside a function 
# without using the 'global' keyword, Python treats it as a local variable.
# This leads to an error if we use the variable before assigning it.

name = "abc"   # global variable

def disp():
    # The next line will give an error because Python thinks 'name' is local
    # but we are trying to print it before assigning it inside this function
    print(name)  

    name = "xyz"   # local variable (Python treats it as local because of assignment)
    print(name)    # printing local variable

disp()  # calling the function
print(name)  # printing global variable


# SEPERATOR
print(10,20,30,40,sep='%')

print(1,2,3,4,sep="***")


# PYTHON IDENTIFIER
# Any name given to a variable, function, class, module, or object in Python is called an identifier.

# Examples of identifiers:
name = "Dipti"          # 'name' is a variable identifier
age = 25                # 'age' is also a variable identifier

def my_function():      # 'my_function' is a function identifier
    pass

class Student:          # 'Student' is a class identifier
    pass

# Rules for Python Identifiers
# 1. Identifiers can contain alphabets, digits, and underscores (_)
# 2. Cannot start with a digit
# 3. Special characters like @, $, % are not allowed
# 4. Identifiers are case sensitive  (age, Age, AGE are different)
# 5. No length limit
# 6. Cannot use Python keywords (like if, for, while, class) as identifiers

#The global keyword is a reserved keyword in Python used inside a function to tell Python that:
# "This variable is a global variable, not a local variable."
# It allows you to access and modify a global variable from inside a function.

#case1
def disp():
    global x       # this is global keyword
    x = "xyz"      # modifying the global variable
    print(x)

disp()
print(x)

#case2
s = "java"
def disp():
    print(s)   # syntax warning : name is used prior the global declaration
    global s
    s = "python"
    print(s)

disp()
print(s)

#case3
s = "xyz"   # Global variable

def disp():
    
    global s   # Telling Python that we want to use the global variable 's'
    s = "pqr"   # Changing the value of the global variable
    print(s)   # Printing the updated value inside the function

disp()   # Calling the function

# Printing the global variable outside the function 
# It will show the updated value because we used 'global'
print(s)

# case 1 -- UnboundLocalError:
# This error occurs because Python considers 's' as a local variable 
# inside the function since we assign a value to it (s = "john").
# But before assigning, we try to print(s), which causes:
# UnboundLocalError: local variable 's' referenced before assignment

s = "alex"   # global variable
def disp():
    # Python thinks 's' is LOCAL because of the assignment below.
    # So, this print tries to access local 's' before it is assigned.
    print(s)  # Causes UnboundLocalError
    s = "john"   # local variable (Python treats this as local)
    print(s)

disp()
print(s)   # prints the global variable "alex"

# case 2 - If we are NOT printing or using the global variable inside the function
# then we CAN declare a local variable with the same name.
# Python will treat the 's' inside the function as a LOCAL variable.

s = "alex"   # global variable
def disp():
    s = "john"   # local variable (only inside this function)
    print(s)     # prints the local variable "john"

# calling the function
disp()

# printing the global variable outside the function
# remains unchanged because local variable does not affect global variable
print(s)     # prints "alex"


# NONLOCAL KEYWORD
# inside the inner function, to represent (modify) the outer function variable
# we have to use the nonlocal keyword
#case1

def outer():
    name1 = "AAA"     # outer function variable

    def inner():      # inner function declaration
        nonlocal name1   # tells Python: use the variable from the outer function
        name1 = "BBB"    # modifying the outer function variable

    print(name1)     # printing outer function variable before calling inner()
    inner()          # calling inner function (this changes name1)
    print(name1)     # printing outer function variable after modification

outer()

#case2

name  = 'PQR'   # global variable

def outer():
    name1 = "ABC"   # outer function variable

    def inner():      # inner function declaration
        nonlocal name1   # use the variable from outer() function
        name1 = "XYZ"     # modifying the outer function variable

        global name       # use the global variable
        name = "EFG"      # modifying the global variable

    print(name1)   # before calling inner() → ABC
    inner()
    print(name1)   # after calling inner() → XYZ

outer()
print(name)        # global name → EFG


# FUNCTIONS IN PYTHON
# 1. PREDEFINED FUNCTIONS (like print(), len(), type())
# 2. USER-DEFINED FUNCTIONS (functions we create using def)

# Functions are used to write the logic of an application and avoid repetition.

# To declare a function, we use the keyword: def
# Function name in this example: disp

def disp():        # Function declaration with zero arguments
    print("good morning:")

disp()             # Function call

# function declaration under function calling (Declaration first, then calling)

# case 1
def disp1():                 # Function declaration with zero arguments
    print("good morning:")

def disp2(name):             # Function declaration with one argument
    print("good evening:", name)

disp1()                      # Function calling
disp2("Dipti")               # Function calling with argument


# case 2 -- variable accessing in function

x, y = 100, 200     # Global variables

def add(a, b):       # Function with 2 arguments
    print(a + b)      # Using local variables (a, b)
    print(x + y)      # Using global variables (x, y)

def mul(a, b):       # Another function with 2 arguments
    print(a * b)      # Using local variables
    print(x * y)      # Using global variables

add(20, 20)           # Function calling
mul(30, 30)


# FUNCTION ARGUMENTS - 1. default  2. required  3. keyword   4. varriable
# 1. default argument -- If a value is not passed, Python uses the default value.

# Function with default arguments
def disp(eid=111, ename='dipti', esal=20000):
    print(eid, ename, esal)# This line prints the employee details
    print("****")  # Separator line

disp()  # No values passed → all default values will be used

disp(222)   # Only the 1st argument passed → eid will change, others use default

disp(333, 'Tina')  # 1st and 2nd arguments passed → eid and ename change, esal stays default

disp(444, 'Riya', 10000)   # All arguments passed → no default values used


#2. required argument - You must pass values for these arguments; otherwise, you get an error.

def disp(eid, ename, esal):
    print(eid, ename, esal)
    print("****")

disp(111,'anu', 10000)


## Mixing default and required arguments in Python

# RULE:
# Once you start giving default values, all the arguments to the RIGHT 
# must also have default values.
#
# VALID EXAMPLES:
# def disp(eid, ename="anu", esal=10000)  → valid (default arguments are at the end)
# def disp(eid, ename, esal=10000)        → valid (default argument comes last)
#
# INVALID EXAMPLE:
# def disp(eid, ename="anu", esal)        → invalid 
# Python error: "non-default argument follows default argument"
# Because 'esal' (required) comes AFTER a default argument.


# -------------------------------------------
# Correct function definition
# -------------------------------------------
def disp(eid, ename="priya", esal=10000):
    # This prints employee details
    print(eid, ename, esal)
    print("***")   # separator

disp(111)  # Only eid provided → ename and esal use default values

disp(222, "siya")  # eid and ename provided → esal uses default

disp(333, "Diya", 20000)    # All values provided → no default used

# 3. Keyword Arguments
# When calling a function, we can pass values in the form key = value.
# The order does NOT matter because each value is mapped using the key name.

def disp(eid, ename, esal):
    print(eid, ename, esal)   # Print the employee information
    print("***")  # Separator line
# Calling using keyword arguments
disp(eid=111, ename='Tina', esal=10000)   # Order is same as function definition, but not required

disp(eid=222, esal=20000, ename="Riya") # Order changed,still valid because values are matched using keys

# RULE:
# Once you start using a keyword argument in a function call,
# all the arguments that come AFTER it must also be keyword arguments.

# ---------------------------------------------
# Examples:
# ---------------------------------------------
# disp(111, ename = 'ABC', esal = 10000) : valid -- # First argument is positional, next are keyword arguments
# disp(111, 'ABC', esal = 10000) : valid -- # First two arguments are positional, last is keyword

# disp(111, ename = 'ABC', 10000) : invalid -- # Keyword argument is used first, but after
#  that a positional argument appears. This breaks the rule → SyntaxError


# 4. VARIABLE ARGUMENT (*args)
# Used when you don't know how many values will be passed.

# ------------------ Case 1 ------------------
# *a collects all positional arguments into a tuple.
def disp(*a):
    for x in a:
        print(x)

disp()           # no arguments → empty tuple
disp(10)         # one argument
disp(10, 20)     # multiple arguments


# ------------------ Case 2 ------------------
# Required argument + variable arguments
def disp(name, *a):   # 'name' MUST be passed, *a collects the rest
    print(name)
    for x in a:
        print(x)

disp("aaa")           # only required argument
disp("bbb", 10)       # + one extra value
disp("ccc", 10, 20)   # + multiple values


# ------------------ Case 3 ------------------
# Default argument + variable arguments
def disp(name="Riya", *a):  # if name not passed, default "Riya" is used
    print(name)
    for x in a:
        print(x)

disp()                 # uses default name
disp("aaa")            # overrides default
disp("bbb", 10)
disp("ccc", 10, 20)


# ------------------ Case 4 ------------------
# Variable argument FIRST, then a normal argument
# Here 'name' must ALWAYS be passed as a keyword argument.
def disp(*a, name):
    print(name)
    for x in a:
        print(x)

disp(name="Tina")              # no positional args, only keyword arg
disp(10, 20, 30, name="Tina")  # positional args collected into *a


# RULE:
# When variable argument (*a) comes LAST → remaining values become part of *a.
#     Example: def disp(name, *a)

# When *a comes FIRST → next normal arg MUST be passed using keyword.
#     Example: def disp(*a, name)
#---------------------------------------------------------------------------------


# RETURN TYPE-------------
#case1
def disp():
    print("good morning")
    return 10

x= disp() # holding return value
print("return value:",x)

# instead of holding and calling the function we can also directly call the function
#ex
def disp():
    print("good morning")
    return 10
print(disp())

# case 2
# Once a return statement is executed,
# the function stops immediately.
# Any code after return will NOT run.

def disp():
    print("good morning")
    return 10      # function ends here
    return 20      # this line is ignored (unreachable)

x = disp()          # calls the function
print("returned value:", x)


# case 3 : Returning one of two values using if-else

def disp():
    print("good morning")

    # Condition decides which value to return
    if 10 < 20:
        return "Tina"   # this will return if the condition is true
    else:
        return "Riya"   # this will return if the condition is false

x = disp()   # the returned value (Tina or Riya) is stored in x
print("return value =", x)


# case 4
# If a function does not have a return statement,
# Python automatically returns "None" by default.

def disp():
    print("good morning")   # only prints something

x = disp()                  # disp() returns None automatically
print("return value =", x)  # prints None

##INNER FUNCTION / NESTED FUNCTION
def outer():
    name1 = "ABC"              # outer function variable
    print("outer =", name1)

    def inner():
        name2 = "PQR"          # inner function variable
        print("inner =", name2)
        print(name1)           # inner can access outer variable

    inner()                    # calling inner function

outer()                         # calling outer function


## WITHOUT USING NON LOCAL KEYWORD
# case1

def outer():
    name1 = "AAA"              # outer variable

    def inner():
        name1 = "BBB"          # this creates a NEW local variable inside inner()
        print("inner =", name1)

    print(name1)               # prints outer variable
    inner()                    # call inner()
    print(name1)               # still prints outer variable (unchanged)

outer()

# case 2: using nonlocal to modify outer function variable

def outer():
    name1 = "dipti"          # outer variable

    def inner():
        nonlocal name1       # use outer variable
        name1 = "pawar"      # modify outer variable
        print("inner =", name1)

    print(name1)             # before calling inner()
    inner()                  # call inner()
    print(name1)             # after inner() modifies it

outer()


# case 3 :
# If inner function is using outer function variable,
# then inside the inner function we cannot create a local variable
# with the same name (it will give error).

def outer():
    name1 = "dipti"              # outer variable

    def inner():
        print(name1)             # using outer variable
        name1 = "pawar"          # ERROR: trying to create local var with same name
        print("inner =", name1)

    inner()

outer()


# GLOBAL KEYWORD
# inside the function to represent the outer function var we are using global keyword

# GLOBAL, NONLOCAL, LOCAL variable behavior 

def outer():
    # This is the variable inside outer() function
    name1 = "dipti"

    def inner1():
        # This creates a LOCAL variable inside inner1()
        # It DOES NOT affect outer() variable
        name1 = "anu"
        print("inner1 function name =", name1)

    def inner2():
        # nonlocal means: use the variable from the outer() function
        nonlocal name1
        name1 = "ajinkya"   # This will change outer() variable
        print("inner2 function name =", name1)

    def inner3():
        # global means: use the global variable (outside all functions)
        global name1
        name1 = "pawar"     # This will create/update global variable
        print("inner3 function name =", name1)

    # Print value inside outer() initially
    print("outer before inner1:", name1)

    inner1()   # local change only
    print("outer after inner1:", name1)

    inner2()   # modifies outer() variable using nonlocal
    print("outer after inner2:", name1)

    inner3()   # modifies global variable
    print("outer after inner3:", name1)   # outer variable is still same

# Call the outer() function
outer()

# Print global name1 (set by inner3)
print("global name1:", name1)


# STRING DATA TYPE
# string represents the group of characters enclose within single or double quotes
# immutable - modifications are not allowed
# index - +ve and -ve

# Example 1: Creating Strings in Python

# String created using double quotes
s1 = "dipti"
print(s1)             # Output: dipti
print(type(s1))       # Output: <class 'str'> → data type is string

# String created using single quotes
s2 = 'Anu'
print(s2)             # Output: Anu

#-------------------------------------------------------------
# Example 2: String Indexing & Slicing

# Negative Indexing : -8 -7 -6 -5 -4 -3 -2 -1
# Characters         i   n   d   e   x   i   n   g

# Positive Indexing : 0  1  2  3  4  5  6  7

s = "indexing"

# --------------------
# POSITIVE INDEXING
# --------------------

print(s[2])        # 'd'  → character at index 2

print(s[2:4])      # 'de' → substring from index 2 to 3

print(s[1:4:2])    # 'nx' → characters at index 1 and 3 (step = 2)

print(s[2:])       # 'dexing' → from index 2 till end

print(s[:4])       # 'inde' → start to index 3

print(s[:])        # 'indexing' → whole string


# print(s[9])      # ERROR → index out of range (string length is 8)


# --------------------
# NEGATIVE INDEXING
# --------------------

print(s[-2])       # 'n' → 2nd character from end

print(s[-5:-1])    # 'exin' → slice using negative indexes

print(s[:-1])      # 'indexin' → whole string except last char

print(s[-5:])      # 'exing' → from -5 to end

print(s[:])        # 'indexing' → entire string
# print(s[-9])     # ERROR → index out of range

# Example 3 : length and strip function
# strip()  → removes spaces/characters from BOTH sides
# lstrip() → removes spaces/characters from the LEFT side
# rstrip() → removes spaces/characters from the RIGHT side
# len()    → returns length of the string

s = "   dipti   "     # string with leading and trailing spaces

print(len(s))          # total length including spaces → 11

print(s.strip())       # removes spaces from both sides → "dipti"

print(len(s.strip()))  # length of "dipti" → 5


s1 = "@@@dipti###"     # string with special characters on both sides

print(s1.lstrip("@"))  # removes only '@' from LEFT → "dipti###"

print(s1.rstrip("#"))  # removes only '#' from RIGHT → "@@@dipti"

# combination of rstrip() then lstrip()
print(s1.rstrip("#").lstrip("@"))  # first remove '#', then remove '@' → "dipti"

# Example 4 : id(), is, == , in operators

# id()        → prints the memory address of a variable
# is          → compares memory address (True if both refer to SAME object)
# is not      → opposite of is
# ==, !=      → compare DATA (True if content is same)
# in, not in  → checks if a substring exists in another string

name1 = "dipti"
name2 = "nikita"
name3 = "dipti"     # same content as name1

# ----------------- id() : memory address -----------------
print(id(name1))     # memory address of name1
print(id(name2))     # memory address of name2
print(id(name3))     # name1 and name3 may have SAME memory address (string interning)

# ----------------- is, is not : memory comparison -----------------
print(name1 is name2)       # False → memory different
print(name1 is name3)       # True  → same memory due to string interning
print(name1 is not name2)   # True
print(name1 is not name3)   # False

# ----------------- ==, != : data comparison -----------------
print(name1 == name2)       # False → data not same
print(name1 == name3)       # True  → data is same
print(name1 != name2)       # True
print(name1 != name3)       # False

# ----------------- in, not in : substring check -----------------
print("di" in name1)        # True → 'di' exists in 'dipti'
print("anu" in name1)       # False → substring not present
print("di" not in name1)    # False
print("anu" not in name1)   # True


# Example 5 : Different ways to format data in Python
# Approaches:
# 1. Using % formatting (old style)
# 2. Using {} with format()
# 3. Using {} with positional indexes
# 4. Using f-strings (modern and recommended)

# Data
eid, ename, esal = 111, "tina", 20000.45

# Using % formatting (old style)
# %d → integer
# %s → string
# %g → float (removes unnecessary zeros)
print("eid = %d, ename = %s, esal = %g" % (eid, ename, esal))

# Using format() without indexes
print("eid = {}, ename = {}, esal = {}".format(eid, ename, esal))

# Using format() with positional indexes
print("eid = {0}, ename = {1}, esal = {2}".format(eid, ename, esal))

# Using f-strings (most recommended)
print(f"eid = {eid}, ename = {ename}, esal = {esal}")

# Example 6 : CONCATENATION AND REPLICATION

# Concatenation (+) and Replication (*) operations work only on the same data type.
# Strings can be concatenated with strings.
# Strings can be replicated using * with an integer.
# Combining different types (e.g., string + int) will give a TypeError.

s1 = "priya"
s2 = "AAA"

s3 = s1 + s2   # This joins two strings together.
print(s3)  

# Then concatenated using +
ss = s1 * 3 + s2 * 2   # s1*3 → "priya" repeated 3 times  and s2*2 → "AAA" repeated 2 times
print(ss) 


# Example 7 : RELATIONAL OPERATORS 
# Operators:  > , >= , <= , == , !=
# These operators compare two values and return a boolean (True/False).
# For strings, comparison is done using **lexicographical order** (dictionary order)
# Python compares character by character based on ASCII/Unicode values.

print("riya" > "siya")   # False, because 'r' comes before 's'
print("riya" < "siya")   # True
print("riya" >= "siya")  # False
print("riya" <= "siya")  # True

print("riya" == "siya")  # False, strings are different
print("riya" == "riya")  # True, both strings are same
print("riya" != "siya")  # True, because they are not equal

# Example 8 : String useful functions

text = "hello everyone"

print("upper = ", text.upper())   # upper() → Converts entire string to uppercase

print("lower = ", text.lower())  # lower() → Converts entire string to lowercase

print("capitalize = ", text.capitalize()) # capitalize() → Makes the first character uppercase and the rest lowercase

# split() → Breaks the string into words (default: split by space)
# join() → Joins the list back into a string using a separator
# Here "+" is used as the joining character
print("join = ", "+".join(text.split()))   # Output: hello+everyone

print("replace=",text.replace("everyone","world")) # replace(old, new)→ Replaces a substring with another substring

# Example 9

# SPLIT FUNCTION
str2 = "hello how are you.where are you"
print(str2.split())  # split() with no argument splits by space

print(str2.split(".")) # split(".") splits the string wherever a dot is found

# ENUMERATE FUNCTION
# enumerate() gives index + value pair from the string
str = "python"
print(tuple(enumerate(str)))  # converting enumerate object to tuple

print(list(enumerate(str))) # converting enumerate object to list

# COUNT FUNCTION
s = "programming"
print(s.count('a')) # count how many times 'a' occurs
print(s.count('m')) # count how many times 'm' occurs
print(s.count('g', 4)) # count how many times 'g' occurs starting from index 4
print(s.count('pro', 0, 3)) # count 'pro' in the substring from index 0 to 3
print(s.count('pro', 3, 6)) # count 'pro' in the substring from index 3 to 6

# Example 10
str1 = "welcome to python programming"

print(str1.endswith("programming"))   # True → string ends with "programming"
print(str1.endswith("to", 2, 16))      # False → substring[2:16] does not end with "to"
print(str1.startswith("welcome"))      # True → starts with "welcome"
print(str1.startswith("come", 3, 10))  # True → substring[3:10] starts with "come"


# Example 11 : find , index and swapcase
str = "lets learn python"

print(str.find("learn"))    # returns starting index if found → 5
print(str.find("hello"))    # returns -1 if not found
print(str.index("earn"))    # returns index if found → 6
print(str.index("l", 3, 9)) # search 'l' between index 3 and 9 → returns 5
# print(str.index("hello")) # ValueError if substring not found

string1 = "python programming language"
print(string1.swapcase())   # swap upper ↔ lower case

# Example 12
# isalnum() returns True only if all characters in the string are alphanumeric (A–Z, a–z, 0–9) 
# and there are no spaces or special characters.
str = "welcome to coding "
print(str.isalnum())

str1 = "python36"    # alphanumeric
print(str.isalnum())

# Returns True if ALL characters in the string are only alphabets (A–Z or a–z)
str2 = "Hellopython"
print(str2.isalpha())

str3 = "This is Python3.1.6"
print(str3.isalpha())

# Returns True if ALL characters are digits (0–9)
str4 = "HelloPython"
print(str4.isdigit())

str5 = "9876547"
print(str5.isdigit())

# Example 13
str1 = "Python"
print(str1.islower())   # islower() : Returns True if all characters are lowercase.

str2 = "python"
print(str2.isupper())  # isupper() : Returns True if all characters are uppercase.

str3 = "python"
print(str3.islower())

str4 = "PYTHON"
print(str4.isupper())

str5 = "WELCOME TO THE WORLD"
print(str5.isspace())   # isspace() : Returns True if the string contains only spaces / whitespace

str6 = " "
print(str6.isspace())

# without using count function how to count no. of occurences
s1 = "pythonpython"
print(s1.count('p'))  # with count function

count = 0
for x in s1:
    if x == 'p':
        count = count + 1
print(count)

s = "python python is python"
print(s.count('python'))

s = "python python is python"
words = s.split()
count = 0
for x in words:
    if x == "python":
        count+=1
print(count)

# LIST DATA TYPE / STRUCTURE
# Used to store group of elements (homogeneous/heterogeneous).
# Ordered → follows indexing (positive & negative).
# Allows duplicate values.
# Mutable → can add, update, delete elements.

# Ex 1
l1 = [10, 20, 30, 40]     # homogeneous list
print(l1)
print(type(l1))            # check type

l2 = [10, 10.5, 'python']  # heterogeneous list
print(l2)

l3 = []                    # empty list
print(l3)

l4 = list()                # empty list using list()
print(l4)

l5 = list("python")        # list from string → each char becomes element
print(l5)
# Note: list() takes only 1 iterable argument

# Ex 2 : Indexing : forward and backward
#     -4  -3  -2  -1   : backward
l1 = [10, 20, 30, 40]
#     0   1   2    3   : forward

print(l1[3])
print(l1[1:3])
print(l1[1:])
print(l1[:2])
print(l1[:])
print(l1[0:3:2])

print(l1[-2])
print(l1[-4:-2])
print(l1[:])

# id function: print the memory address
# is , is not : memory comparision
# in  , not in : checking data
# ==  , !=   : data comparision
l1 = [10,20,30]
l2 = [40,50,60]
l3 = l1      # l3 references same list as l1

print(id(l1))
print(id(l2))
print(id(l3))

print(l1 is l2)
print(l1 is l3)
print(l1 is not l2)
print(l1 is not l3)

print(l1 == l2)
print(l1 == l3)
print(l1 != l2)
print(l1 != l3)

print(10 in l1)
print(100 in l1)
print(10 not in l1)

# Ex 4 : unpacking
l1 =  [10,10.4,"python"]
a,b,c = l1
print(a,b,c)
print(type(a),type(b),type(c))
# while unpacking you must assign the no. of variables which are present in the list

# l2 = [10,20,30]
# a,b = l2
# value error : too many values to unpack

# Ex 5 : Nested list (list inside another list)

#       0           1
l1 = [[10, 20], [30, 40]]
#      0   1      0   1

print(l1[0])        # first inner list → [10, 20]
print(l1[1])        # second inner list → [30, 40]

print(l1[0][1])     # element 20 (inner index 1 of first list)
print(l1[1][1])     # element 40 (inner index 1 of second list)

l2 = [[1, 2, 3], ["python", "java"]]
a, b = l2           # unpack two inner lists

print(type(a))      # list
print(type(b))      # list

x, y, z = a         # unpack elements of first inner list
print(x, y, z)      # 1 2 3

# Ex 6 : printing list data using for loop

l1 = [10, 20, 30, 40]

for x in l1:                 # iterate full list
    print(x)

for x in l1[1:3]:            # iterate slice (20, 30)
    print(x)

# for x in l1[3]:
#     print(x)              # ERROR → int is not iterable

l2 = [[1, 2], ["hii", "hello"]]

for x, y in l2:              # unpack inner lists
    print(x)                 # print first element
    print(y)                 # print second element
    print(x, y)              # print both

# Ex 7 : List Comprehension Examples

l1 = [x for x in range(10)]          # numbers 0 to 9
print(l1)

l2 = [x * 8 for x in range(10, 18)]  # multiply each by 8
print(l2)

l3 = [x + 5 for x in range(3, 99, 3)] # add 5 to multiples of 3
print(l3)

l4 = [x * 2 for x in range(2, 16, 4)] # multiply selected numbers by 2
print(l4)

# Ex 8 : List is mutable → modifications allowed

# Concatenation (combine two lists)
l1 = [10, 20, 30]
l2 = [40, 50, 60]
l3 = l1 + l2               # merge lists
print(l3)

# Replication (repeat list)
l1 = [10, 20, 30]
l2 = l1 * 2                # duplicates list elements
print(l2)

# Copy (shallow copy)
l1 = [10, 20, 30]
l2 = l1.copy()             # creates separate copy
print(l2)

# extend() → adds elements of one list into another
l1 = [10, 20, 30]
l2 = [40, 50, 60]
l1.extend(l2)              # adds all from l2
print(l1)

# append() → add single element at end
l1 = [10, 20, 30]
l1.append(40)
print(l1)

# insert() → insert at specific index
l1 = ["tina", "riya"]
l1.insert(1, "siya")       # insert before index 1
print(l1)

# Ex 9 removing the data : con box
l1 = [10,20,30]
l1.remove(10)
print(l1)
# l1.remove(100)
# print(l1) # value error: list remove(x): x is not in list

# pop() → removes last element by default
l1 = ["rina", "riya", 10]
l1.pop()
print(l1)

# del keyword → delete by index or slice
l1 = [10, 20, 30, 40]

del l1[2]                  # delete index 2
print(l1)

del l1[:2]                 # delete first two elements
# del l1[0:]               # delete all elements
# del l1[:]                # delete entire list
# del l1[1:4]              # delete slice
# del l1[1:4:2]            # delete with step
print(l1)

# clear()  : removes all elements from the list
l1 = [10,20,30]
l1.clear()
print(l1)

# Ex 10 : Separating elements from nested list

l1 = [[1, 2], ["siya", "riya"], [10.5, 20.5]]
l3 = []          # will store first elements
l4 = []          # will store second elements

for x, y in l1:   # unpack each inner list
    l3.append(x)  # add first element
    l4.append(y)  # add second element

print(l3)         # [1, "siya", 10.5]
print(l4)         # [2, "riya", 20.5]

# Ex 11 : Sorting lists

l1 = [10, 20, 30, 5, 6, 1, 2]

l1.sort()                # ascending order
print(l1)

l1.sort(reverse=True)    # descending order
print(l1)

l2 = ["anu", "manu", "bunny"]

l2.sort()                # alphabetical order
print(l2)

l2.sort(reverse=True)    # reverse alphabetical
print(l2)

# l3 = [10, "anu", 10.4]
# l3.sort()              # ERROR → TypeError: cannot compare int and str

# Ex 12 : index, reverse, count, len

l1 = ["anu", "manu", "riya", "anu"]

print(l1.index("riya"))         # index of first occurrence → 2
print(l1.index("anu", 2))       # search 'anu' starting from index 2 → 3
print(l1.index("anu", 2, 4))    # search 'anu' between index 2 to 3 → 3

l1 = [10, 20, 30]
l1.reverse()                    # reverse the list
print(l1)

l1 = [10, 20, 30, 10, 10]
print(l1.count(10))             # count occurrences → 3

l1 = [10, "anu", 10.4]
print(len(l1))                  # length of list → 3

# Ex 13 : min and max

l1 = [10, 20, 30]
print(max(l1))                  # 30
print(min(l1))                  # 10

l2 = ["anu", "manu", "tanu"]
print(max(l2))                  # "tanu" → alphabetically last
print(min(l2))                  # "anu" → alphabetically first

# l3 = [10, "anu"]
# print(max(l3))
# print(min(l3))
# ERROR → TypeError: cannot compare int and str

# Ex 14 : Separating list elements based on condition

l1 = [10, 20, 30, 40, 50, 60]
l2 = []   # elements <= 30
l3 = []   # elements > 30

for x in l1:
    if x <= 30:
        l2.append(x)
    if x > 30:
        l3.append(x)

print(l2)   # [10, 20, 30]
print(l3)   # [40, 50, 60]

# TUPLE DATA TYPE: ()
# group of objects: homogeneous & heterogeneous
# insertion order preserved
# allows duplicates
# supports forward & backward indexing
# immutable

# Ex 1
t1 = (10, 20, 30)             # tuple with integers
print(t1)

t2 = (10, 20.5, "python")     # heterogeneous tuple
print(t2)

t3 = (10)                     # NOT a tuple (treated as int)
print(type(t3))
# if in tuple you want to insert only one value that value must seperated with comma(,)

t4 = (20,)                    # single-value tuple (comma required)
print(type(t4))

t5 = ()                       # empty tuple
print(t5)

t6 = tuple()                  # empty tuple using constructor
print(t6)

t7 = tuple("python")          # tuple created from iterable (string)
print(t7)

# Ex 2  :  INDEXING
#   -5  -4  -3  -2  -1
t = (10, 20, 30, 40, 50)
#    0   1   2   3   4
print(t[0])
print(t[2:4])
print(t[2:])
print(t[-2])

# Ex 3 :  UNPACKING THE DATA
t = (10, 20.5, "python")
a, b, c = t              # unpack tuple into variables
print(a, b, c)
print(type(a), type(b), type(c))

# Incorrect unpacking example
# t1 = (10, 20, 30)
# a, b = t1              # ERROR: number of variables != number of values
# print(a, b)
# ValueError: too many values to unpack

# Ex 4 : Nested tuple → a tuple inside another tuple

#        0            1
t = ((10, 20), (30, 40, 50))
#     0    1     0   1   2

print(t[0])        # prints first inner tuple (10, 20)
print(t[1])        # prints second inner tuple (30, 40, 50)
print(t[1][1])     # element at index 1 of second inner tuple → 40
print(t[0][1])     # element at index 1 of first inner tuple → 20

a, b = t           # unpack top-level tuple
print(type(a))     # both a and b are tuples
print(type(b))

x, y = a           # unpack the first inner tuple
print(type(x), type(y))   # x and y are integers

# Ex 5 : print tuple data using for loop

t = (10, 20, 30)

for x in t:              # iterate through entire tuple
    print(x)

for x in t[1:3]:         # iterate through a slice → elements at index 1 and 2
    print(x)

# for x in t[2]:
#     print(x)          # TypeError: 'int' object is not iterable
# t[2] gives 30 (an int), and integers cannot be looped through

# Ex 6 : adding multiple elements in tuple
t = tuple(x for x in range(4))
print(t)

t2 = tuple(x+2 for x in range(10))
print(t2)

# Ex 7 
# id : print memory address
# is , is not : memory comparision
# == , != : data comparision
# in , not in : data contains or not

t1 = (10,20,30)
t2 = (40,50,60)
t3 = t1

print(id(t1))
print(id(t2))
print(id(t3))

print(t1 is t2)
print(t1 is t3)
print(t1 is not t2)
print(t1 is not t3)

print(t1==t2)
print(t1==t3)

print(t1!=t2)
print(t1!=t3)

print(10 in t1)
print(100 in t1)
print(10 not in t1)
print(100 not in t1)

# Ex 8 : concat and replication
t1 = (10,20,30)
t2 = (40,50,60)
t3 = t1 + t2
print(t3)

t4 = t1 * 2
print(t4)

# Ex 9 : conversion process
# Tuples are immutable, so to modify we convert → list → tuple

t = (20, 30, 40)

l = list(t)        # convert tuple to list
l.append(50)       # modify list
print(l)

t1 = tuple(l)      # convert back to tuple
print(t1)

# Ex 10 : count(), index(), len()

t = (10, 10, 10, 20, 30, 40)

print(len(t))           # length of tuple → 6

print(t.count(10))      # count how many times 10 appears → 3

print(t.index(10))      # first occurrence of 10 → index 0

print(t.index(10, 2))   # search from index 2 → finds 10 at index 2

print(t.index(10, 1, 2))  # search between index 1 and 2 (1 included, 2 excluded) : returns index 1

# Ex 11 : sorting order
# sort()   → only for list (in-place sorting)
# sorted() → works for both list and tuple (returns a NEW sorted list)

t = (30, 1, 4, 90)

# print(t.sort())      # ERROR: tuple has no sort() method
print(sorted(t))        # ascending order → returns a list
print(sorted(t, reverse=True))   # descending order

t = (10, 5, 78, 9)

l = list(t)             # convert tuple → list
l.sort()                # sort list ascending
print(l)

l.sort(reverse=True)    # sort list descending
print(l)

t1 = tuple(l)           # convert back to tuple
print(t1)

# Ex 12 : max and min value : only for homogenous data
t1 = (10,20,30)
print(min(t1))
print(max(t1))

t2 = ("python", "data", "java" )
print(min(t2))
print(max(t2))

# t3 = (10, "python")
# print(min(t3))       # TypeError: '<' not supported between instances of 'str' and 'int'

# Ex 13 : unpacking nested tuples inside a loop

t = ((1, 2), ("tanu", "manu"), (4, 5))

l1 = []
l2 = []

for x, y in t:     # each inner tuple has 2 values → unpack into x and y
    l1.append(x)   # append first value
    l2.append(y)   # append second value

print(l1)          # [1, 'tanu', 4]
print(l2)          # [2, 'manu', 5]

# SET DATA TYPE
# Group of elements → can be homogeneous or heterogeneous
# Duplicates not allowed
# Insertion order not preserved (unordered)
# No indexing, no slicing
# Represented with { }
# Mutable → elements can be added or removed
# Stores only immutable (hashable) elements

# Ex 1: Basic Set Operations

s1 = {10, 20, 30, 40}
print(s1)              # set: unordered, so order not preserved
print(type(s1))        # <class 'set'>

s2 = {10, 10.4, "python"}
print(s2)              # heterogeneous elements allowed

s3 = {10, 20, 30, 10}
print(s3)              # duplicates removed automatically

s4 = {}
print(s4)              # empty {} creates dict
print(type(s4))        # <class 'dict'>

s5 = set()
print(s5)              # correct way to create empty set
print(type(s5))        # <class 'set'>

# Ex 2: Set can store only immutable (hashable) elements

s1 = {10, "python", (10, 20)}   # tuple is immutable → allowed
print(s1)

# s2 = {{10,20}}                # set is mutable → not allowed inside a set (unhashable)
# print(s2)

# s3 = {[10,20]}                # list is mutable → not allowed inside a set (unhashable)
# print(s3)

# Ex 3: Set is mutable → modifications allowed

s1 = {10, 20, 30}
s1.add(40)              # add() → adds a single element
print(s1)

s1.update([1, 2, 3])    # update() → adds multiple elements (expects an iterable)
print(s1)

# s1.update(100)        #  Error: int is not iterable

s2 = s1.copy()          # creates a shallow copy of the set
print(s2)

# Ex 4: Concat and Replication (Not allowed for sets)

s1 = {10, 20, 30}
s2 = {40, 50, 60}

# s3 = s1 + s2                # Sets do NOT support concatenation
# print(s3)

# Reason: concatenation may create duplicates → therefore not allowed

# s4 = s1 * 2                 # Sets do NOT support replication
# print(s4)

# Ex 5: Iterating through a set

s1 = {10, 20, 30, 40}

for x in s1:
    print(x)            # prints elements (order not guaranteed)

for x in s1:
    if x == 30:
        break           # stops loop when x is 30
    print(x)

# Ex 6 : 
# id() : to print the memory address
# is, is not : memory comparision
# == ,  != : data comparision
# in , not in : check the data available or not

s1 = {10,20,30}
s2 = {40,50,60}
s3 = s1
s4 = {10,20,30}
print(id(s1))
print(id(s2))
print(id(s3))

print(s1 is s2)
print(s1 is s3)
print(s1 is not s2)
print(s1 is not s3)

print(s1 == s2)
print(s1 == s3)
print(s1 == s4)
print(s1 != s2)
print(s1 != s4)

print(10 in s1)
print(100 in s1)
print(10 not in s1)
print(100 not in s1)

# Ex 7
a = set("python")
print(a)
b = set("pythonpro")
print(b)

print(b-a)   # Difference: characters present in b but not in a
print(a|b)   # Union: all unique characters from both sets
print(a&b)   # Intersection: common characters in both sets
print(a^b)   # Symmetric Difference: characters in either set but not in both

basket1 = {'orange', 'apple', 'banana', 'pear'}
basket2 = {'pear', 'orange', 'banana'}

print(basket1-basket2)  # Difference: items in basket1 but not in basket2
print(basket1|basket2)  # Union: all unique items from both baskets
print(basket1&basket2)  # Intersection: common items in both baskets
print(basket1^basket2)  # Symmetric Difference: items in either basket but not in both

# Ex 8 
s1 = {x for x in range(10)}
print(s1)

s2 = {x*5 for x in range(3,10,4)}
print(s2)

s3 = {x+99 for x in range(10,20)}
print(s3)

# Ex 9 : set is mutable – removing data from a set
# remove()  -> removes a specific element, raises KeyError if not found
# pop()     -> removes and returns a random element
# discard() -> removes a specific element, no error if not found
# clear()   -> removes all elements from the set

s1 = {10, 20, 30}
s1.remove(10)      # removes 10 from the set
# s1.remove(100)   # KeyError because 100 is not in the set
print(s1)


s1 = {10,20,30}
s1.pop()   # removes one random element
print(s1)

s1 = {10,20,30}
s1.discard(10)  # removes 10 from the set
s1.discard(100)    # does nothing, no error
print(s1)

s2 = {10,20,30}
s2.clear()  # clear() removes all elements from the set and makes it empty
print(s2)