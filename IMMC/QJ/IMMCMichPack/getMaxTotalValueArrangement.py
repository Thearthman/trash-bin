from itertools import repeat
import pandas as pd
import numpy as np
def getMaxTotalValueArrangement(rawData,candidate=4,option=0):
    max = []
    maxId = []
    avgSortedList = pd.DataFrame({'0': [], '1': [], '2': [], '3': [], '4': []})
    sortedList = pd.DataFrame({'Alice': [], 'Bob': [], 'Charlie': [], 'David': [], 'Erin': []})

    for p in range(30):
        max.append(rawData.iloc[p].max())
        maxId.append(int(rawData.iloc[p,:].idxmax()))
        sortedList.loc[p] = list(repeat(0, maxId[p])) + list(repeat(max[p], 1)) + list(repeat(0, (candidate -1  - maxId[p])))
        avgSortedList.loc[p] = list(repeat(np.NaN, maxId[p])) + list(repeat(max[p], 1)) + list(
            repeat(np.NaN, (candidate-1  - maxId[p])))

    if option == 0:
        return sortedList
    elif option == 1:
        return avgSortedList
    else:
        return None
