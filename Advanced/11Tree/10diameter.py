def diameter(root):
    ans=[0]
    def height(node):
        if node==None:
            return 0
        lh=height(node.left)
        rh=height(node.right)
        ans[0]=max(ans[0],lh+rh+1)
        return 1+max(rh,rh)
    height(root)
    return ans[0]