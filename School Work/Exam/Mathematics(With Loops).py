looping = True
while looping:
    print("")
    print("$$This is a Calculator, Press Ctrl+C to Exit")
    try:
        a = int(input("Give me the first number  "))
        b = int(input("Give me the second number  "))
        x = input("What calculation do you want  ")
        end = 0
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
    except ValueError:
        print("Wrong Input")
    except TypeError:
        print("Wrong Input")
    except KeyboardInterrupt:
        print("")
        print("------Exiting-----")
        looping = False
