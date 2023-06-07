import random

looping = True
cal1 = []
cal2 = []
row = []
sum = []
while looping == True:
    try:
        global askrow, askcol
        askrow = int(input("rows?"))
        askcol = int(input("cols?"))
        looping = False
    except ValueError and TypeError:
        print("Wrong input")
looping = True
constrow = askrow
constcol = askcol
for _ in range(askcol):
    row = []
    for _ in range(askrow):
        row.append(random.randint(1, 10))
    cal1.append(row)
print("First Random List: ", cal1)

for _ in range(askcol):
    row = []
    for _ in range(askrow):
        row.append(random.randint(1, 10))
    cal2.append(row)
print("Second Random List: ", cal2)

# sum

sum = []
sumrow = []
for _ in range(askcol):
    sumrow = []
    for _ in range(askrow):
        sumrow.append(0)
    sum.append(sumrow)

for u in range(askcol):
    for i in range(askrow):
        sum[u][i] = cal1[u][i] + cal2[u][i]

print("sum is: ", sum)
