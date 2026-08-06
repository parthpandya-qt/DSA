from collections import deque
q=deque()
def levelTraversal(root):
    if root==None:
        return -1
    res=[]
    q.append(root)
    while q:
        curr=q.popleft()
        res.append(curr.data)
        if curr.left!=None:
            q.append(curr.left)
        if curr.right!=None:
            q.append(curr.right)

