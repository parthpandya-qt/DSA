from collections import deque
class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

def Max(root):
    if root==None:
        return float('-inf')
    else:
        lh=Max(root.left)
        rh=Max(root.right)
        return max(root.data,lh,rh)

    

root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.right.left=Node(40)
root.right.right=Node(50)
print(Max(root))