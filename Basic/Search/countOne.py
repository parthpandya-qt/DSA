
def firstOccurence(arr,x):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if(x>arr[mid]):
            low=mid+1
        elif(x<arr[mid]):
            high=mid-1
        else:
            if(mid==0 or arr[mid-1]!=arr[mid]):
                return mid
            else:
                high=mid-1
    return -1  
def lastOccurence(arr,x):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if(x>arr[mid]):
            low=mid+1
        elif(x<arr[mid]):
            high=mid-1
        else:
            if(mid==len(arr)-1 or arr[mid]!=arr[mid+1]):
                return mid
            else:
                low=mid+1
    return -1              
def count(arr,x):
    first=firstOccurence(arr,x)
    if first==-1:
        return 0
    else:
        return lastOccurence(arr,x)-first+1                


print(count([0,0,0,0,0,1,1,1,1,1,1],1))