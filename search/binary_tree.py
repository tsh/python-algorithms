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

    def contains(self, value):
        if value == self.value:
            return True
        elif value < self.value:
            if self.left:
                return self.left.contains(value)
            else:
                return False
        else:
            if self.right:
                return self.right.contains(value)
            else:
                return False

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root:
            self.root.add(value)
        else:
            self.root = Node(value)

    def contains(self, value):
        return self.root.contains(value)


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

