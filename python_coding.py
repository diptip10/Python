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
    