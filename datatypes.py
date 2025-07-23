# list- group of objects-homogenous or heterogenous,allow duplicates, follow indexing, mutable
list1=[2,3,6,"python"]
print(list1)
print(list1[0])  # get 1st element
print(list1[::-1]) # reversing the list
list1.reverse()
print(list1)
# make a program that asks for two numbers and displays if the first is divisible by the second
numbers= input("enter a number seperated by comma:").split(',')
num1=int(numbers[0])
num2=int(numbers[1])
print(num1)
print(num2)
if num1%num2==0:
    print("num1 is divisible by num2")
else:
    print("not divisible")

# write a program that displays the numbers 1 through 10 using a loop
# using for loop
for numbers in range(1,11):
    print(numbers)

# using while loop
num = 1
while num <= 10:
    print(num)
    num+=1

# write a program that displays all numbers from 1 to 100
number=1
while number in range(1,101):
    print(number)
    number+=1

for numbers in range(1,101):
    print(numbers)

# write a program that prints all even numbers from 1 to 100
num=1
while num <=100:
    if num%2==0:
        print(num)
    num+=1

# by using for loop get even numbers
for numbers in range(1,101):
    if numbers%2==0:
        print(numbers)
        # or
for numbers in range(2,101,2):
    print(numbers)        