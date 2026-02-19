from collections import deque


def maxWidth(root):
    if root==None:
        return None
    q=deque()
    q.append(root)
    width=0
    
    while q:
        res=len(q)
        width=max(res,width)
        for _ in range(res):
            curr=q.popleft()
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
    return width