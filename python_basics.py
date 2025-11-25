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
