from itertools import repeat

import numpy as np
import pandas as pd

import IMMCMichPack as mp

rawData = pd.read_excel(r"/Volumes/Personal/Coding/Python/Main/IMMC/RawData.xlsx", sheet_name="Sheet1")

max = []
maxId = []
iterate = [0]
sortedList = pd.DataFrame({'A+B+C+D': [], 'Erin': []})
avgSortedList = pd.DataFrame({'0': [], '1': []})
newRawData = pd.DataFrame({"A+B+C+D": rawData.iloc[:, 0] + rawData.iloc[:, 1] + rawData.iloc[:, 2] + rawData.iloc[:, 3],
                           "Erin": rawData.iloc[:, 4]})
idxNumberdData = newRawData.rename(columns={"A+B+C+D": "0", "Erin": "1"})

# First Tmax Sort
for p in range(30):
    max.append(newRawData.iloc[p].max())
    maxId.append(int(idxNumberdData.iloc[p].idxmax()))
    sortedList.loc[p] = list(repeat(0, maxId[p])) + list(repeat(max[p], 1)) + list(repeat(0, (1 - maxId[p])))
    avgSortedList.loc[p] = list(repeat(np.NaN, maxId[p])) + list(repeat(max[p], 1)) + list(
        repeat(np.NaN, (1 - maxId[p])))

D = [avgSortedList.sum().max() - avgSortedList.sum().min()]
replacementList = pd.DataFrame({'0': avgSortedList.iloc[:, 0] / 4, '1': avgSortedList.iloc[:, 1]})
adList = [mp.getad(replacementList)]

# Starts Iterating
for i in range(50):
    sortedList, avgSortedList = mp.iteration(replacementList, avgSortedList, newRawData, sortedList)
    replacementList = pd.DataFrame({'0': avgSortedList.iloc[:, 0] / 4, '1': avgSortedList.iloc[:, 1]})
    D.append(avgSortedList.sum().max() - avgSortedList.sum().min())
    iterate.append(i + 1)
    adList.append(mp.getad(replacementList))

mp.printdata(sortedList, avgSortedList, adList)
mp.drawplot(iterate, adList, '(A+B+C+D) vs E  Absolute Deviations against Iteration')
