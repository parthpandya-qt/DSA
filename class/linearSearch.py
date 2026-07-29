def linearSearch(arr,tar):
    n = len(arr)
    res = []
    for i in range(n):
        if arr[i] == tar:
            res.append(i)
    return res

print(linearSearch([10,105,56,4,8,1,87,5,105],105))