print("")
print("$$This is a Calculator, Press Ctrl+C to Exit")
try:
    a = int(input("Give me the first number  "))
    b = int(input("Give me the second number  "))
    x = input("What calculation do you want  ")
    if x == '*':
        end = a * b
    elif x == '/':
        end = a / b
    elif x == '+':
        end = a + b
    elif x == '-':
        end = a - b
    print(a, x, b, "=", end)
    print("")
except:
    print("Wrong Input")
