import random

test = False
rolls = int(input("type in rolls"))
columns = int(input("type in columns"))
a = [[random.randint(1, 10) for i in range(rolls)] for i in range(columns)]
b = int(input("type in the number you want to search for in this random 5*5 matrix"))
print(a)
print("Your number is:", b)
for i in range(columns):
    for j in range(rolls):
        if a[i][j] == b:
            print("there it is!")
            print("found in position:", end='')
            print("[", i, ",", j, "]")
            test = True
if test == False:
    print("😒😒😒what a pity, result doesn't found")
