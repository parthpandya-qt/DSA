def isabalanced(root):
    if root==None:
        return 0 
    lh=isabalanced(root.left)
    if lh==-1:
        return -1
    rh=isabalanced(root.right)
    if rh==-1:
        return -1
    if abs(lh-rh)>1:
        return -1
    return max(lh,rh)+1