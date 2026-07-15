def powerSet(arr):
    n = len(arr)
    res = []
    pSize = 1 << n

    for i in range(pSize):
        temp = []

        for j in range(n):
            if i & (1 << j):
                temp.append(arr[j])

        res.append(temp)

    return res


print(powerSet([1, 2, 3]))