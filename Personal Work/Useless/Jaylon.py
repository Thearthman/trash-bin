score = [
    [10, 10, 10, 10, 25, 8, 67],
    [10, 10, 10, 9, 20, 10, 68],
    [10, 10, 5, 7, 5, 0, 31],
    [10, 10, 10, 9, 23, 0, 57],
    [10, 10, 5, 10, 19, 8, 73],
    [10, 10, 6, 9, 19, 0, 50]
]
amax = (10 + 10 + 10 + 10 + 27 + 10 + 74) / 7
average = [0.0 for i in range(7)]
for j in range(6):
    for i in range(7):
        average[j] += score[j][i]
    average[j] /= 7
for i in range(6):
    print(average[i] / amax)
