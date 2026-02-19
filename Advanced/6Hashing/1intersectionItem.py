def intersect(arr1,arr2):
    s=set(arr1)
    
    res=0
    for i in arr2:
        if i in s:
            res+=1
            s.remove(i)
    return res
arr1 = [10, 20, 10, 30, 20]
arr2 = [20, 10, 10, 40]
print(intersect(arr1, arr2))  