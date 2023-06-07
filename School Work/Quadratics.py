import math

try:
    a = int(input("Give me a    "))
    b = int(input("Give me b    "))
    c = int(input("Give me c    "))
    delta = b ** 2 - 4 * a * c
    print("Delta: ", delta)
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
except ValueError:
    print("Invalid inputs, no real roots")
else:
    print("the value is", x1, ",", x2)
