import numpy as np
def iteration(replacementList,avgSortedList,rawData,sortedList):

    lowestP = int(replacementList.sum().idxmin())
    highestP = int(replacementList.sum().idxmax())

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
    sortedList.iloc[itemTransHTL, lowestP] = rawData.iloc[
        itemTransHTL, lowestP]
    avgSortedList.iloc[itemTransHTL, highestP] = np.NaN
    avgSortedList.iloc[itemTransHTL, lowestP] = rawData.iloc[
        itemTransHTL, lowestP]

    return sortedList,avgSortedList

