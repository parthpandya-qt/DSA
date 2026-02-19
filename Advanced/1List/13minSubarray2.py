def kadan(arr,n):
    res=arr[0]
    maxElement=arr[0]
    for i in range(1,n):
        maxElement=max(arr[i],arr[i]+maxElement)
        res=max(maxElement,res)
    return res

def minSub(arr,n):
    for i in range(n):
        arr[i]=-arr[i]
    res=kadan(arr,n)
    return -res

arr = [8, -4, 3, -5, 4]
n = len(arr)
print(minSub(arr, n))