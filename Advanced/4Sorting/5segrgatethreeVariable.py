def segregateThree(arr):
    l,mid,hi=0,0,(len(arr)-1)
    while mid<=hi:
        if arr[mid]==0:
            arr[mid],arr[l]=arr[l],arr[mid]
            l+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[hi]=arr[hi],arr[mid]
            hi-=1

    return arr
print(segregateThree([1,1,1,0,0,2,1,2,0]))
