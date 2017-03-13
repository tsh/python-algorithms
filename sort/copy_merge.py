import math


def copy_merge(A):
    if len(A) < 2:
        return A
    mid = math.floor(len(A) / 2)
    left = copy_merge(A[:mid])
    right = copy_merge(A[mid:])

    result = []
    l = r = 0
    while len(result) < len(A):
        if r >= len(right) or (l < mid and left[l] < right[r]):
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    return result


if __name__ == '__main__':
    import random
    arr = [random.randint(1, 10) for _ in range(10)]
    assert copy_merge(arr) == sorted(arr)
    assert copy_merge([3, 0, 4, -1]) == [-1, 0, 3, 4]