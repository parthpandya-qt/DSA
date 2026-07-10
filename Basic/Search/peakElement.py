def peakElement(arr):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if mid>0 :
            left=arr[mid-1]
            
        else:
            left=float('-inf')
        if mid<len(arr)-1:
            right=arr[mid+1]
        else:
            right=float('-inf')

        if arr[mid]>left and arr[mid]>right:
            return arr[mid]
        elif arr[mid]<left:
            high=mid-1
        else:
            low=mid+1
    return -1








