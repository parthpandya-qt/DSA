def maxPiece(n,a,b,c):
    if n==0:
        return 0
    if n<=0:
        return -1
    res=max(maxPiece(n-a,a,b,c),
            maxPiece(n-b,a,b,c),
            maxPiece(n-c,a,b,c))
    if res==-1:
        return -1
    return res+1