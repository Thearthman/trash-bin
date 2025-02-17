array = [1, 9, 4, 5, 1, 10]
sum = 0

for i in range(6):
    sum = sum + array[i]
    print(i, array[i], "Sum= ", sum)

biggest = array[0]
for u in range(5):
    if biggest < array[u + 1]:
        biggest = array[u + 1]
        print(biggest)
    else:
        print(biggest)

print("Average = ", sum / (i + 1))
print(biggest)
