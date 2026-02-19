class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def search(root,key):
    if root==None:
        return False
    if root.data==key:
        return True
    if root.data>key:
        return search(root.left,key)
    else:
        return search(root.right,key)

root=Node(10)
root.left=Node(5)
root.left.left=Node(2)
root.right=Node(30)
root.right.left=Node(25)
root.right.right=Node(40)

print(search(root,25))