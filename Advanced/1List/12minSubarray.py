def minSubarray(arr,n):
    res=arr[0]
    minVal=arr[0]
    for i in range(1,n):
        minVal=min(arr[i],arr[i]+minVal)
        res=min(res,minVal)
    return res

arr = [8, -4, 3, -5, 4]
n = len(arr)
print(minSubarray(arr, n))