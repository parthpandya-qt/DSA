def smallestElement(arr):
    smallest=arr[0]
    n=len(arr)
    for i in range(n):
        if arr[i]<smallest:
            smallest=arr[i]
    return smallest

