from itertools import repeat

import numpy as np
import pandas as pd

import IMMCMichPack as mp  # 自创迭代算法工具包

# 初始化变量
iterate = [0]
rawData = pd.read_excel(r"/Volumes/Personal/Coding/Python/Main/IMMC/RawData.xlsx", sheet_name="Sheet1")

# 以成员总获得价值最大方式分配
sortedList = mp.getMaxTotalValueArrangement(rawData, candidate=5, option=0)
avgSortedList = mp.getMaxTotalValueArrangement(rawData, candidate=5, option=1)
D = [avgSortedList.sum().max() - avgSortedList.sum().min()]
adList = [mp.getad(avgSortedList)]

# 迭代从此处开始
for i in range(30):
    sortedList, avgSortedList = mp.iteration(avgSortedList, avgSortedList, rawData, sortedList)

    # 记录每次迭代后的绝对差与极差
    D.append(avgSortedList.sum().max() - avgSortedList.sum().min())
    iterate.append(i + 1)
    adList.append(mp.getad(avgSortedList))

# 输出数据
mp.printdata(sortedList, avgSortedList, adList)
avgSortedListToBePrinted = pd.DataFrame({'0': avgSortedList.sum()}).transpose()

# Starts Iterating for A B
# ------------------------------------------------------------------------------#
newSortList = pd.DataFrame({"Alice": sortedList.iloc[:, 0], "Bob": sortedList.iloc[:, 1]})
newAvgList = pd.DataFrame({"Alice": avgSortedList.iloc[:, 0], "Bob": avgSortedList.iloc[:, 1]})
newRawData = pd.DataFrame({"0": rawData.iloc[:, 0], "1": rawData.iloc[:, 1]})
newCandidateNumber = len(newRawData.columns)
newMax = []
newMaxId = []
mask = []
for j in range(30):
    mask.append(j) if sortedList.iloc[j, 0].item() != 0 or sortedList.iloc[j, 1].item() != 0 else None
print(mask)

iterationCount = 0
for j in mask:
    newMax.append(newRawData.iloc[j].max())
    newMaxId.append(int(newRawData.iloc[j].idxmax()))
    newSortList.loc[j] = list(repeat(0, newMaxId[iterationCount])) + list(repeat(newMax[iterationCount], 1)) + list(
        repeat(0, (1 - newMaxId[iterationCount])))
    newAvgList.loc[j] = list(repeat(np.NaN, newMaxId[iterationCount])) + list(repeat(newMax[iterationCount], 1)) + list(
        repeat(np.NaN, (1 - newMaxId[iterationCount])))
    iterationCount += 1

for r in range(2):
    sortedList.iloc[:, r] = newSortList.iloc[:, r]
    avgSortedList.iloc[:, r] = newSortList.iloc[:, r]

# Starts Iterating for C D E
# ------------------------------------------------------------------------------#
newSortList = pd.DataFrame({"Charlie": sortedList.iloc[:, 2], "David": sortedList.iloc[:, 3],"Erin": sortedList.iloc[:, 4]})
newAvgList = pd.DataFrame({"Charlie": avgSortedList.iloc[:, 2], "David": avgSortedList.iloc[:, 3],"Erin": avgSortedList.iloc[:, 4]})
newRawData = pd.DataFrame({"0": rawData.iloc[:, 2], "1": rawData.iloc[:, 3],'2': rawData.iloc[:,4]})
newCandidateNumber = len(newRawData.columns)
newMax = []
newMaxId = []
mask = []
for j in range(30):
    mask.append(j) if sortedList.iloc[j, 2].item() != 0 or sortedList.iloc[j, 3].item() != 0 or sortedList.iloc[j, 4].item() != 0 else None
print(mask)

iterationCount = 0
for j in mask:
    newMax.append(newRawData.iloc[j].max())
    newMaxId.append(int(newRawData.iloc[j].idxmax()))
    newSortList.loc[j] = list(repeat(0, newMaxId[iterationCount])) + list(repeat(newMax[iterationCount], 1)) + list(
        repeat(0, (2 - newMaxId[iterationCount])))
    newAvgList.loc[j] = list(repeat(np.NaN, newMaxId[iterationCount])) + list(repeat(newMax[iterationCount], 1)) + list(
        repeat(np.NaN, (2 - newMaxId[iterationCount])))
    iterationCount += 1

for r in range(3):
    sortedList.iloc[:, r+2] = newSortList.iloc[:, r]
    avgSortedList.iloc[:, r+2] = newSortList.iloc[:, r]
#------------------------------------------------------------------------------#


adDataFrame = pd.Series({"AD before in-group distribution": min(adList), "AD now": mp.getad(sortedList)})
printList = sortedList._append(avgSortedListToBePrinted._append(avgSortedList.sum().transpose(), ignore_index=True)
                               , ignore_index=True)
printList = printList._append(adDataFrame, ignore_index=True)
with pd.ExcelWriter("DataOut.xlsx", mode="a", if_sheet_exists="replace") as writer:
    printList.to_excel(writer, sheet_name="AB+CDE")

mp.printdata(sortedList, avgSortedList, adList)
