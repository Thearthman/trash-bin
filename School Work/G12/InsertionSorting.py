import random, time

test_arr = [random.randint(0, 10000) for _ in range(10000)]


def insertion_sort(_arr):
    _current_time = time.time_ns()
    _upperbound = len(_arr)
    for _index in range(0, _upperbound):
        key = _arr[_index]
        while _arr[_index - 1] >= key and _index >= 1:
            _arr[_index] = _arr[_index - 1]
            _index -= 1
        _arr[_index] = key
    return _arr, time.time_ns() - _current_time


print(insertion_sort(test_arr)[1])
