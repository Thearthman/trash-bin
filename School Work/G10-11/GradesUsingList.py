s1 = [10, 10, 10, 10, 25, 8, 67]
s2 = [10, 10, 10, 9, 20, 10, 68]
s3 = [10, 10, 5, 7, 5, 0, 31]
s4 = [10, 10, 10, 9, 23, 0, 57]
s5 = [10, 10, 5, 10, 19, 8, 73]
s6 = [10, 10, 6, 9, 19, 0, 50]
MAX = [10, 10, 10, 10, 27, 10, 74]
std = [s1, s2, s3, s4, s5, s6]
decimalplace = int(input("Precision? "))


def printscore():
    for i in range(0, 6):
        avg = 0
        for u in range(0, 7):
            score = std[i][u] / MAX[u]
            avg = avg + score
        print("Student", i + 1, round((avg / 7 * 100), decimalplace))


printscore()
