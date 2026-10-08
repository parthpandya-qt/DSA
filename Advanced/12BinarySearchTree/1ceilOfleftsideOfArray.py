def ceil(arr):
    res = []
    s = set()
    s.add(arr[0])
    res.append(-1)
    for i in range(1,len(arr)):
        it = []
        for j in s:
            if j>arr[i]:
                it.append(j)
        if len(it) == 0:
            res.append(-1)
        else:
            res.append(min(it))
        s.add(arr[i])
    return res



print(ceil([2,8,30,15,25,12]))

