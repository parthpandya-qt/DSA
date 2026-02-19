def maxKsum(arr,k):
    curr=0
    for i in range(k):
        curr+=arr[i]
    res=curr
    n=len(arr)
    for j in range(k,n):
        curr=curr-arr[j-k]+arr[j]
        res=max(res,curr)
    return res
