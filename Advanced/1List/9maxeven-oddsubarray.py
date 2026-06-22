def maxevenOdd(arr,n):
    res=1
    for i in range(0,n):
        count=1
        for j in range(i+1,n):
            if (arr[j]%2==0 and arr[j-1]%2!=0) or (arr[j]%2!=0 and arr[j-1]%2==0):
                count+=1
                res=max(res,count)
            else:
                count=1
    return res


def maxevenOdd(arr, n):
    res = 1
    curr = 1

    for i in range(1, n):
        if (arr[i] % 2 == 0 and arr[i - 1] % 2 != 0) or \
           (arr[i] % 2 != 0 and arr[i - 1] % 2 == 0):
            curr += 1
            res = max(res, curr)
        else:
            curr = 1

    return res