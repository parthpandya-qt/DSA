def lowerBound(arr,x):
    low=0
    high=len(arr)-1
    res=-1
    while(low<=high):
        mid=(low+high)//2
       
        if(arr[mid]<=x):
            res=mid
            low=mid+1 
        else:
            high=mid-1
    return res        
print(lowerBound([1,2,3,4,5,5,5,5,5,5,5,5,5,54,54,54],53))
