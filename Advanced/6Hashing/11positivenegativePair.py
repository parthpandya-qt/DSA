def positiveNegative(arr):
    n = len(arr)
    seen = set()
    res=[]
    for i in arr:
        if -i in seen:
            if i < 0:
                res.append(i)
                res.append(-i)
            else:
                res.append(-i)
                res.append(i)
        else:
            seen.add(i)
    if not res:
        return [0]
    return res