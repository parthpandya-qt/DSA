def isSum(arr,x):
    low=0
    high=len(arr)-1
    while low<high:
        if arr[low]+arr[high]==x:
            return True
        elif arr[low]+arr[high]>x:
            j-=1
        else:
            i+=1
    return False