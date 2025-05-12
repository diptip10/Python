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

# reverse the string without using [::-1] or reversed()
def reverse_string(s):
    reversed_str=""
    for char in s:
        reversed_str= char+ reversed_str
    return reversed_str

print(reverse_string("dipti")) 

# reverse the string with [::-1] and reversed()
def reversed_str1(s):
    return "".join(reversed(s))
reversed_str1("dip")

def reverse(s1):
    return s1[::-1]
print(reverse("Pawar"))


# find the second largest number in a list
def sec_large_num(list1):
    list1=list(set(list1))
    list1.sort(reverse=True)
    return list1[1] if len(list1)> 1 else None
    
nums=[10,20,30,40,50,60,60,70]
print(sec_large_num(nums))



def sec_largest_num(lst):
    lst = list(set(lst))  # Now `list()` refers to the built-in list constructor
    lst.sort(reverse=True)
    return lst[1] if len(lst) > 1 else None

list1 = [10, 20, 30, 40, 40, 50, 60]
print(sec_largest_num(list1))  # Output: 50



l2=[2,3,4,4,5]
#get 2nd largest number from the list
def sec_la_num(list1):
    list1= list(set(list1))
    list1.sort(reverse=True)
    return list1[1] 
print(sec_la_num(l2))

def third_lar_num(list):
    list=list(set(l2))
    list.sort(reverse=True)
    return list[2]
print(third_lar_num(list))


# get the third largest number from list using ,max function
l3=[4,5,6,6,7,8,8]
def third_lar_no(list):
    list=list(set(l3))
    first_largest=max(list)
    sec_largest=max(x for x in list if x!=first_largest)
    third_largest=max(x for x in list if x!=first_largest and x!=sec_largest)
    return third_largest
print(third_lar_no(list))



# get the common letters between the two strings

def common_letters():
    str1=input("enter 1 st string:")
    str2=input("enter a 2nd string:")
    str1=set(str1)
    str2=set(str2)
    print(str1)
    print(str2)
    return str1 & str2
common_letters()    