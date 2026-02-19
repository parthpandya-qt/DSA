class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=Node(10)
root.left=Node(5)
root.left.left=Node(2)
root.right=Node(30)
root.right.left=Node(25)
root.right.right=Node(40)


def floor(root,key):
    res=None
    while root!=None:
        if root.data==key:
            return root.data
        elif root.data>key:
            root=root.left
        else:
            res=root.data
            root=root.right
    return res            