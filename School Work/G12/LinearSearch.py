import random

myList = [random.randint(0,10) for _ in range(10)]
upperBound = 9
lowerBound = 0
index = lowerBound
item = int(input("enter the number to be found:"))
found = False

while not found and index <= upperBound:
    if item == myList[index]:
        found = True
    index += 1

if found:
    print("Found")
else:
    print("Not found")

