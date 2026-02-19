index=0

end=len(inorder)-1

map={}
def conversion(inorder,preorder,start,end):
    global index
    if end<start:
        return None
    root=Node(preorder[index])
    index+=1
    if start==end:
        return root
    for i in range(start,end+1):
        if (inorder[i]==root.data):
            break
    root.left=conversion(inorder,preorder,start,i-1)
    root.right=conversion(inorder,preorder,i+1,end)
    return root