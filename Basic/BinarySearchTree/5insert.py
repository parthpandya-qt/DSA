class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, key):
    parent = None
    curr = root

    while curr is not None:
        parent = curr

        if curr.data == key:
            return root

        if key < curr.data:
            curr = curr.left
        else:
            curr = curr.right

    # Tree is empty
    if parent is None:
        return Node(key)

    # Insert the new node
    if key < parent.data:
        parent.left = Node(key)
    else:
        parent.right = Node(key)

    return root