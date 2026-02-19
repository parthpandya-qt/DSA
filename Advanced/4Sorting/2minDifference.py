def minDifference(arr):
    arr.sort()
    res=float("inf")
    n=len(arr)
    for i in range(1,n):
        res=min(res,abs(arr[i]-arr[i-1]))
    return res