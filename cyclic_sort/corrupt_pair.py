

"""
We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’.
The array originally contained all the numbers from 1 to ‘n’, but due to a data error,
one of the numbers got duplicated which also resulted in one number going missing. Find both these numbers.
"""


def find_corrupt_numbers(nums):
  # TODO: Write your code here
  return [-1, -1]


print('[2, 4]: ', find_corrupt_numbers([3, 1, 2, 5, 2]))
print('[3, 5]: ', find_corrupt_numbers([3, 1, 2, 3, 6, 4]))
