def maxSub(arr,n):
    res=arr[0]
    for i in range(0,n):
        curr=0
        for j in range(i,n):
            curr+=arr[j]
            res=max(res,curr)
    return res
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)
print(maxSub(arr, n)) 
