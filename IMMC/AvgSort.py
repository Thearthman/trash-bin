from itertools import repeat

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

rawData = pd.read_excel(r"/Volumes/Personal/Coding/Python/Main/IMMC/RawData.xlsx", sheet_name="Sheet1")

idxNumberdData = rawData.rename(columns={"Alice": "0", "Bob": "1", "Charlie": "2", "David": "3",
                                         "Erin": '4'})

max = []
maxId = []
maxData = []
sortedList = pd.DataFrame({'Alice': [], 'Bob': [], 'Charlie': [], 'David': [], 'Erin': []})
avgSortedList = pd.DataFrame({'0': [], '1': [], '2': [], '3': [], '4': []})
mask = pd.DataFrame({'Alice': [], 'Bob': [], 'Charlie': [], 'David': [], 'Erin': []})
rebounce = False
iterate = [0]
# -------------------------------------------------------------------------------------- #


# def SortForLowestVariance():
for p in range(30):
    max.append(rawData.iloc[p].max())
    maxId.append(int(idxNumberdData.iloc[p].idxmax()))
    maxData.append([maxId[p], max[p]])
    sortedList.loc[p] = list(repeat(0, maxId[p])) + list(repeat(max[p], 1)) + list(repeat(0, (4 - maxId[p])))
    avgSortedList.loc[p] = list(repeat(np.NaN, maxId[p])) + list(repeat(max[p], 1)) + list(
        repeat(np.NaN, (4 - maxId[p])))
    mask.loc[p] = list(repeat(np.NaN, maxId[p])) + list(repeat(1, 1)) + list(repeat(np.NaN, (4 - maxId[p])))


print(avgSortedList.sum())
D = [avgSortedList.sum().max() - avgSortedList.sum().min()]
dNew = 0
for g in range(5):
    dNew += abs(avgSortedList.sum().sum()/5 - avgSortedList.sum().iloc[g])
dNewList = [dNew]





# Iliteration starts here
for i in range(1000):
    lowestP = int(avgSortedList.sum().idxmin())
    highestP = int(avgSortedList.sum().idxmax())


    # Sorting
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
    dNew += abs(avgSortedList.sum().sum() / 5 - avgSortedList.sum().iloc[0])
    dNew += abs(avgSortedList.sum().sum() / 5 - avgSortedList.sum().iloc[1])
    dNew += abs(avgSortedList.sum().sum() / 5 - avgSortedList.sum().iloc[2])
    dNew += abs(avgSortedList.sum().sum() / 5 - avgSortedList.sum().iloc[3])
    dNew += abs(avgSortedList.sum().sum() / 5 - avgSortedList.sum().iloc[4])  #依托答辩

    D.append(avgSortedList.sum().max() - avgSortedList.sum().min())
    iterate.append(i+1)
    dNewList.append(dNew/5)


print(sortedList)
print(avgSortedList.sum().sum())
print(dNewList[len(dNewList)-10:len(dNewList)-1])

x = iterate
y = dNewList

plt.plot(x,y)
plt.xlabel('Iteration')
plt.ylabel('Absolute Deviation')
plt.title('Absolute Deviations respond to increasing Iteration')
plt.show()







# -------------------------------------------------------------------------------------- #

# A = pd.DataFrame(rawData, columns=["Alice"])
# B = pd.DataFrame(rawData, columns=["Bob"])
# C = pd.DataFrame(rawData, columns=["Charlie"])
# D = pd.DataFrame(rawData, columns=["David"])
# E = pd.DataFrame(rawData, columns=["Erin"])
# avgList = [A, B, C, D, E]
# variance = [A, B, C, D, E]
# allDataAdded = pd.DataFrame(
#     {'Combined_Column': A['Alice'] + B['Bob'] + C['Charlie'] + D['David'] + E['Erin']})

# -------------------------------------------------------------------------------------- #

# for p in range(30):
#     max.append(rawData.iloc[p].min())
#     maxId.append(int(idxNumberdData.iloc[p].idxmin()))
#     maxData.append([maxId[p], max[p]])
#
#     sortedList.loc[p] = list(repeat(0, maxId[p])) + list(repeat(max[p], 1)) + list(repeat(0, (4 - maxId[p])))
#     avgSortedList.loc[p] = list(repeat(np.NaN, maxId[p])) + list(repeat(max[p], 1)) + list(
#         repeat(np.NaN, (4 - maxId[p])))
#     mask.loc[p] = list(repeat(np.NaN, maxId[p])) + list(repeat(1, 1)) + list(repeat(np.NaN, (4 - maxId[p])))
# print(avgSortedList)

# -------------------------------------------------------------------------------------- #


# TransferLowToHigh
# sortedList.iloc[itemTransLTH.iloc[lowestP], lowestP] = 0
# sortedList.iloc[itemTransLTH.iloc[lowestP], highestP] = rawData.iloc[
#     itemTransLTH.iloc[lowestP], highestP]
# avgSortedList.iloc[itemTransLTH.iloc[lowestP], lowestP] = np.NaN
# avgSortedList.iloc[itemTransLTH.iloc[lowestP], highestP] = rawData.iloc[
#     itemTransLTH.iloc[lowestP], highestP]


# -------------------------------------------------------------------------------------- #

# def Draw():
#     N = 50
#     x = [1, 2, 3, 4, 5]
#     y = avgList
#     area = variance
#
#     plt.scatter(x, y, s=area, alpha=0.5)
#     plt.xlabel('avg')
#     plt.ylabel('var')
#     plt.title('spread')
#     plt.show()


# -------------------------------------------------------------------------------------- #

# def getAnyVariance(dataFrame):
#     var = 0
#     for i in range(5):
#         X = 0
#         for z in range(30):
#             X = (dataFrame.iloc[:i].iloc[:z].item() - avgSortedList.mean().iloc[i]) ** 2
#         var = round(X / 30, 2)
#     return var

# -------------------------------------------------------------------------------------- #
