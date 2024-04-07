testList = [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]
answerList = [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def move_zeros(ogList):
    zeroCount = 0
    newList = ogList[:]
    for i in range(len(ogList)):
        if ogList[i] == 0:
            zeroCount += 1
            newList[len(ogList)-zeroCount] = 0
        else:
            newList[i-zeroCount] = ogList[i]
    return newList

if move_zeros(testList) == answerList:
    print("yes!")
else:
    print("fuck u no: ", move_zeros(testList))
    print("answer is: ", answerList)

