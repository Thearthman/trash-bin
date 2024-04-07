def tribonacci(signature, n):
    processedList = signature[:]
    for i in range(n-3):
        processedList.append(processedList[i]+processedList[i+1]+processedList[i+2])
    processedList = processedList[0:n]
    return processedList
