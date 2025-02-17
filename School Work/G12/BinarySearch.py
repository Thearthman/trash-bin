import random, math, statistics
import matplotlib.pyplot as plt


def binary_search(target: int, _arr):
    _lower_bound = 0
    _upper_bound = len(arr)
    _found = False
    count = 0

    while not _found:
        half = math.floor((_lower_bound + _upper_bound) / 2)
        _current_element = _arr[half]
        if _lower_bound + 1 == _upper_bound:
            print("not found")
            return count
        if _current_element == target:
            print("target found, at location", half + 1)
            _found = True
            return count
        elif _current_element < target:
            _lower_bound = half
        elif _current_element > target:
            _upper_bound = half
        count += 1


def linear_search(target: int, arr):
    upperBound = len(arr) - 1
    lowerBound = 0
    index = lowerBound
    found = False

    while not found and index <= upperBound:
        if target == arr[index]:
            found = True
        index += 1

    if found:
        print("found")
    else:
        print("not found")

    return index


arr = [random.randint(0, 10)]
for i in range(10):
    arr.append(arr[i] + random.randint(0, 100))

print(arr)

# target = int(input("enter the number to find"))
# print(binary_search(target,arr))
# print(linear_search(target,arr))

b_list = [0]
l_list = [0]
b_average_list = [0]
l_average_list = [0]
for magnitude in range(100,10000,1000):
    for i in range(100):
        arr = [random.randint(0, 10)]
        for i in range(magnitude):
            arr.append(arr[i] + random.randint(0, 100))
        target = arr[random.randint(0, len(arr) - 1)]
        # target = random.randint(0,500)
        b_list.append(binary_search(target, arr))
        l_list.append(linear_search(target, arr))
    b_average_list.append(statistics.mean(b_list))
    l_average_list.append(statistics.mean(l_list))

plt.plot(b_average_list, color='green', marker="o")
plt.plot(l_average_list, color='red', marker="o")
plt.ylabel("difference in data")
plt.show()
