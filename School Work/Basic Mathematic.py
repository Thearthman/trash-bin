# Active = bool
start = input("Type 'Start' to start: ")
if start == "Start" or start == "start":
    Active = True
    while (Active):
        print("Choose your mode")
        if input() == '*':
            print("First number:  ", end="")
            a = int(input())
            print("Second number:  ", end="")
            b = int(input())
            print(a, end="")
            print("*", end="")
            print(b, end="")
            print("=", end="")
            print(a * b)
        elif input() == '+':
            print("First number:  ", end="")
            a = int(input())
            print("Second number:  ", end="")
            b = int(input())
            print(a, end="")
            print("*", end="")
            print(b, end="")
            print("=", end="")
            print(a + b)
        elif input() == '/':
            print("First number:  ", end="")
            a = int(input())
            print("Second number:  ", end="")
            b = int(input())
            print(a, end="")
            print("*", end="")
            print(b, end="")
            print("=", end="")
            print(a / b)
        elif input() == '-':
            print("First number:  ", end="")
            a = int(input())
            print("Second number:  ", end="")
            b = int(input())
            print(a, end="")
            print("*", end="")
            print(b, end="")
            print("=", end="")
            print(a - b)
        elif input() == "Stop":
            Active = False
            print("Stop")
