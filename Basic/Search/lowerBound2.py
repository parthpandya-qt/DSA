def lowerBound(arr, x):
    low = 0
    high = len(arr) - 1
    ans = len(arr)

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

print(lowerBound([1,2,3,4,5,5,5,5,5,5,5,5,5,54,54,54], 54))