"""
We are given an array containing n distinct numbers taken from the range 0 to n.
Since the array has only n numbers out of the total n+1 numbers, find the missing number."""


def find_missing_number(nums):
    i = 0
    while i < len(nums):
        j = nums[i]
        if j < len(nums) and i != nums[i]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i+=1
    missing = -1
    for i, val in enumerate(nums):
        if i != val:
            missing = i
    return missing


print('2: ', find_missing_number([4, 0, 3, 1]))
print('7: ', find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))
