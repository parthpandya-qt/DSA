index=0

map={}
def mapcreation(inorder):
    global map
    n=len(inorder)
    for i in range(n):
        map[inorder[i]]=i
    

def conversion(inorder,preorder,start,end):
    global map
    global index
    if start>end:
        return None
    root=Node(preorder[index])
    index+=1
    if start==end:
        return root
    i=map[root.data]
    root.left=conversion(inorder,preorder,start,i-1)
    root.right=conversion(inorder,preorder,i+1,end)
    return root

    