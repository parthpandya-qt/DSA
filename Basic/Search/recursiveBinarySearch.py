def binarySearch(l,x,low,high):
    if(low>high):
        return -1
    mid=low+high//2
    if(l[mid]==x):
        return mid
    elif(l[mid]<x):
        binarySearch(l,x,mid+1,high)
    else:
        binarySearch(l,x,low,mid-1)
            