from itertools import repeat

import numpy as np
import pandas as pd

import IMMCMichPack as mp

rawData = pd.read_excel(r"/Volumes/Personal/Coding/Python/Main/IMMC/RawData.xlsx", sheet_name="Sheet2")

max = []
maxId = []
maxData = []
sortedList = pd.DataFrame({'A+B': [], 'Charlie': []})
avgSortedList = pd.DataFrame({'0': [], '1': []})
mask = pd.DataFrame({'A+B': [], 'Charlie': []})
rebounce = False
iterate = [0]
newRawData = pd.DataFrame({"A+B": rawData.iloc[:, 0] + rawData.iloc[:, 1], "Charlie": rawData.iloc[:, 2]})
idxNumberdData = newRawData.rename(columns={"A+B": "0", "Charlie": "1"})

# First Tmax Sort
for p in range(30):
    max.append(newRawData.iloc[p].max())
    maxId.append(int(idxNumberdData.iloc[p].idxmax()))
    maxData.append([maxId[p], max[p]])
    sortedList.loc[p] = list(repeat(0, maxId[p])) + list(repeat(max[p], 1)) + list(repeat(0, (1 - maxId[p])))
    avgSortedList.loc[p] = list(repeat(np.NaN, maxId[p])) + list(repeat(max[p], 1)) + list(
        repeat(np.NaN, (1 - maxId[p])))
    mask.loc[p] = list(repeat(np.NaN, maxId[p])) + list(repeat(1, 1)) + list(repeat(np.NaN, (1 - maxId[p])))

print(avgSortedList.sum())
D = [avgSortedList.sum().max() - avgSortedList.sum().min()]
replacementList = pd.DataFrame({'0': avgSortedList.iloc[:, 0] / 2, '1': avgSortedList.iloc[:, 1]})

adList = [mp.getad(replacementList)]

# Starts Iterating
for i in range(30):
    lowestP = int(replacementList.sum().idxmin())
    highestP = int(replacementList.sum().idxmax())

    lowestPItem = avgSortedList.iloc[:, lowestP].dropna()
    lowestPItemToHigh = newRawData.iloc[lowestPItem.index, highestP].dropna()
    highestPItem = avgSortedList.iloc[:, highestP].dropna()
    highestPItemToHigh = newRawData.iloc[highestPItem.index, lowestP].dropna()
    itemTransHTLCost = highestPItem + highestPItemToHigh

    # find the items in itemTransHTLCost closest to Range
    range = int(replacementList.sum().max().item() - replacementList.sum().min().item())
    itemTransHTL = (itemTransHTLCost.iloc[(itemTransHTLCost - range).abs().argsort()[:1]]).index

    # TransferHighToLow
    sortedList.iloc[itemTransHTL, highestP] = 0
    sortedList.iloc[itemTransHTL, lowestP] = newRawData.iloc[
        itemTransHTL, lowestP]
    avgSortedList.iloc[itemTransHTL, highestP] = np.NaN
    avgSortedList.iloc[itemTransHTL, lowestP] = newRawData.iloc[
        itemTransHTL, lowestP]

    replacementList = pd.DataFrame({'0': avgSortedList.iloc[:, 0] / 2, '1': avgSortedList.iloc[:, 1]})

    D.append(avgSortedList.sum().max() - avgSortedList.sum().min())
    iterate.append(i + 1)
    adList.append(mp.getad(replacementList))

mp.printdata(sortedList, avgSortedList, adList)
mp.drawplot(iterate, adList, "(A+B) vs C Absolute Deviation against iteration")
