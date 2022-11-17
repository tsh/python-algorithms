"""
  A subsequence of an array is a set of numbers that aren't necessarily adjacent
  in the array but that are in the same order as they appear in the array. For
  instance, the numbers <span>[1, 3, 4]</span> form a subsequence of the array
  <span>[1, 2, 3, 4]</span>, and so do the numbers <span>[2, 4]</span>. Note
  that a single number in an array and the array itself are both valid
  subsequences of the array.

"""

def isValidSubsequence(array, sequence):
    arlen = len(array)
    slen = len(sequence)
    ai, si = 0, 0
    while ai < arlen and si < slen:
        if array[ai] == sequence[si]:
            si += 1
        ai += 1
    return si == slen
