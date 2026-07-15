def isSum(arr, x):
    low = 0
    high = len(arr) - 1

    while low < high:
        curr_sum = arr[low] + arr[high]

        if curr_sum == x:
            return True
        elif curr_sum > x:
            high -= 1
        else:
            low += 1

    return False