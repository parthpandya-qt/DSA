def isZero(arr):
    n=len(arr)
    h=set()
    res=0
    for i in range(n):
        res+=arr[i]
    if res==0 or res in h:
        return True
    h.add(res)
    
