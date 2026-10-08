def postorder(root):
    stack = []
    res = []
    curr = root
    while curr:
        stack.append(curr)
        curr = curr.left
    while stack:
        temp = stack.pop()
        if temp.right == None and temp.left == None:
            res.append(temp.data)
        if temp.right in res and temp.left in res:
            res.append(temp)
        if temp.right:
            curr = temp.right
            stack.append(temp)
            while curr:
                stack.append(temp.right)
        if temp.left:
            curr = temp.left
            stack.append(temp)
            while curr:
                stack.append(temp.left)


