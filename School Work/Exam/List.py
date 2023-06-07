a = [int(input())]
count = 0
sum = 0
while count < 8:
    sum = sum + a[count]
    count += 1
print(sum / 8)
sum = 0
for i in range(8):
    sum = sum + a[i]
print(sum / 8)
