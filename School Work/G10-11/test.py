import random

level = 0
randomInt = 0
levels = [11, 12, 13, 14, 15, 16], [21, 22, 23, 24, 25, 26], [31, 32, 33, 34, 35, 36], [41,42,43,44,45,46]
avglevel = 0
correct = False
testing = True

while (testing):
    print(str(levels[level][randomInt]))
    answer = int(input())
    correct = answer == levels[level][randomInt]
    if correct:
        level += 1
    elif not(correct) and (abs(avglevel - (level-1)) > 1):
        level = level
    else:
        level -= 1
    level = min(3,max(0,level))
    randomInt = random.randint(0, 5)
    avglevel = (avglevel + level + 1) /2
    print(correct, level, avglevel)
    testing = not(input() == "stop")
