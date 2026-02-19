class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def inOrder(self):
        
        if self.left:
            self.left.inOrder()
        print(self.data,end =" ")
        if self.right:
            self.right.inOrder()
                

root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.right.left=Node(40)
root.right.right=Node(50)

root.inOrder()  

root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.right.left=Node(40)
root.right.right=Node(50)

root.inOrder()