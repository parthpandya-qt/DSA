from collections import deque

def maxWidth(root):
    if root == None:
        return 0
    q = deque()
    q.append(root)
    width = 0
    while q:
        res = len(q)
        width = max(width,res)
        for _ in range(res):
            temp = q.popleft()
            if temp.left!=None:
                q.append(temp.left)
            if temp.right!=None:
                q.append(temp.right)
    return width