def iterative(root):
    stack = []
    curr = root
    res = []
    while curr:
        stack.push(curr)
        curr=curr.left
    while stack:
        curr = stack.pop()
        res.append(curr)
        if curr.right:
            curr = curr.right
            while curr:
                stack.push(curr)
                curr = curr.left
    return res
