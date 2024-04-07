from itertools import repeat
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import IMMCMichPack as mp
rawData = pd.read_excel(r"/Volumes/Personal/Coding/Python/Main/IMMC/RawData.xlsx", sheet_name="Sheet2")

max = []
maxId = []
maxData = []
sortedList = pd.DataFrame({"Alice": [], "Bob": [],"Charlie": []})
avgSortedList = pd.DataFrame({'0': [], '1': [], '2': []})
mask = pd.DataFrame({'Alice': [], 'Bob': [], 'Charlie':[]})
rebounce = False
iterate = [0]
newRawData = pd.DataFrame({"Alice": rawData.iloc[:,0], "Bob":rawData.iloc[:,1], 'Charlie':rawData.iloc[:,2]})
idxNumberdData = newRawData.rename(columns={"Alice": "0", "Bob": "1", "Charlie": '2'})
candidateNumber = 3

# First Tmax Sort
for p in range(30):
    max.append(newRawData.iloc[p].max())
    maxId.append(int(idxNumberdData.iloc[p].idxmax()))
    maxData.append([maxId[p], max[p]])
    sortedList.loc[p] = list(repeat(0, maxId[p])) + list(repeat(max[p], 1)) + list(repeat(0, (candidateNumber-1 - maxId[p])))
    avgSortedList.loc[p] = list(repeat(np.NaN, maxId[p])) + list(repeat(max[p], 1)) + list(
        repeat(np.NaN, (candidateNumber -1 - maxId[p])))
    mask.loc[p] = list(repeat(np.NaN, maxId[p])) + list(repeat(1, 1)) + list(repeat(np.NaN, (candidateNumber-1 - maxId[p])))

print(avgSortedList.sum())
D = [avgSortedList.sum().max() - avgSortedList.sum().min()]
replacementList = avgSortedList

adList = [mp.getad(replacementList, candidateNumber)]



# Starts Iterating
for i in range(30):

    replacementList = avgSortedList
    lowestP = int(replacementList.sum().idxmin())
    highestP = int(replacementList.sum().idxmax())



    lowestPItem = avgSortedList.iloc[:, lowestP].dropna()
    lowestPItemToHigh = rawData.iloc[lowestPItem.index, highestP].dropna()
    highestPItem = avgSortedList.iloc[:, highestP].dropna()
    highestPItemToHigh = rawData.iloc[highestPItem.index, lowestP].dropna()
    itemTransHTLCost = highestPItem + highestPItemToHigh


    # find the items in itemTransHTLCost closest to Range
    range = int(replacementList.sum().max().item() - replacementList.sum().min().item())
    itemTransHTL = (itemTransHTLCost.iloc[(itemTransHTLCost - range).abs().argsort()[:1]]).index


    # TransferHighToLow
    sortedList.iloc[itemTransHTL, highestP] = 0
    sortedList.iloc[itemTransHTL, lowestP] = rawData.iloc[
        itemTransHTL, lowestP]
    avgSortedList.iloc[itemTransHTL, highestP] = np.NaN
    avgSortedList.iloc[itemTransHTL, lowestP] = rawData.iloc[
        itemTransHTL, lowestP]

    D.append(avgSortedList.sum().max() - avgSortedList.sum().min())
    iterate.append(i+1)
    adList.append(mp.getad(replacementList, candidateNumber))


mp.printdata(sortedList,avgSortedList,adList)
mp.drawplot(iterate,adList,"A vs B vs C Absolute Deviation against iteration")

