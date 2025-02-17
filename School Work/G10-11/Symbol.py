symbol = "*"


def askforsymbol():
    symbol = input("what do you want to be the symbol")
    return (symbol)


def askforarray():
    looping = True
    row = 0
    col = 0
    while looping:
        try:
            col = int(input("How many Columns do you want "))
            row = int(input("How many Rows do you want "))
            looping = False
        except:
            print("Wrong Input")
            col = 1
            row = -1
            looping = True
            # exit()
    return (row, col)


array = askforarray()


def stars(sym1, sym2, row, col):
    m = row / (col - 1)
    constRow = row
    constCol = col
    col2 = 0

    if (((col) % (row)) and col != row) == 0 or ((row) % (col - 1)) == 0:  # If the stepings are consistant

        col2 = 0
        if col > row:  # Whether the shape is vertical or horizontal
            kN = int((col) / (row))
            for rowi in range(row):
                for sym1I in range(col - 1):
                    print(sym1, "", end="")
                for stm2I in range(col2 + 1):
                    print(sym2, "", end="")
                col -= kN
                col2 += kN
                print("1")
        # elif col == row:
        #     for rowi in range(row):
        #         for sym1I in range(col-1):
        #             print(sym1, "", end="")
        #         for stm2I in range(col2+1):
        #             print(sym2, "", end="")
        #         col -= 1
        #         col2 += 1

        else:
            k = int((row) / (col - 1))
            for rowi in range(row):
                if rowi % k == 0:
                    col2 += 1
                    col -= 1
                for sym1I in range(col):
                    print(sym1, "", end="")
                for stm2I in range(col2):
                    print(sym2, "", end="")

                print("2")  # is like for k rows, add n
    elif col == row:
        # k = int((row)/(col-1))
        # col2 = 0
        # if  row % 2 == 0:                    will use the second algrithm
        #     for rowi in range(row):
        #         if rowi % k == 0:
        #             col2 += 1
        #             col -= 1
        #         for sym1I in range(col):
        #             print(sym1, "", end="")
        #         for stm2I in range(col2):
        #             print(sym2, "", end="")
        #         print("3")
        # else:
        #     for rowi in range(row):
        #         if rowi % k == 0:
        #             col2 += 1
        #             col -= 1
        #         for sym1I in range(col):
        #             print(sym1, "", end="")
        #         for stm2I in range(col2):
        #             print(sym2, "", end="")
        print("3")
    elif col % 2 == 0 and row % 2 == 0:
        k = int(round((row) / (col - 1)))
        if (row / k) - col <= 2:
            for rowi in range(row):
                if rowi % k == 0:
                    col2 += 1
                    col -= 1
                for sym1I in range(col):
                    print(sym1, "", end="")
                for stm2I in range(col2):
                    print(sym2, "", end="")
                print("4.1", rowi + 1)
        # else:


    else:  # The stepping is inconsistant

        if m > (3 / 2) and col % 2 == 1:
            k = int((row) / (col - 1) + 1)
            for rowi in range(row - 1):
                if rowi % k == 0:
                    col2 += 1
                    col -= 1
                for sym1I in range(col):
                    print(sym1, "", end="")
                for stm2I in range(col2):
                    print(sym2, "", end="")
                print("3")
            for sym1I in range(1):
                print(sym1, "", end="")
            for stm2I in range(constCol - 1):
                print(sym2, "", end="")


        elif m > (3 / 2) and col % 2 == 0:
            k = int(round((row) / (col - 1)))
            for rowi in range(row - 2):
                if rowi != int(row / 2):
                    if rowi % k == 0:
                        col2 += 1
                        col -= 1
                    for sym1I in range(col):
                        print(sym1, "", end="")
                    for stm2I in range(col2):
                        print(sym2, "", end="")
                    print("3")
                else:
                    if (rowi + 1) % k == 0:
                        if (constCol != 4):
                            for sym1I in range(int(constCol / 2) + 1):
                                print(sym1, "", end="")
                            for stm2I in range(int(constCol / 2) - 1):
                                print(sym2, "", end="")
                        else:
                            for sym1I in range(int(constCol / 2)):
                                print(sym1, "", end="")
                            for stm2I in range(int(constCol / 2)):
                                print(sym2, "", end="")
                            col2 = int(constCol / 2 - 1)
                            col = int(constCol / 2 + 1)
                    else:
                        for sym1I in range(int(constCol / 2)):
                            print(sym1, "", end="")
                        for stm2I in range(int(constCol / 2)):
                            print(sym2, "", end="")
                            col2 = int(constCol / 2)
                            col = int(constCol / 2)
                    print("3+")
            if (constRow / k > constCol):
                for p in range(2, 0, -1):
                    for sym1I in range(1):
                        print(sym1, "", end="")
                    for stm2I in range(constCol - 1):
                        print(sym2, "", end="")
                    print("3.1")
            else:
                for p in range(2, 0, -1):
                    for sym1I in range(p):
                        print(sym1, "", end="")
                    for stm2I in range(constCol - p):
                        print(sym2, "", end="")
                    print("3.")


# Stars(askForSymbol(),askForSymbol(),array[0],array[1])
stars("○", "▲", array[0], array[1])  # △ ○ ☐ ▲
