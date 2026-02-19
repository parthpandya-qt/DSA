def kadans(arr,n):
    res=arr[0]
    maxSum=arr[0]
    for i in range(1,n):
        maxSum=max(arr[i],arr[i]+maxSum)
        res=max(res,maxSum)
    return res
def maxcirularsubArray(arr,n):
    maxSubarray=kadans(arr,n)
    Total=0
    if maxSubarray<0:
        return maxSubarray
    for i in range(0,n):
        Total+=arr[i]
        arr[i]=-arr[i]
    return max(maxSubarray,Total+kadans(arr,n))


arr = [8, -4, 3, -5, 4]
n = 5
print(maxcirularsubArray(arr,n))