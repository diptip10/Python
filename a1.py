print("Pawar")

#  find a sum from the given list
list=["2,3,4,5,6"]
list1=list[0].split(',')

total = 0
for i in list:
    total =total + int(i)

print(total)


# reversing a string using extended slicing technique
string="Python Programming"
print(string[::-1])

#reversing without slicing
reverse_string=""
for i in string:
    reverse_string=i+reverse_string
print(reverse_string)

# counting vowels in the given string
vowels= ['a','e','i','o','u']
string="programming"
count=0
for character in string:
    if character in vowels:
        count=count+1
print(count) 
           
# counting consonents in given string
vowels=['a','e','i','o','u']
string1='programming'
count=0
for char in string1:
    if char not in vowels:
        count=count+1
print('number of consonents:',count)                 

# occurence of character in string
name='python programming'
char='m'
count=0
for i in name:
    if i in char:
        count=count+1
print('count of m in a given string is:',count)        




# printing range of numbers
for x in range (1,11):
    print(x)

## using while loop --printing range of numbers 
num=1
while num<=10:
    print(num)
    num+=1

# calculate the sum of numbers in the list
list=["1,2,3,4"]
list1=list[0].split(",")
total=0
for x in list1:
   total+=int(x)
   print(total)



# printing range of numbers using while loop
numbers=1
while numbers<=10:
    print(numbers)
    numbers=numbers+1


# reverse the sring
def reverse_string(s):
    reversed_str=""
    for char in s:
        reversed_str= char+ reversed_str
    return reversed_str

print(reverse_string("dipti"))


