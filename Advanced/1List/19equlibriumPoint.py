def equilibriumPoint(arr):
    n=len(arr)
    for i in range(n):
        lsum=0
        rsum=0
        for j in range(i+1,n):
            rsum+=arr[j]
        for j in range(i):
            lsum+=arr[j]
        if lsum==rsum:
            return True
    return False