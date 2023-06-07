import random

sum = 0
ran = []
for _ in range(1000):
    ran.append(random.randint(50, 200))
for i in range(1000):
    sum += ran[i]
x = random.randint(1, 3)
sum = round(sum / 1000, x)
print(ran, sum, x)
