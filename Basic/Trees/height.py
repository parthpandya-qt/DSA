class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def height(self):
        
        
        if self.left:
            lh=self.left.height()
        else:
            lh=0    
        if self.right: 
            rh=self.right.height()
        else:
            rh=0
        return max(lh,rh) + 1 
    

root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.right.left=Node(40)
root.right.right=Node(50)

print(root.height())