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



def findSuccer(curr):
    while curr.left!=None:
        curr=curr.left
    return curr.data    
def delete(root,key):
    if root==None:
        return 
    elif root.data>key:
        root.left=delete(root.left,key)
    elif root.data<key:
        root.right=delete(root.right,key)
    else:
        if root.right==None:
            return root.left
        elif root.left==None:
            return root.right
        else:
            succ=findSuccer(root.right)
            root.data=succ
            root.right=delete(root.right,succ)
