print("Pawar")

#  find a sum from the given list
list=["2,3,4,5,6"]
list1=list[0].split(',')

total = 0
for i in list:
    total =total + int(i)

print(total)