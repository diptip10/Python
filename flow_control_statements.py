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
