import numpy as np
def iteration(replacementList, avgSortedList,rawData,sortedList):

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


# import numpy as np
# import pandas as pd
#
#
# def find_index_for_transfer(replacement_sum):
#     """根据需求差找到需求最高和最低的索引。"""
#     lowest_idx = int(replacement_sum.idxmin())
#     highest_idx = int(replacement_sum.idxmax())
#     return lowest_idx, highest_idx
#
#
# def calculate_transfer_costs(data_frame, idx_from, idx_to):
#     """计算从需求高到需求低的成本。"""
#     return data_frame.iloc[:, idx_from].dropna() + data_frame.iloc[:, idx_to].dropna()
#
#
# def perform_transfer(sorted_list, avg_sorted_list, item_index, idx_high, idx_low, raw_data):
#     """执行高需求到低需求的转移。"""
#     sorted_list.iloc[item_index, idx_high] = 0
#     sorted_list.iloc[item_index, idx_low] = raw_data.iloc[item_index, idx_low]
#     avg_sorted_list.iloc[item_index, idx_high] = np.NaN
#     avg_sorted_list.iloc[item_index, idx_low] = raw_data.iloc[item_index, idx_low]
#     return sorted_list, avg_sorted_list
#
#
# def iteration(replacement_list, avg_sort_list, raw_data, sorted_list):
#     try:
#         replacement_sum = replacement_list.sum()
#         lowest_p, highest_p = find_index_for_transfer(replacement_sum)
#
#         trans_costs = calculate_transfer_costs(raw_data, highest_p, lowest_p)
#         range_diff = int(replacement_sum.max() - replacement_sum.min())
#
#         # 查找与需求差最接近的项目索引
#         closest_item_idx = trans_costs.sub(range_diff).abs().argsort()[:1].index
#
#         # 进行资源转移
#         sorted_list, avg_sort_list = perform_transfer(
#             sorted_list, avg_sort_list, closest_item_idx, highest_p, lowest_p, raw_data
#         )
#         return sorted_list, avg_sort_list
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return None, None
#
