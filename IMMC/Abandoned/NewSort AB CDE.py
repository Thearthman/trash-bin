from itertools import repeat

import numpy as np
import pandas as pd

import IMMCMichPack as mp

rawData = pd.read_excel(r"/Volumes/Personal/Coding/Python/Main/IMMC/RawData.xlsx", sheet_name="Sheet1")
newRawData = pd.DataFrame({"A+B": rawData.iloc[:, 0] + rawData.iloc[:, 1],
                           "C+D+E": rawData.iloc[:, 2] + rawData.iloc[:, 3] + rawData.iloc[:, 4]})
max = []
maxId = []
sortedList = pd.DataFrame({'A+B': [], 'C+D+E': []})
avgSortedList = pd.DataFrame({'0': [], '1': []})
iterate = [0]
idxNumberdData = newRawData.rename(columns={"A+B": "0", "C+D+E": "1"})

# First Tmax Sort
for p in range(30):
    max.append(newRawData.iloc[p].max())
    maxId.append(int(idxNumberdData.iloc[p].idxmax()))
    sortedList.loc[p] = list(repeat(0, maxId[p])) + list(repeat(max[p], 1)) + list(repeat(0, (1 - maxId[p])))
    avgSortedList.loc[p] = list(repeat(np.NaN, maxId[p])) + list(repeat(max[p], 1)) + list(
        repeat(np.NaN, (1 - maxId[p])))

D = [avgSortedList.sum().max() - avgSortedList.sum().min()]
replacementList = pd.DataFrame({'0': avgSortedList.iloc[:, 0] / 2, '1': avgSortedList.iloc[:, 1] / 3})
adList = [mp.getad(replacementList)]

# Starts Iterating
for i in range(30):
    lowestP = int(avgSortedList.sum().idxmin())
    highestP = int(avgSortedList.sum().idxmax())

    lowestPItem = avgSortedList.iloc[:, lowestP].dropna()
    lowestPItemToHigh = rawData.iloc[lowestPItem.index, highestP].dropna()
    highestPItem = avgSortedList.iloc[:, highestP].dropna()
    highestPItemToHigh = rawData.iloc[highestPItem.index, lowestP].dropna()
    itemTransHTLCost = highestPItem + highestPItemToHigh

    # find the item closest to transfer bound
    range = int(replacementList.sum().max().item() - replacementList.sum().min().item())

    # find the items in itemTransHTLCost closest to Range
    itemTransHTL = (itemTransHTLCost.iloc[(itemTransHTLCost - range).abs().argsort()[:1]]).index

    # TransferHighToLow
    sortedList.iloc[itemTransHTL, highestP] = 0
    sortedList.iloc[itemTransHTL, lowestP] = newRawData.iloc[
        itemTransHTL, lowestP]
    avgSortedList.iloc[itemTransHTL, highestP] = np.NaN
    avgSortedList.iloc[itemTransHTL, lowestP] = newRawData.iloc[
        itemTransHTL, lowestP]

    replacementList = pd.DataFrame({'0': avgSortedList.iloc[:, 0] / 2, '1': avgSortedList.iloc[:, 1] / 3})
    D.append(avgSortedList.sum().max() - avgSortedList.sum().min())
    iterate.append(i + 1)
    adList.append(mp.getad(replacementList))

mp.printdata(sortedList, avgSortedList, adList)
mp.drawplot(iterate, adList, "(A+B) vs (C+D+E) Absolute Deviation against iteration")
