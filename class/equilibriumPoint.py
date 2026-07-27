def equilibrium(arr):
    n=len(arr)
    total=sum(arr)
    leftSum=0
    for i in range(n):
        rightSum=total-arr[i]-leftSum
        if leftSum==rightSum:
            return i
        leftSum+=arr[i]
    return -1