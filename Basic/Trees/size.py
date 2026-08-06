def size(root):
    if root == None:
        return 0
    else:
        ls = size(root.left)
        rs = size(root.right)
        return ls+rs+1