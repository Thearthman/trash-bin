looping = True
while looping:
    age = input("Enter your age: ")
    try:
        age = int(age)
        # print(type(age))
    except ValueError:
        print("Wrong input, try again")
        exception_triggered = True
    except KeyboardInterrupt:
        print("Exit")
        exception_triggered = False
    else:
        print("Calculating...")
        if age >= 18:
            print("Approved")
        else:
            print("Disapproved")
