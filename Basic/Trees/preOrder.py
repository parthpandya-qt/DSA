class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def preOrder(self):
        
        print(self.data,end =" ")
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()

root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.right.left=Node(40)
root.right.right=Node(50)

root.preOrder()  

