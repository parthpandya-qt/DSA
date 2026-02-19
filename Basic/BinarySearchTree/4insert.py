class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def insert(root,key):
    if root==None:
        return Node(key)
    if root.data==key:
        return
    
    if root.data>key:
        root.left=insert(root.left,key)
    if root.data<key:
        root.right=insert(root.right,key)
    return root    
