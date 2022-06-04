def circular_array_loop_exists(arr):
    for i in range(len(arr)):
        is_forward = arr[i] >= 0  # initial direction
        slow, fast = i, i
        while slow != is_forward or fast != is_forward:
          slow = next_index(arr, slow)
          fast = next_index(arr, fast)
          if fast != is_forward:
            break
          fast = next_index(arr, fast)
          if slow == fast and slow != -1:
            return True
    return False

def next_index(arr, cur_i):
    return (cur_i + arr[cur_i]) % len(arr)


def main():
    print(circular_array_loop_exists([1, 2, -1, 2, 2]), True)
    print(circular_array_loop_exists([2, 2, -1, 2]), True)
    print(circular_array_loop_exists([2, 1, -1, -2]), False)


main()
