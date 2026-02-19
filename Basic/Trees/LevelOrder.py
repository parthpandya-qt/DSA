from collections import deque
class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

def levelOrder(root):
    if root==None:
        return 
    q=deque()
    q.append(root)
    while len(q)>0:
        node=q.popleft()
        print(node.data, end=" ")
        if node.left!=None:
            q.append(node.left)
        if node.right!=None:
            q.append(node.right)
        
    

root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.right.left=Node(40)
root.right.right=Node(50)

levelOrder(root)