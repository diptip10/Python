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

# Ex 10 : conversion process – list to set and set to list

l1 = [10, 20, 30, 10, 20, 40, 10, 20]
s = set(l1)          # converts list to set (removes duplicates)
print(s)

newlist = list(s)    # converts set back to list
print(newlist)

# Ex 11: Unpacking set data
s1 = {10, 20.5, 'python'}

# Unpacking set elements into variables (order is not guaranteed)
a, b, c = s1

# Print the data types of unpacked values
print(type(a), type(b), type(c))

s2 = {10, 20, 30}

# Unpacking error example:
# a, b = s2  
# ValueError: too many values to unpack (expected 2)

# Ex 12: Sorting a set (only homogeneous data types)
s1 = {10, 3, 24, 1, 30}

print(sorted(s1))   # Sort set in ascending order (returns a list)

print(sorted(s1, reverse=True))   # Sort set in descending order

print(len(s1))  # Length of the set (number of elements)

# Ex 13: Finding minimum and maximum values in sets

# Set with integers
s1 = {10, 20, 30}
print(min(s1))   # Smallest number
print(max(s1))   # Largest number

# Set with strings (lexicographical order)
s2 = {"python", "language", "java"}
print(min(s2))   # Alphabetically smallest string
print(max(s2))   # Alphabetically largest string

s3 = {10, "python"}   # Set with mixed data types
# print(min(s3))
# print(max(s3))  # TypeError: '<' not supported between instances of 'str' and 'int'

# DICTIONARY DATA TYPE
# It is used to store data in the form of key : value pairs (called items)
# Syntax: {key: value, key: value}
# Keys   → must be unique
# Values → can be duplicate
# Mutable → allows modification (add, update, delete items)

# Ex 1 : Dictionary basics and operations

# creating a dictionary
d1 = {111: "dipti", 222: "riya", 333: "siya"}
print(d1)            # prints dictionary
print(type(d1))      # <class 'dict'>

# duplicate keys are not allowed
# old value is replaced by the new value
d2 = {1: "Dipti", 2: "Pratiksha", 1: "Surabhi"}
print(d2)            # key 1 holds "Surabhi"

# creating an empty dictionary
d3 = {}
print(d3)
print(type(d3))      # <class 'dict'>

# inserting data into an empty dictionary
d3[11] = "Dipti"
d3[22] = "pratiksha"
print(d3)

# Ex 2
# accessing dictionary methods
d1 = {111: "dipti", 222: "swaraj", 333: "Ajinkya"}

print(d1.keys())     # returns all keys
print(d1.values())   # returns all values
print(d1.items())    # returns key-value pairs

# converting keys, values, items to list
print(list(d1.keys()))
print(list(d1.values()))
print(list(d1.items()))

# converting keys, values, items to tuple
print(tuple(d1.keys()))
print(tuple(d1.values()))
print(tuple(d1.items()))

# converting keys, values, items to set
print(set(d1.keys()))
print(set(d1.values()))
print(set(d1.items()))

# Ex 3 : printing dictionary data using for loop

d1 = {111: "dipti", 222: "swaraj", 333: "ajinkya"}

# prints only keys
for x in d1:
    print(x)

# prints keys with their values
for x in d1:
    print(x, d1[x])

# prints keys and values using items()
for x, y in d1.items():
    print(x, y)

# Ex 4 : Dictionary keys must be immutable
# Allowed key types: int, float, string, tuple
# Not allowed: list, set, dict (mutable types)

# d1 = {[1,2]:"dipti", 222:"swaraj", 333:"supriya"}
# TypeError: unhashable type: 'list' (list cannot be a key)

d1 = {111: [1, 2, 3], 222: "dipti", 333: "ajinkya"}
# Values can be mutable (like list)
print(d1)

# Ex 5 : reading data from dictionary
# Access data using keys and get() method

d1 = {111: "nikita", 222: "surabhi", 333: "pratiksha"}

# accessing values using keys
print(d1[111])
print(d1[222])
print(d1[333])
# print(d1[1])   # KeyError if key does not exist

# accessing values using get()
print(d1.get(111))
print(d1.get(222))
print(d1.get(333))
# print(d1.get(1))  # returns None (no KeyError)

# Ex 6 : Dictionary operators and functions
# id()        -> returns memory address of an object
# is / is not -> compares memory location (identity comparison)
# in / not in -> checks key availability in dictionary
# == / !=     -> compares data (both keys and values)

d1 = {111: "dipti", 222: "anu"}
d2 = {333: "riya", 444: "siya"}
d3 = d1
d4 = {111: "dipri", 222: "anu"}

# memory addresses
print(id(d1))
print(id(d2))
print(id(d3))
print(id(d4))

# identity comparison
print(d1 is d2)       # False (different objects)
print(d1 is d3)       # True (same reference)
print(d1 is d4)       # False
print(d1 is not d2)   # True
print(d1 is not d3)   # False

# data comparison
print(d1 == d2)       # False
print(d1 == d3)       # True
print(d1 == d4)       # False (value mismatch)
print(d1 != d2)       # True
print(d1 != d4)       # True

# key membership check
print(111 in d1)      # True
print(11 in d1)       # False
print(111 not in d1)  # False
print(11 not in d1)   # True

# Ex 7 : Creating dictionary using zip()

# list to dictionary
l1 = [1, 2, 3, 4]
l2 = ["dipti", "nikita", "pratiksha", "surabhi"]
x = zip(l1, l2)    # combine two lists into a dictionary
d = dict(x)
print(d)

# tuple to dictionary
t1 = (1, 2, 3, 4)
t2 = ("dipti", "pratiksha", "surabhi", "nikita")
x = zip(t1, t2)   # combine two tuples into a dictionary
d = dict(x)
print(d)

# set to dictionary (order may vary because sets are unordered)
s1 = {1, 2, 3, 4}
s2 = {"dipti", "pratiksha", "surabhi", "nikita"}
x = zip(s1, s2)     # combine two sets into a dictionary
d = dict(x)
print(d)

# swapping keys and values using zip
# In zip() the first iterable always provides the KEYS and the second iterable provides
#  the VALUES when you convert it to a dictionary.
t2 = (1, 2, 3, 4)
t1 = ("dipti", "pratiksha", "surabhi", "nikita")
x = zip(t1, t2)   # create dictionary by swapping
d = dict(x)
print(d)

# Ex 8 : Dictionary unpacking

# When unpacking a dictionary with multiple variables,
# only KEYS are unpacked (not values)

d1 = {1: "aaa", 2: "bbb", 3: "ccc"}
a, b, c = d1        # unpacking keys
print(a, b, c)

# If only one variable is used,
# the entire dictionary is assigned to that variable

d2 = {1: "aaa"}
a = d2
print(a)

# Ex 9 : Dictionary - modifications allowed

d1 = {1: "aaa", 2: "bbb", 3: "ccc"}
print(len(d1))         # number of items in dictionary

print(d1.popitem())    # removes and returns last inserted key-value pair
print(d1.pop(2))       # removes key 2 and returns its value
# print(d1.pop(222))   # KeyError if key not found

print(d1)              # remaining dictionary

d1.clear()             # removes all items
print(d1)              # empty dictionary

# Ex 10 : Merging dictionaries

d1 = {1: "aaa", 2: "bbb"}
d2 = {3: "ccc", 4: "ddd"}

# Method 1: update() - adds d2 items into d1
d1.update(d2)
print(d1)

# Method 2: dictionary unpacking (**)
d1 = {1: "aaa", 2: "bbb"}
d2 = {3: "ccc", 4: "ddd"}

# d3 = d1 + d2   # TypeError, cannot use + with dicts
# The ** operator in Python is used for dictionary unpacking. In the context of dictionaries, 
# it allows you to merge dictionaries or pass dictionary items as keyword arguments.
x = {**d1, **d2}   # merges d1 and d2 into new dictionary
print(x)

# Ex 11: Sorting operations on dictionary

d1 = {1:"aaa", 2:"bbb", 3:"ccc", 4:"ddd"}

# Sort dictionary keys in ascending order
print(sorted(d1.keys()))

# Sort dictionary keys in descending order
print(sorted(d1.keys(), reverse=True))

# Sort dictionary values in ascending (alphabetical) order
print(sorted(d1.values()))

# Loop through dictionary using sorted keys
for key in sorted(d1.keys()):
    print("key=%d value=%s" % (key, d1[key]))

# Ex 12: Dictionary value update

d1 = {1: None, 2: "aaa", 3: "bbb", 4: "ccc"}
print(d1)   # Print original dictionary

d1[1] = "ddd"   # Update value of key 1 from None to "ddd"
print(d1)   # Print updated dictionary

# Ex 13: min() and max() on dictionary keys
d1 = {1: "aaa", 2: "bbb", 3: "ccc", 4: "ddd"}

# min() and max() return smallest and largest KEY (numeric comparison)
print(min(d1))   # 1
print(max(d1))   # 4

d2 = {"aa": "dipti", "bb": "swaraj"}

# min() and max() return smallest and largest KEY (alphabetical order)
print(min(d2))   # "aa"
print(max(d2))   # "bb"

# Mixed key types (int and str)
# Python cannot compare different data types
# d3 = {111: "dipti", "aa": "pawar"}
# print(min(d3))   # TypeError
# print(max(d3))   # TypeError


# LAMBDA, FILTER, MAP, REDUCE
# A lambda function is an anonymous function in Python used to write small, one-line expressions.
# It helps reduce code length and is commonly used with filter(), map(), and reduce().

# Ex 1
# Normal function with one argument
def m1(x):
    print(2 * x)

m1(3)

# Same operation using lambda function
a = lambda x: x * 2
print(a(3))

# Ex 2: Lambda with two arguments
# Normal function with two arguments
def m1(x, y):
    print(x * y)

m1(2, 3)

# Same logic using lambda function
b = lambda x, y: x * y
print(b(2, 3))

# Ex 3: filter() function

# filter() is used to filter elements from an iterable based on a condition.
# It returns only those elements for which the function returns True.

# List of numbers
l1 = [2, 3, 4, 5]

# Function to check even numbers
def m1(x):
    if x % 2 == 0:
        return True
    else:
        return False

# Filter even numbers using normal function
print(list(filter(m1, l1)))

# Filter even numbers using lambda function
print(list(filter(lambda x: x % 2 == 0, l1)))

# Convert filtered result into tuple
print(tuple(filter(lambda x: x % 2 == 0, l1)))

# ---------------------------------------
### other ways of filtering even numbers from the given list
#1. Using List Comprehension (Most Common)
even_no = [x for x in l1 if x%2 == 0]
print(even_no)

# 2. Using for loop
even_num = [] 
for x in l1:
    if x%2 == 0:
        print(even_num.append(x))

print(even_num)

# 3. Using set comprehension : use when unique values are required
even_num = {x for x in l1 if x%2==0}
print(even_num)

# 4. Using generator expression
even_nums = (x for x in l1 if x % 2 == 0)
print(list(even_nums))

# using while loop
# Rarely used, but good for logic understanding
l=[1,2,3,4]
i = 0
even_nums = []
while i < len(l):
    if l[i]%2 == 0 :
        even_nums.append(l[i])
    i=i+1

print(even_nums)
# -----------------------------------------------------------

# Ex 4: filter() with string values

# List containing duplicate strings
l1 = ["aaa", "bbb", "aaa", "ddd"]

# Function to check specific value
def m1(x):
    if x == "aaa":
        return True
    else:
        return False

# Filter values equal to "aaa" using normal function
print(list(filter(m1, l1)))

# Filter values equal to "aaa" using lambda function
print(list(filter(lambda x: x == "aaa", l1)))

# Convert filtered result into tuple
print(tuple(filter(lambda x: x == "aaa", l1)))

# Store filtered result in a list
l2 = list(filter(lambda x: x == "aaa", l1))
print(l2)

# Ex 5
# map() is used to apply a function to every element of an iterable and return the result.
# map() is used to perform operations on every element of the list

l1 = [2, 45, 6, 3, 7]

# Function to double each element
def m1(x):
    return x * 2

# Using map() with normal function
print(list(map(m1, l1)))

# Using map() with lambda function
print(list(map(lambda x: x * 2, l1)))

# Ex 6: map() with string values

# List of strings
l1 = ["dipti", "nikita", "surabhi", "pratiksha"]

# Function to append "world" to each string
def m1(x):
    return x + "world"

# Using map() with normal function
print(list(map(m1, l1)))

# Using map() with lambda function
print(list(map(lambda x: x + "world", l1)))

# Convert mapped result into tuple
print(tuple(map(lambda x: x + "world", l1)))

# Ex 7: map() with multiple iterables
l1 = [1, 2, 3, 4]
l2 = [10, 20, 30, 40]
l3 = [100, 200, 300, 400]

# Add elements of l1 and l2 (index-wise)
print(list(map(lambda x, y: x + y, l1, l2)))

# Add elements of l1, l2, and l3 (index-wise)
print(list(map(lambda x, y, z: x + y + z, l1, l2, l3)))

# Ex 8: map() to find length of each word

# Input string
s = "hi bunny how are you"

# Split string into words
words = s.split()

# Print each word
for x in words:
    print(x)

# Find length of each word using map()
print(list(map(lambda x: len(x), words)))

# Ex 9: reduce() function
# reduce() is used to perform computation on all elements and return a single value

from functools import reduce

l1 = [25, 34, 54, 23]

# Sum using for loop
total = 0
for x in l1:
    total = total + x
print(total)

# Sum using reduce() with lambda
print(reduce(lambda x, y: x + y, l1))


# Addition (sum) of numbers from 1 to 100 using reduce()

from functools import reduce

# range(1, 100) adds numbers from 1 to 99
print(reduce(lambda x, y: x + y, range(1, 100)))

# If you want sum from 1 to 100 (inclusive)
print(reduce(lambda x, y: x + y, range(1, 101)))

# CLASS CONCEPT
# Class is a logical entity and blueprint for object creation
# Object is a physical entity and occupies memory
# Multiple objects can be created from a single class
# In Python 3.x, all classes implicitly inherit from object

# Ex 1: Checking whether classes are subclasses of object

class myclass1:
    pass        # class without explicitly mentioning parent

class myclass2():
    pass        # class with empty parentheses

class myclass3(object):
    pass        # class explicitly inheriting from object

# issubclass() checks whether a class is derived from another class
print(issubclass(myclass1, object))   # True → default inheritance in Python 3
print(issubclass(myclass2, object))   # True → default inheritance in Python 3
print(issubclass(myclass3, object))   # True → explicit inheritance

# Ex 2
# Class is a logical entity
# Functions defined inside a class are called methods

class myclass:
    
    def disp1(self):                   # self refers to the current object
        print("good morning")
    
    def disp2(self, name):             # name is a parameter passed to the method
        print("good evening :", name)

# Creating object of the class
c = myclass()

# Calling methods using object reference
c.disp1()              # calls disp1()
c.disp2("dipti")       # calls disp2() with argument

# Ex 3: Instance method and Static method

class myclass():
    
    def m1(self):                 # Instance method; self refers to current object
        print("instance method")
    
    @staticmethod                # Static method
    def m2():                     # Does not use self or class data
        print("static method")

c = myclass()                     # Creating object of the class

c.m1()                            # Calling instance method using object
c.m2()                            # Calling static method using object

# Example: Instance method and Static method behavior
class myclass():

    def m1(self):
        # Instance method: self refers to the current object
        print("instance method")

    @staticmethod
    def m2(self):
        # Static method: 'self' here is just a normal parameter
        # No object reference is passed automatically
        print("static method")

# Creating an object of the class
c = myclass()

# Calling instance method (object is passed automatically as self)
c.m1()

# Calling static method (argument is passed manually)
myclass.m2("dipti")
#---------------------
# A function declared outside a class is called a function
def greet():
    print("Hello")

# A function declared inside a class is called a method
# Functionality may be same, but calling style is different
class Demo:
    def greet(self):
        print("Hello")
#-----------------------

# Ex 4: Declaring variables inside the class
# Variables declared inside the class and outside methods are called class variables
# Inside methods, class variables can be accessed using self or class name
# Outside the class, class variables should be accessed using the class name

class MyClass:

    a, b = 10, 20          # Class variables

    def add(self):
        # Accessing class variables using self
        print(self.a + self.b)

    def mul(self):
        # Accessing class variables using self
        print(self.a * self.b)


# Creating object of the class
c = MyClass()

# Calling methods using object
c.add()   
c.mul()

# Ex 5: Local variables, Class variables, and Global variables (different names)

i, j = 100, 200   # Global variables (accessible everywhere in the program)

class MyClass:
    a, b = 10, 20   # Class variables (shared by all objects of the class)

    def add(self, x, y):     # x, y → Local variables (method scope)
        print(x + y)              # using local variables
        print(self.a + self.b)    # Accessing class variables
        print(i + j)               # Accessing global variables

    def mul(self, x, y):       # x, y → Local variables (method scope)
        print(x * y)              # using local variables
        print(self.a * self.b)       # Accessing class variables
        print(i * j)              # Accessing global variables


# Creating object of the class
c = MyClass()

# Calling methods with arguments
c.add(2, 3)
c.mul(3, 4)

# Ex 6: Local, Class, and Global variables with SAME names

a, b = 100, 200          # Global variables

class MyClass:

    a, b = 10, 20        # Class variables

    def add(self, a, b):               # a, b → Local variables (method parameters)
        print(a + b)                     # using local variables
        print(self.a + self.b)        # Accessing class variables
        print(globals()['a'] + globals()['b'])    # Accessing global variables using globals()

    def mul(self, a, b):       # a, b → Local variables (method parameters)
        print(a * b)                     # using local variables
        print(self.a * self.b)         # Accessing class variables
        print(globals()['a'] * globals()['b'])      # Accessing global variables using globals()


c = MyClass()    # Creating object of the class

# Calling methods
c.add(3, 2)
c.mul(3, 4)

# Ex 7 : For a single class, we can create multiple objects

# Defining a class
class MyClass:
    def disp(self):              # Instance method
        print("Good Morning")    # This method prints a message

c1 = MyClass()     # Creating first object of MyClass
c1.disp()          # Calling method using first object

c2 = MyClass()    # Creating second object of MyClass
c2.disp()         # Calling method using second object

# Ex 8 : We can create objects in two ways
# 1. Named object: Stored in a variable and can be reused.
# 2. Nameless object: Not stored in a variable, used for one-time method call.
#  Nameless objects are commonly used when the object is not needed again.

# Defining a class
class MyClass:
    def disp(self):         # Instance method
        print("Good Morning")       # This method prints a message

c1 = MyClass()   # 1. Creating a named object
c1.disp()       # Calling method using named object

MyClass().disp() #Creating a nameless(anonymous)object Object is created and method is called immediately

# Ex 9 : Printing memory address using id()
# is / is not operators are used for memory comparison

# Defining an empty class
class MyClass:
    pass


# Creating objects
c1 = MyClass()   # First object
c2 = MyClass()   # Second object (different memory)
c3 = c1          # c3 refers to the same object as c1


# Printing memory addresses
print(id(c1))    # Memory address of c1
print(id(c2))    # Memory address of c2
print(id(c3))    # Memory address of c3 (same as c1)


# Memory comparison using 'is' operator
print(c1 is c2)      # False → different objects (different memory)
print(c1 is c3)      # True  → both refer to same object


# Memory comparison using 'is not' operator
print(c1 is not c2)  # True  → different memory locations
print(c1 is not c3)  # False → same memory location

# Ex 10
# One object modifying a variable will affect only that object
# The change will NOT reflect in another object
# For every object, a separate instance-level copy can be created

# Defining a class
class MyClass:
    name = "dipti"     # Class variable

# Creating first object
c1 = MyClass()
print(c1.name)    # Accessing class variable using object    # Output: dipti
# Modifying variable using c1
c1.name = "siya"    # This creates an INSTANCE variable for c1 only

c2 = MyClass() # Creating second object
# Accessing name using c2
print(c2.name)   # c2 still refers to the class variable     # Output: dipti

# ---------------------
# PYTHON CLASS CONCEPT
# ---------------------
# Main Difference between Constructor and Method:
#
# 1. Constructor (__init__):
#    - Executed automatically when an object is created
#    - Used to initialize object data
#
# 2. Method:
#    - Executed only when it is explicitly called using the object
# ---------------------

# Example 1: Declaring a constructor inside a class

class MyClass:
    
    # Constructor (no-argument constructor)
    def __init__(self):
        print("Zero-argument constructor called")
    
    # Normal method
    def m1(self):
        print("Good morning")


# Object creation
c = MyClass()      # Constructor is called automatically

# Method call
c.m1()             # Method is called using the object


# Ex 2: Local Variable and Class (Instance) Variable
# Local Variables:
# - Declared inside a method
# - Can be used only within that method
#
# Class (Instance) Variables:
# - Created using self
# - Can be accessed by all methods of the class

class MyClass:
    
    def values(self, val1, val2):
        # val1 and val2 are local variables
        print(val1)
        print(val2)

        # Converting local variables into instance variables
        self.val1 = val1
        self.val2 = val2

    def add(self):
        # Accessing instance variables
        print(self.val1 + self.val2)
    
    def mul(self):
        # Accessing instance variables
        print(self.val1 * self.val2)


# Object creation
c = MyClass()

# Calling methods
c.values(2, 3)
c.add()
c.mul()

# Ex 3: Calling methods using self

# - A method of a class can call another method of the same class
#   using the 'self' keyword.
# - 'self' represents the current object.

class MyClass:
    
    def m1(self):
        print("m1 method")
        self.m2(10)            # Calling another method of the same class using self
    
    def m2(self, a):
        print("m2 method:", a)

c = MyClass()    # Object creation
c.m1()         # Calling m1() method

# ---------------------
# Ex 4: Constructor with Argument
# ---------------------
# - A constructor can accept arguments
# - Local variables are passed as parameters to the constructor
# - Class variables are accessed using 'self'
# - Constructor is executed automatically when an object is created

class MyClass:
    
    name = "Dipti"      # Class variable

    def __init__(self, name):   # Constructor with argument (local variable)
        print("Good morning:", name)        # Printing local variable
        print("Good evening:", self.name)   # Accessing class variable using self


# Object creation
# While creating the object, argument must be passed
# Constructor is executed automatically
c = MyClass("Swaraj")

# ---------------------
# Ex 5: Conversion of Local Variables to Instance Variables
# ---------------------
# - Constructor parameters are local variables
# - Using 'self', local variables can be converted into instance variables
# - Instance variables can be accessed by all methods of the class

class Operations:
    
    def __init__(self, val1, val2):      # val1 and val2 are local variables
        print(val1)
        print(val2)

        # Converting local variables into instance variables
        self.val1 = val1
        self.val2 = val2

    def add(self):
        print(self.val1 + self.val2)    # Accessing instance variables

    def mul(self):
        print(self.val1 * self.val2)     # Accessing instance variables


# Object creation
o = Operations(3, 4)   # Constructor is executed automatically

# Method calls
o.add()
o.mul()

# ---------------------
# Ex 6: Employee Class Example
# ---------------------
# - Constructor initializes employee details
# - Local variables are converted into instance variables using 'self'
# - Data is displayed using different string formatting techniques

class Employee:
    
    def __init__(self, eid, ename, esal):
        # Constructor parameters are local variables
        # Converting local variables into instance variables
        self.eid = eid
        self.ename = ename
        self.esal = esal

    def display(self):
        # Display using format() method
        print("eid:{} ename:{} esal:{}".format(self.eid, self.ename, self.esal))
        
        # Display using % formatting
        print("eid: %d ename: %s esal: %g" % (self.eid, self.ename, self.esal))


# Object creation
e = Employee(111, "Dipti", 20000)

# Method call
e.display()

# ---------------------
# Ex 7: __str__() Method in Python
# ---------------------
# __str__() is executed automatically when we print
# the reference variable of an object.
#
# - __str__() must always return a STRING



# Case 1: No __str__() method
# Output will be the object's memory address
class MyClass:
    pass

c = MyClass()
print(c)


# Case 2: __str__() returns a string
class MyClass:
    def __str__(self):
        return "python"

c = MyClass()
print(c)


# Case 3: __str__() returns a non-string (int)
# This will raise a TypeError
class MyClass:
    def __str__(self):
        return 10      #  Invalid return type

# c = MyClass()
# print(c)


# Case 4: __str__() does not return anything
# This will raise a TypeError because return value is None
class MyClass:
    def __str__(self):
        print("Dipti")     #  No return statement

# c = MyClass()
# print(c)

# Ex 8
# ---------------------
# Example: Using __str__() in Employee Class
# ---------------------
# - __str__() is used to define a user-friendly
#   string representation of an object
# - It is executed automatically when we print
#   the reference variable

class Employee:
    
    def __init__(self, eid, ename, esal):      # Constructor parameters are local variables
        # Converting local variables into instance variables
        self.eid = eid
        self.ename = ename
        self.esal = esal

    def __str__(self):
        # Must return a string
        return "eid:{} ename:{} esal:{}".format(self.eid, self.ename, self.esal)


# Object creation
e1 = Employee(111, "Dipti", 20000)
print(e1)   # Calls __str__() automatically

e2 = Employee(222, "Nikita", 30000)
print(e2)   # Calls __str__() automatically

# ---------------------
# Special Methods in Python
# ---------------------
# - Constructor (__init__):
#   Executed automatically during object creation.
#
# - __str__():
#   Executed when we print the reference variable of an object.
#   It must return a string.
#
# - __del__():
#   Executed automatically when an object is destroyed.
#   Used for cleanup activities.
# ---------------------

# Ex 9: __del__() Method (Destructor)
# - __del__() is executed automatically when an object is destroyed
# - Used to release resources such as memory, files, or database connections

class MyClass:
    
    def __del__(self):
        print("Object destroyed...")


# Object creation
c1 = MyClass()
c2 = MyClass()

# Destroying objects explicitly
del c1
del c2

# Ex 10: Multiple Reference Variables for the Same Object

# - An object can have multiple reference variables
# - __del__() is executed only when the reference count becomes ZERO

class MyClass:
    
    def __del__(self):
        print("Object destroyed...")


# Object creation
c1 = MyClass()

# Multiple references pointing to the same object
c2 = c1
c3 = c1

# Deleting references
del c1   # Object NOT destroyed (still referenced by c2 and c3)
del c2   # Object NOT destroyed (still referenced by c3)
del c3   # Reference count becomes zero → __del__() executed

# Case 1: Exception inside __del__() method
# - If an exception occurs inside __del__(),
#   Python does NOT propagate the exception
# - Instead, it prints: "Exception ignored in: <function __del__>"

class MyClass:
    
    def __del__(self):
        print("Object destroyed...")
        
        # Exception inside destructor
        print(10 / 0)   # ZeroDivisionError (ignored)


# Object creation
c1 = MyClass()

# Destroying object
del c1

# OOPS
# Class (Logical Entity) vs Object (Physical Entity)

# Class
# A class is a logical entity (blueprint) used to create objects.
# It does not occupy memory.

# Object
# An object is a physical entity (instance of a class).
# It occupies memory.

# Example 1
# case 1: Python 3.x
# In Python 3.x, every class is by default a child of 'object'

class MyClass1:
    pass

class MyClass2:
    pass

class MyClass3(object):
    pass

# issubclass() checks whether a class is derived from another class
print(issubclass(MyClass1, object))   # True
print(issubclass(MyClass2, object))   # True
print(issubclass(MyClass3, object))   # True

# case 2: Python 2.7
# In Python 2.7, a class is NOT a child of 'object' by default
# unless it explicitly inherits from 'object'

## ============================================================
# 4 BUILDING BLOCKS OF OOPS
# ============================================================
# 1. Inheritance
# 2. Polymorphism
# 3. Encapsulation
# 4. Abstraction


# 1. Inheritance

# Inheritance is the process of creating a new class
# by using the properties of an existing class.
#
# OR
#
# The process of acquiring the properties from one class
# to another class is called inheritance.

# Example 2 – Single Inheritance

class Parent:
    def m1(self):
        print("Parent m1 method")


class Child(Parent):
    def m2(self):
        print("Child m2 method")


# Creating object of Parent class
p = Parent()
p.m1()

# Creating object of Child class (recommended)
c = Child()
c.m1()   # accessing Parent class method
c.m2()   # accessing Child class method

# Note:
# Child class object creation is recommended because
# using a child class reference, we can access both
# parent and child class properties.

# Ex 3: Calling Parent Class Method using super()

# super() is used to call the methods of the parent (super) class
# from the child class.
#
# Requirement:
# While executing the child class method (m2),
# call the parent class method (m1).

class Parent:
    def m1(self):      # Parent class method
        print("Parent m1 method")


class Child(Parent):
    def m2(self):
        super().m1()        # Calling parent class method using super()
        
        print("Child m2 method")       # Child class method


# Creating object of Child class
# Child class object is recommended because it can access
# both parent and child class methods
c = Child()
c.m2()


# Ex 4 : Super Class Variables

# Variable declaration in Parent and Child classes
#
# Rule:
# When we access variables using 'self',
# Python first checks the Child class.
# If the variable is not found in the Child class,
# it then checks the Parent class.

class Parent:
    a, b = 10, 20      # Parent class variables


class Child(Parent):
    x, y = 100, 200        # Child class variables

    def add(self, i, j):   # Local variables
        print(i + j)
        print(self.x + self.y)      # Accessing Child class variables using self

        # Accessing Parent class variables using self
        # (not found in child, so taken from parent)
        print(self.a + self.b)


# Creating object of Child class
c = Child()
c.add(1000, 2000)

# Example 5: Variables with the same names in Parent and Child classes

# Case 1: Accessing variables using self

class Parent:
    # Class variables of Parent
    a, b = 10, 20


class Child(Parent):
    # Class variables of Child (same names as Parent)
    a, b = 100, 200

    def add(self, a, b):
        # Local variables (method parameters)
        print(a + b)              # Uses local variables → 1000 + 2000 = 3000

        # Accessing class variables using self
        # Priority:
        # 1. Child class variables
        # 2. Parent class variables (if not found in Child)
        print(self.a + self.b)    # Uses Child.a and Child.b → 100 + 200 = 300

        # Repeated to show consistent behavior
        print(self.a + self.b)


# Object creation
c = Child()
c.add(1000, 2000)

# Case 2: Accessing Parent class variables using super()

class Parent:
    # Class variables of Parent
    a, b = 10, 20


class Child(Parent):
    # Class variables of Child
    a, b = 100, 200

    def add(self, a, b):
        # Local variables
        print(a + b)               # 1000 + 2000 = 3000

        # Accessing Child class variables using self
        print(self.a + self.b)     # 100 + 200 = 300

        # Accessing Parent class variables using super()
        print(super().a + super().b)  # 10 + 20 = 30


# Object creation
c = Child()
c.add(1000, 2000)

# Case 3: Local, Child, Parent, and Global variables

a, b = 1, 2   # Global variables

class Parent:
    a, b = 10, 20  # Parent class variables

class Child(Parent):
    a, b = 100, 200  # Child class variables

    def add(self, a, b):
        print(a + b)                       # Local variables
        print(self.a + self.b)             # Child class variables
        print(super().a + super().b)       # Parent class variables
        print(globals()['a'] + globals()['b'])  # Global variables

c = Child()
c.add(1000, 2000)

# Ex 6
# Case 1:
# If the child class does not have its own constructor,
# the parent class constructor is executed automatically.

class Parent:
    def __init__(self):
        print("Parent class constructor")


class Child(Parent):
    pass


c = Child()


# Case 2:
# If the child class defines its own constructor,
# the parent constructor is NOT executed automatically.

class Parent:
    def __init__(self):
        print("Parent class constructor")


class Child(Parent):
    def __init__(self):
        print("Child class constructor")


c = Child()


# case3 : while executing child class we want to call parent class cons
# to call the parent class cons super() keyword is required

class parent():
    def __init__(self,name):
        print("parent class cons: ", name)

class child(parent):
    def __init__(self):
        super().__init__("dipti")
        print("child class cons")

c = child()

# Case 4:
# Parent constructor can also be called using the class name.
# When using the class name, 'self' must be passed explicitly.

class Parent:
    def __init__(self, name):
        print("Parent class constructor:", name)


class Child(Parent):
    def __init__(self):
        super().__init__("Dipti")          # Using super()
        Parent.__init__(self, "Anu")       # Using class name
        print("Child class constructor")


c = Child()

# TYPES OF INHERITANCE
# 1. single : one parent class contains one child class
# 2. multilevel
# 3. multiple
# 4. hierarchical
# 5. hybrid

## -- 1. single inheritance : One child class inherits from one parent class.
class Parent:
    def show(self):
        print("Parent class method")

class Child(Parent):  # Child inherits Parent
    pass

c = Child()
c.show()
# Ex
# Parent class
class Parent:
    def show_parent(self):
        print("This is parent class method")

# Child class inheriting Parent
class Child(Parent):
    def show_child(self):
        print("This is child class method")

# Creating object of Child class
c = Child()

# Child can access both parent and child methods
c.show_parent()   # inherited from Parent
c.show_child()    # own method


## -- 2. multilevel inheritace : A child class inherits from a parent class,
#  and another child inherits from that child.
class A:
    pass
class B(A):
    pass
class c(B):
    pass
# Ex
# Grandparent class
class GrandParent:
    def gp_method(self):
        print("Grandparent class method")

# Parent class inherits GrandParent
class Parent(GrandParent):
    def p_method(self):
        print("Parent class method")

# Child class inherits Parent
class Child(Parent):
    def c_method(self):
        print("Child class method")

# Creating object of Child class
c = Child()

# Child can access all methods
c.gp_method()   # from GrandParent
c.p_method()    # from Parent
c.c_method()    # from Child


##  -- 3. Multiple Inheritance
# A child class inherits from more than one parent class
class A:
    pass
class B:
    pass
class C(A,B):
    pass

# Ex

class A:
    def method_a(self):
        print("Method from class A")

class B:
    def method_b(self):
        print("Method from class B")

# Child class inherits from both A and B
class C(A, B):
    pass

# Creating object of child class
obj = C()

# Child can access methods of both parent classes
obj.method_a()
obj.method_b()

## 4. hierarchial inheritance : one parent contains multiple child
class A:
    pass
class B(A):
    pass
class C(A):
    pass

# Ex
class A:
    def show_parent(self):
        print("This is parent class method")

# Child class B inherits from A
class B(A):
    def show_b(self):
        print("This is B class method")

# Child class C inherits from A
class C(A):
    def show_c(self):
        print("This is C class method")

# Creating objects
b = B()
c = C()

# Accessing parent and child methods
b.show_parent()  # inherited from A
b.show_b()       # own method

c.show_parent()  # inherited from A
c.show_c()       # own method
## -- 4. Hybrid Inheritance
# Combination of multiple and hierarchical inheritance

# Base class
class A:
    def show_a(self):
        print("Method from class A")

# Parent class B inherits A
class B(A):
    def show_b(self):
        print("Method from class B")

# Parent class C inherits A
class C(A):
    def show_c(self):
        print("Method from class C")

# Child class D inherits from B and C (multiple inheritance)
class D(B, C):
    def show_d(self):
        print("Method from class D")

# Creating object of D
d = D()

# Accessing methods from all parent classes
d.show_a()   # from A
d.show_b()   # from B
d.show_c()   # from C
d.show_d()   # own method

# Ex 7
# Multilevel Inheritance
# A → B → C

class A:
    def m1(self):
        print("m1 method")   # method of class A

class B(A):
    def m2(self):
        print("m2 method")   # method of class B

class C(B):
    def m3(self):
        print("m3 method")   # method of class C

# Creating object of class C
c = C()

# Accessing methods from all levels
c.m1()   # inherited from class A
c.m2()   # inherited from class B
c.m3()   # own method

# Ex 8 : Hierarchical Inheritance
# One parent class (vehicle) with multiple child classes (car, plane)

class vehicle:
    def disp1(self):
        print("vehicle info")   # parent class method

class car(vehicle):
    def disp2(self):
        print("car info")       # child class method

class plane(vehicle):
    def disp3(self):
        print("plane info")     # child class method

# Creating objects
v = vehicle()
v.disp1()     # access parent method

c = car()
c.disp1()     # inherited from vehicle
c.disp2()     # own method

p = plane()
p.disp1()     # inherited from vehicle
p.disp3()     # own method

# Ex 9 : Multiple Inheritance
# Child class inherits from multiple parent classes

class Parent1:
    def m1(self):
        print("parent1 m1 method")   # method of Parent1

class Parent2:
    def m2(self):
        print("parent2 m2 method")   # method of Parent2

# Child class inherits from Parent1 and Parent2
class Child(Parent1, Parent2):
    def m3(self):
        print("child m3 method")     # child class method

# Creating object of Child
c = Child()

# Accessing methods from all classes
c.m1()   # inherited from Parent1
c.m2()   # inherited from Parent2
c.m3()   # own method

# Ex 10 : Demonstrating different ways to initialize parent class variables

class person:
    def __init__(self, first, last):
        self.first = first   # initialize first name
        self.last = last     # initialize last name
        
class emp(person):
    def __init__(self, first, last, id):

        # # Method 1: Directly assigning parent class variables (not recommended)
        # self.first = first
        # self.last = last
        # self.id = id

        # Method 2: Using super() to call parent class constructor (recommended)
        super().__init__(first, last)
        self.id = id         # child class variable

        # # Method 3: Calling parent class constructor using class name (allowed but not recommended)
        # person.__init__(self, first, last)
        # self.id = id  

    def disp(self):
        # display employee details
        print("emp id = {} emp first name = {} emp last name = {}".format(
            self.id, self.first, self.last))

e1 = emp("dipti", "pawar", 111)
e1.disp()

e2 = emp("swaraj", "pawar", 222)
e2.disp()

# Ex 11 : Method overriding using __str__()

class person:
    def __init__(self, first, last):     # local variables
        self.first = first               # instance variable
        self.last = last

class emp(person):
    def __init__(self, first, last, id): # local variables
        person.__init__(self, first, last)  # calling parent class constructor
        self.id = id                       # child class instance variable

    def __str__(self):
        # overriding __str__() to return object data as string
        return "emp_id = {} emp first name = {} emp last name = {}".format(
            self.id, self.first, self.last)
    
e1 = emp("dipti", "pawar", 111)
print(e1)   # calls overridden __str__() method

e2 = emp("nikita", "pawar", 222)
print(e2)   # calls overridden __str__() method

# Ex 12 : isinstance() with inheritance

class parent:
    pass

class child(parent):
    pass

p = parent()   # creating parent class object
c = child()    # creating child class object

print(isinstance(p, parent))    # True → p is an object of parent
print(isinstance(c, child))     # True → c is an object of child
print(isinstance(c, parent))    # True → child IS-A parent
print(isinstance(c, object))    # True → every class inherits from object
print(isinstance(p, object))    # True → parent also inherits from object


# POLYMORPHISM
# One functionality with different behaviors
# Ability to appear in more than one form

# Ex 1 : Variable Overriding
# If a variable is overridden, child class value is used

class Parent:
    name = "dipti"

class Child(Parent):
    name = "swaraj"   # overriding parent variable

c = Child()
print(c.name)        # Output: swaraj

# Variable Inheritance (No Overriding)
# If child does not override, parent variable is used
class Parent:
    name = "dipti"

class Child(Parent):
    pass

c = Child()
print(c.name)        # Output: dipti

# Ex 2:
# METHOD OVERRIDING
# Child class provides its own implementation
# of the parent class method

# Case 1: Method Overriding
# Child method is executed

class Parent:
    def mrg(self):
        print("Marriage color is Black")

class Child(Parent):
    def mrg(self):
        print("Marriage color is Red")   # overridden method

c = Child()
c.mrg()        # Output: Marriage color is Red


# Case 2: No Overriding
# Child uses parent class method

class Parent:
    def mrg(self):
        print("Black girl")

class Child(Parent):
    pass        # no overriding

c = Child()
c.mrg()        # Output: Black girl

class Parrot:
    # Method to describe flying behavior
    def fly(self):
        print("Parrot can fly")

    # Method to describe swimming behavior
    def swim(self):
        print("Parrot can't swim")

# Ex 3

# Penguin class
class Penguin:
    # Method to describe flying behavior
    def fly(self):
        print("Penguin can't fly")

    # Method to describe swimming behavior
    def swim(self):
        print("Penguin can swim")


# Common interface function
# This function works with any object that has a fly() method
def flying_test(bird):
    bird.fly()


# Creating objects of different classes
parrot = Parrot()
penguin = Penguin()

# Passing different objects to the same function
# Python decides which fly() method to call at runtime
flying_test(parrot)
flying_test(penguin)

# Ex 4 : 
# Unicorn class
class Unicorn:
    # Method to display speed of unicorn
    def speed(self):
        print("Unicorn speed is 250 kmph")


# Splender class
class Splender:
    # Method to display speed of splender bike
    def speed(self):
        print("Splender speed is 100 kmph")


# Common interface function
# This function accepts any object that has a speed() method
def speed_test(vehicle):
    vehicle.speed()


# Creating objects of different classes
unicorn = Unicorn()
splender = Splender()

# Passing different objects to the same function
# Python calls the appropriate speed() method at runtime
speed_test(unicorn)
speed_test(splender)

# 3 . Encapsulation is the process of binding data (variables) and methods into a single unit (class)
#  and restricting direct access to some of the object's components.

# In Python, private members are created using double underscore (__).

# Ex 1: Private Variable Example
# Note: Private variables can be accessed only inside the class.
class A:
    # Private variable (cannot be accessed directly outside the class)
    __a = 10

    # Public method to access private variable
    def disp(self):
        print(self.__a)


# Creating object of class A
obj = A()

# Accessing private variable using class method
obj.disp()

# Direct access is NOT allowed
# print(obj.__a)   # AttributeError

# Ex 2: Encapsulation – Private Methods
# Note: Private methods are used for internal class operations only.
class MyClass:
    # Private method
    def __disp1(self):
        print("This is a private method")

    # Public method calling private method
    def disp2(self):
        print("disp2 is calling disp1")
        self.__disp1()


# Creating object
c = MyClass()

# Calling public method
c.disp2()

# Direct access is NOT allowed
# c.__disp1()   # AttributeError


# Private variables cannot be accessed directly, 
# but they can be read or modified indirectly using getter and setter methods.
# (this is indirect access)
# setters - to set the Data
# getters -   to get the data

# Ex 3 : to private variables we cannot do the direct modifications but we can do the modifications
# with the help of the get and set methods(indirect approach)
class emp:
    __eid = 111
    def seteid (self,eid):
        self.__eid = eid
    
    def geteid(self):
        return self.__eid

e = emp()
print(e.__eid())
print(e.geteid())

e.seteid(222)
print(e.geteid())

# Ex 4 :  Object Created Multiple Times
# Each method creates a new object of class A,
# which is inefficient and unnecessary

class A:
    num1, num2 = 100, 200

class B:
    def add(self):
        a = A()   # object created every time method is called
        print(a.num1 + a.num2)

    def mul(self):
        a = A()   # object created again
        print(a.num1 * a.num2)


# Creating object of class B
b = B()
b.add()
b.mul()


# Ex 5 : Solution – Create Object Only Once
# Object of class A is created at class level
# and reused by all methods of class B

class A:
    num1, num2 = 100, 200

class B:
    a = A()   # class-level object (created once)

    def add(self):
        print(self.a.num1 + self.a.num2)

    def mul(self):
        print(self.a.num1 * self.a.num2)


# Creating object of class B
b = B()
b.add()
b.mul()

# Note:
# 'a' is a class variable, so it is accessed using 'self'

# ABSTRACTION
# Abstraction is the process of hiding implementation details
# and showing only essential services (functionalities) to the user.
#
# In Python, abstraction is achieved using:
# 1. Abstract Classes
# 2. Abstract Methods
#
# ABC (Abstract Base Class) is a predefined abstract class
# present in the 'abc' module.
#
# Rules of Abstract Class:
# - An abstract class must inherit from ABC.
# - It can contain abstract methods (method declarations).
# - An abstract class object cannot be created.
# - A child class must implement all abstract methods,
#   otherwise it will also be treated as an abstract class.

from abc import ABC, abstractmethod

# Abstract class
class A(ABC):

    @abstractmethod
    def disp(self):
        pass    # abstract method (no implementation)

# Object creation is not possible for abstract classes
# a = A()     # TypeError: Can't instantiate abstract class A

# Ex 1 : 
from abc import ABC, abstractmethod
# Abstract class
class A(ABC):

    @abstractmethod
    def disp(self):
        pass    # abstract method (no implementation)

# Child class implementing abstract method
class B(A):

    def disp(self):
        print("Good Morning")

# Object creation
# a = A()   # TypeError: Can't instantiate abstract class A :(class A is abstract class)
b = B()
b.disp()

# To make a class an abstract class, it must inherit from the ABC class
# and it must contain at least one abstract method.
#
# To define an abstract method, we use the @abstractmethod decorator.


#   Abstract method:
# - Forces all child classes to implement eat()
# - Ensures consistency across subclasses
# - Prevents object creation of Person class
# Ex 2 :
from abc import ABC, abstractmethod
# Abstract class
class Person(ABC):

    @abstractmethod
    def eat(self):
        pass    # abstract method

# Child class Siya
class Siya(Person):

    def eat(self):
        print("3 idly")   # implementation

# Child class Piya
class Piya(Person):

    def eat(self):
        print("4 idly")   # implementation

s = Siya()   # object of Siya
s.eat()

p = Piya()   # object of Piya
p.eat()

# Ex 3 :
from abc import ABC, abstractmethod

# Abstract class with two abstract methods
class A(ABC):
    @abstractmethod
    def disp1(self):
        pass    # abstract method 1

    @abstractmethod
    def disp2(self):
        pass    # abstract method 2

# Partially implemented child class (still abstract)
class B(A):
    def disp1(self):
        print("Good Morning")   # implementation of disp1

# Child class completing all abstract methods
class Anu(B):

    def disp2(self):
        print("Good Evening")   # implementation of disp2

# Object creation is possible only after full implementation
a = Anu()
a.disp1()
a.disp2()

# Object creation is NOT possible for incomplete implementation
# b = B()   # TypeError: Can't instantiate abstract class B

# We can create any number of child classes, but all abstract methods
# must be fully implemented to allow object creation.

# Ex 4 : 
from abc import ABC, abstractmethod
# Abstract Base Class
class A(ABC):
    def __init__(self, value):
        self.value = value   # common data member

    @abstractmethod
    def disp(self):
        pass    # abstract method (must be implemented by child classes)

# Child class implementing the abstract method
class Add(A):
    def disp(self):
        print(10 + self.value)   # addition operation

# Another child class implementing the abstract method
class Mul(A):
    def disp(self):
        print(10 * self.value)   # multiplication operation

# Object creation is allowed because abstract method is fully implemented
a = Add(5)
a.disp()     # Output: 15

m = Mul(5)
m.disp()     # Output: 50

# ================================
# PACKAGES AND MODULES IN PYTHON
# ================================

# Package:
# A package is a folder (directory) that contains multiple Python modules.
# It is used to organize related modules into a structured hierarchy.

# Module:
# A module is a single Python file (.py) that contains functions, classes, or variables.
# Any Python file can be treated as a module.

'''
A project can be divided into small pieces (scripts).
Each script is called a module (Python file).

Any Python file that is reused or imported is referred to as a module.
'''

# ================================
# TYPES OF MODULES
# ================================

# 1. Predefined (Built-in) Modules:
# These modules are already available in Python.
# Examples:
# re          -> Regular Expressions
# abc         -> Abstract Base Classes
# os          -> Operating System related tasks
# time        -> Time-related functions
# threading  -> Multi-threading support

# 2. User-Defined Modules:
# Modules created by the user to organize project code.

# ================================
# IMPORTING A MODULE
# ================================

# Approach:
# import module_name

# When using this approach,
# functions or variables are accessed using the module name.

# Example:
# import operation
# operation.add()
# operation.sub()
'''
#  operations.py

def add(num1,num2):
    print(num1+num2)

def mul(num1,num2):
    print(num1*num2)

'''


# EXAMPLE 1: IMPORTING USER-DEFINED MODULE

# File Name: operations.py
# This file acts as a module containing reusable functions

def add(a, b):
    print("Addition:", a + b)

def mul(a, b):
    print("Multiplication:", a * b)

# APPROACH 1: import module_name
import operations          # importing the entire module
operations.add(3, 3)       # access using module name
operations.mul(4, 4)       # access using module name

# APPROACH 2: from module import function
from operations import add, mul   # importing only required functions
add(2, 2)                         # direct function call
mul(6, 6)


# APPROACH 3: from module import *
from operations import *     # importing all functions from the module
add(4, 4)
mul(8, 8)

# EXAMPLE 2: IMPORTING MULTIPLE MODULES

# File Name: operations1.py
# User-defined module containing functions

def disp1():
    print("This is disp1 from operations1 module")

def disp2():
    print("This is disp2 from operations1 module")

# File Name: A.py
# Another user-defined module

def show1():
    print("This is show1 from A module")

def show2():
    print("This is show2 from A module")

# File Name: client.py
# Main program file

# Approach 1 
# import module_name

import operations1          # importing operations1 module
import A                    # importing A module

operations1.disp1()         # access using module name
operations1.disp2()
A.show1()
A.show2()

# Approach 2 
# from module import function

from operations1 import disp1, disp2
from A import show1, show2

disp1()                     # direct function call
disp2()
show1()
show2()

# Approach 3 
# from module import *

from operations1 import *   # importing all functions
from A import *

disp1()
disp2()
show1()
show2()

# EXAMPLE 3: NAME CONFLICT IN MODULE IMPORTS
# ================================

# File Name: operations.py
def disp():
    print("operations : good morning")

# File Name: A.py
def disp():
    print("A : good morning")

# File Name: client.py
# ======================
# Approach 1 (RECOMMENDED) 
# import module_name
# Avoids name conflict by using module name

import operations
import A

operations.disp()    # Output: operations : good morning
A.disp()             # Output: A : good morning

# Approach 2 (NOT RECOMMENDED)
# from module import function
# Causes name conflict when function names are same

from operations import disp
from A import disp

disp()               # Output: A : good morning
# Reason: the most recently imported function overrides the previous one

# Another example showing overwrite behavior
from operations import disp
disp()               # Output: operations : good morning

from A import disp
disp()               # Output: A : good morning


# IMPORTING DATA: 3 APPROACHES
#==================================
# 1. Approach 1: import module_name
#    - Access functions using module name
#    - Safest and most recommended approach

# 2. Approach 2: from module import function
#    - Access functions directly
#    - Can cause name conflicts if names are same

# 3. Approach 3: from module import *
#    - Imports all functions directly
#    - High risk of name conflicts
#    - Not recommended for large projects


# Ex 4: IMPORTING CLASSES FROM MODULES

# File Name: A1.py
# Module containing a class

class fruits:
    def disp(self):
        print("I like mango")

# File Name: B1.py
# Module containing a class

class animals:
    def disp(self):
        print("I like tiger")


# File Name: client.py

# Approach 1 (RECOMMENDED)
# import module_name
# Class must be accessed using module name

import A1
import B1

f = A1.fruits()          # accessing class using module name
f.disp()

an = B1.animals()
an.disp()

# Approach 2 
# from module import ClassName

from A1 import fruits
from B1 import animals

f1 = fruits()            # direct class access
f1.disp()

an1 = animals()
an1.disp()

#  Approach 3
# from module import *
# Not recommended in large projects

from A1 import *
from B1 import *

f2 = fruits()
f2.disp()

an2 = animals()
an2.disp()

# ================================
# CHECKING CLASSES AND FUNCTIONS IN A MODULE
# ================================

# The dir() function is used to list
# all attributes present inside a module.
# This includes:
# - Classes
# - Functions
# - Variables
# - Built-in attributes (__name__, __file__, etc.)

# Ex 1: MODULE CONTAINING CLASSES
# File Name: first.py

class test:
    pass

class A:
    def m1(self):
        print("m1 method")
    
    def m2(self):
        print("m2 method")

# client.py
import first
print(dir(first))    # shows class names: test, A

# Ex 2: MODULE CONTAINING FUNCTIONS
# File Name: first.py

def m1():
    print("m1 method")

def m2():
    print("m2 method")

# client.py
import first
print(dir(first))    # shows function names: m1, m2

# The math module provides mathematical functions and constants.
# Importing math module
import math

# dir() is used to list all functions and constants present in the module
content = dir(math)
print(content)

import math

# ceil() returns the smallest integer greater than or equal to the number
print(math.ceil(30.3))      # Output: 31

# fabs() returns the absolute value as a float
print(math.fabs(10))        # Output: 10.0

# factorial() returns the factorial of a number
print(math.factorial(4))    # Output: 24

# floor() returns the largest integer less than or equal to the number
print(math.floor(30.9))     # Output: 30

# pow() returns x raised to the power y
print(math.pow(3, 4))       # Output: 81.0

# sqrt() returns the square root
print(math.sqrt(4))         # Output: 2.0

# sin() returns sine of the angle (in radians)
print(math.sin(90))         # Output: 0.8939966636005579

# Mathematical constants
print(math.pi)              # Output: 3.141592653589793
print(math.e)               # Output: 2.718281828459045

# 2. os Module

# The os module is used to interact with the operating system, 
# especially for file and directory operations.

import os

# Removes a file (file must exist)
os.remove("sample.txt")

# Creates a new directory
os.mkdir("new")

# Changes the current working directory
os.chdir("data")

# Prints current working directory
print(os.getcwd())

# Removes an empty directory
os.rmdir("new")

# Ex 3  :  random  : Used to generate random values
import random        # Import random module
print(dir(random))     # Display all available functions in random module

print(random.randint(1, 100))   # Generate a random integer between 1 and 100 (inclusive)
print(random.choice(['red', 'black', 'green']))   # Select a random element from a list
 
mylist = [1, 10.5, False, "dipti", "swaraj"]    # List with mixed data types
print(random.choice(mylist))     # Select a random element from the list

# Ex 4 : time : Used to work with time-related operations
import time    # Import time module
print(dir(time))    # Display all available functions in time module

print("hii dipti")   
time.sleep(1)         # Pause execution for 1 second
print(time.strftime('%x %x %z'))     # Display current date and timezone
print("hi dipti")

# Ex 5 : sys module : sys module data is pointing to the path locations
import sys
print(dir(sys))

# Ex 6 : regular expresssion :  also call regex or regexp for string pattern matching
# most common uses of re
# search a string (search and match)
# finding string(findall)
# break string into a sub string (split)
# replace part of a string(sub)

import re
print(dir(re))

# Ex 7 abc module : abstract
import abc
print(dir(abc))

# Ex 8 : zipfile  : Used to create, read, write, and extract ZIP files
import zipfile
print(dir(zipfile))

# Ex 9 :  logging   : Used for logging messages instead of print statements
import logging
print(dir(logging))

# Ex 10 : threading : Used for multi-threaded execution
import threading
print(dir(threading))

# Exception Handling in Python (try – except)
# 
#  Errors are problems that occur during program execution.

# Types of Errors
# 1. Syntax Error – Occurs due to incorrect syntax (detected at compile time)

# 2. Exception (Runtime Error) – Occurs while the program is running
#  ZeroDivisionError
#  IndexError
#  ValueError
#  TypeError

# Problems Without Exception Handling
# If an application contains an exception:
# 1. The program terminates abnormally
# 2. The rest of the application does not execute

# Main Objective of Exception Handling
# Using try-except:
# 1. Program terminates normally
# 2. Remaining code continues execution

# Syntax:
# try:
#     risky code
# except:
#     alternate code (executes when exception occurs)

# Ex 1: Application WITHOUT try-except
print("dipti")
print(10 / 0)           # ZeroDivisionError → abnormal termination
print("rest of the application")

#  Application WITH try-except
print("dipti")

try:
    print(10 / 0)       # risky code
except ZeroDivisionError as e:
    print(10 / 5)       # alternate code when exception occurs

print("rest of the application")

# Ex 2 : If the except block does NOT match the raised exception,
# the program terminates abnormally
try:
    print(10 / 0)          # Raises ZeroDivisionError

except TypeError as e:     # This except block does NOT match
    print(10 / 5)
    print("rest of the application")
# Since ZeroDivisionError is not handled,
# the program stops and code below is NOT executed

# Ex 3 : If there is NO exception in the try block,
# the except block is NOT executed

try:
    print("dipti")        # No exception occurs

except TypeError as e:
    print(10 / 5)         # This block is skipped

print("rest of the application")  # Executes normally

# Ex 4 : Only try block is INVALID
# A try block must be followed by at least one except or finally block

# try:
#     print("dipti")

# # SyntaxError: expected 'except' or 'finally'

# print("rest of the application")

# Ex 5 : Statements are NOT allowed between try and except blocks
# try, except, else, and finally must be continuous

# try:

# print("invalid")     #  INVALID: statement between try and except

# except Exception as e:
#     print("exception occurred")

# Ex 6 : Multiple statements in try block
# Case 1 : Exception occurs in the middle of try block

try:
    print("python")              # Executes
    print("java")                # Executes
    print(10 + "python")         # TypeError occurs here

except TypeError as e:
    print("python codes", e)     # Handles the exception

print("rest of the application") # Executes normally

#  Case 2
# If an exception occurs at the first statement in try block,
# remaining statements in try block are NOT executed

try:
    print(10 + "python")          # TypeError occurs here
    print("dipti")                # Skipped
    print("data")                 # Skipped

except TypeError as e:
    print("python program :", e)  # Handles the exception

print("rest of the application")  # Executes normally

# EXCEPTION HANDLING : else block and default except
# else block is executed ONLY when no exception occurs in try block

# Ex 1 : try-except-else
 
try:
    num = int(input("enter a number : "))    # enter number 2 -- no exception in try block
    print(10 / num)                       # risky code

except ArithmeticError as e:
    print("arithmetic error")             # handles arithmetic exceptions

else:
    print("no exception in try block : this is else")  # runs if no exception
   
print("rest of the application")  # this will always executed

# Notes:
# - Input = 2  → try block successful → else block executes
# - Input = 0  → ArithmeticError → else block does NOT execute
# - Input = abc → ValueError → else block does NOT execute
# - Code after try-except-else always executes# enter a number 0 (zero)  # else block will not execute

# the else block is always executed if there is no exception in try block

# Ex 2 : 
try:
    num = int(input("enter a number: "))
    print(10/num)
    for x in range(10):
        if x==2:
            break
except ArithmeticError as e:
    print("error occured ..")

else:
    print("no exception in try block : this is else ")

print("rest of the application")

# Ex 3 : default except block
# case when we are not using default except block
try:
    num = int(input("enter a number:"))   # enter string → ValueError
    print(10/num)

except ArithmeticError as e:
    print("error occured..")

else:
    print("no exception in try block : this is else block")

print("rest of the application")
# ValueError is not handled, so the program crashes.

# to avoid this we have to use default except block
# case 1 :
try:
    num = int(input("enter a number : "))
    print(10/num)

except ArithmeticError as e:
    print("arithmetic error occurred")

except:
    # default except block
    print("some other error occurred")

else:
    print("no exception in try block : this is else")

print("rest of the application")

# case 2 :
try :
    num = int(input("enter a number : "))
    print(10/num)

except ArithmeticError as e :
    print("this is arithmetic error")

except :      # default except block
    print("other error is handle with this default except")

else : 
    print("no exception in try block : this is else ")

print("rest of the application")

# # Ex 4 : the default except block must be last
# try:
#     num = int(input("enter a number : "))
#     print(10/0)

# except:         # default
#     print("default except block")

# except ArithmeticError as e:    SyntaxError: default 'except:' must be last
#     print("arithmetic error")

