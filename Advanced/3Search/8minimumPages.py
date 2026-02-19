def minPages(arr,k):
    Sum=sum(arr)
    Max=max(arr)
    n=len(arr)
    low,high=Max,Sum
    res=0
    while low<=high:
        mid=(high+low)//2
        if (isFeasible(arr,k,mid)):
            res=mid
            high=mid-1
        else:
            low=mid+1
    return res

def isFeasible(arr,k,ans):
    req,s=1,0
    n=len(arr)
    for i in range(n):
        if (s+arr[i])>ans:
            req+=1
            s=arr[i]
        else:
            s+=arr[i]
    return (req<=k)