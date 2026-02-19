class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    
    
def nodeAtkposition(root,k):
    if root==None:
        return 
    if k==0:
        print(root.data, end =" ")
    else:
        nodeAtkposition(root.left,k-1)    
        nodeAtkposition(root.right,k-1)    
root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.right.left=Node(40)
root.right.right=Node(50)

nodeAtkposition(root,2)

