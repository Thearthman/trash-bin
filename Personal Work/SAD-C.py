import numpy as np

n = 0
bufferRead = [0, 0, 0, 0]


def conversion(rawData):
    processedData = 0
    for placeDigit in range(rawData[3]):
        placeValue = np.clip(rawData[rawData[3] - placeDigit - 1] - 48, 0, 9)
        processedData += placeValue * (10 ** placeDigit)
    return processedData

while True:
    while n < 3:
        bufferInt = int(input())
        if bufferInt == 10:
            numberOfUnfilledDigit = 3 - n
            for i in range(numberOfUnfilledDigit):
                bufferRead[n + i] = 0
            bufferRead[3] = n
            print(conversion(bufferRead))
            n = 0
            break
        bufferRead[n] = bufferInt
        n += 1
    bufferRead[3] = n
    if n == 3:
        print(conversion(bufferRead))
        n = 0
