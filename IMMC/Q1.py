from itertools import repeat
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

rawData = pd.read_excel(r"/Volumes/Personal/Coding/Python/Main/IMMC/RawData.xlsx", sheet_name="Q1")

max = []
maxId = []
maxData = []
sortedList = pd.DataFrame({'A': [], 'B': []})
avgSortedList = pd.DataFrame({'0': [], '1': []})
mask = pd.DataFrame({'A': [], 'B': []})
rebounce = False
iterate = [0]
idxNumberdData = rawData.rename(columns={"Alice": "0", "Bob": "1"})
q1 = pd.DataFrame({'0': [], '1': []})

# First Tmax Sort
for p in range(30):
    max.append(rawData.iloc[p].max())
    maxId.append(int(idxNumberdData.iloc[p].idxmax()))
    maxData.append([maxId[p], max[p]])
    sortedList.loc[p] = list(repeat(0, maxId[p])) + list(repeat(max[p], 1)) + list(repeat(0, (1 - maxId[p])))
    avgSortedList.loc[p] = list(repeat(np.NaN, maxId[p])) + list(repeat(max[p], 1)) + list(
        repeat(np.NaN, (1 - maxId[p])))
    mask.loc[p] = list(repeat(np.NaN, maxId[p])) + list(repeat(1, 1)) + list(repeat(np.NaN, (1 - maxId[p])))

print(sortedList)

D = [avgSortedList.sum().max() - avgSortedList.sum().min()]
dNew = 0
for g in range(2):
    dNew += abs(avgSortedList.sum().sum()/2 - avgSortedList.sum().iloc[g])
dNewList = [dNew]

q1 = sortedList
dNew = 0
dNew += abs(avgSortedList.sum().sum() / 2 - avgSortedList.sum().iloc[0])
dNew += abs(avgSortedList.sum().sum() / 2 - avgSortedList.sum().iloc[1])
print(dNew/2)

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
    range = int(avgSortedList.sum().max().item() - avgSortedList.sum().min().item())


    # find the items in itemTransHTLCost closest to Range
    itemTransHTL = (itemTransHTLCost.iloc[(itemTransHTLCost - range).abs().argsort()[:1]]).index


    # TransferHighToLow
    sortedList.iloc[itemTransHTL, highestP] = 0
    sortedList.iloc[itemTransHTL, lowestP] = rawData.iloc[
        itemTransHTL, lowestP]
    avgSortedList.iloc[itemTransHTL, highestP] = np.NaN
    avgSortedList.iloc[itemTransHTL, lowestP] = rawData.iloc[
        itemTransHTL, lowestP]

    dNew = 0
    dNew += abs(avgSortedList.sum().sum() / 2 - avgSortedList.sum().iloc[0])
    dNew += abs(avgSortedList.sum().sum() / 2 - avgSortedList.sum().iloc[1])  #依托答辩

    D.append(avgSortedList.sum().max() - avgSortedList.sum().min())
    iterate.append(i+1)
    dNewList.append(dNew/2)





print(sortedList)
# print(avgSortedList.sum())
print(dNewList[len(dNewList)-10:len(dNewList)-1])


x = iterate
y = dNewList

plt.plot(x,y)
plt.xlabel('Iteration')
plt.ylabel('Absolute Deviation')
plt.title('B & (A+C) Absolute Deviations respond to increasing Iteration')
plt.show()

