class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def insert(root,key):
    parant=None
    curr=root
    while curr!=None:
        parant=curr
        if curr.data==key:
            return root
        if curr.data<key:
            curr=curr.right
        
        else:
            curr=curr.left
    if parant==None:
        return Node(key)
    if parant.data>key:
        parant.left=Node(key)
    if parant.data<key:
        parant.right=Node(key)    
