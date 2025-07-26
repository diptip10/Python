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


# write a program that displays even numbers from 1 to 50 and odd numbers 51 to 100 using a repeating loop
for numbers in range(1,51):
    if numbers%2==0:
        print("even number:",numbers)

for numbers in range(51,101):
    if numbers%2!=0:
        print("odd number:",numbers)

number=1
while number <=100:
    if number<=50:
        if number%2==0:
            print('even',number)
    else:
        if number%2!=0:
            print("odd",number)
    number+=1


# create a program that prompts the user for a number and display the table of that number using a loop
number = int(input("Enter a number for table creation: "))
for i in range(1, 11):
    product = number * i
    print(number,"X",i,"=",product)


i=1
while i<=10:
    product=number*i
    print(number,'X',i,'=',product)
    i+=1

# write a program that asks for a number N and displays the sum of all numbers from 1 to N
number=int(input('enter a number:'))
sum_of_numbers=0
for num in range(1,number+1):
    sum_of_numbers+=num
    print("sum of N numbers using for loop",sum_of_numbers)

sum_of_numbers=0
num=1
while num<=number:
    sum_of_numbers+=num
    num+=1
    print("sum of numbers using while loop:",sum_of_numbers)
        
# write a program that calculates and displays the sum of even numbers from 1 to 100 using repeating loop
# by using for loop
sum_of_numbers=0
for num in range(101):
    if num%2==0:
        sum_of_numbers+=num
    print(sum_of_numbers)

# by using while loop
sum_of_numbers=0
num=0
while num <= 101:
    sum_of_numbers+=num
    print(sum_of_numbers)
    num+=2

# write a program that asks the user for number N and says whether it is prime or not
number= int(input('enter a number:'))
def is_prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
for x in range(2,number+1):
    if is_prime(x):
        print("prime number:", x)


# get primes from the given list of numbers
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

# given list
list = [1,2,3,4,5,6]
for n in list:
    if is_prime(n):
        print('prime',n)    


# get the prime numbers from 1 to 30
n=30
def is_prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

for x in range(n+1):
    if is_prime(x):
        print('prime',x)
    
## now get the prime numbers from 1 to 50
n=50
def is_prime(num):
    if num<=1:
        return False
    for x in range(2,int(num**0.5)+1):
        if num%x==0:
            return False
    return True
for x in range(2,n+1):
    if is_prime(x):
        print("prime",x)






