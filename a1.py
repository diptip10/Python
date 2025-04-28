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
           
