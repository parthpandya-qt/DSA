def searchRotatedList(arr,x,low,high):
    
    
    while low<high:
        mid=(low+high)//2
        if arr[mid]==x:
            return mid
        if arr[low]<arr[mid]:
            if arr[low]<=x<arr[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if arr[mid]<x<=arr[high]:
                low=mid+1
            else:
                high=mid-1
        return -1

            

