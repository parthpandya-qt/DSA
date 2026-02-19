class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

root=Node(10)
root.left=Node(20)
root.right=Node(20)
root.left.left=Node(40)
        