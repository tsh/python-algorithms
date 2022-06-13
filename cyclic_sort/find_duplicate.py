


"""
We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’.
The array has only one duplicate but it can be repeated multiple times.
Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.
"""


def find_duplicate(arr):
    i = 0
    while i < len(arr) - 1:
        j = arr[i]
        if arr[i] == arr[j]:
            return arr[i]
        elif i +1 == j:
            i += 1
        arr[i], arr[j] = arr[j], arr[i]
    return -1


print('4: ', find_duplicate([1, 4, 4, 3, 2]))
print('3: ', find_duplicate([2, 1, 3, 3, 5, 4]))
print('4: ', find_duplicate([2, 4, 1, 4, 4]))