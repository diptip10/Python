## flow control statements
# 1)conditional statements -- if, if-else, elif [based on specific condition specific block is executed]
a = 10
if a==10:
    print('if condition')
elif a==20:
    print('elif condition')    
else:
    print('else condition')    


# 2)iteration statements-- fpr and while[same code is repeated multiple times] 
# for - when we have starting value or ending value increment or decrement
# while- to check whether the data is available or not
for x in range(3):
    print('for loop')

# in 3 cases else block is not executed
# case1: whenever their is break statement in for loop
for x in range(20):
    if x==10:
        break
    print('python', x)
else:
    print('normal execution for for loop')

# case2: whenever we get an exception in for loop
for x in range(10):
    print('for loop',x)
    print(10/0)
else:
    print("normal execution of for loop")

# case3: when virtual machine / programme is shut down
import os
for x in range(10):
    print('python', x)
    os._exit(0)
else:
    print("normal execution of for loop")    

# while loop
a = 0
while a<10:
    print('dipti')
    a=a+1
    print("normal code")

# python variables
# 1) local -- declare inside the function
# 2) global -- declare outside the function
# functions are use to write the logics of the operation
# case1:
def disp():
    print("hello")
def disp2(name):              # here name is local variable
    print('hello',name)
disp()
disp2("dipti")        

# case2:
def disp1(name):
    print('hello',name)
def disp2():
    name= "language"   # local variable
    print(name)
disp1("world")
disp2()        

# case3: scope of local variable only within the function
def disp():
    name= 'python'
    print(name)
disp()
#print(name)     here we are printing outside the function so it will give name error 

# global-- scope--all the functions can access the global variable
# case1:
name= "dipti"
def dips():
    print(name)
def dips1():
    print('hello',name)
disp()
dips1()        

# case2: local and global combination with different names
a,b = 10,20
def add(x,y):
    print(a+b)
    print(x+y)
def mul(x,y):
    print(a*b)
    print(x*y) 
add(4,5)
mul(6,7)       

# case3: lobal and local var with same names---priority always goes to local to represent global 
# we have to use globals() to represent global variable
m,n = 20,30
def add(m,n):
    print(m+n)
    print(globals()['m']+globals()['n'])
def mul(m,n):
    print(m*n)
    print(globals()['m']*globals()['n'])
add(4,5)
mul(5,6)        

# case4: using global variable inside and outside the function
x=98
def disp1():
    print(x)  # printing global variable inside the function
disp1()
print(x)   # printing global var outside the function    

# inside the function once we are using global variable in this case with the same name it is not 
# possible to declare local variable

#global keyword-- inside the function to represent the global keyword variable we have function-global s

def disp():
    global s    # this is global keyword
    s='python'
    print(s)
disp()
print(s)    

# non-locak keyword-->Useful in closures when you want to modify a variable in the outer (non-global) function
def outer():
    y = 5
    def inner():
        nonlocal y
        y = 15  # Modifies y in outer()
    inner()
    print(y)

outer()  # Output: 15


def outer():
    name1= 'dipti'
    def inner():
        nonlocal name1
        name1='swaraj'
    print(name1)    
    inner()
    print(name1)
outer()    

name='python'
def outer():
    name1= 'java'
    def inner():
        nonlocal name1
        name1="scala"
        global name
        name= 'c++'
    print(name1)   # outer name1
    inner()    # inner function calling
    print(name1)  # scala
outer()
print(name)      # c++ global python change to c++


# functions in python
# 1) prefefined functions   2) user-defined functions

# function arguments
# 1) default argument  2) required argument  3) keyword argument   4) var argument

# default
def disp(eid=111, ename='john', esal= 10000):
    print(eid,ename,esal)
disp()              # if not pass any value then default value will be taken
disp(222)  
disp(333,"bella") 

# 2) required
def disp(eid, ename,esal):
    print(eid,ename, esal)
disp(1,'john',10000)    
disp('jack',2,20000)

# mixing both required and default
def disp(eid,ename="prince",esal=30000):   # once the default arguments started next all must be default 
    print(eid,ename, esal)
disp(3)    

#3) keyword argument-- while passing the data we must specify the name of the variable
def disp(eid,ename,esal):
    print(eid,ename, esal)
disp(eid=1,ename= "albert",esal=10000)    
disp(ename= "albert",eid=1,esal=10000)     # order of argument is not required

#4) variable argument
def disp(*a):
    for x in a:
        print(a)
disp()        
disp(2,3)       


##
name1='anil'
def outer():
    name1= 'dipti'
    def inner1():
        name1='swaraj'
        print("inner function name",name1)
    def inner2():
        nonlocal name1
        name1='ajinkya'
        print("inner function name",name1)
    def inner3():
        global name1
        name1='sangita'
        print("inner function name",name1) 
    print(name1)
    inner1()
    print(name1)
    inner2()
    print(name1)
    inner3()
    print(name1)
#print(name1)    
outer()
print(name1)              