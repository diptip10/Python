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