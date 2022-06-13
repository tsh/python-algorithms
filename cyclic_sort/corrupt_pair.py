"""
We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’.
The array originally contained all the numbers from 1 to ‘n’, but due to a data error,
one of the numbers got duplicated which also resulted in one number going missing. Find both these numbers.
"""


def find_corrupt_numbers(nums):
    i, n = 0, len(nums)
    while i < n:
        j = nums[i] -1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i +=1

    i = 0
    while i < len(nums):
        if nums[i] != i+1:
            return [nums[i], i+1]
        i+=1
    return [-1, -1]


print('[2, 4]: ', find_corrupt_numbers([3, 1, 2, 5, 2]))
print('[3, 5]: ', find_corrupt_numbers([3, 1, 2, 3, 6, 4]))
