board = [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']
potential = [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']
antipotential = [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']
turn = "white"
winner = ""
judge = False
end = False
looping = True
coordinate = [0, 0]
player = 'o'
ai = 'x'
# debug
skip = False


def init():
    global firstplayer, secondplayer, turn
    looping = True
    while looping:
        userinput = input("what player do you want to be: (w or b)")

        if userinput == 'w':
            firstplayer = player
            secondplayer = ai
            looping = False
        elif userinput == 'b':
            firstplayer = ai
            secondplayer = player
            looping = False
        else:
            print("invalid input, try again")

    if firstplayer == player:
        turn = "white"
    else:
        turn = "black"


def print_line(line):
    line -= 1
    print("| ", end='')
    for i in range(3):
        print(board[line][i], "| ", end="")
    print()


def print_board():
    for i in range(3, 0, -1):
        print("  ", end='')
        for _ in range(13):
            print("-", end='')
        print()
        print(i, end=' ')
        print_line(i)
    print("  ", end='')
    for _ in range(13):
        print("-", end='')
    print()
    print("    1   2   3  ")


def judge_system():
    global judge, end

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            judge = True
        elif board[0][i] == board[1][i] == board[2][i] != ' ':
            judge = True
        elif board[0][0] == board[1][1] == board[2][2] != ' ':
            judge = True
        elif board[0][2] == board[1][1] == board[2][0] != ' ':
            judge = True

    i = 0
    k = 0
    while board[i][k] != ' ' and not end and not judge:
        if k < 2:
            k += 1
        elif k == 2 and i == 2:
            end = True
        else:
            k = 0
            i += 1

    return end


def coord_update():
    if turn == "white":
        player_update()
    if turn == "black":
        ai_update()


def player_update():
    global coordinate, skip
    looping = True
    while looping:
        coordinput = input("Enter Coordinate you want to place (x,y): ")
        if coordinput == "skip":
            skip = True
            coordinate = [0, 0]
            break
        elif ',' not in coordinput:
            print("Invalid input. Please enter two numbers separated by a comma.")
            continue
        try:
            coordinate = coordinput.split(',')
            if not len(coordinate) > 2:
                coordinate[0] = int(coordinate[0]) - 1
                coordinate[1] = int(coordinate[1]) - 1
            else:
                raise ValueError
            looping = False
        except (ValueError, TypeError, IndexError):
            print("Wrong Input. Please enter two numbers separated by a comma.")


def board_update(line, row):
    global turn, winner, board
    if skip == True:
        board = ['x', 'o', 'x'], ['x', 'x', 'o'], ['o', 'x', 'o']
    elif turn == "white":
        board[row][line] = 'o'
        turn = "black"
        winner = "White"
    elif turn == "black":
        board[row][line] = 'x'
        turn = "white"
        winner = "Black"

    return winner


def attack_update():
    global suggestedattack
    for i in range(3):
        for u in range(3):
            if board[i][u] == ai:
                potential[i][u] = 1
            elif board[i][u] == player:
                potential[i][u] = -3
            elif board[i][u] == ' ':
                potential[i][u] = 0

    way1 = [0, 0, 0]
    way2 = [0, 0, 0]
    for i in range(3):
        way1[i] = potential[i][0] + potential[i][1] + potential[i][2]
        way2[i] = potential[0][i] + potential[1][i] + potential[2][i]
    way3 = potential[0][0] + potential[1][1] + potential[2][2]
    way4 = potential[0][2] + potential[1][1] + potential[2][0]
    potentialattack = [*way1, *way2, way3, way4]  # [y=1, y=2, y=3; x=1, x=2, x=3; lb to rf; lf to rb]

    # Compare to get the most likely way to win
    biggest = potentialattack[0]
    listofbiggest = [[0, potentialattack[0]]]
    suggestedattacklist = [0]
    for u in range(7):
        if biggest < potentialattack[u + 1]:
            biggest = potentialattack[u + 1]
            suggestedattacklist.append(u + 1)
        listofbiggest.append([u + 1, biggest])
    suggestedattack = 0
    for i in range(len(suggestedattacklist) - 1):
        if suggestedattack < suggestedattacklist[i + 1]:
            suggestedattack = suggestedattacklist[i + 1]
    suggestedattack = [suggestedattack, biggest]
    print(suggestedattack)


def defense_update():
    global suggesteddefence
    for i in range(3):
        for u in range(3):
            if board[i][u] == player:
                antipotential[i][u] = 1
            elif board[i][u] == ai:
                antipotential[i][u] = -3
            elif board[i][u] == ' ':
                antipotential[i][u] = 0

    way1 = [0, 0, 0]
    way2 = [0, 0, 0]
    for i in range(3):
        way1[i] = antipotential[i][0] + antipotential[i][1] + antipotential[i][2]
        way2[i] = antipotential[0][i] + antipotential[1][i] + antipotential[2][i]
    way3 = antipotential[0][0] + antipotential[1][1] + antipotential[2][2]
    way4 = antipotential[0][2] + antipotential[1][1] + antipotential[2][0]
    potentialdefence = [*way1, *way2, way3, way4]  # [y=1, y=2, y=3; x=1, x=2, x=3; lb to rf; lf to rb]

    # Compare to get the most likely way to win
    biggest = potentialdefence[0]
    suggesteddefencelist = [0]
    for u in range(7):
        if biggest < potentialdefence[u + 1]:
            biggest = potentialdefence[u + 1]
            suggesteddefencelist.append(u + 1)
    suggesteddefence = 0
    for i in range(len(suggesteddefencelist) - 1):
        if suggesteddefence < suggesteddefencelist[i + 1]:
            suggesteddefence = suggesteddefencelist[i + 1]
    suggesteddefence = [suggesteddefence, biggest]
    print(suggesteddefence)


def coord_conversion(attack):
    if attack:
        print("attack")
        # first find the line/row the coord is at / [y=1, y=2, y=3; x=1, x=2, x=3; lb to rf; lf to rb]
        if suggestedattack[1] < 0:
            coordinate[0] = 0
            coordinate[1] = 0
            for i in range(3):
                for u in range(3):
                    if board[i][u] == ' ':
                        coordinate[1] = i
                        coordinate[0] = u
        elif suggestedattack[1] == 0 and suggestedattack[0] == 0 and suggesteddefence[1] == 0 and suggesteddefence[
            0] == 0:
            coordinate[0] = 1
            coordinate[1] = 1
        elif suggestedattack[0] < 3:
            coordinate[1] = suggestedattack[0]
            coordinate[0] = 0
            while board[coordinate[1]][coordinate[0]] != ' ':
                coordinate[0] += 1
        elif suggestedattack[0] < 6:
            coordinate[0] = suggestedattack[0] - 3
            coordinate[1] = 0
            while board[coordinate[1]][coordinate[0]] != ' ':
                coordinate[1] += 1
        elif suggestedattack[0] == 6:
            # can't make sure x-value nor y-value of the coord
            coordinate[0] = 0
            coordinate[1] = 0
            while board[coordinate[0]][1] != ' ':
                coordinate[0] += 1
                coordinate[1] += 1
            print(coordinate)
        else:
            coordinate[0] = 0
            coordinate[1] = 2
            while board[coordinate[0]][coordinate[1]] != ' ':
                coordinate[0] += 1
                coordinate[1] -= 1
            print(coordinate)


    elif not attack:
        print("defence")
        if suggesteddefence[1] < 0:
            coordinate[0] = 0
            coordinate[1] = 0
            for i in range(3):
                for u in range(3):
                    if board[i][u] == ' ':
                        coordinate[1] = i
                        coordinate[0] = u
        elif suggesteddefence[0] < 3:
            coordinate[1] = suggesteddefence[0]
            coordinate[0] = 0
            while board[coordinate[1]][coordinate[0]] != ' ':
                coordinate[0] += 1
        elif suggesteddefence[0] < 6:
            coordinate[0] = suggesteddefence[0] - 3
            coordinate[1] = 0
            while board[coordinate[1]][coordinate[0]] != ' ':
                coordinate[1] += 1
        elif suggesteddefence[0] == 6:
            # can't make sure x-value nor y-value of the coord
            coordinate[0] = 0
            coordinate[1] = 0
            while board[coordinate[1]][0] != ' ':
                coordinate[0] += 1
                coordinate[1] += 1
            print("1", coordinate)
        else:
            coordinate[0] = 0
            coordinate[1] = 2
            while board[coordinate[1]][coordinate[0]] != ' ':
                coordinate[0] += 1
                coordinate[1] -= 1
            print("2", coordinate)


def ai_update():
    attack_update()
    defense_update()
    if suggesteddefence[1] <= suggestedattack[1]:
        # attack
        coord_conversion(True)
    else:
        coord_conversion(False)


def mainfunction():
    init()
    while not end:
        print_board()
        while not judge and not end:
            coord_update()  # coord_update
            looping = True
            while looping and not skip:
                if coordinate[0] > 2 or coordinate[1] > 2 or board[coordinate[1]][coordinate[0]] != ' ':
                    print("Wrong Input")
                    player_update()
                else:
                    looping = False
            board_update(*coordinate)
            judge_system()
            print_board()
        if not end:
            print("Winner is", winner, '!')
            break
        else:
            print("Draw")
            break


mainfunction()
