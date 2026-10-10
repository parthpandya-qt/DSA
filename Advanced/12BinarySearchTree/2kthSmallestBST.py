def kth(root,k):
    res = []
    
    def inorder(curr):
        nonlocal res
        if curr != None:
            inorder(curr.left)
            res.append(curr.data)
            inorder(curr.right)
    inorder(root)
    return res[k-1]






def kth(root,k):
    res = 0
    count = 0
    
    def inorder(curr):
        nonlocal res,count
        if curr != None:
            inorder(curr.left)
            count += 1
            if count == k:
                res = curr.data
                return
            inorder(curr.right)
    inorder(root)
    return res