
prev=None
head=None
def conversion(root):
    global  prev
    global head
    if root==None:
        return 
    head= conversion(root.left)
    
    if prev==None:
        head=root
    else:
        prev.right=root
        root.left=prev
    prev=root
    conversion(root.right)
    return head
    
