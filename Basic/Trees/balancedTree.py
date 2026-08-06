def  balancedTree(root):
    def check(root):
        if root==None:
            return 0
        lh=check(root.left)
        if lh==-1:
            return -1
        rh=check(root.right)
        if rh==-1:
            return -1
        if abs(lh-rh)>1:
            return -1
        else:
            return max(lh,rh)+1
    result = check(root)
    if result==-1:
        return False
    else:
        return True