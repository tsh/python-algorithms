import math
import unittest

n = 50000
array = range(50000)


def bs_search(ordered, target):
    low = 0
    high = len(ordered) -1
    while low <= high:
        mid = math.floor((low + high) / 2)
        if target == ordered[mid]:
            return mid
        elif target < ordered[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == '__main__':
    assert bs_search(array, 42) == 42
    assert bs_search(array, n+1) is None
    assert bs_search(array, -1) is None