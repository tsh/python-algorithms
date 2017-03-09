def insertion_sort(A):
    for i in range(len(A)-1):
        while i >= 0 and A[i+1] < A[i]:
            A[i], A[i+1] = A[i+1], A[i]
            i -= 1
    return A

if __name__ == '__main__':
    import random
    arr = [random.randint(1, 10) for _ in range(10)]
    assert insertion_sort(arr) == sorted(arr)
    assert insertion_sort([3, 0, 4, -1]) == [-1, 0, 3, 4]