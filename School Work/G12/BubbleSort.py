import random, time

test_data = [random.randint(0, 10000) for _ in range(10000)]


def bubble_sort(data_list):
    start_time = time.time_ns()
    swap = False
    upperLimit = len(data_list)
    lowerLimit = 0
    for count in range(upperLimit):
        for index in range(lowerLimit, upperLimit - count - 1):
            swap = False
            if data_list[index] > data_list[index + 1]:
                data_list[index], data_list[index + 1] = data_list[index + 1], data_list[index]
                swap = True
        if not swap:
            break
    return data_list, time.time_ns() - start_time


print(bubble_sort(test_data)[1])

