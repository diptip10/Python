# print the statement - "python uses \n for newline"
print("python uses \n for newline")

# how will you print "/\/\/\/\"
print("/\\/\\/\\/\\")

# slicing
str = 'python coding'
print(str[2:10:2])

#merge three lists
x = [2,3,4]
y = [5,6,7]
z = [8,9,1]
print(list(zip(x,y,z)))
print(x+y+z)

# reverse the words from the string
str="Dipti Anil Pawar"
# split the string
str1=str.split()
# reversing
str1=str1[::-1]
# use .join() 
str2= " ".join(str1)
print(str2)
# or we can directly print the output
print(" ".join(str.split()[::-1]))

# print the list of numbers from the given list where numbers iteration = 1
mylist = [1,1,2,2,2,3,4,4,5,6,6,7]
new_list = []
for num in mylist:
    if mylist.count(num) == 1 :
        new_list.append(num)
print(new_list)

# by using list comprehension
[num for num in mylist if mylist.count(num)==1]

# if i want sum of all the numbers from the given list
sum=0
for num in mylist:
    sum+=num
print("sum of numbers in list",sum)    

# we have a string with comma seperated chara we have to get in dictionary format as it should contain 
# chara : iteration

str = "a,a,a,b,b,c,c,c"
mylist = str.split(",")
visited = []
for ch in mylist:
    if ch not in visited:
        print(f"{ch}:{mylist.count(ch)}",end=",")
        visited.append(ch)

# OR
mylist = str.split(",")
visited = []
final_list = []
for ch in mylist:
    if ch not in visited:
        final_list.append(f"{ch}:{mylist.count(ch)}")
        visited.append(ch)

print(final_list)

# counting vowels in a the word
vowels = ['a','e','i','o','u']
word = "python coding"
count = 0
found_vowels = []
for x in word:
    if x in vowels:
        count+=1
        found_vowels.append(x)
print(count)         
print(found_vowels)     


# counting number of occurences of letter 'm' in a word
str = 'programming'
ocuurence = 0
for occ in str:
    if occ == 'm' :
        ocuurence+=1
print("occurence of letter 'm' in a str is", ocuurence)


# finding the max number in the list
num_list = [2,3,4,5,6,7,22,34,32,53]
max = num_list[0]
for num in num_list:
    if max < num :
        max = num
print(max)        
    
    

        
