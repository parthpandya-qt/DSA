class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def search(root,key):
    while root!=None:
        if root.data==key:
            return True
        elif root.data>key:
            root=root.left
        else:
            root=root.right
    return False            
root=Node(10)
root.left=Node(5)
root.left.left=Node(2)
root.right=Node(30)
root.right.left=Node(25)
root.right.right=Node(40)
print(search(root,25))
