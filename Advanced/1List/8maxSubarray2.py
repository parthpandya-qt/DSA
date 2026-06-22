def subArray(arr,n):
    res=arr[0]
    maxElement=arr[0]
    for i in range(1,n):
        maxElement=max(arr[i],arr[i]+maxElement)
        res=max(maxElement,res)
    return res    



