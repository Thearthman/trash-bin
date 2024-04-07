from itertools import repeat

import numpy as np
import pandas as pd

import IMMCMichPack as mp

rawData = pd.read_excel(r"/Volumes/Personal/Coding/Python/Main/IMMC/RawData.xlsx", sheet_name="Sheet1")

maxValue = []
maxId = []
maxData = []
sortedList = pd.DataFrame({'A+B': [], 'Charlie': [], 'David': [], 'Erin': []})
avgSortedList = pd.DataFrame({'0': [], '1': [], '2': [], '3': []})
mask = pd.DataFrame({'A+B': [], 'Charlie': [], 'David': [], 'Erin': []})
rebounce = False
iterate = [0]
newRawData = pd.DataFrame({"A+B": rawData.iloc[:, 0] + rawData.iloc[:, 1], "Charlie": rawData.iloc[:, 2]
                              , "David": rawData.iloc[:, 3], "Erin": rawData.iloc[:, 4]})
idxNumberdData = newRawData.rename(columns={"A+B": '0', "Charlie": '1', "David": '2', "Erin": '3'})

# First Tmax Sort
for p in range(30):
    maxValue.append(newRawData.iloc[p].max())
    maxId.append(int(idxNumberdData.iloc[p].idxmax()))
    maxData.append([maxId[p], maxValue[p]])
    sortedList.loc[p] = list(repeat(0, maxId[p])) + list(repeat(maxValue[p], 1)) + list(repeat(0, (3 - maxId[p])))
    avgSortedList.loc[p] = list(repeat(np.NaN, maxId[p])) + list(repeat(maxValue[p], 1)) + list(
        repeat(np.NaN, (3 - maxId[p])))
    mask.loc[p] = list(repeat(np.NaN, maxId[p])) + list(repeat(1, 1)) + list(repeat(np.NaN, (3 - maxId[p])))

# weighting each group according to their member count
replacementList = pd.DataFrame(
    {'0': avgSortedList.iloc[:, 0] / 2, '1': avgSortedList.iloc[:, 1], '2': avgSortedList.iloc[:, 2],
     '3': avgSortedList.iloc[:, 3]})

# Assess the deviation of the data
adList = [mp.getad(replacementList)]
D = [avgSortedList.sum().max() - avgSortedList.sum().min()]

# Starts Iterating
for i in range(30):
    # find the person with the lowest total value and the person with the highest total value
    lowestP = int(replacementList.sum().idxmin())
    highestP = int(replacementList.sum().idxmax())
    lowestPItem = avgSortedList.iloc[:, lowestP].dropna()
    lowestPItemToHigh = rawData.iloc[lowestPItem.index, highestP].dropna()
    highestPItem = avgSortedList.iloc[:, highestP].dropna()
    highestPItemToHigh = rawData.iloc[highestPItem.index, lowestP].dropna()
    itemTransHTLCost = highestPItem + highestPItemToHigh

    # find the items in itemTransHTLCost closest to Range of total values obtained each group
    range = int(replacementList.sum().max().item() - replacementList.sum().min().item())
    itemTransHTL = (itemTransHTLCost.iloc[(itemTransHTLCost - range).abs().argsort()[:1]]).index

    # Transfer items
    sortedList.iloc[itemTransHTL, highestP] = 0
    sortedList.iloc[itemTransHTL, lowestP] = rawData.iloc[
        itemTransHTL, lowestP]
    avgSortedList.iloc[itemTransHTL, highestP] = np.NaN
    avgSortedList.iloc[itemTransHTL, lowestP] = rawData.iloc[
        itemTransHTL, lowestP]

    # Assess the absolute deviation
    replacementList = pd.DataFrame(
        {'0': avgSortedList.iloc[:, 0] / 2, '1': avgSortedList.iloc[:, 1], '2': avgSortedList.iloc[:, 2],
         '3': avgSortedList.iloc[:, 3]})
    D.append(avgSortedList.sum().max() - avgSortedList.sum().min())
    iterate.append(i + 1)
    adList.append(mp.getad(replacementList))

mp.printdata(sortedList, avgSortedList, adList)
mp.drawplot(iterate, adList, '(A+B) vs C vs D vs E  Absolute Deviations against Iteration')
