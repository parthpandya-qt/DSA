def findpath(root,path,x):
    if root==None:
        return False
    path.append(root.data)
    if root.data==x:
        return True
    if (root.left!=None and findpath(root.left,path,x)) or (root.right!=None and findpath(root.right,path,x)):
        return True 
    path.pop()
    return False

def commonAncestor(root,x,y):
    p1=[]
    p2=[]
    if not findpath(root,p1,x) or not findpath(root,p2,y):
        return -1
    i=0
    while i<len(p1) and i<len(p2):
        if p1[i] != p2[i]:
            break
        i+=1
    return p1[i-1]
        