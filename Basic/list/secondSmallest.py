def secondSmallest(arr):
    smallest=arr[0]
    secondSmallest=None
    n=len(arr)
    for i in range(1,n):

        if arr[i]<smallest:
            secondSmallest=smallest
            smallest=arr[i]
        elif arr[i]!=smallest:
            if arr[i]>secondSmallest or secondSmallest==None:
                secondSmallest=arr[i]
    return secondSmallest