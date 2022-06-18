"""
Given an unsorted array containing numbers, find the smallest missing positive number in it.
Note: Positive numbers start from ‘1’.
"""


def find_first_smallest_missing_positive(nums):
    i, n = 0, len(nums)
    while i < n:
        j = nums[i] -1
        if i != j and j >= 0 and j < n:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i +=1

    for i in range(n):
        if i+1 != nums[i] :
            return i + 1


print('3: ', find_first_smallest_missing_positive([-3, 1, 5, 4, 2]))
print('4: ', find_first_smallest_missing_positive([3, -2, 0, 1, 2]))
print('4: ', find_first_smallest_missing_positive([3, 2, 5, 1]))
