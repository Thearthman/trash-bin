from itertools import repeat
import numpy as np
import pandas as pd
import IMMCMichPack as mp

rawData = pd.read_excel(r"/Volumes/Personal/Coding/Python/Main/IMMC/RawData.xlsx", sheet_name="Sheet2")

max = []
maxId = []
iterate = [0]
sortedList = pd.DataFrame({'A+C': [], 'Bob': []})
avgSortedList = pd.DataFrame({'0': [], '1': []})
newRawData = pd.DataFrame({"A+C": rawData.iloc[:, 0] + rawData.iloc[:, 2], "Bob": rawData.iloc[:, 1]})
idxNumberdData = newRawData.rename(columns={"A+C": "0", "Bob": "1"})

# First Tmax Sort
for p in range(30):
    max.append(newRawData.iloc[p].max())
    maxId.append(int(idxNumberdData.iloc[p].idxmax()))
    sortedList.loc[p] = list(repeat(0, maxId[p])) + list(repeat(max[p], 1)) + list(repeat(0, (1 - maxId[p])))
    avgSortedList.loc[p] = list(repeat(np.NaN, maxId[p])) + list(repeat(max[p], 1)) + list(
        repeat(np.NaN, (1 - maxId[p])))

replacementList = pd.DataFrame({'0': avgSortedList.iloc[:, 0] / 2, '1': avgSortedList.iloc[:, 1]})
D = [avgSortedList.sum().max() - avgSortedList.sum().min()]
adList = [mp.getad(replacementList)]

# Starts Iterating
for i in range(30):
    sortedList, avgSortedList = mp.iteration(replacementList,avgSortedList,newRawData,sortedList)
    replacementList = pd.DataFrame({'0': avgSortedList.iloc[:, 0] / 2, '1': avgSortedList.iloc[:, 1]})
    D.append(avgSortedList.sum().max() - avgSortedList.sum().min())
    iterate.append(i + 1)
    adList.append(mp.getad(replacementList))

mp.printdata(sortedList, avgSortedList, adList)
mp.drawplot(iterate, adList, "(A+C) & B Absolute Deviations against iteration")
