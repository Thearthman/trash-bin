std = []
test = []
maxstd = 0
listofstd = []
exception = True


# decimalplace = int(input("Precision? "))

def creatstudent(name):
    global maxstd, exception
    exception = True

    maxstd += 1
    staticname = ""

    stddata = name
    testdata = ""

    globals()[staticname] = [name]

    while exception:
        try:
            listofstd.append(name)
            global times
            times = int(input("how many assignments do you want: "))
            globals()[stddata] = [int(input(a + 1)) for a in range(times)]
            std.append(globals()[staticname])
            globals()[staticname].append(globals()[stddata])
            if input("Uniform Max score? (Answer y or n)") == 'n':
                print("Now for each task, the max score")
                globals()[testdata] = [int(input(b + 1)) for b in range(times)]
                test.append(globals()[testdata])
            else:
                maxscore = int(input("Input the Max score: "))
                globals()[testdata] = [maxscore for _ in range(times)]
                test.append(globals()[testdata])
            exception = False
        except:
            print("Invalid input")
            exception = True

    return std


# def initvar():

def printscore():
    if input("Average test score or Individual test score (Type 'avg' or 'idv'): ") == "avg":
        global avgdata, selectedstd, newgrade
        newgrade = []
        avgdata = [[] for _ in range(maxstd)]
        for selectedstd in range(0, maxstd):
            avg = 0
            for u in range(0, times):
                score = std[selectedstd][1][u] / test[selectedstd][u]
                avg = avg + score
            # avgdata contains all the student's data. avgdata[0] gives you the data for the first student [name, score]
            # avgdata[0][1] only gives you the score.
            avgdata[selectedstd] = [listofstd[selectedstd], round((avg / times * 100), 2)]
            avgdata[selectedstd].append(gradingsystem())

        return avgdata
    else:

        print("here goes nothing")


def MyBestScores(stdname, task):
    stdnum = listofstd.index(stdname)
    nameordata = 1
    task -= 1
    stdtaskscore = std[stdnum][nameordata][task]

    return [stdtaskscore, ]


def gradingsystem():
    global grade
    grade = ''
    if avgdata[selectedstd][1] < 50:
        grade = 'E'
    elif avgdata[selectedstd][1] < 60:
        grade = 'D'
    elif avgdata[selectedstd][1] < 70:
        grade = 'C'
    elif avgdata[selectedstd][1] < 80:
        grade = 'B'
    elif avgdata[selectedstd][1] < 90:
        grade = 'A'
    elif avgdata[selectedstd][1] < 101:
        grade = 'A*'
    return grade


def mainfunction():
    creatstudent(input("name? "))


mainfunction()
print(printscore())
