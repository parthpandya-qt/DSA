# def count(arr,n,x):
#     count=0
#     for i in range(len(arr)):
#         if(arr[i]==x):
#             count+=1
#     return count

def firstOccurence(arr,n,x):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if(x>arr[mid]):
            low=mid=1
        elif(x<arr[mid]):
            high=mid-1
        else:
            if(mid==0 or arr[mid-1]!=arr[mid]):
                return mid
            else:
                high=mid-1
    return -1  
def lastOccurence(arr,n,x):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if(x>arr[mid]):
            low=mid=1
        elif(x<arr[mid]):
            high=mid-1
        else:
            if(mid==len(arr)-1 or arr[mid]!=arr[mid+1]):
                return mid
            else:
                low=mid+1
    return -1              


def count(arr,n,x):
    first=firstOccurence(arr,n,x)
    if first==-1:
        return 0
    else:
        lastOccurence(arr,n,x)-first+1                