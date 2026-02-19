def subsetSum(arr,sum,n):
    if n<0:
        if sum==0:
            return 1
        else:
            return 0
    else:
        exclude=subsetSum(arr,sum-arr[n],n-1)
        include=subsetSum(arr,sum,n-1)
    return exclude+include
