def devide3(arr):
    Sum=sum(arr)
    n=len(arr)
    if Sum%3!=0:
        return -1
    S=Sum//3
    total=0
    count=0
    for i in range(n):
        total+=arr[i]
        if total==S:
            count+=1
            total=0
    if count>=3:
        return 1

