def inversion(arr, l, r):
    res = 0
    if l < r:
        mid = (l + r) // 2
        res += inversion(arr, l, mid)
        res += inversion(arr, mid + 1, r)
        res += countMerge(arr, l, mid, r)
    return res


def countMerge(arr, l, mid, r):
    left = arr[l:mid+1]
    right = arr[mid+1:r+1]

    i = j = 0
    k = l
    res = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:      # use <=
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            res += len(left) - i      # remaining elements in left
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return res