def maxDifference(arr,n):
    res=arr[1]-arr[0]
    minValue=arr[0]
    for j in range(1,n):
        res=max(res,arr[j]-minValue)
        minValue=min(arr[j],minValue)
    return res    