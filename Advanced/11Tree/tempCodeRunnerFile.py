class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


index = 0

inorder = [40, 20, 50, 10, 60, 30, 70]
preorder = [10, 20, 40, 50, 30, 60, 70]
end = len(inorder) - 1









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
