from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + " ", end='')
            temp = temp.next
        print()

    def __repr__(self):
        return f'N: {self.value} -> {self.next}'


def reorder(head):
    # find middle
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # merge
    first_half = head
    second_half = reverse(slow)
    while first_half and second_half:
        temp = first_half.next
        first_half.next = second_half
        first_half = temp

        temp = second_half.next
        second_half.next = first_half
        second_half = temp
    if first_half is not None:
        first_half.next = None

def reverse(head):
    prev = None
    while head:
        next_ = head.next
        head.next = prev
        prev = head
        head = next_
    return prev


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    reorder(head)
    head.print_list()


main()
