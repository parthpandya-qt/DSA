def postorder(root):
    if root is None:
        return []

    stack1 = [root]
    stack2 = []
    res = []

    while stack1:
        curr = stack1.pop()
        stack2.append(curr)

        if curr.left:
            stack1.append(curr.left)

        if curr.right:
            stack1.append(curr.right)

    while stack2:
        res.append(stack2.pop())

    return res