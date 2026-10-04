def countNodes(root):
    if root == None:
        return 0
    lh = 0
    rh = 0
    curr = root
    while curr:
        lh+=1
        curr = curr.left
    curr = root
    while curr:
        rh+=1
        curr = curr.right
    if lh == rh:
        return (1<<lh)-1
    return 1 + countNodes(root.left) + countNodes(root.right) 
 