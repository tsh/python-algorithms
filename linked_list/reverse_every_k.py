from __future__ import print_function

"""
Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized sub-list starting from the head.
If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()

    def __repr__(self):
        return f'{self.value} -> {self.next}'


def reverse_every_k_elements(head, k):
    new_head = None
    while True:
        i = 0
        prev = None
        last_node = None
        while i < k:
            if head is None:
                return new_head
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
            i += 1
        if last_node:
            last_node.next = prev
        else:
            head = prev


    return new_head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_every_k_elements(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
