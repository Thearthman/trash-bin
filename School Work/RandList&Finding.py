import random

looping = True
col = []
row = []
global i
start = 0
while looping == True:
    try:
        global askrow, askcol
        askrow = int(input("rows?"))
        askcol = int(input("cols?"))
        looping = False
    except ValueError and TypeError:
        print("Wrong input")
looping = True

for _ in range(askcol):
    row = []
    for _ in range(askrow):
        row.append(random.randint(50, 60))
    col.append(row)
print(col)

find = int(input("which number u would like to find"))
while looping == True:
    try:
        for i in range(start, askcol):
            print([i + 1, col[i].index(find) + 1])
        looping = False
    except ValueError:
        print("nf")
        start = i + 1
