def searchInfinite(arr, x):
    low = 0
    high = 1

    while arr[high] < x:
        low = high
        high = high * 2

  

    return binarySearch(arr, low, high, x)


def binarySearch(arr, low, high, x):
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1