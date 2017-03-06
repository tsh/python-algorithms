class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        if value <= self.value:
            if self.left:
                self.left.add(value)
            else:
                self.left = Node(value)
        else:
            if self.right:
                self.right.add(value)
            else:
                self.right = Node(value)


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root:
            self.root.add(value)
        else:
            self.root = Node(value)

    def contains(self, value):
        node = self.root
        while node:
            if value == node.value:
                return True
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        return False


if __name__ == '__main__':
    bt = BinaryTree()
    bt.add(10)
    assert bt.root.value == 10
    bt.add(7)
    assert bt.root.left.value == 7
    bt.add(12)
    assert bt.root.right.value == 12
    # contains
    assert bt.contains(10)
    assert bt.contains(7)
    assert bt.contains(12)
    assert not bt.contains(42)

