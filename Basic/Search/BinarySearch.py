def binarySearch(l,x):
    low=0
    high=len(l)-1
    while low<=high:
        mid=high+low//2
        if(l[mid]==x):
            return mid
        elif(l[mid]<x):
            low=mid+1
        else:
            high=high -1
    return -1

l=[23,34,56,567,34,2,3,4,5,6,7,8,9,]        
x=4
print(binarySearch(l,x))

def binarySearchRecursion(arr,tar,low,high):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == tar:
            return mid
        elif arr[mid] > tar:
            return binarySearchRecursion(arr, tar, low, mid - 1)
        else:
            return binarySearchRecursion(arr, tar, mid + 1, high)
    else:
        return -1
