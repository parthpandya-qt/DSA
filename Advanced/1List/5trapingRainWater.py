def maxWater(arr,n):
    res=0
    for i in range(1,n-1):
        lmax=arr[i]
        for j in range(0,i):
            lmax=max(arr[j],lmax)
        rmax=arr[i]
        for j in range(i+1,n):
            rmax=max(arr[j],rmax)
        res+=min(lmax,rmax)-arr[i]
    return res
print(maxWater([3,0,1,2,5],5))