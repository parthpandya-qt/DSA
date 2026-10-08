def kth(root,k):
    count = 0
    curr = root
    
    def inorder(curr):
        if curr != None:
            
            inorder(curr.left)
            count += 1
            if count == k:
                print(curr.data)
            inorder(curr.right)
    inorder(curr)