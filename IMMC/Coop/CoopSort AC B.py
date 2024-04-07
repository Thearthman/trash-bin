from itertools import repeat

import numpy as np
import pandas as pd

import IMMCMichPack as mp

rawData = pd.read_excel(r"/Volumes/Personal/Coding/Python/Main/IMMC/RawData.xlsx", sheet_name="Sheet2")

max = []
maxId = []
iterate = [0]
sortedList = pd.DataFrame({"Alice": [], "Bob": [], "Charlie": []})
avgSortedList = pd.DataFrame({'0': [], '1': [], '2': []})
candidateNumber = 3

# First Tmax Sort
for p in range(30):
    max.append(rawData.iloc[p].max())
    maxId.append(int(rawData.iloc[p].idxmax()))
    sortedList.loc[p] = list(repeat(0, maxId[p])) + list(repeat(max[p], 1)) + list(
        repeat(0, (candidateNumber - 1 - maxId[p])))
    avgSortedList.loc[p] = list(repeat(np.NaN, maxId[p])) + list(repeat(max[p], 1)) + list(
        repeat(np.NaN, (candidateNumber - 1 - maxId[p])))

D = [avgSortedList.sum().max() - avgSortedList.sum().min()]
replacementList = avgSortedList
adList = [mp.getad(replacementList)]

# Starts Iterating for A B C
for i in range(50):
    sortedList, avgSortedList = mp.iteration(avgSortedList, avgSortedList, rawData, sortedList)
    D.append(avgSortedList.sum().max() - avgSortedList.sum().min())
    iterate.append(i + 1)
    adList.append(mp.getad(replacementList))
    if i > 20 and adList[len(iterate) - 1] == min(adList):
        break

mp.printdata(sortedList, avgSortedList, adList)

# Starts Iterating for A B
newSortList = pd.DataFrame({"Alice": sortedList.iloc[:, 0], "Charlie": sortedList.iloc[:, 2]})
newAvgList = pd.DataFrame({"Alice": avgSortedList.iloc[:, 0], "Charlie": avgSortedList.iloc[:, 2]})
newRawData = pd.DataFrame({"0": rawData.iloc[:, 0], "1": rawData.iloc[:, 2]})
newCandidateNumber = len(newRawData.columns)
newMax = []
newMaxId = []
mask = []

for j in range(30):
    mask.append(j) if sortedList.iloc[j, 0].item() != 0 or sortedList.iloc[j, 2].item() != 0 else None
print(mask)

iterationCount = 0
for j in mask:
    newMax.append(newRawData.iloc[j].max())
    newMaxId.append(int(newRawData.iloc[j].idxmax()))
    newSortList.loc[j] = list(repeat(0, newMaxId[iterationCount])) + list(repeat(newMax[iterationCount], 1)) + list(
        repeat(0, (1-newMaxId[iterationCount])))
    newAvgList.loc[j] = list(repeat(np.NaN, newMaxId[iterationCount])) + list(repeat(newMax[iterationCount], 1)) + list(
        repeat(np.NaN, (1-newMaxId[iterationCount])))
    iterationCount +=1


    sortedList.iloc[:, 0] = newSortList.iloc[:, 0]
    avgSortedList.iloc[:, 0] = newSortList.iloc[:, 0]
    sortedList.iloc[:, 2] = newSortList.iloc[:,1]
    avgSortedList.iloc[:, 2] = newSortList.iloc[:, 1]

adDataFrame = pd.Series({"AD before in-group distribution": min(adList), "AD now": mp.getad(sortedList)})
printList = sortedList._append(avgSortedList.sum(), ignore_index=True)
printList = printList._append(adDataFrame,ignore_index=True)
with pd.ExcelWriter("DataOut.xlsx",mode = "a", if_sheet_exists="replace") as writer:
    printList.to_excel(writer,sheet_name="AC+B")

mp.printdata(sortedList, avgSortedList, adList)
mp.drawplot(iterate, adList, "A vs B vs C Absolute Deviation against iteration", save=False)
