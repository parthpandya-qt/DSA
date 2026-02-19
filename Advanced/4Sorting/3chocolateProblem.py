def minDiff(arr,m):
    if (len(arr)==0 or m ==0):
        return -1
    if len(arr)<m:
        return -1
    arr.sort()
    res=arr[m-1]-arr[0]
    for i in range(1,len(arr)-m+1):
        res=min(res,arr[i+m-1]-arr[i])
    return res