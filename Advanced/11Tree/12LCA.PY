def lca(root,n1,n2):
    if root==None:
        return None
    if root.data==n1 or root.data==n2:
        return root
    lca1=lca(root.left,n1,n2)
    lca2=lca(root.right,n1,n2)
    if lca1 and lca2:
        return root
    if lca1:
        return lca1
    else:
        return lca2