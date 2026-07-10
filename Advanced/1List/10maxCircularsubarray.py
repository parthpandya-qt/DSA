def maxCircular(arr, n):
    res = arr[0]

    for i in range(n):
        curr_sum = arr[i]
        curr_max = arr[i]

        for j in range(1, n):
            index = (i + j) % n
            curr_sum += arr[index]
            curr_max = max(curr_max, curr_sum)

        res = max(res, curr_max)

    return res