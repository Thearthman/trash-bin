import pandas as pd
import IMMCMichPack as mp  # 自创迭代算法工具包

# 初始化变量
iterate = [0]
rawData = pd.read_excel(r"/Volumes/Personal/Coding/Python/Main/IMMC/RawData.xlsx", sheet_name="Sheet1")

# 以成员总获得价值最大方式分配
sortedList = mp.getMaxTotalValueArrangement(rawData,candidate=5,option=0)
avgSortedList = mp.getMaxTotalValueArrangement(rawData,candidate=5,option=1)
D = [avgSortedList.sum().max() - avgSortedList.sum().min()]
adList = [mp.getad(avgSortedList)]
sumList = [avgSortedList.sum().sum().item()]
# 迭代从此处开始
for i in range(30):
    sortedList , avgSortedList = mp.iteration(avgSortedList,avgSortedList,rawData,sortedList)

    # 记录每次迭代后的绝对差与极差
    D.append(avgSortedList.sum().max() - avgSortedList.sum().min())
    iterate.append(i + 1)
    adList.append(mp.getad(avgSortedList))
    sumList.append(avgSortedList.sum().sum().item())
# 输出数据
mp.printdata(sortedList, avgSortedList, adList)
mp.drawplot(iterate, sumList, "A vs B vs C vs D vs E Absolute Deviation against iteration")


