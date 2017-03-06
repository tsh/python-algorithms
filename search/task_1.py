"""
Create a balanced binary tree from sorted collection. [2, 5, 6, 7, 8, 10, 12]
"""
import math
from binary_tree import BinaryTree


def create_tree(ordered):
    bt = BinaryTree()
    add_from_range(bt, ordered, 0, len(ordered)-1)
    return bt


def add_from_range(bt, ordered, low, high):
    if low <= high:
        mid = math.floor((low + high) / 2)
        bt.add(ordered[mid])
        add_from_range(bt, ordered, 0, mid-1)
        add_from_range(bt, ordered, mid+1, high)


if __name__ == '__main__':
    ordered = [2, 5, 6, 7, 8, 10, 12, 13, 15, 22]
    bt = create_tree(ordered)
    assert bt.root.value == 8
    assert bt.root.left.value == 5
    assert bt.root.right.value == 13
    assert bt.root.right.left.value == 10
    assert bt.contains(22)
    assert not bt.contains(42)